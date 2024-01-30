# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from item import Item, ItemMesh, ItemType, ItemFlag, ItemCapability, IModBit, DamageType
from simple_trigger import SimpleTrigger
from MBAxe import MBAxe
from MBShield import MBShield



#["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],
no_item = Item("no_item", "INVALID ITEM", 3)
no_item.add_mesh(ItemMesh("invalid_item"))
no_item.set_type(ItemType.ONE_HANDED_WEAPON)
no_item.add_flag(ItemFlag.IS_PRIMARY)
no_item.add_flag(ItemFlag.IS_SECONDARY)
no_item.add_capability(ItemCapability.LONGSWORD)
no_item.set_weight(1.5)



axe = MBAxe("my_axe", "My Axe", 315)
axe.add_mesh(ItemMesh("battle_ax"))
axe.add_flag(ItemFlag.HAS_CRUSH_THROUGH)
axe.add_flag(ItemFlag.FORCE_ATTACH_RIGHT_HAND)
#axe.add_capability(ItemCapability.THROW_AXE)
axe.add_modifier(IModBit.CHAMPION)
axe.set_abundance(100)
axe.set_difficulty(0)
axe.set_weight(2.5)
axe.set_length(72)
axe.set_swing_damage(27, DamageType.PIERCE)

#axe.allow_in_faction("fac_kingdom_1")

triggy1 = SimpleTrigger(16.0)

def coolCode():
    print("Hello World!")

triggy1.codeBlock = coolCode
#axe.add_trigger(triggy1)


siege_supply = Item("siege_supply", "Siege Supply")


master_shield = MBShield("master_shield", "Master Shield", 831)
master_shield.set_abundance(9)
master_shield.add_flag(ItemFlag.IS_UNIQUE)
master_shield.add_mesh(ItemMesh("arena_shield_green"))
master_shield.set_hit_points(399)
master_shield.set_body_armor(10)
master_shield.set_difficulty(10)
master_shield.set_height(200)
master_shield.set_weight(5)
master_shield.set_width(75)






