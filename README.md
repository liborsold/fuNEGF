# fuNEGF
Non Equillibrium Green's Functions solvers and examples for educational purposes.

## Features
* object-oriented
* thoroughly documented
* PEP8-compliant
* with unit tests

## Structure
* the ```LinearChain``` class including the NEGF routines resides in ```models.py```
* a Jupyter notebook ```one-dimensional_channel.ipynb``` in the ```examples``` folder contains the linear chain case study with the underlying physics explained
* a Jupyter notebok ```time_complexity.ipynb``` in the ```examples``` folder contains a time complexity study of constructing the model $\mathcal{O}(N)$ and calculating the transmission coefficient $\mathcal{O}(N^2)$