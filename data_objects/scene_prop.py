# This Python file uses the following encoding: utf-8

from enum import Enum
from simple_trigger import SimpleTrigger


class ScenePropFlag(Enum):
    TYPE_CONTAINER = "sokf_type_container"       # = 0x0000000000000005
    TYPE_AI_LIMITER = "sokf_type_ai_limiter"      # = 0x0000000000000008
    TYPE_BARRIER = "sokf_type_barrier"         # = 0x0000000000000009
    TYPE_BARRIER_LEAVE = "sokf_type_barrier_leave"   # = 0x000000000000000a
    TYPE_LADDER = "sokf_type_ladder"          # = 0x000000000000000b
    TYPE_BARRIER_3D = "sokf_type_barrier3d"       # = 0x000000000000000c
    TYPE_PLAYER_LIMITER = "sokf_type_player_limiter"  # = 0x000000000000000d
    TYPE_AI_LIMITER_3D = "sokf_type_ai_limiter3d"    # = 0x000000000000000e
    #TYPE_MASK = "sokf_type_mask"            # = 0x00000000000000FF
    ADD_FIRE = "sokf_add_fire"             # = 0x0000000000000100
    ADD_SMOKE = "sokf_add_smoke"            # = 0x0000000000000200
    ADD_LIGHT = "sokf_add_light"            # = 0x0000000000000400
    SHOW_HIT_POINT_BAR = "sokf_show_hit_point_bar"   # = 0x0000000000000800
    PLACE_AT_ORIGIN = "sokf_place_at_origin"      # = 0x0000000000001000
    DYNAMIC = "sokf_dynamic"              # = 0x0000000000002000
    INVISIBLE = "sokf_invisible"            # = 0x0000000000004000
    DESTRUCTIBLE = "sokf_destructible"         # = 0x0000000000008000
    MOVEABLE = "sokf_moveable"             # = 0x0000000000010000
    FACE_PLAYER = "sokf_face_player"          # = 0x0000000000020000
    DYNAMIC_PHYSICS = "sokf_dynamic_physics"      # = 0x0000000000040000
    MISSILES_NOT_ATTACHED = "sokf_missiles_not_attached" # = 0x0000000000080000 #works only for dynamic mission objects
    ENFORCE_SHADOWS = "sokf_enforce_shadows"      # = 0x0000000000100000
    DONT_MOVE_AGENT_OVER = "sokf_dont_move_agent_over" # = 0x0000000000200000
    HANDLE_AS_FLORA = "sokf_handle_as_flora"      # = 0x0000000001000000
    STATIC_MOVEMENT = "sokf_static_movement"      # = 0x0000000002000000



class SceneProp:
    def __init__(self, id : str, mesh_name : str = "0", physics_object_name : str = "0"):
        self.id = id
        self.mesh_name = mesh_name
        self.physics_object_name = physics_object_name
        self.hit_points = 0
        self.use_time = 0
        self.flags = []
        self.triggers = []


    def set_hit_points(self, hitpoints : int):
        self.hit_points = hitpoints


    def set_use_time(self, use_time : int):
        self.use_time = use_time


    def add_trigger(self, trigger : SimpleTrigger):
        if not trigger in self.triggers:
            self.triggers.append(trigger)


    def add_flag(self, flag : ScenePropFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : ScenePropFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : ScenePropFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]
