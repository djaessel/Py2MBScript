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
[(0, mtef_team_1|mtef_defenders, af_override_all, 0, 1, []),
(1, mtef_team_0|mtef_attackers, af_override_all, 0, 1, []),
],
[
(ti_tab_pressed, 0, 0, [
], [
(set_trigger_result, 1),
]),

(ti_on_agent_knocked_down, 0, 0, [
], [
(display_message, "@One down!"),
]),

]),

] # MISSION TEMPLATES END
