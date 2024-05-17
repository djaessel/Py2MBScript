# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")

from sound import Sound, SoundFlag

click = Sound("click")
click.add_flag(SoundFlag.IS_2D)
click.set_volume(3)
click.add_file("drum_3.ogg")


tutorial_1 = Sound("tutorial_1")
tutorial_1.add_flag(SoundFlag.IS_2D)
tutorial_1.set_volume(7)
tutorial_1.add_file("tutorial_1.ogg")


tutorial_2 = Sound("tutorial_2")
tutorial_2.add_flag(SoundFlag.IS_2D)
tutorial_2.set_volume(7)
tutorial_2.add_file("tutorial_2.ogg")


gong = Sound("gong")
gong.add_flag(SoundFlag.IS_2D)
gong.set_volume(7)
gong.set_priority(9)
gong.add_file("s_cymbals.ogg")


quest_taken = Sound("quest_taken")
quest_taken.add_flag(SoundFlag.IS_2D)
quest_taken.set_volume(7)
quest_taken.set_priority(9)


quest_completed = Sound("quest_completed")
quest_completed.add_flag(SoundFlag.IS_2D)
quest_completed.set_volume(8)
quest_completed.set_priority(9)
quest_completed.add_file("quest_completed.ogg")


quest_succeeded = Sound("quest_succeeded")
quest_succeeded.add_flag(SoundFlag.IS_2D)
quest_succeeded.set_volume(6)
quest_succeeded.set_priority(9)
quest_succeeded.add_file("quest_succeeded.ogg")


quest_concluded = Sound("quest_concluded")
quest_concluded.add_flag(SoundFlag.IS_2D)
quest_concluded.set_volume(7)
quest_concluded.set_priority(9)
quest_concluded.add_file("quest_concluded.ogg")


quest_failed = Sound("quest_failed")
quest_failed.add_flag(SoundFlag.IS_2D)
quest_failed.set_volume(7)
quest_failed.set_priority(9)
quest_failed.add_file("quest_failed.ogg")


quest_cancelled = Sound("quest_cancelled")
quest_cancelled.add_flag(SoundFlag.IS_2D)
quest_cancelled.set_volume(7)
quest_cancelled.set_priority(9)
quest_cancelled.add_file("quest_cancelled.ogg")


rain = Sound("rain")
rain.add_flag(SoundFlag.IS_2D)
rain.add_flag(SoundFlag.LOOPING)
rain.set_volume(4)
rain.set_priority(10)
rain.add_file("rain_1.ogg")


money_received = Sound("money_received")
money_received.add_flag(SoundFlag.IS_2D)
money_received.set_volume(4)
money_received.set_priority(10)
money_received.add_file("coins_dropped_1.ogg")


money_paid = Sound("money_paid")
money_paid.add_flag(SoundFlag.IS_2D)
money_paid.set_volume(10)
money_paid.set_priority(10)
money_paid.add_file("coins_dropped_2.ogg")


sword_clash_1 = Sound("sword_clash_1")
sword_clash_1.set_volume(8)
sword_clash_1.set_priority(5)
sword_clash_1.add_file("sword_clank_metal_09.ogg")
sword_clash_1.add_file("sword_clank_metal_09b.ogg")
sword_clash_1.add_file("sword_clank_metal_10.ogg")
sword_clash_1.add_file("sword_clank_metal_10b.ogg")
sword_clash_1.add_file("sword_clank_metal_12.ogg")
sword_clash_1.add_file("sword_clank_metal_12b.ogg")
sword_clash_1.add_file("sword_clank_metal_13.ogg")
sword_clash_1.add_file("sword_clank_metal_13b.ogg")


sword_clash_2 = Sound("sword_clash_2")
sword_clash_2.set_volume(9)
sword_clash_2.set_priority(5)
sword_clash_2.add_file("s_swordClash2.wav")


sword_clash_3 = Sound("sword_clash_3")
sword_clash_3.set_volume(9)
sword_clash_3.set_priority(5)
sword_clash_3.add_file("s_swordClash3.wav")


sword_swing = Sound("sword_swing")
sword_swing.set_volume(8)
sword_swing.set_priority(2)
sword_swing.add_file("s_swordSwing.wav")


footstep_grass = Sound("footstep_grass")
footstep_grass.set_volume(4)
footstep_grass.set_priority(1)
footstep_grass.add_file("footstep_1.ogg")
footstep_grass.add_file("footstep_2.ogg")
footstep_grass.add_file("footstep_3.ogg")
footstep_grass.add_file("footstep_4.ogg")


footstep_wood = Sound("footstep_wood")
footstep_wood.set_volume(5)
footstep_wood.set_priority(1)
footstep_wood.add_file("footstep_wood_1.ogg")
footstep_wood.add_file("footstep_wood_2.ogg")
footstep_wood.add_file("footstep_wood_4.ogg")


footstep_water = Sound("footstep_water")
footstep_water.set_volume(4)
footstep_water.set_priority(3)
footstep_water.add_file("water_walk_1.ogg")
footstep_water.add_file("water_walk_2.ogg")
footstep_water.add_file("water_walk_3.ogg")
footstep_water.add_file("water_walk_4.ogg")


footstep_horse = Sound("footstep_horse")
footstep_horse.set_volume(8)
footstep_horse.set_priority(3)
footstep_horse.add_file("footstep_horse_5.ogg")
footstep_horse.add_file("footstep_horse_2.ogg")
footstep_horse.add_file("footstep_horse_3.ogg")
footstep_horse.add_file("footstep_horse_4.ogg")


footstep_horse_1b = Sound("footstep_horse_1b")
footstep_horse_1b.set_volume(8)
footstep_horse_1b.set_priority(3)
footstep_horse_1b.add_file("s_footstep_horse_4b.wav")
footstep_horse_1b.add_file("s_footstep_horse_4f.wav")
footstep_horse_1b.add_file("s_footstep_horse_5b.wav")
footstep_horse_1b.add_file("s_footstep_horse_5f.wav")


footstep_horse_1f = Sound("footstep_horse_1f")
footstep_horse_1f.set_volume(8)
footstep_horse_1f.set_priority(3)
footstep_horse_1f.add_file("s_footstep_horse_2b.wav")
footstep_horse_1f.add_file("s_footstep_horse_2f.wav")
footstep_horse_1f.add_file("s_footstep_horse_3b.wav")
footstep_horse_1f.add_file("s_footstep_horse_3f.wav")


footstep_horse_2b = Sound("footstep_horse_2b")
footstep_horse_2b.set_volume(8)
footstep_horse_2b.set_priority(3)
footstep_horse_2b.add_file("s_footstep_horse_2b.wav")


footstep_horse_2f = Sound("footstep_horse_2f")
footstep_horse_2f.set_volume(8)
footstep_horse_2f.set_priority(3)
footstep_horse_2f.add_file("s_footstep_horse_2f.wav")


footstep_horse_3b = Sound("footstep_horse_3b")
footstep_horse_3b.set_volume(8)
footstep_horse_3b.set_priority(3)
footstep_horse_3b.add_file("s_footstep_horse_3b.wav")


footstep_horse_3f = Sound("footstep_horse_3f")
footstep_horse_3f.set_volume(8)
footstep_horse_3f.set_priority(3)
footstep_horse_3f.add_file("s_footstep_horse_3f.wav")


footstep_horse_4b = Sound("footstep_horse_4b")
footstep_horse_4b.set_volume(8)
footstep_horse_4b.set_priority(3)
footstep_horse_4b.add_file("s_footstep_horse_4b.wav")


