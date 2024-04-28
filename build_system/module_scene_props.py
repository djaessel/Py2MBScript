# -*- coding: cp1252 -*-
from header_common import *
from header_scene_props import *
from header_operations import *
from header_triggers import *
from header_sounds import *
from module_constants import *
import string

scene_props = [

("invalid_object", 0, "question_mark", "0", []),
("inventory", sokf_type_container|sokf_place_at_origin, "package", "bobaggage", []),
("empty", 0, "0", "0", []),
("chest_a", sokf_type_container, "chest_gothic", "bochest_gothic", []),
("container_small_chest", sokf_type_container, "package", "bobaggage", []),
("container_chest_b", sokf_type_container, "chest_b", "bo_chest_b", []),
("container_chest_c", sokf_type_container, "chest_c", "bo_chest_c", []),
("player_chest", sokf_type_container, "player_chest", "bo_player_chest", []),
("locked_player_chest", 0, "player_chest", "bo_player_chest", []),
("light_sun", sokf_invisible, "light_sphere", "0", [
(ti_on_scene_prop_init, [
(try_begin),
    (neg|is_currently_night),
    (store_trigger_param_1,":prop_instance_no"),
    (set_fixed_point_multiplier, 100),
    (prop_instance_get_scale, pos5, ":prop_instance_no"),
    (position_get_scale_x,":scale",pos5),
    (store_time_of_day,reg12),
    (try_begin),
        (is_between,reg12,5,20),
        (store_mul, ":red", 1000, ":scale"),
        (store_mul, ":green", 965, ":scale"),
        (store_mul, ":blue", 900, ":scale"),
    (else_try),
        (store_mul, ":red", 450, ":scale"),
        (store_mul, ":green", 575, ":scale"),
        (store_mul, ":blue", 750, ":scale"),
    (try_end),
    (val_div, ":red", 100),
    (val_div, ":green", 100),
    (val_div, ":blue", 100),
    (set_current_color,":red",":red",":red"),
    (set_position_delta,0,0,0),
    (add_point_light_to_entity,0,0),
(try_end),
]),

]),
("winch", sokf_moveable, "winch", "bo_winch", []),
("winch_b", spr_use_time(5)|sokf_moveable, "winch_b", "bo_winch", [
(ti_on_scene_prop_use, [
(store_script_param, ":agent_id", 1),
(store_script_param, ":instance_id", 2),
(call_script, "script_use_item", ":instance_id", ":agent_id"),
(get_max_players, ":num_players"),
(try_for_range, ":player_no", 1, ":num_players"),
    (player_is_active, ":player_no"),
    (multiplayer_send_2_int_to_player, ":player_no", 76, ":instance_id", ":agent_id"), # mevent
(try_end),
]),

]),
("door_destructible", spr_use_time(2)|sokf_moveable|sokf_show_hit_point_bar|sokf_destructible, "tutorial_door_a", "bo_tutorial_door_a", [
(ti_on_scene_prop_use, [
(store_script_param, ":agent_id", 1),
(store_script_param, ":instance_id", 2),
(call_script, "script_use_item", ":instance_id", ":agent_id"),
(get_max_players, ":num_players"),
(try_for_range, ":player_no", 1, ":num_players"),
    (player_is_active, ":player_no"),
    (multiplayer_send_2_int_to_player, ":player_no", 76, ":instance_id", ":agent_id"), # mevent
(try_end),
]),

(ti_on_scene_prop_init, [
(store_script_param, ":instance_no", 1),
(scene_prop_set_hit_points, ":instance_no", 2000),
]),

(ti_on_scene_prop_destroy, [
(store_script_param, ":instance_no", 1),
(store_script_param, ":attacker_agent_no", 2),
(play_sound,"snd_dummy_destroyed"),
(assign,":rotate_side",86),
(try_begin),
    (this_or_next|multiplayer_is_server),
    (neg|game_in_multiplayer_mode),
    (set_fixed_point_multiplier, 100),
    (prop_instance_get_position, pos1, ":instance_no"),
    (try_begin),
        (ge,":attacker_agent_no",0),
        (agent_get_position,pos2,":attacker_agent_no"),
        (try_begin),
            (position_is_behind_position,pos2,pos1),
            (val_mul, ":rotate_side", -1),
        (try_end),
    (try_end),
    (init_position,pos3),
    (try_begin),
        (ge,":rotate_side",0),
        (position_move_y,pos3,-100),
    (else_try),
        (position_move_y,pos3,100),
    (try_end),
    (position_move_x,pos3,-50),
    (position_transform_position_to_parent,pos4,pos1,pos3),
    (position_move_z,pos4,100),
    (position_get_distance_to_ground_level, ":height_to_terrain", pos4),
    (val_sub, ":height_to_terrain", 100),
    (assign,":z_difference",":height_to_terrain"),
    (val_div, ":z_difference", 3),
    (try_begin),
        (ge,":rotate_side",0),
        (val_add, ":rotate_side", ":z_difference"),
    (else_try),
        (val_sub, ":rotate_side", ":z_difference"),
    (try_end),
    (position_rotate_x,pos1,":rotate_side"),
    (prop_instance_animate_to_position, ":instance_no", pos1, 70),
(try_end),
]),

(ti_on_scene_prop_hit, [
(play_sound,"snd_dummy_hit"),
(particle_system_burst,"psys_dummy_smoke",pos1,3),
(particle_system_burst,"psys_dummy_straw",pos1,10),
]),

]),
("portcullis", 0, "0", "0", []),
("castle_e_sally_door_a", 0, "0", "0", []),
("castle_f_sally_door_a", 0, "0", "0", []),
("earth_sally_gate_left", 0, "0", "0", []),
("earth_sally_gate_right", 0, "0", "0", []),
("viking_keep_destroy_sally_door_left", 0, "0", "0", []),
("viking_keep_destroy_sally_door_right", 0, "0", "0", []),
("castle_f_door_a", 0, "0", "0", []),
("siege_ladder_move_6m", 0, "0", "0", []),
("siege_ladder_move_8m", 0, "0", "0", []),
("siege_ladder_move_10m", 0, "0", "0", []),
("siege_ladder_move_12m", 0, "0", "0", []),
("siege_ladder_move_14m", 0, "0", "0", []),
("castle_f_door_b", sokf_moveable|sokf_show_hit_point_bar|sokf_destructible, "castle_e_sally_door_a", "bo_castle_e_sally_door_a", [
(ti_on_scene_prop_use, [
(store_script_param, ":agent_id", 1),
(store_script_param, ":instance_id", 2),
(agent_get_position,pos1,":agent_id"),
(prop_instance_get_starting_position, pos2, ":instance_id"),
(scene_prop_get_slot,":opened_or_closed",":instance_id",1), # slot_openclose
(try_begin),
    (ge,":agent_id",0),
    (agent_get_team, ":agent_team", ":agent_id"),
    (try_begin),
        (this_or_next|eq,":agent_team",0),
        (eq,":opened_or_closed",1),
        (call_script, "script_use_item", ":instance_id", ":agent_id"),
        (get_max_players, ":num_players"),
        (try_for_range, ":player_no", 1, ":num_players"),
            (player_is_active, ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", 76, ":instance_id", ":agent_id"), # mevent
        (try_end),
    (try_end),
(try_end),
]),

(ti_on_scene_prop_init, [
(store_script_param, ":instance_no", 1),
(scene_prop_set_hit_points, ":instance_no", 1000),
]),

]),

] # SCENE PROPS END
