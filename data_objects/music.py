# This Python file uses the following encoding: utf-8

from enum import Enum


class TrackFlag(Enum):
    CULTURE_1 = "mtf_culture_1"                         # = 0x00000001
    CULTURE_2 = "mtf_culture_2"                         # = 0x00000002
    CULTURE_3 = "mtf_culture_3"                         # = 0x00000004
    CULTURE_4 = "mtf_culture_4"                         # = 0x00000008
    CULTURE_5 = "mtf_culture_5"                         # = 0x00000010
    CULTURE_6 = "mtf_culture_6"                         # = 0x00000020
    CULTURE_ALL = "mtf_culture_all"                       # = 0x0000003F

    LOOPING = "mtf_looping"                           # = 0x00000040
    START_IMMEDIATELY = "mtf_start_immediately"                 # = 0x00000080
    PERSIST_UNTIL_FINISHED = "mtf_persist_until_finished"            # = 0x00000100

    SIT_TAVERN = "mtf_sit_tavern"                        # = 0x00000200
    SIT_FIGHT = "mtf_sit_fight"                         # = 0x00000400
    SIT_MULTIPLAYER_FIGHT = "mtf_sit_multiplayer_fight"             # = 0x00000800
    SIT_AMBUSHED = "mtf_sit_ambushed"                      # = 0x00001000
    SIT_TOWN = "mtf_sit_town"                          # = 0x00002000
    SIT_TOWN_INFILTRATE = "mtf_sit_town_infiltrate"               # = 0x00004000
    SIT_KILLED = "mtf_sit_killed"                        # = 0x00008000
    SIT_TRAVEL = "mtf_sit_travel"                        # = 0x00010000
    SIT_ARENA = "mtf_sit_arena"                         # = 0x00020000
    SIT_SIEGE = "mtf_sit_siege"                         # = 0x00040000
    SIT_NIGHT = "mtf_sit_night"                         # = 0x00080000
    SIT_DAY = "mtf_sit_day"                           # = 0x00100000
    SIT_ENCOUNTER_HOSTILE = "mtf_sit_encounter_hostile"             # = 0x00200000
    SIT_MAIN_TITLE = "mtf_sit_main_title"                    # = 0x00400000
    SIT_VICTORIOUS = "mtf_sit_victorious"                    # = 0x00800000
    SIT_FEAST = "mtf_sit_feast"                         # = 0x01000000

    MODULE_TRACK = "mtf_module_track"                      # = 0x10000000 ##set this flag for tracks placed under module folder



class MusicTrack:
    def __init__(self, id : str, file : str):
        self.id = id
        self.file = file
        self.flags = []
        self.continue_flags = []


    def add_flag(self, flag : TrackFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : TrackFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : TrackFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]


    def add_continue_flag(self, flag : TrackFlag):
        if not self.contains_continue_flag(flag):
            self.continue_flags.append(flag.value)


    def contains_continue_flag(self, flag : TrackFlag):
        contains = False
        for x in self.continue_flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_continue_flag(self, flag : TrackFlag):
        if self.contains_continue_flag(flag):
            remi = -1
            for i, f in enumerate(self.continue_flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.continue_flags[remi]


