from qiskit import QuantumCircuit, transpile, assemble, execute
from qiskit.providers.basicaer import BasicAer  # Alternativa a Aer

# Crear un circuito cuántico simple
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Usar BasicAer como simulador
simulator = BasicAer.get_backend('qasm_simulator')
job = execute(qc, simulator)
result = job.result()

# Mostrar los resultados
print(result.get_counts(qc))






