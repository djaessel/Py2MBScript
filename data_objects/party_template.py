# This Python file uses the following encoding: utf-8

from enum import Enum
from troop import Troop
from faction import Faction
from game_menu import GameMenu

import factions as fac


class PartyPersonality(Enum):
    SOLDIER = "soldier_personality"  # = "aggressiveness_8 | courage_9"
    MERCHANT = "merchant_personality" # = "aggressiveness_0 | courage_7"
    ESCORTED_MERCHANT = "escorted_merchant_personality" # = "aggressiveness_0 | courage_11"
    BANDIT = "bandit_personality"   # = "aggressiveness_3 | courage_8 | banditness"


class PartyTemplate:
    def __init__(self, id : str, name : str, faction : Faction = fac.no_faction, menu : GameMenu = None, personality = "0"):
        self.id = id
        self.flags = []
        self.name = name
        self.faction = faction
        self.menu = menu
        self.personality = personality
        self.stacks = []
        self.carriesGold = 0
        self.carriesGoods = 0


    def setCarriesGoods(self, carriesGoods : int):
        self.carriesGoods = carriesGoods


    def setCarriesGold(self, carriesGold : int):
        self.carriesGold = carriesGold


    def addStack(self, troop : Troop, min : int, max : int = -1, are_prisoners : bool = False):
        if len(self.stacks) < 6:
            if max < 0:
                max = min
            self.stacks.append((troop.id, min, max, are_prisoners))
        else:
            print("ERROR: Stack limit reached! > pt_" + self.id)


