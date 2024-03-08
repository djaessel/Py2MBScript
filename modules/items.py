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





