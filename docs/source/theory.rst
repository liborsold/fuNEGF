Theory
======================

Here, we summarize the physics used by the ``fuNEGF`` package in a nutshell. For a full account please refer to `Supriyo Datta - Lessons from Nanoelectronics — Part B: Quantum
Transport (2018) <https://www.worldscientific.com/worldscibooks/10.1142/10440-vol2#t=aboutBook>`_.

Non-Equilibrium Green's functions (NEGF)
----------------------------

The *retarded Green's function*

.. math::
    \mathbf{G}^{\mathrm{R}}=[E \mathbf{I}-\mathbf{H}-\mathbf{\Sigma}]^{-1}

is a function of energy :math:`E` multiplied by the identity matrix :math:`\mathbf{I}`. The Hamiltonian :math:`\mathbf{H}` and self-energy :math:`\mathbf{\Sigma}` matrices are to be defined by the physical model.

Along with the *advanced Green's function*

.. math::
    \mathbf{G}^{\mathrm{A}} = \left[ \mathbf{G}^{\mathrm{R}} \right]^\dagger


they provide the *spectral function*

.. math::
    \mathbf{A}=i\left[\mathbf{G}^{\mathrm{R}}-\mathbf{G}^{\mathrm{A}}\right]


and are used to solve for the *"electron occupation" Green's function*

.. math::
    \mathbf{G}^{\mathrm{n}}=\mathbf{G}^{\mathrm{R}} \mathbf{\Sigma}^{\mathrm{in}} \mathbf{G}^{\mathrm{A}}


which gives the *density matrix* 

.. math::
    \hat{\rho} = \mathbf{G}^{\mathrm{n}} / 2\pi .


The in-scattering term :math:`\mathbf{\Sigma}^{\mathrm{in}}` is also defined by the physical model.


Both, the self-energy :math:`\mathbf{\Sigma}` and the in-scattering term :math:`\mathbf{\Sigma}^{\mathrm{in}}` are sums of the left contact :math:`\mathbf{\Sigma}_1`, right contact :math:`\mathbf{\Sigma}_2` and an intrinsic term :math:`\mathbf{\Sigma}_0`, hence

.. math::
    \begin{align}
        \mathbf{\Sigma} &= \mathbf{\Sigma}_1 + \mathbf{\Sigma}_2 + \mathbf{\Sigma}_0 , \\
        \mathbf{\Sigma}^{\mathrm{in}} &= \mathbf{\Sigma}^{\mathrm{in}}_1 + \mathbf{\Sigma}^{\mathrm{in}}_2 + \mathbf{\Sigma}^{\mathrm{in}}_0 .
   \end{align}        


NOTE: We use the (physically expressive) notation of S. Datta, where the self-energies and Green's functions in relation to the standard notation (on the right) are defined as  

.. math::
    \begin{align}
        \mathbf{\Sigma} &\equiv \mathbf{\Sigma}^\mathrm{R} , \\
        \mathbf{G}^\mathrm{n} &\equiv -i \mathbf{G}^< , \\
        \mathbf{\Sigma}^\mathrm{in} &\equiv -i \mathbf{\Sigma}^< .
    \end{align}


Linear Chain Model
----------------------------

For the ``LinearChain`` model, the **Hamiltonian**

.. math::
    H_{ij} = \begin{cases}
                \epsilon_0, & \text { if } i=j \\ 
                t, & \text{ if } i \neq j 
            \end{cases}


Impurity potential :math:`U` can be added to the on-site energy as 

.. math::
    \mathbf{H}=\left[
        \begin{array}{ccccc}
    \ddots & \vdots & \vdots & \vdots & \ddots \\
    \cdots & \varepsilon & t & 0 & \cdots \\
    \cdots & t & \varepsilon+U & t & \cdots \\
    \cdots & 0 & t & \varepsilon & \cdots \\
    \ddots & \vdots & \vdots & \vdots & \ddots
    \end{array}
    \right] .