footstep_horse_4f = Sound("footstep_horse_4f")
footstep_horse_4f.set_volume(8)
footstep_horse_4f.set_priority(3)
footstep_horse_4f.add_file("s_footstep_horse_4f.wav")


footstep_horse_5b = Sound("footstep_horse_5b")
footstep_horse_5b.set_volume(8)
footstep_horse_5b.set_priority(3)
footstep_horse_5b.add_file("s_footstep_horse_5b.wav")


footstep_horse_5f = Sound("footstep_horse_5f")
footstep_horse_5f.set_volume(8)
footstep_horse_5f.set_priority(3)
footstep_horse_5f.add_file("s_footstep_horse_5f.wav")


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


release_bow = Sound("release_bow")
release_bow.set_volume(4)
release_bow.add_file("release_bow_1.ogg")


release_crossbow = Sound("release_crossbow")
release_crossbow.set_volume(7)
release_crossbow.add_file("release_crossbow_1.ogg")


throw_javelin = Sound("throw_javelin")
throw_javelin.set_volume(5)
throw_javelin.add_file("throw_javelin_2.ogg")


throw_axe = Sound("throw_axe")
throw_axe.set_volume(7)
throw_axe.add_file("throw_axe_1.ogg")


throw_knife = Sound("throw_knife")
throw_knife.set_volume(5)
throw_knife.add_file("throw_knife_1.ogg")


throw_stone = Sound("throw_stone")
throw_stone.set_volume(7)
throw_stone.add_file("throw_stone_1.ogg")


reload_crossbow = Sound("reload_crossbow")
reload_crossbow.set_volume(3)
reload_crossbow.add_file("reload_crossbow_1.ogg")


reload_crossbow_continue = Sound("reload_crossbow_continue")
reload_crossbow_continue.set_volume(6)
reload_crossbow_continue.add_file("put_back_dagger.ogg")


pull_bow = Sound("pull_bow")
pull_bow.set_volume(5)
pull_bow.add_file("pull_bow_1.ogg")


pull_arrow = Sound("pull_arrow")
pull_arrow.set_volume(5)
pull_arrow.add_file("pull_arrow.ogg")


arrow_pass_by = Sound("arrow_pass_by")
arrow_pass_by.set_priority(7)
arrow_pass_by.add_file("arrow_pass_by_1.ogg")
arrow_pass_by.add_file("arrow_pass_by_2.ogg")
arrow_pass_by.add_file("arrow_pass_by_3.ogg")
arrow_pass_by.add_file("arrow_pass_by_4.ogg")


bolt_pass_by = Sound("bolt_pass_by")
bolt_pass_by.set_priority(7)
bolt_pass_by.add_file("bolt_pass_by_1.ogg")


javelin_pass_by = Sound("javelin_pass_by")
javelin_pass_by.set_priority(7)
javelin_pass_by.add_file("javelin_pass_by_1.ogg")
javelin_pass_by.add_file("javelin_pass_by_2.ogg")


stone_pass_by = Sound("stone_pass_by")
stone_pass_by.set_volume(9)
stone_pass_by.set_priority(7)
stone_pass_by.add_file("stone_pass_by_1.ogg")


axe_pass_by = Sound("axe_pass_by")
axe_pass_by.set_priority(7)
axe_pass_by.add_file("axe_pass_by_1.ogg")


knife_pass_by = Sound("knife_pass_by")
knife_pass_by.set_priority(7)
knife_pass_by.add_file("knife_pass_by_1.ogg")


bullet_pass_by = Sound("bullet_pass_by")
bullet_pass_by.set_priority(7)
bullet_pass_by.add_file("arrow_whoosh_1.ogg")


incoming_arrow_hit_ground = Sound("incoming_arrow_hit_ground")
incoming_arrow_hit_ground.set_volume(7)
incoming_arrow_hit_ground.set_priority(7)
incoming_arrow_hit_ground.add_file("arrow_hit_ground_2.ogg")
incoming_arrow_hit_ground.add_file("arrow_hit_ground_3.ogg")
incoming_arrow_hit_ground.add_file("incoming_bullet_hit_ground_1.ogg")


incoming_bolt_hit_ground = Sound("incoming_bolt_hit_ground")
incoming_bolt_hit_ground.set_volume(7)
incoming_bolt_hit_ground.set_priority(7)
incoming_bolt_hit_ground.add_file("arrow_hit_ground_2.ogg")
incoming_bolt_hit_ground.add_file("arrow_hit_ground_3.ogg")
incoming_bolt_hit_ground.add_file("incoming_bullet_hit_ground_1.ogg")


incoming_javelin_hit_ground = Sound("incoming_javelin_hit_ground")
incoming_javelin_hit_ground.set_volume(7)
incoming_javelin_hit_ground.set_priority(7)
incoming_javelin_hit_ground.add_file("incoming_javelin_hit_ground_1.ogg")


incoming_stone_hit_ground = Sound("incoming_stone_hit_ground")
incoming_stone_hit_ground.set_volume(7)
incoming_stone_hit_ground.set_priority(7)
incoming_stone_hit_ground.add_file("incoming_stone_hit_ground_1.ogg")


incoming_axe_hit_ground = Sound("incoming_axe_hit_ground")
incoming_axe_hit_ground.set_volume(7)
incoming_axe_hit_ground.set_priority(7)
incoming_axe_hit_ground.add_file("incoming_javelin_hit_ground_1.ogg")


incoming_knife_hit_ground = Sound("incoming_knife_hit_ground")
incoming_knife_hit_ground.set_volume(7)
incoming_knife_hit_ground.set_priority(7)
incoming_knife_hit_ground.add_file("incoming_stone_hit_ground_1.ogg")


incoming_bullet_hit_ground = Sound("incoming_bullet_hit_ground")
incoming_bullet_hit_ground.set_volume(7)
incoming_bullet_hit_ground.set_priority(7)
incoming_bullet_hit_ground.add_file("incoming_bullet_hit_ground_1.ogg")


outgoing_arrow_hit_ground = Sound("outgoing_arrow_hit_ground")
outgoing_arrow_hit_ground.set_volume(7)
outgoing_arrow_hit_ground.set_priority(7)
outgoing_arrow_hit_ground.add_file("outgoing_arrow_hit_ground.ogg")


outgoing_bolt_hit_ground = Sound("outgoing_bolt_hit_ground")
outgoing_bolt_hit_ground.set_volume(7)
outgoing_bolt_hit_ground.set_priority(7)
outgoing_bolt_hit_ground.add_file("outgoing_arrow_hit_ground.ogg")


outgoing_javelin_hit_ground = Sound("outgoing_javelin_hit_ground")
outgoing_javelin_hit_ground.set_volume(10)
outgoing_javelin_hit_ground.set_priority(7)
outgoing_javelin_hit_ground.add_file("outgoing_arrow_hit_ground.ogg")


outgoing_stone_hit_ground = Sound("outgoing_stone_hit_ground")
outgoing_stone_hit_ground.set_volume(7)
outgoing_stone_hit_ground.set_priority(7)
outgoing_stone_hit_ground.add_file("incoming_stone_hit_ground_1.ogg")


outgoing_axe_hit_ground = Sound("outgoing_axe_hit_ground")
outgoing_axe_hit_ground.set_volume(7)
outgoing_axe_hit_ground.set_priority(7)
outgoing_axe_hit_ground.add_file("incoming_javelin_hit_ground_1.ogg")


outgoing_knife_hit_ground = Sound("outgoing_knife_hit_ground")
outgoing_knife_hit_ground.set_volume(7)
outgoing_knife_hit_ground.set_priority(7)
outgoing_knife_hit_ground.add_file("incoming_stone_hit_ground_1.ogg")


