[pypi-image]: https://badge.fury.io/py/torch-geometric-temporal.svg
[pypi-url]: https://pypi.python.org/pypi/torch-geometric-temporal
[size-image]: https://img.shields.io/github/repo-size/benedekrozemberczki/pytorch_geometric_temporal.svg
[size-url]: https://github.com/benedekrozemberczki/pytorch_geometric_temporal/archive/master.zip
[build-image]: https://github.com/benedekrozemberczki/pytorch_geometric_temporal/workflows/CI/badge.svg
[build-url]: https://github.com/benedekrozemberczki/pytorch_geometric_temporal/actions?query=workflow%3ACI
[docs-image]: https://readthedocs.org/projects/pytorch-geometric-temporal/badge/?version=latest
[docs-url]: https://pytorch-geometric-temporal.readthedocs.io/en/latest/?badge=latest
[coverage-image]: https://codecov.io/gh/benedekrozemberczki/pytorch_geometric_temporal/branch/master/graph/badge.svg
[coverage-url]: https://codecov.io/github/benedekrozemberczki/pytorch_geometric_temporal?branch=master



<p align="center">
  <img width="90%" src="https://raw.githubusercontent.com/benedekrozemberczki/pytorch_geometric_temporal/master/docs/source/_static/img/text_logo.jpg?sanitize=true" />
</p>

-----------------------------------------------------

[![PyPI Version][pypi-image]][pypi-url]
[![Docs Status][docs-image]][docs-url]
[![Code Coverage][coverage-image]][coverage-url]
[![Build Status][build-image]][build-url]
[![Arxiv](https://img.shields.io/badge/ArXiv-2104.07788-orange.svg)](https://arxiv.org/abs/2104.07788)
[![benedekrozemberczki](https://img.shields.io/twitter/follow/benrozemberczki?style=social&logo=twitter)](https://twitter.com/intent/follow?screen_name=benrozemberczki)

**[Documentation](https://pytorch-geometric-temporal.readthedocs.io)** | **[External Resources](https://pytorch-geometric-temporal.readthedocs.io/en/latest/notes/resources.html)** | **[Datasets](https://pytorch-geometric-temporal.readthedocs.io/en/latest/notes/introduction.html#discrete-time-datasets)**

*PyTorch Geometric Temporal* is a temporal (dynamic) extension library for [PyTorch Geometric](https://github.com/rusty1s/pytorch_geometric).

--------------------------------------------------------------------------------

**Installation**

First install [pytorch][pytorch-install] and [pytorch-geometric][pyg-install]
and then run

```sh
pip install torch-geometric-temporal
```

[pytorch-install]: https://pytorch.org/get-started/locally/
[pyg-install]: https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html

--------------------------------------------------------------------------------

**Before Executing run**

```sh
python setup.py build
```
and
```sh
python setup.py install
```

--------------------------------------------------------------------------------

**Adaptation to make**

1. Edit '/torch_geometric_temporal/dataset/custom.py' to your desired database name

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

5. Check 'examples\recurrent\dcrnn_example.py' for possible changes and this is the code you need to run for tests and results.

6. After all edits and changes *DO THE PREVIOUS SECTION* "Before Executing run"

7. Run 'examples\recurrent\dcrnn_example.py'