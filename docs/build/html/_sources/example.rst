=======================
Example
=======================

An example of use is given in ``./examples/one-dimensional_channel.ipynb``. 

There is also a time-complexity study in ``./examples/time_complexity.ipynb``.

1. Linear-chain tight-binding Hamiltonian
==============================================================

.. code-block:: python

   from fuNEGF.models import LinearChain
   import numpy as np

   chain = LinearChain(N=100, eps_0=0.0, t=1.0, a=1.0, H_impurity=None, plot_dispersion=True)

.. image::
   ./_images/linear_chain_dispersion_analytic_vs_diagonalized.png
   :width: 550px
   :align: center

2. Impurity potential
==============================================================

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


3. Chemical potential with impurities
==============================================================

There is a **potential drop** at the impurities - the impurities act as *quantum resistors in series*. 
This can be demonstrated by calculating the occupation function profile. 


3.1. No relaxation
---------------------------------------------------

Without any relaxation mechanism, strong resonances arise, making the potential drop unclear.

.. code-block:: python
   # no relaxation
   D0_phase = 0.00 * t**2
   D0_phase_momentum = 0.00 * t**2

   plot_onsite_and_occupation(E_to_plot, D0_phase, D0_phase_momentum, N_sc)

.. image::
   ./_images/single_imp_middle_no_relaxation.png
   :width: 350px
   :align: center

3.2. Phase relaxation
---------------------------------------------------

Phase relaxation attenuates the Fabry-Pérot resonances.

.. code-block:: python
   # only phase
   D0_phase = 0.09 * t**2
   D0_phase_momentum = 0.00 * t**2

   plot_onsite_and_occupation(E_to_plot, D0_phase, D0_phase_momentum, N_sc)

.. image::
   ./_images/single_imp_middle_phase_relaxation.png
   :width: 350px
   :align: center


3.3. Phase and momentum relaxation
---------------------------------------------------

With an additional momentum relaxation, the potential drop is partially distributed over the whole channel length.

.. code-block:: python
   # phase and momentum
   D0_phase = 0.09 * t**2
   D0_phase_momentum = 0.03 * t**2

   plot_onsite_and_occupation(E_to_plot, D0_phase, D0_phase_momentum, N_sc)

.. image::
   ./_images/single_imp_middle_phase_and_momentum_relaxation.png
   :width: 350px
   :align: center


4. Transmission function
==============================================================

The transmission function reads

.. math::
   \bar{T}(E)=\operatorname{Trace}\left[\boldsymbol{\Gamma}_1 \mathbf{G}^R \boldsymbol{\Gamma}_2 \mathbf{G}^A\right].


4.1. Single impurity
--------------------------------------

A single impurity in the center

.. code-block:: python

   H_impurity = np.zeros((N, N), dtype=complex)
   H_impurity[N // 2, N // 2] += -2 * t
   chain.add_H_impurity(H_impurity, plot_dispersion=False)

   chain.plot_transmission()


reduces the transmission from the clean limit :math:`T(E) = 1.0` to (at most) half of that value :math:`T(E=0.0) = 0.5`:

.. image::
   ./_images/transmission_single_imp_middle.png
   :width: 250px
   :align: center


4.2. Different impurity distributions
--------------------------------------

Let us now compare the transmission for several cases.
   1. Without impurities, the transmission function is constant :math:`T(E) = 1.0 = \mathrm{const.}`.
   2. With a single impurity of :math:`U=-2.0 t`, the transmission reaches at most the half of the clean-limit maximum :math:`T(E=0.0) = 0.5`.
   3. With two impurities of :math:`U=-t` each, the function looks almost the same but with strong resonances.
   4. With many distributed impurities of equivalent total strength :math:`\Sigma_i U_i = -2.0 t`, the transmission starts to resemble the clean limit :math:`T(E) = 1.0 = \mathrm{const.}`


.. image::
   ./_images/example_fuNEGF.png
   :width: 950px
   :align: center
