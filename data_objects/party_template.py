# This Python file uses the following encoding: utf-8

from enum import Enum
from troop import Troop
from faction import Faction
from game_menu import GameMenu
from mapicon import MapIcon

import factions as fac



class PartyFlag(Enum):
    #ICON_MASK = "pf_icon_mask"                # = 0x000000ff
    IS_DISABLED = "pf_disabled"                 # = 0x00000100
    IS_SHIP = "pf_is_ship"                  # = 0x00000200
    IS_STATIC = "pf_is_static"                # = 0x00000400

    LABEL_SMALL = "pf_label_small"              # = 0x00000000
    LABEL_MEDIUM = "pf_label_medium"             # = 0x00001000
    LABEL_LARGE = "pf_label_large"              # = 0x00002000

    IS_ALWAYS_VISIBLE = "pf_always_visible"           # = 0x00004000
    HAS_DEFAULT_BEHAVIOR = "pf_default_behavior"         # = 0x00010000
    AUTO_REMOVE_IN_TOWN = "pf_auto_remove_in_town"      # = 0x00020000
    IS_QUEST_PARTY = "pf_quest_party"              # = 0x00040000
    HAS_NO_LABEL = "pf_no_label"                 # = 0x00080000
    LIMIT_MEMBERS = "pf_limit_members"            # = 0x00100000
    HIDE_DEFENDERS = "pf_hide_defenders"           # = 0x00200000
    SHOW_FACTION = "pf_show_faction"             # = 0x00400000
    #IS_HIDDEN = "pf_is_hidden"               # = 0x01000000 #used in the engine, do not overwrite this flag
    DONT_ATTACK_CIVILIANS = "pf_dont_attack_civilians"    # = 0x02000000
    IS_CIVILIAN = "pf_civilian"                 # = 0x04000000

    IS_TOWN = "pf_town"
    IS_CASTLE = "pf_castle"
    IS_VILLAGE = "pf_village"


class PartyPersonality(Enum):
    SOLDIER = "soldier_personality"  # = "aggressiveness_8 | courage_9"
    MERCHANT = "merchant_personality" # = "aggressiveness_0 | courage_7"
    ESCORTED_MERCHANT = "escorted_merchant_personality" # = "aggressiveness_0 | courage_11"
    BANDIT = "bandit_personality"   # = "aggressiveness_3 | courage_8 | banditness"


class PartyTemplate:
    def __init__(self, id : str, name : str, faction : Faction = fac.no_faction, menu : GameMenu = None, personality = "0"):
        self.id = id
        self.flags = []
        self.icon = None
        self.name = name
        self.faction = faction
        self.menu = menu
        self.personality = personality
        self.stacks = []
        self.carriesGold = 0
        self.carriesGoods = 0


    def set_icon(self, icon : MapIcon):
        self.icon = icon


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


    def add_flag(self, flag : PartyFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : PartyFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : PartyFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]
