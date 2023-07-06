# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:01:29 2023

@author: My
"""

from warrior import Warrior
from mage import Mage

from zombie import Zombie
from twins import Twins
from troll import Troll

from arena import Arena

stanley = Mage("stanley", 100, "staff")

marcus = Warrior("marcus", 100, "broadsword", 12)

zombie = Zombie("Zomboid", 80, "claws")

twins = Twins("Ana and Bob", 60, "psychic abilities")

troll = Troll("Trollium", 70, "Big Club")

monsters = [twins, zombie, troll]
arena = Arena(stanley, monsters)
arena.run()
