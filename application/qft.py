# (C) Copyright IBM 2022.

# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
""" QSAM-Bench is a quantum-software bencmark suite """
import math
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister


class QFT:
    """
    QFT Generator
    """
    def __init__(self, seed):
        self.name = "qft"
        self.seed = seed

    @classmethod
    def cu1(cls, circ, l_value, a_value, b_value):
        """
        cu1 gate
        """
        circ.u1(l_value/2, a_value)
        circ.cx(a_value, b_value)
        circ.u1(-l_value/2, b_value)
        circ.cx(a_value, b_value)
        circ.u1(l_value/2, b_value)

    def qft(self, circ, qreg, num):
        """n-qubit QFT on q in circ."""
        for j in range(num):
            for k in range(j):
                self.cu1(circ, math.pi/float(2**(j-k)), qreg[j], qreg[k])
                circ.h(qreg[j])

    def build_model_circuits(self, num):
        """
        create model
        """
        qreg = QuantumRegister(num)
        creg = ClassicalRegister(num)

        qftcirc = QuantumCircuit(qreg, creg)

        self.qft(qftcirc, qreg, num)
        qftcirc.barrier(qreg)

        for j in range(num):
            qftcirc.measure(qreg[j], creg[j])

        return qftcirc

    def gen_application(self, app_arg):
        """
        generate application
        """
        qubits = app_arg["qubit"]
        q_p = self.build_model_circuits(qubits)
        return q_p
