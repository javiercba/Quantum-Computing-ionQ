Generar una api key en ionq

!pip install qiskit-ionq qiskit-aer

verificar simuladores:
from qiskit_ionq import IonQProvider
provider = IonQProvider('api-key-ionq')

Esto imprimirá una lista con los nombres exactos que puedes usar:
print("Backends disponibles:", provider.backends())

Ejemplo:
Backends disponibles: 

[<qiskit_ionq.ionq_backend.IonQSimulatorBackend object at 0x7fd393ecb1d0>, 
<qiskit_ionq.ionq_backend.IonQQPUBackend object at 0x7fd393e4fc80>]


seleccionar el 1er simulador disponible: 
provider.backends()[0]
