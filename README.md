# Quantum Computing con IonQ + Qiskit

Este proyecto muestra cómo conectarse a IonQ desde Qiskit, instalar dependencias
y verificar los backends disponibles (simulador y hardware cuántico).

---

## Generar API key en IonQ

Para usar IonQ necesitas una API key desde su plataforma:

- https://cloud.ionq.com/

---

## Instalación de dependencias

```bash
pip install qiskit-ionq qiskit-aer
```

---

## Verificar backends disponibles

Conectar con IonQ y listar los backends disponibles (simulador y QPU):

```python
from qiskit_ionq import IonQProvider

provider = IonQProvider('tu-api-key-ionq')
print("Backends disponibles:", provider.backends())
```

Esto imprimirá algo como:

Backends disponibles: [
<qiskit_ionq.ionq_backend.IonQSimulatorBackend object at 0x7fd393ecb1d0>,
<qiskit_ionq.ionq_backend.IonQQPUBackend object at 0x7fd393e4fc80>
]

Para seleccionar el simulador (primer backend), usá:

```python
simulator = provider.backends()[0]
```

> **Nota:** el primer elemento suele ser el simulador, pero podés filtrarlo
> por nombre para mayor seguridad:
> ```python
> simulator = provider.get_backend('ionq_simulator')
> ```
