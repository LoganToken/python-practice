# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:48:36 2023

@author: My
"""

from hero import Hero
import random
import math

class Mage(Hero):
    
    def __init__(self, name, health, weapon):
        super().__init__(name, health, weapon)
        
        self.intelligence = 20
    
    def attack(self, opponent):
        damage = math.floor(random.random()*self.intelligence)
        opponent.defend(damage)
    
    def defend(self, damage):
        guaranteed_damage = 4
        
        if (damage <= guaranteed_damage):
            self.apply_damage(damage)
            return
        
        residual = damage - guaranteed_damage
        shield_multiplier = self.intelligence / (25 + damage)
        residual_taken = math.floor(shield_multiplier * residual)
        damage_taken = guaranteed_damage + residual_taken
        self.apply_damage(damage_taken)