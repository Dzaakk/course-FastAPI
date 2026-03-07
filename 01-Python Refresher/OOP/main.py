from Enemy import *

zombie = Enemy("Zombie", 10, 1)
big_zombie = Enemy("Big Zombie", 50, 5)

print(zombie.talk())
print(zombie.walk_forward())
print(zombie.attack())

print(big_zombie.talk())
print(big_zombie.walk_forward())
print(big_zombie.attack())
