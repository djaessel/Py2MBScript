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


# Foot steps horse
footstep_horse = Sound("footstep_horse")
footstep_horse.set_priority(3)
footstep_horse.set_volume(8)
footstep_horse.add_files(["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"])

footstep_horse_1b = Sound("footstep_horse_1b")
footstep_horse_1b.set_priority(3)
footstep_horse_1b.set_volume(8)
footstep_horse_1b.add_files(["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"])

footstep_horse_1f = Sound("footstep_horse_1f")
footstep_horse_1f.set_priority(3)
footstep_horse_1f.set_volume(8)
footstep_horse_1f.add_files(["s_footstep_horse_2b.wav","s_footstep_horse_2f.wav","s_footstep_horse_3b.wav","s_footstep_horse_3f.wav"])

footstep_horse_2b = Sound("footstep_horse_2b")
footstep_horse_2b.set_priority(3)
footstep_horse_2b.set_volume(8)
footstep_horse_2b.add_file("s_footstep_horse_2b.wav")

footstep_horse_2f = Sound("footstep_horse_2f")
footstep_horse_2f.set_priority(3)
footstep_horse_2f.set_volume(8)
footstep_horse_2f.add_file("s_footstep_horse_2f.wav")

footstep_horse_3b = Sound("footstep_horse_3b")
footstep_horse_3b.set_priority(3)
footstep_horse_3b.set_volume(8)
footstep_horse_3b.add_file("s_footstep_horse_3b.wav")

footstep_horse_3f = Sound("footstep_horse_3f")
footstep_horse_3f.set_priority(3)
footstep_horse_3f.set_volume(8)
footstep_horse_3f.add_file("s_footstep_horse_3f.wav")

footstep_horse_4b = Sound("footstep_horse_4b")
footstep_horse_4b.set_priority(3)
footstep_horse_4b.set_volume(8)
footstep_horse_4b.add_file("s_footstep_horse_4b.wav")

footstep_horse_4f = Sound("footstep_horse_4f")
footstep_horse_4f.set_priority(3)
footstep_horse_4f.set_volume(8)
footstep_horse_4f.add_file("s_footstep_horse_4f.wav")

footstep_horse_5b = Sound("footstep_horse_5b")
footstep_horse_5b.set_priority(3)
footstep_horse_5b.set_volume(8)
footstep_horse_5b.add_file("s_footstep_horse_5b.wav")

footstep_horse_5f = Sound("footstep_horse_5f")
footstep_horse_5f.set_priority(3)
footstep_horse_5f.set_volume(8)
footstep_horse_5f.add_file("s_footstep_horse_5f.wav")


# Jumps
jump_begin = Sound("jump_begin")
jump_begin.set_volume(6)
jump_begin.set_priority(9)
jump_begin.add_file("jump_begin.ogg")

jump_end = Sound("jump_end")
jump_end.set_volume(5)
jump_end.set_priority(9)
jump_end.add_file("jump_end.ogg")

jump_begin_water = Sound("jump_begin_water")
jump_begin_water.set_volume(3)
jump_begin_water.set_priority(9)
jump_begin_water.add_file("jump_begin_water.ogg")

jump_end_water = Sound("jump_end_water")
jump_end_water.set_volume(3)
jump_end_water.set_priority(9)
jump_end_water.add_file("jump_end_water.ogg")


# Horse Jumps
horse_jump_begin = Sound("horse_jump_begin")
horse_jump_begin.set_volume(6)
horse_jump_begin.set_priority(9)
horse_jump_begin.add_file("horse_jump_begin.ogg")

horse_jump_end = Sound("horse_jump_end")
horse_jump_end.set_volume(7)
horse_jump_end.set_priority(9)
horse_jump_end.add_file("horse_jump_end.ogg")

horse_jump_begin_water = Sound("horse_jump_begin_water")
horse_jump_begin_water.set_volume(6)
horse_jump_begin_water.set_priority(9)
horse_jump_begin_water.add_file("jump_begin_water.ogg")

horse_jump_end_water = Sound("horse_jump_end_water")
horse_jump_end_water.set_volume(6)
horse_jump_end_water.set_priority(9)
horse_jump_end_water.add_file("jump_end_water.ogg")


