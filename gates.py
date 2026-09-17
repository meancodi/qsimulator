import numpy as np

I = np.array([
    [1,0],
    [0,1]
], dtype=complex)

X = np.array([
    [1,0],
    [0,1]
], dtype=complex)

Y = np.array([
    [0,-1j],
    [1j,0]
], dtype=complex)

Z = np.array([
    [1,0],
    [0,-1]
], dtype=complex)

H = (1/np.sqrt(2)) * np.array([
    [1,1],
    [1,-1]
], dtype=complex)

S = np.array([
    [1,0],
    [0,1j]
], dtype=complex)

T = np.array([
    [1,0],
    [0,np.exp(1j * (np.pi / 4))]
])

CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
], dtype=complex)


CZ = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, -1]
], dtype=complex)


def RZ(theta): # Rz(theta) introduces theta phase difference. Needs to be a function cause it has a variable theta
    return np.array([
        [np.exp(-1j * theta / 2), 0],
        [0, np.exp(1j * theta / 2)]
    ], dtype=complex)
