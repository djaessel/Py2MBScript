# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from item import Item, ItemMesh, ItemType, ItemFlag
from simple_trigger import SimpleTrigger


axe = Item("my_axe", "My Axe", 512)
axe.set_type(ItemType.ONE_HANDED_WEAPON)

axe.add_mesh(ItemMesh("simple_axe"))
axe.add_mesh(ItemMesh("simple_axe_extra", "extra_thing"))

axe.add_flag(ItemFlag.HAS_CRUSH_THROUGH)
axe.add_flag(ItemFlag.FORCE_ATTACH_LEFT_HAND)
axe.add_flag(ItemFlag.FORCE_ATTACH_RIGHT_HAND)

axe.allow_in_faction("fac_kingdom_1")

triggy1 = SimpleTrigger(16.0)

def coolCode():
    print("Hello World!")

triggy1.codeBlock = coolCode
axe.add_trigger(triggy1)
