Non-Equillibrium Green's Functions solvers and examples for educational purposes. Limited to a 1D linear chain for now.
See the [documentation](https://liborsold.github.io/fuNEGF/).

Install with **```pip install fuNEGF```** from the [project's PyPI repository](https://pypi.org/project/fuNEGF/).

## Structure
* the ```LinearChain``` class including the NEGF routines resides in ```src/fuNEGF/models.py```
* a Jupyter notebook ```examples/one-dimensional_channel.ipynb``` contains the linear chain case study with the underlying physics explained
* a Jupyter notebok ```examples/time_complexity.ipynb``` contains a time complexity study of constructing the model $\mathcal{O}(N)$ and calculating the transmission coefficient $\mathcal{O}(N^2)$

## Example
A linear chain with a single or multiple on-site potential impurities will present a chemical potential (occupation) drop, which may not be apparent unless a phase relaxation is included, as shown below.
An additional momentum relaxation will cause a non-zero chemical potential slope in between the impurity regions.
The complete description and calculation are provided in the ```examples/one-dimensional_channel.ipynb``` notebook.

![example](./example.png)

## Features
* object-oriented
* PEP8-compliant
* including unit tests (limited for now)
* with automatically generated [documentation online](https://liborsold.github.io/fuNEGF/)


## The Theory In A Nutshell
The *retarded Green's function*

$$
\mathbf{G}^{\mathrm{R}}=[E \mathbf{I}-\mathbf{H}-\mathbf{\Sigma}]^{-1}
$$

along with the *advanced Green's function*

$$
    \mathbf{G}^{\mathrm{A}} = \left[ \mathbf{G}^{\mathrm{R}} \right]^\dagger
$$

provide the *spectral function*

$$
\mathbf{A}=i\left[\mathbf{G}^{\mathrm{R}}-\mathbf{G}^{\mathrm{A}}\right]
$$

and are used to solve for the *"electron occupation" Green's function* ($\mathbf{G}^{\mathrm{n}} \equiv -i \mathbf{G}^< $)

$$
\mathbf{G}^{\mathrm{n}}=\mathbf{G}^{\mathrm{R}} \Sigma^{\mathrm{in}} \mathbf{G}^{\mathrm{A}}
$$

which gives the *density matrix* 

$$
    \hat{\rho} = \mathbf{G}^{\mathrm{n}} / 2\pi .
$$


Both, the self-energy $\mathbf{\Sigma}$ and the in-scattering term $\Sigma^{\mathrm{in}}$ are sums of the left contact and right contact, while the self-energy also contains an intrinsic term

$$ \begin{align}
        \mathbf{\Sigma}^{\mathrm{in}} &= \mathbf{\Sigma}^{\mathrm{in}}_1 + \mathbf{\Sigma}^{\mathrm{in}}_2 , \\
        \mathbf{\Sigma} &= \mathbf{\Sigma}_1 + \mathbf{\Sigma}_2 + \mathbf{\Sigma}_0 
   \end{align}        
$$

NOTE: We use the (physically expressive) notation of S. Datta, where the self-energies and Green's functions in relation to the standard notation (on the right) are defined as  

$$
\begin{align}
    \mathbf{\Sigma} &\equiv \mathbf{\Sigma}^\mathrm{R} , \\
    \mathbf{G}^\mathrm{n} &\equiv -i \mathbf{G}^< , \\
    \mathbf{\Sigma}^\mathrm{in} &\equiv -i \mathbf{\Sigma}^< .
\end{align}
$$

