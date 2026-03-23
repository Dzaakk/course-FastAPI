from Enemy import *
import random

class Zombie(Enemy):
    
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Zombie', health_points=health_points, attack_damage=attack_damage)
    
    def talk(self):
        print("Braaaains...")
    
    def spread_disease(self):
        print("The zombie spreads a deadly disease to you!")
    
    def special_attack(self):
        did_special_attack_succeed = random.random() < 0.5
        if did_special_attack_succeed:
            self.health_points += 1
            print("Zombie regenerated 1HP!")