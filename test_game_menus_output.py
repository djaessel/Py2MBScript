from header_operations import *
from header_common import *

game_menus = [

("start_game_0", 0, 
  "Welcome adventurer, hopefully you will enjoy this new adventure through another world.", 
  "none", [
],
[
("continue", [
], "Continue...", [
(assign,reg12,255),
(assign,reg13,500),
(str_store_string,s0,"@Current gold: {reg13}"),
(str_store_string,s1,"@Current xp: {reg12}"),
(str_store_string,s2,"str_yes"),
(jump_to_menu,"mnu_start_game_1"),
]),

("go_back", [
], "Go back...", [
(try_begin),
    (is_edit_mode_enabled),
(else_try),
    (change_screen_quit),
(try_end),
]),

]),
]