'''
("release_bow",sf_vol_4, ["release_bow_1.ogg"]),
 ("release_crossbow",sf_vol_7, ["release_crossbow_1.ogg"]),
 ("throw_javelin",sf_vol_5, ["throw_javelin_2.ogg"]),
 ("throw_axe",sf_vol_7, ["throw_axe_1.ogg"]),
 ("throw_knife",sf_vol_5, ["throw_knife_1.ogg"]),
 ("throw_stone",sf_vol_7, ["throw_stone_1.ogg"]),

 ("reload_crossbow",sf_vol_3, ["reload_crossbow_1.ogg"]),
 ("reload_crossbow_continue",sf_vol_6, ["put_back_dagger.ogg"]),
 ("pull_bow",sf_vol_5, ["pull_bow_1.ogg"]),
 ("pull_arrow",sf_vol_5, ["pull_arrow.ogg"]),

 ("arrow_pass_by",sf_priority_7, ["arrow_pass_by_1.ogg","arrow_pass_by_2.ogg","arrow_pass_by_3.ogg","arrow_pass_by_4.ogg"]),
 ("bolt_pass_by",sf_priority_7, ["bolt_pass_by_1.ogg"]),
 ("javelin_pass_by",sf_priority_7, ["javelin_pass_by_1.ogg","javelin_pass_by_2.ogg"]),
 ("stone_pass_by",sf_vol_9|sf_priority_7, ["stone_pass_by_1.ogg"]),
 ("axe_pass_by",sf_priority_7, ["axe_pass_by_1.ogg"]),
 ("knife_pass_by",sf_priority_7, ["knife_pass_by_1.ogg"]),
 ("bullet_pass_by",sf_priority_7, ["arrow_whoosh_1.ogg"]),

 ("incoming_arrow_hit_ground",sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.ogg","arrow_hit_ground_3.ogg","incoming_bullet_hit_ground_1.ogg"]),
 ("incoming_bolt_hit_ground",sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.ogg","arrow_hit_ground_3.ogg","incoming_bullet_hit_ground_1.ogg"]),
 ("incoming_javelin_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("incoming_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("incoming_bullet_hit_ground",sf_priority_7|sf_vol_7, ["incoming_bullet_hit_ground_1.ogg"]),

 ("outgoing_arrow_hit_ground",sf_priority_7|sf_vol_7, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_bolt_hit_ground",sf_priority_7|sf_vol_7,  ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_javelin_hit_ground",sf_priority_7|sf_vol_10, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("outgoing_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("outgoing_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("outgoing_bullet_hit_ground",sf_priority_7|sf_vol_7, ["incoming_bullet_hit_ground_1.ogg"]),

 ("draw_sword",sf_priority_2|sf_vol_4, ["draw_sword.ogg"]),
 ("put_back_sword",sf_priority_1|sf_vol_4, ["put_back_sword.ogg"]),
 ("draw_greatsword",sf_priority_2|sf_vol_4, ["draw_greatsword.ogg"]),
 ("put_back_greatsword",sf_priority_1|sf_vol_4, ["put_back_sword.ogg"]),
 ("draw_axe",sf_priority_2|sf_vol_4, ["draw_mace.ogg"]),
 ("put_back_axe",sf_priority_1|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_greataxe",sf_priority_2|sf_vol_4, ["draw_greataxe.ogg"]),
 ("put_back_greataxe",sf_priority_1|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_spear",sf_priority_2|sf_vol_4, ["draw_spear.ogg"]),
 ("put_back_spear",sf_priority_1|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_crossbow",sf_priority_2|sf_vol_4, ["draw_crossbow.ogg"]),
 ("put_back_crossbow",sf_priority_1|sf_vol_4, ["put_back_to_leather.ogg"]),
 ("draw_revolver",sf_priority_2|sf_vol_4, ["draw_from_holster.ogg"]),
 ("put_back_revolver",sf_priority_1|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_dagger",sf_priority_2|sf_vol_4, ["draw_dagger.ogg"]),
 ("put_back_dagger",sf_priority_1|sf_vol_4, ["put_back_dagger.ogg"]),
 ("draw_bow",sf_priority_2|sf_vol_4, ["draw_bow.ogg"]),
 ("put_back_bow",sf_priority_1|sf_vol_4, ["put_back_to_holster.ogg"]),
 ("draw_shield",sf_priority_2|sf_vol_4, ["draw_shield.ogg"]),
 ("put_back_shield",sf_priority_1|sf_vol_4, ["put_back_shield.ogg"]),
 ("draw_other",sf_priority_2|sf_vol_4, ["draw_other.ogg"]),
 ("put_back_other",sf_priority_1|sf_vol_4, ["draw_other2.ogg"]),
''' and None