The **self-energies**

.. math::
    \mathbf{\Sigma}_1=\left[\begin{array}{ccccc}
    \mathrm{te}^{i k a} & 0 & 0 & \cdots & 0 \\
    0 & 0 & 0 & \cdots & 0 \\
    0 & 0 & 0 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & 0 & \cdots & 0
    \end{array}\right], \quad \mathbf{\Sigma}_2=\left[\begin{array}{ccccc}
    0 & \cdots & 0 & 0 & 0 \\
    \vdots & \ddots & \vdots & \vdots & \vdots \\
    0 & \cdots & 0 & 0 & 0 \\
    0 & \cdots & 0 & 0 & 0 \\
    0 & \cdots & 0 & 0 & \mathrm{te}^{i k a}
    \end{array}\right] ,


with the broadening functions :math:`\mathbf{\Gamma} \equiv i\left[ \mathbf{\Sigma} - \mathbf{\Sigma}^\dagger\right]`

.. math::
    \mathbf{\Gamma}_1=\frac{\hbar v}{a}\left[\begin{array}{ccccc}
    1 & 0 & 0 & \cdots & 0 \\
    0 & 0 & 0 & \cdots & 0 \\
    0 & 0 & 0 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & 0 & \cdots & 0
    \end{array}\right], \quad \mathbf{\Gamma}_2=\frac{\hbar v}{a}\left[\begin{array}{ccccc}
    0 & \cdots & 0 & 0 & 0 \\
    \vdots & \ddots & \vdots & \vdots & \vdots \\
    0 & \cdots & 0 & 0 & 0 \\
    0 & \cdots & 0 & 0 & 0 \\
    0 & \cdots & 0 & 0 & 1
    \end{array}\right] ,


where :math:`v=\mathrm{d} E /(\hbar \mathrm{d} k) = -2 a t / \hbar \sin (k a)` so that :math:`\frac{\hbar v}{a} = -2 t / \sin (k a)`.

The in-scattering terms

.. math::
    \mathbf{\Sigma}^\mathrm{in}_i = \mathbf{\Gamma}_i \cdot f_i(E) ,

where :math:`f_i(E)` is the Fermi-Dirac distribution function for contact :math:`i \in \set{1, 2}`.

The self-energies describing the **phase and phase-momentum relaxation** are defined in terms of the Green's functions themselves. Their strength is defined via the (scalar) coefficients :math:`D_0^\text{phase}` and :math:`D_0^\text{phase-momentum}`, creating a "mask" matrix

.. math::
            \mathbf{D} = D_0^\text{phase} 
            \left[\begin{array}{ccccc}
    1 & 1 & 1 & \cdots & 1 \\
    1 & 1 & 1 & \cdots & 1 \\
    1 & 1 & 1 & \cdots & 1 \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    1 & 1 & 1 & \cdots & 1
    \end{array}\right]
            + D_0^\text{phase-momentum}
            \left[\begin{array}{ccccc}
    1 & 0 & 0 & \cdots & 0 \\
    0 & 1 & 0 & \cdots & 0 \\
    0 & 0 & 1 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & 0 & \cdots & 1
    \end{array}\right] ,


which is used for an element-wise multiplication :math:`\odot` of the Green's function matrices

.. math::
    \begin{align}
            \mathbf{\Sigma}_0 &= \mathbf{D} \odot \mathbf{G}^\text{R}, \\
            \mathbf{\Sigma}^\text{in}_0 &= \mathbf{D} \odot \mathbf{G}^\text{n} .
    \end{align}


Since the Green's functions enter the definition of the self-energy, a self-consistent loop is performed, where :math:`\mathbf{G}^\text{R}` and :math:`\mathbf{G}^\text{n}` are initially set as zero matrices and iteratively updated, along with :math:`\mathbf{\Sigma}_0` and :math:`\mathbf{\Sigma}^\text{in}_0`. About 70 iteration steps are usually enough to reach a convergence.