outgoing_bullet_hit_ground = Sound("outgoing_bullet_hit_ground")
outgoing_bullet_hit_ground.set_volume(7)
outgoing_bullet_hit_ground.set_priority(7)
outgoing_bullet_hit_ground.add_file("incoming_bullet_hit_ground_1.ogg")


draw_sword = Sound("draw_sword")
draw_sword.set_volume(4)
draw_sword.set_priority(2)
draw_sword.add_file("draw_sword.ogg")


put_back_sword = Sound("put_back_sword")
put_back_sword.set_volume(4)
put_back_sword.set_priority(1)
put_back_sword.add_file("put_back_sword.ogg")


draw_greatsword = Sound("draw_greatsword")
draw_greatsword.set_volume(4)
draw_greatsword.set_priority(2)
draw_greatsword.add_file("draw_greatsword.ogg")


put_back_greatsword = Sound("put_back_greatsword")
put_back_greatsword.set_volume(4)
put_back_greatsword.set_priority(1)
put_back_greatsword.add_file("put_back_sword.ogg")


draw_axe = Sound("draw_axe")
draw_axe.set_volume(4)
draw_axe.set_priority(2)
draw_axe.add_file("draw_mace.ogg")


put_back_axe = Sound("put_back_axe")
put_back_axe.set_volume(4)
put_back_axe.set_priority(1)
put_back_axe.add_file("put_back_to_holster.ogg")


draw_greataxe = Sound("draw_greataxe")
draw_greataxe.set_volume(4)
draw_greataxe.set_priority(2)
draw_greataxe.add_file("draw_greataxe.ogg")


put_back_greataxe = Sound("put_back_greataxe")
put_back_greataxe.set_volume(4)
put_back_greataxe.set_priority(1)
put_back_greataxe.add_file("put_back_to_leather.ogg")


draw_spear = Sound("draw_spear")
draw_spear.set_volume(4)
draw_spear.set_priority(2)
draw_spear.add_file("draw_spear.ogg")


put_back_spear = Sound("put_back_spear")
put_back_spear.set_volume(4)
put_back_spear.set_priority(1)
put_back_spear.add_file("put_back_to_leather.ogg")


draw_crossbow = Sound("draw_crossbow")
draw_crossbow.set_volume(4)
draw_crossbow.set_priority(2)
draw_crossbow.add_file("draw_crossbow.ogg")


put_back_crossbow = Sound("put_back_crossbow")
put_back_crossbow.set_volume(4)
put_back_crossbow.set_priority(1)
put_back_crossbow.add_file("put_back_to_leather.ogg")


draw_revolver = Sound("draw_revolver")
draw_revolver.set_volume(4)
draw_revolver.set_priority(2)
draw_revolver.add_file("draw_from_holster.ogg")


put_back_revolver = Sound("put_back_revolver")
put_back_revolver.set_volume(4)
put_back_revolver.set_priority(1)
put_back_revolver.add_file("put_back_to_holster.ogg")


draw_dagger = Sound("draw_dagger")
draw_dagger.set_volume(4)
draw_dagger.set_priority(2)
draw_dagger.add_file("draw_dagger.ogg")


put_back_dagger = Sound("put_back_dagger")
put_back_dagger.set_volume(4)
put_back_dagger.set_priority(1)
put_back_dagger.add_file("put_back_dagger.ogg")


draw_bow = Sound("draw_bow")
draw_bow.set_volume(4)
draw_bow.set_priority(2)
draw_bow.add_file("draw_bow.ogg")


put_back_bow = Sound("put_back_bow")
put_back_bow.set_volume(4)
put_back_bow.set_priority(1)
put_back_bow.add_file("put_back_to_holster.ogg")


draw_shield = Sound("draw_shield")
draw_shield.set_volume(4)
draw_shield.set_priority(2)
draw_shield.add_file("draw_shield.ogg")


put_back_shield = Sound("put_back_shield")
put_back_shield.set_volume(4)
put_back_shield.set_priority(1)
put_back_shield.add_file("put_back_shield.ogg")


draw_other = Sound("draw_other")
draw_other.set_volume(4)
draw_other.set_priority(2)
draw_other.add_file("draw_other.ogg")


put_back_other = Sound("put_back_other")
put_back_other.set_volume(4)
put_back_other.set_priority(1)
put_back_other.add_file("draw_other2.ogg")


body_fall_small = Sound("body_fall_small")
body_fall_small.set_volume(9)
body_fall_small.set_priority(5)
body_fall_small.add_file("body_fall_small_1.ogg")
body_fall_small.add_file("body_fall_small_2.ogg")


body_fall_big = Sound("body_fall_big")
body_fall_big.set_volume(8)
body_fall_big.set_priority(6)
body_fall_big.add_file("body_fall_1.ogg")
body_fall_big.add_file("body_fall_2.ogg")
body_fall_big.add_file("body_fall_3.ogg")


horse_body_fall_begin = Sound("horse_body_fall_begin")
horse_body_fall_begin.set_volume(10)
horse_body_fall_begin.set_priority(6)
horse_body_fall_begin.add_file("horse_body_fall_begin_1.ogg")


horse_body_fall_end = Sound("horse_body_fall_end")
horse_body_fall_end.set_volume(10)
horse_body_fall_end.set_priority(6)
horse_body_fall_end.add_file("horse_body_fall_end_1.ogg")
horse_body_fall_end.add_file("body_fall_2.ogg")
horse_body_fall_end.add_file("body_fall_very_big_1.ogg")


hit_wood_wood = Sound("hit_wood_wood")
hit_wood_wood.set_volume(12)
hit_wood_wood.set_priority(7)
hit_wood_wood.add_file("hit_wood_wood_1.ogg")
hit_wood_wood.add_file("hit_wood_wood_2.ogg")
hit_wood_wood.add_file("hit_wood_wood_3.ogg")
hit_wood_wood.add_file("hit_wood_wood_4.ogg")
hit_wood_wood.add_file("hit_wood_metal_4.ogg")
hit_wood_wood.add_file("hit_wood_metal_5.ogg")
hit_wood_wood.add_file("hit_wood_metal_6.ogg")


hit_metal_metal = Sound("hit_metal_metal")
hit_metal_metal.set_volume(10)
hit_metal_metal.set_priority(7)
hit_metal_metal.add_file("hit_metal_metal_3.ogg")
hit_metal_metal.add_file("hit_metal_metal_4.ogg")
hit_metal_metal.add_file("hit_metal_metal_5.ogg")
hit_metal_metal.add_file("hit_metal_metal_6.ogg")
hit_metal_metal.add_file("hit_metal_metal_7.ogg")
hit_metal_metal.add_file("hit_metal_metal_8.ogg")
hit_metal_metal.add_file("hit_metal_metal_9.ogg")
hit_metal_metal.add_file("hit_metal_metal_10.ogg")
hit_metal_metal.add_file("clang_metal_1.ogg")
hit_metal_metal.add_file("clang_metal_2.ogg")


hit_wood_metal = Sound("hit_wood_metal")
hit_wood_metal.set_volume(10)
hit_wood_metal.set_priority(7)
hit_wood_metal.add_file("hit_metal_metal_1.ogg")
hit_wood_metal.add_file("hit_metal_metal_2.ogg")
hit_wood_metal.add_file("hit_wood_metal_7.ogg")


