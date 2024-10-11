.. fuNEGF documentation master file, created by
   sphinx-quickstart on Tue Apr  9 17:51:34 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==================================
Welcome to fuNEGF's documentation!
==================================

The `fuNEGF project on GitHub <https://github.com/liborsold/fuNEGF/>`_ is a Python package for the calculation of the electronic transport properties of nanostructures using the Non-Equilibrium Green's Function (NEGF) formalism for educational purposes. Limited to a 1D linear chain for now.

Quickstart
================

.. code-block:: python
   
   pip install fuNEGF

and

.. code-block:: python
   
   git clone https://github.com/liborsold/fuNEGF.git
   
to execute the ``./examples/one-dimensional_channel.ipynb`` Jupyter notebook and see an example of calculating the NEGF transmission and chemical potential in the presence of impurities.


.. fuNEGF example image
.. image::
   ./_images/multiple_imp_wire.png
   :width: 310px
   :align: right

.. fuNEGF example image
.. image::
   ./_images/example_fuNEGF.png
   :width: 650px
   :align: center

The impurities acts as quantum resistors, causing a drop in the chemical potential (occupation number). Without *phase relaxation* mechanisms, this might be difficult to see. Additionally, *momentum relaxation* mechanisms spread the chemical potential decrease into the clean wire region. 

Strong localized impurities reduce the transmission function from its clean limit :math:`T(E) = 1.0 = \mathrm{const.}` to half of this value. With weak, randomly distributed impurities, the transmission starts to resemble the clean limit again.

Navigation
==========

.. toctree::
   :maxdepth: 3

   theory
   example
   modules
   classes

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
