from header_common import *
from ID_animations import *
from header_mission_templates import *
from header_tableau_materials import *
from header_items import *
from module_constants import *

tableaus = [

("game_character_sheet", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 266, 532, [
(store_script_param, ":troop_no", 1),
(cur_tableau_set_background_color, 0xFF888888),
(cur_tableau_set_ambient_light, 10, 11, 15),
(set_fixed_point_multiplier, 100),
(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
(init_position,pos1),
(position_set_z,pos1,100),
(position_set_x,pos1,-20),
(position_set_y,pos1,-20),
(cur_tableau_add_tableau_mesh, "tableau_troop_character_color", ":troop_no", pos1),
(position_set_z,pos1,200),
(cur_tableau_add_tableau_mesh, "tableau_troop_character_alpha_mask", ":troop_no", pos1),
(position_set_z,pos1,300),
]),

("game_inventory_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 180, 270, [
(store_script_param, ":troop_no", 1),
(cur_tableau_set_background_color, 0xFF888888),
(cur_tableau_set_ambient_light, 10, 11, 15),
(set_fixed_point_multiplier, 100),
(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
(init_position,pos1),
(position_set_z,pos1,100),
(position_set_x,pos1,-20),
(position_set_y,pos1,-20),
(cur_tableau_add_tableau_mesh, "tableau_troop_character_color", ":troop_no", pos1),
(position_set_z,pos1,200),
(cur_tableau_add_tableau_mesh, "tableau_troop_character_alpha_mask", ":troop_no", pos1),
(position_set_z,pos1,300),
]),

("troop_character_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":troop_no", 1),
(cur_tableau_set_background_color, 0xFFE0CFB1),
(cur_tableau_set_ambient_light, 10, 11, 15),
(call_script, "script_add_troop_to_cur_tableau_for_character", ":troop_no"),
]),

("troop_character_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":troop_no", 1),
(cur_tableau_set_background_color, 0x00888888),
(cur_tableau_set_ambient_light, 10, 11, 15),
(cur_tableau_render_as_alpha_mask),
(call_script, "script_add_troop_to_cur_tableau_for_character", ":troop_no"),
]),


] # TABLEAU MATERIALS END