# Body Fall
body_fall_small = Sound("body_fall_small")
body_fall_small.set_priority(5)
body_fall_small.set_volume(9)
body_fall_small.add_files(["body_fall_small_1.ogg","body_fall_small_2.ogg"])

body_fall_big = Sound("body_fall_big")
body_fall_big.set_priority(5)
body_fall_big.set_volume(9)
body_fall_big.add_files(["body_fall_1.ogg","body_fall_2.ogg","body_fall_3.ogg"])

# ("body_fall_very_big",sf_priority_9|sf_vol_10, ["body_fall_very_big_1.ogg"]),

horse_body_fall_begin = Sound("horse_body_fall_begin")
horse_body_fall_begin.set_priority(6)
horse_body_fall_begin.set_volume(10)
horse_body_fall_begin.add_file("horse_body_fall_begin_1.ogg")

horse_body_fall_end = Sound("horse_body_fall_end")
horse_body_fall_end.set_priority(6)
horse_body_fall_end.set_volume(10)
horse_body_fall_end.add_files(["horse_body_fall_end_1.ogg","body_fall_2.ogg","body_fall_very_big_1.ogg"])


'''
## ("clang_metal",sf_priority_9, ["clang_metal_1.ogg","clang_metal_2.ogg","s_swordClash1.wav","s_swordClash2.wav","s_swordClash3.wav"]),
 ("hit_wood_wood",sf_priority_7|sf_vol_12, ["hit_wood_wood_1.ogg","hit_wood_wood_2.ogg","hit_wood_wood_3.ogg","hit_wood_wood_4.ogg","hit_wood_metal_4.ogg","hit_wood_metal_5.ogg","hit_wood_metal_6.ogg"]),#dummy
 ("hit_metal_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_3.ogg","hit_metal_metal_4.ogg",
                                              "hit_metal_metal_5.ogg","hit_metal_metal_6.ogg","hit_metal_metal_7.ogg","hit_metal_metal_8.ogg",
                                              "hit_metal_metal_9.ogg","hit_metal_metal_10.ogg",
                                              "clang_metal_1.ogg","clang_metal_2.ogg"]),
 ("hit_wood_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_1.ogg","hit_metal_metal_2.ogg","hit_wood_metal_7.ogg"]),
# ("clang_metal", sf_priority_9,["sword_clank_metal_09.ogg","sword_clank_metal_10.ogg","sword_clank_metal_12.ogg","sword_clank_metal_13.ogg"]),
## ("shield_hit_cut",sf_priority_5, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg"]),
 ("shield_hit_wood_wood",sf_priority_7|sf_vol_9, ["shield_hit_wood_wood_1.ogg","shield_hit_wood_wood_2.ogg","shield_hit_wood_wood_3.ogg"]),
 ("shield_hit_metal_metal",sf_priority_7|sf_vol_10, ["shield_hit_metal_metal_1.ogg","shield_hit_metal_metal_2.ogg","shield_hit_metal_metal_3.ogg","shield_hit_metal_metal_4.ogg"]),
 ("shield_hit_wood_metal",sf_priority_7|sf_vol_10, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg","shield_hit_cut_10.ogg"]), #(shield is wood)
 ("shield_hit_metal_wood",sf_priority_7|sf_vol_10, ["shield_hit_metal_wood_1.ogg","shield_hit_metal_wood_2.ogg","shield_hit_metal_wood_3.ogg"]),#(shield is metal)
 ("shield_broken",sf_priority_9, ["shield_broken.ogg"]),
''' and None



# Skin Sounds 1
man_hit = Sound("man_hit")
man_hit.set_priority(7)
man_hit.set_volume(7)
man_hit.add_files(["man_hit_5.ogg","man_hit_6.ogg","man_hit_7.ogg","man_hit_8.ogg","man_hit_9.ogg","man_hit_10.ogg","man_hit_11.ogg","man_hit_12.ogg","man_hit_13.ogg","man_hit_14.ogg","man_hit_15.ogg","man_hit_17.ogg","man_hit_18.ogg","man_hit_19.ogg","man_hit_22.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg","man_hit_59.ogg"])

