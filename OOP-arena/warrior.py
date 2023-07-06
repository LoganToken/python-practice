# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:49:48 2023

@author: My
"""

from hero import Hero
import random

class Warrior(Hero):
    
    def __init__(self, name, health, weapon, strength):
        assert strength >= 0, "strength must be non negative"
        
        super().__init__(name, health, weapon)
        self.strength = strength
    
    def __repr__(self):
        return f"{self.name} is a mighty warrior with a strength of {self.strength}"
    
    def defend(self, damage):
        blocked = self._roll_for_block(damage)
        if blocked:
            print(f"{self.name} blocked the hit!")
            self.apply_damage(0)
        else:
            self.apply_damage(damage)
      
    def _roll_for_block(self, damage):
        if (damage >= self.strength):
            return False
        
        block_constant = 1
        block_chance = (block_constant + damage) / (block_constant + self.strength)
        random_number = random.random()
        if (random_number > block_chance):
            return True
        
        return False
        
        
        