# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from troop import Troop, TroopFlag
import test_skills as skl
import test_items as itm
from test_items import IModBit


npc1 = Troop("npc1", "Peter", faction="fac_player_faction", strength=10, level=7)
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


npc2 = Troop("npc2", "Sarah", faction="fac_player_faction", level=3)
# weapon proficies
npc2.wpe(30,52,55,100)
#npc2.set_firearm(50)
# flags
npc2.add_flag(TroopFlag.IS_FEMALE)
npc2.add_flag(TroopFlag.IS_HERO)
npc2.add_flag(TroopFlag.GUARANTEE_ALL)
# skills
#npc2.add_skill(skl.inventory_mgmt, 8)
# items
npc2.add_item(itm.master_shield, [IModBit.CHAMPION, IModBit.GOOD])

