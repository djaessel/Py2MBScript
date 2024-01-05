from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *

mission_templates = [

("my_mission", mtf_battle_mode, -1,
"My super mission!",
[(0, mtef_team_0|mtef_defenders, af_override_all, 0, 1, [itm_my_axe,itm_master_shield,]),
(1, mtef_team_1|mtef_attackers, af_override_all, 0, 4, [itm_my_axe,itm_master_shield,]),
],
[
(ti_after_mission_start, 0, 0, [
(this_or_next|eq,reg1,0),
(eq,reg1,2),
(try_begin),
    (eq,reg0,0),
    (display_message, "@EXTRA SAFE!"),
(try_end),
], [
(assign,reg0,30),
(display_message, "@{reg0}"),
]),

(ti_tab_pressed, 0, 0, [
], [
(set_trigger_result, 1),
]),

]),

] # MISSION TEMPLATES END
