# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from item import Item, ItemMesh, ItemType, ItemFlag, ItemCapability, IModBit
from simple_trigger import SimpleTrigger


axe = Item("my_axe", "My Axe", 512)
axe.set_type(ItemType.ONE_HANDED_WEAPON)

axe.add_mesh(ItemMesh("simple_axe"))
axe.add_mesh(ItemMesh("simple_axe_extra", "extra_thing"))

axe.add_flag(ItemFlag.HAS_CRUSH_THROUGH)
axe.add_flag(ItemFlag.FORCE_ATTACH_LEFT_HAND)
axe.add_flag(ItemFlag.FORCE_ATTACH_RIGHT_HAND)

axe.add_capability(ItemCapability.CARRY_AXE_LEFT_HIP)

axe.add_capability(ItemCapability.HORSEBACK_ONEHANDED_OVERSWING_LEFT)
axe.add_capability(ItemCapability.HORSEBACK_ONEHANDED_OVERSWING_RIGHT)
axe.add_capability(ItemCapability.HORSEBACK_ONEHANDED_THRUST)

axe.add_capability(ItemCapability.ONEHANDED_OVERSWING)
axe.add_capability(ItemCapability.ONEHANDED_TRUST)
axe.add_capability(ItemCapability.ONEHANDED_PARRY_UP)
axe.add_capability(ItemCapability.ONEHANDED_PARRY_FORWARD)
axe.add_capability(ItemCapability.ONEHANDED_PARRY_LEFT)
axe.add_capability(ItemCapability.ONEHANDED_PARRY_RIGHT)

axe.add_capability(ItemCapability.THROW_AXE)

axe.add_modifier(IModBit.CHAMPION)

axe.allow_in_faction("fac_kingdom_1")

triggy1 = SimpleTrigger(16.0)

def coolCode():
    print("Hello World!")

triggy1.codeBlock = coolCode
axe.add_trigger(triggy1)
