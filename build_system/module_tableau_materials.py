from header_common import *
from ID_animations import *
from header_mission_templates import *
from header_tableau_materials import *
from header_items import *
from module_constants import *

tableaus = [

("game_character_sheet", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 266, 532, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4287137928),
(cur_tableau_set_ambient_light, 10, 11, 15),
(set_fixed_point_multiplier, 100),
(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
(init_position,1),
(position_set_z,1,100),
(position_set_x,1,-20),
(position_set_y,1,-20),
(cur_tableau_add_tableau_mesh, "tab_troop_character_color", ":var001", 1),
(position_set_z,1,200),
(cur_tableau_add_tableau_mesh, "tab_troop_character_alpha_mask", ":var001", 1),
(position_set_z,1,300),
]),

("game_inventory_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 180, 270, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4287137928),
(cur_tableau_set_ambient_light, 10, 11, 15),
(set_fixed_point_multiplier, 100),
(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
(init_position,1),
(position_set_z,1,100),
(position_set_x,1,-20),
(position_set_y,1,-20),
(cur_tableau_add_tableau_mesh, "tab_troop_inventory_color", ":var001", 1),
(position_set_z,1,200),
(cur_tableau_add_tableau_mesh, "tab_troop_inventory_alpha_mask", ":var001", 1),
(position_set_z,1,300),
]),

("game_profile_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 320, 480, [
(store_script_param, ":var001", 1),
(assign,":var002",":var001"),
(val_mod, ":var002", 2),
(try_begin),
    (eq,":var002",0),
    (assign,":troop_id_003","trp_multiplayer_profile_troop_male"),
(else_try),
    (assign,":troop_id_003","trp_multiplayer_profile_troop_female"),
(try_end),
(troop_set_face_key_from_current_profile, ":troop_id_003"),
(cur_tableau_set_background_color, 4287137928),
(cur_tableau_set_ambient_light, 10, 11, 15),
(set_fixed_point_multiplier, 100),
(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
(init_position,1),
(position_set_z,1,100),
(position_set_x,1,-20),
(position_set_y,1,-20),
(cur_tableau_add_tableau_mesh, "tab_troop_profile_color", ":troop_id_003", 1),
(position_set_z,1,200),
(cur_tableau_add_tableau_mesh, "tab_troop_profile_alpha_mask", ":troop_id_003", 1),
]),

("game_party_window", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 300, 300, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4287137928),
(cur_tableau_set_ambient_light, 10, 11, 15),
(set_fixed_point_multiplier, 100),
(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
(init_position,1),
(position_set_z,1,100),
(position_set_x,1,-20),
(position_set_y,1,-20),
(cur_tableau_add_tableau_mesh, "tab_troop_party_color", ":var001", 1),
(position_set_z,1,200),
(cur_tableau_add_tableau_mesh, "tab_troop_party_alpha_mask", ":var001", 1),
(position_set_z,1,300),
]),

("game_troop_label_banner", 0, "tableau_with_transparency", 256, 256, -128, 0, 128, 256, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4287137928),
(set_fixed_point_multiplier, 100),
(cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
(init_position,1),
(position_set_y,1,120),
(cur_tableau_add_mesh, ":var001", 1, 120, 120),
]),

("round_shield_1", 0, "sample_shield_round_1", 512, 256, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-50),
(position_set_y,1,125),
(cur_tableau_add_mesh, ":var001", 1, 120, 120),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_1", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
]),

("round_shield_2", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-50),
(position_set_y,1,120),
(cur_tableau_add_mesh, ":var001", 1, 116, 116),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_2", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
]),

("round_shield_3", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-50),
(position_set_y,1,120),
(cur_tableau_add_mesh, ":var001", 1, 116, 116),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_3", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
]),

("round_shield_4", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-50),
(position_set_y,1,125),
(cur_tableau_add_mesh, ":var001", 1, 123, 123),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_4", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
]),

