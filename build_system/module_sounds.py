from header_sounds import *
sounds = [

("click", sf_2d|sf_vol_3, ["drum_3.ogg"]),
("gong", sf_2d|sf_vol_7|sf_priority_9, ["s_cymbals.ogg"]),
("quest_taken", sf_2d|sf_vol_7|sf_priority_9, []),
("quest_completed", sf_2d|sf_vol_8|sf_priority_9, ["quest_completed.ogg"]),
("quest_succeeded", sf_2d|sf_vol_6|sf_priority_9, ["quest_succeeded.ogg"]),
("quest_concluded", sf_2d|sf_vol_7|sf_priority_9, ["quest_concluded.ogg"]),
("quest_failed", sf_2d|sf_vol_7|sf_priority_9, ["quest_failed.ogg"]),
("quest_cancelled", sf_2d|sf_vol_7|sf_priority_9, ["quest_cancelled.ogg"]),
("rain", sf_2d|sf_looping|sf_vol_4|sf_priority_10, ["rain_1.ogg"]),
("money_received", sf_2d|sf_vol_4|sf_priority_10, ["coins_dropped_1.ogg"]),
("money_paid", sf_2d|sf_vol_10|sf_priority_10, ["coins_dropped_2.ogg"]),
("sword_clash_1", 0|sf_vol_8|sf_priority_5, ["sword_clank_metal_09.ogg","sword_clank_metal_09b.ogg","sword_clank_metal_10.ogg","sword_clank_metal_10b.ogg","sword_clank_metal_12.ogg","sword_clank_metal_12b.ogg","sword_clank_metal_13.ogg","sword_clank_metal_13b.ogg"]),
("sword_clash_2", 0|sf_vol_9|sf_priority_5, ["s_swordClash2.wav"]),
("sword_clash_3", 0|sf_vol_9|sf_priority_5, ["s_swordClash3.wav"]),
("sword_swing", 0|sf_vol_8|sf_priority_2, ["s_swordSwing.wav"]),
("footstep_grass", 0|sf_vol_4|sf_priority_1, ["footstep_1.ogg","footstep_2.ogg","footstep_3.ogg","footstep_4.ogg"]),
("footstep_wood", 0|sf_vol_5|sf_priority_1, ["footstep_wood_1.ogg","footstep_wood_2.ogg","footstep_wood_4.ogg"]),
("footstep_water", 0|sf_vol_4|sf_priority_3, ["water_walk_1.ogg","water_walk_2.ogg","water_walk_3.ogg","water_walk_4.ogg"]),
("sounds_end", sf_2d|sf_vol_10|sf_priority_10, ["enemy_scored_a_point.ogg"]),

] # SOUNDS END
