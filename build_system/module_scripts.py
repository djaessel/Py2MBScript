# -*- coding: cp1254 -*-
from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from header_presentations import *
from ID_animations import *

scripts = [

("game_start", [
(display_message, "@Hello world!"),
(set_spawn_radius,1),
(try_for_range, ":unused", 0, 3),
    (spawn_around_party,"p_main_party","pt_hunters"),
    (party_set_ai_behavior,reg0,0),
(try_end),
]),

("game_event_party_encounter", [
(store_script_param, "$g_encountered_party", 1),
(store_script_param, "$g_encountered_party_2", 2),
(store_faction_of_party, "$g_encountered_party_faction", "$g_encountered_party"),
(store_relation,"$g_encountered_party_relation","$g_encountered_party_faction","fac_player_faction"),
(jump_to_menu,"mnu_town"),
]),

]
