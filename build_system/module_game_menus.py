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
(change_screen_return),
(set_show_messages,1),
]),

("go_back", [
], "Go back...", [
(change_screen_quit),
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
], "TEST_POSITION", [
(try_for_parties, ":partyx"),
    (try_begin),
        (party_is_active,":partyx"),
        (party_get_template_id,":template_idx",":partyx"),
        (try_begin),
            (eq,":template_idx","pt_hunters"),
            (party_get_position,pos1,":partyx"),
            (position_get_x,":x",pos1),
            (val_add,":x",100),
            (position_set_x,pos1,":x"),
            (party_set_position,":partyx",pos1),
            (position_get_x, reg69, pos1),
            (position_get_y, reg70, pos1),
            (position_get_z, reg71, pos1),
            (display_message, "@DEBUG: Pos1 :[{reg69}, {reg70}, {reg71}]"),
        (try_end),
    (try_end),
(try_end),
]),

]),
]
