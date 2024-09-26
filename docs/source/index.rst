.. fuNEGF documentation master file, created by
   sphinx-quickstart on Tue Apr  9 17:51:34 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==================================
Welcome to fuNEGF's documentation!
==================================

The `fuNEGF project <https://github.com/liborsold/fuNEGF/>`_ is a Python package for the calculation of the electronic transport properties of nanostructures using the Non-Equilibrium Green's Function (NEGF) formalism for educational purposes. Limited to a 1D linear chain for now.

.. fuNEGF example image
.. image::
   ./_images/example_fuNEGF.png
   :width: 650px
   :align: center


Quickstart
================

.. code-block:: python
   
   pip install fuNEGF

then 

.. code-block:: python
   
   git clone https://github.com/liborsold/fuNEGF.git
   
and execute the ``./examples/one-dimensional_channel.ipynb`` Jupyter notebook to see an example of calculating the NEGF transmission and chemical potential in the presence of impurities.


Navigation
==========

.. toctree::
   :maxdepth: 3

   theory
   modules
   classes

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
