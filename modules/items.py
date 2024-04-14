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
no_item.set_type(ItemType.ONE_HANDED_WPN)
no_item.add_flag(ItemFlag.IS_PRIMARY)
no_item.add_flag(ItemFlag.IS_SECONDARY)
no_item.add_capability(ItemCapability.ONEHANDED_TRUST)
no_item.add_capability(ItemCapability.ONEHANDED_OVERSWING)
no_item.add_capability(ItemCapability.ONEHANDED_SLASHRIGHT)
no_item.add_capability(ItemCapability.ONEHANDED_SLASHLEFT)
no_item.add_capability(ItemCapability.HORSEBACK_ONEHANDED_SLASHRIGHT)
no_item.add_capability(ItemCapability.HORSEBACK_ONEHANDED_SLASHLEFT)
no_item.add_capability(ItemCapability.ONEHANDED_PARRY_FORWARD)
no_item.add_capability(ItemCapability.ONEHANDED_PARRY_UP)
no_item.add_capability(ItemCapability.ONEHANDED_PARRY_RIGHT)
no_item.add_capability(ItemCapability.ONEHANDED_PARRY_LEFT)
no_item.add_capability(ItemCapability.FORCE_64_BITS)
no_item.set_weight(1.5)


club = Item("club", "Club")
club.add_mesh(ItemMesh("club"))

military_hammer = Item("military_hammer", "Military Hammer")
military_hammer.add_mesh(ItemMesh("military_hammer"))

iron_hammer = Item("iron_hammer", "Iron Hammer")
iron_hammer.add_mesh(ItemMesh("iron_hammer"))


items_end = Item("items_end", "Items End")
items_end.add_mesh(ItemMesh("invalid_item")) # bug with openBrf Lib

