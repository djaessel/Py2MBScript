from header_operations import *
from header_common import *

tableau_materials = [

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


] # TABLEAU MATERIALS END
