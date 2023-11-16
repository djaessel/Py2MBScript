from __future__ import division
from past.utils import old_div
import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

troops = [

["npc1","Peter","Peter",
tf_male|tf_hero|tf_unkillable|tf_guarantee_all,
no_scene,reserved,fac_player_faction,
[(itm_my_axe, 0),],
str_10|agi_5|int_4|cha_4|level(7),wp(30)|wp_firearm(50),
knowns_riding_1|knowns_inventory_management_2|knowns_prisoner_management_1|knowns_leadership_1|knowns_trade_10,
man_face_middle_1,man_face_middle_1],

["npc2","Sarah","Sarah",
tf_female|tf_hero|tf_guarantee_all,
no_scene,reserved,fac_player_faction,
[(itm_master_shield, imodbit_champion|imodbits_good),],
str_7|agi_5|int_4|cha_4|level(3),wpe(30,52,55,100),
knows_common,
man_face_middle_1,man_face_middle_1],

] # TROOPS END
