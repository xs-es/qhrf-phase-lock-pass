from ucc_bench.compilers.base_compiler import BaseCompiler
from ucc_bench.registry import register
from qiskit import QuantumCircuit
from qhrf_pass import QHRFPhaseLockPass
from qiskit.transpiler import PassManager

@register.compiler("qhrf")
class QHRFCompiler(BaseCompiler[QuantumCircuit]):
    @classmethod
    def version(cls) -> str:
        return "QHRF-PhaseLockPass v1.0"

    def compile(self, circuit: QuantumCircuit) -> QuantumCircuit:
        pm = PassManager([QHRFPhaseLockPass()])
        return pm.run(circuit)

    def count_multi_qubit_gates(self, circuit: QuantumCircuit) -> int:
        return circuit.count_ops().get('cx', 0)
