# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:05:15 2023

@author: My
"""

from abc import ABC, abstractmethod

class Fighter(ABC):
    
    @abstractmethod
    def attack(self, defender: 'Fighter') -> None:
        pass
    
    @abstractmethod
    def defend(self, damage: int) -> int:
        pass
    
    @abstractmethod
    def apply_damage(self, damage: int) -> None:
        pass