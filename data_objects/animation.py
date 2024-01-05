# This Python file uses the following encoding: utf-8

from enum import Enum


class AnimationSequenceFlag(Enum):
    BLEND_IN_0 = "arf_blend_in_0"              # = 0x00000001
    BLEND_IN_1 = "arf_blend_in_1"              # = 0x00000002
    BLEND_IN_2 = "arf_blend_in_2"              # = 0x00000003
    BLEND_IN_3 = "arf_blend_in_3"              # = 0x00000004
    BLEND_IN_4 = "arf_blend_in_4"              # = 0x00000005
    BLEND_IN_5 = "arf_blend_in_5"              # = 0x00000006
    BLEND_IN_6 = "arf_blend_in_6"              # = 0x00000007
    BLEND_IN_7 = "arf_blend_in_7"              # = 0x00000008
    BLEND_IN_8 = "arf_blend_in_8"              # = 0x00000009
    BLEND_IN_9 = "arf_blend_in_9"              # = 0x0000000a
    BLEND_IN_10 = "arf_blend_in_10"             # = 0x0000000b
    BLEND_IN_11 = "arf_blend_in_11"             # = 0x0000000c
    BLEND_IN_12 = "arf_blend_in_12"             # = 0x0000000d
    BLEND_IN_13 = "arf_blend_in_13"             # = 0x0000000e
    BLEND_IN_14 = "arf_blend_in_14"             # = 0x0000000f
    BLEND_IN_15 = "arf_blend_in_15"             # = 0x00000010
    BLEND_IN_16 = "arf_blend_in_16"             # = 0x00000011
    BLEND_IN_17 = "arf_blend_in_17"             # = 0x00000012
    BLEND_IN_18 = "arf_blend_in_18"             # = 0x00000013
    BLEND_IN_19 = "arf_blend_in_19"             # = 0x00000014
    BLEND_IN_20 = "arf_blend_in_20"             # = 0x00000015
    BLEND_IN_21 = "arf_blend_in_21"             # = 0x00000016
    BLEND_IN_22 = "arf_blend_in_22"             # = 0x00000017
    BLEND_IN_23 = "arf_blend_in_23"             # = 0x00000018
    BLEND_IN_24 = "arf_blend_in_24"             # = 0x00000019
    BLEND_IN_25 = "arf_blend_in_25"             # = 0x0000001a
    BLEND_IN_26 = "arf_blend_in_26"             # = 0x0000001b
    BLEND_IN_27 = "arf_blend_in_27"             # = 0x0000001c
    BLEND_IN_28 = "arf_blend_in_28"             # = 0x0000001d
    BLEND_IN_29 = "arf_blend_in_29"             # = 0x0000001e
    BLEND_IN_30 = "arf_blend_in_30"             # = 0x0000001f
    BLEND_IN_31 = "arf_blend_in_31"             # = 0x00000020
    BLEND_IN_32 = "arf_blend_in_32"             # = 0x00000021
    BLEND_IN_48 = "arf_blend_in_48"             # = 0x00000031
    BLEND_IN_64 = "arf_blend_in_64"             # = 0x00000041
    BLEND_IN_128 = "arf_blend_in_128"            # = 0x00000081
    BLEND_IN_254 = "arf_blend_in_254"            # = 0x000000ff

    BLEND_IN_DEFENSE = "blend_in_defense" # = arf_blend_in_3
    BLEND_IN_READY = "blend_in_ready"  # = arf_blend_in_6
    BLEND_IN_RELEASE = "blend_in_release" # = arf_blend_in_5
    BLEND_IN_PARRY = "blend_in_parry" # = arf_blend_in_5
    BLEND_IN_PARRIED = "blend_in_parried" # = arf_blend_in_3

    BLEND_IN_WALK = "blend_in_walk" # = arf_blend_in_3
    BLEND_IN_CONTINUE = "blend_in_continue" # = arf_blend_in_1


    MAKE_WALK_SOUND = "arf_make_walk_sound"         # = 0x00000100
    MAKE_CUSTOM_SOUND = "arf_make_custom_sound"       # = 0x00000200

    TWO_HANDED_BLADE = "arf_two_handed_blade"        # = 0x01000000
    LANCER = "arf_lancer"                  # = 0x02000000
    STICK_ITEM_TO_LEFT_HAND = "arf_stick_item_to_left_hand" # = 0x04000000
    CYCLIC = "arf_cyclic"                  # = 0x10000000

    USE_WALK_PROGRESS = "arf_use_walk_progress"       # = 0x20000000
    USE_STAND_PROGRESS = "arf_use_stand_progress"      # = 0x40000000
    USE_INV_WALK_PROGRESS = "arf_use_inv_walk_progress"   # = 0x80000000



