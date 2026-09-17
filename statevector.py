import numpy as np

class StateVectorSimulator: # represents a state vect

    def __init__(self, n_qubits):
        self.n = n_qubits
        self.dim = 2**n_qubits

        self.state = np.zeroes(self.dim, dtype=complex)

        self.state[0] = 1.0 + 0j # sets 0 as significant. Equivalent to 1|0> + 0|1> 