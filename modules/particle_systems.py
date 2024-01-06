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


game_snow = ParticleSystem("game_snow", "prt_mesh_snow_fall_1", 150, 2, 0.2, 0.1, 30, 20)
game_snow.add_flag(ParticleSystemFlag.BILLBOARD_3D)
game_snow.add_flag(ParticleSystemFlag.GLOBAL_EMIT_DIR)
game_snow.add_flag(ParticleSystemFlag.ALWAYS_EMIT)
game_snow.add_flag(ParticleSystemFlag.RANDOMIZE_SIZE)
game_snow.add_flag(ParticleSystemFlag.RANDOMIZE_ROTATION)
game_snow.set_alpha_keys(0, 0.2, 1)
game_snow.set_emit_box_size(10, 10, 0.5)
game_snow.set_emit_velocity(0, 0, -5.0)
game_snow.set_emit_direction_randomness(1)
game_snow.set_rotation(200, 0.5)


game_blood = ParticleSystem("game_blood", "prt_mesh_blood_1", 500, 0.65, 3, 0.5, 0, 0)
game_blood.add_flag(ParticleSystemFlag.BILLBOARD_3D)
game_blood.add_flag(ParticleSystemFlag.RANDOMIZE_SIZE)
game_blood.add_flag(ParticleSystemFlag.RANDOMIZE_ROTATION)
game_blood.set_alpha_keys(0, 0.0, 0.7)
game_blood.set_alpha_keys(1, 0.7, 0.7)
game_blood.set_red_keys(0, 0.1, 0.7)
game_blood.set_red_keys(1, 1, 0.7)
game_blood.set_green_keys(0, 0.1, 0.7)
game_blood.set_green_keys(1, 1, 0.7)
game_blood.set_blue_keys(0, 0.1, 0.7)
game_blood.set_blue_keys(1, 1, 0.7)
game_blood.set_scale_keys(0, 0.0, 0.015)
game_blood.set_scale_keys(1, 1, 0.018)
game_blood.set_emit_box_size(0, 0.05, 0)
game_blood.set_emit_velocity(0, 1.0, 0.3)
game_blood.set_emit_direction_randomness(0.9)


game_blood_2 = ParticleSystem("game_blood_2", "prt_mesh_blood_3", 2000, 0.6, 3, 0.3, 0, 0)
game_blood_2.add_flag(ParticleSystemFlag.BILLBOARD_3D)
game_blood_2.add_flag(ParticleSystemFlag.RANDOMIZE_SIZE)
game_blood_2.add_flag(ParticleSystemFlag.RANDOMIZE_ROTATION)
game_blood_2.set_alpha_keys(0, 0.0, 0.25)
game_blood_2.set_alpha_keys(1, 0.7, 0.1)
game_blood_2.set_red_keys(0, 0.1, 0.7)
game_blood_2.set_red_keys(1, 1, 0.7)
game_blood_2.set_green_keys(0, 0.1, 0.7)
game_blood_2.set_green_keys(1, 1, 0.7)
game_blood_2.set_blue_keys(0, 0.1, 0.7)
game_blood_2.set_blue_keys(1, 1, 0.7)
game_blood_2.set_scale_keys(0, 0.0, 0.15)
game_blood_2.set_scale_keys(1, 1, 0.35)
game_blood_2.set_emit_box_size(0.01, 0.2, 0.01)
game_blood_2.set_emit_velocity(0.2, 0.3, 0)
game_blood_2.set_emit_direction_randomness(0.3)
game_blood_2.set_rotation(150, 0)


