import numpy as np

class StateVectorSimulator: # represents a state vect

    def __init__(self, n_qubits):
        self.n = n_qubits
        self.dim = 2**n_qubits

        self.state = np.zeros(self.dim, dtype=complex)

        self.state[0] = 1.0 + 0j # sets 0 as significant. Equivalent to 1|0> + 0|1> 



    def apply_single_qubit_gate(self, gate, qubit): 
        # applies gate to one qubit
        # instead of tensor product to get the gate into a 2^n x 2^n matrix, we do it in a easier way

        if gate.shape != (2,2): # check to ensure the correct size gate
            raise ValueError("Gate must be 2x2 matrix")

        if qubit <0 or qubit >= self.n: # index check
            raise ValueError("Invalid qubit index.")

        bit_position = self.n - 1 - qubit # bit position in the state of the qubit we're trying to change

        new_state = np.zeros_like(self.state)

        for index in range(self.dim):
            bit = (index >> bit_position) & 1

            if bit == 0: # Only the qubit to be considered gets triggered here
                index_0 = index
                index_1 = index | (1 << bit_position)

                a0 = self.state[index_0]
                a1 = self.state[index_1]

                new_state[index_0] = (gate[0,0] * a0 + gate[0,1] * a1)
                new_state[index_1] = (gate[1,0] * a0 + gate[1,1] * a1)

        self.state = new_state



    def apply_cnot(self, control, target):

        if control < 0 or control >= self.n:
            raise ValueError("Invalid control qubit.")

        if target < 0 or target >= self.n:
            raise ValueError("Invalid target qubit.")

        if control == target:
            raise ValueError("Control and target must be different.")

        control_bit = self.n - 1 - control
        target_bit = self.n - 1 - target

        new_state = self.state.copy()

        for index in range(self.dim):
            control_value = (index >> control_bit) & 1
            target_value = (index >> target_bit) & 1

            if control_value == 1 and target_value == 0:
                target_index = index ^ (1 << target_bit)

                new_state[target_index] = self.state[index]
                new_state[index] = self.state[target_index]

        self.state = new_state



    def apply_cz(self, control, target):

        if control < 0 or control >= self.n:
            raise ValueError("Invalid control qubit.")

        if target < 0 or target >= self.n:
            raise ValueError("Invalid target qubit.")

        if control == target:
            raise ValueError("Control and target must be different.")

        control_bit = self.n - 1 - control
        target_bit = self.n - 1 - target

        for index in range(self.dim):

            control_value = (index >> control_bit) & 1
            target_value = (index >> target_bit) & 1

            if control_value == 1 and target_value == 1:
                self.state[index] *= -1

    