from Enemy import *
from Zombie import *
from Ogre import * 

zombie = Zombie( 10, 1)
ogre = Ogre( 20, 2)
# big_zombie = Enemy("Big Zombie", 50, 5)

print(zombie. talk())
print(zombie.spread_disease())

print(ogre.get_type_of_enemy())
print(ogre.talk())

# print(zombie.talk())
# print(zombie.walk_forward())
# print(zombie.attack())

# print(big_zombie.talk())
# print(big_zombie.walk_forward())
# print(big_zombie.attack())