game_hoof_dust = ParticleSystem("game_hoof_dust", "prt_mesh_dust_1", 5, 2.0,  10, 0.05, 10.0, 39.0)
game_hoof_dust.add_flag(ParticleSystemFlag.BILLBOARD_3D)
game_hoof_dust.add_flag(ParticleSystemFlag.RANDOMIZE_SIZE)
game_hoof_dust.add_flag(ParticleSystemFlag.RANDOMIZE_ROTATION)
game_hoof_dust.add_flag(ParticleSystemFlag.HAS_2D_TURBULANCE)
game_hoof_dust.set_alpha_keys(0, 0.2, 0.5)
game_hoof_dust.set_alpha_keys(1, 1, 0.0)
game_hoof_dust.set_red_keys(0, 0, 1)
#game_hoof_dust.set_red_keys(1, 1, 1)
game_hoof_dust.set_green_keys(0, 0, 0.9)
game_hoof_dust.set_green_keys(1, 1, 0.9)
game_hoof_dust.set_blue_keys(0, 0, 0.78)
game_hoof_dust.set_blue_keys(1, 1, 0.78)
game_hoof_dust.set_scale_keys(0, 0.0, 2.0)
game_hoof_dust.set_scale_keys(1, 1.0, 3.5)
game_hoof_dust.set_emit_box_size(0.2, 0.3, 0.2)
game_hoof_dust.set_emit_velocity(0, 0, 3.9)
game_hoof_dust.set_emit_direction_randomness(0.5)
game_hoof_dust.set_rotation(130, 0.5)


game_hoof_dust_snow = ParticleSystem("game_hoof_dust_snow", "prt_mesh_snow_dust_1", 6, 2, 3.5, 1, 10.0, 0.0)
game_hoof_dust_snow.add_flag(ParticleSystemFlag.BILLBOARD_3D)
game_hoof_dust_snow.add_flag(ParticleSystemFlag.RANDOMIZE_SIZE)
game_hoof_dust_snow.set_alpha_keys(0, 0.2, 1)
#game_hoof_dust_snow.set_alpha_keys(1, 1, 1)
game_hoof_dust_snow.set_red_keys(0, 0, 1)
game_hoof_dust_snow.set_green_keys(0, 0, 1)
game_hoof_dust_snow.set_blue_keys(0, 0, 1)
game_hoof_dust_snow.set_scale_keys(0, 0.5, 4)
game_hoof_dust_snow.set_scale_keys(1, 1.0, 5.7)
game_hoof_dust_snow.set_emit_box_size(0.2, 1, 0.1)
game_hoof_dust_snow.set_emit_velocity(0, 0, 1)
game_hoof_dust_snow.set_emit_direction_randomness(2)


game_hoof_dust_mud = ParticleSystem("game_hoof_dust_mud", "prt_mesh_mud_1", 5, .7,  10, 3, 0, 0)
game_hoof_dust_mud.add_flag(ParticleSystemFlag.BILLBOARD_2D)
game_hoof_dust_mud.add_flag(ParticleSystemFlag.RANDOMIZE_SIZE)
game_hoof_dust_mud.add_flag(ParticleSystemFlag.RANDOMIZE_ROTATION)
game_hoof_dust_mud.add_flag(ParticleSystemFlag.HAS_2D_TURBULANCE)
game_hoof_dust_mud.set_alpha_keys(0, 0, 1)
#game_hoof_dust_mud.set_alpha_keys(1, 1, 1)
game_hoof_dust_mud.set_red_keys(0, 0, 0.7)
game_hoof_dust_mud.set_red_keys(1, 1, 0.7)
game_hoof_dust_mud.set_green_keys(0, 0, 0.6)
game_hoof_dust_mud.set_green_keys(1, 1, 0.6)
game_hoof_dust_mud.set_blue_keys(0, 0, 0.4)
game_hoof_dust_mud.set_blue_keys(1, 1, 0.4)
game_hoof_dust_mud.set_scale_keys(0, 0.0, 0.2)
game_hoof_dust_mud.set_scale_keys(1, 1.0, 0.22)
game_hoof_dust_mud.set_emit_box_size(0.15, 0.5, 0.1)
game_hoof_dust_mud.set_emit_velocity(0, 0, 15)
game_hoof_dust_mud.set_emit_direction_randomness(6)
game_hoof_dust_mud.set_rotation(200, 0.5)


# TODO: add more from original game
