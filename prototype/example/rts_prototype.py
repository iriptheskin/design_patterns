from copy import deepcopy
from typing import Union

from prototype.prototype import Prototype


class Unit(Prototype):
    unit_type = None

    def __init__(self, level):
        if not self.unit_type:
            raise ValueError('The `unit_type` variable is not set.')

        self.level, self.life, self.speed, \
            self.attack_power, self.attack_range, self.weapon = self.__read_stats(level)

    def __read_stats(self, level) -> list[Union[str, int]]:
        """
        Read stats from file.
        :param level: Determines the stat file to read.
        :return:
        """
        filename = f"data/{self.unit_type}_{level}.dat"

        with open(filename) as parameter_file:
            lines = parameter_file.read().split("\n")

        return lines

    def __repr__(self) -> str:
        return f'{self.unit_type} ' \
               f'Level={self.level} ' \
               f'Life={self.life} ' \
               f'Speed={self.speed} ' \
               f'Attack Power={self.attack_power} ' \
               f'Attack Range={self.attack_range} ' \
               f'Weapon={self.weapon}'

    def clone(self) -> 'Unit':
        """ Concrete method to clone the unit."""
        return deepcopy(self)


class Knight(Unit):
    unit_type: str = 'Knight'


class Archer(Unit):
    unit_type: str = 'Archer'


class Barrack:
    units = {
        'Knight': {1: Knight(1)},
        'Archer': {5: Archer(5)},
    }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()