shield_hit_wood_wood = Sound("shield_hit_wood_wood")
shield_hit_wood_wood.set_volume(9)
shield_hit_wood_wood.set_priority(7)
shield_hit_wood_wood.add_file("shield_hit_wood_wood_1.ogg")
shield_hit_wood_wood.add_file("shield_hit_wood_wood_2.ogg")
shield_hit_wood_wood.add_file("shield_hit_wood_wood_3.ogg")


shield_hit_metal_metal = Sound("shield_hit_metal_metal")
shield_hit_metal_metal.set_volume(10)
shield_hit_metal_metal.set_priority(7)
shield_hit_metal_metal.add_file("shield_hit_metal_metal_1.ogg")
shield_hit_metal_metal.add_file("shield_hit_metal_metal_2.ogg")
shield_hit_metal_metal.add_file("shield_hit_metal_metal_3.ogg")
shield_hit_metal_metal.add_file("shield_hit_metal_metal_4.ogg")


shield_hit_wood_metal = Sound("shield_hit_wood_metal")
shield_hit_wood_metal.set_volume(10)
shield_hit_wood_metal.set_priority(7)
shield_hit_wood_metal.add_file("shield_hit_cut_3.ogg")
shield_hit_wood_metal.add_file("shield_hit_cut_4.ogg")
shield_hit_wood_metal.add_file("shield_hit_cut_5.ogg")
shield_hit_wood_metal.add_file("shield_hit_cut_10.ogg")


shield_hit_metal_wood = Sound("shield_hit_metal_wood")
shield_hit_metal_wood.set_volume(10)
shield_hit_metal_wood.set_priority(7)
shield_hit_metal_wood.add_file("shield_hit_metal_wood_1.ogg")
shield_hit_metal_wood.add_file("shield_hit_metal_wood_2.ogg")
shield_hit_metal_wood.add_file("shield_hit_metal_wood_3.ogg")


shield_broken = Sound("shield_broken")
shield_broken.set_priority(9)
shield_broken.add_file("shield_broken.ogg")


man_hit = Sound("man_hit")
man_hit.set_volume(7)
man_hit.set_priority(7)
man_hit.add_file("man_hit_5.ogg")
man_hit.add_file("man_hit_6.ogg")
man_hit.add_file("man_hit_7.ogg")
man_hit.add_file("man_hit_8.ogg")
man_hit.add_file("man_hit_9.ogg")
man_hit.add_file("man_hit_10.ogg")
man_hit.add_file("man_hit_11.ogg")
man_hit.add_file("man_hit_12.ogg")
man_hit.add_file("man_hit_13.ogg")
man_hit.add_file("man_hit_14.ogg")
man_hit.add_file("man_hit_15.ogg")
man_hit.add_file("man_hit_17.ogg")
man_hit.add_file("man_hit_18.ogg")
man_hit.add_file("man_hit_19.ogg")
man_hit.add_file("man_hit_22.ogg")
man_hit.add_file("man_hit_29.ogg")
man_hit.add_file("man_hit_32.ogg")
man_hit.add_file("man_hit_47.ogg")
man_hit.add_file("man_hit_57.ogg")
man_hit.add_file("man_hit_59.ogg")


man_die = Sound("man_die")
man_die.set_volume(8)
man_die.set_priority(10)
man_die.add_file("man_death_1.ogg")
man_die.add_file("man_death_8.ogg")
man_die.add_file("man_death_8b.ogg")
man_die.add_file("man_death_11.ogg")
man_die.add_file("man_death_14.ogg")
man_die.add_file("man_death_16.ogg")
man_die.add_file("man_death_18.ogg")
man_die.add_file("man_death_21.ogg")
man_die.add_file("man_death_29.ogg")
man_die.add_file("man_death_40.ogg")
man_die.add_file("man_death_44.ogg")
man_die.add_file("man_death_46.ogg")
man_die.add_file("man_death_48.ogg")
man_die.add_file("man_death_64.ogg")


woman_hit = Sound("woman_hit")
woman_hit.set_priority(7)
woman_hit.add_file("woman_hit_2.ogg")
woman_hit.add_file("woman_hit_3.ogg")
woman_hit.add_file("woman_hit_b_2.ogg")
woman_hit.add_file("woman_hit_b_4.ogg")
woman_hit.add_file("woman_hit_b_6.ogg")
woman_hit.add_file("woman_hit_b_7.ogg")
woman_hit.add_file("woman_hit_b_8.ogg")
woman_hit.add_file("woman_hit_b_11.ogg")
woman_hit.add_file("woman_hit_b_14.ogg")
woman_hit.add_file("woman_hit_b_16.ogg")


woman_die = Sound("woman_die")
woman_die.set_volume(9)
woman_die.set_priority(10)
woman_die.add_file("woman_fall_1.ogg")
woman_die.add_file("woman_hit_b_5.ogg")


woman_yell = Sound("woman_yell")
woman_yell.set_volume(9)
woman_yell.set_priority(8)
woman_yell.add_file("woman_yell_1.ogg")
woman_yell.add_file("woman_yell_2.ogg")


hide = Sound("hide")
hide.add_file("s_hide.wav")


unhide = Sound("unhide")
unhide.add_file("s_unhide.wav")


neigh = Sound("neigh")
neigh.add_file("horse_exterior_whinny_01.ogg")
neigh.add_file("horse_exterior_whinny_02.ogg")
neigh.add_file("horse_exterior_whinny_03.ogg")
neigh.add_file("horse_exterior_whinny_04.ogg")
neigh.add_file("horse_exterior_whinny_05.ogg")
neigh.add_file("horse_whinny.ogg")


gallop = Sound("gallop")
gallop.set_volume(4)
gallop.add_file("horse_gallop_3.ogg")
gallop.add_file("horse_gallop_4.ogg")
gallop.add_file("horse_gallop_5.ogg")


battle = Sound("battle")
battle.set_volume(4)
battle.add_file("battle.ogg")


arrow_hit_body = Sound("arrow_hit_body")
arrow_hit_body.set_priority(4)
arrow_hit_body.add_file("arrow_hit_body_1.ogg")
arrow_hit_body.add_file("arrow_hit_body_2.ogg")
arrow_hit_body.add_file("arrow_hit_body_3.ogg")


metal_hit_low_armor_low_damage = Sound("metal_hit_low_armor_low_damage")
metal_hit_low_armor_low_damage.set_volume(9)
metal_hit_low_armor_low_damage.set_priority(5)
metal_hit_low_armor_low_damage.add_file("sword_hit_lo_armor_lo_dmg_1.ogg")
metal_hit_low_armor_low_damage.add_file("sword_hit_lo_armor_lo_dmg_2.ogg")
metal_hit_low_armor_low_damage.add_file("sword_hit_lo_armor_lo_dmg_3.ogg")


metal_hit_low_armor_high_damage = Sound("metal_hit_low_armor_high_damage")
metal_hit_low_armor_high_damage.set_volume(9)
metal_hit_low_armor_high_damage.set_priority(5)
metal_hit_low_armor_high_damage.add_file("sword_hit_lo_armor_hi_dmg_1.ogg")
metal_hit_low_armor_high_damage.add_file("sword_hit_lo_armor_hi_dmg_2.ogg")
metal_hit_low_armor_high_damage.add_file("sword_hit_lo_armor_hi_dmg_3.ogg")


metal_hit_high_armor_low_damage = Sound("metal_hit_high_armor_low_damage")
metal_hit_high_armor_low_damage.set_volume(9)
metal_hit_high_armor_low_damage.set_priority(5)
metal_hit_high_armor_low_damage.add_file("metal_hit_high_armor_low_damage.ogg")
metal_hit_high_armor_low_damage.add_file("metal_hit_high_armor_low_damage_2.ogg")
metal_hit_high_armor_low_damage.add_file("metal_hit_high_armor_low_damage_3.ogg")


