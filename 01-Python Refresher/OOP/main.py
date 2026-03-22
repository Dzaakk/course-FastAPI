from Enemy import *
from Zombie import *
from Ogre import * 

zombie = Zombie( 10, 1)
ogre = Ogre( 20, 2)

def battle(e: Enemy):
    e.talk()
    e.attack()

battle(zombie)
battle(ogre)
