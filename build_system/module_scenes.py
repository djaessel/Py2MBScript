from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

scenes = [

("random_scene", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0, 0), (240, 240), -0.5, "0x300028000003e8fa0000034e00004b34000059be", [], []),
("conversation_scene", 0, "encounter_spot", "bo_encounter_spot", (-40, -40), (40, 40), -100, "0", [], []),
("water", 0, "none", "none", (-1000, -1000), (1000, 1000), -0.5, "0", [], []),
("town_1_alley", sf_generate, "none", "none", (0, 0), (100, 100), -100, "0x300bc5430001e0780000448a0000049f00007932", [], [], "outer_terrain_plain"),
("castle_1_interior", sf_indoors, "dungeon_entry_a", "bo_dungeon_entry_a", (-100, -100), (100, 100), -100, "0", ["exit"], []),

] # SCENES END
