from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag
imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
items = [

["my_axe","My Axe",[("battle_ax",0)],
itp_type_one_handed_wpn|itp_crush_through|itp_force_attach_right_hand,
itcf_horseback_overswing_left_onehanded|itcf_horseback_overswing_right_onehanded|itcf_horseback_thrust_onehanded|itcf_overswing_onehanded|itcf_thrust_onehanded|itcf_parry_up_onehanded|itcf_parry_forward_onehanded|itcf_parry_left_onehanded|itcf_parry_right_onehanded|itcf_carry_axe_left_hip,
315,
weight(2.5)|weapon_length(72)|abundance(100)|swing_damage(27, pierce),
imodbits_axe|imodbit_champion],
["siege_supply","Siege Supply",[],
0,
0,
0,
0,
imodbits_none],
["master_shield","Master Shield",[("arena_shield_green",0)],
itp_type_shield|itp_unique,
0,
831,
weight(5)|body_armor(10)|difficulty(10)|hit_points(399)|shield_width(75)|shield_height(200)|abundance(9),
imodbits_shield],

] # ITEMS END