class AnimationMasterFlag(Enum):
    PRIORITY_JUMP = "amf_priority_jump"          # = 2
    PRIORITY_RIDE = "amf_priority_ride"          # = 2
    PRIORITY_CONTINUE = "amf_priority_continue"      # = 1
    PRIORITY_ATTACK = "amf_priority_attack"        # = 10
    PRIORITY_CANCEL = "amf_priority_cancel"        # = 12
    PRIORITY_DEFEND = "amf_priority_defend"        # = 14
    PRIORITY_DEFEND_PARRY = "amf_priority_defend_parry"  # = amf_priority_defend + 1
    PRIORITY_THROW = "amf_priority_throw"         # = amf_priority_defend + 1
    PRIORITY_BLOCKED = "amf_priority_blocked"       # = amf_priority_defend_parry
    PRIORITY_PARRIED = "amf_priority_parried"       # = amf_priority_defend_parry
    PRIORITY_KICK = "amf_priority_kick"          # = 33
    PRIORITY_JUMP_END = "amf_priority_jump_end"      # = 33
    PRIORITY_RELOAD = "amf_priority_reload"        # = 60
    PRIORITY_MOUNT = "amf_priority_mount"         # = 64
    PRIORITY_EQUIP = "amf_priority_equip"         # = 70
    PRIORITY_REAR = "amf_priority_rear"          # = 74
    PRIORITY_STRIKED = "amf_priority_striked"       # = 80
    PRIORITY_FALL_FROM_HORSE = "amf_priority_fall_from_horse" # = 81
    PRIORITY_DIE = "amf_priority_die"           # = 95

    RIDER_ROT_BOW = "amf_rider_rot_bow"                         # = 0x00001000
    RIDER_ROT_THROW = "amf_rider_rot_throw"                       # = 0x00002000
    RIDER_ROT_CROSSBOW = "amf_rider_rot_crossbow"                    # = 0x00003000
    RIDER_ROT_PISTOL = "amf_rider_rot_pistol"                      # = 0x00004000
    RIDER_ROT_OVERSWING = "amf_rider_rot_overswing"                   # = 0x00005000
    RIDER_ROT_THRUST = "amf_rider_rot_thrust"                      # = 0x00006000
    RIDER_ROT_SWING_RIGHT = "amf_rider_rot_swing_right"                 # = 0x00007000
    RIDER_ROT_SWING_LEFT = "amf_rider_rot_swing_left"                  # = 0x00008000
    RIDER_ROT_COUCHED_LANCE = "amf_rider_rot_couched_lance"               # = 0x00009000
    RIDER_ROT_SHIELD = "amf_rider_rot_shield"                      # = 0x0000a000
    RIDER_ROT_DEFEND = "amf_rider_rot_defend"                      # = 0x0000b000

    START_INSTANTLY = "amf_start_instantly"                       # = 0x00010000
    USE_CYCLE_PERIOD = "amf_use_cycle_period"                      # = 0x00100000
    USE_WEAPON_SPEED = "amf_use_weapon_speed"                      # = 0x00200000
    USE_DEFEND_SPEED = "amf_use_defend_speed"                      # = 0x00400000
    ACCURATE_BODY = "amf_accurate_body"                         # = 0x00800000
    CLIENT_PREDICTION = "amf_client_prediction"                     # = 0x01000000
    PLAY = "amf_play"                                  # = 0x02000000
    KEEP = "amf_keep"                                     # = 0x04000000
    RESTART = "amf_restart"                               # = 0x08000000 # restart animation even if it is the current animation
    HIDE_WEAPON = "amf_hide_weapon"                           # = 0x10000000
    CLIENT_OWNER_PREDICTION = "amf_client_owner_prediction"               # = 0x20000000
    USE_INERTIA = "amf_use_inertia"                           # = 0x40000000
    CONTINUE_TO_NEXT = "amf_continue_to_next"                      # = 0x80000000