("round_shield_5", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-50),
(position_set_y,1,125),
(cur_tableau_add_mesh, ":var001", 1, 122, 122),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_round_5", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
]),

("small_round_shield_1", 0, "sample_shield_small_round_1", 512, 256, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-50),
(position_set_y,1,130),
(cur_tableau_add_mesh, ":var001", 1, 127, 127),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_small_round_1", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
]),

("small_round_shield_2", 0, "sample_shield_small_round_2", 512, 256, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-50),
(position_set_y,1,130),
(cur_tableau_add_mesh, ":var001", 1, 127, 127),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_small_round_2", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
]),

("small_round_shield_3", 0, "sample_shield_matte", 512, 256, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-50),
(position_set_y,1,130),
(cur_tableau_add_mesh, ":var001", 1, 127, 127),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_small_round_3", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 100, 0, 100000),
]),

("kite_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-60),
(position_set_y,1,140),
(cur_tableau_add_mesh, ":var001", 1, 116, 116),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_1", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("kite_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-57),
(position_set_y,1,140),
(cur_tableau_add_mesh, ":var001", 1, 116, 116),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_2", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("kite_shield_3", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-57),
(position_set_y,1,140),
(cur_tableau_add_mesh, ":var001", 1, 116, 116),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_3", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("kite_shield_4", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-50),
(position_set_y,1,160),
(cur_tableau_add_mesh, ":var001", 1, 120, 120),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_kite_4", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("heater_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-60),
(position_set_y,1,151),
(cur_tableau_add_mesh, ":var001", 1, 116, 116),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_heater_1", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("heater_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-50),
(position_set_y,1,150),
(cur_tableau_add_mesh, ":var001", 1, 116, 116),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_heater_2", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("pavise_shield_1", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-54),
(position_set_y,1,120),
(cur_tableau_add_mesh, ":var001", 1, 118, 118),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_pavise_1", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("pavise_shield_2", 0, "sample_shield_matte", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(position_set_x,1,-54),
(position_set_y,1,120),
(cur_tableau_add_mesh, ":var001", 1, 116, 116),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_shield_pavise_2", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("heraldic_armor_a", 0, "sample_heraldic_armor_a", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(store_sub, ":slot_no_002", ":var001", ":mesh.arms_a01"),
(troop_get_slot,":troop_slot_003","trp_banner_background_color_array",":slot_no_002"),
(cur_tableau_set_background_color, ":troop_slot_003"),
(init_position,1),
(cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", 1, 200, 200, ":troop_slot_003"),
(init_position,1),
(position_set_z,1,50),
(position_set_x,1,-25),
(position_set_y,1,130),
(cur_tableau_add_mesh, ":var001", 1, 103, 103),
(init_position,1),
(position_set_z,1,100),
(cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_a", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("heraldic_armor_b", 0, "sample_heraldic_armor_b", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(store_sub, ":slot_no_002", ":var001", ":mesh.arms_a01"),
(troop_get_slot,":troop_slot_003","trp_banner_background_color_array",":slot_no_002"),
(cur_tableau_set_background_color, ":troop_slot_003"),
(init_position,1),
(cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", 1, 200, 200, ":troop_slot_003"),
(init_position,1),
(position_set_z,1,10),
(position_set_x,1,-5),
(position_set_y,1,130),
(cur_tableau_add_mesh, ":var001", 1, 113, 113),
(init_position,1),
(position_set_z,1,100),
(cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_b", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("heraldic_armor_c", 0, "sample_heraldic_armor_c", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(store_sub, ":slot_no_002", ":var001", ":mesh.arms_a01"),
(troop_get_slot,":troop_slot_003","trp_banner_background_color_array",":slot_no_002"),
(cur_tableau_set_background_color, ":troop_slot_003"),
(init_position,1),
(cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", 1, 200, 200, ":troop_slot_003"),
(init_position,1),
(position_set_z,1,10),
(position_set_x,1,0),
(position_set_y,1,130),
(cur_tableau_add_mesh, ":var001", 1, 115, 115),
(init_position,1),
(position_set_z,1,100),
(cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_c", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("heraldic_armor_d", 0, "sample_heraldic_armor_d", 512, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(store_sub, ":slot_no_002", ":var001", ":mesh.arms_a01"),
(troop_get_slot,":troop_slot_003","trp_banner_background_color_array",":slot_no_002"),
(cur_tableau_set_background_color, ":troop_slot_003"),
(init_position,1),
(cur_tableau_add_mesh_with_vertex_color, "mesh_heraldic_armor_bg", 1, 200, 200, ":troop_slot_003"),
(init_position,1),
(position_set_z,1,10),
(position_set_x,1,0),
(position_set_y,1,130),
(cur_tableau_add_mesh, ":var001", 1, 113, 113),
(init_position,1),
(position_set_z,1,100),
(cur_tableau_add_mesh, "mesh_tableau_mesh_heraldic_armor_d", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 200, 200, 0, 100000),
]),

("troop_note_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 8947848),
(cur_tableau_set_ambient_light, 10, 11, 15),
(cur_tableau_render_as_alpha_mask),
(call_script, "script_add_troop_to_cur_tableau", ":var001"),
]),

("troop_note_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4291214228),
(cur_tableau_set_ambient_light, 10, 11, 15),
(call_script, "script_add_troop_to_cur_tableau", ":var001"),
]),

("troop_character_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 8947848),
(cur_tableau_set_ambient_light, 10, 11, 15),
(cur_tableau_render_as_alpha_mask),
(call_script, "script_add_troop_to_cur_tableau_for_character", ":var001"),
]),

("troop_character_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4292923313),
(cur_tableau_set_ambient_light, 10, 11, 15),
(call_script, "script_add_troop_to_cur_tableau_for_character", ":var001"),
]),

