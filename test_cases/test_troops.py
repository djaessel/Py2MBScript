# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from troop import Troop, TroopFlag


npc1 = Troop("npc1", "Peter", "", "fac_player_faction", strength=10, level=7)
npc1.wp(30)
npc1.set_firearm(50)
npc1.add_flag(TroopFlag.IS_MALE)
npc1.add_flag(TroopFlag.GUARANTEE_ARMOR)
npc1.add_flag(TroopFlag.GUARANTEE_BOOTS)
npc1.add_flag(TroopFlag.GUARANTEE_GLOVES)
npc1.add_flag(TroopFlag.GUARANTEE_HELMET)
npc1.add_flag(TroopFlag.GUARANTEE_SHIELD)
npc1.add_flag(TroopFlag.IS_HERO)
npc1.add_flag(TroopFlag.IS_UNKILLABLE)
