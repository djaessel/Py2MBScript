from header_operations import *
from header_common import *

triggers = [

[anyone, "lord_pretalk", [], "Anything else?", "lord_talk", []],
[anyone, "lord_talk", [
(eq,"$g_talk_troop_faction","fac_player_supporters_faction"),
], "I want to give some troops to you.", "lord_give_troops", []],
] # DIALOGS END
