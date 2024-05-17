# This Python file uses the following encoding: utf-8

from scene import Scene, SceneFlag
import troops as trp

#import sys
#sys.path.append("../data_objects/")


random_scene = Scene("random_scene", water_level=-0.5, terrain_code="0x300028000003e8fa0000034e00004b34000059be")
random_scene.add_flag(SceneFlag.GENERATE)
random_scene.add_flag(SceneFlag.RANDOMIZE)
random_scene.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
random_scene.set_min_pos(240.0, 240.0)


conversation_scene = Scene("conversation_scene", mesh_name="encounter_spot", body_name="bo_encounter_spot")
conversation_scene.set_min_pos(-40.0, -40.0)
conversation_scene.set_min_pos(40.0, 40.0)


water = Scene("water", water_level=-0.5)
water.set_min_pos(-1000.0, -1000.0)
water.set_min_pos(1000.0, 1000.0)


random_scene_steppe = Scene("random_scene_steppe", water_level=-0.5, terrain_code="0x0000000229602800000691a400003efe00004b34000059be", extra_terrain="outer_terrain_steppe")
random_scene_steppe.add_flag(SceneFlag.GENERATE)
random_scene_steppe.add_flag(SceneFlag.RANDOMIZE)
random_scene_steppe.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
random_scene_steppe.set_min_pos(240.0, 240.0)


random_scene_plain = Scene("random_scene_plain", water_level=-0.5, terrain_code="0x0000000229602800000691a400003efe00004b34000059be", extra_terrain="outer_terrain_plain")
random_scene_plain.add_flag(SceneFlag.GENERATE)
random_scene_plain.add_flag(SceneFlag.RANDOMIZE)
random_scene_plain.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
random_scene_plain.set_min_pos(240.0, 240.0)


random_scene_snow = Scene("random_scene_snow", water_level=-0.5, terrain_code="0x0000000229602800000691a400003efe00004b34000059be", extra_terrain="outer_terrain_snow")
random_scene_snow.add_flag(SceneFlag.GENERATE)
random_scene_snow.add_flag(SceneFlag.RANDOMIZE)
random_scene_snow.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
random_scene_snow.set_min_pos(240.0, 240.0)


random_scene_desert = Scene("random_scene_desert", water_level=-0.5, terrain_code="0x0000000229602800000691a400003efe00004b34000059be", extra_terrain="outer_terrain_desert_b")
random_scene_desert.add_flag(SceneFlag.GENERATE)
random_scene_desert.add_flag(SceneFlag.RANDOMIZE)
random_scene_desert.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
random_scene_desert.set_min_pos(240.0, 240.0)


random_scene_steppe_forest = Scene("random_scene_steppe_forest", water_level=-0.5, terrain_code="0x300028000003e8fa0000034e00004b34000059be", extra_terrain="outer_terrain_plain")
random_scene_steppe_forest.add_flag(SceneFlag.GENERATE)
random_scene_steppe_forest.add_flag(SceneFlag.RANDOMIZE)
random_scene_steppe_forest.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
random_scene_steppe_forest.set_min_pos(240.0, 240.0)


random_scene_plain_forest = Scene("random_scene_plain_forest", water_level=-0.5, terrain_code="0x300028000003e8fa0000034e00004b34000059be", extra_terrain="outer_terrain_plain")
random_scene_plain_forest.add_flag(SceneFlag.GENERATE)
random_scene_plain_forest.add_flag(SceneFlag.RANDOMIZE)
random_scene_plain_forest.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
random_scene_plain_forest.set_min_pos(240.0, 240.0)


random_scene_snow_forest = Scene("random_scene_snow_forest", water_level=-0.5, terrain_code="0x300028000003e8fa0000034e00004b34000059be", extra_terrain="outer_terrain_snow")
random_scene_snow_forest.add_flag(SceneFlag.GENERATE)
random_scene_snow_forest.add_flag(SceneFlag.RANDOMIZE)
random_scene_snow_forest.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
random_scene_snow_forest.set_min_pos(240.0, 240.0)


random_scene_desert_forest = Scene("random_scene_desert_forest", water_level=-0.5, terrain_code="0x300028000003e8fa0000034e00004b34000059be", extra_terrain="outer_terrain_desert")
random_scene_desert_forest.add_flag(SceneFlag.GENERATE)
random_scene_desert_forest.add_flag(SceneFlag.RANDOMIZE)
random_scene_desert_forest.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
random_scene_desert_forest.set_min_pos(240.0, 240.0)


camp_scene = Scene("camp_scene", water_level=-0.5, terrain_code="0x300028000003e8fa0000034e00004b34000059be", extra_terrain="outer_terrain_plain")
camp_scene.add_flag(SceneFlag.GENERATE)
camp_scene.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
camp_scene.set_min_pos(240.0, 240.0)


camp_scene_horse_track = Scene("camp_scene_horse_track", water_level=-0.5, terrain_code="0x300028000003e8fa0000034e00004b34000059be", extra_terrain="outer_terrain_plain")
camp_scene_horse_track.add_flag(SceneFlag.GENERATE)
camp_scene_horse_track.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
camp_scene_horse_track.set_min_pos(240.0, 240.0)


four_ways_inn = Scene("four_ways_inn", terrain_code="0x0000000030015f2b000350d4000011a4000017ee000054af", extra_terrain="outer_terrain_town_thir_1")
four_ways_inn.add_flag(SceneFlag.GENERATE)
four_ways_inn.set_min_pos(120.0, 120.0)


test_scene = Scene("test_scene", terrain_code="0x0230817a00028ca300007f4a0000479400161992", extra_terrain="outer_terrain_plain")
test_scene.add_flag(SceneFlag.GENERATE)
test_scene.set_min_pos(120.0, 120.0)


quick_battle_1 = Scene("quick_battle_1", terrain_code="0x30401ee300059966000001bf0000299a0000638f", extra_terrain="outer_terrain_plain")
quick_battle_1.add_flag(SceneFlag.GENERATE)
quick_battle_1.set_min_pos(120.0, 120.0)


quick_battle_2 = Scene("quick_battle_2", terrain_code="0xa0425ccf0004a92a000063d600005a8a00003d9a", extra_terrain="outer_terrain_steppe")
quick_battle_2.add_flag(SceneFlag.GENERATE)
quick_battle_2.set_min_pos(120.0, 120.0)


quick_battle_3 = Scene("quick_battle_3", terrain_code="0x4c6024e3000691a400001b7c0000591500007b52", extra_terrain="outer_terrain_snow")
quick_battle_3.add_flag(SceneFlag.GENERATE)
quick_battle_3.set_min_pos(120.0, 120.0)


quick_battle_4 = Scene("quick_battle_4", terrain_code="0x00001d63c005114300006228000053bf00004eb9", extra_terrain="outer_terrain_plain")
quick_battle_4.add_flag(SceneFlag.GENERATE)
quick_battle_4.set_min_pos(120.0, 120.0)


quick_battle_5 = Scene("quick_battle_5", terrain_code="0x3a078bb2000589630000667200002fb90000179c", extra_terrain="outer_terrain_plain")
quick_battle_5.add_flag(SceneFlag.GENERATE)
quick_battle_5.set_min_pos(120.0, 120.0)


quick_battle_6 = Scene("quick_battle_6", terrain_code="0xa0425ccf0004a92a000063d600005a8a00003d9a", extra_terrain="outer_terrain_steppe")
quick_battle_6.add_flag(SceneFlag.GENERATE)
quick_battle_6.set_min_pos(120.0, 120.0)


quick_battle_7 = Scene("quick_battle_7", terrain_code="0x314d060900036cd70000295300002ec9000025f3", extra_terrain="outer_terrain_plain")
quick_battle_7.add_flag(SceneFlag.GENERATE)


salt_mine = Scene("salt_mine", terrain_code="0x2a07b23200025896000023ee00007f9c000022a8", extra_terrain="outer_terrain_steppe")
salt_mine.add_flag(SceneFlag.GENERATE)
salt_mine.set_min_pos(-200.0, -200.0)
salt_mine.set_min_pos(200.0, 200.0)


novice_ground = Scene("novice_ground", mesh_name="training_house_a", body_name="bo_training_house_a")
novice_ground.add_flag(SceneFlag.IS_INDOORS)
novice_ground.set_min_pos(-100.0, -100.0)


zendar_arena = Scene("zendar_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_plain")
zendar_arena.add_flag(SceneFlag.GENERATE)


dhorak_keep = Scene("dhorak_keep", terrain_code="0x33a7946000028ca300007f4a0000479400161992")
dhorak_keep.add_flag(SceneFlag.GENERATE)
dhorak_keep.set_min_pos(120.0, 120.0)
dhorak_keep.add_accessible_scene("exit")


reserved4 = Scene("reserved4", terrain_code="28791")
reserved4.add_flag(SceneFlag.GENERATE)
reserved4.set_min_pos(120.0, 120.0)


reserved5 = Scene("reserved5", terrain_code="117828")
reserved5.add_flag(SceneFlag.GENERATE)
reserved5.set_min_pos(120.0, 120.0)


reserved6 = Scene("reserved6", terrain_code="6849")
reserved6.add_flag(SceneFlag.GENERATE)


reserved7 = Scene("reserved7", terrain_code="6849")
reserved7.add_flag(SceneFlag.GENERATE)


reserved8 = Scene("reserved8", terrain_code="13278")
reserved8.add_flag(SceneFlag.GENERATE)


reserved9 = Scene("reserved9", mesh_name="thirsty_lion", body_name="bo_thirsty_lion")
reserved9.add_flag(SceneFlag.IS_INDOORS)
reserved9.set_min_pos(-100.0, -100.0)


reserved10 = Scene("reserved10")
reserved10.set_min_pos(-100.0, -100.0)


reserved11 = Scene("reserved11")
reserved11.set_min_pos(-100.0, -100.0)


reserved12 = Scene("reserved12", mesh_name="thirsty_lion", body_name="bo_thirsty_lion")
reserved12.add_flag(SceneFlag.IS_INDOORS)
reserved12.set_min_pos(-100.0, -100.0)


training_ground = Scene("training_ground", terrain_code="0x30000500400360d80000189f00002a8380006d91", extra_terrain="outer_terrain_plain_1")
training_ground.add_flag(SceneFlag.GENERATE)
training_ground.set_min_pos(120.0, 120.0)
training_ground.add_chest_troop(trp.tutorial_chest_1)
training_ground.add_chest_troop(trp.tutorial_chest_2)


tutorial_1 = Scene("tutorial_1", mesh_name="tutorial_1_scene", body_name="bo_tutorial_1_scene")
tutorial_1.add_flag(SceneFlag.IS_INDOORS)
tutorial_1.set_min_pos(-100.0, -100.0)


tutorial_2 = Scene("tutorial_2", mesh_name="tutorial_2_scene", body_name="bo_tutorial_2_scene")
tutorial_2.add_flag(SceneFlag.IS_INDOORS)
tutorial_2.set_min_pos(-100.0, -100.0)


tutorial_3 = Scene("tutorial_3", mesh_name="tutorial_3_scene", body_name="bo_tutorial_3_scene")
tutorial_3.add_flag(SceneFlag.IS_INDOORS)
tutorial_3.set_min_pos(-100.0, -100.0)


tutorial_4 = Scene("tutorial_4", terrain_code="0x30000500400360d80000189f00002a8380006d91", extra_terrain="outer_terrain_plain")
tutorial_4.add_flag(SceneFlag.GENERATE)
tutorial_4.set_min_pos(120.0, 120.0)


tutorial_5 = Scene("tutorial_5", terrain_code="0x3a06dca80005715c0000537400001377000011fe", extra_terrain="outer_terrain_plain")
tutorial_5.add_flag(SceneFlag.GENERATE)
tutorial_5.set_min_pos(120.0, 120.0)


training_ground_horse_track_1 = Scene("training_ground_horse_track_1", terrain_code="0x00000000337553240004d53700000c0500002a0f80006267", extra_terrain="outer_terrain_plain")
training_ground_horse_track_1.add_flag(SceneFlag.GENERATE)
training_ground_horse_track_1.set_min_pos(120.0, 120.0)


training_ground_horse_track_2 = Scene("training_ground_horse_track_2", terrain_code="0x00000000301553240004d5370000466000002a0f800073f1", extra_terrain="outer_terrain_plain")
training_ground_horse_track_2.add_flag(SceneFlag.GENERATE)
training_ground_horse_track_2.set_min_pos(120.0, 120.0)


training_ground_horse_track_3 = Scene("training_ground_horse_track_3", terrain_code="0x00000000400c12b2000515470000216b0000485e00006928", extra_terrain="outer_terrain_snow")
training_ground_horse_track_3.add_flag(SceneFlag.GENERATE)
training_ground_horse_track_3.set_min_pos(120.0, 120.0)


training_ground_horse_track_4 = Scene("training_ground_horse_track_4", terrain_code="0x00000000200b60320004a5290000180d0000452f00000e90", extra_terrain="outer_terrain_steppe")
training_ground_horse_track_4.add_flag(SceneFlag.GENERATE)
training_ground_horse_track_4.set_min_pos(120.0, 120.0)


training_ground_horse_track_5 = Scene("training_ground_horse_track_5", terrain_code="0x000000003008208e0006419000000f730000440f00003c86", extra_terrain="outer_terrain_plain")
training_ground_horse_track_5.add_flag(SceneFlag.GENERATE)
training_ground_horse_track_5.set_min_pos(120.0, 120.0)


training_ground_ranged_melee_1 = Scene("training_ground_ranged_melee_1", terrain_code="0x00000001350455c20005194a000041cb00005ae800000ff5", extra_terrain="outer_terrain_plain")
training_ground_ranged_melee_1.add_flag(SceneFlag.GENERATE)
training_ground_ranged_melee_1.set_min_pos(120.0, 120.0)


training_ground_ranged_melee_2 = Scene("training_ground_ranged_melee_2", terrain_code="0x0000000532c8dccb0005194a000041cb00005ae800001bdd", extra_terrain="outer_terrain_plain")
training_ground_ranged_melee_2.add_flag(SceneFlag.GENERATE)
training_ground_ranged_melee_2.set_min_pos(120.0, 120.0)


training_ground_ranged_melee_3 = Scene("training_ground_ranged_melee_3", terrain_code="0x000000054327dcba0005194a00001b1d00005ae800004d63", extra_terrain="outer_terrain_snow")
training_ground_ranged_melee_3.add_flag(SceneFlag.GENERATE)
training_ground_ranged_melee_3.set_min_pos(120.0, 120.0)


training_ground_ranged_melee_4 = Scene("training_ground_ranged_melee_4", terrain_code="0x000000012247dcba0005194a000041ef00005ae8000050af", extra_terrain="outer_terrain_steppe")
training_ground_ranged_melee_4.add_flag(SceneFlag.GENERATE)
training_ground_ranged_melee_4.set_min_pos(120.0, 120.0)


training_ground_ranged_melee_5 = Scene("training_ground_ranged_melee_5", terrain_code="0x00000001324a9cba0005194a000041ef00005ae800003c55", extra_terrain="outer_terrain_plain")
training_ground_ranged_melee_5.add_flag(SceneFlag.GENERATE)
training_ground_ranged_melee_5.set_min_pos(120.0, 120.0)


