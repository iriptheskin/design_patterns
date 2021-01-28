from creational.prototype import Barrack

barrack = Barrack()
knight = barrack.build_unit('Knight', 1)
archer = barrack.build_unit('Archer', 5)


assert barrack.units['Knight'][1] is not knight, 'New knight is the same one.'
assert barrack.units['Archer'][5] is not archer, 'New archer is the same one.'
