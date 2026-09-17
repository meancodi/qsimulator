import numpy as np

def measure(simulator, qubit):

    if qubit < 0 or qubit >= simulator.n:
        raise ValueError("Invalid qubit index")

    bit_position = simulator.n - 1 - qubit

    prob_0 = 0.0
    prob_1 = 0.0

    for index in range(simulator.dim):
        bit = (index >> bit_position) & 1
        prob = abs(simulator.state[index]) ** 2 # calculate prob here

        if bit == 0:
            prob_0 += prob
        else:
            prob_1 = prob

    total_prob = prob_0 + prob_1

    prob_0 /= total_prob
    prob_1 /= total_prob

    result = np.random.choice([0,1], p=[prob_0, prob_1])

    new_state = simulator.state.copy()

    for index in range(simulator.dim):
        bit = (index >> bit_position) & 1
        if bit != result: # set prob of all states that are impossible to 0
            new_state[index] = 0.0

    norm = np.linalg.norm(new_state)

    if norm == 0:
        raise RuntimeError("Norm is zero, so invalid zero state has been measured")

    new_state /= norm

    simulator.state = new_state

    return result