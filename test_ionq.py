# -*- coding: utf-8 -*-
"""test_ionq; prueba de Entrelazamiento cuantico, 
   autor: javier uranga - abril de 2026
"""

from qiskit_ionq import IonQProvider
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile

# 1. Configuración de registros
# define 2 qbits
qubits = QuantumRegister(2, name="q_ion")
# define 2 bits clasicos
bits = ClassicalRegister(2, name="c_out")
qc = QuantumCircuit(qubits, bits)

# 2. Construcción del Circuito
qc.h(qubits[0])             # usando una puerta H de Hadamard, se pone al 1er qbit en superposicion
qc.cx(qubits[0], qubits[1]) # Se hace el entrelazamiento de los 2 qbits con una operacion CX: abreviatura de Controlled-NOT, si el 1er qbit es 1, se invierte el 2do

# 3. Medición Explícita
# se mide cada qbit y se copia su valor en un bit clasico.
# Debido al entrelazamiento el resultado correcto debe ser 00 ó 11.
qc.measure(qubits[0], bits[0])
qc.measure(qubits[1], bits[1])

# 4. Conexión con IonQ
provider = IonQProvider('api-key-ionq')
backend = provider.get_backend('ionq_simulator') #seria lo mismo hacer: backend = provider.backends()[0]

# 5. Transpilación y Ejecución
qc_ionq = transpile(qc, backend=backend, optimization_level=1)
print(f"Ejecutando {qc.name} en {backend.name}...")

job = backend.run(qc_ionq, shots=100)
result = job.result()

print("Resultados:", result.get_counts())