("troop_inventory_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 8947848),
(cur_tableau_set_ambient_light, 10, 11, 15),
(cur_tableau_render_as_alpha_mask),
(call_script, "script_add_troop_to_cur_tableau_for_inventory", ":var001"),
]),

("troop_inventory_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4285159482),
(cur_tableau_set_ambient_light, 10, 11, 15),
(call_script, "script_add_troop_to_cur_tableau_for_inventory", ":var001"),
]),

("troop_profile_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 8947848),
(cur_tableau_set_ambient_light, 10, 11, 15),
(cur_tableau_render_as_alpha_mask),
(call_script, "script_add_troop_to_cur_tableau_for_profile", ":var001"),
]),

("troop_profile_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4294567848),
(cur_tableau_set_ambient_light, 10, 11, 15),
(call_script, "script_add_troop_to_cur_tableau_for_profile", ":var001"),
]),

("troop_party_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 8947848),
(cur_tableau_set_ambient_light, 10, 11, 15),
(cur_tableau_render_as_alpha_mask),
(call_script, "script_add_troop_to_cur_tableau_for_party", ":var001"),
]),

("troop_party_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4290681970),
(cur_tableau_set_ambient_light, 10, 11, 15),
(call_script, "script_add_troop_to_cur_tableau_for_party", ":var001"),
]),

("troop_note_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 350, 350, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4287137928),
(cur_tableau_set_ambient_light, 10, 11, 15),
(set_fixed_point_multiplier, 100),
(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
(init_position,1),
(position_set_z,1,100),
(position_set_x,1,-20),
(position_set_y,1,-20),
(cur_tableau_add_tableau_mesh, "tab_troop_note_color", ":var001", 1),
(position_set_z,1,200),
(cur_tableau_add_tableau_mesh, "tab_troop_note_alpha_mask", ":var001", 1),
(position_set_z,1,300),
(cur_tableau_add_mesh, "mesh_portrait_blend_out", 1, 0, 0),
]),

