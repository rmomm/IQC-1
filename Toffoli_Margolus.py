import math
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator

def toffoli_matrix() -> np.ndarray:
    mat = np.eye(8, dtype=complex)
    mat[6,6] = 0
    mat[7,7] = 0
    mat[6,7] = 1
    mat[7,6] = 1
    return mat

def margolus_matrix() -> np.ndarray:
    mat = np.zeros((8,8), dtype=complex)
    for i in range(4):
        mat[i,i] = 1
    mat[4,4] = 1
    mat[5,5] = -1
    mat[6,7] = 1
    mat[7,6] = 1
    return mat


def toffoli_decomposed_circuit():
    qc = QuantumCircuit(3, name="Toffoli")

    qc.h(2)
    qc.cx(1, 2)
    qc.tdg(2)
    qc.cx(0, 2)
    qc.t(2)
    qc.cx(1, 2)
    qc.tdg(2)
    qc.cx(0, 2)
    qc.t(1)
    qc.t(2)
    qc.h(2)
    qc.cx(0, 1)
    qc.t(0)
    qc.tdg(1)
    qc.cx(0, 1)

    return qc

def margolus_decomposed_circuit():
    qc = QuantumCircuit(3, name="Margolus")

    angle = math.pi / 4
    qc.ry(angle, 2)
    qc.cx(1, 2)
    qc.ry(angle, 2)
    qc.cx(0, 2)
    qc.ry(-angle, 2)
    qc.cx(1, 2)
    qc.ry(-angle, 2)

    return qc

def display_circuits():
    qc_t = toffoli_decomposed_circuit()
    print("\nToffoli (decomposed):")
    print(qc_t.draw("text"))

    qc_m = margolus_decomposed_circuit()
    print("\nMargolus (decomposed):")
    print(qc_m.draw("text"))



def basis_state(i):
    state = np.zeros((8,1), dtype=complex)
    state[i,0] = 1
    return state

def apply_gate(gate_matrix, name="Gate"):
    print(f"\n {name} ")
    for i in range(8):
        state_in = basis_state(i)
        state_out = gate_matrix @ state_in
        idx = np.argmax(np.abs(state_out))
        amp = state_out[idx]
        sign = "-" if np.isclose(amp, -1) else ""
        print(f"|{format(i,'03b')}> -> {sign}|{format(idx,'03b')}>")


if __name__ == "__main__":

    display_circuits()

    apply_gate(toffoli_matrix(), "Toffoli matrix action")
    apply_gate(margolus_matrix(), "Margolus matrix action")