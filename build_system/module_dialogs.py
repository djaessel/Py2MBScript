# -*- coding: cp1254 -*-
from header_common import *
from header_dialogs import *
from header_operations import *
from header_parties import *
from header_item_modifiers import *
from header_skills import *
from header_triggers import *
from ID_troops import *
from ID_party_templates import *

from module_constants import *

dialogs = [

[anyone, "lord_pretalk", [], "Anything else?", "lord_talk", []],
[anyone, "lord_talk", [
(eq,"$g_talk_troop_faction","fac_player_supporters_faction"),
], "I want to give some troops to you.", "lord_give_troops", []],
] # DIALOGS END
