from Enemy import *
import random


class Ogre(Enemy):
    
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Ogre', health_points=health_points, attack_damage=attack_damage)
    
    def talk(self):
        print("Grrr... I am an Ogre!")

    def special_attack(self):
        did_special_attack_succeed = random.random() < 0.2
        if did_special_attack_succeed:
            self.attack_damage += 4
            print("Ogre's angry and attack damage increased by 4!")