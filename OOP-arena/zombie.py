# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 15:15:25 2023

@author: My
"""
from monster import Monster

class Zombie(Monster):
    
    def __init__(self, name: str, health: int, weapon: str):
        super().__init__(name, health, weapon)
        
        # reanimated describes wether the zombie has died once and is now reanimated
        self.reanimated = False
        self.attack_damage = 6
        
    def apply_damage(self, damage: int):
        print(f"The Ugly {self.name} takes {damage} damage!")
        self.health -= damage
        if (self.health <= 0):
            if (self.reanimated):
                self.health = 0
                self.is_alive = False
                print(f"The Ugly {self.name} has been vanquished")
            else:
                self.reanimated = True
                self.health = self.max_health // 2
                self.attack_damage = self.attack_damage // 2
                print(f"{self.name} Reanimates!")