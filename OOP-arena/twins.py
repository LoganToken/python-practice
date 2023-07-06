# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:40:03 2023

@author: My
"""

from monster import Monster

class Twins(Monster):
    
    def __init__(self, name, health, weapon):
        super().__init__(name, health, weapon)
        
        self.attack_damage = 5
        
    def attack(self, opponent):
        print(f"The twins {self.name} unleash their double attack!")
        opponent.defend(self.attack_damage)
        opponent.defend(self.attack_damage)