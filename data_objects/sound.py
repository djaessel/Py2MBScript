# This Python file uses the following encoding: utf-8

from enum import Enum


class SoundFlag(Enum):
    IS_2D                   = "sf_2d"       # = 0x00000001
    LOOPING                 = "sf_looping"  # = 0x00000002
    START_AT_RANDOM_POS     = "sf_start_at_random_pos" # = 0x00000004
    STREAM_FROM_HD          = "sf_stream_from_hd"      # = 0x00000008
    ALWAYS_SEND_VIA_NETWORK = "sf_always_send_via_network" # = 0x00100000

    #PRIORITY_15 = "sf_priority_15"   # = 0x000000f0
    #PRIORITY_14 = "sf_priority_14"   # = 0x000000e0
    #PRIORITY_13 = "sf_priority_13"   # = 0x000000d0
    #PRIORITY_12 = "sf_priority_12"   # = 0x000000c0
    #PRIORITY_11 = "sf_priority_11"   # = 0x000000b0
    #PRIORITY_10 = "sf_priority_10"   # = 0x000000a0
    #PRIORITY_9  = "sf_priority_9"    # = 0x00000090
    #PRIORITY_8  = "sf_priority_8"    # = 0x00000080
    #PRIORITY_7  = "sf_priority_7"    # = 0x00000070
    #PRIORITY_6  = "sf_priority_6"    # = 0x00000060
    #PRIORITY_5  = "sf_priority_5"    # = 0x00000050
    #PRIORITY_4  = "sf_priority_4"    # = 0x00000040
    #PRIORITY_3  = "sf_priority_3"    # = 0x00000030
    #PRIORITY_2  = "sf_priority_2"    # = 0x00000020
    #PRIORITY_1  = "sf_priority_1"    # = 0x00000010

    #VOL_15 = "sf_vol_15"        # = 0x00000f00
    #VOL_14 = "sf_vol_14"        # = 0x00000e00
    #VOL_13 = "sf_vol_13"        # = 0x00000d00
    #VOL_12 = "sf_vol_12"        # = 0x00000c00
    #VOL_11 = "sf_vol_11"        # = 0x00000b00
    #VOL_10 = "sf_vol_10"        # = 0x00000a00
    #VOL_9  = "sf_vol_9"         # = 0x00000900
    #VOL_8  = "sf_vol_8"         # = 0x00000800
    #VOL_7  = "sf_vol_7"         # = 0x00000700
    #VOL_6  = "sf_vol_6"         # = 0x00000600
    #VOL_5  = "sf_vol_5"         # = 0x00000500
    #VOL_4  = "sf_vol_4"         # = 0x00000400
    #VOL_3  = "sf_vol_3"         # = 0x00000300
    #VOL_2  = "sf_vol_2"         # = 0x00000200
    #VOL_1  = "sf_vol_1"         # = 0x00000100



class Sound:
    def __init__(self, id):
        self.id = id
        self.flags = []
        self.files = []
        self.volume = 0
        self.priority = 0


    def set_volume(self, volume : int):
        if volume >= 0 or volume < 16:
            self.volume = volume
        else:
            print(self.id, "invalid volume", volume, "using", self.volume)


    def set_priority(self, priority : int):
        if priority >= 0 or priority < 16:
            self.volume = priority
        else:
            print(self.id, "invalid priority", priority, "using", self.priority)


    def add_file(self, file : str):
        self.files.append(file)


    def add_files(self, files : list):
        self.files.extend(files)


    def add_flag(self, flag : SoundFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : SoundFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : SoundFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]
