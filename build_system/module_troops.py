from __future__ import division
from past.utils import old_div
import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from module_items import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

def wp(x):
  n = 0
  r = 10 + int(old_div(x, 10))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wp_melee(x):
  n = 0
  r = 10 + int(old_div(x, 10))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
knows_common_multiplayer = knows_trade_10|knows_inventory_management_10|knows_prisoner_management_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10
def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = int_30 | cha_30

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

reserved = 0
no_scene = 0

man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000

troops = [

["player","Player","Player",
tf_hero|tf_unmoveable_in_party_window,
no_scene,reserved,fac_player_faction,
[],
str_4|agi_4|int_4|cha_4|level(1),wp(15),
knows_common,
0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000,],

["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female",
tf_hero|tf_female|tf_guarantee_all,
no_scene,reserved,fac_commoners,
[],
str_7|agi_5|int_4|cha_4|level(1),wp(15),
knows_common,
0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000,],

["temp_troop","Temp Troop","Temp Troop",
tf_hero,
no_scene,reserved,fac_commoners,
[],
str_7|agi_5|int_4|cha_4|level(1),wp(0),
knows_common|knows_inventory_management_10,
0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000,],

["npc1","Peter","Peter",
tf_male|tf_hero|tf_unkillable|tf_guarantee_all,
no_scene,reserved,fac_player_faction,
[(itm_my_axe, 0),],
str_10|agi_5|int_4|cha_4|level(7),wp(30)|wp_firearm(50),
knows_common|knows_trade_10,
man_face_middle_1,man_face_middle_1],

["npc2","Sarah","Sarah",
tf_female|tf_hero|tf_guarantee_all,
no_scene,reserved,fac_player_faction,
[(itm_master_shield, imodbit_champion|imodbits_good),],
str_7|agi_5|int_4|cha_4|level(3),wpe(30,52,55,100),
knows_common,
man_face_middle_1,man_face_middle_1],

["looter","Looter","Looter",
0,
no_scene,reserved,fac_commoners,
[],
str_7|agi_5|int_4|cha_4|level(1),wp(0),
knows_common,
man_face_middle_1,man_face_middle_1],

] # TROOPS END
