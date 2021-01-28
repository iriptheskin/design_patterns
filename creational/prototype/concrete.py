from copy import deepcopy

from creational.prototype import Prototype


class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)
