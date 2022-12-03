from qiskit import QuantumCircuit,QuantumRegister
from qiskit.quantum_info import DensityMatrix,partial_trace
import numpy as np

qr=QuantumRegister(2)

circ=QuantumCircuit (qr)

circ. h(qr[0])

circ.cx(qr[0],qr[1])
DM=DensityMatrix.from_instruction(circ)
print(DM.data)

PT=partial_trace(DM,[0])

print (PT.data)
