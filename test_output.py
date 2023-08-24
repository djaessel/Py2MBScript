from header_operations import *
from header_common import *

scripts = [

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
(try_end),
(display_message, "@Hello World!"),
]),

("helloWorld", [
(options_get_campaign_ai, ":ai_strength"),
(display_message, "@Hello World!"),
(assign, reg0, ":ai_strength"),
(display_message, "@{reg0}"),
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

]
