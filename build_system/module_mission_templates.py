from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *

mission_templates = [

("village_training", mtf_arena_fight, -1,
"village_training",
[(2, mtef_team_0|mtef_visitor_source, af_override_everything, 0, 1, []),
(4, mtef_team_1|mtef_visitor_source, af_override_everything, 0, 1, []),
],
[
(ti_before_mission_start, 0, 0, [
], [
]),

(ti_tab_pressed, 0, 0, [
], [
(question_box,"str_give_up_fight"),
]),

(ti_question_answered, 0, 0, [
], [
(store_trigger_param_1,":answer"),
(try_begin),
    (eq,":answer",0),
    (finish_mission, 0),
(try_end),
]),

(ti_inventory_key_pressed, 0, 0, [
], [
(display_message, "str_cant_use_inventory_now"),
]),

(1, 4, ti_once, [
(this_or_next|main_hero_fallen),
(num_active_teams_le,1),
], [
(try_begin),
    (neg|main_hero_fallen),
(try_end),
(finish_mission, 0),
]),

]),

] # MISSION TEMPLATES END
