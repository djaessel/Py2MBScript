# This Python file uses the following encoding: utf-8

from simple_trigger import SimpleTrigger
from enum import Enum


class ItemFlag(Enum):
    FORCE_ATTACH_LEFT_HAND = "itp_force_attach_left_hand"      # = 0x0000000000000100
    FORCE_ATTACH_RIGHT_HAND = "itp_force_attach_right_hand"     # = 0x0000000000000200
    FORCE_ATTACH_LEFT_FOREARM = "itp_force_attach_left_forearm"   # = 0x0000000000000300
    ATTACH_ARMATURE = "itp_attach_armature"             # = 0x0000000000000f00
    # ATTACHMENT_MASK = "itp_attachment_mask"             # = 0x0000000000000f00

    IS_UNIQUE = "itp_unique"               # = 0x0000000000001000
    ALWAYS_LOOT = "itp_always_loot"          # = 0x0000000000002000
    NO_PARRY = "itp_no_parry"             # = 0x0000000000004000
    IS_DEFAULT_AMMO = "itp_default_ammo"         # = 0x0000000000008000
    IS_MERCHANDISE = "itp_merchandise"          # = 0x0000000000010000
    WOODEN_ATTACK_SOUND = "itp_wooden_attack"        # = 0x0000000000020000
    WOODEN_PARRY_SOUND = "itp_wooden_parry"         # = 0x0000000000040000
    IS_FOOD = "itp_food"                 # = 0x0000000000080000

    CANT_RELOAD_ON_HORSEBACK = "itp_cant_reload_on_horseback" # = 0x0000000000100000
    IS_TWO_HANDED = "itp_two_handed"               # = 0x0000000000200000
    IS_PRIMARY = "itp_primary"                  # = 0x0000000000400000
    IS_SECONDARY = "itp_secondary"                # = 0x0000000000800000
    COVERS_LEGS = "itp_covers_legs"              # = 0x0000000001000000
    DOESNT_COVER_HAIR = "itp_doesnt_cover_hair"        # = 0x0000000001000000
    CAN_PENETRATE_SHIELD = "itp_can_penetrate_shield"     # = 0x0000000001000000
    IS_CONSUMABLE = "itp_consumable"               # = 0x0000000002000000
    HAS_BONUS_AGAINST_SHIELD = "itp_bonus_against_shield"     # = 0x0000000004000000
    PENALTY_WITH_SHIELD = "itp_penalty_with_shield"      # = 0x0000000008000000
    CANT_USE_ON_HORSEBACK = "itp_cant_use_on_horseback"    # = 0x0000000010000000
    IS_CIVILIAN = "itp_civilian"                 # = 0x0000000020000000
    NEXT_ITEM_AS_MELEE = "itp_next_item_as_melee"       # = 0x0000000020000000
    FITS_TO_HEAD = "itp_fit_to_head"              # = 0x0000000040000000
    OFFSET_LANCE = "itp_offset_lance"             # = 0x0000000040000000
    COVERS_HEAD = "itp_covers_head"              # = 0x0000000080000000
    IS_COUCHABLE = "itp_couchable"                # = 0x0000000080000000
    HAS_CRUSH_THROUGH = "itp_crush_through"            # = 0x0000000100000000
    HAS_KNOCK_BACK = "itp_knock_back"               # = 0x0000000200000000 # being used?
    REMOVE_ITEM_ON_USE = "itp_remove_item_on_use"       # = 0x0000000400000000
    IS_UNBALANCED = "itp_unbalanced"               # = 0x0000000800000000

    COVERS_BEARD = "itp_covers_beard"             # = 0x0000001000000000    #remove beard mesh
    NO_PICKUP_FROM_GROUND = "itp_no_pick_up_from_ground"   # = 0x0000002000000000
    CAN_KNOCK_DOWN = "itp_can_knock_down"           # = 0x0000004000000000
    COVERS_HAIR = "itp_covers_hair"              # = 0x0000008000000000    #remove hair mesh for armors only

    FORCE_SHOW_BODY = "itp_force_show_body"          # = 0x0000010000000000 # forces showing body (works on body armor items)
    FORCE_SHOW_LEFT_HAND = "itp_force_show_left_hand"     # = 0x0000020000000000 # forces showing left hand (works on hand armor items)
    FORCE_SHOW_RIGHT_HAND = "itp_force_show_right_hand"    # = 0x0000040000000000 # forces showing right hand (works on hand armor items)
    COVERS_HAIR_PARTIALLY = "itp_covers_hair_partially"    # = 0x0000080000000000

    HAS_EXTRA_PENETRATION = "itp_extra_penetration"        # = 0x0000100000000000
    HAS_BAYONET = "itp_has_bayonet"              # = 0x0000200000000000
    CANT_RELOAD_WHILE_MOVING = "itp_cant_reload_while_moving" # = 0x0000400000000000
    IGNORE_GRAVITY = "itp_ignore_gravity"           # = 0x0000800000000000
    IGNORE_FRICTION = "itp_ignore_friction"          # = 0x0001000000000000
    IS_PIKE = "itp_is_pike"                  # = 0x0002000000000000
    OFFSET_MUSKET = "itp_offset_musket"            # = 0x0004000000000000
    HAS_NO_BLUR = "itp_no_blur"                  # = 0x0008000000000000

    CANT_RELOAD_WHILE_MOVING_MOUNTED = "itp_cant_reload_while_moving_mounted" # = 0x0010000000000000
    HAS_UPPER_STAB = "itp_has_upper_stab"           # = 0x0020000000000000
    DISABLE_AGENT_SOUNDS = "itp_disable_agent_sounds"     # = 0x0040000000000000 #disable agent related sounds, but not voices. useful for animals


