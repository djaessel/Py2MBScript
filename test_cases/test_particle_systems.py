# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from particle_system import ParticleSystem, ParticleSystemFlag


game_rain = ParticleSystem("game_rain", "prtcl_rain", 500, 0.5, 0.33, 1.0, 10.0, 0.0)
game_rain.add_flag(ParticleSystemFlag.BILLBOARD_2D)
game_rain.add_flag(ParticleSystemFlag.GLOBAL_EMIT_DIR)
game_rain.add_flag(ParticleSystemFlag.ALWAYS_EMIT)
game_rain.set_alpha_keys(0, 1.0, 0.3)
game_rain.set_alpha_keys(1, 1.0, 0.3)
game_rain.set_emit_box_size(8.2, 8.2, 0.2)
game_rain.set_emit_velocity(0, 0, -10)
game_rain.set_rotation(0, 0.5)

#("game_rain", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "prtcl_rain",
# (1.0, 0.3), (1, 0.3),        #alpha keys
# (1.0, 1.0), (1, 1.0),      #red keys
# (1.0, 1.0), (1, 1.0),      #green keys
# (1.0, 1.0), (1, 1.0),      #blue keys
# (1.0, 1.0),   (1.0, 1.0),   #scale keys
# (8.2, 8.2, 0.2),           #emit box size
# (0, 0, -10.0),               #emit velocity
# 0.0,                       #emit dir randomness
# 0,                       #rotation speed
# 0.5                        #rotation damping
#),
