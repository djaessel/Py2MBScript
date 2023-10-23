# This Python file uses the following encoding: utf-8

from enum import Enum
from trigger import Trigger
from item import Item


class MissionTemplateFlag(Enum):
    ARENA_FIGHT = "mtf_arena_fight"        # = 0x00000001 #identify enemies through team_no
    TEAM_FIGHT = "mtf_team_fight"         # = 0x00000001 #identify enemies through team_no
    BATTLE_MODE = "mtf_battle_mode"        # = 0x00000002 #No inventory access
    COMMIT_CASUALTIES = "mtf_commit_casualties"  # = 0x00000010
    NO_BLOOD = "mtf_no_blood"           # = 0x00000100
    SYNCH_INVENTORY = "mtf_synch_inventory"    # = 0x00010000 #Make a backup of player inventory and restore it at mission end.



class AIFlag(Enum):
    #"aif_group_bits"   # = 0
    #"aif_group_mask"   # = 0xF
    START_ALARMED = "aif_start_alarmed" # = 0x00000010


class SpawnFlag(Enum):
    ENEMY_PARTY = "mtef_enemy_party"        # = 0x00000001
    ALLY_PARTY = "mtef_ally_party"         # = 0x00000002
    SCENE_SOURCE = "mtef_scene_source"       # = 0x00000004
    CONVERSATION_SOURCE = "mtef_conversation_source" # = 0x00000008
    VISITOR_SOURCE = "mtef_visitor_source"     # = 0x00000010
    DEFENDERS = "mtef_defenders"          # = 0x00000040
    ATTACKERS = "mtef_attackers"          # = 0x00000080
    NO_LEADER = "mtef_no_leader"          # = 0x00000100
    NO_COMPANIONS = "mtef_no_companions"      # = 0x00000200
    NO_REGULARS = "mtef_no_regulars"        # = 0x00000400
    TEAM_0 = "mtef_team_0"             # = 0x00001000
    TEAM_1 = "mtef_team_1"             # = 0x00002000
    TEAM_2 = "mtef_team_2"             # = 0x00003000
    TEAM_3 = "mtef_team_3"             # = 0x00004000
    TEAM_4 = "mtef_team_4"             # = 0x00005000
    TEAM_5 = "mtef_team_5"             # = 0x00006000
    TEAM_MEMBER_2 = "mtef_team_member_2"      # = 0x00008000
    INFANTRY_FIRST = "mtef_infantry_first"     # = 0x00010000
    ARCHERS_FIRST = "mtef_archers_first"      # = 0x00020000
    CAVALRY_FIRST = "mtef_cavalry_first"      # = 0x00040000
    NO_AUTO_RESET = "mtef_no_auto_reset"      # = 0x00080000
    REVERSE_ORDER = "mtef_reverse_order"      # = 0x01000000
    USE_EXACT_NUMBER = "mtef_use_exact_number"   # = 0x02000000

    LEADER_ONLY = "mtef_leader_only"        # = mtef_no_companions | mtef_no_regulars
    REGULARS_ONLY = "mtef_regulars_only"      # = mtef_no_companions | mtef_no_leader




class AlterFlag(Enum):
    OVERRIDE_WEAPONS = "af_override_weapons"        # = 0x0000000f
    OVERRIDE_WEAPON_0 = "af_override_weapon_0"       # = 0x00000001
    OVERRIDE_WEAPON_1 = "af_override_weapon_1"       # = 0x00000002
    OVERRIDE_WEAPON_2 = "af_override_weapon_2"       # = 0x00000004
    OVERRIDE_WEAPON_3 = "af_override_weapon_3"       # = 0x00000008
    OVERRIDE_HEAD = "af_override_head"           # = 0x00000010
    OVERRIDE_BODY = "af_override_body"           # = 0x00000020
    #af_override_leg             = 0x00000040
    OVERRIDE_FOOT = "af_override_foot"           # = 0x00000040
    OVERRIDE_GLOVES = "af_override_gloves"         # = 0x00000080
    OVERRIDE_HORSE = "af_override_horse"          # = 0x00000100
    OVERRIDE_FULLHELM = "af_override_fullhelm"       # = 0x00000200

    #af_override_hands           = 0x00000100
    REQUIRE_CIVILIAN = "af_require_civilian"        # = 0x10000000

    #af_override_all_but_horse   = 0x000000ff
    OVERRIDE_ALL_BUT_HORSE = "af_override_all_but_horse"  # = af_override_weapons | af_override_head | af_override_body |af_override_gloves
    OVERRIDE_ALL = "af_override_all"            # = af_override_horse | af_override_all_but_horse
    OVERRIDE_EVERYTHING = "af_override_everything"     # = af_override_all | af_override_foot




class SpawnRecord:
    def __init__(self, entry_no : int, number_of_troops : int, equipment : list = []):
        self.entry_no = entry_no
        self.number_of_troops = number_of_troops
        self.equipment = equipment
        self.alterFlags = []
        self.spawnFlags = []
        self.aiFlags = []


    def add_spawn_flag(self, flag : SpawnFlag):
        if not self.contains_spawn_flag(flag):
            self.spawnFlags.append(flag.value)


    def contains_spawn_flag(self, flag : SpawnFlag):
        contains = False
        for x in self.spawnFlags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_spawn_flag(self, flag : SpawnFlag):
        if self.contains_spawn_flag(flag):
            remi = -1
            for i, f in enumerate(self.spawnFlags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.spawnFlags[remi]


    def add_alter_flag(self, flag : AlterFlag):
        if not self.contains_alter_flag(flag):
            self.alterFlags.append(flag.value)


    def contains_alter_flag(self, flag : AlterFlag):
        contains = False
        for x in self.alterFlags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_alter_flag(self, flag : AlterFlag):
        if self.contains_alter_flag(flag):
            remi = -1
            for i, f in enumerate(self.alterFlags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.alterFlags[remi]


    def add_ai_flag(self, flag : AIFlag):
        if not self.contains_ai_flag(flag):
            self.aiFlags.append(flag.value)


    def contains_ai_flag(self, flag : AIFlag):
        contains = False
        for x in self.aiFlags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_ai_flag(self, flag : AIFlag):
        if self.contains_ai_flag(flag):
            remi = -1
            for i, f in enumerate(self.aiFlags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.aiFlags[remi]


    def addItem(self, item : Item):
        if len(self.equipment) < 8:
            self.equipment.append(item)
        else:
            print("TOO MANY ITEMS! >", self)




class MissionTemplate:
    def __init__(self, id : str, missionType : int = -1, description : str = "{!}no description"):
        self.id = id
        self.flags = []
        self.missionType = missionType
        self.description = description
        self.spawnRecords = []
        self.triggers = []


    def addSpawnRecord(self, record : SpawnRecord):
        self.spawnRecords.append(record)


    def add_trigger(self, trigger : Trigger):
        if not trigger in self.triggers:
            self.triggers.append(trigger)


    def add_flag(self, flag : MissionTemplateFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : MissionTemplateFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : MissionTemplateFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]