metal_hit_high_armor_high_damage = Sound("metal_hit_high_armor_high_damage")
metal_hit_high_armor_high_damage.set_volume(9)
metal_hit_high_armor_high_damage.set_priority(5)
metal_hit_high_armor_high_damage.add_file("sword_hit_hi_armor_hi_dmg_1.ogg")
metal_hit_high_armor_high_damage.add_file("sword_hit_hi_armor_hi_dmg_2.ogg")
metal_hit_high_armor_high_damage.add_file("sword_hit_hi_armor_hi_dmg_3.ogg")


wooden_hit_low_armor_low_damage = Sound("wooden_hit_low_armor_low_damage")
wooden_hit_low_armor_low_damage.set_volume(9)
wooden_hit_low_armor_low_damage.set_priority(5)
wooden_hit_low_armor_low_damage.add_file("blunt_hit_low_1.ogg")
wooden_hit_low_armor_low_damage.add_file("blunt_hit_low_2.ogg")
wooden_hit_low_armor_low_damage.add_file("blunt_hit_low_3.ogg")


wooden_hit_low_armor_high_damage = Sound("wooden_hit_low_armor_high_damage")
wooden_hit_low_armor_high_damage.set_volume(9)
wooden_hit_low_armor_high_damage.set_priority(5)
wooden_hit_low_armor_high_damage.add_file("blunt_hit_high_1.ogg")
wooden_hit_low_armor_high_damage.add_file("blunt_hit_high_2.ogg")
wooden_hit_low_armor_high_damage.add_file("blunt_hit_high_3.ogg")


wooden_hit_high_armor_low_damage = Sound("wooden_hit_high_armor_low_damage")
wooden_hit_high_armor_low_damage.set_volume(9)
wooden_hit_high_armor_low_damage.set_priority(5)
wooden_hit_high_armor_low_damage.add_file("wooden_hit_high_armor_low_damage.ogg")
wooden_hit_high_armor_low_damage.add_file("wooden_hit_high_armor_low_damage_2.ogg")


wooden_hit_high_armor_high_damage = Sound("wooden_hit_high_armor_high_damage")
wooden_hit_high_armor_high_damage.set_volume(9)
wooden_hit_high_armor_high_damage.set_priority(5)
wooden_hit_high_armor_high_damage.add_file("blunt_hit_high_1.ogg")
wooden_hit_high_armor_high_damage.add_file("blunt_hit_high_2.ogg")
wooden_hit_high_armor_high_damage.add_file("blunt_hit_high_3.ogg")


mp_arrow_hit_target = Sound("mp_arrow_hit_target")
mp_arrow_hit_target.add_flag(SoundFlag.IS_2D)
mp_arrow_hit_target.set_volume(9)
mp_arrow_hit_target.set_priority(15)
mp_arrow_hit_target.add_file("mp_arrow_hit_target.ogg")


blunt_hit = Sound("blunt_hit")
blunt_hit.set_volume(9)
blunt_hit.set_priority(5)
blunt_hit.add_file("punch_1.ogg")
blunt_hit.add_file("punch_4.ogg")
blunt_hit.add_file("punch_4.ogg")
blunt_hit.add_file("punch_5.ogg")


player_hit_by_arrow = Sound("player_hit_by_arrow")
player_hit_by_arrow.set_volume(10)
player_hit_by_arrow.set_priority(10)
player_hit_by_arrow.add_file("player_hit_by_arrow.ogg")


pistol_shot = Sound("pistol_shot")
pistol_shot.set_volume(10)
pistol_shot.set_priority(10)
pistol_shot.add_file("fl_pistol.wav")


man_grunt = Sound("man_grunt")
man_grunt.set_volume(4)
man_grunt.set_priority(6)
man_grunt.add_file("man_excercise_1.ogg")
man_grunt.add_file("man_excercise_2.ogg")
man_grunt.add_file("man_excercise_4.ogg")


man_breath_hard = Sound("man_breath_hard")
man_breath_hard.set_volume(8)
man_breath_hard.set_priority(3)
man_breath_hard.add_file("man_ugh_1.ogg")
man_breath_hard.add_file("man_ugh_2.ogg")
man_breath_hard.add_file("man_ugh_4.ogg")
man_breath_hard.add_file("man_ugh_7.ogg")
man_breath_hard.add_file("man_ugh_12.ogg")
man_breath_hard.add_file("man_ugh_13.ogg")
man_breath_hard.add_file("man_ugh_17.ogg")


man_stun = Sound("man_stun")
man_stun.set_volume(8)
man_stun.set_priority(3)
man_stun.add_file("man_stun_1.ogg")


man_grunt_long = Sound("man_grunt_long")
man_grunt_long.set_volume(7)
man_grunt_long.set_priority(6)
man_grunt_long.add_file("man_grunt_1.ogg")
man_grunt_long.add_file("man_grunt_2.ogg")
man_grunt_long.add_file("man_grunt_3.ogg")
man_grunt_long.add_file("man_grunt_5.ogg")
man_grunt_long.add_file("man_grunt_13.ogg")
man_grunt_long.add_file("man_grunt_14.ogg")


man_yell = Sound("man_yell")
man_yell.set_volume(8)
man_yell.set_priority(5)
man_yell.add_file("man_yell_4.ogg")
man_yell.add_file("man_yell_4_2.ogg")
man_yell.add_file("man_yell_7.ogg")
man_yell.add_file("man_yell_9.ogg")
man_yell.add_file("man_yell_11.ogg")
man_yell.add_file("man_yell_13.ogg")
man_yell.add_file("man_yell_15.ogg")
man_yell.add_file("man_yell_16.ogg")
man_yell.add_file("man_yell_17.ogg")
man_yell.add_file("man_yell_20.ogg")
man_yell.add_file("man_shortyell_4.ogg")
man_yell.add_file("man_shortyell_5.ogg")
man_yell.add_file("man_shortyell_6.ogg")
man_yell.add_file("man_shortyell_9.ogg")
man_yell.add_file("man_shortyell_11.ogg")
man_yell.add_file("man_shortyell_11b.ogg")
man_yell.add_file("man_yell_b_18.ogg")
man_yell.add_file("man_yell_22.ogg")
man_yell.add_file("man_yell_c_20.ogg")


man_warcry = Sound("man_warcry")
man_warcry.set_priority(5)
man_warcry.add_file("man_insult_2.ogg")
man_warcry.add_file("man_insult_3.ogg")
man_warcry.add_file("man_insult_7.ogg")
man_warcry.add_file("man_insult_9.ogg")
man_warcry.add_file("man_insult_13.ogg")
man_warcry.add_file("man_insult_15.ogg")
man_warcry.add_file("man_insult_16.ogg")


encounter_looters = Sound("encounter_looters")
encounter_looters.add_flag(SoundFlag.IS_2D)
encounter_looters.set_volume(8)
encounter_looters.add_file("encounter_river_pirates_5.ogg")
encounter_looters.add_file("encounter_river_pirates_6.ogg")
encounter_looters.add_file("encounter_river_pirates_9.ogg")
encounter_looters.add_file("encounter_river_pirates_10.ogg")
encounter_looters.add_file("encounter_river_pirates_4.ogg")


