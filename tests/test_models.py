# import the LinearChain class from the models module within the fuNEGF package in the parallel directory
# print the directories in path

from fuNEGF.models import LinearChain
from random import random
import numpy as np


def test_linear_chain_1_atom():
    # Test the creation of a single atom chain
    N = 1
    eps_0, t, a = random(), random(), random()
    single_atom = LinearChain(N=N, eps_0=eps_0, t=t, a=a, plot_dispersion=False)
    assert np.all(
        single_atom.H == np.array([[eps_0]])
    ), "Single atom Hamiltonian should be a 1x1 matrix [[eps_0]] !"


def test_linear_chain_2_atoms():
    # Test the creation of a 2 atom chain
    N = 2
    eps_0, t, a = random(), random(), random()
    single_atom = LinearChain(N=N, eps_0=eps_0, t=t, a=a, plot_dispersion=False)
    assert np.all(
        single_atom.H == np.array([[eps_0, t], [t, eps_0]])
    ), "Two atom Hamiltonian should be a 2x2 matrix [[eps_0, t], [t, eps_0]] !"
