import json
import urllib 
import numpy as np
import torch
from ..signal import StaticGraphTemporalSignal


class CustomDatasetLoader(object):
    """Description of the Dataset.
    """

    def __init__(self):
        self._read_web_data()

    def _read_web_data(self):
        url = "https://raw.githubusercontent.com/imsouza/pytorch-geometric-temporal-dcrnn/master/lr-data.json"  # DEFINE JSON URL HERE, TIPS: UPLOAD JSON TO GITHUB (can be on this project, path:dataset) AND COPY RAW URL+
        self._dataset = json.loads(urllib.request.urlopen(url).read())

    def _get_edges(self):
        self._edges = np.array(self._dataset["edges"]).T

    def _get_edge_weights(self):
        self._edge_weights = np.array(self._dataset["edge_weights"])

    def _get_targets_and_features(self):
        stacked_target = np.array(self._dataset["database"])
        self.features = [
            stacked_target[i : i + self.lags, :].T
            for i in range(stacked_target.shape[0] - self.lags)
        ]
        self.targets = [
            stacked_target[i + self.lags, :].T
            for i in range(stacked_target.shape[0] - self.lags)
        ]

    def get_dataset(self, lags: int = 4) -> StaticGraphTemporalSignal:
        """Returning the Custom data iterator.

        Args types:
            * **lags** *(int)* - The number of time lags.
        Return types:
            * **dataset** *(StaticGraphTemporalSignal)* - The Custom dataset.
        """
        self.lags = lags
        self._get_edges()
        self._get_edge_weights()
        self._get_targets_and_features()
        dataset = StaticGraphTemporalSignal(
            self._edges, self._edge_weights, self.features, self.targets
        )
        return dataset
