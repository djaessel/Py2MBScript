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
]),

("game_event_party_encounter", [
(store_script_param, "$g_encountered_party", 1),
(store_script_param, "$g_encountered_party_2", 2),
(store_faction_of_party, "$g_encountered_party_faction", "$g_encountered_party"),
(store_relation,"$g_encountered_party_relation","$g_encountered_party_faction","fac_player_faction"),
(party_get_template_id,":template_idx","$g_encountered_party"),
(try_begin),
    (eq,":template_idx",0),
    (jump_to_menu,"mnu_town"),
(else_try),
    (jump_to_menu,"mnu_simple_encounter"),
(try_end),
]),

("add_troop_to_cur_tableau_for_character", [
(store_script_param, ":troop_no", 1),
(set_fixed_point_multiplier, 100),
(cur_tableau_clear_override_items),
(init_position,pos2),
(cur_tableau_set_camera_parameters, 1, 4, 8, 10, 10000),
(init_position,pos5),
(assign,":cam_height",150),
(assign,":camera_distance",360),
(assign,":camera_yaw",-15),
(assign,":camera_pitch",-18),
(assign,":animation",1),
(position_set_z,pos5,":cam_height"),
(position_rotate_x,pos5,-90),
(position_rotate_z,pos5,180,0),
(position_rotate_y,pos5,":camera_yaw"),
(position_rotate_x,pos5,":camera_pitch"),
(position_move_z,pos5,":camera_distance",0),
(position_move_x,pos5,5,0),
(try_begin),
    (troop_is_hero,":troop_no"),
    (cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
(else_try),
(try_end),
(store_mul, ":random_seed", ":troop_no", 126233),
(val_mod, ":random_seed", 1000),
(val_add, ":random_seed", 1),
(cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
(cur_tableau_set_camera_position, pos5),
(copy_position,pos8,pos5),
(position_rotate_x,pos8,-90),
(position_rotate_z,pos8,30,0),
(position_rotate_x,pos8,-60),
(cur_tableau_add_sun_light, 0, pos8, 175, 150, 125),
]),

]
