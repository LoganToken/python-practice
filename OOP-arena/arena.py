# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:14:15 2023

@author: My
"""

class Arena:
    
    def __init__(self, hero, monsters):
        self.hero = hero
        self.monsters = monsters
    
    def choose_monster(self):
        return self.monsters.pop()
    
    def battle(self, monster):
        heros_turn = True
        while (self.hero.is_alive and monster.is_alive):
            if (heros_turn):
                self.hero.attack(monster)
            else:
                monster.attack(self.hero)
            heros_turn = not heros_turn
        print("The battle has ceased.")
        if (not self.hero.is_alive):
            print("oh dear, you have been defeated")
        if (not monster.is_alive):
            print(f"you have defeated {monster}!")
        
    def run(self):
        while (len(self.monsters) > 0):
            monster = self.choose_monster()
            print(f"\nUp next is a battle between {self.hero} and {monster}!")
            self.battle(monster)
            if (not self.hero.is_alive):
                print(f"{self.hero.name} has been defeated by the flurry of monsters")
                return
            
        print("You have defeated all of the monsters!")