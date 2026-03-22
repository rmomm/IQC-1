from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

#Superposition

qc = QuantumCircuit(1, 1)

qc.h(0)
qc.measure(0, 0)

print("Superposition:")
print(qc.draw("text"))

#Bell state

qc_bell = QuantumCircuit(2, 2)

qc_bell.h(0)
qc_bell.cx(0, 1)

qc_bell.measure([0, 1], [0, 1])

print("\nBell state:")

print(qc_bell.draw("text"))
