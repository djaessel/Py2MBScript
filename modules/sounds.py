# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")

from sound import Sound, SoundFlag

# Basic
click = Sound("click")
click.add_flag(SoundFlag.IS_2D)
click.add_file("drum_3.ogg")
click.set_volume(3)

gong = Sound("gong")
gong.add_flag(SoundFlag.IS_2D)
gong.set_priority(9)
gong.set_volume(7)
gong.add_file("s_cymbals.ogg")


# Quests
quest_taken = Sound("quest_taken")
quest_taken.add_flag(SoundFlag.IS_2D)
quest_taken.set_priority(9)
quest_taken.set_volume(7)

quest_completed = Sound("quest_completed")
quest_completed.add_flag(SoundFlag.IS_2D)
quest_completed.set_priority(9)
quest_completed.set_volume(8)
quest_completed.add_file("quest_completed.ogg")

quest_succeeded = Sound("quest_succeeded")
quest_succeeded.add_flag(SoundFlag.IS_2D)
quest_succeeded.set_priority(9)
quest_succeeded.set_volume(6)
quest_succeeded.add_file("quest_succeeded.ogg")

quest_concluded = Sound("quest_concluded")
quest_concluded.add_flag(SoundFlag.IS_2D)
quest_concluded.set_priority(9)
quest_concluded.set_volume(7)
quest_concluded.add_file("quest_concluded.ogg")

quest_failed = Sound("quest_failed")
quest_failed.add_flag(SoundFlag.IS_2D)
quest_failed.set_priority(9)
quest_failed.set_volume(7)
quest_failed.add_file("quest_failed.ogg")

quest_cancelled = Sound("quest_cancelled")
quest_cancelled.add_flag(SoundFlag.IS_2D)
quest_cancelled.set_priority(9)
quest_cancelled.set_volume(7)
quest_cancelled.add_file("quest_cancelled.ogg")


# Basic
rain = Sound("rain")
rain.add_flag(SoundFlag.IS_2D)
rain.add_flag(SoundFlag.LOOPING)
rain.set_priority(10)
rain.set_volume(4)
rain.add_file("rain_1.ogg")

money_received = Sound("money_received")
money_received.add_flag(SoundFlag.IS_2D)
money_received.set_priority(10)
money_received.set_volume(4)
money_received.add_file("coins_dropped_1.ogg")

money_paid = Sound("money_paid")
money_paid.add_flag(SoundFlag.IS_2D)
money_paid.set_priority(10)
money_paid.set_volume(10)
money_paid.add_file("coins_dropped_2.ogg")


# Swords
sword_clash_1 = Sound("sword_clash_1")
sword_clash_1.set_priority(5)
sword_clash_1.set_volume(8)
sword_clash_1.add_files(["sword_clank_metal_09.ogg","sword_clank_metal_09b.ogg","sword_clank_metal_10.ogg","sword_clank_metal_10b.ogg","sword_clank_metal_12.ogg","sword_clank_metal_12b.ogg","sword_clank_metal_13.ogg","sword_clank_metal_13b.ogg"])

sword_clash_2 = Sound("sword_clash_2")
sword_clash_2.set_priority(5)
sword_clash_2.set_volume(9)
sword_clash_2.add_file("s_swordClash2.wav")

sword_clash_3 = Sound("sword_clash_3")
sword_clash_3.set_priority(5)
sword_clash_3.set_volume(9)
sword_clash_3.add_file("s_swordClash3.wav")

sword_swing = Sound("sword_swing")
sword_swing.set_priority(2)
sword_swing.set_volume(8)
sword_swing.add_file("s_swordSwing.wav")


# Foot steps
footstep_grass = Sound("footstep_grass")
footstep_grass.set_priority(1)
footstep_grass.set_volume(4)
footstep_grass.add_files(["footstep_1.ogg","footstep_2.ogg","footstep_3.ogg","footstep_4.ogg"])

footstep_wood = Sound("footstep_wood")
footstep_wood.set_priority(1)
footstep_wood.set_volume(5)
footstep_wood.add_files(["footstep_wood_1.ogg","footstep_wood_2.ogg","footstep_wood_4.ogg"])

footstep_water = Sound("footstep_water")
footstep_water.set_priority(3)
footstep_water.set_volume(4)
footstep_water.add_files(["water_walk_1.ogg","water_walk_2.ogg","water_walk_3.ogg","water_walk_4.ogg"])

#("footstep_horse",sf_priority_3|sf_vol_8, ["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),
#("footstep_horse_1b",sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
#("footstep_horse_1f",sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav","s_footstep_horse_2f.wav","s_footstep_horse_3b.wav","s_footstep_horse_3f.wav"]),
#("footstep_horse_2b",sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav"]),
#("footstep_horse_2f",sf_priority_3|sf_vol_8, ["s_footstep_horse_2f.wav"]),
#("footstep_horse_3b",sf_priority_3|sf_vol_8, ["s_footstep_horse_3b.wav"]),
#("footstep_horse_3f",sf_priority_3|sf_vol_8, ["s_footstep_horse_3f.wav"]),
#("footstep_horse_4b",sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav"]),
#("footstep_horse_4f",sf_priority_3|sf_vol_8, ["s_footstep_horse_4f.wav"]),
#("footstep_horse_5b",sf_priority_3|sf_vol_8, ["s_footstep_horse_5b.wav"]),
#("footstep_horse_5f",sf_priority_3|sf_vol_8, ["s_footstep_horse_5f.wav"]),


# Jumps

#("jump_begin", sf_vol_6|sf_priority_9,["jump_begin.ogg"]),
#("jump_end", sf_vol_5|sf_priority_9,["jump_end.ogg"]),
#("jump_begin_water", sf_vol_3|sf_priority_9,["jump_begin_water.ogg"]),
#("jump_end_water", sf_vol_3|sf_priority_9,["jump_end_water.ogg"]),
#("horse_jump_begin", sf_vol_6|sf_priority_9,["horse_jump_begin.ogg"]),
#("horse_jump_end", sf_vol_7|sf_priority_9,["horse_jump_end.ogg"]),
#("horse_jump_begin_water", sf_vol_6|sf_priority_9,["jump_begin_water.ogg"]),
#("horse_jump_end_water", sf_vol_6|sf_priority_9,["jump_end_water.ogg"]),


sounds_end = Sound("sounds_end")
sounds_end.add_flag(SoundFlag.IS_2D)
sounds_end.set_priority(10)
sounds_end.set_volume(10)
sounds_end.add_file("enemy_scored_a_point.ogg")

