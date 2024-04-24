# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from item import Item, ItemMesh, ItemType, ItemFlag, ItemCapability, IModBit, DamageType
from simple_trigger import SimpleTrigger



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

# - - -

club = Item("club", "Club", 11)
club.add_mesh(ItemMesh("club"))
club.set_type(ItemType.ONE_HANDED_WPN)
club.add_flag(ItemFlag.IS_MERCHANDISE)
club.add_flag(ItemFlag.WOODEN_ATTACK_SOUND)
club.add_flag(ItemFlag.WOODEN_PARRY_SOUND)
club.add_flag(ItemFlag.IS_PRIMARY)
club.add_flag(ItemFlag.CAN_KNOCK_DOWN)
club.add_capability(ItemCapability.ONEHANDED_OVERSWING)
club.add_capability(ItemCapability.ONEHANDED_SLASHRIGHT)
club.add_capability(ItemCapability.ONEHANDED_SLASHLEFT)
club.add_capability(ItemCapability.HORSEBACK_ONEHANDED_SLASHRIGHT)
club.add_capability(ItemCapability.HORSEBACK_ONEHANDED_SLASHLEFT)
club.add_capability(ItemCapability.ONEHANDED_PARRY_FORWARD)
club.add_capability(ItemCapability.ONEHANDED_PARRY_UP)
club.add_capability(ItemCapability.ONEHANDED_PARRY_RIGHT)
club.add_capability(ItemCapability.ONEHANDED_PARRY_LEFT)
club.add_capability(ItemCapability.FORCE_64_BITS)
club.set_weight(2.5)
club.set_speed_rating(98)
club.set_weapon_length(70)
club.set_swing_damage(20, 2)


military_hammer = Item("military_hammer", "Military Hammer", 317)
military_hammer.add_mesh(ItemMesh("military_hammer"))
military_hammer.set_type(ItemType.ONE_HANDED_WPN)
military_hammer.add_flag(ItemFlag.IS_MERCHANDISE)
military_hammer.add_flag(ItemFlag.WOODEN_PARRY_SOUND)
military_hammer.add_flag(ItemFlag.IS_PRIMARY)
military_hammer.add_capability(ItemCapability.ONEHANDED_OVERSWING)
military_hammer.add_capability(ItemCapability.ONEHANDED_SLASHRIGHT)
military_hammer.add_capability(ItemCapability.ONEHANDED_SLASHLEFT)
military_hammer.add_capability(ItemCapability.HORSEBACK_ONEHANDED_SLASHRIGHT)
military_hammer.add_capability(ItemCapability.HORSEBACK_ONEHANDED_SLASHLEFT)
military_hammer.add_capability(ItemCapability.ONEHANDED_PARRY_FORWARD)
military_hammer.add_capability(ItemCapability.ONEHANDED_PARRY_UP)
military_hammer.add_capability(ItemCapability.ONEHANDED_PARRY_RIGHT)
military_hammer.add_capability(ItemCapability.ONEHANDED_PARRY_LEFT)
military_hammer.add_capability(ItemCapability.CARRY_MACE_LEFT_HIP)
military_hammer.add_capability(ItemCapability.FORCE_64_BITS)
military_hammer.set_weight(2)
military_hammer.set_speed_rating(95)
military_hammer.set_weapon_length(70)
military_hammer.set_swing_damage(31, 2)


tools = Item("tools", "Tools", 410)
tools.add_mesh(ItemMesh("iron_hammer"))
tools.add_mesh(ItemMesh("iron_hammer_new", ItemMesh.ixmesh_inventory))
tools.set_type(ItemType.GOODS)
tools.add_flag(ItemFlag.IS_MERCHANDISE)
tools.set_weight(50)
tools.set_abundance(90)





# - - -

items_end = Item("items_end", "Items End")
items_end.add_mesh(ItemMesh("invalid_item")) # bug with openBrf Lib

