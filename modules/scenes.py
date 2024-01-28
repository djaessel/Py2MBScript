# This Python file uses the following encoding: utf-8

from scene import Scene, SceneFlag

#import sys
#sys.path.append("../data_objects/")


random_scene = Scene("random_scene", water_level=-0.5, terrain_code="0x300028000003e8fa0000034e00004b34000059be")
random_scene.set_max_pos(240, 240)
random_scene.add_flag(SceneFlag.GENERATE)
random_scene.add_flag(SceneFlag.RANDOMIZE)
random_scene.add_flag(SceneFlag.AUTO_ENTRY_POINTS)

conversation_scene = Scene("conversation_scene", mesh_name="encounter_spot", body_name="bo_encounter_spot")
conversation_scene.set_min_pos(-40, -40)
conversation_scene.set_max_pos(40, 40)

water = Scene("water", water_level=-0.5)
water.set_min_pos(-1000, -1000)
water.set_max_pos(1000, 1000)

#---

town_1_alley = Scene("town_1_alley", terrain_code="0x300bc5430001e0780000448a0000049f00007932", extra_terrain="outer_terrain_plain")
town_1_alley.add_flag(SceneFlag.GENERATE)

#---

castle_1_interior = Scene("castle_1_interior", mesh_name="dungeon_entry_a", body_name="bo_dungeon_entry_a")
castle_1_interior.set_min_pos(-100, -100)
castle_1_interior.add_flag(SceneFlag.IS_INDOORS)
castle_1_interior.add_accessible_scene("exit")


