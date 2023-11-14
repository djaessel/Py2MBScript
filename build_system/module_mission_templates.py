from header_operations import *
from header_common import *

mission_templates = [

("my_mission", mtf_battle_mode, -1,
"My super mission!",
[(0, mtef_team_0|mtef_defenders, 0, 0, [itm_my_axe,itm_master_shield,]),
(1, mtef_team_1|mtef_attackers, 0, 0, [itm_my_axe,]),
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

]),

] # MISSION TEMPLATES END