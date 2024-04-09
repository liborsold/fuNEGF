# fuNEGF
Non-Equillibrium Green's Functions solvers and examples for educational purposes. Limited to a 1D linear chain for now.
See the [online documentation](https://funegf.readthedocs.io/en/latest/).

## Structure
* the ```LinearChain``` class including the NEGF routines resides in ```models.py```
* a Jupyter notebook ```one-dimensional_channel.ipynb``` in the ```examples``` folder contains the linear chain case study with the underlying physics explained
* a Jupyter notebok ```time_complexity.ipynb``` in the ```examples``` folder contains a time complexity study of constructing the model $\mathcal{O}(N)$ and calculating the transmission coefficient $\mathcal{O}(N^2)$

## Example
A linear chain with a single or multiple on-site potential impurities will present a chemical potential (occupation) drop, which may not be apparent unless a phase relaxation is included, as shown below.
An additional momentum relaxation will cause a non-zero chemical potential slope in between the impurity regions.
The complete description and calculation are provided in the ```one-dimensional_channel.ipynb``` notebook.

![example](./example.png)

## Features
* object-oriented
* with automatically generated [online documentation](https://funegf.readthedocs.io/en/latest/)
* PEP8-compliant
* including unit tests
