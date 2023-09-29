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
(assign,s0,"Current gold: {reg13}"),
(assign,s1,"Current xp: {reg12}"),
(jump_to_menu,"mnu_start_game_1"),
]),

("go_back", [
], "Go back...", [
(change_screen_quit),
]),

]),
]
