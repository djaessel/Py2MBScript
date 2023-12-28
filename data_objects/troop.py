# This Python file uses the following encoding: utf-8

import sys
sys.path.append("./test_cases/")

from enum import Enum
from skill import Skill
from item import Item, IModBit

import skills as skl
from test_items import *

class TroopFlag(Enum):
    SKIN1 = "tf_male"          # = 0
    SKIN2 = "tf_female"        # = 1
    SKIN3 = "2"
    SKIN4 = "3"
    SKIN5 = "4"
    SKIN6 = "5"
    SKIN7 = "6"
    SKIN8 = "7"
    SKIN9 = "8"
    SKIN10 = "9"
    SKIN11 = "10"
    SKIN12 = "11"
    SKIN13 = "12"
    SKIN14 = "13"
    SKIN15 = "14"
    SKIN16 = "15"
    IS_MALE = SKIN1
    IS_FEMALE = SKIN2
    # "tf_undead"        # = 2
    # "troop_type_mask"  # = 0x0000000f

    IS_HERO = "tf_hero"             # = 0x00000010
    IS_INACTIVE = "tf_inactive"         # = 0x00000020
    IS_UNKILLABLE = "tf_unkillable"       # = 0x00000040
    ALWAYS_FALL_DEAD = "tf_allways_fall_dead" # = 0x00000080
    NO_CAPTURE_ALIVE = "tf_no_capture_alive" # = 0x00000100
    IS_MOUNTED = "tf_mounted"          # = 0x00000400 #Troop's movement speed on map is determined by riding skill.
    IS_MERCHANT = "tf_is_merchant"      # = 0x00001000 #When set, troop does not equip stuff he owns
    HAS_RANDOM_FACE = "tf_randomize_face"   # = 0x00008000 #randomize face at the beginning of the game.

    GUARANTEE_BOOTS = "tf_guarantee_boots"           # = 0x00100000
    GUARANTEE_ARMOR = "tf_guarantee_armor"           # = 0x00200000
    GUARANTEE_HELMET = "tf_guarantee_helmet"          # = 0x00400000
    GUARANTEE_GLOVES = "tf_guarantee_gloves"          # = 0x00800000
    GUARANTEE_HORSE = "tf_guarantee_horse"           # = 0x01000000
    GUARANTEE_SHIELD = "tf_guarantee_shield"          # = 0x02000000
    GUARANTEE_RANGED = "tf_guarantee_ranged"          # = 0x04000000
    GUARANTEE_POLEARM = "tf_guarantee_polearm"         # = 0x08000000

    GUARANTEE_ALL = "tf_guarantee_all"

    UNMOVEABLE_IN_PARTY_WINDOW = "tf_unmoveable_in_party_window" # = 0x10000000





