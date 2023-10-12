# This Python file uses the following encoding: utf-8

from scene import Scene, SceneFlag

#import sys
#sys.path.append("../data_objects/")


#("random_scene",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
#  [],[]),
#("conversation_scene",0,"encounter_spot", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
#  [],[]),
#("water",0,"none", "none", (-1000,-1000),(1000,1000),-0.5,"0",
#  [],[]),
#
#("town_1_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
#  [],[],"outer_terrain_plain"),
#
#("castle_1_interior",sf_indoors, "dungeon_entry_a", "bo_dungeon_entry_a", (-100,-100),(100,100),-100,"0",
#  ["exit"],[]),


scene1 = Scene("random_scene", water_level=-0.5, terrain_code="0x300028000003e8fa0000034e00004b34000059be")
scene1.set_max_pos(240, 240)
scene1.add_flag(SceneFlag.GENERATE)
scene1.add_flag(SceneFlag.RANDOMIZE)
scene1.add_flag(SceneFlag.AUTO_ENTRY_POINTS)

scene2 = Scene("conversation_scene", mesh_name="encounter_spot", body_name="bo_encounter_spot")
scene2.set_min_pos(-40, -40)
scene2.set_max_pos(40, 40)

scene3 = Scene("water", water_level=-0.5)
scene3.set_min_pos(-1000, -1000)
scene3.set_max_pos(1000, 1000)


scene5 = Scene("town_1_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_plain")
scene5.add_flag(SceneFlag.GENERATE)


scene4 = Scene("castle_1_interior", mesh_name="dungeon_entry_a", body_name="bo_dungeon_entry_a")
scene4.set_min_pos(-100, -100)
scene4.add_flag(SceneFlag.IS_INDOORS)
scene4.add_accessible_scene("exit")