man_die = Sound("man_die")
man_die.set_priority(10)
man_die.set_volume(8)
man_die.add_files(["man_death_1.ogg","man_death_8.ogg","man_death_8b.ogg","man_death_11.ogg","man_death_14.ogg","man_death_16.ogg","man_death_18.ogg","man_death_21.ogg","man_death_29.ogg","man_death_40.ogg","man_death_44.ogg","man_death_46.ogg","man_death_48.ogg","man_death_64.ogg"]),# ["man_fall_1.ogg","man_fall_2.ogg","man_fall_3.ogg","man_fall_4.ogg"])

woman_hit = Sound("woman_hit")
woman_hit.set_priority(7)
woman_hit.add_files(["woman_hit_2.ogg","woman_hit_3.ogg", "woman_hit_b_2.ogg","woman_hit_b_4.ogg","woman_hit_b_6.ogg","woman_hit_b_7.ogg","woman_hit_b_8.ogg", "woman_hit_b_11.ogg","woman_hit_b_14.ogg","woman_hit_b_16.ogg"])

woman_die = Sound("woman_die")
woman_die.set_priority(10)
woman_die.set_volume(9)
woman_die.add_files(["woman_fall_1.ogg","woman_hit_b_5.ogg"])

woman_yell = Sound("woman_yell")
woman_yell.set_priority(8)
woman_yell.set_volume(9)
woman_yell.add_files(["woman_yell_1.ogg","woman_yell_2.ogg"])



# Misc
hide = Sound("hide")
hide.add_file("s_hide.wav")

unhide = Sound("unhide")
unhide.add_file("s_unhide.wav")

neigh = Sound("neigh")
neigh.add_files(["horse_exterior_whinny_01.ogg","horse_exterior_whinny_02.ogg","horse_exterior_whinny_03.ogg","horse_exterior_whinny_04.ogg","horse_exterior_whinny_05.ogg","horse_whinny.ogg"])

gallop = Sound("gallop")
gallop.set_volume(4)
gallop.add_files(["horse_gallop_3.ogg","horse_gallop_4.ogg","horse_gallop_5.ogg"])

battle = Sound("battle")
battle.set_volume(4)
battle.add_file("battle.ogg")




# Hit Sounds
'''
 ("arrow_hit_body",sf_priority_4, ["arrow_hit_body_1.ogg","arrow_hit_body_2.ogg","arrow_hit_body_3.ogg"]),
 ("metal_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_lo_dmg_1.ogg","sword_hit_lo_armor_lo_dmg_2.ogg","sword_hit_lo_armor_lo_dmg_3.ogg"]),
 ("metal_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_hi_dmg_1.ogg","sword_hit_lo_armor_hi_dmg_2.ogg","sword_hit_lo_armor_hi_dmg_3.ogg"]),
 ("metal_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_hit_high_armor_low_damage.ogg","metal_hit_high_armor_low_damage_2.ogg","metal_hit_high_armor_low_damage_3.ogg"]),
 ("metal_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["sword_hit_hi_armor_hi_dmg_1.ogg","sword_hit_hi_armor_hi_dmg_2.ogg","sword_hit_hi_armor_hi_dmg_3.ogg"]),
 ("wooden_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_hit_low_1.ogg","blunt_hit_low_2.ogg","blunt_hit_low_3.ogg"]),
 ("wooden_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
 ("wooden_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["wooden_hit_high_armor_low_damage.ogg","wooden_hit_high_armor_low_damage_2.ogg"]),
 ("wooden_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
 ("mp_arrow_hit_target",sf_2d|sf_priority_15|sf_vol_9, ["mp_arrow_hit_target.ogg"]),
''' and None

blunt_hit = Sound("blunt_hit")
blunt_hit.set_priority(5)
blunt_hit.set_volume(9)
blunt_hit.add_files(["punch_1.ogg","punch_4.ogg","punch_4.ogg","punch_5.ogg"])

