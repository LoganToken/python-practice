# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:13:51 2023

@author: My
"""
from fighter import Fighter


class Monster(Fighter):
    
    def __init__(self, name: str, health: int, weapon: str):
        assert health > 0, "monster must have non zero health (tried to pass {health})"
        
        self.name = name
        self.max_health = health
        self.health = self.max_health
        self.weapon = weapon
        self.is_alive = True
        self.attack_damage = 8
        
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.health}, {self.weapon})"
    
    def attack(self, opponent: 'Fighter'):
        damage = self.attack_damage
        print(f"The Ugly {self.name} attacks {opponent.name} for {damage} damage!")
        opponent.defend(damage)
        return
    
    def defend(self, damage: int):
        self.apply_damage(damage)
        return
    
    def apply_damage(self, damage: int):
        print(f"The Ugly {self.name} takes {damage} damage!")
        self.health -= damage
        if (self.health <= 0):
            self.health = 0
            self.is_alive = False
            print(f"The Ugly {self.name} has been vanquished")