class AnimationFlag(Enum):
    SYNC_WITH_HORSE = "acf_synch_with_horse"         # = 0x00000001
    ALIGN_WITH_GROUND = "acf_align_with_ground"       # = 0x00000002
    ENFORCE_LOWERBODY = "acf_enforce_lowerbody"       # = 0x00000100
    ENFORCE_RIGHTSIDE = "acf_enforce_rightside"       # = 0x00000200
    ENFORCE_ALL = "acf_enforce_all"             # = 0x00000400
    PARALLELS_FOR_LOOK_SLOPE = "acf_parallels_for_look_slope" # = 0x00001000
    LOCK_CAMERA = "acf_lock_camera"             # = 0x00002000
    DISPLAE_POSITION = "acf_displace_position"       # = 0x00004000
    IGNORE_SLOPE = "acf_ignore_slope"            # = 0x00008000
    THRUST = "acf_thrust"                  # = 0x00010000
    RIGHT_CUT = "acf_right_cut"               # = 0x00020000
    LEFT_CUT = "acf_left_cut"                # = 0x00040000
    OVERSWING = "acf_overswing"               # = 0x00080000
    ROT_VERTICAL_MASK = "acf_rot_vertical_mask"       # = 0x00300000
    ROT_VERTICAL_BOW = "acf_rot_vertical_bow"        # = 0x00100000
    ROT_VERTICAL_SWORD = "acf_rot_vertical_sword"      # = 0x00200000
    ANIM_LENGTH_MASK = "acf_anim_length_mask"        # = 0xff000000

    # = "acf_anim_length_bits"         = 24
    # def acf_anim_length(x):



class AnimationSequence:
    def __init__(self, duration : float, resource_name : str, beginning_frame : int, ending_frame : int):
        self.duration = duration
        self.resource_name = resource_name
        self.beginning_frame = beginning_frame
        self.ending_frame = ending_frame
        self.flags = []
        self.extra_vals = [0, 0, 0, 0, 0, 0, 0, 0]


    def add_flag(self, flag : AnimationSequenceFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : AnimationSequenceFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : AnimationSequenceFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]


    def setExtraVals(self, index, val : float):
        if index >= 0 and index < len(self.extra_vals):
            self.extra_vals[index] = val
        else:
            print("AnimationSequence:", "Invalid values!")



class Animation:
    def __init__(self, id : str, animation_length : int = 0):
        self.id = id
        self.flags = []
        self.masterFlags = []
        self.sequences = []
        self.animation_length = animation_length


    def add_sequence(self, sequence : AnimationSequence):
        self.sequences.append(sequence)


    def add_flag(self, flag : AnimationFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : AnimationFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : AnimationFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]


    def add_master_flag(self, flag : AnimationMasterFlag):
        if not self.contains_master_flag(flag):
            self.masterFlags.append(flag.value)


    def contains_master_flag(self, flag : AnimationMasterFlag):
        contains = False
        for x in self.masterFlags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_master_flag(self, flag : AnimationMasterFlag):
        if self.contains_master_flag(flag):
            remi = -1
            for i, f in enumerate(self.masterFlags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.masterFlags[remi]

