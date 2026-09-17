import numpy as np

def expectation_z(simulator, qubit):

    if qubit < 0 or qubit >= simulator.n:
        raise ValueError("Invalid qubit index")

    bit_position = simulator.n - 1 - qubit

    expectation = 0.0

    for index in range(simulator.dim):
        bit = (index >> bit_position) & 1
        probability = abs(simulator.state[index])**2

        if bit == 0:
            expectation += probability
        else:
            expectation -= probability

    expectation = float(np.real(expectation))
    assert -1.0 - 1e-12 <= expectation <= 1.0 + 1e-12

    return expectation

def expectation_zz(simulator, qubit_a, qubit_b):

    if qubit_a < 0 or qubit_a >= simulator.n:
        raise ValueError("Invalid first qubit index.")

    if qubit_b < 0 or qubit_b >= simulator.n:
        raise ValueError("Invalid second qubit index.")

    if qubit_a == qubit_b:
        raise ValueError("The two qubits must be different.")

    bit_a = simulator.n - 1 - qubit_a
    bit_b = simulator.n - 1 - qubit_b

    expectation = 0.0

    for index in range(simulator.dim):
        value_a = (index >> bit_a) & 1
        value_b = (index >> bit_b) & 1

        probability = abs(simulator.state[index]) ** 2

        if value_a == value_b:
            expectation += probability
        else:
            expectation -= probability

    expectation = float(np.real(expectation))
    assert -1.0 - 1e-12 <= expectation <= 1.0 + 1e-12

    return expectation