player_hit_by_arrow = Sound("player_hit_by_arrow")
player_hit_by_arrow.set_priority(10)
player_hit_by_arrow.set_volume(10)
player_hit_by_arrow.add_file("player_hit_by_arrow.ogg")

pistol_shot = Sound("pistol_shot")
pistol_shot.set_priority(10)
pistol_shot.set_volume(10)
pistol_shot.add_file("fl_pistol.wav")


# Skin Sounds 2
man_grunt = Sound("man_grunt")
man_grunt.set_priority(6)
man_grunt.set_volume(4)
man_grunt.add_files(["man_excercise_1.ogg","man_excercise_2.ogg","man_excercise_4.ogg"])

man_breath_hard = Sound("man_breath_hard")
man_breath_hard.set_priority(3)
man_breath_hard.set_volume(8)
man_breath_hard.add_files(["man_ugh_1.ogg","man_ugh_2.ogg","man_ugh_4.ogg","man_ugh_7.ogg","man_ugh_12.ogg","man_ugh_13.ogg","man_ugh_17.ogg"])

man_stun = Sound("man_stun")
man_stun.set_priority(3)
man_stun.set_volume(8)
man_stun.add_file("man_stun_1.ogg")

man_grunt_long = Sound("man_grunt_long")
man_grunt_long.set_priority(6)
man_grunt_long.set_volume(7)
man_grunt_long.add_files(["man_grunt_1.ogg","man_grunt_2.ogg","man_grunt_3.ogg","man_grunt_5.ogg","man_grunt_13.ogg","man_grunt_14.ogg"])

man_yell = Sound("man_yell")
man_yell.set_priority(5)
man_yell.set_volume(8)
man_yell.add_files(["man_yell_4.ogg","man_yell_4_2.ogg","man_yell_7.ogg","man_yell_9.ogg","man_yell_11.ogg","man_yell_13.ogg","man_yell_15.ogg","man_yell_16.ogg","man_yell_17.ogg","man_yell_20.ogg","man_shortyell_4.ogg","man_shortyell_5.ogg","man_shortyell_6.ogg","man_shortyell_9.ogg","man_shortyell_11.ogg","man_shortyell_11b.ogg","man_yell_b_18.ogg","man_yell_22.ogg", "man_yell_c_20.ogg"])

man_warcry = Sound("man_warcry")
man_warcry.set_priority(5)
man_warcry.add_files(["man_insult_2.ogg","man_insult_3.ogg","man_insult_7.ogg","man_insult_9.ogg","man_insult_13.ogg","man_insult_15.ogg","man_insult_16.ogg"])

man_victory = Sound("man_victory")
man_victory.set_priority(5)
man_victory.set_volume(10)
man_victory.add_files(["man_victory_3.ogg","man_victory_4.ogg","man_victory_5.ogg","man_victory_8.ogg","man_victory_15.ogg","man_victory_49.ogg","man_victory_52.ogg","man_victory_54.ogg","man_victory_57.ogg","man_victory_71.ogg"])