encounter_bandits = Sound("encounter_bandits")
encounter_bandits.add_flag(SoundFlag.IS_2D)
encounter_bandits.set_volume(8)
encounter_bandits.add_file("encounter_bandit_2.ogg")
encounter_bandits.add_file("encounter_bandit_9.ogg")
encounter_bandits.add_file("encounter_bandit_12.ogg")
encounter_bandits.add_file("encounter_bandit_13.ogg")
encounter_bandits.add_file("encounter_bandit_15.ogg")
encounter_bandits.add_file("encounter_bandit_16.ogg")
encounter_bandits.add_file("encounter_bandit_10.ogg")


encounter_farmers = Sound("encounter_farmers")
encounter_farmers.add_flag(SoundFlag.IS_2D)
encounter_farmers.set_volume(8)
encounter_farmers.add_file("encounter_farmer_2.ogg")
encounter_farmers.add_file("encounter_farmer_5.ogg")
encounter_farmers.add_file("encounter_farmer_7.ogg")
encounter_farmers.add_file("encounter_farmer_9.ogg")


encounter_sea_raiders = Sound("encounter_sea_raiders")
encounter_sea_raiders.add_flag(SoundFlag.IS_2D)
encounter_sea_raiders.set_volume(8)
encounter_sea_raiders.add_file("encounter_sea_raider_5.ogg")
encounter_sea_raiders.add_file("encounter_sea_raider_9.ogg")
encounter_sea_raiders.add_file("encounter_sea_raider_9b.ogg")
encounter_sea_raiders.add_file("encounter_sea_raider_10.ogg")


encounter_steppe_bandits = Sound("encounter_steppe_bandits")
encounter_steppe_bandits.add_flag(SoundFlag.IS_2D)
encounter_steppe_bandits.set_volume(8)
encounter_steppe_bandits.add_file("encounter_steppe_bandit_3.ogg")
encounter_steppe_bandits.add_file("encounter_steppe_bandit_3b.ogg")
encounter_steppe_bandits.add_file("encounter_steppe_bandit_8.ogg")
encounter_steppe_bandits.add_file("encounter_steppe_bandit_10.ogg")
encounter_steppe_bandits.add_file("encounter_steppe_bandit_12.ogg")


encounter_nobleman = Sound("encounter_nobleman")
encounter_nobleman.add_flag(SoundFlag.IS_2D)
encounter_nobleman.set_volume(8)
encounter_nobleman.add_file("encounter_nobleman_1.ogg")


encounter_vaegirs_ally = Sound("encounter_vaegirs_ally")
encounter_vaegirs_ally.add_flag(SoundFlag.IS_2D)
encounter_vaegirs_ally.set_volume(8)
encounter_vaegirs_ally.add_file("encounter_vaegirs_ally.ogg")
encounter_vaegirs_ally.add_file("encounter_vaegirs_ally_2.ogg")


encounter_vaegirs_neutral = Sound("encounter_vaegirs_neutral")
encounter_vaegirs_neutral.add_flag(SoundFlag.IS_2D)
encounter_vaegirs_neutral.set_volume(8)
encounter_vaegirs_neutral.add_file("encounter_vaegirs_neutral.ogg")
encounter_vaegirs_neutral.add_file("encounter_vaegirs_neutral_2.ogg")
encounter_vaegirs_neutral.add_file("encounter_vaegirs_neutral_3.ogg")
encounter_vaegirs_neutral.add_file("encounter_vaegirs_neutral_4.ogg")


encounter_vaegirs_enemy = Sound("encounter_vaegirs_enemy")
encounter_vaegirs_enemy.add_flag(SoundFlag.IS_2D)
encounter_vaegirs_enemy.set_volume(8)
encounter_vaegirs_enemy.add_file("encounter_vaegirs_neutral.ogg")
encounter_vaegirs_enemy.add_file("encounter_vaegirs_neutral_2.ogg")
encounter_vaegirs_enemy.add_file("encounter_vaegirs_neutral_3.ogg")
encounter_vaegirs_enemy.add_file("encounter_vaegirs_neutral_4.ogg")


sneak_town_halt = Sound("sneak_town_halt")
sneak_town_halt.add_flag(SoundFlag.IS_2D)
sneak_town_halt.add_file("sneak_halt_1.ogg")
sneak_town_halt.add_file("sneak_halt_2.ogg")


horse_walk = Sound("horse_walk")
horse_walk.set_volume(5)
horse_walk.set_priority(3)
horse_walk.add_file("horse_walk_1.ogg")
horse_walk.add_file("horse_walk_2.ogg")
horse_walk.add_file("horse_walk_3.ogg")
horse_walk.add_file("horse_walk_4.ogg")


horse_trot = Sound("horse_trot")
horse_trot.set_volume(6)
horse_trot.set_priority(4)
horse_trot.add_file("horse_trot_1.ogg")
horse_trot.add_file("horse_trot_2.ogg")
horse_trot.add_file("horse_trot_3.ogg")
horse_trot.add_file("horse_trot_4.ogg")


horse_canter = Sound("horse_canter")
horse_canter.set_volume(7)
horse_canter.set_priority(4)
horse_canter.add_file("horse_canter_1.ogg")
horse_canter.add_file("horse_canter_2.ogg")
horse_canter.add_file("horse_canter_3.ogg")
horse_canter.add_file("horse_canter_4.ogg")


horse_gallop = Sound("horse_gallop")
horse_gallop.set_volume(8)
horse_gallop.set_priority(5)
horse_gallop.add_file("horse_gallop_6.ogg")
horse_gallop.add_file("horse_gallop_7.ogg")
horse_gallop.add_file("horse_gallop_8.ogg")
horse_gallop.add_file("horse_gallop_9.ogg")


horse_breath = Sound("horse_breath")
horse_breath.set_volume(4)
horse_breath.set_priority(1)
horse_breath.add_file("horse_breath_4.ogg")
horse_breath.add_file("horse_breath_5.ogg")
horse_breath.add_file("horse_breath_6.ogg")
horse_breath.add_file("horse_breath_7.ogg")


horse_snort = Sound("horse_snort")
horse_snort.set_volume(2)
horse_snort.set_priority(1)
horse_snort.add_file("horse_snort_1.ogg")
horse_snort.add_file("horse_snort_2.ogg")
horse_snort.add_file("horse_snort_3.ogg")
horse_snort.add_file("horse_snort_4.ogg")
horse_snort.add_file("horse_snort_5.ogg")


horse_low_whinny = Sound("horse_low_whinny")
horse_low_whinny.set_volume(12)
horse_low_whinny.add_file("horse_whinny-1.ogg")
horse_low_whinny.add_file("horse_whinny-2.ogg")


block_fist = Sound("block_fist")
block_fist.add_file("block_fist_3.ogg")
block_fist.add_file("block_fist_4.ogg")


man_hit_blunt_weak = Sound("man_hit_blunt_weak")
man_hit_blunt_weak.set_volume(10)
man_hit_blunt_weak.set_priority(5)
man_hit_blunt_weak.add_file("man_hit_13.ogg")
man_hit_blunt_weak.add_file("man_hit_29.ogg")
man_hit_blunt_weak.add_file("man_hit_32.ogg")
man_hit_blunt_weak.add_file("man_hit_47.ogg")
man_hit_blunt_weak.add_file("man_hit_57.ogg")


man_hit_blunt_strong = Sound("man_hit_blunt_strong")
man_hit_blunt_strong.set_volume(10)
man_hit_blunt_strong.set_priority(5)
man_hit_blunt_strong.add_file("man_hit_13.ogg")
man_hit_blunt_strong.add_file("man_hit_29.ogg")
man_hit_blunt_strong.add_file("man_hit_32.ogg")
man_hit_blunt_strong.add_file("man_hit_47.ogg")
man_hit_blunt_strong.add_file("man_hit_57.ogg")


