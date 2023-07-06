# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:02:27 2023

@author: My
"""

from fighter import Fighter

class Hero(Fighter):
    
    def __init__(self, name: str, health: int, weapon: str):
        assert health > 0, "health must be greater than 0"
        
        self.name = name
        self.max_health = health
        self.health = self.max_health
        self.weapon = weapon
        self.is_alive = True
        
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.health}, {self.weapon})"
    
    def attack(self, opponent: 'Fighter'):
        damage = 10
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        opponent.defend(damage)
        return
    
    def defend(self, damage: int):
        self.apply_damage(damage)
        return
    
    def apply_damage(self, damage: int):
        print(f"{self.name} takes {damage} damage!")
        self.health -= damage
        if (self.health <= 0):
            self.health = 0
            self.is_alive = False
            print("oh dear, you have died")
    