'''
("encounter_looters",sf_2d|sf_vol_8, ["encounter_river_pirates_5.ogg","encounter_river_pirates_6.ogg","encounter_river_pirates_9.ogg","encounter_river_pirates_10.ogg","encounter_river_pirates_4.ogg"]),

("encounter_bandits",sf_2d|sf_vol_8, ["encounter_bandit_2.ogg","encounter_bandit_9.ogg","encounter_bandit_12.ogg","encounter_bandit_13.ogg","encounter_bandit_15.ogg","encounter_bandit_16.ogg","encounter_bandit_10.ogg",]),
("encounter_farmers",sf_2d|sf_vol_8, ["encounter_farmer_2.ogg","encounter_farmer_5.ogg","encounter_farmer_7.ogg","encounter_farmer_9.ogg"]),
("encounter_sea_raiders",sf_2d|sf_vol_8, ["encounter_sea_raider_5.ogg","encounter_sea_raider_9.ogg","encounter_sea_raider_9b.ogg","encounter_sea_raider_10.ogg"]),
("encounter_steppe_bandits",sf_2d|sf_vol_8, ["encounter_steppe_bandit_3.ogg","encounter_steppe_bandit_3b.ogg","encounter_steppe_bandit_8.ogg","encounter_steppe_bandit_10.ogg","encounter_steppe_bandit_12.ogg"]),
("encounter_nobleman",sf_2d|sf_vol_8, ["encounter_nobleman_1.ogg"]),
# ("encounter_vaegirs_ally",sf_2d|sf_vol_8, ["encounter_vaegirs_ally.ogg","encounter_vaegirs_ally_2.ogg"]),
# ("encounter_vaegirs_neutral",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
# ("encounter_vaegirs_enemy",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
("sneak_town_halt",sf_2d, ["sneak_halt_1.ogg","sneak_halt_2.ogg"]),
("horse_walk",sf_priority_3|sf_vol_5, ["horse_walk_1.ogg","horse_walk_2.ogg","horse_walk_3.ogg","horse_walk_4.ogg"]),
("horse_trot",sf_priority_4|sf_vol_6, ["horse_trot_1.ogg","horse_trot_2.ogg","horse_trot_3.ogg","horse_trot_4.ogg"]),
("horse_canter",sf_priority_4|sf_vol_7, ["horse_canter_1.ogg","horse_canter_2.ogg","horse_canter_3.ogg","horse_canter_4.ogg"]),
("horse_gallop",sf_priority_5|sf_vol_8, ["horse_gallop_6.ogg","horse_gallop_7.ogg","horse_gallop_8.ogg","horse_gallop_9.ogg"]),
("horse_breath",sf_priority_1|sf_vol_4, ["horse_breath_4.ogg","horse_breath_5.ogg","horse_breath_6.ogg","horse_breath_7.ogg"]),
("horse_snort",sf_priority_1|sf_vol_2, ["horse_snort_1.ogg","horse_snort_2.ogg","horse_snort_3.ogg","horse_snort_4.ogg","horse_snort_5.ogg"]),
("horse_low_whinny",sf_vol_12, ["horse_whinny-1.ogg","horse_whinny-2.ogg"]),
("block_fist",0, ["block_fist_3.ogg","block_fist_4.ogg"]),
("man_hit_blunt_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
("man_hit_blunt_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
("man_hit_pierce_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
("man_hit_pierce_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
("man_hit_cut_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
("man_hit_cut_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
''' and None

# man_victory was placed here before


'''
("fire_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
("torch_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
("dummy_hit",sf_priority_9, ["shield_hit_cut_3.ogg","shield_hit_cut_5.ogg"]),
("dummy_destroyed",sf_priority_9, ["shield_broken.ogg"]),
("gourd_destroyed",sf_priority_9, ["shield_broken.ogg"]),#TODO
("cow_moo", sf_2d|sf_priority_9|sf_vol_8, ["cow_moo_1.ogg"]),
("cow_slaughter", sf_2d|sf_priority_9|sf_vol_8, ["cow_slaughter.ogg"]),
("distant_dog_bark", sf_2d|sf_priority_3|sf_vol_8, ["d_dog1.ogg","d_dog2.ogg","d_dog3.ogg","d_dog7.ogg"]),
("distant_owl", sf_2d|sf_priority_3|sf_vol_9, ["d_owl2.ogg","d_owl3.ogg","d_owl4.ogg"]),
("distant_chicken", sf_2d|sf_priority_3|sf_vol_8, ["d_chicken1.ogg","d_chicken2.ogg"]),
("distant_carpenter", sf_2d|sf_priority_3|sf_vol_3, ["d_carpenter1.ogg","d_saw_short3.ogg"]),
("distant_blacksmith", sf_2d|sf_priority_3|sf_vol_4, ["d_blacksmith2.ogg"]),
("arena_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["arena_loop11.ogg"]),
("town_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["town_loop_3.ogg"]),
("tutorial_fail", sf_2d|sf_vol_7,["cue_failure.ogg"]),
("your_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_taken.ogg"]),
("enemy_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["enemy_flag_taken.ogg"]),
("flag_returned", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_returned.ogg"]),
("team_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["you_scored_a_point.ogg"]),
("enemy_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["enemy_scored_a_point.ogg"]),
''' and None


# END
sounds_end = Sound("sounds_end")
sounds_end.add_flag(SoundFlag.IS_2D)
sounds_end.set_priority(10)
sounds_end.set_volume(10)
sounds_end.add_file("enemy_scored_a_point.ogg")

