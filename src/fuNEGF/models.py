"""Contains the physical model classes for the NEGF solver.
"""

import numpy as np
import matplotlib.pyplot as plt

class LinearChain:
    """Linear chain tight-binding model with NEGF solver. Include arbitrary on-site potential impurities.
    """
        # Args:
        # H (N-by-N numpy array): Hamiltonian matrix.
        # E_vs_k_fun (function): Analytical dispersion E(k).
        # k_vs_E_fun (function): Inverse dispersion k(E).
        # k_states (list): The N allowed values of the k quantum number.
        # E_levels (list): The corresponding energy levels.
        # Sigma_1_fun_k (function): Self-energy Sigma_1(k).
        # Sigma_2_fun_k (function): Self-energy Sigma_2(k).
        # Sigma_fun_k (function): Self-energy Sigma(k).
        # Gamma_1_fun_k (function): Broadening Gamma_1(k).
        # Gamma_2_fun_k (function): Broadening Gamma_2(k).
        # f_1 (int): Fermi-Dirac distribution for lead 1.
        # f_2 (int): Fermi-Dirac distribution for lead 2.
        # Sigma_in_1_fun_k (function): In-scattering self-energy Sigma_in_1(k).
        # Sigma_in_2_fun_k (function): In-scattering self-energy Sigma_in_2(k).
        # Sigma_in_fun_k (function): In-scattering self-energy Sigma_in(k).

    def __init__(
        self,
        N=100,
        eps_0=0,
        t=1,
        a=1,
        H_impurity=None,
        make_H_periodic=False,
        plot_dispersion=True,
    ):
        """Initialize the parameters for a linear chain model.

        Args:
            N (int): Number of sites in the chain. Defaults to 100.
            eps_0 (float): On-site energy. Defaults to 0.
            t (float): Hopping. Defaults to 1.
            a (float): Lattice constant. Defaults to 1.
            H_impurity (numpy array, optional): Impurity Hamiltonian (typically on-site potential (Anderson) disorder). Defaults to None.
            make_H_periodic (bool, optional): If True, the Hamiltonian will be made periodic by adding t hopping to the [N-1, 0] and [0, N-1] sites. Defaults to False.
            plot_dispersion (bool, optional): If True, the dispersion will be plotted after constructing the Hamiltonian. Defaults to True.
        """
        # initialize the model parameters
        self.N = N
        self.eps_0 = eps_0
        self.t = t
        self.a = a

        # analytical dispersion E(k)
        self.E_vs_k_fun = lambda k: eps_0 + 2 * t * np.cos(k * a)
        # the inverse dispersion k(E)
        self.k_vs_E_fun = lambda E: np.arccos((E - eps_0) / (2 * t) + 0j) / a
        # the N allowed values of the k quantum number
        self.k_states = [-np.pi + 2 * np.pi / (N * a) * i for i in range(N)]
        # the corresponding energy levels
        self.E_levels = [self.E_vs_k_fun(k) for k in self.k_states]

        self.construct_H(make_H_periodic, print_H_matrix=False)
        self.add_H_impurity(H_impurity)
        if plot_dispersion:
            self.compare_dispersion_analytic_vs_numerical()

        # define the self-energies for a tight-binding model following Datta's Lessons from Nanoelectronics B
        self.Sigma_1_fun_k = lambda k: np.diag([t * np.exp(1j * k * a)] + [0] * (N - 1))
        self.Sigma_2_fun_k = lambda k: np.diag([0] * (N - 1) + [t * np.exp(1j * k * a)])
        self.Sigma_fun_k = lambda k: self.Sigma_1_fun_k(k) + self.Sigma_2_fun_k(k)

        # define the corresponding broadenings
        self.Gamma_1_fun_k = lambda k: np.diag([-2 * t * np.sin(k * a)] + [0] * (N - 1))
        self.Gamma_2_fun_k = lambda k: np.diag([0] * (N - 1) + [-2 * t * np.sin(k * a)])

        # Fermi-Dirac distributions for lead1 and lead2: lead 1 fully occupied, lead 2 empty
        self.f_1 = 1
        self.f_2 = 0

        # define the in-scattering self-energy (equivalent to )
        self.Sigma_in_1_fun_k = lambda k: self.Gamma_1_fun_k(k) * self.f_1
        self.Sigma_in_2_fun_k = lambda k: self.Gamma_2_fun_k(k) * self.f_2
        self.Sigma_in_fun_k = lambda k: self.Sigma_in_1_fun_k(
            k
        ) + self.Sigma_in_2_fun_k(k)

    def G_R_fun(self, k, E, Sigma_0=None):
        """The retarded Green's function for a given k and energy E.

        Args:
            k (float): the Bloch wave vector.
            E (float): Energy in eV.
            Sigma_0 (N-by-N numpy array, optional): The internal self-energy. Defaults to None.

        Returns:
            N-by-N numpy array: the retarded Green's function in matrix form.
        """
        if Sigma_0 is None:
            Sigma_0 = np.zeros((self.N, self.N))
        return np.linalg.inv(
            E * np.eye(self.N) - self.H - self.Sigma_fun_k(k) - Sigma_0
        )

    def construct_H(self, make_H_periodic=False, print_H_matrix=False):
        """Construct the linear chain tight-binding Hamiltonian.

        Args:
            make_H_periodic (bool, optional): If True, the Hamiltonian will be made periodic by adding t hopping to the [N-1, 0] and [0, N-1] sites. Defaults to False.
            print_H_matrix (bool, optional): If True, prints the Hamiltonian matrix. Defaults to False.
        """
        self.H = (
            np.diag([self.eps_0] * self.N)
            + np.diag([self.t] * (self.N - 1), k=1)
            + np.diag([np.conj(self.t)] * (self.N - 1), k=-1)
            + 0j
        )
        if make_H_periodic is True:
            self.H[0, self.N - 1] = self.t
            self.H[self.N - 1, 0] = np.conj(self.t)
        if print_H_matrix is True:
            print_H_matrix(self.H)

    def add_H_impurity(self, H_impurity, plot_dispersion=False):
        """Add an impurity Hamiltonian.

        Args:
            H_impurity (N-by-N numpy array): The impurity Hamiltonian (typically an Anderson disorder).
            plot_dispersion (bool, optional): Plot the numerical and analytical dispersion. Defaults to False.
        """
        if H_impurity is not None:
            self.H += H_impurity
        if plot_dispersion is True:
            self.compare_dispersion_analytic_vs_numerical()

    def plot_onsite_energy(self, ax=None):
        """Plot the on-site energy as horizontal lines.

        Args:
            ax (matplotlib.pyplot axis object, optional): If provided, the figure will be plotted to ax. Defaults to None.
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(5.5, 1.5))
        ax.step(
            range(self.N), np.real(np.diag(self.H)), where="mid", color="k", linewidth=1
        )
        ax.set_xlabel("site", fontsize=12)
        ax.set_ylabel("on-site energy (eV)", fontsize=12)
        ax.set_title("On-site energy")

    def compare_dispersion_analytic_vs_numerical(self):
        """Plots a comparison of the analytical and numerical dispersion."""
        self.eigvals, self.eigvecs = np.linalg.eigh(self.H)
        self.eigvals_ordered = list(self.eigvals[::2]) + list(self.eigvals[-1::-2])

        # plot the analytic energy dispersion
        fig, axes = plt.subplots(1, 2, figsize=[6.5, 3.5])
        plt.suptitle(f"t = {self.t}, eps_0 = {self.eps_0}")
        axes[0].plot(
            self.k_states,
            [self.E_vs_k_fun(k) for k in self.k_states],
            "-",
            label="E = eps + 2t cos(ka)",
            markersize=4,
        )
        # plot the energy dispersion from the Hamiltonian
        axes[0].plot(
            self.k_states,
            self.eigvals_ordered,
            "o",
            label="diagonalized H",
            markerfacecolor="none",
            markersize=5,
        )
        axes[0].set_ylabel(r"$E$ (eV)", fontsize=12)
        axes[0].set_xlabel(r"$k \cdot a$ (rad)", fontsize=12)
        axes[0].legend()

        # plot as a histogram
        axes[1].hist(
            [
                self.E_vs_k_fun(k) - self.eigvals_ordered[i]
                for i, k in enumerate(self.k_states)
            ]
        )
        axes[1].set_ylabel(r"#", fontsize=12)
        axes[1].set_xlabel(
            r"$E_{\rm analytic} - E_{\rm diagonalized}$ (eV)", fontsize=10
        )
        plt.tight_layout()
        plt.show()

    def plot_transmission(self, ax=None):
        """Plots the transmission function T(E) given by T = Tr[Gamma_1 G_R Gamma_2 G_A].

        Args:
            ax (matplotlib.pyplot axis object, optional): If provided, the figure will be plotted to ax. Defaults to None.
        """
        E_to_plot = []
        T_states = []
        for k in self.k_states:
            E = self.E_vs_k_fun(k)
            # for E in E_array: #np.linspace(8.0, 12, 200):
            #     k = self.k_fun(E)
            G_R = self.G_R_fun(k, E)
            G_A = np.conj(G_R.T)
            T = np.real(
                np.trace(self.Gamma_1_fun_k(k) @ G_R @ self.Gamma_2_fun_k(k) @ G_A)
            )
            T_states.append(T)
            E_to_plot.append(E)
        if ax is None:
            fig, ax = plt.subplots(figsize=(2.5, 3))
        ax.plot(
            T_states,
            E_to_plot,
            "o-",
            markerfacecolor="none",
            markersize=2,
            color="olive",
        )
        ax.set_title("Transmission")
        ax.set_ylabel("energy (eV)", fontsize=12)
        ax.set_xlabel("Transmission function " + r"$T(E)$", fontsize=12)
        ax.set_xlim([-0.1, 1.1])
        # ax.grid(True)

    def Greens_functions_solver(self, k, E, D0_phase, D0_phase_momentum, N_sc=70):
        """Self-consistent iterative NEGF solver in case where the phase and momentum relaxation
            are defined in terms of the Green's functions themselves (see Datta's Lessons from Nanoelectronics B).

        Args:
            k (float): the Bloch wave vector.
            E (float): Energy in eV.
            D0_phase (float): The phase relaxation parameter.
            D0_phase_momentum (float): The phase+momentum relaxation parameter.
            N_sc (int, optional): Number of self-consistent iteration steps: typically a value around 50 should be enough. Defaults to 70.

        Returns:
            N-by-N numpy arrays: the self-consistently solved Green's functions (retarded, advanced, electron occupation), the internal self-energy Sigma_0,
                and the in-scattering self-energy Sigma_in_0.
        """
        # define the D matrix used to define Sigma_0 and Sigma_in_0
        D = D0_phase * np.ones((self.N, self.N)) + D0_phase_momentum * np.eye(self.N)
        # in the very first step, the Green's functions will not contribute to the self-energies, so let's initialize them with 0 matrices
        G_R = np.zeros((self.N, self.N), dtype=complex)
        G_n = np.zeros((self.N, self.N), dtype=complex)
        Sigma_0 = np.multiply(D, G_R)
        Sigma_in_0 = np.multiply(D, G_n)
        for i in range(N_sc):
            G_R = self.G_R_fun(k, E, Sigma_0=Sigma_0)
            G_A = np.conj(G_R.T)
            G_n = G_R @ (self.Sigma_in_fun_k(k) + Sigma_in_0) @ G_A
            Sigma_0 = np.multiply(D, G_R)
            Sigma_in_0 = np.multiply(D, G_n)
        return G_R, G_A, G_n, Sigma_0, Sigma_in_0

    def plot_occupation(
        self, D0_phase, D0_phase_momentum, N_sc=70, E_to_plot=0, show=True, ax=None
    ):
        """Plot the occupation f(j) of the sites j in the chain, which in the case f1=1, f2=0 corresponds to the
            electrochemical potential mu(j) = qV f(j), where a potential V is imagined to be applied across the
            device and q is the electron charge.

        Args:
            D0_phase (float): The phase relaxation parameter.
            D0_phase_momentum (float): The phase+momentum relaxation parameter.
            N_sc (int, optional): Number of self-consistent iteration steps: typically a value around 50 should be enough. Defaults to 70.
                                    N_sc=1 effectively turns off the phase/momentum relaxation.
            E_to_plot (int, optional): The energy at which to plot the occupation. Defaults to 0.
            show (bool, optional): If True, the plot will be shown. Defaults to True.
            ax (_type_, optional): If provided, the figure will be plotted to ax. Defaults to None.
        """

        E = E_to_plot
        k = self.k_vs_E_fun(E_to_plot)

        G_R, G_A, G_n, Sigma_0, Sigma_in_0 = self.Greens_functions_solver(
            k, E, D0_phase, D0_phase_momentum, N_sc
        )

        A = 1j * (G_R - G_A)
        f = np.divide(np.diag(G_n), np.diag(A))

        if ax is None:
            fig, ax = plt.subplots(figsize=(3.5, 3))
        n_sites_contact = 3
        ax.plot(
            range(-n_sites_contact, self.N + n_sites_contact),
            n_sites_contact * [self.f_1] + list(f) + n_sites_contact * [self.f_2],
            linestyle="-",
            linewidth=1,
        )
        ax.set_title("Occupation")
        ax.set_xlabel("site", fontsize=12)
        ax.set_ylabel("occupation " + r"$f$", fontsize=12)
        ax.set_ylim([-0.05, 1.05])
        # ax.grid(True)
