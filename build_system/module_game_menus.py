from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *

game_menus = [

("start_game_0", 0, 
  "Welcome adventurer, hopefully you will enjoy this new adventure through another world.", 
  "none", [
],
[
("continue", [
], "Continue...", [
(set_show_messages,1),
(jump_to_menu,"mnu_start_game_1"),
]),

("go_back", [
], "Go back...", [
(change_screen_quit),
]),

]),
("welcome_menu", 0, 
  "Welcome on the map!", 
  "none", [
],
[
("continue", [
], "Continue...", [
(change_screen_return),
]),

]),
("start_game_1", 0, 
  "Select your skin.", 
  "none", [
],
[
("start_male", [
], "Skin1 | Male", [
(troop_set_type,"trp_player",0),
(change_screen_return),
]),

("start_female", [
], "Skin2 | Female", [
(troop_set_type,"trp_player",1),
(change_screen_return),
]),

]),
("reports", 0, 
  "Reports test {reg1}", 
  "none", [
(assign,reg1,123456),
],
[
("continue", [
], "Continue...", [
(change_screen_return),
]),

]),
("town", 0, 
  "Test Town", 
  "none", [
],
[
("town_leave", [
], "Leave...", [
(change_screen_return),
]),

("test_position", [
], "TEST POSITION", [
(try_for_parties, ":partyx"),
    (try_begin),
        (party_is_active,":partyx"),
        (try_begin),
            (eq,1,1),
            (party_get_position,pos1,":partyx"),
            (position_get_x,":x",pos1),
            (val_add, ":x", 100),
            (position_set_x,pos1,":x"),
            (party_set_position,":partyx",pos1),
            (position_get_x, reg69, pos1),
            (position_get_y, reg70, pos1),
            (position_get_z, reg71, pos1),
            (display_message, "@DEBUG - Pos1 :[{reg69}, {reg70}, {reg71}]"),
        (try_end),
    (try_end),
(try_end),
]),

("test_break", [
], "TEST BREAK", [
(assign,":start",200),
(assign,":end",100),
(try_for_range_backwards, ":x", ":end", ":start"),
    (assign, reg0, ":x"),
    (display_message, "@{reg0}"),
    (try_begin),
        (eq,":x",150),
        (assign, ":end", ":start"),
    (try_end),
(try_end),
(assign,":end",30),
(try_for_range, ":x", 0, ":end"),
    (assign, reg0, ":x"),
    (display_message, "@{reg0}"),
    (try_begin),
        (eq,":x",10),
        (assign, ":end", 0),
    (try_end),
(try_end),
(assign, ":__break__", 0),
(try_for_parties, ":p"),
    (eq, ":__break__", 0),
    (assign, reg1, ":p"),
    (display_message, "@Party: {reg1}"),
    (try_begin),
        (eq,":p","p_test_town"),
        (assign, ":__break__", 1),
    (try_end),
(try_end),
]),

("test_break", [
], "TEST LIST", [
(assign,":x",8),
(try_begin),
    (this_or_next|eq,":x",0),
    (this_or_next|eq,":x",1),
    (this_or_next|eq,":x",2),
    (this_or_next|eq,":x",4),
    (this_or_next|eq,":x",8),
    (this_or_next|eq,":x",16),
    (this_or_next|eq,":x",32),
    (this_or_next|eq,":x",64),
    (eq,":x",128),
    (assign, reg0, ":x"),
    (display_message, "@{reg0} is in the list!"),
(try_end),
]),

]),
]
