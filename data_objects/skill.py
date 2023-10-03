# This Python file uses the following encoding: utf-8

from enum import Enum


class SkillFlag(Enum):
    BASE_AT_STR = "sf_base_att_str"        # = 0x000
    BASE_AT_AGI = "sf_base_att_agi"        # = 0x001
    BASE_AT_INT = "sf_base_att_int"        # = 0x002
    BASE_AT_CHA = "sf_base_att_cha"        # = 0x003
    EFFECTS_PARTY = "sf_effects_party"       # = 0x010
    IS_INACTIVE = "sf_inactive"            # = 0x100



class Skill:
    def __init__(self, id, name, max_level, description=""):
        self.id = id
        self.name = name
        self.max_level = max_level
        self.description = description
        self.flags = []


    def set_description(self, description : str):
        self.description = description


    def add_flag(self, flag : SkillFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : SkillFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : SkillFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]
