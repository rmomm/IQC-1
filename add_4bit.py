import math
from qiskit import QuantumCircuit
from qiskit.visualization import plot_circuit_layout
from qiskit_aer import AerSimulator
from qiskit import transpile

def maj(circ, a, b, c):
    circ.cx(a, b)
    circ.cx(a, c)
    circ.ccx(b, c, a)

def uma(circ, a, b, c):
    circ.ccx(b, c, a)
    circ.cx(a, c)
    circ.cx(c, b)

def four_bit_adder():
    circ = QuantumCircuit(9, 4)  
    
    a = [0,1,2,3]
    b = [4,5,6,7]
    c = 8  

    circ.x(a[0])
    circ.x(a[2])
    circ.x(b[1])
    circ.x(b[2])


    maj(circ, a[0], b[0], c)
    maj(circ, a[1], b[1], a[0])
    maj(circ, a[2], b[2], a[1])
    maj(circ, a[3], b[3], a[2])


    uma(circ, a[3], b[3], a[2])
    uma(circ, a[2], b[2], a[1])
    uma(circ, a[1], b[1], a[0])
    uma(circ, a[0], b[0], c)

    return circ

if __name__ == "__main__":
    circ = four_bit_adder()
    print(circ.draw("text", fold=-1))