zendar_center = Scene("zendar_center", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_plain_1")
zendar_center.add_flag(SceneFlag.GENERATE)


the_happy_boar = Scene("the_happy_boar", mesh_name="interior_town_house_f", body_name="bo_interior_town_house_f")
the_happy_boar.add_flag(SceneFlag.IS_INDOORS)
the_happy_boar.set_min_pos(-100.0, -100.0)
the_happy_boar.add_chest_troop(trp.zendar_chest)


zendar_merchant = Scene("zendar_merchant", mesh_name="interior_town_house_i", body_name="bo_interior_town_house_i")
zendar_merchant.add_flag(SceneFlag.IS_INDOORS)
zendar_merchant.set_min_pos(-100.0, -100.0)


town_1_center = Scene("town_1_center", terrain_code="0x000000003002498000035cd50000104100005e940000147b", extra_terrain="outer_terrain_town_thir_1")
town_1_center.add_flag(SceneFlag.GENERATE)
town_1_center.add_chest_troop(trp.bonus_chest_3)


town_2_center = Scene("town_2_center", terrain_code="0x0000000030015f2b000350d4000011a4000017ee000054af", extra_terrain="outer_terrain_town_thir_1")
town_2_center.add_flag(SceneFlag.GENERATE)
town_2_center.add_chest_troop(trp.bonus_chest_3)


town_3_center = Scene("town_3_center", terrain_code="0x00000000300214100003ecfb00002b930000051900002c29", extra_terrain="outer_terrain_plain")
town_3_center.add_flag(SceneFlag.GENERATE)


town_4_center = Scene("town_4_center", terrain_code="0x30001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_plain")
town_4_center.add_flag(SceneFlag.GENERATE)


town_5_center = Scene("town_5_center", terrain_code="0x00000000300214100003ecfb00002b930000051900002c29", extra_terrain="outer_terrain_plain")
town_5_center.add_flag(SceneFlag.GENERATE)
town_5_center.add_chest_troop(trp.bonus_chest_2)


town_6_center = Scene("town_6_center", terrain_code="0x00000002300491830004a529000036230000312a00003653", extra_terrain="outer_terrain_plain")
town_6_center.add_flag(SceneFlag.GENERATE)


town_7_center = Scene("town_7_center", terrain_code="0x00000001300785320004c93200002bc700005e48000008d2", extra_terrain="outer_terrain_plain")
town_7_center.add_flag(SceneFlag.GENERATE)


town_8_center = Scene("town_8_center", terrain_code="0x3000148000025896000074e600006c260000125a", extra_terrain="outer_terrain_plain")
town_8_center.add_flag(SceneFlag.GENERATE)


town_9_center = Scene("town_9_center", terrain_code="0x400790b20002c8b0000050d500006f8c00006dbd", extra_terrain="outer_terrain_snow")
town_9_center.add_flag(SceneFlag.GENERATE)


town_10_center = Scene("town_10_center", terrain_code="0x00000000200016da000364d9000060f500007591000064e7", extra_terrain="outer_terrain_steppe")
town_10_center.add_flag(SceneFlag.GENERATE)


town_11_center = Scene("town_11_center", terrain_code="0x400790b20002c8b0000050d500006f8c00006dbd", extra_terrain="outer_terrain_snow")
town_11_center.add_flag(SceneFlag.GENERATE)


town_12_center = Scene("town_12_center", terrain_code="0x3002cd340002b4ac00002ccd800026dc00000c1d", extra_terrain="outer_terrain_town_thir_1")
town_12_center.add_flag(SceneFlag.GENERATE)


town_13_center = Scene("town_13_center", terrain_code="0x300416a600035cd600007ee80000012100003fbc")
town_13_center.add_flag(SceneFlag.GENERATE)
town_13_center.add_chest_troop(trp.bonus_chest_1)


town_14_center = Scene("town_14_center", terrain_code="0x00000000200016da000364d9000060f500007591000064e7", extra_terrain="outer_terrain_steppe")
town_14_center.add_flag(SceneFlag.GENERATE)


town_15_center = Scene("town_15_center", terrain_code="0x0000000030024e108003fd0100007bd300006c31000061aa", extra_terrain="outer_terrain_plain")
town_15_center.add_flag(SceneFlag.GENERATE)


town_16_center = Scene("town_16_center", terrain_code="0x0000000130001887000334d0000073ed00004f1a00007a35", extra_terrain="outer_terrain_steppe")
town_16_center.add_flag(SceneFlag.GENERATE)


town_17_center = Scene("town_17_center", terrain_code="0x0000000020045abc000308c4000029d9000033bd000009b9", extra_terrain="outer_terrain_steppe")
town_17_center.add_flag(SceneFlag.GENERATE)


town_18_center = Scene("town_18_center", terrain_code="0x0000000020049cbd00025896000048e90000164400002b3f", extra_terrain="outer_terrain_steppe")
town_18_center.add_flag(SceneFlag.GENERATE)


town_19_center = Scene("town_19_center", terrain_code="0x0000000020049cbd00025896000048e90000164400002b3f", extra_terrain="outer_terrain_steppe")
town_19_center.add_flag(SceneFlag.GENERATE)


town_20_center = Scene("town_20_center", terrain_code="0x00000a0650001e9a00a505418000581f000028c800000143", extra_terrain="outer_terrain_desert")
town_20_center.add_flag(SceneFlag.GENERATE)


town_21_center = Scene("town_21_center", terrain_code="0x0000000150051a800004190400003f8c0000352b000014d8", extra_terrain="outer_terrain_desert")
town_21_center.add_flag(SceneFlag.GENERATE)


town_22_center = Scene("town_22_center", terrain_code="0x000000025a03253200042d08000079d6000004fd00006910", extra_terrain="outer_terrain_desert")
town_22_center.add_flag(SceneFlag.GENERATE)


town_1_castle = Scene("town_1_castle", mesh_name="viking_interior_keep_a", body_name="bo_viking_interior_keep_a")
town_1_castle.add_flag(SceneFlag.IS_INDOORS)
town_1_castle.set_min_pos(-100.0, -100.0)
town_1_castle.add_accessible_scene("exit")
town_1_castle.add_chest_troop(trp.town_1_seneschal)


town_2_castle = Scene("town_2_castle", mesh_name="viking_interior_keep_a", body_name="bo_viking_interior_keep_a")
town_2_castle.add_flag(SceneFlag.IS_INDOORS)
town_2_castle.set_min_pos(-100.0, -100.0)
town_2_castle.add_accessible_scene("exit")
town_2_castle.add_chest_troop(trp.town_2_seneschal)


town_3_castle = Scene("town_3_castle", mesh_name="castle_h_interior_b", body_name="bo_castle_h_interior_b")
town_3_castle.add_flag(SceneFlag.IS_INDOORS)
town_3_castle.set_min_pos(-100.0, -100.0)
town_3_castle.add_accessible_scene("exit")
town_3_castle.add_chest_troop(trp.town_3_seneschal)


town_4_castle = Scene("town_4_castle", mesh_name="interior_castle_q", body_name="bo_interior_castle_q")
town_4_castle.add_flag(SceneFlag.IS_INDOORS)
town_4_castle.set_min_pos(-100.0, -100.0)
town_4_castle.add_accessible_scene("exit")
town_4_castle.add_chest_troop(trp.town_4_seneschal)


town_5_castle = Scene("town_5_castle", mesh_name="castle_h_interior_a", body_name="bo_castle_h_interior_a")
town_5_castle.add_flag(SceneFlag.IS_INDOORS)
town_5_castle.set_min_pos(-100.0, -100.0)
town_5_castle.add_accessible_scene("exit")
town_5_castle.add_chest_troop(trp.town_5_seneschal)


town_6_castle = Scene("town_6_castle", mesh_name="interior_castle_z", body_name="bo_interior_castle_z")
town_6_castle.add_flag(SceneFlag.IS_INDOORS)
town_6_castle.set_min_pos(-100.0, -100.0)
town_6_castle.add_accessible_scene("exit")
town_6_castle.add_chest_troop(trp.town_6_seneschal)


town_7_castle = Scene("town_7_castle", mesh_name="interior_castle_v", body_name="bo_interior_castle_v")
town_7_castle.add_flag(SceneFlag.IS_INDOORS)
town_7_castle.set_min_pos(-100.0, -100.0)
town_7_castle.add_accessible_scene("exit")
town_7_castle.add_chest_troop(trp.town_7_seneschal)


town_8_castle = Scene("town_8_castle", mesh_name="interior_castle_w", body_name="bo_interior_castle_w")
town_8_castle.add_flag(SceneFlag.IS_INDOORS)
town_8_castle.set_min_pos(-100.0, -100.0)
town_8_castle.add_accessible_scene("exit")
town_8_castle.add_chest_troop(trp.town_8_seneschal)


town_9_castle = Scene("town_9_castle", mesh_name="interior_castle_g", body_name="bo_interior_castle_g")
town_9_castle.add_flag(SceneFlag.IS_INDOORS)
town_9_castle.set_min_pos(-100.0, -100.0)
town_9_castle.add_accessible_scene("exit")
town_9_castle.add_chest_troop(trp.town_9_seneschal)


town_10_castle = Scene("town_10_castle", terrain_code="0x00000007300005000002308c00004a840000624700004fda")
town_10_castle.add_flag(SceneFlag.GENERATE)
town_10_castle.set_min_pos(-100.0, -100.0)
town_10_castle.add_accessible_scene("exit")
town_10_castle.add_chest_troop(trp.town_10_seneschal)


town_11_castle = Scene("town_11_castle", mesh_name="interior_castle_i", body_name="bo_interior_castle_i")
town_11_castle.add_flag(SceneFlag.IS_INDOORS)
town_11_castle.set_min_pos(-100.0, -100.0)
town_11_castle.add_accessible_scene("exit")
town_11_castle.add_chest_troop(trp.town_11_seneschal)


town_12_castle = Scene("town_12_castle", mesh_name="viking_interior_keep_a", body_name="bo_viking_interior_keep_a")
town_12_castle.add_flag(SceneFlag.IS_INDOORS)
town_12_castle.set_min_pos(-100.0, -100.0)
town_12_castle.add_accessible_scene("exit")
town_12_castle.add_chest_troop(trp.town_12_seneschal)


town_13_castle = Scene("town_13_castle", mesh_name="interior_castle_b", body_name="bo_interior_castle_b")
town_13_castle.add_flag(SceneFlag.IS_INDOORS)
town_13_castle.set_min_pos(-100.0, -100.0)
town_13_castle.add_accessible_scene("exit")
town_13_castle.add_chest_troop(trp.town_13_seneschal)


town_14_castle = Scene("town_14_castle", mesh_name="interior_castle_g_square_keep", body_name="bo_interior_castle_g_square_keep")
town_14_castle.add_flag(SceneFlag.IS_INDOORS)
town_14_castle.set_min_pos(-100.0, -100.0)
town_14_castle.add_accessible_scene("exit")
town_14_castle.add_chest_troop(trp.town_14_seneschal)


town_15_castle = Scene("town_15_castle", mesh_name="castle_h_interior_a", body_name="bo_castle_h_interior_a")
town_15_castle.add_flag(SceneFlag.IS_INDOORS)
town_15_castle.set_min_pos(-100.0, -100.0)
town_15_castle.add_accessible_scene("exit")
town_15_castle.add_chest_troop(trp.town_15_seneschal)


town_16_castle = Scene("town_16_castle", mesh_name="interior_castle_n", body_name="bo_interior_castle_n")
town_16_castle.add_flag(SceneFlag.IS_INDOORS)
town_16_castle.set_min_pos(-100.0, -100.0)
town_16_castle.add_accessible_scene("exit")
town_16_castle.add_chest_troop(trp.town_16_seneschal)


town_17_castle = Scene("town_17_castle", mesh_name="interior_castle_g_square_keep", body_name="bo_interior_castle_g_square_keep")
town_17_castle.add_flag(SceneFlag.IS_INDOORS)
town_17_castle.set_min_pos(-100.0, -100.0)
town_17_castle.add_accessible_scene("exit")
town_17_castle.add_chest_troop(trp.town_17_seneschal)


town_18_castle = Scene("town_18_castle", terrain_code="0x00000007300005000002308c00004a840000624700004fda")
town_18_castle.add_flag(SceneFlag.GENERATE)
town_18_castle.set_min_pos(-100.0, -100.0)
town_18_castle.add_accessible_scene("exit")
town_18_castle.add_chest_troop(trp.town_18_seneschal)


town_19_castle = Scene("town_19_castle", mesh_name="arabian_interior_keep_a", body_name="bo_arabian_interior_keep_a")
town_19_castle.add_flag(SceneFlag.IS_INDOORS)
town_19_castle.set_min_pos(-100.0, -100.0)
town_19_castle.add_accessible_scene("exit")
town_19_castle.add_chest_troop(trp.town_19_seneschal)


town_20_castle = Scene("town_20_castle", mesh_name="arabian_interior_keep_b", body_name="bo_arabian_interior_keep_b")
town_20_castle.add_flag(SceneFlag.IS_INDOORS)
town_20_castle.set_min_pos(-100.0, -100.0)
town_20_castle.add_accessible_scene("exit")
town_20_castle.add_chest_troop(trp.town_20_seneschal)


town_21_castle = Scene("town_21_castle", mesh_name="arabian_interior_keep_b", body_name="bo_arabian_interior_keep_b")
town_21_castle.add_flag(SceneFlag.IS_INDOORS)
town_21_castle.set_min_pos(-100.0, -100.0)
town_21_castle.add_accessible_scene("exit")
town_21_castle.add_chest_troop(trp.town_21_seneschal)


town_22_castle = Scene("town_22_castle", mesh_name="arabian_interior_keep_a", body_name="bo_arabian_interior_keep_a", terrain_code="0x00000007300005000002308c00004a840000624700004fda")
town_22_castle.add_flag(SceneFlag.IS_INDOORS)
town_22_castle.set_min_pos(-100.0, -100.0)
town_22_castle.add_accessible_scene("exit")
town_22_castle.add_chest_troop(trp.town_22_seneschal)


town_1_tavern = Scene("town_1_tavern", mesh_name="viking_interior_tavern_a", body_name="bo_viking_interior_tavern_a")
town_1_tavern.add_flag(SceneFlag.IS_INDOORS)
town_1_tavern.set_min_pos(-100.0, -100.0)
town_1_tavern.add_accessible_scene("exit")


town_2_tavern = Scene("town_2_tavern", mesh_name="viking_interior_tavern_a", body_name="bo_viking_interior_tavern_a", extra_terrain="outer_terrain_town_thir_1")
town_2_tavern.add_flag(SceneFlag.IS_INDOORS)
town_2_tavern.set_min_pos(-100.0, -100.0)
town_2_tavern.add_accessible_scene("exit")


town_3_tavern = Scene("town_3_tavern", mesh_name="interior_rhodok_houses_b", body_name="bo_interior_rhodok_houses_b")
town_3_tavern.add_flag(SceneFlag.IS_INDOORS)
town_3_tavern.set_min_pos(-100.0, -100.0)
town_3_tavern.add_accessible_scene("exit")


town_4_tavern = Scene("town_4_tavern", mesh_name="interior_tavern_f", body_name="bo_interior_tavern_f")
town_4_tavern.add_flag(SceneFlag.IS_INDOORS)
town_4_tavern.set_min_pos(-100.0, -100.0)
town_4_tavern.add_accessible_scene("exit")


town_5_tavern = Scene("town_5_tavern", mesh_name="interior_rhodok_houses_d", body_name="bo_interior_rhodok_houses_d")
town_5_tavern.add_flag(SceneFlag.IS_INDOORS)
town_5_tavern.set_min_pos(-100.0, -100.0)
town_5_tavern.add_accessible_scene("exit")


town_6_tavern = Scene("town_6_tavern", mesh_name="interior_tavern_g", body_name="bo_interior_tavern_g")
town_6_tavern.add_flag(SceneFlag.IS_INDOORS)
town_6_tavern.set_min_pos(-100.0, -100.0)
town_6_tavern.add_accessible_scene("exit")


town_7_tavern = Scene("town_7_tavern", mesh_name="interior_town_house_f", body_name="bo_interior_town_house_f")
town_7_tavern.add_flag(SceneFlag.IS_INDOORS)
town_7_tavern.set_min_pos(-100.0, -100.0)
town_7_tavern.add_accessible_scene("exit")


town_8_tavern = Scene("town_8_tavern", mesh_name="interior_tavern_h", body_name="bo_interior_tavern_h")
town_8_tavern.add_flag(SceneFlag.IS_INDOORS)
town_8_tavern.set_min_pos(-100.0, -100.0)
town_8_tavern.add_accessible_scene("exit")


town_9_tavern = Scene("town_9_tavern", mesh_name="interior_tavern_g", body_name="bo_interior_tavern_g")
town_9_tavern.add_flag(SceneFlag.IS_INDOORS)
town_9_tavern.set_min_pos(-100.0, -100.0)
town_9_tavern.add_accessible_scene("exit")


town_10_tavern = Scene("town_10_tavern", mesh_name="interior_town_house_steppe_c", body_name="bo_interior_town_house_steppe_c")
town_10_tavern.add_flag(SceneFlag.IS_INDOORS)
town_10_tavern.set_min_pos(-100.0, -100.0)
town_10_tavern.add_accessible_scene("exit")


town_11_tavern = Scene("town_11_tavern", mesh_name="interior_tavern_c", body_name="bo_interior_tavern_c")
town_11_tavern.add_flag(SceneFlag.IS_INDOORS)
town_11_tavern.set_min_pos(-100.0, -100.0)
town_11_tavern.add_accessible_scene("exit")


town_12_tavern = Scene("town_12_tavern", mesh_name="viking_interior_tavern_a", body_name="bo_viking_interior_tavern_a")
town_12_tavern.add_flag(SceneFlag.IS_INDOORS)
town_12_tavern.set_min_pos(-100.0, -100.0)
town_12_tavern.add_accessible_scene("exit")


town_13_tavern = Scene("town_13_tavern", mesh_name="interior_tavern_g", body_name="bo_interior_tavern_g")
town_13_tavern.add_flag(SceneFlag.IS_INDOORS)
town_13_tavern.set_min_pos(-100.0, -100.0)
town_13_tavern.add_accessible_scene("exit")


town_14_tavern = Scene("town_14_tavern", mesh_name="interior_town_house_steppe_g", body_name="bo_interior_town_house_steppe_g")
town_14_tavern.add_flag(SceneFlag.IS_INDOORS)
town_14_tavern.set_min_pos(-100.0, -100.0)
town_14_tavern.add_accessible_scene("exit")


town_15_tavern = Scene("town_15_tavern", mesh_name="interior_rhodok_houses_d", body_name="bo_interior_rhodok_houses_d")
town_15_tavern.add_flag(SceneFlag.IS_INDOORS)
town_15_tavern.set_min_pos(-100.0, -100.0)
town_15_tavern.add_accessible_scene("exit")


town_16_tavern = Scene("town_16_tavern", mesh_name="interior_tavern_b", body_name="bo_interior_tavern_b")
town_16_tavern.add_flag(SceneFlag.IS_INDOORS)
town_16_tavern.set_min_pos(-100.0, -100.0)
town_16_tavern.add_accessible_scene("exit")


town_17_tavern = Scene("town_17_tavern", mesh_name="interior_town_house_steppe_g", body_name="bo_interior_town_house_steppe_g")
town_17_tavern.add_flag(SceneFlag.IS_INDOORS)
town_17_tavern.set_min_pos(-100.0, -100.0)
town_17_tavern.add_accessible_scene("exit")


town_18_tavern = Scene("town_18_tavern", mesh_name="interior_town_house_steppe_c", body_name="bo_interior_town_house_steppe_c")
town_18_tavern.add_flag(SceneFlag.IS_INDOORS)
town_18_tavern.set_min_pos(-100.0, -100.0)
town_18_tavern.add_accessible_scene("exit")


town_19_tavern = Scene("town_19_tavern", mesh_name="interior_town_house_steppe_d", body_name="bo_interior_town_house_steppe_d")
town_19_tavern.add_flag(SceneFlag.IS_INDOORS)
town_19_tavern.set_min_pos(-100.0, -100.0)
town_19_tavern.add_accessible_scene("exit")


town_20_tavern = Scene("town_20_tavern", mesh_name="interior_town_house_steppe_c", body_name="bo_interior_town_house_steppe_c")
town_20_tavern.add_flag(SceneFlag.IS_INDOORS)
town_20_tavern.set_min_pos(-100.0, -100.0)
town_20_tavern.add_accessible_scene("exit")


town_21_tavern = Scene("town_21_tavern", mesh_name="interior_town_house_steppe_g", body_name="bo_interior_town_house_steppe_g")
town_21_tavern.add_flag(SceneFlag.IS_INDOORS)
town_21_tavern.set_min_pos(-100.0, -100.0)
town_21_tavern.add_accessible_scene("exit")


town_22_tavern = Scene("town_22_tavern", mesh_name="interior_town_house_steppe_c", body_name="bo_interior_town_house_steppe_c")
town_22_tavern.add_flag(SceneFlag.IS_INDOORS)
town_22_tavern.set_min_pos(-100.0, -100.0)
town_22_tavern.add_accessible_scene("exit")


town_1_store = Scene("town_1_store", mesh_name="viking_interior_merchant_a", body_name="bo_viking_interior_merchant_a")
town_1_store.add_flag(SceneFlag.IS_INDOORS)
town_1_store.set_min_pos(-100.0, -100.0)
town_1_store.add_accessible_scene("exit")


town_2_store = Scene("town_2_store", mesh_name="viking_interior_merchant_a", body_name="bo_viking_interior_merchant_a")
town_2_store.add_flag(SceneFlag.IS_INDOORS)
town_2_store.set_min_pos(-100.0, -100.0)
town_2_store.add_accessible_scene("exit")


town_3_store = Scene("town_3_store", mesh_name="interior_rhodok_houses_d", body_name="bo_interior_rhodok_houses_d")
town_3_store.add_flag(SceneFlag.IS_INDOORS)
town_3_store.set_min_pos(-100.0, -100.0)
town_3_store.add_accessible_scene("exit")


town_4_store = Scene("town_4_store", mesh_name="interior_town_house_a", body_name="bo_interior_town_house_a")
town_4_store.add_flag(SceneFlag.IS_INDOORS)
town_4_store.set_min_pos(-100.0, -100.0)
town_4_store.add_accessible_scene("exit")


town_5_store = Scene("town_5_store", mesh_name="interior_rhodok_houses_b", body_name="bo_interior_rhodok_houses_b")
town_5_store.add_flag(SceneFlag.IS_INDOORS)
town_5_store.set_min_pos(-100.0, -100.0)
town_5_store.add_accessible_scene("exit")


town_6_store = Scene("town_6_store", mesh_name="interior_town_house_j", body_name="bo_interior_town_house_j")
town_6_store.add_flag(SceneFlag.IS_INDOORS)
town_6_store.set_min_pos(-100.0, -100.0)
town_6_store.add_accessible_scene("exit")


town_7_store = Scene("town_7_store", mesh_name="interior_house_a", body_name="bo_interior_house_a")
town_7_store.add_flag(SceneFlag.IS_INDOORS)
town_7_store.set_min_pos(-100.0, -100.0)
town_7_store.add_accessible_scene("exit")


town_8_store = Scene("town_8_store", mesh_name="interior_house_b", body_name="bo_interior_house_b")
town_8_store.add_flag(SceneFlag.IS_INDOORS)
town_8_store.set_min_pos(-100.0, -100.0)
town_8_store.add_accessible_scene("exit")


town_9_store = Scene("town_9_store", mesh_name="interior_tavern_a", body_name="bo_interior_tavern_a")
town_9_store.add_flag(SceneFlag.IS_INDOORS)
town_9_store.set_min_pos(-100.0, -100.0)
town_9_store.add_accessible_scene("exit")


town_10_store = Scene("town_10_store", mesh_name="interior_town_house_steppe_d", body_name="bo_interior_town_house_steppe_d")
town_10_store.add_flag(SceneFlag.IS_INDOORS)
town_10_store.set_min_pos(-100.0, -100.0)
town_10_store.add_accessible_scene("exit")


town_11_store = Scene("town_11_store", mesh_name="interior_town_house_j", body_name="bo_interior_town_house_j")
town_11_store.add_flag(SceneFlag.IS_INDOORS)
town_11_store.set_min_pos(-100.0, -100.0)
town_11_store.add_accessible_scene("exit")


town_12_store = Scene("town_12_store", mesh_name="viking_interior_merchant_a", body_name="bo_viking_interior_merchant_a")
town_12_store.add_flag(SceneFlag.IS_INDOORS)
town_12_store.set_min_pos(-100.0, -100.0)
town_12_store.add_accessible_scene("exit")


town_13_store = Scene("town_13_store", mesh_name="interior_town_house_j", body_name="bo_interior_town_house_j")
town_13_store.add_flag(SceneFlag.IS_INDOORS)
town_13_store.set_min_pos(-100.0, -100.0)
town_13_store.add_accessible_scene("exit")


town_14_store = Scene("town_14_store", mesh_name="interior_house_extension_h", body_name="bo_interior_house_extension_h")
town_14_store.add_flag(SceneFlag.IS_INDOORS)
town_14_store.set_min_pos(-100.0, -100.0)
town_14_store.add_accessible_scene("exit")


town_15_store = Scene("town_15_store", mesh_name="interior_rhodok_houses_b", body_name="bo_interior_rhodok_houses_b")
town_15_store.add_flag(SceneFlag.IS_INDOORS)
town_15_store.set_min_pos(-100.0, -100.0)
town_15_store.add_accessible_scene("exit")


town_16_store = Scene("town_16_store", mesh_name="interior_town_house_i", body_name="bo_interior_town_house_i")
town_16_store.add_flag(SceneFlag.IS_INDOORS)
town_16_store.set_min_pos(-100.0, -100.0)
town_16_store.add_accessible_scene("exit")


town_17_store = Scene("town_17_store", mesh_name="interior_town_house_steppe_g", body_name="bo_interior_town_house_steppe_g")
town_17_store.add_flag(SceneFlag.IS_INDOORS)
town_17_store.set_min_pos(-100.0, -100.0)
town_17_store.add_accessible_scene("exit")


town_18_store = Scene("town_18_store", mesh_name="interior_town_house_steppe_d", body_name="bo_interior_town_house_steppe_d")
town_18_store.add_flag(SceneFlag.IS_INDOORS)
town_18_store.set_min_pos(-100.0, -100.0)
town_18_store.add_accessible_scene("exit")


town_19_store = Scene("town_19_store", mesh_name="interior_town_house_steppe_d", body_name="bo_interior_town_house_steppe_d")
town_19_store.add_flag(SceneFlag.IS_INDOORS)
town_19_store.set_min_pos(-100.0, -100.0)
town_19_store.add_accessible_scene("exit")


town_20_store = Scene("town_20_store", mesh_name="interior_town_house_steppe_d", body_name="bo_interior_town_house_steppe_d")
town_20_store.add_flag(SceneFlag.IS_INDOORS)
town_20_store.set_min_pos(-100.0, -100.0)
town_20_store.add_accessible_scene("exit")


town_21_store = Scene("town_21_store", mesh_name="interior_town_house_steppe_g", body_name="bo_interior_town_house_steppe_g")
town_21_store.add_flag(SceneFlag.IS_INDOORS)
town_21_store.set_min_pos(-100.0, -100.0)
town_21_store.add_accessible_scene("exit")


town_22_store = Scene("town_22_store", mesh_name="interior_town_house_steppe_d", body_name="bo_interior_town_house_steppe_d")
town_22_store.add_flag(SceneFlag.IS_INDOORS)
town_22_store.set_min_pos(-100.0, -100.0)
town_22_store.add_accessible_scene("exit")


town_1_arena = Scene("town_1_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_plain")
town_1_arena.add_flag(SceneFlag.GENERATE)


town_2_arena = Scene("town_2_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_town_thir_1")
town_2_arena.add_flag(SceneFlag.GENERATE)


town_3_arena = Scene("town_3_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c")
town_3_arena.add_flag(SceneFlag.GENERATE)


town_4_arena = Scene("town_4_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_plain")
town_4_arena.add_flag(SceneFlag.GENERATE)


town_5_arena = Scene("town_5_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_plain")
town_5_arena.add_flag(SceneFlag.GENERATE)


town_6_arena = Scene("town_6_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_plain")
town_6_arena.add_flag(SceneFlag.GENERATE)


town_7_arena = Scene("town_7_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_plain")
town_7_arena.add_flag(SceneFlag.GENERATE)


town_8_arena = Scene("town_8_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_plain")
town_8_arena.add_flag(SceneFlag.GENERATE)


town_9_arena = Scene("town_9_arena", terrain_code="0x40001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_snow")
town_9_arena.add_flag(SceneFlag.GENERATE)


town_10_arena = Scene("town_10_arena", terrain_code="0x00000002200005000005f57b00005885000046bd00006d9c", extra_terrain="outer_terrain_steppe")
town_10_arena.add_flag(SceneFlag.GENERATE)


town_11_arena = Scene("town_11_arena", terrain_code="0x40001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_snow")
town_11_arena.add_flag(SceneFlag.GENERATE)


town_12_arena = Scene("town_12_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_town_thir_1")
town_12_arena.add_flag(SceneFlag.GENERATE)


town_13_arena = Scene("town_13_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c")
town_13_arena.add_flag(SceneFlag.GENERATE)


town_14_arena = Scene("town_14_arena", terrain_code="0x00000002200005000005f57b00005885000046bd00006d9c", extra_terrain="outer_terrain_steppe")
town_14_arena.add_flag(SceneFlag.GENERATE)


town_15_arena = Scene("town_15_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_plain")
town_15_arena.add_flag(SceneFlag.GENERATE)


town_16_arena = Scene("town_16_arena", terrain_code="0xa0001d9300031ccb0000156f000048ba0000361c", extra_terrain="outer_terrain_plain")
town_16_arena.add_flag(SceneFlag.GENERATE)


town_17_arena = Scene("town_17_arena", terrain_code="0x00000002200005000005f57b00005885000046bd00006d9c", extra_terrain="outer_terrain_steppe")
town_17_arena.add_flag(SceneFlag.GENERATE)


town_18_arena = Scene("town_18_arena", terrain_code="0x00000002200005000005f57b00005885000046bd00006d9c", extra_terrain="outer_terrain_steppe")
town_18_arena.add_flag(SceneFlag.GENERATE)


town_19_arena = Scene("town_19_arena", terrain_code="0x00000002200005000005f57b00005885000046bd00006d9c", extra_terrain="outer_terrain_desert")
town_19_arena.add_flag(SceneFlag.GENERATE)


town_20_arena = Scene("town_20_arena", terrain_code="0x00000002200005000005f57b00005885000046bd00006d9c", extra_terrain="outer_terrain_desert")
town_20_arena.add_flag(SceneFlag.GENERATE)


town_21_arena = Scene("town_21_arena", terrain_code="0x00000002200005000005f57b00005885000046bd00006d9c", extra_terrain="outer_terrain_desert")
town_21_arena.add_flag(SceneFlag.GENERATE)


town_22_arena = Scene("town_22_arena", terrain_code="0x00000002200005000005f57b00005885000046bd00006d9c", extra_terrain="outer_terrain_desert")
town_22_arena.add_flag(SceneFlag.GENERATE)


town_1_prison = Scene("town_1_prison", mesh_name="interior_prison_cell_a", body_name="bo_interior_prison_cell_a")
town_1_prison.add_flag(SceneFlag.IS_INDOORS)
town_1_prison.set_min_pos(-100.0, -100.0)


town_2_prison = Scene("town_2_prison", mesh_name="interior_prison_cell_a", body_name="bo_interior_prison_cell_a")
town_2_prison.add_flag(SceneFlag.IS_INDOORS)
town_2_prison.set_min_pos(-100.0, -100.0)


town_3_prison = Scene("town_3_prison", mesh_name="interior_prison_f", body_name="bo_interior_prison_f")
town_3_prison.add_flag(SceneFlag.IS_INDOORS)
town_3_prison.set_min_pos(-100.0, -100.0)


town_4_prison = Scene("town_4_prison", mesh_name="interior_prison_g", body_name="bo_interior_prison_g")
town_4_prison.add_flag(SceneFlag.IS_INDOORS)
town_4_prison.set_min_pos(-100.0, -100.0)


town_5_prison = Scene("town_5_prison", mesh_name="interior_prison_f", body_name="bo_interior_prison_f")
town_5_prison.add_flag(SceneFlag.IS_INDOORS)
town_5_prison.set_min_pos(-100.0, -100.0)
town_5_prison.add_accessible_scene("exit")


town_6_prison = Scene("town_6_prison", mesh_name="interior_prison_e", body_name="bo_interior_prison_e")
town_6_prison.add_flag(SceneFlag.IS_INDOORS)
town_6_prison.set_min_pos(-100.0, -100.0)
town_6_prison.add_accessible_scene("exit")


town_7_prison = Scene("town_7_prison", mesh_name="interior_prison_i", body_name="bo_interior_prison_i")
town_7_prison.add_flag(SceneFlag.IS_INDOORS)
town_7_prison.set_min_pos(-100.0, -100.0)
town_7_prison.add_accessible_scene("exit")


town_8_prison = Scene("town_8_prison", mesh_name="dungeon_cell_b", body_name="bo_dungeon_cell_b")
town_8_prison.add_flag(SceneFlag.IS_INDOORS)
town_8_prison.set_min_pos(-100.0, -100.0)
town_8_prison.add_accessible_scene("exit")


town_9_prison = Scene("town_9_prison", mesh_name="interior_prison_j", body_name="bo_interior_prison_j")
town_9_prison.add_flag(SceneFlag.IS_INDOORS)
town_9_prison.set_min_pos(-100.0, -100.0)
town_9_prison.add_accessible_scene("exit")


town_10_prison = Scene("town_10_prison", mesh_name="interior_prison_o", body_name="bo_interior_prison_o")
town_10_prison.add_flag(SceneFlag.IS_INDOORS)
town_10_prison.set_min_pos(-100.0, -100.0)
town_10_prison.add_accessible_scene("exit")


town_11_prison = Scene("town_11_prison", mesh_name="dungeon_a", body_name="bo_dungeon_a")
town_11_prison.add_flag(SceneFlag.IS_INDOORS)
town_11_prison.set_min_pos(-100.0, -100.0)
town_11_prison.add_accessible_scene("exit")


town_12_prison = Scene("town_12_prison", mesh_name="interior_prison_cell_a", body_name="bo_interior_prison_cell_a")
town_12_prison.add_flag(SceneFlag.IS_INDOORS)
town_12_prison.set_min_pos(-100.0, -100.0)
town_12_prison.add_accessible_scene("exit")


town_13_prison = Scene("town_13_prison", mesh_name="interior_prison_a", body_name="bo_interior_prison_a")
town_13_prison.add_flag(SceneFlag.IS_INDOORS)
town_13_prison.set_min_pos(-100.0, -100.0)
town_13_prison.add_accessible_scene("exit")


town_14_prison = Scene("town_14_prison", mesh_name="interior_prison_n", body_name="bo_interior_prison_n")
town_14_prison.add_flag(SceneFlag.IS_INDOORS)
town_14_prison.set_min_pos(-100.0, -100.0)
town_14_prison.add_accessible_scene("exit")


town_15_prison = Scene("town_15_prison", mesh_name="interior_prison_f", body_name="bo_interior_prison_f")
town_15_prison.add_flag(SceneFlag.IS_INDOORS)
town_15_prison.set_min_pos(-100.0, -100.0)
town_15_prison.add_accessible_scene("exit")


town_16_prison = Scene("town_16_prison", mesh_name="interior_prison_k", body_name="bo_interior_prison_k")
town_16_prison.add_flag(SceneFlag.IS_INDOORS)
town_16_prison.set_min_pos(-100.0, -100.0)
town_16_prison.add_accessible_scene("exit")


town_17_prison = Scene("town_17_prison", mesh_name="interior_prison_n", body_name="bo_interior_prison_n")
town_17_prison.add_flag(SceneFlag.IS_INDOORS)
town_17_prison.set_min_pos(-100.0, -100.0)
town_17_prison.add_accessible_scene("exit")


town_18_prison = Scene("town_18_prison", mesh_name="interior_prison_o", body_name="bo_interior_prison_o")
town_18_prison.add_flag(SceneFlag.IS_INDOORS)
town_18_prison.set_min_pos(-100.0, -100.0)
town_18_prison.add_accessible_scene("exit")


town_19_prison = Scene("town_19_prison", mesh_name="interior_prison_o", body_name="bo_interior_prison_o")
town_19_prison.add_flag(SceneFlag.IS_INDOORS)
town_19_prison.set_min_pos(-100.0, -100.0)
town_19_prison.add_accessible_scene("exit")


town_20_prison = Scene("town_20_prison", mesh_name="interior_prison_o", body_name="bo_interior_prison_o")
town_20_prison.add_flag(SceneFlag.IS_INDOORS)
town_20_prison.set_min_pos(-100.0, -100.0)
town_20_prison.add_accessible_scene("exit")


town_21_prison = Scene("town_21_prison", mesh_name="interior_prison_n", body_name="bo_interior_prison_n")
town_21_prison.add_flag(SceneFlag.IS_INDOORS)
town_21_prison.set_min_pos(-100.0, -100.0)
town_21_prison.add_accessible_scene("exit")


town_22_prison = Scene("town_22_prison", mesh_name="interior_prison_o", body_name="bo_interior_prison_o")
town_22_prison.add_flag(SceneFlag.IS_INDOORS)
town_22_prison.set_min_pos(-100.0, -100.0)
town_22_prison.add_accessible_scene("exit")


town_1_walls = Scene("town_1_walls", terrain_code="0x00000001300010c800054d5c00004af000005d3f00002ca0", extra_terrain="outer_terrain_plain")
town_1_walls.add_flag(SceneFlag.GENERATE)


town_2_walls = Scene("town_2_walls", terrain_code="0x00000001300010c800054d5c00004af000005d3f00002ca0", extra_terrain="outer_terrain_plain")
town_2_walls.add_flag(SceneFlag.GENERATE)


town_3_walls = Scene("town_3_walls", terrain_code="0x00000000300214100003ecfb00002b930000051900002c29", extra_terrain="outer_terrain_plain")
town_3_walls.add_flag(SceneFlag.GENERATE)


town_4_walls = Scene("town_4_walls", terrain_code="0x00000001300010c800054d5c00004af000005d3f00002ca0", extra_terrain="outer_terrain_plain")
town_4_walls.add_flag(SceneFlag.GENERATE)


town_5_walls = Scene("town_5_walls", terrain_code="0x0000000030024e108003fd0100007bd300006c31000061aa", extra_terrain="outer_terrain_plain")
town_5_walls.add_flag(SceneFlag.GENERATE)


town_6_walls = Scene("town_6_walls", terrain_code="0x00000002300015e300063d8800002757000055df00001b08", extra_terrain="sea_outer_terrain_1")
town_6_walls.add_flag(SceneFlag.GENERATE)


town_7_walls = Scene("town_7_walls", terrain_code="0x000000013002491600055157000000d20000152a0000611a", extra_terrain="outer_terrain_plain")
town_7_walls.add_flag(SceneFlag.GENERATE)


town_8_walls = Scene("town_8_walls", terrain_code="0x000000013002491600055157000000d20000152a0000611a", extra_terrain="outer_terrain_plain")
town_8_walls.add_flag(SceneFlag.GENERATE)


town_9_walls = Scene("town_9_walls", terrain_code="0x0000000140015033000651900000159f0000619800006af6", extra_terrain="outer_terrain_snow")
town_9_walls.add_flag(SceneFlag.GENERATE)


town_10_walls = Scene("town_10_walls", terrain_code="0x00000002200011af00065192000067110000688300003435", extra_terrain="outer_terrain_steppe")
town_10_walls.add_flag(SceneFlag.GENERATE)


town_11_walls = Scene("town_11_walls", terrain_code="0x0000000140015033000651900000159f0000619800006af6", extra_terrain="outer_terrain_snow")
town_11_walls.add_flag(SceneFlag.GENERATE)


town_12_walls = Scene("town_12_walls", terrain_code="0x00000001300010c800054d5c00004af000005d3f00002ca0", extra_terrain="outer_terrain_plain")
town_12_walls.add_flag(SceneFlag.GENERATE)


town_13_walls = Scene("town_13_walls", terrain_code="0x0000000130028e320005e17b00004a14000006d70000019d", extra_terrain="outer_terrain_plain")
town_13_walls.add_flag(SceneFlag.GENERATE)


town_14_walls = Scene("town_14_walls", terrain_code="0x00000002200011af00065192000067110000688300003435", extra_terrain="outer_terrain_steppe")
town_14_walls.add_flag(SceneFlag.GENERATE)


town_15_walls = Scene("town_15_walls", terrain_code="0x0000000030024e108003fd0100007bd300006c31000061aa", extra_terrain="outer_terrain_plain")
town_15_walls.add_flag(SceneFlag.GENERATE)


town_16_walls = Scene("town_16_walls", terrain_code="0x000000013001c98d0005b56d000072a70000240a00001e09", extra_terrain="outer_terrain_steppe")
town_16_walls.add_flag(SceneFlag.GENERATE)


town_17_walls = Scene("town_17_walls", terrain_code="0x00000002200011af00065192000067110000688300003435", extra_terrain="outer_terrain_steppe")
town_17_walls.add_flag(SceneFlag.GENERATE)


town_18_walls = Scene("town_18_walls", terrain_code="0x00000002200011af00065192000067110000688300003435", extra_terrain="outer_terrain_steppe")
town_18_walls.add_flag(SceneFlag.GENERATE)


town_19_walls = Scene("town_19_walls", terrain_code="0x00000002200011af00065192000067110000688300003435", extra_terrain="outer_terrain_desert")
town_19_walls.add_flag(SceneFlag.GENERATE)


town_20_walls = Scene("town_20_walls", terrain_code="0x00000a0650001e9a00a505418000581f000028c800000143", extra_terrain="outer_terrain_desert")
town_20_walls.add_flag(SceneFlag.GENERATE)


town_21_walls = Scene("town_21_walls", terrain_code="0x0000000150051a800004190400003f8c0000352b000014d8", extra_terrain="outer_terrain_desert")
town_21_walls.add_flag(SceneFlag.GENERATE)


town_22_walls = Scene("town_22_walls", terrain_code="0x000000025a00723200046d1b00003e020000147600004387", extra_terrain="outer_terrain_desert")
town_22_walls.add_flag(SceneFlag.GENERATE)


town_1_alley = Scene("town_1_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_plain")
town_1_alley.add_flag(SceneFlag.GENERATE)


town_2_alley = Scene("town_2_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_town_thir_1")
town_2_alley.add_flag(SceneFlag.GENERATE)


town_3_alley = Scene("town_3_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932")
town_3_alley.add_flag(SceneFlag.GENERATE)


town_4_alley = Scene("town_4_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_plain")
town_4_alley.add_flag(SceneFlag.GENERATE)


town_5_alley = Scene("town_5_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_plain")
town_5_alley.add_flag(SceneFlag.GENERATE)


town_6_alley = Scene("town_6_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_plain")
town_6_alley.add_flag(SceneFlag.GENERATE)


town_7_alley = Scene("town_7_alley", terrain_code="0x20008a110002589600006af30000356b00002c27", extra_terrain="outer_terrain_plain")
town_7_alley.add_flag(SceneFlag.GENERATE)


town_8_alley = Scene("town_8_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_plain")
town_8_alley.add_flag(SceneFlag.GENERATE)


town_9_alley = Scene("town_9_alley", terrain_code="0x400211130001e07800002ad400001172000035c4", extra_terrain="outer_terrain_snow")
town_9_alley.add_flag(SceneFlag.GENERATE)


town_10_alley = Scene("town_10_alley", terrain_code="0x0000000420000500000334ce00001d1100003d0600000d27", extra_terrain="outer_terrain_steppe")
town_10_alley.add_flag(SceneFlag.GENERATE)


town_11_alley = Scene("town_11_alley", terrain_code="0x400211130001e07800002ad400001172000035c4", extra_terrain="outer_terrain_snow")
town_11_alley.add_flag(SceneFlag.GENERATE)


town_12_alley = Scene("town_12_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_town_thir_1")
town_12_alley.add_flag(SceneFlag.GENERATE)


town_13_alley = Scene("town_13_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932")
town_13_alley.add_flag(SceneFlag.GENERATE)


town_14_alley = Scene("town_14_alley", terrain_code="0x0000000420000500000334ce00001d1100003d0600000d27", extra_terrain="outer_terrain_steppe")
town_14_alley.add_flag(SceneFlag.GENERATE)


town_15_alley = Scene("town_15_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_steppe")
town_15_alley.add_flag(SceneFlag.GENERATE)


town_16_alley = Scene("town_16_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_steppe")
town_16_alley.add_flag(SceneFlag.GENERATE)


town_17_alley = Scene("town_17_alley", terrain_code="0x0000000420000500000334ce00001d1100003d0600000d27", extra_terrain="outer_terrain_steppe")
town_17_alley.add_flag(SceneFlag.GENERATE)


town_18_alley = Scene("town_18_alley", terrain_code="0x0000000420000500000334ce00001d1100003d0600000d27", extra_terrain="outer_terrain_steppe")
town_18_alley.add_flag(SceneFlag.GENERATE)


town_19_alley = Scene("town_19_alley", terrain_code="0x0000000220002f000003fd0400006e120000359900004e13", extra_terrain="outer_terrain_desert")
town_19_alley.add_flag(SceneFlag.GENERATE)


town_20_alley = Scene("town_20_alley", terrain_code="0x00000a0650001e9a00a505418000581f000028c800000143", extra_terrain="outer_terrain_desert")
town_20_alley.add_flag(SceneFlag.GENERATE)


town_21_alley = Scene("town_21_alley", terrain_code="0x0000000150051a800004190400003f8c0000352b000014d8", extra_terrain="outer_terrain_desert")
town_21_alley.add_flag(SceneFlag.GENERATE)


town_22_alley = Scene("town_22_alley", terrain_code="0x000000025a00723200046d1b00003e0200001476000052ae", extra_terrain="outer_terrain_desert")
town_22_alley.add_flag(SceneFlag.GENERATE)


castle_1_exterior = Scene("castle_1_exterior", terrain_code="0x30054da28004050000005a76800022aa00002e3b", extra_terrain="outer_terrain_steppe")
castle_1_exterior.add_flag(SceneFlag.GENERATE)


castle_1_interior = Scene("castle_1_interior", mesh_name="dungeon_entry_a", body_name="bo_dungeon_entry_a")
castle_1_interior.add_flag(SceneFlag.IS_INDOORS)
castle_1_interior.set_min_pos(-100.0, -100.0)
castle_1_interior.add_accessible_scene("exit")
castle_1_interior.add_chest_troop(trp.castle_1_seneschal)


castle_1_prison = Scene("castle_1_prison", mesh_name="interior_prison_a", body_name="bo_interior_prison_a")
castle_1_prison.add_flag(SceneFlag.IS_INDOORS)
castle_1_prison.set_min_pos(-100.0, -100.0)


castle_2_exterior = Scene("castle_2_exterior", terrain_code="0xa00363638005c16d00003c82000037e000002303", extra_terrain="outer_terrain_plain")
castle_2_exterior.add_flag(SceneFlag.GENERATE)


castle_2_interior = Scene("castle_2_interior", mesh_name="interior_castle_u", body_name="bo_interior_castle_u")
castle_2_interior.add_flag(SceneFlag.IS_INDOORS)
castle_2_interior.set_min_pos(-100.0, -100.0)
castle_2_interior.add_accessible_scene("exit")
castle_2_interior.add_chest_troop(trp.castle_2_seneschal)


castle_2_prison = Scene("castle_2_prison", mesh_name="interior_prison_d", body_name="bo_interior_prison_d")
castle_2_prison.add_flag(SceneFlag.IS_INDOORS)
castle_2_prison.set_min_pos(-100.0, -100.0)


castle_3_exterior = Scene("castle_3_exterior", terrain_code="0x0000000030044e900003dd02000077b20000400100005697", extra_terrain="outer_terrain_plain")
castle_3_exterior.add_flag(SceneFlag.GENERATE)


castle_3_interior = Scene("castle_3_interior", mesh_name="interior_castle_m", body_name="bo_interior_castle_m")
castle_3_interior.add_flag(SceneFlag.IS_INDOORS)
castle_3_interior.set_min_pos(-100.0, -100.0)
castle_3_interior.add_accessible_scene("exit")
castle_3_interior.add_chest_troop(trp.castle_3_seneschal)


castle_3_prison = Scene("castle_3_prison", mesh_name="interior_prison_e", body_name="bo_interior_prison_e")
castle_3_prison.add_flag(SceneFlag.IS_INDOORS)
castle_3_prison.set_min_pos(-100.0, -100.0)


castle_4_exterior = Scene("castle_4_exterior", terrain_code="0x0000000030044e900003dd02000077b20000400100005697", extra_terrain="outer_terrain_plain")
castle_4_exterior.add_flag(SceneFlag.GENERATE)


castle_4_interior = Scene("castle_4_interior", mesh_name="interior_castle_k", body_name="bo_interior_castle_k")
castle_4_interior.add_flag(SceneFlag.IS_INDOORS)
castle_4_interior.set_min_pos(-100.0, -100.0)
castle_4_interior.add_accessible_scene("exit")
castle_4_interior.add_chest_troop(trp.castle_4_seneschal)


castle_4_prison = Scene("castle_4_prison", mesh_name="interior_prison_l", body_name="bo_interior_prison_l")
castle_4_prison.add_flag(SceneFlag.IS_INDOORS)
castle_4_prison.set_min_pos(-100.0, -100.0)


castle_5_exterior = Scene("castle_5_exterior", terrain_code="0x3189dc1a000429090000619700007cbd00005ab7", extra_terrain="outer_terrain_plain")
castle_5_exterior.add_flag(SceneFlag.GENERATE)


castle_5_interior = Scene("castle_5_interior", mesh_name="interior_castle_j", body_name="bo_interior_castle_j")
castle_5_interior.add_flag(SceneFlag.IS_INDOORS)
castle_5_interior.set_min_pos(-100.0, -100.0)
castle_5_interior.add_accessible_scene("exit")
castle_5_interior.add_chest_troop(trp.castle_5_seneschal)


castle_5_prison = Scene("castle_5_prison", mesh_name="interior_prison_l", body_name="bo_interior_prison_l")
castle_5_prison.add_flag(SceneFlag.IS_INDOORS)
castle_5_prison.set_min_pos(-100.0, -100.0)


castle_6_exterior = Scene("castle_6_exterior", terrain_code="0x00000000b009723200059d6800005f4f0000757f000069cd", extra_terrain="outer_terrain_plain")
castle_6_exterior.add_flag(SceneFlag.GENERATE)


castle_6_interior = Scene("castle_6_interior", mesh_name="interior_castle_p", body_name="bo_interior_castle_p")
castle_6_interior.add_flag(SceneFlag.IS_INDOORS)
castle_6_interior.set_min_pos(-100.0, -100.0)
castle_6_interior.add_accessible_scene("exit")
castle_6_interior.add_chest_troop(trp.castle_6_seneschal)


castle_6_prison = Scene("castle_6_prison", mesh_name="interior_prison_j", body_name="bo_interior_prison_j")
castle_6_prison.add_flag(SceneFlag.IS_INDOORS)
castle_6_prison.set_min_pos(-100.0, -100.0)


castle_7_exterior = Scene("castle_7_exterior", terrain_code="0x00000000c007a56300047d1e00006c9100002859000028bc", extra_terrain="outer_terrain_snow")
castle_7_exterior.add_flag(SceneFlag.GENERATE)


castle_7_interior = Scene("castle_7_interior", mesh_name="interior_castle_o", body_name="bo_interior_castle_o")
castle_7_interior.add_flag(SceneFlag.IS_INDOORS)
castle_7_interior.set_min_pos(-100.0, -100.0)
castle_7_interior.add_accessible_scene("exit")
castle_7_interior.add_chest_troop(trp.castle_7_seneschal)


castle_7_prison = Scene("castle_7_prison", mesh_name="interior_prison_i", body_name="bo_interior_prison_i")
castle_7_prison.add_flag(SceneFlag.IS_INDOORS)
castle_7_prison.set_min_pos(-100.0, -100.0)


castle_8_exterior = Scene("castle_8_exterior", terrain_code="0x314d060900036cd70000295300002ec9000025f3", extra_terrain="outer_terrain_plain")
castle_8_exterior.add_flag(SceneFlag.GENERATE)


castle_8_interior = Scene("castle_8_interior", mesh_name="interior_castle_t", body_name="bo_interior_castle_t")
castle_8_interior.add_flag(SceneFlag.IS_INDOORS)
castle_8_interior.set_min_pos(-100.0, -100.0)
castle_8_interior.add_accessible_scene("exit")
castle_8_interior.add_chest_troop(trp.castle_8_seneschal)


castle_8_prison = Scene("castle_8_prison", mesh_name="interior_prison_e", body_name="bo_interior_prison_e")
castle_8_prison.add_flag(SceneFlag.IS_INDOORS)
castle_8_prison.set_min_pos(-100.0, -100.0)


castle_9_exterior = Scene("castle_9_exterior", terrain_code="0xa0048e000004d93700004f91000065980000229b", extra_terrain="outer_terrain_steppe")
castle_9_exterior.add_flag(SceneFlag.GENERATE)


castle_9_interior = Scene("castle_9_interior", mesh_name="interior_castle_l", body_name="bo_interior_castle_l")
castle_9_interior.add_flag(SceneFlag.IS_INDOORS)
castle_9_interior.set_min_pos(-100.0, -100.0)
castle_9_interior.add_accessible_scene("exit")
castle_9_interior.add_chest_troop(trp.castle_9_seneschal)


castle_9_prison = Scene("castle_9_prison", mesh_name="interior_prison_d", body_name="bo_interior_prison_d")
castle_9_prison.add_flag(SceneFlag.IS_INDOORS)
castle_9_prison.set_min_pos(-100.0, -100.0)


castle_10_exterior = Scene("castle_10_exterior", terrain_code="0x000000023007b23200049d2a00003c37000040ef000037cd", extra_terrain="outer_terrain_castle_9")
castle_10_exterior.add_flag(SceneFlag.GENERATE)


castle_10_interior = Scene("castle_10_interior", mesh_name="interior_castle_j", body_name="bo_interior_castle_j")
castle_10_interior.add_flag(SceneFlag.IS_INDOORS)
castle_10_interior.set_min_pos(-100.0, -100.0)
castle_10_interior.add_accessible_scene("exit")
castle_10_interior.add_chest_troop(trp.castle_10_seneschal)


castle_10_prison = Scene("castle_10_prison", mesh_name="interior_prison_l", body_name="bo_interior_prison_l")
castle_10_prison.add_flag(SceneFlag.IS_INDOORS)
castle_10_prison.set_min_pos(-100.0, -100.0)


castle_11_exterior = Scene("castle_11_exterior", terrain_code="0x0000000030044e900003dd02000077b20000400100005697", extra_terrain="outer_terrain_plain")
castle_11_exterior.add_flag(SceneFlag.GENERATE)


castle_11_interior = Scene("castle_11_interior", mesh_name="interior_castle_a", body_name="bo_interior_castle_a")
castle_11_interior.add_flag(SceneFlag.IS_INDOORS)
castle_11_interior.set_min_pos(-100.0, -100.0)
castle_11_interior.add_accessible_scene("exit")
castle_11_interior.add_chest_troop(trp.castle_11_seneschal)


castle_11_prison = Scene("castle_11_prison", mesh_name="interior_prison_k", body_name="bo_interior_prison_k")
castle_11_prison.add_flag(SceneFlag.IS_INDOORS)
castle_11_prison.set_min_pos(-100.0, -100.0)


castle_12_exterior = Scene("castle_12_exterior", terrain_code="0x0000000230054f630005fd820000222a00003de000005f00", extra_terrain="outer_terrain_town_thir_1")
castle_12_exterior.add_flag(SceneFlag.GENERATE)


castle_12_interior = Scene("castle_12_interior", mesh_name="interior_castle_y", body_name="bo_interior_castle_y")
castle_12_interior.add_flag(SceneFlag.IS_INDOORS)
castle_12_interior.set_min_pos(-100.0, -100.0)
castle_12_interior.add_accessible_scene("exit")
castle_12_interior.add_chest_troop(trp.castle_12_seneschal)


castle_12_prison = Scene("castle_12_prison", mesh_name="interior_prison_i", body_name="bo_interior_prison_i")
castle_12_prison.add_flag(SceneFlag.IS_INDOORS)
castle_12_prison.set_min_pos(-100.0, -100.0)


castle_13_exterior = Scene("castle_13_exterior", terrain_code="0x0000000230054f630005fd820000222a00003de000005f00", extra_terrain="outer_terrain_plain")
castle_13_exterior.add_flag(SceneFlag.GENERATE)


castle_13_interior = Scene("castle_13_interior", mesh_name="interior_castle_v", body_name="bo_interior_castle_v")
castle_13_interior.add_flag(SceneFlag.IS_INDOORS)
castle_13_interior.set_min_pos(-100.0, -100.0)
castle_13_interior.add_accessible_scene("exit")
castle_13_interior.add_chest_troop(trp.castle_13_seneschal)


castle_13_prison = Scene("castle_13_prison", mesh_name="interior_prison_j", body_name="bo_interior_prison_j")
castle_13_prison.add_flag(SceneFlag.IS_INDOORS)
castle_13_prison.set_min_pos(-100.0, -100.0)


castle_14_exterior = Scene("castle_14_exterior", terrain_code="0x000000023007a3b20005795e0000706d0000381800000bbc", extra_terrain="outer_terrain_plain")
castle_14_exterior.add_flag(SceneFlag.GENERATE)


castle_14_interior = Scene("castle_14_interior", mesh_name="interior_castle_j", body_name="bo_interior_castle_j")
castle_14_interior.add_flag(SceneFlag.IS_INDOORS)
castle_14_interior.set_min_pos(-100.0, -100.0)
castle_14_interior.add_accessible_scene("exit")
castle_14_interior.add_chest_troop(trp.castle_14_seneschal)


castle_14_prison = Scene("castle_14_prison", mesh_name="interior_prison_m", body_name="bo_interior_prison_m")
castle_14_prison.add_flag(SceneFlag.IS_INDOORS)
castle_14_prison.set_min_pos(-100.0, -100.0)


castle_15_exterior = Scene("castle_15_exterior", terrain_code="0x000000023007941f0005415000007e650000225f00003b3e", extra_terrain="outer_terrain_plain")
castle_15_exterior.add_flag(SceneFlag.GENERATE)


castle_15_interior = Scene("castle_15_interior", mesh_name="interior_castle_p", body_name="bo_interior_castle_p")
castle_15_interior.add_flag(SceneFlag.IS_INDOORS)
castle_15_interior.set_min_pos(-100.0, -100.0)
castle_15_interior.add_accessible_scene("exit")
castle_15_interior.add_chest_troop(trp.castle_15_seneschal)


castle_15_prison = Scene("castle_15_prison", mesh_name="interior_prison_a", body_name="bo_interior_prison_a")
castle_15_prison.add_flag(SceneFlag.IS_INDOORS)
castle_15_prison.set_min_pos(-100.0, -100.0)


castle_16_exterior = Scene("castle_16_exterior", terrain_code="0x000000023007a3b20005795e0000706d0000381800000bbc", extra_terrain="outer_terrain_plain")
castle_16_exterior.add_flag(SceneFlag.GENERATE)


castle_16_interior = Scene("castle_16_interior", mesh_name="interior_castle_k", body_name="bo_interior_castle_k")
castle_16_interior.add_flag(SceneFlag.IS_INDOORS)
castle_16_interior.set_min_pos(-100.0, -100.0)
castle_16_interior.add_accessible_scene("exit")
castle_16_interior.add_chest_troop(trp.castle_16_seneschal)


castle_16_prison = Scene("castle_16_prison", mesh_name="interior_prison_l", body_name="bo_interior_prison_l")
castle_16_prison.add_flag(SceneFlag.IS_INDOORS)
castle_16_prison.set_min_pos(-100.0, -100.0)


castle_17_exterior = Scene("castle_17_exterior", terrain_code="0x0000000220045d9b0005d9760000034a00002a3e00006fbd", extra_terrain="outer_terrain_steppe")
castle_17_exterior.add_flag(SceneFlag.GENERATE)


castle_17_interior = Scene("castle_17_interior", mesh_name="interior_castle_l", body_name="bo_interior_castle_l")
castle_17_interior.add_flag(SceneFlag.IS_INDOORS)
castle_17_interior.set_min_pos(-100.0, -100.0)
castle_17_interior.add_accessible_scene("exit")
castle_17_interior.add_chest_troop(trp.castle_17_seneschal)


castle_17_prison = Scene("castle_17_prison", mesh_name="interior_prison_a", body_name="bo_interior_prison_a")
castle_17_prison.add_flag(SceneFlag.IS_INDOORS)
castle_17_prison.set_min_pos(-100.0, -100.0)


castle_18_exterior = Scene("castle_18_exterior", terrain_code="0x0000000240079f9e0005695a0000035f00003ef400004aa8", extra_terrain="outer_terrain_snow")
castle_18_exterior.add_flag(SceneFlag.GENERATE)


castle_18_interior = Scene("castle_18_interior", mesh_name="interior_castle_n", body_name="bo_interior_castle_n")
castle_18_interior.add_flag(SceneFlag.IS_INDOORS)
castle_18_interior.set_min_pos(-100.0, -100.0)
castle_18_interior.add_accessible_scene("exit")
castle_18_interior.add_chest_troop(trp.castle_18_seneschal)


castle_18_prison = Scene("castle_18_prison", mesh_name="interior_prison_k", body_name="bo_interior_prison_k")
castle_18_prison.add_flag(SceneFlag.IS_INDOORS)
castle_18_prison.set_min_pos(-100.0, -100.0)


castle_19_exterior = Scene("castle_19_exterior", terrain_code="0x000000014004d81100057963000062ce0000255800004c09", extra_terrain="outer_terrain_snow")
castle_19_exterior.add_flag(SceneFlag.GENERATE)


castle_19_interior = Scene("castle_19_interior", mesh_name="interior_castle_c", body_name="bo_interior_castle_c")
castle_19_interior.add_flag(SceneFlag.IS_INDOORS)
castle_19_interior.set_min_pos(-100.0, -100.0)
castle_19_interior.add_accessible_scene("exit")
castle_19_interior.add_chest_troop(trp.castle_19_seneschal)


castle_19_prison = Scene("castle_19_prison", mesh_name="interior_prison_e", body_name="bo_interior_prison_e")
castle_19_prison.add_flag(SceneFlag.IS_INDOORS)
castle_19_prison.set_min_pos(-100.0, -100.0)


castle_20_exterior = Scene("castle_20_exterior", terrain_code="0x000000013006199a0004e5370000494f000028fc00006cf6", extra_terrain="outer_terrain_plain")
castle_20_exterior.add_flag(SceneFlag.GENERATE)


castle_20_interior = Scene("castle_20_interior", mesh_name="interior_castle_a", body_name="bo_interior_castle_a")
castle_20_interior.add_flag(SceneFlag.IS_INDOORS)
castle_20_interior.set_min_pos(-100.0, -100.0)
castle_20_interior.add_accessible_scene("exit")
castle_20_interior.add_chest_troop(trp.castle_20_seneschal)


castle_20_prison = Scene("castle_20_prison", mesh_name="interior_prison_d", body_name="bo_interior_prison_d")
castle_20_prison.add_flag(SceneFlag.IS_INDOORS)
castle_20_prison.set_min_pos(-100.0, -100.0)


castle_21_exterior = Scene("castle_21_exterior", terrain_code="0x0000000230011ab20005d57800003a2600004b7a000071ef", extra_terrain="outer_terrain_plain")
castle_21_exterior.add_flag(SceneFlag.GENERATE)


castle_21_interior = Scene("castle_21_interior", mesh_name="interior_castle_c", body_name="bo_interior_castle_c")
castle_21_interior.add_flag(SceneFlag.IS_INDOORS)
castle_21_interior.set_min_pos(-100.0, -100.0)
castle_21_interior.add_accessible_scene("exit")
castle_21_interior.add_chest_troop(trp.castle_21_seneschal)


castle_21_prison = Scene("castle_21_prison", mesh_name="interior_prison_d", body_name="bo_interior_prison_d")
castle_21_prison.add_flag(SceneFlag.IS_INDOORS)
castle_21_prison.set_min_pos(-100.0, -100.0)


castle_22_exterior = Scene("castle_22_exterior", terrain_code="0x000000003000ad340004d537000024650000253c00000461", extra_terrain="outer_terrain_plain")
castle_22_exterior.add_flag(SceneFlag.GENERATE)


castle_22_interior = Scene("castle_22_interior", mesh_name="interior_castle_a", body_name="bo_interior_castle_a")
castle_22_interior.add_flag(SceneFlag.IS_INDOORS)
castle_22_interior.set_min_pos(-100.0, -100.0)
castle_22_interior.add_accessible_scene("exit")
castle_22_interior.add_chest_troop(trp.castle_22_seneschal)


castle_22_prison = Scene("castle_22_prison", mesh_name="interior_prison_i", body_name="bo_interior_prison_i")
castle_22_prison.add_flag(SceneFlag.IS_INDOORS)
castle_22_prison.set_min_pos(-100.0, -100.0)


castle_23_exterior = Scene("castle_23_exterior", terrain_code="0x00000002300658bc0007bded000025520000093800006114", extra_terrain="outer_terrain_plain")
castle_23_exterior.add_flag(SceneFlag.GENERATE)


castle_23_interior = Scene("castle_23_interior", mesh_name="interior_castle_y", body_name="bo_interior_castle_y")
castle_23_interior.add_flag(SceneFlag.IS_INDOORS)
castle_23_interior.set_min_pos(-100.0, -100.0)
castle_23_interior.add_accessible_scene("exit")
castle_23_interior.add_chest_troop(trp.castle_23_seneschal)


castle_23_prison = Scene("castle_23_prison", mesh_name="interior_prison_b", body_name="bo_interior_prison_b")
castle_23_prison.add_flag(SceneFlag.IS_INDOORS)
castle_23_prison.set_min_pos(-100.0, -100.0)


castle_24_exterior = Scene("castle_24_exterior", terrain_code="0x0000000130021f63000721ca000055be000079d90000156d", extra_terrain="outer_terrain_plain")
castle_24_exterior.add_flag(SceneFlag.GENERATE)


castle_24_interior = Scene("castle_24_interior", mesh_name="castle_h_interior_b", body_name="bo_castle_h_interior_b")
castle_24_interior.add_flag(SceneFlag.IS_INDOORS)
castle_24_interior.set_min_pos(-100.0, -100.0)
castle_24_interior.add_accessible_scene("exit")
castle_24_interior.add_chest_troop(trp.castle_24_seneschal)


castle_24_prison = Scene("castle_24_prison", mesh_name="interior_prison_f", body_name="bo_interior_prison_f")
castle_24_prison.add_flag(SceneFlag.IS_INDOORS)
castle_24_prison.set_min_pos(-100.0, -100.0)


castle_25_exterior = Scene("castle_25_exterior", terrain_code="0x000000013004e0a600061989000053d50000749800005f64", extra_terrain="outer_terrain_plain")
castle_25_exterior.add_flag(SceneFlag.GENERATE)


castle_25_interior = Scene("castle_25_interior", mesh_name="castle_h_interior_b", body_name="bo_castle_h_interior_b")
castle_25_interior.add_flag(SceneFlag.IS_INDOORS)
castle_25_interior.set_min_pos(-100.0, -100.0)
castle_25_interior.add_accessible_scene("exit")
castle_25_interior.add_chest_troop(trp.castle_25_seneschal)


castle_25_prison = Scene("castle_25_prison", mesh_name="interior_prison_a", body_name="bo_interior_prison_a")
castle_25_prison.add_flag(SceneFlag.IS_INDOORS)
castle_25_prison.set_min_pos(-100.0, -100.0)


castle_26_exterior = Scene("castle_26_exterior", terrain_code="0x000000013005213200077dda0000733300002edf000052ba", extra_terrain="outer_terrain_plain")
castle_26_exterior.add_flag(SceneFlag.GENERATE)


castle_26_interior = Scene("castle_26_interior", mesh_name="castle_h_interior_a", body_name="bo_castle_h_interior_a")
castle_26_interior.add_flag(SceneFlag.IS_INDOORS)
castle_26_interior.set_min_pos(-100.0, -100.0)
castle_26_interior.add_accessible_scene("exit")
castle_26_interior.add_chest_troop(trp.castle_26_seneschal)


castle_26_prison = Scene("castle_26_prison", mesh_name="interior_prison_h", body_name="bo_interior_prison_h")
castle_26_prison.add_flag(SceneFlag.IS_INDOORS)
castle_26_prison.set_min_pos(-100.0, -100.0)


castle_27_exterior = Scene("castle_27_exterior", terrain_code="0x000000013007b23200070dbc000041de00000c4900003cfc", extra_terrain="outer_terrain_plain")
castle_27_exterior.add_flag(SceneFlag.GENERATE)


castle_27_interior = Scene("castle_27_interior", mesh_name="castle_h_interior_a", body_name="bo_castle_h_interior_a")
castle_27_interior.add_flag(SceneFlag.IS_INDOORS)
castle_27_interior.set_min_pos(-100.0, -100.0)
castle_27_interior.add_accessible_scene("exit")
castle_27_interior.add_chest_troop(trp.castle_27_seneschal)


castle_27_prison = Scene("castle_27_prison", mesh_name="interior_prison_i", body_name="bo_interior_prison_i")
castle_27_prison.add_flag(SceneFlag.IS_INDOORS)
castle_27_prison.set_min_pos(-100.0, -100.0)


castle_28_exterior = Scene("castle_28_exterior", terrain_code="0x000000013007b232000715c50000084c00001b5b000018ec", extra_terrain="outer_terrain_plain")
castle_28_exterior.add_flag(SceneFlag.GENERATE)


castle_28_interior = Scene("castle_28_interior", mesh_name="castle_h_interior_a", body_name="bo_castle_h_interior_a")
castle_28_interior.add_flag(SceneFlag.IS_INDOORS)
castle_28_interior.set_min_pos(-100.0, -100.0)
castle_28_interior.add_accessible_scene("exit")
castle_28_interior.add_chest_troop(trp.castle_28_seneschal)


castle_28_prison = Scene("castle_28_prison", mesh_name="interior_prison_j", body_name="bo_interior_prison_j")
castle_28_prison.add_flag(SceneFlag.IS_INDOORS)
castle_28_prison.set_min_pos(-100.0, -100.0)


castle_29_exterior = Scene("castle_29_exterior", terrain_code="0x00000006400796b20005053e000042ed0000199b000037cd", extra_terrain="outer_terrain_snow")
castle_29_exterior.add_flag(SceneFlag.GENERATE)


castle_29_interior = Scene("castle_29_interior", mesh_name="interior_castle_n", body_name="bo_interior_castle_n")
castle_29_interior.add_flag(SceneFlag.IS_INDOORS)
castle_29_interior.set_min_pos(-100.0, -100.0)
castle_29_interior.add_accessible_scene("exit")
castle_29_interior.add_chest_troop(trp.castle_29_seneschal)


castle_29_prison = Scene("castle_29_prison", mesh_name="interior_prison_a", body_name="bo_interior_prison_a")
castle_29_prison.add_flag(SceneFlag.IS_INDOORS)
castle_29_prison.set_min_pos(-100.0, -100.0)


castle_30_exterior = Scene("castle_30_exterior", terrain_code="0x0000000220035e32000611840000147f00003dac00000660", extra_terrain="outer_terrain_plain")
castle_30_exterior.add_flag(SceneFlag.GENERATE)


castle_30_interior = Scene("castle_30_interior", mesh_name="interior_castle_g_square_keep", body_name="bo_interior_castle_g_square_keep")
castle_30_interior.add_flag(SceneFlag.IS_INDOORS)
castle_30_interior.set_min_pos(-100.0, -100.0)
castle_30_interior.add_accessible_scene("exit")
castle_30_interior.add_chest_troop(trp.castle_30_seneschal)


castle_30_prison = Scene("castle_30_prison", mesh_name="interior_prison_n", body_name="bo_interior_prison_n")
castle_30_prison.add_flag(SceneFlag.IS_INDOORS)
castle_30_prison.set_min_pos(-100.0, -100.0)


castle_31_exterior = Scene("castle_31_exterior", terrain_code="0x0000000230025b8d0006459400006a3700002adb00007091", extra_terrain="outer_terrain_plain")
castle_31_exterior.add_flag(SceneFlag.GENERATE)


castle_31_interior = Scene("castle_31_interior", mesh_name="interior_castle_y", body_name="bo_interior_castle_y")
castle_31_interior.add_flag(SceneFlag.IS_INDOORS)
castle_31_interior.set_min_pos(-100.0, -100.0)
castle_31_interior.add_accessible_scene("exit")
castle_31_interior.add_chest_troop(trp.castle_31_seneschal)


castle_31_prison = Scene("castle_31_prison", mesh_name="interior_prison_i", body_name="bo_interior_prison_i")
castle_31_prison.add_flag(SceneFlag.IS_INDOORS)
castle_31_prison.set_min_pos(-100.0, -100.0)


castle_32_exterior = Scene("castle_32_exterior", terrain_code="0x0000000230041fb20005fd7d00002692000029b700007d12", extra_terrain="outer_terrain_plain")
castle_32_exterior.add_flag(SceneFlag.GENERATE)


castle_32_interior = Scene("castle_32_interior", mesh_name="castle_h_interior_a", body_name="bo_castle_h_interior_a")
castle_32_interior.add_flag(SceneFlag.IS_INDOORS)
castle_32_interior.set_min_pos(-100.0, -100.0)
castle_32_interior.add_accessible_scene("exit")
castle_32_interior.add_chest_troop(trp.castle_32_seneschal)


castle_32_prison = Scene("castle_32_prison", mesh_name="interior_prison_j", body_name="bo_interior_prison_j")
castle_32_prison.add_flag(SceneFlag.IS_INDOORS)
castle_32_prison.set_min_pos(-100.0, -100.0)


castle_33_exterior = Scene("castle_33_exterior", terrain_code="0x0000000230029cb2000709c200003c9500004b9b00002f4d", extra_terrain="outer_terrain_plain")
castle_33_exterior.add_flag(SceneFlag.GENERATE)


castle_33_interior = Scene("castle_33_interior", mesh_name="interior_castle_v", body_name="bo_interior_castle_v")
castle_33_interior.add_flag(SceneFlag.IS_INDOORS)
castle_33_interior.set_min_pos(-100.0, -100.0)
castle_33_interior.add_accessible_scene("exit")
castle_33_interior.add_chest_troop(trp.castle_33_seneschal)


castle_33_prison = Scene("castle_33_prison", mesh_name="interior_prison_d", body_name="bo_interior_prison_d")
castle_33_prison.add_flag(SceneFlag.IS_INDOORS)
castle_33_prison.set_min_pos(-100.0, -100.0)


castle_34_exterior = Scene("castle_34_exterior", terrain_code="0x00000002b007b232000715c50000084c00001b5b00006580", extra_terrain="outer_terrain_plain")
castle_34_exterior.add_flag(SceneFlag.GENERATE)


castle_34_interior = Scene("castle_34_interior", mesh_name="interior_castle_c", body_name="bo_interior_castle_c")
castle_34_interior.add_flag(SceneFlag.IS_INDOORS)
castle_34_interior.set_min_pos(-100.0, -100.0)
castle_34_interior.add_accessible_scene("exit")
castle_34_interior.add_chest_troop(trp.castle_34_seneschal)


castle_34_prison = Scene("castle_34_prison", mesh_name="interior_prison_f", body_name="bo_interior_prison_f")
castle_34_prison.add_flag(SceneFlag.IS_INDOORS)
castle_34_prison.set_min_pos(-100.0, -100.0)


castle_35_exterior = Scene("castle_35_exterior", terrain_code="0x0000000130031be30006f9bc00000aae00000fb80000243f", extra_terrain="outer_terrain_plain")
castle_35_exterior.add_flag(SceneFlag.GENERATE)


castle_35_interior = Scene("castle_35_interior", mesh_name="castle_h_interior_a", body_name="bo_castle_h_interior_a")
castle_35_interior.add_flag(SceneFlag.IS_INDOORS)
castle_35_interior.set_min_pos(-100.0, -100.0)
castle_35_interior.add_accessible_scene("exit")
castle_35_interior.add_chest_troop(trp.castle_35_seneschal)


castle_35_prison = Scene("castle_35_prison", mesh_name="interior_prison_f", body_name="bo_interior_prison_f")
castle_35_prison.add_flag(SceneFlag.IS_INDOORS)
castle_35_prison.set_min_pos(-100.0, -100.0)


castle_36_exterior = Scene("castle_36_exterior", terrain_code="0x000000013007b2630005695c00001ebe0000028e00007e37", extra_terrain="outer_terrain_plain")
castle_36_exterior.add_flag(SceneFlag.GENERATE)


castle_36_interior = Scene("castle_36_interior", mesh_name="castle_h_interior_b", body_name="bo_castle_h_interior_b")
castle_36_interior.add_flag(SceneFlag.IS_INDOORS)
castle_36_interior.set_min_pos(-100.0, -100.0)
castle_36_interior.add_accessible_scene("exit")
castle_36_interior.add_chest_troop(trp.castle_36_seneschal)


castle_36_prison = Scene("castle_36_prison", mesh_name="interior_prison_h", body_name="bo_interior_prison_h")
castle_36_prison.add_flag(SceneFlag.IS_INDOORS)
castle_36_prison.set_min_pos(-100.0, -100.0)


castle_37_exterior = Scene("castle_37_exterior", terrain_code="0x0000000130025cb20006097f00005b1400000e2f00005fd9", extra_terrain="outer_terrain_plain")
castle_37_exterior.add_flag(SceneFlag.GENERATE)


castle_37_interior = Scene("castle_37_interior", mesh_name="interior_castle_k", body_name="bo_interior_castle_k")
castle_37_interior.add_flag(SceneFlag.IS_INDOORS)
castle_37_interior.set_min_pos(-100.0, -100.0)
castle_37_interior.add_accessible_scene("exit")
castle_37_interior.add_chest_troop(trp.castle_37_seneschal)


castle_37_prison = Scene("castle_37_prison", mesh_name="interior_prison_l", body_name="bo_interior_prison_l")
castle_37_prison.add_flag(SceneFlag.IS_INDOORS)
castle_37_prison.set_min_pos(-100.0, -100.0)


castle_38_exterior = Scene("castle_38_exterior", terrain_code="0x000000012007985300055550000064d500005c060000759e", extra_terrain="outer_terrain_steppe")
castle_38_exterior.add_flag(SceneFlag.GENERATE)


castle_38_interior = Scene("castle_38_interior", terrain_code="0x00000007300005000002308c00004a840000624700004fda")
castle_38_interior.add_flag(SceneFlag.GENERATE)
castle_38_interior.set_min_pos(-100.0, -100.0)
castle_38_interior.add_accessible_scene("exit")
castle_38_interior.add_chest_troop(trp.castle_38_seneschal)


castle_38_prison = Scene("castle_38_prison", mesh_name="interior_prison_o", body_name="bo_interior_prison_o")
castle_38_prison.add_flag(SceneFlag.IS_INDOORS)
castle_38_prison.set_min_pos(-100.0, -100.0)


castle_39_exterior = Scene("castle_39_exterior", terrain_code="0x000000014007a0320005695f0000601c00007a8800001a17", extra_terrain="outer_terrain_snow")
castle_39_exterior.add_flag(SceneFlag.GENERATE)


castle_39_interior = Scene("castle_39_interior", mesh_name="interior_castle_n", body_name="bo_interior_castle_n")
castle_39_interior.add_flag(SceneFlag.IS_INDOORS)
castle_39_interior.set_min_pos(-100.0, -100.0)
castle_39_interior.add_accessible_scene("exit")
castle_39_interior.add_chest_troop(trp.castle_39_seneschal)


castle_39_prison = Scene("castle_39_prison", mesh_name="interior_prison_k", body_name="bo_interior_prison_k")
castle_39_prison.add_flag(SceneFlag.IS_INDOORS)
castle_39_prison.set_min_pos(-100.0, -100.0)


castle_40_exterior = Scene("castle_40_exterior", terrain_code="0x000000012007985300055550000064d500005c060000759e", extra_terrain="outer_terrain_steppe")
castle_40_exterior.add_flag(SceneFlag.GENERATE)


castle_40_interior = Scene("castle_40_interior", mesh_name="interior_castle_g_square_keep", body_name="bo_interior_castle_g_square_keep")
castle_40_interior.add_flag(SceneFlag.IS_INDOORS)
castle_40_interior.set_min_pos(-100.0, -100.0)
castle_40_interior.add_accessible_scene("exit")
castle_40_interior.add_chest_troop(trp.castle_40_seneschal)


castle_40_prison = Scene("castle_40_prison", mesh_name="interior_prison_n", body_name="bo_interior_prison_n")
castle_40_prison.add_flag(SceneFlag.IS_INDOORS)
castle_40_prison.set_min_pos(-100.0, -100.0)


castle_41_exterior = Scene("castle_41_exterior", terrain_code="0x000000005a0932320004cd3000004e7d00007d6e00006c58", extra_terrain="outer_terrain_desert")
castle_41_exterior.add_flag(SceneFlag.GENERATE)


castle_41_interior = Scene("castle_41_interior", mesh_name="interior_castle_y", body_name="bo_interior_castle_y")
castle_41_interior.add_flag(SceneFlag.IS_INDOORS)
castle_41_interior.set_min_pos(-100.0, -100.0)
castle_41_interior.add_accessible_scene("exit")
castle_41_interior.add_chest_troop(trp.castle_31_seneschal)


castle_41_prison = Scene("castle_41_prison", mesh_name="interior_prison_i", body_name="bo_interior_prison_i")
castle_41_prison.add_flag(SceneFlag.IS_INDOORS)
castle_41_prison.set_min_pos(-100.0, -100.0)


castle_42_exterior = Scene("castle_42_exterior", terrain_code="0x000000005a039fb20005114400004f690000467a00004400", extra_terrain="outer_terrain_desert")
castle_42_exterior.add_flag(SceneFlag.GENERATE)


castle_42_interior = Scene("castle_42_interior", mesh_name="arabian_interior_keep_b", body_name="bo_arabian_interior_keep_b")
castle_42_interior.add_flag(SceneFlag.IS_INDOORS)
castle_42_interior.set_min_pos(-100.0, -100.0)
castle_42_interior.add_accessible_scene("exit")
castle_42_interior.add_chest_troop(trp.castle_32_seneschal)


castle_42_prison = Scene("castle_42_prison", mesh_name="interior_prison_o", body_name="bo_interior_prison_o")
castle_42_prison.add_flag(SceneFlag.IS_INDOORS)
castle_42_prison.set_min_pos(-100.0, -100.0)


castle_43_exterior = Scene("castle_43_exterior", terrain_code="0x000000005a0ae6480004952400003e1800005d9f00002c7e", extra_terrain="outer_terrain_desert")
castle_43_exterior.add_flag(SceneFlag.GENERATE)


castle_43_interior = Scene("castle_43_interior", mesh_name="arabian_interior_keep_b", body_name="bo_arabian_interior_keep_b")
castle_43_interior.add_flag(SceneFlag.IS_INDOORS)
castle_43_interior.set_min_pos(-100.0, -100.0)
castle_43_interior.add_accessible_scene("exit")
castle_43_interior.add_chest_troop(trp.castle_33_seneschal)


castle_43_prison = Scene("castle_43_prison", mesh_name="interior_prison_o", body_name="bo_interior_prison_o")
castle_43_prison.add_flag(SceneFlag.IS_INDOORS)
castle_43_prison.set_min_pos(-100.0, -100.0)


castle_44_exterior = Scene("castle_44_exterior", terrain_code="0x0000000053e3b2320004ed3800001eb400006277000068ea", extra_terrain="outer_terrain_desert")
castle_44_exterior.add_flag(SceneFlag.GENERATE)


castle_44_interior = Scene("castle_44_interior", mesh_name="arabian_interior_keep_b", body_name="bo_arabian_interior_keep_b")
castle_44_interior.add_flag(SceneFlag.IS_INDOORS)
castle_44_interior.set_min_pos(-100.0, -100.0)
castle_44_interior.add_accessible_scene("exit")
castle_44_interior.add_chest_troop(trp.castle_34_seneschal)


castle_44_prison = Scene("castle_44_prison", mesh_name="interior_prison_o", body_name="bo_interior_prison_o")
castle_44_prison.add_flag(SceneFlag.IS_INDOORS)
castle_44_prison.set_min_pos(-100.0, -100.0)


castle_45_exterior = Scene("castle_45_exterior", terrain_code="0x0000000254c2ec0000042509000016da0000017200000ed3", extra_terrain="outer_terrain_desert")
castle_45_exterior.add_flag(SceneFlag.GENERATE)


castle_45_interior = Scene("castle_45_interior", mesh_name="arabian_interior_keep_b", body_name="bo_arabian_interior_keep_b")
castle_45_interior.add_flag(SceneFlag.IS_INDOORS)
castle_45_interior.set_min_pos(-100.0, -100.0)
castle_45_interior.add_accessible_scene("exit")
castle_45_interior.add_chest_troop(trp.castle_35_seneschal)


castle_45_prison = Scene("castle_45_prison", mesh_name="interior_prison_n", body_name="bo_interior_prison_n")
castle_45_prison.add_flag(SceneFlag.IS_INDOORS)
castle_45_prison.set_min_pos(-100.0, -100.0)


castle_46_exterior = Scene("castle_46_exterior", terrain_code="0x0000000254c2ec0000042509000016da0000017200000ed3", extra_terrain="outer_terrain_desert")
castle_46_exterior.add_flag(SceneFlag.GENERATE)


castle_46_interior = Scene("castle_46_interior", mesh_name="arabian_interior_keep_b", body_name="bo_arabian_interior_keep_b")
castle_46_interior.add_flag(SceneFlag.IS_INDOORS)
castle_46_interior.set_min_pos(-100.0, -100.0)
castle_46_interior.add_accessible_scene("exit")
castle_46_interior.add_chest_troop(trp.castle_36_seneschal)


castle_46_prison = Scene("castle_46_prison", mesh_name="interior_prison_o", body_name="bo_interior_prison_o")
castle_46_prison.add_flag(SceneFlag.IS_INDOORS)
castle_46_prison.set_min_pos(-100.0, -100.0)


castle_47_exterior = Scene("castle_47_exterior", terrain_code="0x000000005a07b2320002b8ad000036c80000409d00001987", extra_terrain="outer_terrain_desert")
castle_47_exterior.add_flag(SceneFlag.GENERATE)


castle_47_interior = Scene("castle_47_interior", mesh_name="arabian_interior_keep_b", body_name="bo_arabian_interior_keep_b")
castle_47_interior.add_flag(SceneFlag.IS_INDOORS)
castle_47_interior.set_min_pos(-100.0, -100.0)
castle_47_interior.add_accessible_scene("exit")
castle_47_interior.add_chest_troop(trp.castle_37_seneschal)


castle_47_prison = Scene("castle_47_prison", mesh_name="interior_prison_n", body_name="bo_interior_prison_n")
castle_47_prison.add_flag(SceneFlag.IS_INDOORS)
castle_47_prison.set_min_pos(-100.0, -100.0)


castle_48_exterior = Scene("castle_48_exterior", terrain_code="0x0000000056c3da200003a0e6000002a900002d7a0000409e", extra_terrain="outer_terrain_desert")
castle_48_exterior.add_flag(SceneFlag.GENERATE)


castle_48_interior = Scene("castle_48_interior", mesh_name="arabian_interior_keep_b", body_name="bo_arabian_interior_keep_b")
castle_48_interior.add_flag(SceneFlag.IS_INDOORS)
castle_48_interior.set_min_pos(-100.0, -100.0)
castle_48_interior.add_accessible_scene("exit")
castle_48_interior.add_chest_troop(trp.castle_37_seneschal)


castle_48_prison = Scene("castle_48_prison", mesh_name="interior_prison_o", body_name="bo_interior_prison_o")
castle_48_prison.add_flag(SceneFlag.IS_INDOORS)
castle_48_prison.set_min_pos(-100.0, -100.0)


village_1 = Scene("village_1", terrain_code="0x0000000030081763000589620000338e00004f2c00005cfb", extra_terrain="outer_terrain_plain")
village_1.add_flag(SceneFlag.GENERATE)


village_2 = Scene("village_2", terrain_code="0x000000003007a21c0003ecfe000001f0000073b100000fd2", extra_terrain="outer_terrain_plain")
village_2.add_flag(SceneFlag.GENERATE)


village_3 = Scene("village_3", terrain_code="0x000000023003dc4e0006118b000029f8000034670000105f", extra_terrain="outer_terrain_plain")
village_3.add_flag(SceneFlag.GENERATE)


village_4 = Scene("village_4", terrain_code="0x0000000230079732000651a00000044c0000177200000234", extra_terrain="outer_terrain_plain")
village_4.add_flag(SceneFlag.GENERATE)


village_5 = Scene("village_5", terrain_code="0x000000003001ce100006097d0000134c000016d8000042a2", extra_terrain="outer_terrain_plain")
village_5.add_flag(SceneFlag.GENERATE)


village_6 = Scene("village_6", terrain_code="0x0000000230035598000761df000058ea000006f3000005e7", extra_terrain="outer_terrain_plain")
village_6.add_flag(SceneFlag.GENERATE)


village_7 = Scene("village_7", terrain_code="0x0000000031059a0d0004792000005c3a00004df500000dbc", extra_terrain="outer_terrain_plain")
village_7.add_flag(SceneFlag.GENERATE)


village_8 = Scene("village_8", terrain_code="0x00000002300798320006499200002acc000040d70000421d", extra_terrain="outer_terrain_plain")
village_8.add_flag(SceneFlag.GENERATE)


village_9 = Scene("village_9", terrain_code="0x00000004300005008005b57000004e31800017d80000754b", extra_terrain="outer_terrain_plain")
village_9.add_flag(SceneFlag.GENERATE)


village_10 = Scene("village_10", terrain_code="0x000000013005dad40005f57b0000543e0000279d000052b4", extra_terrain="outer_terrain_plain")
village_10.add_flag(SceneFlag.GENERATE)


village_11 = Scene("village_11", terrain_code="0x0000000220029c4400077de100002dcc00002edf00003925", extra_terrain="outer_terrain_steppe")
village_11.add_flag(SceneFlag.GENERATE)


village_12 = Scene("village_12", terrain_code="0x00000002200213e300077ddf000019d3000034520000626e", extra_terrain="outer_terrain_steppe")
village_12.add_flag(SceneFlag.GENERATE)


village_13 = Scene("village_13", terrain_code="0x00000000300265e3400691a400005e4d80006dfa00003bc8", extra_terrain="outer_terrain_plain")
village_13.add_flag(SceneFlag.GENERATE)


village_14 = Scene("village_14", terrain_code="0x0000000230029ce30004912400002acc000040d7000077db", extra_terrain="outer_terrain_plain")
village_14.add_flag(SceneFlag.GENERATE)


village_15 = Scene("village_15", terrain_code="0x00000002300029d4000691a4000015148000335800004190", extra_terrain="outer_terrain_plain")
village_15.add_flag(SceneFlag.GENERATE)


village_16 = Scene("village_16", terrain_code="0x0000000240031a0f0006b9ae00006e1b00006e9000007281", extra_terrain="outer_terrain_snow")
village_16.add_flag(SceneFlag.GENERATE)


village_17 = Scene("village_17", terrain_code="0x00000002c003131700066da00000484c000008630000613d")
village_17.add_flag(SceneFlag.GENERATE)


village_18 = Scene("village_18", terrain_code="0x000000024003561a00070dbe000016f8000010ca000069f8", extra_terrain="outer_terrain_snow")
village_18.add_flag(SceneFlag.GENERATE)


village_19 = Scene("village_19", terrain_code="0x000000024003991e0006f1bc000055cc0000085600001563", extra_terrain="outer_terrain_snow")
village_19.add_flag(SceneFlag.GENERATE)


village_20 = Scene("village_20", terrain_code="0x000000024003d7d20007d1f40000374100001e120000097b", extra_terrain="outer_terrain_snow")
village_20.add_flag(SceneFlag.GENERATE)


village_21 = Scene("village_21", terrain_code="0x0000000240024d3800074dcc0000488b0000016100002047", extra_terrain="outer_terrain_snow")
village_21.add_flag(SceneFlag.GENERATE)


village_22 = Scene("village_22", terrain_code="0x000000024003d7d20007d1f40000374100001e120000097b", extra_terrain="outer_terrain_snow")
village_22.add_flag(SceneFlag.GENERATE)


village_23 = Scene("village_23", terrain_code="0x00000002300415380007b5e600005f7b00000a9200001615")
village_23.add_flag(SceneFlag.GENERATE)


village_24 = Scene("village_24", terrain_code="0x000000023002e1ad00048924000031e70000677500002a0c", extra_terrain="outer_terrain_plain")
village_24.add_flag(SceneFlag.GENERATE)


village_25 = Scene("village_25", terrain_code="0x00000002d0021ede000775dd000032670000173700007c40", extra_terrain="outer_terrain_steppe")
village_25.add_flag(SceneFlag.GENERATE)


village_26 = Scene("village_26", terrain_code="0x0000000230020a008005294c000063fc0000771c0000216f", extra_terrain="outer_terrain_plain")
village_26.add_flag(SceneFlag.GENERATE)


village_27 = Scene("village_27", terrain_code="0x000000013001b2320004a52900004d390000518c00001ab1", extra_terrain="outer_terrain_plain")
village_27.add_flag(SceneFlag.GENERATE)


village_28 = Scene("village_28", terrain_code="0x000000022002de4c00077ddd00007e1300000af400006de1", extra_terrain="outer_terrain_steppe")
village_28.add_flag(SceneFlag.GENERATE)


village_29 = Scene("village_29", terrain_code="0x000000023007b2320004f93c000023ed000053e500002949", extra_terrain="outer_terrain_plain")
village_29.add_flag(SceneFlag.GENERATE)


village_30 = Scene("village_30", terrain_code="0x0000000230025e0a0004dd3700004822000032ea0000011b", extra_terrain="outer_terrain_plain")
village_30.add_flag(SceneFlag.GENERATE)


village_31 = Scene("village_31", terrain_code="0x00000001300619e38003a8ec00004c8380005c6600001cb5", extra_terrain="outer_terrain_plain")
village_31.add_flag(SceneFlag.GENERATE)


village_32 = Scene("village_32", terrain_code="0x00000001300619e30003a8ec00004c8380007de100001cb5", extra_terrain="outer_terrain_plain")
village_32.add_flag(SceneFlag.GENERATE)


village_33 = Scene("village_33", terrain_code="0x0000000130001700000649920000423900007768000062c3", extra_terrain="outer_terrain_plain")
village_33.add_flag(SceneFlag.GENERATE)


village_34 = Scene("village_34", terrain_code="0x00000002300323e3000611860000392d00005c05000067e1", extra_terrain="outer_terrain_plain")
village_34.add_flag(SceneFlag.GENERATE)


village_35 = Scene("village_35", terrain_code="0x0000000230079cb20005394e00001ef90000753000000731", extra_terrain="outer_terrain_town_thir_1")
village_35.add_flag(SceneFlag.GENERATE)


village_36 = Scene("village_36", terrain_code="0x000000013003a1560006118d00003ce300004123000043b2", extra_terrain="outer_terrain_plain")
village_36.add_flag(SceneFlag.GENERATE)


village_37 = Scene("village_37", terrain_code="0x000000022004d36300077dd600002e08000036ab00004651", extra_terrain="outer_terrain_steppe")
village_37.add_flag(SceneFlag.GENERATE)


village_38 = Scene("village_38", terrain_code="0x000000013003e21e0005fd7f000028920000650500005c53", extra_terrain="outer_terrain_plain")
village_38.add_flag(SceneFlag.GENERATE)


village_39 = Scene("village_39", terrain_code="0x000000013003e5990005fd78000069670000446c00007476", extra_terrain="outer_terrain_plain")
village_39.add_flag(SceneFlag.GENERATE)


village_40 = Scene("village_40", terrain_code="0x0000000220031f6300076dda000056f100004f6d000070b3", extra_terrain="outer_terrain_steppe")
village_40.add_flag(SceneFlag.GENERATE)


village_41 = Scene("village_41", terrain_code="0x000000022000a3e300062d8d0000444e0000276e00006eb1", extra_terrain="outer_terrain_steppe")
village_41.add_flag(SceneFlag.GENERATE)


village_42 = Scene("village_42", terrain_code="0x000000022007b23200062d8d000060b900003b8b00006c93", extra_terrain="outer_terrain_steppe")
village_42.add_flag(SceneFlag.GENERATE)


village_43 = Scene("village_43", terrain_code="0x000000022000320e0005856300001d770000792700002aa1", extra_terrain="outer_terrain_steppe")
village_43.add_flag(SceneFlag.GENERATE)


village_44 = Scene("village_44", terrain_code="0x00000002200020200005c574000075480000002d00004be7", extra_terrain="outer_terrain_steppe")
village_44.add_flag(SceneFlag.GENERATE)


village_45 = Scene("village_45", terrain_code="0x000000012007a3df0004e52b0000167700005180000051ea", extra_terrain="outer_terrain_steppe")
village_45.add_flag(SceneFlag.GENERATE)


village_46 = Scene("village_46", terrain_code="0x000000013007a03200061184000058d20000717a00001af0", extra_terrain="outer_terrain_plain")
village_46.add_flag(SceneFlag.GENERATE)


village_47 = Scene("village_47", terrain_code="0x00000000300621b100051d47000034e300007926000048d3", extra_terrain="outer_terrain_plain")
village_47.add_flag(SceneFlag.GENERATE)


village_48 = Scene("village_48", terrain_code="0x00000001b0051ebc00062d8b0000570d00005b3900001ae1", extra_terrain="outer_terrain_plain")
village_48.add_flag(SceneFlag.GENERATE)


village_49 = Scene("village_49", terrain_code="0x0000000140029bbc0006799b000009cb0000720000006555", extra_terrain="outer_terrain_snow")
village_49.add_flag(SceneFlag.GENERATE)


village_50 = Scene("village_50", terrain_code="0x0000000140029bbc0006799b000009cb0000720000006555", extra_terrain="outer_terrain_snow")
village_50.add_flag(SceneFlag.GENERATE)


village_51 = Scene("village_51", terrain_code="0x000000023002b0e30006a5a90000722700002f5200005e2b", extra_terrain="outer_terrain_plain")
village_51.add_flag(SceneFlag.GENERATE)


village_52 = Scene("village_52", terrain_code="0x0000000220011de30005655900002c2300003b2400000d47", extra_terrain="outer_terrain_steppe")
village_52.add_flag(SceneFlag.GENERATE)


village_53 = Scene("village_53", terrain_code="0x000000023002dd19000691a40000566a000012a000001037", extra_terrain="outer_terrain_plain")
village_53.add_flag(SceneFlag.GENERATE)


village_54 = Scene("village_54", terrain_code="0x00000002300032300005c5740000243e000056aa00003a7a", extra_terrain="outer_terrain_plain")
village_54.add_flag(SceneFlag.GENERATE)


village_55 = Scene("village_55", terrain_code="0x00000002300019500006c1b4000065c700002bea0000154e", extra_terrain="outer_terrain_plain")
village_55.add_flag(SceneFlag.GENERATE)


village_56 = Scene("village_56", terrain_code="0x00000002300296320006b5aa00006f3200003a5000004fed", extra_terrain="outer_terrain_town_thir_1")
village_56.add_flag(SceneFlag.GENERATE)


village_57 = Scene("village_57", terrain_code="0x00000002300027b200065d9700004dcf0000212800001bf0", extra_terrain="outer_terrain_plain")
village_57.add_flag(SceneFlag.GENERATE)


village_58 = Scene("village_58", terrain_code="0x00000002300018e38005e58300000376000027e70000015c", extra_terrain="outer_terrain_plain")
village_58.add_flag(SceneFlag.GENERATE)


village_59 = Scene("village_59", terrain_code="0x00000002300022a60005314c0000428100007e0100002e97", extra_terrain="outer_terrain_plain")
village_59.add_flag(SceneFlag.GENERATE)


village_60 = Scene("village_60", terrain_code="0x0000000230079c3200060d860000428100007e01000071b4", extra_terrain="outer_terrain_plain")
village_60.add_flag(SceneFlag.GENERATE)


village_61 = Scene("village_61", terrain_code="0x00000001300325350006659e0000603500006b0200005676", extra_terrain="outer_terrain_plain")
village_61.add_flag(SceneFlag.GENERATE)


village_62 = Scene("village_62", terrain_code="0x0000000143c08f060004e53a00000a500000187700007c9b", extra_terrain="outer_terrain_snow")
village_62.add_flag(SceneFlag.GENERATE)


village_63 = Scene("village_63", terrain_code="0x000000013007a6b20006258b00006bb8000074df00002f18", extra_terrain="outer_terrain_plain")
village_63.add_flag(SceneFlag.GENERATE)


village_64 = Scene("village_64", terrain_code="0x00000001300410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_plain")
village_64.add_flag(SceneFlag.GENERATE)


village_65 = Scene("village_65", terrain_code="0x000000013004d8320006358b00006d2b000005d5000023e5", extra_terrain="outer_terrain_plain")
village_65.add_flag(SceneFlag.GENERATE)


village_66 = Scene("village_66", terrain_code="0x000000013007a2b20006097f00001342000050d900003545", extra_terrain="outer_terrain_town_thir_1")
village_66.add_flag(SceneFlag.GENERATE)


village_67 = Scene("village_67", terrain_code="0x000000013003e02d0005ed7800002c2e0000688800005fe4", extra_terrain="outer_terrain_plain")
village_67.add_flag(SceneFlag.GENERATE)


village_68 = Scene("village_68", terrain_code="0x0000000130079a3200062d8b0000297c00000def000067b7", extra_terrain="outer_terrain_plain")
village_68.add_flag(SceneFlag.GENERATE)


village_69 = Scene("village_69", terrain_code="0x00000002300022a60005314c0000428100007e0100002e97", extra_terrain="outer_terrain_plain")
village_69.add_flag(SceneFlag.GENERATE)


village_70 = Scene("village_70", terrain_code="0x0000000230079c3200060d860000428100007e01000071b4", extra_terrain="outer_terrain_plain")
village_70.add_flag(SceneFlag.GENERATE)


village_71 = Scene("village_71", terrain_code="0x0000000630079ab20005fd7f0000687300007190000006df", extra_terrain="outer_terrain_plain")
village_71.add_flag(SceneFlag.GENERATE)


village_72 = Scene("village_72", terrain_code="0x00000006300654ac00062d910000635800007c9600005d35", extra_terrain="outer_terrain_plain")
village_72.add_flag(SceneFlag.GENERATE)


village_73 = Scene("village_73", terrain_code="0x0000000230079db200050d4500001b4b00007cf400001973", extra_terrain="outer_terrain_plain")
village_73.add_flag(SceneFlag.GENERATE)


village_74 = Scene("village_74", terrain_code="0x00000002300794320005f17c00003187000051540000350a", extra_terrain="outer_terrain_plain")
village_74.add_flag(SceneFlag.GENERATE)


village_75 = Scene("village_75", terrain_code="0x00000002400798b20005ed7b000019160000650f000072d2", extra_terrain="outer_terrain_snow")
village_75.add_flag(SceneFlag.GENERATE)


village_76 = Scene("village_76", terrain_code="0x000000022007a7b200045d19000004920000076d00003b0a", extra_terrain="outer_terrain_steppe")
village_76.add_flag(SceneFlag.GENERATE)


village_77 = Scene("village_77", terrain_code="0x000000023009629a0005615800005564000023590000579e", extra_terrain="outer_terrain_plain")
village_77.add_flag(SceneFlag.GENERATE)


village_78 = Scene("village_78", terrain_code="0x000000023004561e00069da700000f490000256b000058b5", extra_terrain="outer_terrain_plain")
village_78.add_flag(SceneFlag.GENERATE)


village_79 = Scene("village_79", terrain_code="0x0000000230084fac00057d5f00002ba900004a7a000060be", extra_terrain="outer_terrain_plain")
village_79.add_flag(SceneFlag.GENERATE)


village_80 = Scene("village_80", terrain_code="0x000000013001b21e0004f13e000042b2000058e400007fce", extra_terrain="outer_terrain_plain")
village_80.add_flag(SceneFlag.GENERATE)


village_81 = Scene("village_81", terrain_code="0x0000000230079ab20005fd7f0000621700007190000006df", extra_terrain="outer_terrain_plain")
village_81.add_flag(SceneFlag.GENERATE)


village_82 = Scene("village_82", terrain_code="0x000000013002541c00062d8b00000a01000068cb00006d9b", extra_terrain="outer_terrain_plain")
village_82.add_flag(SceneFlag.GENERATE)


village_83 = Scene("village_83", terrain_code="0x000000013007b2320005956300001e640000462c00003a51", extra_terrain="outer_terrain_plain")
village_83.add_flag(SceneFlag.GENERATE)


village_84 = Scene("village_84", terrain_code="0x0000000130069b270004dd390000689b00002d3b00001876", extra_terrain="outer_terrain_plain")
village_84.add_flag(SceneFlag.GENERATE)


village_85 = Scene("village_85", terrain_code="0x000000014007b26300059563000051e000001aa4000034ee", extra_terrain="outer_terrain_snow")
village_85.add_flag(SceneFlag.GENERATE)


village_86 = Scene("village_86", terrain_code="0x000000014007b26300059563000051e000001aa4000034ee", extra_terrain="outer_terrain_snow")
village_86.add_flag(SceneFlag.GENERATE)


village_87 = Scene("village_87", terrain_code="0x000000013001c98a0004dd3000001a5e00005c6200001ec9", extra_terrain="outer_terrain_plain")
village_87.add_flag(SceneFlag.GENERATE)


village_88 = Scene("village_88", terrain_code="0x000000012007a83200049924000049bd00001f7a00006c57", extra_terrain="outer_terrain_steppe")
village_88.add_flag(SceneFlag.GENERATE)


village_89 = Scene("village_89", terrain_code="0x00000001200513940005314c00001f6d00006d7700006698", extra_terrain="outer_terrain_steppe")
village_89.add_flag(SceneFlag.GENERATE)


village_90 = Scene("village_90", terrain_code="0x000000012002cd900005314c00001f6d00006d7700003493", extra_terrain="outer_terrain_steppe")
village_90.add_flag(SceneFlag.GENERATE)


village_91 = Scene("village_91", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_91.add_flag(SceneFlag.GENERATE)


village_92 = Scene("village_92", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_92.add_flag(SceneFlag.GENERATE)


village_93 = Scene("village_93", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_93.add_flag(SceneFlag.GENERATE)


village_94 = Scene("village_94", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_94.add_flag(SceneFlag.GENERATE)


village_95 = Scene("village_95", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_95.add_flag(SceneFlag.GENERATE)


village_96 = Scene("village_96", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_96.add_flag(SceneFlag.GENERATE)


village_97 = Scene("village_97", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_97.add_flag(SceneFlag.GENERATE)


village_98 = Scene("village_98", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_98.add_flag(SceneFlag.GENERATE)


village_99 = Scene("village_99", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_99.add_flag(SceneFlag.GENERATE)


village_100 = Scene("village_100", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_100.add_flag(SceneFlag.GENERATE)


village_101 = Scene("village_101", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_101.add_flag(SceneFlag.GENERATE)


village_102 = Scene("village_102", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_102.add_flag(SceneFlag.GENERATE)


village_103 = Scene("village_103", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_103.add_flag(SceneFlag.GENERATE)


village_104 = Scene("village_104", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_104.add_flag(SceneFlag.GENERATE)


village_105 = Scene("village_105", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_105.add_flag(SceneFlag.GENERATE)


village_106 = Scene("village_106", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_106.add_flag(SceneFlag.GENERATE)


village_107 = Scene("village_107", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_107.add_flag(SceneFlag.GENERATE)


village_108 = Scene("village_108", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_108.add_flag(SceneFlag.GENERATE)


village_109 = Scene("village_109", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_109.add_flag(SceneFlag.GENERATE)


village_110 = Scene("village_110", terrain_code="0x00000001500410320005a96800006b5300004edc00000d11", extra_terrain="outer_terrain_desert")
village_110.add_flag(SceneFlag.GENERATE)


field_1 = Scene("field_1", terrain_code="0x000000033a059a5a0009525600002005000060e300001175", extra_terrain="outer_terrain_plain")
field_1.add_flag(SceneFlag.GENERATE)


field_2 = Scene("field_2", terrain_code="0x000000033a079a3f000a3a8000006dfd000030a100006522", extra_terrain="outer_terrain_steppe")
field_2.add_flag(SceneFlag.GENERATE)


field_3 = Scene("field_3", terrain_code="0x30054da28004050000005a76800022aa00002e3b", extra_terrain="outer_terrain_steppe")
field_3.add_flag(SceneFlag.GENERATE)


field_4 = Scene("field_4", terrain_code="0x30054da28004050000005a76800022aa00002e3b", extra_terrain="outer_terrain_steppe")
field_4.add_flag(SceneFlag.GENERATE)


field_5 = Scene("field_5", terrain_code="0x30054da28004050000005a76800022aa00002e3b", extra_terrain="outer_terrain_steppe")
field_5.add_flag(SceneFlag.GENERATE)


test2 = Scene("test2", terrain_code="0x00000000b0078cb20003fd0000005e480000288c0000286f", extra_terrain="outer_terrain_steppe")
test2.add_flag(SceneFlag.GENERATE)


test3 = Scene("test3", terrain_code="0x00000000b00511d98004b12e0000039f00004e6300005c7d", extra_terrain="outer_terrain_plain")
test3.add_flag(SceneFlag.GENERATE)


multi_scene_1 = Scene("multi_scene_1", terrain_code="0x00000001300389800003a4ea000058340000637a0000399b", extra_terrain="outer_terrain_plain")
multi_scene_1.add_flag(SceneFlag.GENERATE)


multi_scene_2 = Scene("multi_scene_2", terrain_code="0x000000012002a0b20004992700006e54000007fe00001fd2", extra_terrain="outer_terrain_steppe")
multi_scene_2.add_flag(SceneFlag.GENERATE)


multi_scene_3 = Scene("multi_scene_3", terrain_code="0x000000013002e0b20005154500006e540000235600007b55", extra_terrain="outer_terrain_plain")
multi_scene_3.add_flag(SceneFlag.GENERATE)


multi_scene_4 = Scene("multi_scene_4", terrain_code="0x00000001300659630003c8f300003ca000006a8900003c89", extra_terrain="outer_terrain_plain")
multi_scene_4.add_flag(SceneFlag.GENERATE)


multi_scene_5 = Scene("multi_scene_5", terrain_code="0x000000023002a1ba0004210900003ca000006a8900007a7b", extra_terrain="outer_terrain_plain")
multi_scene_5.add_flag(SceneFlag.GENERATE)


multi_scene_6 = Scene("multi_scene_6", terrain_code="0x00000002300494b200048524000059e80000453300001d32", extra_terrain="outer_terrain_plain")
multi_scene_6.add_flag(SceneFlag.GENERATE)


multi_scene_7 = Scene("multi_scene_7", terrain_code="0x0000000130010e0e0005fd84000011c60000285b00005cbe", extra_terrain="outer_terrain_plain")
multi_scene_7.add_flag(SceneFlag.GENERATE)


multi_scene_8 = Scene("multi_scene_8", terrain_code="0x0000000020004db18004611400005c918000397b00004c2e", extra_terrain="outer_terrain_plain")
multi_scene_8.add_flag(SceneFlag.GENERATE)


multi_scene_9 = Scene("multi_scene_9", terrain_code="0x00000000400032320003c0f300001f9e000011180000031c", extra_terrain="outer_terrain_snow")
multi_scene_9.add_flag(SceneFlag.GENERATE)


multi_scene_10 = Scene("multi_scene_10", terrain_code="0x000000003009cde1000599630000423b00005756000000af", extra_terrain="outer_terrain_plain")
multi_scene_10.add_flag(SceneFlag.GENERATE)


multi_scene_11 = Scene("multi_scene_11", terrain_code="0x0000000030015f2b000350d4000011a4000017ee000054af", extra_terrain="outer_terrain_plain")
multi_scene_11.add_flag(SceneFlag.GENERATE)


multi_scene_12 = Scene("multi_scene_12", terrain_code="0x000000013003d7e30005053f00003b4e0000146300006e84", extra_terrain="outer_terrain_beach")
multi_scene_12.add_flag(SceneFlag.GENERATE)


multi_scene_13 = Scene("multi_scene_13", terrain_code="0x00000001300389800003a4ea000058340000637a0000399b", extra_terrain="outer_terrain_plain")
multi_scene_13.add_flag(SceneFlag.GENERATE)


multi_scene_14 = Scene("multi_scene_14", terrain_code="0x0000000040000c910003e8fa0000538900003e9e00005301", extra_terrain="outer_terrain_snow")
multi_scene_14.add_flag(SceneFlag.GENERATE)


multi_scene_15 = Scene("multi_scene_15", terrain_code="0x00000000500b1d158005394c00001230800072880000018f", extra_terrain="outer_terrain_desert")
multi_scene_15.add_flag(SceneFlag.GENERATE)


multi_scene_16 = Scene("multi_scene_16", terrain_code="0x00000000d007abd20002c8b1000050c50000752a0000788c", extra_terrain="outer_terrain_desert")
multi_scene_16.add_flag(SceneFlag.GENERATE)


multi_scene_17 = Scene("multi_scene_17", terrain_code="0x00000002200005000005f57b00005885000046bd00006d9c", extra_terrain="outer_terrain_plain")
multi_scene_17.add_flag(SceneFlag.GENERATE)


multi_scene_18 = Scene("multi_scene_18", terrain_code="0x00000000b00037630002308c00000c9400005d4c00000f3a", extra_terrain="outer_terrain_plain")
multi_scene_18.add_flag(SceneFlag.GENERATE)
multi_scene_18.add_flag(SceneFlag.MUDDY_WATER)


multi_scene_19 = Scene("multi_scene_19", terrain_code="0x00000001300389800003a4ea000058340000637a0000399b", extra_terrain="outer_terrain_plain")
multi_scene_19.add_flag(SceneFlag.GENERATE)


multi_scene_20 = Scene("multi_scene_20", terrain_code="0x000000013002ab630004651800000d7a00007f3100002701", extra_terrain="outer_terrain_plain")
multi_scene_20.add_flag(SceneFlag.GENERATE)


multi_scene_21 = Scene("multi_scene_21", terrain_code="0x0000000040000c910003e8fa0000538900003e9e00005301", extra_terrain="outer_terrain_beach_snowy")
multi_scene_21.add_flag(SceneFlag.GENERATE)


random_multi_plain_medium = Scene("random_multi_plain_medium", water_level=-0.5, terrain_code="0x00000001394018dd000649920004406900002920000056d7", extra_terrain="outer_terrain_plain")
random_multi_plain_medium.add_flag(SceneFlag.GENERATE)
random_multi_plain_medium.add_flag(SceneFlag.RANDOMIZE)
random_multi_plain_medium.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
random_multi_plain_medium.set_min_pos(240.0, 240.0)


random_multi_plain_large = Scene("random_multi_plain_large", water_level=-0.5, terrain_code="0x000000013a001853000aa6a40004406900002920001e4f81", extra_terrain="outer_terrain_plain")
random_multi_plain_large.add_flag(SceneFlag.GENERATE)
random_multi_plain_large.add_flag(SceneFlag.RANDOMIZE)
random_multi_plain_large.add_flag(SceneFlag.AUTO_ENTRY_POINTS)
random_multi_plain_large.set_min_pos(240.0, 240.0)


random_multi_steppe_medium = Scene("random_multi_steppe_medium", water_level=-0.5, terrain_code="0x0000000128601ae300063d8f0004406900002920001e4f81", extra_terrain="outer_terrain_steppe")
random_multi_steppe_medium.add_flag(SceneFlag.GENERATE)
random_multi_steppe_medium.add_flag(SceneFlag.RANDOMIZE)
random_multi_steppe_medium.add_flag(SceneFlag.AUTO_ENTRY_POINTS)


random_multi_steppe_large = Scene("random_multi_steppe_large", water_level=-0.5, terrain_code="0x000000012a00d8630009fe7f0004406900002920001e4f81", extra_terrain="outer_terrain_steppe")
random_multi_steppe_large.add_flag(SceneFlag.GENERATE)
random_multi_steppe_large.add_flag(SceneFlag.RANDOMIZE)
random_multi_steppe_large.add_flag(SceneFlag.AUTO_ENTRY_POINTS)


multiplayer_maps_end = Scene("multiplayer_maps_end", terrain_code="0x00000001300389800003a4ea000058340000637a0000399b", extra_terrain="outer_terrain_plain")
multiplayer_maps_end.add_flag(SceneFlag.GENERATE)


wedding = Scene("wedding", mesh_name="castle_h_interior_a", body_name="bo_castle_h_interior_a")
wedding.add_flag(SceneFlag.IS_INDOORS)
wedding.set_min_pos(-100.0, -100.0)


lair_steppe_bandits = Scene("lair_steppe_bandits", terrain_code="0x00000000200c69ac80043d0d0000556b0000768400003ea9", extra_terrain="outer_terrain_steppe")
lair_steppe_bandits.add_flag(SceneFlag.GENERATE)


lair_taiga_bandits = Scene("lair_taiga_bandits", terrain_code="0x000000004c079c3e000499280000420f0000495d000048d6", extra_terrain="outer_terrain_snow")
lair_taiga_bandits.add_flag(SceneFlag.GENERATE)


lair_desert_bandits = Scene("lair_desert_bandits", terrain_code="0x000000005024cd120005595400003882000037a90000673e", extra_terrain="outer_terrain_desert")
lair_desert_bandits.add_flag(SceneFlag.GENERATE)


lair_forest_bandits = Scene("lair_forest_bandits", terrain_code="0x00000000b00326d90003ecfb0000657e0000213500002461", extra_terrain="outer_terrain_plain")
lair_forest_bandits.add_flag(SceneFlag.GENERATE)


lair_mountain_bandits = Scene("lair_mountain_bandits", terrain_code="0x00000000200434070004450c000022bf00006ad6000060ed", extra_terrain="outer_terrain_steppe")
lair_mountain_bandits.add_flag(SceneFlag.GENERATE)


lair_sea_raiders = Scene("lair_sea_raiders", terrain_code="0x00000000b00562e200040900000063f40000679f00006cda", extra_terrain="sea_outer_terrain_1")
lair_sea_raiders.add_flag(SceneFlag.GENERATE)


quick_battle_scene_1 = Scene("quick_battle_scene_1", terrain_code="0x000000023002dee300045d1d000001bf0000299a0000638f", extra_terrain="outer_terrain_plain")
quick_battle_scene_1.add_flag(SceneFlag.GENERATE)
quick_battle_scene_1.set_min_pos(120.0, 120.0)


quick_battle_scene_2 = Scene("quick_battle_scene_2", terrain_code="0x0000000250001d630005114300006228000053bf00004eb9", extra_terrain="outer_terrain_desert_b")
quick_battle_scene_2.add_flag(SceneFlag.GENERATE)
quick_battle_scene_2.set_min_pos(120.0, 120.0)


quick_battle_scene_3 = Scene("quick_battle_scene_3", terrain_code="0x000000023002b76300046d2400000190000076300000692a", extra_terrain="outer_terrain_plain")
quick_battle_scene_3.add_flag(SceneFlag.GENERATE)
quick_battle_scene_3.set_min_pos(120.0, 120.0)


quick_battle_scene_4 = Scene("quick_battle_scene_4", terrain_code="0x000000025a00f23700057d5f00006d6a000050ba000036df", extra_terrain="outer_terrain_desert_b")
quick_battle_scene_4.add_flag(SceneFlag.GENERATE)
quick_battle_scene_4.set_min_pos(120.0, 120.0)


quick_battle_scene_5 = Scene("quick_battle_scene_5", terrain_code="0x000000012007985300055550000064d500005c060000759e", extra_terrain="outer_terrain_plain")
quick_battle_scene_5.add_flag(SceneFlag.GENERATE)


quick_battle_maps_end = Scene("quick_battle_maps_end", terrain_code="0x00000001300389800003a4ea000058340000637a0000399b", extra_terrain="outer_terrain_plain")
quick_battle_maps_end.add_flag(SceneFlag.GENERATE)


tutorial_training_ground = Scene("tutorial_training_ground", terrain_code="0x000000003000050000046d1b0000189f00002a8380006d91", extra_terrain="outer_terrain_plain")
tutorial_training_ground.add_flag(SceneFlag.GENERATE)
tutorial_training_ground.set_min_pos(120.0, 120.0)


town_1_room = Scene("town_1_room", mesh_name="viking_interior_tavern_a", body_name="bo_viking_interior_tavern_a")
town_1_room.add_flag(SceneFlag.IS_INDOORS)
town_1_room.set_min_pos(-100.0, -100.0)


town_5_room = Scene("town_5_room", mesh_name="interior_town_house_d", body_name="bo_interior_town_house_d")
town_5_room.add_flag(SceneFlag.IS_INDOORS)
town_5_room.set_min_pos(-100.0, -100.0)
town_5_room.add_accessible_scene("exit")


town_6_room = Scene("town_6_room", mesh_name="interior_town_house_j", body_name="bo_interior_town_house_j")
town_6_room.add_flag(SceneFlag.IS_INDOORS)
town_6_room.set_min_pos(-100.0, -100.0)
town_6_room.add_accessible_scene("exit")


town_8_room = Scene("town_8_room", mesh_name="interior_house_b", body_name="bo_interior_house_b")
town_8_room.add_flag(SceneFlag.IS_INDOORS)
town_8_room.set_min_pos(-100.0, -100.0)
town_8_room.add_accessible_scene("exit")


town_10_room = Scene("town_10_room", mesh_name="interior_town_house_steppe_c", body_name="bo_interior_town_house_steppe_c")
town_10_room.add_flag(SceneFlag.IS_INDOORS)
town_10_room.set_min_pos(-100.0, -100.0)
town_10_room.add_accessible_scene("exit")


town_19_room = Scene("town_19_room", mesh_name="interior_town_house_steppe_d", body_name="bo_interior_town_house_steppe_d")
town_19_room.add_flag(SceneFlag.IS_INDOORS)
town_19_room.set_min_pos(-100.0, -100.0)
town_19_room.add_accessible_scene("exit")


meeting_scene_steppe = Scene("meeting_scene_steppe", mesh_name="ch_meet_steppe_a", body_name="bo_encounter_spot")
meeting_scene_steppe.set_min_pos(-40.0, -40.0)
meeting_scene_steppe.set_min_pos(40.0, 40.0)


meeting_scene_plain = Scene("meeting_scene_plain", mesh_name="ch_meet_plain_a", body_name="bo_encounter_spot")
meeting_scene_plain.set_min_pos(-40.0, -40.0)
meeting_scene_plain.set_min_pos(40.0, 40.0)


meeting_scene_snow = Scene("meeting_scene_snow", mesh_name="ch_meet_snow_a", body_name="bo_encounter_spot")
meeting_scene_snow.set_min_pos(-40.0, -40.0)
meeting_scene_snow.set_min_pos(40.0, 40.0)


meeting_scene_desert = Scene("meeting_scene_desert", mesh_name="ch_meet_desert_a", body_name="bo_encounter_spot")
meeting_scene_desert.set_min_pos(-40.0, -40.0)
meeting_scene_desert.set_min_pos(40.0, 40.0)


meeting_scene_steppe_forest = Scene("meeting_scene_steppe_forest", mesh_name="ch_meet_steppe_a", body_name="bo_encounter_spot")
meeting_scene_steppe_forest.set_min_pos(-40.0, -40.0)
meeting_scene_steppe_forest.set_min_pos(40.0, 40.0)


meeting_scene_plain_forest = Scene("meeting_scene_plain_forest", mesh_name="ch_meet_plain_a", body_name="bo_encounter_spot")
meeting_scene_plain_forest.set_min_pos(-40.0, -40.0)
meeting_scene_plain_forest.set_min_pos(40.0, 40.0)


meeting_scene_snow_forest = Scene("meeting_scene_snow_forest", mesh_name="ch_meet_snow_a", body_name="bo_encounter_spot")
meeting_scene_snow_forest.set_min_pos(-40.0, -40.0)
meeting_scene_snow_forest.set_min_pos(40.0, 40.0)


meeting_scene_desert_forest = Scene("meeting_scene_desert_forest", mesh_name="ch_meet_desert_a", body_name="bo_encounter_spot")
meeting_scene_desert_forest.set_min_pos(-40.0, -40.0)
meeting_scene_desert_forest.set_min_pos(40.0, 40.0)


enterprise_tannery = Scene("enterprise_tannery", mesh_name="ch_meet_steppe_a", body_name="bo_encounter_spot", terrain_code="0x000000012004480500040902000041cb00005ae800000ff5")
enterprise_tannery.add_flag(SceneFlag.GENERATE)
enterprise_tannery.set_min_pos(-40.0, -40.0)
enterprise_tannery.set_min_pos(40.0, 40.0)


enterprise_winery = Scene("enterprise_winery", mesh_name="winery_interior", body_name="bo_winery_interior")
enterprise_winery.add_flag(SceneFlag.IS_INDOORS)
enterprise_winery.set_min_pos(-40.0, -40.0)
enterprise_winery.set_min_pos(40.0, 40.0)


enterprise_mill = Scene("enterprise_mill", mesh_name="mill_interior", body_name="bo_mill_interior")
enterprise_mill.add_flag(SceneFlag.IS_INDOORS)
enterprise_mill.set_min_pos(-40.0, -40.0)
enterprise_mill.set_min_pos(40.0, 40.0)


enterprise_smithy = Scene("enterprise_smithy", mesh_name="smithy_interior", body_name="bo_smithy_interior")
enterprise_smithy.add_flag(SceneFlag.IS_INDOORS)
enterprise_smithy.set_min_pos(-40.0, -40.0)
enterprise_smithy.set_min_pos(40.0, 40.0)


enterprise_dyeworks = Scene("enterprise_dyeworks", mesh_name="weavery_interior", body_name="bo_weavery_interior")
enterprise_dyeworks.add_flag(SceneFlag.IS_INDOORS)
enterprise_dyeworks.set_min_pos(-40.0, -40.0)
enterprise_dyeworks.set_min_pos(40.0, 40.0)


enterprise_linen_weavery = Scene("enterprise_linen_weavery", mesh_name="weavery_interior", body_name="bo_weavery_interior")
enterprise_linen_weavery.add_flag(SceneFlag.IS_INDOORS)
enterprise_linen_weavery.set_min_pos(-40.0, -40.0)
enterprise_linen_weavery.set_min_pos(40.0, 40.0)


enterprise_wool_weavery = Scene("enterprise_wool_weavery", mesh_name="weavery_interior", body_name="bo_weavery_interior")
enterprise_wool_weavery.add_flag(SceneFlag.IS_INDOORS)
enterprise_wool_weavery.set_min_pos(-40.0, -40.0)
enterprise_wool_weavery.set_min_pos(40.0, 40.0)


enterprise_brewery = Scene("enterprise_brewery", mesh_name="brewery_interior", body_name="bo_brewery_interior")
enterprise_brewery.add_flag(SceneFlag.IS_INDOORS)
enterprise_brewery.set_min_pos(-40.0, -40.0)
enterprise_brewery.set_min_pos(40.0, 40.0)


enterprise_oil_press = Scene("enterprise_oil_press", mesh_name="oil_press_interior", body_name="bo_oil_press_interior")
enterprise_oil_press.add_flag(SceneFlag.IS_INDOORS)
enterprise_oil_press.set_min_pos(-40.0, -40.0)
enterprise_oil_press.set_min_pos(40.0, 40.0)


# Accessible Scenes (Deprecated)
#zendar_center.add_accessible_scene(the_happy_boar)
#zendar_center.add_accessible_scene(zendar_merchant)
#the_happy_boar.add_accessible_scene(zendar_center)
