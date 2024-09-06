# (C) Copyright IBM 2022.

# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""
application generator
"""
from application.qft import QFT
from application.quantum_volume import QuantumVolume
from application.counterfeit_coin import CounterfeitCoin
from application.berstein_vazirani import BersteinVazirani


class ApplicationGenerator:
    """
    application generator
    """
    def __init__(self, seed):
        self.application_list = [QFT(seed), QuantumVolume(seed),
                                 CounterfeitCoin(seed), BersteinVazirani(seed)]
        return

    def get_app(self, name):
        """
        get application generator
        """
        for app in self.application_list:
            if name == app.name:
                return app
        return None

    def get_app_name_list(self):
        """
        get application list
        """
        name_list = []
        for app in self.application_list:
            name_list.append(app.name)
        return name_list
