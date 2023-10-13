# This Python file uses the following encoding: utf-8

from enum import Enum

class ParticleSystemFlag(Enum):
    ALWAYS_EMIT = "psf_always_emit"         # = 0x0000000002
    GLOBAL_EMIT_DIR = "psf_global_emit_dir"     # = 0x0000000010
    EMIT_AT_WATER_LEVEL = "psf_emit_at_water_level" # = 0x0000000020
    BILLBOARD_2D = "psf_billboard_2d"        # = 0x0000000100 # up_vec = dir, front rotated towards camera
    BILLBOARD_3D = "psf_billboard_3d"        # = 0x0000000200 # front_vec point to camera.
    BILLBOARD_DROP = "psf_billboard_drop"      # = 0x0000000300
    TURN_TO_VELOCITY = "psf_turn_to_velocity"    # = 0x0000000400
    RANDOMIZE_ROTATION = "psf_randomize_rotation"  # = 0x0000001000
    RANDOMIZE_SIZE = "psf_randomize_size"      # = 0x0000002000
    HAS_2D_TURBULANCE = "psf_2d_turbulance"       # = 0x0000010000
    NEXT_EFFECT_IS_LOD = "psf_next_effect_is_lod"  # = 0x0000020000



class ParticleSystem:
    #("game_blood", psf_billboard_3d |psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_1",
    # 500, 0.65, 3, 0.5, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
    # (0.0, 0.7), (0.7, 0.7),          #alpha keys
    # (0.1, 0.7), (1, 0.7),      #red keys
    # (0.1, 0.7), (1, 0.7),       #green keys
    # (0.1, 0.7), (1, 0.7),      #blue keys
    # (0.0, 0.015),   (1, 0.018),  #scale keys
    # (0, 0.05, 0),               #emit box size
    # (0, 1.0, 0.3),                #emit velocity
    # 0.9,                       #emit dir randomness
    # 0,                         #rotation speed
    # 0,                         #rotation damping
    #),

    def __init__(self, id : str, mesh_name : str, num_particles : int, life : float, damping : float, gravity_strength : float, turbulance_size : float, turbulance_strength : float):
        self.id = id
        self.flags = []
        self.mesh_name = mesh_name
        self.num_particles = num_particles
        self.life = life
        self.damping = damping
        self.gravity_strength = gravity_strength
        self.turbulance_size = turbulance_size
        self.turbulance_strength = turbulance_strength
        self.alpha_keys = [(0.0, 0.0), (0.0, 0.0)]
        self.red_keys = [(1.0, 1.0), (1.0, 1.0)]
        self.green_keys = [(1.0, 1.0), (1.0, 1.0)]
        self.blue_keys = [(1.0, 1.0), (1.0, 1.0)]
        self.scale_keys = [(1.0, 1.0), (1.0, 1.0)]
        self.emit_box_size = (1, 1, 1)
        self.emit_velocity = (0, 1.0, 0)
        self.emit_dir_randomness = 0.0
        self.rotation_speed = 0
        self.rotation_damping = 0


    def add_flag(self, flag : ParticleSystemFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : ParticleSystemFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : ParticleSystemFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]


    def set_alpha_keys(self, index : int, time : float, magnitude : float):
        self.alpha_keys[index] = (time, magnitude)


    def set_red_keys(self, index : int, time : float, magnitude : float):
        self.red_keys[index] = (time, magnitude)


    def set_green_keys(self, index : int, time : float, magnitude : float):
        self.green_keys[index] = (time, magnitude)


    def set_blue_keys(self, index : int, time : float, magnitude : float):
        self.blue_keys[index] = (time, magnitude)


    def set_scale_keys(self, index : int, time : float, magnitude : float):
        self.scale_keys[index] = (time, magnitude)


    def set_emit_box_size(self, x : float, y : float, z : float):
        self.emit_box_size = (x,y,z)


    def set_emit_velocity(self, x : float, y : float, z : float):
        self.emit_velocity = (x,y,z)


    def set_emit_direction_randomness(self, r : float):
        self.emit_dir_randomness = r


    def set_rotation(self, speed : float, damping : float):
        self.rotation_speed = speed
        self.rotation_damping = damping



