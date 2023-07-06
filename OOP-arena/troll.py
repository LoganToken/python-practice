# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:58:53 2023

@author: My
"""

from monster import Monster
import random

class Troll(Monster):
    
    def __init__(self, name, health, weapon):
        super().__init__(name, health, weapon)
        
        self.attack_damage = 20
        self.accuracy = 0.5
        
    def attack(self, opponent):
        print(f"{self.name} takes a swing!")
        accuracy_roll = random.random()
        if (accuracy_roll < self.accuracy):
            print(f"{self.name} lands a devastating blow!")
            opponent.defend(self.attack_damage)
        else:
            print(f"{self.name} missed their attack!")