man_hit_pierce_weak = Sound("man_hit_pierce_weak")
man_hit_pierce_weak.set_volume(10)
man_hit_pierce_weak.set_priority(5)
man_hit_pierce_weak.add_file("man_hit_13.ogg")
man_hit_pierce_weak.add_file("man_hit_29.ogg")
man_hit_pierce_weak.add_file("man_hit_32.ogg")
man_hit_pierce_weak.add_file("man_hit_47.ogg")
man_hit_pierce_weak.add_file("man_hit_57.ogg")


man_hit_pierce_strong = Sound("man_hit_pierce_strong")
man_hit_pierce_strong.set_volume(10)
man_hit_pierce_strong.set_priority(5)
man_hit_pierce_strong.add_file("man_hit_13.ogg")
man_hit_pierce_strong.add_file("man_hit_29.ogg")
man_hit_pierce_strong.add_file("man_hit_32.ogg")
man_hit_pierce_strong.add_file("man_hit_47.ogg")
man_hit_pierce_strong.add_file("man_hit_57.ogg")


man_hit_cut_weak = Sound("man_hit_cut_weak")
man_hit_cut_weak.set_volume(10)
man_hit_cut_weak.set_priority(5)
man_hit_cut_weak.add_file("man_hit_13.ogg")
man_hit_cut_weak.add_file("man_hit_29.ogg")
man_hit_cut_weak.add_file("man_hit_32.ogg")
man_hit_cut_weak.add_file("man_hit_47.ogg")
man_hit_cut_weak.add_file("man_hit_57.ogg")


man_hit_cut_strong = Sound("man_hit_cut_strong")
man_hit_cut_strong.set_volume(10)
man_hit_cut_strong.set_priority(5)
man_hit_cut_strong.add_file("man_hit_13.ogg")
man_hit_cut_strong.add_file("man_hit_29.ogg")
man_hit_cut_strong.add_file("man_hit_32.ogg")
man_hit_cut_strong.add_file("man_hit_47.ogg")
man_hit_cut_strong.add_file("man_hit_57.ogg")


man_victory = Sound("man_victory")
man_victory.set_volume(10)
man_victory.set_priority(5)
man_victory.add_file("man_victory_3.ogg")
man_victory.add_file("man_victory_4.ogg")
man_victory.add_file("man_victory_5.ogg")
man_victory.add_file("man_victory_8.ogg")
man_victory.add_file("man_victory_15.ogg")
man_victory.add_file("man_victory_49.ogg")
man_victory.add_file("man_victory_52.ogg")
man_victory.add_file("man_victory_54.ogg")
man_victory.add_file("man_victory_57.ogg")
man_victory.add_file("man_victory_71.ogg")


fire_loop = Sound("fire_loop")
fire_loop.add_flag(SoundFlag.LOOPING)
fire_loop.add_flag(SoundFlag.START_AT_RANDOM_POS)
fire_loop.set_volume(4)
fire_loop.set_priority(9)
fire_loop.add_file("Fire_Torch_Loop3.ogg")


torch_loop = Sound("torch_loop")
torch_loop.add_flag(SoundFlag.LOOPING)
torch_loop.add_flag(SoundFlag.START_AT_RANDOM_POS)
torch_loop.set_volume(4)
torch_loop.set_priority(9)
torch_loop.add_file("Fire_Torch_Loop3.ogg")


dummy_hit = Sound("dummy_hit")
dummy_hit.set_priority(9)
dummy_hit.add_file("shield_hit_cut_3.ogg")
dummy_hit.add_file("shield_hit_cut_5.ogg")


dummy_destroyed = Sound("dummy_destroyed")
dummy_destroyed.set_priority(9)
dummy_destroyed.add_file("shield_broken.ogg")


gourd_destroyed = Sound("gourd_destroyed")
gourd_destroyed.set_priority(9)
gourd_destroyed.add_file("shield_broken.ogg")


cow_moo = Sound("cow_moo")
cow_moo.add_flag(SoundFlag.IS_2D)
cow_moo.set_volume(8)
cow_moo.set_priority(9)
cow_moo.add_file("cow_moo_1.ogg")


cow_slaughter = Sound("cow_slaughter")
cow_slaughter.add_flag(SoundFlag.IS_2D)
cow_slaughter.set_volume(8)
cow_slaughter.set_priority(9)
cow_slaughter.add_file("cow_slaughter.ogg")


distant_dog_bark = Sound("distant_dog_bark")
distant_dog_bark.add_flag(SoundFlag.IS_2D)
distant_dog_bark.set_volume(8)
distant_dog_bark.set_priority(3)
distant_dog_bark.add_file("d_dog1.ogg")
distant_dog_bark.add_file("d_dog2.ogg")
distant_dog_bark.add_file("d_dog3.ogg")
distant_dog_bark.add_file("d_dog7.ogg")


distant_owl = Sound("distant_owl")
distant_owl.add_flag(SoundFlag.IS_2D)
distant_owl.set_volume(9)
distant_owl.set_priority(3)
distant_owl.add_file("d_owl2.ogg")
distant_owl.add_file("d_owl3.ogg")
distant_owl.add_file("d_owl4.ogg")


distant_chicken = Sound("distant_chicken")
distant_chicken.add_flag(SoundFlag.IS_2D)
distant_chicken.set_volume(8)
distant_chicken.set_priority(3)
distant_chicken.add_file("d_chicken1.ogg")
distant_chicken.add_file("d_chicken2.ogg")


distant_carpenter = Sound("distant_carpenter")
distant_carpenter.add_flag(SoundFlag.IS_2D)
distant_carpenter.set_volume(3)
distant_carpenter.set_priority(3)
distant_carpenter.add_file("d_carpenter1.ogg")
distant_carpenter.add_file("d_saw_short3.ogg")


distant_blacksmith = Sound("distant_blacksmith")
distant_blacksmith.add_flag(SoundFlag.IS_2D)
distant_blacksmith.set_volume(4)
distant_blacksmith.set_priority(3)
distant_blacksmith.add_file("d_blacksmith2.ogg")


arena_ambiance = Sound("arena_ambiance")
arena_ambiance.add_flag(SoundFlag.IS_2D)
arena_ambiance.add_flag(SoundFlag.LOOPING)
arena_ambiance.set_volume(3)
arena_ambiance.set_priority(8)
arena_ambiance.add_file("arena_loop11.ogg")


town_ambiance = Sound("town_ambiance")
town_ambiance.add_flag(SoundFlag.IS_2D)
town_ambiance.add_flag(SoundFlag.LOOPING)
town_ambiance.set_volume(3)
town_ambiance.set_priority(8)
town_ambiance.add_file("town_loop_3.ogg")


tutorial_fail = Sound("tutorial_fail")
tutorial_fail.add_flag(SoundFlag.IS_2D)
tutorial_fail.set_volume(7)
tutorial_fail.add_file("cue_failure.ogg")


your_flag_taken = Sound("your_flag_taken")
your_flag_taken.add_flag(SoundFlag.IS_2D)
your_flag_taken.set_volume(10)
your_flag_taken.set_priority(10)
your_flag_taken.add_file("your_flag_taken.ogg")


enemy_flag_taken = Sound("enemy_flag_taken")
enemy_flag_taken.add_flag(SoundFlag.IS_2D)
enemy_flag_taken.set_volume(10)
enemy_flag_taken.set_priority(10)
enemy_flag_taken.add_file("enemy_flag_taken.ogg")


flag_returned = Sound("flag_returned")
flag_returned.add_flag(SoundFlag.IS_2D)
flag_returned.set_volume(10)
flag_returned.set_priority(10)
flag_returned.add_file("your_flag_returned.ogg")