("center_note_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(cur_tableau_set_background_color, 8947848),
(cur_tableau_set_ambient_light, 10, 11, 15),
(init_position,8),
(position_set_x,8,-210),
(position_set_y,8,200),
(position_set_z,8,300),
(cur_tableau_add_point_light, 0, 8, 550, 500, 450),
(cur_tableau_set_camera_parameters, 1, 10, 10, 10, 10000),
(init_position,1),
(position_set_z,1,0),
(position_set_z,1,-500),
(init_position,1),
(position_set_y,1,-100),
(position_set_x,1,-100),
(position_set_z,1,100),
(position_rotate_z,1,200),
(party_get_icon, ":party_icon_002", ":var001"),
(try_begin),
    (ge,":party_icon_002",0),
    (cur_tableau_add_map_icon, ":party_icon_002", 1, 0),
(try_end),
(init_position,5),
(position_set_x,5,-90),
(position_set_z,5,500),
(position_set_y,5,480),
(position_rotate_x,5,-90),
(position_rotate_z,5,180),
(position_rotate_x,5,-35),
(cur_tableau_set_camera_position, 5),
]),

("faction_note_mesh_for_menu", 0, "pic_arms_swadian", 1024, 512, 0, 0, 450, 225, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4294967295),
(set_fixed_point_multiplier, 100),
(try_begin),
    (is_between,":var001","fac_kingdom_1","fac_kingdoms_end"),
    (assign,":var002","mesh_pic_arms_swadian"),
    (val_add, ":var002", ":var001"),
    (assign,":var002 -","fac_kingdom_1"),
    (init_position,1),
    (position_set_y,1,-5),
    (position_set_x,1,-45),
    (cur_tableau_add_mesh, ":var002", 1, 0, 0),
    (cur_tableau_set_camera_parameters, 0, 160, 80, 0, 100000),
(try_end),
]),

("faction_note_mesh", 0, "pic_arms_swadian", 1024, 512, 0, 0, 500, 250, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4294967295),
(set_fixed_point_multiplier, 100),
(try_begin),
    (is_between,":var001","fac_kingdom_1","fac_kingdoms_end"),
    (assign,":var002","mesh_pic_arms_swadian"),
    (val_add, ":var002", ":var001"),
    (assign,":var002 -","fac_kingdom_1"),
    (init_position,1),
    (position_set_y,1,-5),
    (cur_tableau_add_mesh, ":var002", 1, 0, 0),
    (cur_tableau_set_camera_parameters, 0, 100, 50, 0, 100000),
(try_end),
]),

("faction_note_mesh_banner", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200, [
(store_script_param, ":faction_id_001", 1),
(set_fixed_point_multiplier, 100),
(try_begin),
    (eq,1,1),
    (faction_get_slot,":faction_slot_002",":faction_id_001",11),
    (try_begin),
        (ge,":faction_slot_002",0),
        (troop_get_slot,":troop_slot_003",":faction_slot_002",13),
        (assign,":var004","spr_banner_f21"),
        (val_add, ":var004", 1),
        (try_begin),
            (is_between,":troop_slot_003","spr_banner_a",":var004"),
            (assign,":troop_slot_003 -","spr_banner_a"),
            (store_add, ":var005", ":troop_slot_003", ":mesh.banner_a01"),
            (init_position,1),
            (position_set_y,1,100),
            (cur_tableau_add_mesh, ":var005", 1, 0, 0),
            (cur_tableau_set_camera_parameters, 0, 210, 210, 0, 100000),
        (try_end),
    (try_end),
(try_end),
]),

