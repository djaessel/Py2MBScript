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

["no_item","INVALID ITEM",[("invalid_item",0x0)],
itp_type_one_handed_wpn|itp_primary|itp_secondary,
itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_force_64_bits,
3,
weight(1.5),
imodbits_none],
["club","Club",[("club",0x0)],
itp_type_one_handed_wpn|itp_merchandise|itp_wooden_attack|itp_wooden_parry|itp_primary|itp_can_knock_down,
itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_force_64_bits,
11,
weight(2.5)|spd_rtng(98)|weapon_length(70)|swing_damage(20, blunt),
imodbits_none],
["military_hammer","Military Hammer",[("military_hammer",0x0)],
itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary,
itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_carry_mace_left_hip|itcf_force_64_bits,
317,
weight(2)|spd_rtng(95)|weapon_length(70)|swing_damage(31, blunt),
imodbits_none],
["tools","Tools",[("iron_hammer",0x0),("iron_hammer_new",0x1000000000000000)],
itp_type_goods|itp_merchandise,
0,
410,
weight(50)|abundance(90),
imodbits_none],
["items_end","Items End",[("invalid_item",0x0)],
0,
0,
0,
0,
imodbits_none],

] # ITEMS END
