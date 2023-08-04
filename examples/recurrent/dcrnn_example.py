try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable):
        return iterable

import torch
import torch.nn.functional as F
from torch_geometric_temporal.nn.recurrent import DCRNN

#from torch_geometric_temporal.dataset import CustomDatasetLoader
from torch_geometric_temporal.dataset import CustomDatasetLoader
from torch_geometric_temporal.signal import temporal_signal_split

loader = CustomDatasetLoader()

dataset = loader.get_dataset()

train_dataset, test_dataset = temporal_signal_split(dataset, train_ratio=0.2)

class RecurrentGCN(torch.nn.Module):
    def __init__(self, node_features):
        super(RecurrentGCN, self).__init__()
        self.recurrent = DCRNN(node_features, 32, 1)
        self.linear = torch.nn.Linear(32, 1)

    def forward(self, x, edge_index, edge_weight):
        h = self.recurrent(x, edge_index, edge_weight)
        h = F.relu(h)
        h = self.linear(h)
        return h
        
model = RecurrentGCN(node_features = 3)     # PROBABBLY NEED TO CHANGE THIS AS TO THE NUMBER OF NODES IN THE GRAPH

optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

model.train()

for epoch in tqdm(range(200)):
    cost = 0
    for time, snapshot in enumerate(train_dataset):
        y_hat = model(snapshot.x, snapshot.edge_index, snapshot.edge_attr)
        cost = cost + torch.mean((y_hat-snapshot.y)**2)
    cost = cost / (time+1)
    cost.backward()
    optimizer.step()
    optimizer.zero_grad()
    
model.eval()
cost = 0
results = {} # dictionary to store the results

for time, snapshot in enumerate(test_dataset):
    y_hat = model(snapshot.x, snapshot.edge_index, snapshot.edge_attr)
    cost = cost + torch.mean((y_hat-snapshot.y)**2)
    y_res = y_hat.detach().numpy()
    y_tru_res = snapshot.y.detach().numpy()
    results.update({time: {"y": y_tru_res.tolist(), "y_hat": y_res.tolist()}}) # update the dictionary with the results
    if(time == 0):
        print("y_hat: ", y_hat.detach().numpy())
        print("y: " , snapshot.y.detach().numpy())

cost = cost / (time+1)
cost = cost.item()
print("MSE: {:.4f}".format(cost))
results.update({"mse": cost}) # update the dictionary with the mse

import json
path = r"" # path to the folder where you want to save the results
with open(f'{path}{10}_results_test.json', 'w') as fp:
    json.dump(results, fp)