class ItemType(Enum):
    HORSE = "itp_type_horse"           # = 0x0000000000000001
    ONE_HANDED_WEAPON = "itp_type_one_handed_wpn"  # = 0x0000000000000002
    TWO_HANDED_WEAPON = "itp_type_two_handed_wpn"  # = 0x0000000000000003
    POLEARM = "itp_type_polearm"         # = 0x0000000000000004
    ARROWS = "itp_type_arrows"          # = 0x0000000000000005
    BOLTS = "itp_type_bolts"           # = 0x0000000000000006
    SHIELD = "itp_type_shield"          # = 0x0000000000000007
    BOW = "itp_type_bow"             # = 0x0000000000000008
    CROSSBOW = "itp_type_crossbow"        # = 0x0000000000000009
    THROWN = "itp_type_thrown"          # = 0x000000000000000a
    GOODS = "itp_type_goods"           # = 0x000000000000000b
    HEAD_ARMOR = "itp_type_head_armor"      # = 0x000000000000000c
    BODY_ARMOR = "itp_type_body_armor"      # = 0x000000000000000d
    FOOT_ARMOR = "itp_type_foot_armor"      # = 0x000000000000000e
    HAND_ARMOR = "itp_type_hand_armor"      # = 0x000000000000000f
    PISTOL = "itp_type_pistol"          # = 0x0000000000000010
    MUSKET = "itp_type_musket"          # = 0x0000000000000011
    BULLETS = "itp_type_bullets"         # = 0x0000000000000012
    ANIMAL = "itp_type_animal"          # = 0x0000000000000013
    BOOK = "itp_type_book"            # = 0x0000000000000014



class ItemMesh:
    id = "ID_NOT_SET"
    modifier = ""

    def __init__(self, id, modifier="0"):
        self.id = id
        self.modifier = modifier



class Item:
    id = "ID_NOT_SET"
    name = ""
    plural_name = ""
    meshes = []
    flags = []
    capabilities = []
    price = 0
    stats = []
    modifiers = []
    triggers = []
    factions = []


    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.plural_name = name
        self.price = price


    def add_trigger(self, trigger : SimpleTrigger):
        if not trigger in self.triggers:
            self.triggers.append(trigger)


    def add_mesh(self, mesh : ItemMesh):
        if not self.contains_mesh(mesh):
            self.meshes.append(mesh)


    def set_type(self, type : ItemType):
        if not self.contains_flags(type.value):
            idx = -1
            for i, flag in enumerate(self.flags):
                if flag.startswith("itp_type"):
                    idx = i
            if idx >= 0:
                del self.flags[idx]
            self.flags.append(type.value)


    def add_flag(self, flag : ItemFlag|ItemType):
        if not self.contains_flags(flag.value):
            self.flags.append(flag.value)


    def add_modifier(self, modifier : str):
        if not self.contains_modifier(modifier):
            self.modifiers.append(modifier)


    def add_capability(self, capability : str):
        if not self.contains_capability(capability):
            self.capabilities.append(capability)


    def add_stat(self, stat : str):
        if not self.contains_stat(stat):
            self.stats.append(stat)


    def allow_in_faction(self, faction : str):
        if not self.contains_faction(faction):
            self.factions.append(faction)


    def contains_stat(self, stat : str):
        contains = False
        for x in self.stats:
            if x == stat:
                contains = True
                break
        return contains


    def contains_flags(self, flag : str):
        contains = False
        for x in self.flags:
            if x == flag:
                contains = True
                break
        return contains


    def contains_modifier(self, modifier : str):
        contains = False
        for x in self.modifiers:
            if x == modifier:
                contains = True
                break
        return contains


    def contains_capability(self, capability : str):
        contains = False
        for x in self.capabilities:
            if x == capability:
                contains = True
                break
        return contains


    def contains_mesh(self, mesh : ItemMesh):
        contains = False
        for x in self.meshes:
            if x.id == mesh.id:
                contains = True
                break
        return contains


    def contains_faction(self, faction : str):
        contains = False
        for x in self.factions:
            if x == faction:
                contains = True
                break
        return contains