team_scored_a_point = Sound("team_scored_a_point")
team_scored_a_point.add_flag(SoundFlag.IS_2D)
team_scored_a_point.set_volume(10)
team_scored_a_point.set_priority(10)
team_scored_a_point.add_file("you_scored_a_point.ogg")


enemy_scored_a_point = Sound("enemy_scored_a_point")
enemy_scored_a_point.add_flag(SoundFlag.IS_2D)
enemy_scored_a_point.set_volume(10)
enemy_scored_a_point.set_priority(10)
enemy_scored_a_point.add_file("enemy_scored_a_point.ogg")


ccoop_spawn_companion_0 = Sound("ccoop_spawn_companion_0")
ccoop_spawn_companion_0.add_flag(SoundFlag.IS_2D)
ccoop_spawn_companion_0.set_volume(8)
ccoop_spawn_companion_0.add_file("encounter_farmer_2.ogg")


ccoop_spawn_companion_1 = Sound("ccoop_spawn_companion_1")
ccoop_spawn_companion_1.add_flag(SoundFlag.IS_2D)
ccoop_spawn_companion_1.set_volume(8)
ccoop_spawn_companion_1.add_file("encounter_farmer_5.ogg")


ccoop_spawn_companion_2 = Sound("ccoop_spawn_companion_2")
ccoop_spawn_companion_2.add_flag(SoundFlag.IS_2D)
ccoop_spawn_companion_2.set_volume(8)
ccoop_spawn_companion_2.add_file("encounter_farmer_7.ogg")


ccoop_spawn_companion_3 = Sound("ccoop_spawn_companion_3")
ccoop_spawn_companion_3.add_flag(SoundFlag.IS_2D)
ccoop_spawn_companion_3.set_volume(8)
ccoop_spawn_companion_3.add_file("encounter_farmer_9.ogg")


ccoop_nobleman_taunt = Sound("ccoop_nobleman_taunt")
ccoop_nobleman_taunt.add_flag(SoundFlag.IS_2D)
ccoop_nobleman_taunt.set_volume(8)
ccoop_nobleman_taunt.add_file("encounter_nobleman_1.ogg")


ccoop_looter_taunt_0 = Sound("ccoop_looter_taunt_0")
ccoop_looter_taunt_0.add_flag(SoundFlag.IS_2D)
ccoop_looter_taunt_0.set_volume(8)
ccoop_looter_taunt_0.add_file("encounter_river_pirates_5.ogg")


ccoop_looter_taunt_1 = Sound("ccoop_looter_taunt_1")
ccoop_looter_taunt_1.add_flag(SoundFlag.IS_2D)
ccoop_looter_taunt_1.set_volume(8)
ccoop_looter_taunt_1.add_file("encounter_river_pirates_6.ogg")


ccoop_looter_taunt_2 = Sound("ccoop_looter_taunt_2")
ccoop_looter_taunt_2.add_flag(SoundFlag.IS_2D)
ccoop_looter_taunt_2.set_volume(8)
ccoop_looter_taunt_2.add_file("encounter_river_pirates_9.ogg")


ccoop_looter_taunt_3 = Sound("ccoop_looter_taunt_3")
ccoop_looter_taunt_3.add_flag(SoundFlag.IS_2D)
ccoop_looter_taunt_3.set_volume(8)
ccoop_looter_taunt_3.add_file("encounter_river_pirates_10.ogg")


ccoop_looter_taunt_4 = Sound("ccoop_looter_taunt_4")
ccoop_looter_taunt_4.add_flag(SoundFlag.IS_2D)
ccoop_looter_taunt_4.set_volume(8)
ccoop_looter_taunt_4.add_file("encounter_river_pirates_4.ogg")


ccoop_bandit_taunt_0 = Sound("ccoop_bandit_taunt_0")
ccoop_bandit_taunt_0.add_flag(SoundFlag.IS_2D)
ccoop_bandit_taunt_0.set_volume(8)
ccoop_bandit_taunt_0.add_file("encounter_bandit_2.ogg")


ccoop_bandit_taunt_1 = Sound("ccoop_bandit_taunt_1")
ccoop_bandit_taunt_1.add_flag(SoundFlag.IS_2D)
ccoop_bandit_taunt_1.set_volume(8)
ccoop_bandit_taunt_1.add_file("encounter_bandit_9.ogg")


ccoop_bandit_taunt_2 = Sound("ccoop_bandit_taunt_2")
ccoop_bandit_taunt_2.add_flag(SoundFlag.IS_2D)
ccoop_bandit_taunt_2.set_volume(8)
ccoop_bandit_taunt_2.add_file("encounter_bandit_12.ogg")


ccoop_bandit_taunt_3 = Sound("ccoop_bandit_taunt_3")
ccoop_bandit_taunt_3.add_flag(SoundFlag.IS_2D)
ccoop_bandit_taunt_3.set_volume(8)
ccoop_bandit_taunt_3.add_file("encounter_bandit_13.ogg")


ccoop_bandit_taunt_4 = Sound("ccoop_bandit_taunt_4")
ccoop_bandit_taunt_4.add_flag(SoundFlag.IS_2D)
ccoop_bandit_taunt_4.set_volume(8)
ccoop_bandit_taunt_4.add_file("encounter_bandit_15.ogg")


ccoop_bandit_taunt_5 = Sound("ccoop_bandit_taunt_5")
ccoop_bandit_taunt_5.add_flag(SoundFlag.IS_2D)
ccoop_bandit_taunt_5.set_volume(8)
ccoop_bandit_taunt_5.add_file("encounter_bandit_16.ogg")


ccoop_bandit_taunt_6 = Sound("ccoop_bandit_taunt_6")
ccoop_bandit_taunt_6.add_flag(SoundFlag.IS_2D)
ccoop_bandit_taunt_6.set_volume(8)
ccoop_bandit_taunt_6.add_file("encounter_bandit_10.ogg")


ccoop_sea_raider_taunt_0 = Sound("ccoop_sea_raider_taunt_0")
ccoop_sea_raider_taunt_0.add_flag(SoundFlag.IS_2D)
ccoop_sea_raider_taunt_0.set_volume(8)
ccoop_sea_raider_taunt_0.add_file("encounter_sea_raider_5.ogg")


ccoop_sea_raider_taunt_1 = Sound("ccoop_sea_raider_taunt_1")
ccoop_sea_raider_taunt_1.add_flag(SoundFlag.IS_2D)
ccoop_sea_raider_taunt_1.set_volume(8)
ccoop_sea_raider_taunt_1.add_file("encounter_sea_raider_9.ogg")


ccoop_sea_raider_taunt_2 = Sound("ccoop_sea_raider_taunt_2")
ccoop_sea_raider_taunt_2.add_flag(SoundFlag.IS_2D)
ccoop_sea_raider_taunt_2.set_volume(8)
ccoop_sea_raider_taunt_2.add_file("encounter_sea_raider_9b.ogg")


ccoop_sea_raider_taunt_3 = Sound("ccoop_sea_raider_taunt_3")
ccoop_sea_raider_taunt_3.add_flag(SoundFlag.IS_2D)
ccoop_sea_raider_taunt_3.set_volume(8)
ccoop_sea_raider_taunt_3.add_file("encounter_sea_raider_10.ogg")


sounds_end = Sound("sounds_end")
sounds_end.add_flag(SoundFlag.IS_2D)
sounds_end.set_volume(10)
sounds_end.set_priority(10)
sounds_end.add_file("enemy_scored_a_point.ogg")