("2_factions_mesh", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200, [
(store_script_param, ":faction_id_001", 1),
(store_mod,":faction_id_002",":faction_id_001",128),
(val_div, ":faction_id_001", 128),
(assign,":faction_id_001 +","fac_player_supporters_faction"),
(assign,":faction_id_002 +","fac_player_supporters_faction"),
(set_fixed_point_multiplier, 100),
(try_begin),
    (eq,1,1),
    (faction_get_slot,":faction_slot_003",":faction_id_001",11),
    (try_begin),
        (ge,":faction_slot_003",0),
        (troop_get_slot,":troop_slot_004",":faction_slot_003",13),
        (assign,":var005","spr_banner_f21"),
        (val_add, ":var005", 1),
        (try_begin),
            (is_between,":troop_slot_004","spr_banner_a",":var005"),
            (assign,":troop_slot_004 -","spr_banner_a"),
            (store_add, ":var006", ":troop_slot_004", ":mesh.banner_a01"),
            (init_position,1),
            (position_set_x,1,-50),
            (position_set_y,1,100),
            (cur_tableau_add_mesh, ":var006", 1, 0, 0),
        (try_end),
    (try_end),
(try_end),
(try_begin),
    (eq,1,1),
    (faction_get_slot,":faction_slot_003",":faction_id_002",11),
    (try_begin),
        (ge,":faction_slot_003",0),
        (troop_get_slot,":troop_slot_004",":faction_slot_003",13),
        (assign,":var005","spr_banner_f21"),
        (val_add, ":var005", 1),
        (try_begin),
            (is_between,":troop_slot_004","spr_banner_a",":var005"),
            (assign,":troop_slot_004 -","spr_banner_a"),
            (store_add, ":var006", ":troop_slot_004", ":mesh.banner_a01"),
            (init_position,1),
            (position_set_x,1,50),
            (position_set_y,1,100),
            (cur_tableau_add_mesh, ":var006", 1, 0, 0),
        (try_end),
    (try_end),
(try_end),
(cur_tableau_set_camera_parameters, 0, 210, 210, 0, 100000),
]),

("color_picker", 0, "missiles", 32, 32, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(init_position,1),
(cur_tableau_add_mesh, "mesh_color_picker", 1, 0, 0),
(position_move_z,1,1),
(position_move_x,1,-2),
(position_move_y,1,-2),
(cur_tableau_add_mesh_with_vertex_color, "mesh_white_plane", 1, 200, 200, ":var001"),
(cur_tableau_set_camera_parameters, 0, 20, 20, 0, 100000),
]),

("custom_banner_square_no_mesh", 0, "missiles", 512, 512, 0, 0, 300, 300, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(call_script, "script_draw_banner_to_region", ":var001", 0, 0, 10000, 10000, 9800, 9800, 10000, 10000, 0),
(cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
]),

("custom_banner_default", 0, "missiles", 512, 256, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(call_script, "script_draw_banner_to_region", ":var001", -9, -2, 7450, 19400, 7200, 18000, 9000, 10000, 0),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_custom_banner", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 100, 200, 0, 100000),
]),

("custom_banner_tall", 0, "missiles", 512, 256, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(call_script, "script_draw_banner_to_region", ":var001", -9, 12, 8250, 18000, 8000, 21000, 10000, 10000, 0),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_custom_banner", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 100, 200, 0, 100000),
]),

("custom_banner_square", 0, "missiles", 256, 256, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(call_script, "script_draw_banner_to_region", ":var001", -11, 10, 7700, 7700, 7500, 7500, 8300, 10000, 0),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_custom_banner_square", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
]),

("custom_banner_short", 0, "missiles", 256, 512, 0, 0, 0, 0, [
(store_script_param, ":var001", 1),
(set_fixed_point_multiplier, 100),
(call_script, "script_draw_banner_to_region", ":var001", -10, 0, 8050, 5000, 4200, 4800, 6600, 10000, 0),
(init_position,1),
(position_set_z,1,10),
(cur_tableau_add_mesh, "mesh_tableau_mesh_custom_banner_short", 1, 0, 0),
(cur_tableau_set_camera_parameters, 0, 100, 50, 0, 100000),
]),