class Troop:
    #  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
    #  2) Troop name (string).
    #  3) Plural troop name (string).
    #  4) Troop flags (int). See header_troops.py for a list of available flags
    #  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
    #  6) Reserved (int). Put constant "reserved" or 0.
    #  7) Faction (int)
    #  8) Inventory (list): Must be a list of items
    #  9) Attributes (int): Example usage:
    #           str_6|agi_6|int_4|cha_5|level(5)
    # 10) Weapon proficiencies (int): Example usage:
    #           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
    #     The function wp(x) will create random weapon proficiencies close to value x.
    #     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
    #           wp_archery(160) | wp(60)
    # 11) Skills (int): See header_skills.py to see a list of skills. Example:
    #           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
    # 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
    # 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
    #     The game will create random faces between Face code 1 and face code 2 for generated troops
    # 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations

    def __init__(self, id, name, plural_name="", faction="", strength=7, agility=5, intelligence=4, charisma=4, level=1, face_code_1="man_face_middle_1", face_code_2="man_face_middle_1", troop_image=""):
        self.id = id
        self.name = name

        if len(plural_name) == 0:
            self.plural_name = self.name
        else:
            self.plural_name = plural_name

        self.faction = faction

        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.charisma = charisma
        self.level = level

        self.face1 = face_code_1
        self.face2 = face_code_2
        self.image = troop_image

        self.inventory = []
        self.skills = []
        self.flags = []

        self.reserved = "reserved"
        self.scene = "no_scene"

        self.one_handed = 0
        self.two_handed = 0
        self.polearm = 0
        self.archery = 0
        self.crossbow = 0
        self.throwing = 0
        self.firearm = 0

        self.add_skill(skl.riding, 1)
        self.add_skill(skl.trade, 2)
        self.add_skill(skl.inventory_management, 2)
        self.add_skill(skl.prisoner_mgmt, 1)
        self.add_skill(skl.leadership, 1)


    def get_attributes(self):
        re = "str_" + str(self.strength)
        re += "|agi_" + str(self.agility)
        re += "|int_" + str(self.intelligence)
        re += "|cha_" + str(self.charisma)
        re += "|level(" + str(self.level) + ")"
        return re


    def get_weapon_proficies(self):
        if self.one_handed == self.two_handed == self.polearm == self.archery == self.throwing == self.crossbow:
            re = "wp(" + str(self.one_handed) + ")"
        elif self.one_handed == self.two_handed == self.polearm:
            re = "wpe(" + str(self.one_handed) + "," + str(self.archery) + "," + str(self.crossbow) + "," + str(self.throwing) + ")"
        else:
            re = "wpex(" + str(self.one_handed) + "," + str(self.two_handed) + "," + str(self.polearm) + "," + str(self.archery) + "," + str(self.crossbow) + "," + str(self.throwing) + ")"

        if self.firearm > 0:
            re += "|wp_firearm(" + str(self.firearm) + ")"

        return re


    def wp(self, x : int):
        self.one_handed = x
        self.two_handed = x
        self.polearm = x
        self.archery = x
        self.crossbow = x
        self.throwing = x


    def wpe(self, melee : int, a : int, c : int, t : int):
        self.one_handed = melee
        self.two_handed = melee
        self.polearm = melee
        self.archery = a
        self.crossbow = c
        self.throwing = t


    def wpex(self, o : int, w : int, p : int, a : int, c : int, t : int):
        self.one_handed = o
        self.two_handed = w
        self.polearm = p
        self.archery = a
        self.crossbow = c
        self.throwing = t


    def set_firearm(self, x : int):
        self.firearm = x


    def set_scene_code(self, scene : str):
        self.scene = scene


    def set_reserved(self, reserved : str):
        self.reserved = reserved


    def set_face1(self, face_code : str):
        self.face1 = face_code


    def set_face2(self, face_code : str):
        self.face2 = face_code


    def add_flag(self, flag : TroopFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : TroopFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : TroopFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]


    def add_skill(self, skill : Skill, val : int = 1, remove_alt : bool = True):
        if skill.max_level >= val and val > 0:
            if remove_alt:
                contains, found_idx = self.contains_skill(skill)
                if contains:
                    del self.skills[found_idx]
            contains, _ = self.contains_skill(skill, val)
            if not contains:
                skill_knows = "knows_" + skill.id + "_" + str(val)
                self.skills.append(skill_knows)
        else:
            print("trp_" + self.id, ": Invalid skill level:", val, "-> Max Level:", skill.max_level)



    def contains_skill(self, skill : Skill, val : int = -1):
        contains = False
        found_skill_idx = -1
        skill_knows = "knowns_" + skill.id + "_"
        if val > 0:
            skill_knows += str(val)
        for i, x in enumerate(self.skills):
            if (val > 0 and x == skill_knows) or x.startswith(skill_knows):
                contains = True
                found_skill_idx = i
                break
        return contains, found_skill_idx


    def remove_skill(self, skill : Skill):
        contains, _ = self.contains_skill(skill)
        if contains:
            remi = -1
            skill_knows = "knowns_" + skill.id + "_"
            for i, s in enumerate(self.skills):
                if s.startswith(skill_knows):
                    remi = i
                    break
            if remi >= 0:
                del self.skills[remi]


    def add_item(self, item : Item, modbits : list[IModBit] = None):
        wholex = "0"
        if modbits != None:
            if len(modbits) > 0:
                wholex = ""
                for modbit in modbits:
                    wholex += modbit.value + "|"
                wholex = wholex.rstrip('|')
        self.inventory.append((item.id, wholex))


    def remove_item(self, item : Item):
        remi = -1
        for i, itemx in enumerate(self.inventory):
            if itemx[0] == item.id:
                remi = i
                break
        if remi >= 0:
            del self.inventory[remi]




#            troop_has_item_equipped         = 151 # (troop_has_item_equipped,<troop_id>,<item_id>),
#            troop_is_mounted                = 152 # (troop_is_mounted,<troop_id>),
#            troop_is_guarantee_ranged       = 153 # (troop_is_guarantee_ranged, <troop_id>),
#            troop_is_guarantee_horse        = 154 # (troop_is_guarantee_horse, <troop_id>),

#            troop_set_slot                  = 500 # (troop_set_slot,<troop_id>,<slot_no>,<value>),
#            troop_get_slot                  = 520 # (troop_get_slot,<destination>,<troop_id>,<slot_no>),
#            troop_slot_eq                   = 540 # (troop_slot_eq,<troop_id>,<slot_no>,<value>),
#            troop_slot_ge                   = 560 # (troop_slot_ge,<troop_id>,<slot_no>,<value>),

#            troop_set_note_available        = 1095 # (troop_set_note_available, <troop_id>, <value>), #1 = available, 0 = not available

#            troop_join                      = 1203 # (troop_join,<troop_id>),
#            troop_join_as_prisoner          = 1204 # (troop_join_as_prisoner,<troop_id>),


