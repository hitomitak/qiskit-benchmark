# (C) Copyright IBM 2022.

# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""
Executor Class
"""
from backends.qiskit_executor import QiskitExecutor
from backends.qsharp_executor import QsharpExecutor
from backends.projectq_executor import ProjectQExecutor


class Executor:
    """
    Backend Executor
    """
    def __init__(self, backend_name=None, name=None, seed=None):
        self.seed = seed
        self.name = name
        self.backend_name = backend_name
        self.backend_list = [QiskitExecutor(self), QsharpExecutor(self), ProjectQExecutor(self)]
        return

    def get_backend(self, name):
        """
        get backend class
        """
        for backend in self.backend_list:
            for bk_name in backend.name:
                if bk_name == name:
                    return backend
        return None

    def get_backend_name_list(self):
        """
        get backend name list
        """
        name_list = []
        for backend in self.backend_list:
            for name in backend.name:
                name = backend.name
                name_list.append(name)
        return name_list
