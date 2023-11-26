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
(assign,reg12,255),
(assign,reg13,500),
(str_store_string,s0,"@Current gold: {reg13}"),
(str_store_string,s1,"@Current xp: {reg12}"),
(str_store_string,s2,"str_yes"),
(display_message, "@{s0} {s1} {s2}"),
(call_script, "script_helloWorld"),
(change_screen_return),
(set_show_messages,1),
]),

("go_back", [
], "Go back...", [
(try_begin),
    (is_edit_mode_enabled),
(else_try),
    (change_screen_quit),
(try_end),
]),

("hack", [
(is_edit_mode_enabled),
], "I hacked it!", [
(display_message, "@LOL"),
]),

]),
]