#            troop_set_name                         = 1501   # (troop_set_name, <troop_id>, <string_no>),
#            troop_set_plural_name                  = 1502   # (troop_set_plural_name, <troop_id>, <string_no>),
#            troop_set_face_key_from_current_profile= 1503   # (troop_set_face_key_from_current_profile, <troop_id>),
#            troop_set_type                         = 1505	# (troop_set_type,<troop_id>,<gender>),
#            troop_get_type                         = 1506   # (troop_get_type,<destination>,<troop_id>),
#            troop_is_hero                          = 1507   # (troop_is_hero,<troop_id>),
#            troop_is_wounded                       = 1508   # (troop_is_wounded,<troop_id>), #only for heroes!
#            troop_set_auto_equip                   = 1509   # (troop_set_auto_equip,<troop_id>,<value>),#disables otr enables auto-equipping
#            troop_ensure_inventory_space           = 1510	# (troop_ensure_inventory_space,<troop_id>,<value>),
#            troop_sort_inventory                   = 1511	# (troop_sort_inventory,<troop_id>),
#            troop_add_merchandise                  = 1512	# (troop_add_merchandise,<troop_id>,<item_type_id>,<value>),
#            troop_add_merchandise_with_faction     = 1513	# (troop_add_merchandise_with_faction,<troop_id>,<faction_id>,<item_type_id>,<value>), #faction_id is given to check if troop is eligible to produce that item
#            troop_get_xp                           = 1515   # (troop_get_xp, <destination>, <troop_id>),
#            troop_get_class                        = 1516   # (troop_get_class, <destination>, <troop_id>),
#            troop_set_class                        = 1517 # (troop_set_class, <troop_id>, <value>),

#            troop_raise_attribute                  = 1520	# (troop_raise_attribute,<troop_id>,<attribute_id>,<value>),
#            troop_raise_skill                      = 1521	# (troop_raise_skill,<troop_id>,<skill_id>,<value>),
#            troop_raise_proficiency                = 1522	# (troop_raise_proficiency,<troop_id>,<proficiency_no>,<value>),
#            troop_raise_proficiency_linear         = 1523	# raises weapon proficiencies linearly without being limited by weapon master skill
                                                            # (troop_raise_proficiency,<troop_id>,<proficiency_no>,<value>),

#            troop_add_proficiency_points           = 1525   # (troop_add_proficiency_points,<troop_id>,<value>),
#            troop_add_gold                         = 1528	# (troop_add_gold,<troop_id>,<value>),
#            troop_remove_gold                      = 1529	# (troop_remove_gold,<troop_id>,<value>),
#            troop_add_item                         = 1530	# (troop_add_item,<troop_id>,<item_id>,[modifier]),
#            troop_remove_item                      = 1531	# (troop_remove_item,<troop_id>,<item_id>),
#            troop_clear_inventory                  = 1532	# (troop_clear_inventory,<troop_id>),
#            troop_equip_items                      = 1533   # (troop_equip_items,<troop_id>), #equips the items in the inventory automatically
#            troop_inventory_slot_set_item_amount   = 1534   # (troop_inventory_slot_set_item_amount,<troop_id>,<inventory_slot_no>,<value>),
#            troop_inventory_slot_get_item_amount   = 1537   # (troop_inventory_slot_get_item_amount,<destination>,<troop_id>,<inventory_slot_no>),
#            troop_inventory_slot_get_item_max_amount = 1538  # (troop_inventory_slot_get_item_max_amount,<destination>,<troop_id>,<inventory_slot_no>),

#            troop_add_items                        = 1535	# (troop_add_items,<troop_id>,<item_id>,<number>),
#            troop_remove_items                     = 1536	# puts cost of items to reg0
                                                            # (troop_remove_items,<troop_id>,<item_id>,<number>),
#            troop_loot_troop                       = 1539	# (troop_loot_troop,<target_troop>,<source_troop_id>,<probability>),

#            troop_get_inventory_capacity           = 1540	# (troop_get_inventory_capacity,<destination>,<troop_id>),
#            troop_get_inventory_slot               = 1541	# (troop_get_inventory_slot,<destination>,<troop_id>,<inventory_slot_no>),
#            troop_get_inventory_slot_modifier      = 1542	# (troop_get_inventory_slot_modifier,<destination>,<troop_id>,<inventory_slot_no>),
#            troop_set_inventory_slot               = 1543	# (troop_set_inventory_slot,<troop_id>,<inventory_slot_no>,<value>),
#            troop_set_inventory_slot_modifier      = 1544	# (troop_set_inventory_slot_modifier,<troop_id>,<inventory_slot_no>,<value>),
#            troop_set_faction                      = 1550 # (troop_set_faction,<troop_id>,<faction_id>),
#            troop_set_age                          = 1555 # (troop_set_age, <troop_id>, <age_slider_pos>),  #Enter a value between 0..100
#            troop_set_health                       = 1560	# (troop_set_health,<troop_id>,<relative health (0-100)>),

#            troop_get_upgrade_troop                = 1561   # (troop_get_upgrade_troop,<destination>,<troop_id>,<upgrade_path>), #upgrade_path can be: 0 = get first node, 1 = get second node (returns -1 if not available)

#            troop_set_face_keys                   = 2751 # (troop_set_face_keys, <troop_no>, <string_no>, [<alt>]), #Sets <troop_no>'s face keys from string. if [<alt>] is non-zero the second pair of face keys is set.