("background_selection", 0, "missiles", 512, 512, 0, 0, 100, 100, [
(store_script_param, ":var001", 1),
(troop_get_slot,":troop_slot_002","trp_player",91),
(troop_set_slot,"trp_player",91,":var001"),
(set_fixed_point_multiplier, 100),
(call_script, "script_draw_banner_to_region", "trp_player", 0, 0, 10000, 10000, 9800, 9800, 10000, 10000, 0),
(cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
(troop_set_slot,"trp_player",91,":troop_slot_002"),
]),

("positioning_selection", 0, "missiles", 512, 512, 0, 0, 100, 100, [
(store_script_param, ":var001", 1),
(troop_get_slot,":troop_slot_002","trp_player",98),
(troop_set_slot,"trp_player",98,":var001"),
(set_fixed_point_multiplier, 100),
(call_script, "script_draw_banner_to_region", "trp_player", 0, 0, 10000, 10000, 9800, 9800, 10000, 10000, 0),
(cur_tableau_set_camera_parameters, 0, 100, 100, 0, 100000),
(troop_set_slot,"trp_player",98,":troop_slot_002"),
]),

("retired_troop_alpha_mask", 0, "mat_troop_portrait_mask", 2048, 2048, 0, 0, 600, 600, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 8947848),
(cur_tableau_set_ambient_light, 10, 11, 15),
(cur_tableau_render_as_alpha_mask),
(call_script, "script_add_troop_to_cur_tableau_for_retirement", ":var001"),
]),

("retired_troop_color", 0, "mat_troop_portrait_color", 2048, 2048, 0, 0, 600, 600, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4293383065),
(cur_tableau_set_ambient_light, 10, 11, 15),
(call_script, "script_add_troop_to_cur_tableau_for_retirement", ":var001"),
]),

("retirement_troop", 0, "tableau_with_transparency", 2048, 2048, 0, 0, 600, 600, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 4287137928),
(cur_tableau_set_ambient_light, 10, 11, 15),
(set_fixed_point_multiplier, 100),
(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
(init_position,1),
(position_set_z,1,100),
(position_set_x,1,-20),
(position_set_y,1,-20),
(cur_tableau_add_tableau_mesh, "tab_retired_troop_color", ":var001", 1),
(position_set_z,1,200),
(cur_tableau_add_tableau_mesh, "tab_retired_troop_alpha_mask", ":var001", 1),
]),

("coop_companion_select_alpha_mask", 0, "mat_troop_portrait_mask", 1024, 1024, 0, 0, 600, 600, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 8947848),
(cur_tableau_set_ambient_light, 10, 11, 15),
(cur_tableau_render_as_alpha_mask),
(try_begin),
    (eq,":var001",-1),
    (call_script, "script_add_player_to_cur_tableau_for_coop", ":var001"),
(else_try),
    (call_script, "script_add_troop_to_cur_tableau_for_coop", ":var001"),
(try_end),
]),

("coop_companion_select_color", 0, "mat_troop_portrait_color", 1024, 1024, 0, 0, 600, 600, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 1140850688),
(cur_tableau_set_ambient_light, 10, 11, 15),
(try_begin),
    (eq,":var001",-1),
    (call_script, "script_add_player_to_cur_tableau_for_coop", ":var001"),
    (cur_tableau_set_background_color, 1140850688),
(else_try),
    (call_script, "script_add_troop_to_cur_tableau_for_coop", ":var001"),
    (cur_tableau_set_background_color, 1140850688),
(try_end),
]),

("coop_companion_select_0", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 300, 300, [
(store_script_param, ":var001", 1),
(cur_tableau_set_background_color, 8947848),
(cur_tableau_set_ambient_light, 10, 11, 15),
(set_fixed_point_multiplier, 100),
(cur_tableau_set_camera_parameters, 0, 40, 40, 0, 100000),
(init_position,1),
(position_set_z,1,100),
(position_set_x,1,-20),
(position_set_y,1,-20),
(cur_tableau_add_tableau_mesh, "tab_coop_companion_select_color", ":var001", 1),
(position_set_z,1,200),
(cur_tableau_add_tableau_mesh, "tab_coop_companion_select_alpha_mask", ":var001", 1),
]),


] # TABLEAU MATERIALS END
