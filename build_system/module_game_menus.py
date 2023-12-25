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

]),
]
