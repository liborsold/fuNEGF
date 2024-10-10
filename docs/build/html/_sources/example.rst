Example
=======================

An example of use is given in ``./examples/one-dimensional_channel.ipynb``. 

There is also a time-complexity study in ``./examples/time_complexity.ipynb``.

1. Construct a linear-chain tight-binding Hamiltonian
--------------------------------------------------------

.. code-block:: python

   from fuNEGF.models import LinearChain

   chain = LinearChain(N=100, eps_0=0.0, t=1.0, a=1.0, H_impurity=None, plot_dispersion=True)

.. image::
   ./_images/linear_chain_dispersion_analytic_vs_diagonalized.png
   :width: 550px
   :align: center

2. Impurity - *quantum resistors in series*
--------------------------------------------------------
.. code-block:: python

   H_impurity = np.zeros((N, N), dtype=complex)

   # (1) add a single impurity in the middle
   H_impurity[N // 2, N // 2] += -2 * t

   chain.add_H_impurity(H_impurity, plot_dispersion=False)
   chain.plot_onsite_energy()

.. image::
   ./_images/impurity_single_middle.png
   :width: 450px
   :align: center


3. Transmission function
--------------------------------------------------------

.. math::
   \bar{T}(E)=\operatorname{Trace}\left[\boldsymbol{\Gamma}_1 \mathbf{G}^R \boldsymbol{\Gamma}_2 \mathbf{G}^A\right]

Cases:
   1. without impurities it is constant :math:`T(E) = 1.0` 
   2. with a single impurity of :math:`U=-2 t`, it reaches maximum of :math:`T(E) = 0.5`
   3. with two impurities of :math:`U=-t` each, the function looks almost the same, but with strong oscillations

.. code-block:: python

    chain.plot_transmission()

.. image::
   ./_images/transmission_single_imp_middle.png
   :width: 250px
   :align: center
