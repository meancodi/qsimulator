from measurement import *
from observables import *
from gates import *
from statevector import *
import numpy as np


def test_bell_state():

    sim = StateVectorSimulator(2)

    expected_initial = np.array([1,0,0,0],dtype=complex)
    print("Initial state = ", sim.state)
    assert np.allclose(sim.state, expected_initial) # checks if they are almost equal, within some tolerance

    sim.apply_single_qubit_gate(H,0)
    expected_after_h  = np.array(
        [1/np.sqrt(2), 0, 1/np.sqrt(2), 0],
        dtype=complex
    )
    print("After H gate", sim.state)
    assert np.allclose(sim.state, expected_after_h)

    sim.apply_cnot(0, 1)
    expected_bell = np.array(
        [ 1 / np.sqrt(2), 0, 0, 1 / np.sqrt(2)],
        dtype=complex
    )
    print("After CNOT =", sim.state)
    assert np.allclose(sim.state,expected_bell)

    z0 = expectation_z(sim,0)
    z1 = expectation_z(sim,1)
    zz = expectation_zz(sim,0,1)

    print(f"Z0 = {z0}\nZ1 = {z1}\nZZ = {zz}")

    assert np.isclose(z0, 0.0)
    assert np.isclose(z1, 0.0)
    assert np.isclose(zz, 1.0)



def test_measurement_bell_state():
    sim = StateVectorSimulator(2)

    print(f"Initial state {sim.state}")
    
    sim.apply_single_qubit_gate(H,0)
    sim.apply_cnot(0,1)

    print(f"State after H and CNOT = {sim.state}")

    result = measure(sim, 0)

    print(f"Result = {result}")

    assert result in [0,1]

    bit_position = 1

    for index in range(sim.dim): # to check that q0 is def the value we measured
        bit = (index >> bit_position) & 1
        if bit != result:
            assert np.isclose(sim.state[index], 0.0)

    assert np.isclose(np.linalg.norm(sim.state), 1.0)



print("---- bell state test ----")
test_bell_state()
print("---- measurement test ----")
test_measurement_bell_state()

