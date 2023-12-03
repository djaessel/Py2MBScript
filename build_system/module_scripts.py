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

("game_get_use_string", [
(store_script_param, ":instance_id", 1),
(prop_instance_get_scene_prop_type, ":scene_prop_id", ":instance_id"),
(try_begin),
    (this_or_next|eq,":scene_prop_id","spr_winch_b"),
    (eq,":scene_prop_id","spr_winch"),
    (assign,":effected_object","spr_portcullis"),
(else_try),
    (this_or_next|eq,":scene_prop_id","spr_door_destructible"),
    (this_or_next|eq,":scene_prop_id","spr_castle_f_door_b"),
    (eq,":scene_prop_id","spr_siege_ladder_move_14m"),
    (assign,":effected_object",":scene_prop_id"),
(try_end),
(assign, reg1, ":effected_object"),
(display_message, "@Effected object: {reg1}"),
]),

("script1", [
(store_script_param, ":waterLevel", 1),
(store_script_param, ":fishCount", 2),
(get_operation_set_version, ":versionx"),
(try_begin),
    (gt,":versionx",0),
    (le,":versionx",1101),
    (profile_get_banner_id, ":banner_id"),
    (try_begin),
        (this_or_next|gt,":banner_id",20),
        (this_or_next|eq,":banner_id",0),
        (eq,":banner_id",10),
        (assign, reg0, ":versionx"),
        (display_message, "@{reg0}"),
        (try_begin),
            (eq,":versionx",1011),
            (display_message, "@YES!"),
        (else_try),
            (display_message, "@Nope"),
        (try_end),
    (try_end),
(try_end),
(try_begin),
    (eq,":fishCount",1),
    (is_edit_mode_enabled),
    (display_message, "@Test1"),
(else_try),
    (this_or_next|is_edit_mode_enabled),
    (gt,":versionx",1011),
    (display_message, "@Test4"),
(try_end),
(try_begin),
    (this_or_next|eq,":waterLevel",2),
    (eq,":fishCount",1),
    (display_message, "@TEST2"),
(else_try),
    (display_message, "@TEST3"),
    (display_message, "@Hello World!"),
(try_end),
]),

("helloWorld", [
(options_get_campaign_ai, ":ai_strength"),
(try_begin),
    (is_edit_mode_enabled),
    (display_message, "@Hello World!"),
(try_end),
(val_mul, ":ai_strength", 5),
(assign,":sun",10),
(store_add, ":water", ":sun", 2),
(val_div, ":ai_strength", ":water"),
(options_set_damage_to_friends, ":ai_strength"),
(store_div, ":sun", ":sun", 2),
(str_store_string,s0,"@LOL"),
(try_begin),
    (is_edit_mode_enabled),
    (assign, reg1, ":ai_strength"),
    (assign, reg3, ":water"),
    (display_message, "@Strength: {reg1} Water: {reg3} {s0}"),
(else_try),
    (call_script, "script_script1", ":water", ":ai_strength"),
(try_end),
]),

("loopy", [
(try_for_range, ":i", 2, 10),
    (assign, reg0, ":i"),
    (display_message, "@{reg0}"),
(try_end),
(try_for_range, ":i", 0, 5),
    (options_get_campaign_ai, ":ai_strength"),
    (try_begin),
        (eq,":ai_strength",1),
        (display_message, "@YES!"),
    (try_end),
(try_end),
(try_for_range_backwards, ":x", 0, 200),
    (assign,reg0,":x"),
    (display_message, "@Backwards: {reg0}"),
(try_end),
]),

("whoIsMyPlayerTeam", [
(store_script_param, ":playerId", 1),
(player_get_team_no, ":team_no", ":playerId"),
(assign,reg0,":team_no"),
(display_message, "@{reg0}"),
]),

("itemx", [
(store_script_param, ":playerId", 1),
(store_script_param, ":item", 2),
(player_add_spawn_item, ":playerId", 0, ":item"),
(player_get_team_no, ":teamNo", ":playerId"),
(multiplayer_find_spawn_point, ":entry_point", ":teamNo", 1, 0),
(display_message, "@Spawn point"),
(assign, reg0, ":entry_point"),
(display_message, "@{reg0}"),
]),

("setNewTeam", [
(store_script_param, ":playerId", 1),
(store_script_param, ":teamNo", 2),
(player_set_team_no, ":playerId", ":teamNo"),
(assign,reg0,":playerId"),
(assign,reg1,":teamNo"),
(display_message, "@{reg0} has team {reg1}"),
]),

("changeFactionIfActive", [
(store_script_param, ":partyId", 1),
(store_script_param, ":newFactionNo", 2),
(try_begin),
    (party_is_active,":partyId"),
    (party_set_faction,":partyId",":newFactionNo"),
    (party_add_members,":partyId","trp_looter",15),
(else_try),
    (assign, reg1, ":partyId"),
    (display_message, "@Party {reg1} is inactive"),
(try_end),
]),

("tryAgain", [
(store_script_param, ":randomVal", 1),
(try_begin),
    (is_edit_mode_enabled),
    (assign,":waterLevel",5),
    (try_begin),
        (neg|eq,":randomVal",3),
        (val_sub, ":waterLevel", 2),
    (else_try),
        (val_add, ":waterLevel", 1),
        (assign, reg0, ":waterLevel"),
        (display_message, "@{reg0}"),
    (try_end),
(else_try),
    (display_message, "@There was an error!"),
(try_end),
]),

("well", [
(store_script_param, ":water", 1),
(try_begin),
    (gt,":water",10),
    (display_message, "@Well... well!"),
(else_try),
    (gt,":water",3),
    (display_message, "@Well!"),
(else_try),
    (display_message, "@Well..."),
(try_end),
]),

("prepareItem", [
(store_script_param, ":item_id", 1),
(item_get_difficulty, ":diffy", ":item_id"),
(try_begin),
    (lt,":diffy",10),
    (item_get_body_armor, ":armor", ":item_id"),
    (assign, reg0, ":armor"),
    (display_message, "@{reg0} armor!"),
(else_try),
    (assign, reg0, ":diffy"),
    (display_message, "@{reg0}  too high!"),
(try_end),
]),

]
