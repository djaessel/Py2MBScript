# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")
sys.path.append("../modules/")

from troop import Troop, TroopFlag
import skills as skl
import factions as fac
import test_items as itm
from test_items import IModBit


player = Troop("player", "Player", faction=fac.player_faction, strength=4, agility=4, face_code_1="0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000")
player.wp(15)
player.add_flag(TroopFlag.IS_HERO)
player.add_flag(TroopFlag.UNMOVEABLE_IN_PARTY_WINDOW)

multiplayer_profile_troop_male = Troop("multiplayer_profile_troop_male", "multiplayer_profile_troop_male", faction=fac.commoners, face_code_1="0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000")
multiplayer_profile_troop_male.wp(15)
multiplayer_profile_troop_male.add_flag(TroopFlag.IS_HERO)
multiplayer_profile_troop_male.add_flag(TroopFlag.GUARANTEE_ALL)

multiplayer_profile_troop_male = Troop("multiplayer_profile_troop_female", "multiplayer_profile_troop_female", faction=fac.commoners, face_code_1="0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000")
multiplayer_profile_troop_male.wp(15)
multiplayer_profile_troop_male.add_flag(TroopFlag.IS_HERO)
multiplayer_profile_troop_male.add_flag(TroopFlag.IS_FEMALE)
multiplayer_profile_troop_male.add_flag(TroopFlag.GUARANTEE_ALL)

temp_troop = Troop("temp_troop", "Temp Troop", faction=fac.commoners, face_code_1="0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000")
temp_troop.add_flag(TroopFlag.IS_HERO)
temp_troop.add_skill(skl.inventory_management, 10)

##################################################################
# Troops above this point are hardwired/hardcoded into the game! #
##################################################################

npc1 = Troop("npc1", "Peter", faction=fac.player_faction, strength=10, level=7)
# weapon proficies
npc1.wp(30)
npc1.set_firearm(50)
# flags
npc1.add_flag(TroopFlag.IS_MALE)
npc1.add_flag(TroopFlag.IS_HERO)
npc1.add_flag(TroopFlag.IS_UNKILLABLE)
npc1.add_flag(TroopFlag.GUARANTEE_ALL)
# skills
npc1.add_skill(skl.trade, 10)
# items
npc1.add_item(itm.axe)


npc2 = Troop("npc2", "Sarah", faction=fac.player_faction, level=3)
# weapon proficies
npc2.wpe(30,52,55,100)
npc2.set_firearm(30)
# flags
npc2.add_flag(TroopFlag.IS_FEMALE)
npc2.add_flag(TroopFlag.IS_HERO)
npc2.add_flag(TroopFlag.GUARANTEE_ALL)
# skills
npc2.add_skill(skl.inventory_management, 8)
# items
npc2.add_item(itm.master_shield, [IModBit.CHAMPION, IModBit.GOOD])


looter = Troop("looter", "Looter", faction=fac.commoners)

