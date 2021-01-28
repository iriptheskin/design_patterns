from copy import deepcopy

from prototype.prototype import Prototype


class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)
