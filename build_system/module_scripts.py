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
(call_script, "script_superMaths", 4, 26, 7),
]),

("game_get_use_string", [
(store_script_param, ":instance_id", 1),
(prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
(try_begin),
    (this_or_next|eq,":scene_prop_id","spr_winch_b"),
    (eq,":scene_prop_id","spr_winch"),
    (assign,":effected_object","spr_portcullis"),
(else_try),
    (this_or_next|eq,":scene_prop_id","spr_door_destructible"),
    (this_or_next|eq,":scene_prop_id","spr_castle_f_door_b"),
    (this_or_next|eq,":scene_prop_id","spr_castle_e_sally_door_a"),
    (this_or_next|eq,":scene_prop_id","spr_castle_f_sally_door_a"),
    (this_or_next|eq,":scene_prop_id","spr_earth_sally_gate_left"),
    (this_or_next|eq,":scene_prop_id","spr_earth_sally_gate_right"),
    (this_or_next|eq,":scene_prop_id","spr_viking_keep_destroy_sally_door_left"),
    (this_or_next|eq,":scene_prop_id","spr_viking_keep_destroy_sally_door_right"),
    (this_or_next|eq,":scene_prop_id","spr_castle_f_door_a"),
    (this_or_next|eq,":scene_prop_id","spr_siege_ladder_move_6m"),
    (this_or_next|eq,":scene_prop_id","spr_siege_ladder_move_8m"),
    (this_or_next|eq,":scene_prop_id","spr_siege_ladder_move_10m"),
    (this_or_next|eq,":scene_prop_id","spr_siege_ladder_move_12m"),
    (eq,":scene_prop_id","spr_siege_ladder_move_14m"),
    (assign,":effected_object",":scene_prop_id"),
(try_end),
(assign,":slotx",1),
(scene_prop_get_slot,":item_situation",":instance_id",":slotx"),
(try_begin),
    (eq,":effected_object","spr_portcullis"),
    (try_begin),
        (eq,":item_situation",0),
        (str_store_string,s0,"str_open_gate"),
    (else_try),
        (str_store_string,s0,"str_close_gate"),
    (try_end),
(else_try),
    (this_or_next|eq,":effected_object","spr_door_destructible"),
    (this_or_next|eq,":effected_object","spr_castle_f_door_b"),
    (this_or_next|eq,":effected_object","spr_castle_e_sally_door_a"),
    (this_or_next|eq,":effected_object","spr_castle_f_sally_door_a"),
    (this_or_next|eq,":effected_object","spr_earth_sally_gate_left"),
    (this_or_next|eq,":effected_object","spr_earth_sally_gate_right"),
    (this_or_next|eq,":effected_object","spr_viking_keep_destroy_sally_door_left"),
    (this_or_next|eq,":effected_object","spr_viking_keep_destroy_sally_door_right"),
    (eq,":effected_object","spr_castle_f_door_a"),
    (try_begin),
        (eq,":item_situation",0),
        (str_store_string,s0,"str_open_door"),
    (else_try),
        (str_store_string,s0,"str_close_door"),
    (try_end),
(else_try),
    (try_begin),
        (eq,":item_situation",0),
        (str_store_string,s0,"str_raise_ladder"),
    (else_try),
        (str_store_string,s0,"str_drop_ladder"),
    (try_end),
(try_end),
]),

("game_set_multiplayer_mission_end", [
(assign,"$g_multiplayer_mission_end_screen",1),
]),

("game_enable_cheat_menu", [
(store_script_param, ":input", 1),
(try_begin),
    (eq,":input",0),
    (assign,"$cheat_mode",0),
(else_try),
    (eq,":input",1),
    (assign,"$cheat_mode",1),
(try_end),
]),

("game_get_console_command", [
(store_script_param, ":input", 1),
(store_script_param, ":val1", 2),
(store_script_param, ":val2", 3),
(try_begin),
    (eq,":input",1),
    (assign,reg0,":val1"),
    (try_begin),
        (eq,":val1",1),
        (assign,reg1,"$g_multiplayer_num_bots_team_1"),
        (str_store_string,s0,"str_team_reg0_bot_count_is_reg1"),
    (else_try),
        (eq,":val1",2),
        (assign,reg1,"$g_multiplayer_num_bots_team_2"),
        (str_store_string,s0,"str_team_reg0_bot_count_is_reg1"),
    (else_try),
        (str_store_string,s0,"str_input_is_not_correct_for_the_command_type_help_for_more_information"),
    (try_end),
(else_try),
    (eq,":input",2),
    (assign,reg0,":val1"),
    (assign,reg1,":val2"),
    (try_begin),
        (eq,":val1",1),
        (ge,":val2",0),
        (assign,"$g_multiplayer_num_bots_team_1",":val2"),
        (str_store_string,s0,"str_team_reg0_bot_count_is_reg1"),
    (else_try),
        (eq,":val1",2),
        (ge,":val2",0),
        (assign,"$g_multiplayer_num_bots_team_2",":val2"),
        (str_store_string,s0,"str_team_reg0_bot_count_is_reg1"),
    (else_try),
        (str_store_string,s0,"str_input_is_not_correct_for_the_command_type_help_for_more_information"),
    (try_end),
(else_try),
    (eq,":input",3),
    (assign,reg0,"$g_multiplayer_round_max_seconds"),
    (str_store_string,s0,"str_maximum_seconds_for_round_is_reg0"),
(else_try),
    (eq,":input",4),
    (assign,reg0,":val1"),
    (assign,":mins",60),
    (assign,":maxs",901),
    (try_begin),
        (is_between,":val1",":mins",":maxs"),
        (assign,"$g_multiplayer_round_max_seconds",":val1"),
        (str_store_string,s0,"str_maximum_seconds_for_round_is_reg0"),
        (get_max_players, ":num_players"),
        (try_for_range, ":cur_player", 1, ":num_players"),
            (try_begin),
                (player_is_active, ":cur_player"),
                (assign,":retx",59),
                (multiplayer_send_int_to_player, ":cur_player", ":retx", ":val1"),
            (try_end),
        (try_end),
    (else_try),
        (str_store_string,s0,"str_input_is_not_correct_for_the_command_type_help_for_more_information"),
    (try_end),
(else_try),
    (eq,":input",5),
    (assign,reg0,"$g_multiplayer_respawn_period"),
    (str_store_string,s0,"str_respawn_period_is_reg0_seconds"),
(else_try),
    (str_store_string,s0,"@@{!}DEBUG : SYSTEM ERROR!"),
(try_end),
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

("game_event_simulate_battle", [
(store_script_param, ":root_defender_party", 1),
(store_script_param, ":root_attacker_party", 2),
(display_message, "@Battle simulation:"),
(assign, reg1, ":root_defender_party"),
(display_message, "@- Defender: {reg1}"),
(assign, reg1, ":root_attacker_party"),
(display_message, "@- Attacker: {reg1}"),
]),

("game_event_battle_end", [
(store_script_param, ":root_defender_party", 1),
(store_script_param, ":root_attacker_party", 2),
(display_message, "@Battle ended:"),
(assign, reg1, ":root_defender_party"),
(display_message, "@- Defender: {reg1}"),
(assign, reg1, ":root_attacker_party"),
(display_message, "@- Attacker: {reg1}"),
]),

("game_get_item_buy_price_factor", [
(store_script_param, ":item_kind_id", 1),
(assign,":price_factor",100),
(val_div, ":price_factor", 100),
(store_add, reg0, ":price_factor", ":item_kind_id"),
(set_trigger_result, reg0),
]),

("game_get_item_sell_price_factor", [
(store_script_param, ":item_kind_id", 1),
(assign,":price_factor",100),
(val_div, ":price_factor", 100),
(store_add, reg0, ":price_factor", ":item_kind_id"),
(set_trigger_result, reg0),
]),

("superMaths", [
(store_script_param, ":bul", 1),
(store_script_param, ":bal", 2),
(store_script_param, ":bil", 3),
(store_mul, ":var___x1", 3, 5),
(store_mul, ":var___x2", 2, 7),
(store_mul, ":var___x3", 5, 2),
(store_add, ":x", 1, ":var___x1"),
(val_add, ":x", ":var___x2"),
(val_add, ":x", ":var___x3"),
(assign, reg0, ":x"),
(display_message, "@{reg0}"),
(store_div, ":var___y1", ":x", 4),
(store_div, ":var___y2", 3, 3),
(store_mul, ":var___x1", ":var___y1", ":var___y2"),
(store_add, ":y", 1, 3),
(val_add, ":y", ":var___x1"),
(assign, reg0, ":y"),
(display_message, "@{reg0}"),
(store_add, ":var___z1", ":x", ":y"),
(store_mul, ":var___x1", ":var___z1", 4),
(store_add, ":z", 1, 3),
(val_add, ":z", ":var___x1"),
(assign, reg0, ":z"),
(display_message, "@{reg0}"),
(store_add, ":var___z1", 1, 3),
(store_add, ":var___z2", 4, 8),
(store_mul, ":var___x1", ":var___z1", ":var___z2"),
(assign,":z2",":var___x1"),
(assign, reg0, ":z2"),
(display_message, "@{reg0}"),
(store_sub, ":var___z1", 3, 1),
(store_sub, ":var___z2", 8, 4),
(store_mul, ":var___x1", ":var___z1", ":var___z2"),
(assign,":z3",":var___x1"),
(assign, reg0, ":z3"),
(display_message, "@{reg0}"),
(store_add, ":var___z1", ":x", ":y"),
(store_div, ":var___y1", ":z", ":var___z1"),
(store_mul, ":var___x1", ":var___y1", ":z2"),
(assign,":z4",":var___x1"),
(assign, reg0, ":z4"),
(display_message, "@{reg0}"),
(store_sub, ":var___a1", ":x", 4),
(val_sub, ":var___a1", 5),
(store_add, ":z5", ":var___a1", ":z3"),
(assign, reg0, ":z5"),
(display_message, "@{reg0}"),
(store_mul, ":var___x1", 3, 2),
(store_add, ":var___z1", 9, ":var___x1"),
(store_mul, ":var___z2", 5, 2),
(store_sub, ":var___z3", 3, 1),
(store_sub, ":var___a1", ":var___z1", ":var___z2"),
(store_add, ":x2", ":var___a1", ":var___z3"),
(assign, reg0, ":x2"),
(display_message, "@{reg0}"),
(store_mul, ":var___x1", 6, 2),
(store_add, ":var___z1", 9, ":var___x1"),
(store_div, ":var___x1", 8, 2),
(assign,":var___z2",":var___x1"),
(store_sub, ":var___z3", 3, 1),
(store_sub, ":y2", ":var___z1", ":var___z2"),
(val_sub, ":y2", ":var___z3"),
(assign, reg0, ":y2"),
(display_message, "@{reg0}"),
(store_mul, ":var___z1", ":bul", ":bal"),
(store_div, ":var___x1", ":var___z1", ":bil"),
(store_add, ":qq", ":var___x1", ":bil"),
(assign, reg0, ":qq"),
(display_message, "@{reg0}"),
]),

("use_item", [
(store_script_param, ":agent_id", 1),
(store_script_param, ":user_id", 2),
(assign, reg1, ":agent_id"),
(assign, reg2, ":user_id"),
(display_message, "@USE_ITEM: {reg1} {reg2}"),
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
    (store_mul, ":random_seed", ":troop_no", 126233),
    (val_mod, ":random_seed", 1000),
    (val_add, ":random_seed", 1),
    (cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
(try_end),
(cur_tableau_set_camera_position, pos5),
(copy_position,pos8,pos5),
(position_rotate_x,pos8,-90),
(position_rotate_z,pos8,30,0),
(position_rotate_x,pos8,-60),
(cur_tableau_add_sun_light, 0, pos8, 175, 150, 125),
]),

]
