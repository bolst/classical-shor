from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
import math

# input: coprime integers N and a (1 < a < N)
# output: order of a (i.e., min(r > 0) such that a^r = 1 mod N
def find_order(a, N):

    # second register size
    m = math.ceil( math.log(N, 2) )

    # first register size
    n = 2*m

    circ = QuantumCircuit(n, m)
    circ.draw()

    # return the order r of a
    return 1