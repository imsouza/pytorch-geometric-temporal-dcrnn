
# **Installation**

First install [pytorch][pytorch-install] and [pytorch-geometric][pyg-install]
and then run

```sh
pip install torch-geometric-temporal
```

[pytorch-install]: https://pytorch.org/get-started/locally/
[pyg-install]: https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html


# **Adaptation to make**

1. Edit *'/torch_geometric_temporal/dataset/custom.py'* to your desired database name

2. Create and upload a json for the dataset, needs to contain a few values that can be modified but here is a preview:

```json
{"edges": [[0, 0], [1, 1], [1, 0], [0, 1]], 
"edge_weights": [1.0, 1.0, 1.0, 1.0],
"node_ids": {"node0_name": 0, "node1_name": 1}, 
"datababase": [[]]
}
```

3. After created and uploaded the json database, edit this funcion on custom.py
```python
def _read_web_data(self):
    url = ""  # DEFINE JSON URL HERE, TIPS: UPLOAD JSON TO GITHUB (can be on this project, path:dataset) AND COPY RAW URL+
    self._dataset = json.loads(urllib.request.urlopen(url).read())
``` 

4. If you edited the name of the file custom.py and Class, change on *'torch_geometric_temporal\dataset\__init__.py'*:

```python
#...
from .custom import CustomDatasetLoader  # if you edit the custom.py file, you need to restart the kernel and update name here
#...
```

5. Check I for possible changes and this is the code you need to run for tests and results.

6. After all edits and changes **DO THE NEXT SECTION** "Before Executing run"

7. Run *'examples\recurrent\dcrnn_example.py'*

--------------------------------------------------------------------------------

# **Before Executing run on root folder**

```sh
python setup.py build
```
and
```sh
python setup.py install
```

--------------------------------------------------------------------------------