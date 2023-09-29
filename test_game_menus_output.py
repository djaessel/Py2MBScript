from header_operations import *
from header_common import *

game_menus = [

("start_game_0", 0, 
  "Welcome adventurer, hopefully you will enjoy this new adventure through another world.", 
  "none", [
(try_end),
],
[
("continue", [
(try_end),
], "Continue...", [
(jump_to_menu,"mnu_start_game_1"),
(try_end),
]),

("go_back", [
(try_end),
], "Go back...", [
(jump_to_menu,"mnu_start_game_1"),
(try_end),
]),

]),
]
