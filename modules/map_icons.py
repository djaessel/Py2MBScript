# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from mapicon import MapIcon
import sounds as snd
from simple_trigger import SimpleTrigger
import header_triggers as tri


__banner_scale__ = 0.3
__avatar_scale__ = 0.15


player = MapIcon("player", mesh_name="player", scale=0.15, sound=snd.footstep_grass, offset_x=0.15, offset_y=0.173, offset_z=0.0)

player_horseman = MapIcon("player_horseman", mesh_name="player_horseman", scale=0.15, sound=snd.gallop, offset_x=0.15, offset_y=0.173, offset_z=0.0)

gray_knight = MapIcon("gray_knight", mesh_name="knight_a", scale=0.15, sound=snd.gallop, offset_x=0.15, offset_y=0.173, offset_z=0.0)

vaegir_knight = MapIcon("vaegir_knight", mesh_name="knight_b", scale=0.15, sound=snd.gallop, offset_x=0.15, offset_y=0.173, offset_z=0.0)

flagbearer_a = MapIcon("flagbearer_a", mesh_name="flagbearer_a", scale=0.15, sound=snd.gallop, offset_x=0.15, offset_y=0.173, offset_z=0.0)

flagbearer_b = MapIcon("flagbearer_b", mesh_name="flagbearer_b", scale=0.15, sound=snd.gallop, offset_x=0.15, offset_y=0.173, offset_z=0.0)

peasant = MapIcon("peasant", mesh_name="peasant_a", scale=0.15, sound=snd.footstep_grass, offset_x=0.15, offset_y=0.173, offset_z=0.0)

khergit = MapIcon("khergit", mesh_name="khergit_horseman", scale=0.15, sound=snd.gallop, offset_x=0.15, offset_y=0.173, offset_z=0.0)

khergit_horseman_b = MapIcon("khergit_horseman_b", mesh_name="khergit_horseman_b", scale=0.15, sound=snd.gallop, offset_x=0.15, offset_y=0.173, offset_z=0.0)

axeman = MapIcon("axeman", mesh_name="bandit_a", scale=0.15, sound=snd.footstep_grass, offset_x=0.15, offset_y=0.173, offset_z=0.0)

woman = MapIcon("woman", mesh_name="woman_a", scale=0.15, sound=snd.footstep_grass, offset_x=0.15, offset_y=0.173, offset_z=0.0)

woman_b = MapIcon("woman_b", mesh_name="woman_b", scale=0.15, sound=snd.footstep_grass, offset_x=0.15, offset_y=0.173, offset_z=0.0)

town = MapIcon("town", mesh_name="map_town_a", scale=0.35, no_shadow=True)

town_steppe = MapIcon("town_steppe", mesh_name="map_town_steppe_a", scale=0.35, no_shadow=True)

town_desert = MapIcon("town_desert", mesh_name="map_town_desert_a", scale=0.35, no_shadow=True)

village_a = MapIcon("village_a", mesh_name="map_village_a", scale=0.45, no_shadow=True)

village_b = MapIcon("village_b", mesh_name="map_village_b", scale=0.45, no_shadow=True)

village_c = MapIcon("village_c", mesh_name="map_village_c", scale=0.45, no_shadow=True)

village_burnt_a = MapIcon("village_burnt_a", mesh_name="map_village_burnt_a", scale=0.45, no_shadow=True)

village_deserted_a = MapIcon("village_deserted_a", mesh_name="map_village_deserted_a", scale=0.45, no_shadow=True)

village_burnt_b = MapIcon("village_burnt_b", mesh_name="map_village_burnt_b", scale=0.45, no_shadow=True)

village_deserted_b = MapIcon("village_deserted_b", mesh_name="map_village_deserted_b", scale=0.45, no_shadow=True)

village_burnt_c = MapIcon("village_burnt_c", mesh_name="map_village_burnt_c", scale=0.45, no_shadow=True)

village_deserted_c = MapIcon("village_deserted_c", mesh_name="map_village_deserted_c", scale=0.45, no_shadow=True)

village_snow_a = MapIcon("village_snow_a", mesh_name="map_village_snow_a", scale=0.45, no_shadow=True)

village_snow_burnt_a = MapIcon("village_snow_burnt_a", mesh_name="map_village_snow_burnt_a", scale=0.45, no_shadow=True)

village_snow_deserted_a = MapIcon("village_snow_deserted_a", mesh_name="map_village_snow_deserted_a", scale=0.45, no_shadow=True)

camp = MapIcon("camp", mesh_name="camp_tent", scale=0.13, no_shadow=True)

ship = MapIcon("ship", mesh_name="boat_sail_on", scale=0.23, no_shadow=True, sound=snd.footstep_grass, offset_x=0.0, offset_y=0.05, offset_z=0.0)

ship_on_land = MapIcon("ship_on_land", mesh_name="boat_sail_off", scale=0.23, no_shadow=True)

castle_a = MapIcon("castle_a", mesh_name="map_castle_a", scale=0.35, no_shadow=True)

castle_b = MapIcon("castle_b", mesh_name="map_castle_b", scale=0.35, no_shadow=True)

castle_c = MapIcon("castle_c", mesh_name="map_castle_c", scale=0.35, no_shadow=True)

castle_d = MapIcon("castle_d", mesh_name="map_castle_d", scale=0.35, no_shadow=True)

town_snow = MapIcon("town_snow", mesh_name="map_town_snow_a", scale=0.35, no_shadow=True)

castle_snow_a = MapIcon("castle_snow_a", mesh_name="map_castle_snow_a", scale=0.35, no_shadow=True)

castle_snow_b = MapIcon("castle_snow_b", mesh_name="map_castle_snow_b", scale=0.35, no_shadow=True)

mule = MapIcon("mule", mesh_name="icon_mule", scale=0.2, sound=snd.footstep_grass, offset_x=0.15, offset_y=0.173, offset_z=0.0)

cattle = MapIcon("cattle", mesh_name="icon_cow", scale=0.2, sound=snd.footstep_grass, offset_x=0.15, offset_y=0.173, offset_z=0.0)

training_ground = MapIcon("training_ground", mesh_name="training", scale=0.35, no_shadow=True)

bridge_a = MapIcon("bridge_a", mesh_name="map_river_bridge_a", scale=1.27, no_shadow=True)

bridge_b = MapIcon("bridge_b", mesh_name="map_river_bridge_b", scale=0.7, no_shadow=True)

bridge_snow_a = MapIcon("bridge_snow_a", mesh_name="map_river_bridge_snow_a", scale=1.27, no_shadow=True)

custom_banner_01 = MapIcon("custom_banner_01", mesh_name="custom_map_banner_01", scale=0.3)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_init_map_icon)
#def code(party_id_001):
#    party_slot_002 = party_get_slot(party_id_001,7)
#    if party_slot_002 >= 0:
#        cur_map_icon_set_tableau_material(tab.custom_banner_square,party_slot_002)
#    #end
#trigger0.codeBlock = code
custom_banner_01.add_trigger(trigger0)


custom_banner_02 = MapIcon("custom_banner_02", mesh_name="custom_map_banner_02", scale=0.3)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_init_map_icon)
#def code(party_id_001):
#    party_slot_002 = party_get_slot(party_id_001,7)
#    if party_slot_002 >= 0:
#        cur_map_icon_set_tableau_material(tab.custom_banner_short,party_slot_002)
#    #end
#trigger0.codeBlock = code
custom_banner_02.add_trigger(trigger0)


custom_banner_03 = MapIcon("custom_banner_03", mesh_name="custom_map_banner_03", scale=0.3)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_init_map_icon)
#def code(party_id_001):
#    party_slot_002 = party_get_slot(party_id_001,7)
#    if party_slot_002 >= 0:
#        cur_map_icon_set_tableau_material(tab.custom_banner_tall,party_slot_002)
#    #end
#trigger0.codeBlock = code
custom_banner_03.add_trigger(trigger0)


banner_01 = MapIcon("banner_01", mesh_name="map_flag_01", scale=0.3)

banner_02 = MapIcon("banner_02", mesh_name="map_flag_02", scale=0.3)

banner_03 = MapIcon("banner_03", mesh_name="map_flag_03", scale=0.3)

banner_04 = MapIcon("banner_04", mesh_name="map_flag_04", scale=0.3)

banner_05 = MapIcon("banner_05", mesh_name="map_flag_05", scale=0.3)

banner_06 = MapIcon("banner_06", mesh_name="map_flag_06", scale=0.3)

banner_07 = MapIcon("banner_07", mesh_name="map_flag_07", scale=0.3)

banner_08 = MapIcon("banner_08", mesh_name="map_flag_08", scale=0.3)

banner_09 = MapIcon("banner_09", mesh_name="map_flag_09", scale=0.3)

banner_10 = MapIcon("banner_10", mesh_name="map_flag_10", scale=0.3)

banner_11 = MapIcon("banner_11", mesh_name="map_flag_11", scale=0.3)

banner_12 = MapIcon("banner_12", mesh_name="map_flag_12", scale=0.3)

banner_13 = MapIcon("banner_13", mesh_name="map_flag_13", scale=0.3)

banner_14 = MapIcon("banner_14", mesh_name="map_flag_14", scale=0.3)

banner_15 = MapIcon("banner_15", mesh_name="map_flag_f21", scale=0.3)

banner_16 = MapIcon("banner_16", mesh_name="map_flag_16", scale=0.3)

banner_17 = MapIcon("banner_17", mesh_name="map_flag_17", scale=0.3)

banner_18 = MapIcon("banner_18", mesh_name="map_flag_18", scale=0.3)

banner_19 = MapIcon("banner_19", mesh_name="map_flag_19", scale=0.3)

banner_20 = MapIcon("banner_20", mesh_name="map_flag_20", scale=0.3)

banner_21 = MapIcon("banner_21", mesh_name="map_flag_21", scale=0.3)

banner_22 = MapIcon("banner_22", mesh_name="map_flag_22", scale=0.3)

banner_23 = MapIcon("banner_23", mesh_name="map_flag_23", scale=0.3)

banner_24 = MapIcon("banner_24", mesh_name="map_flag_24", scale=0.3)

banner_25 = MapIcon("banner_25", mesh_name="map_flag_25", scale=0.3)

banner_26 = MapIcon("banner_26", mesh_name="map_flag_26", scale=0.3)

banner_27 = MapIcon("banner_27", mesh_name="map_flag_27", scale=0.3)

banner_28 = MapIcon("banner_28", mesh_name="map_flag_28", scale=0.3)

banner_29 = MapIcon("banner_29", mesh_name="map_flag_29", scale=0.3)

banner_30 = MapIcon("banner_30", mesh_name="map_flag_30", scale=0.3)

banner_31 = MapIcon("banner_31", mesh_name="map_flag_31", scale=0.3)

banner_32 = MapIcon("banner_32", mesh_name="map_flag_32", scale=0.3)

banner_33 = MapIcon("banner_33", mesh_name="map_flag_33", scale=0.3)

banner_34 = MapIcon("banner_34", mesh_name="map_flag_34", scale=0.3)

banner_35 = MapIcon("banner_35", mesh_name="map_flag_35", scale=0.3)

banner_36 = MapIcon("banner_36", mesh_name="map_flag_36", scale=0.3)

banner_37 = MapIcon("banner_37", mesh_name="map_flag_37", scale=0.3)

banner_38 = MapIcon("banner_38", mesh_name="map_flag_38", scale=0.3)

banner_39 = MapIcon("banner_39", mesh_name="map_flag_39", scale=0.3)

banner_40 = MapIcon("banner_40", mesh_name="map_flag_40", scale=0.3)

banner_41 = MapIcon("banner_41", mesh_name="map_flag_41", scale=0.3)

banner_42 = MapIcon("banner_42", mesh_name="map_flag_42", scale=0.3)

banner_43 = MapIcon("banner_43", mesh_name="map_flag_43", scale=0.3)

banner_44 = MapIcon("banner_44", mesh_name="map_flag_44", scale=0.3)

banner_45 = MapIcon("banner_45", mesh_name="map_flag_45", scale=0.3)

banner_46 = MapIcon("banner_46", mesh_name="map_flag_46", scale=0.3)

banner_47 = MapIcon("banner_47", mesh_name="map_flag_47", scale=0.3)

banner_48 = MapIcon("banner_48", mesh_name="map_flag_48", scale=0.3)

banner_49 = MapIcon("banner_49", mesh_name="map_flag_49", scale=0.3)

banner_50 = MapIcon("banner_50", mesh_name="map_flag_50", scale=0.3)

banner_51 = MapIcon("banner_51", mesh_name="map_flag_51", scale=0.3)

banner_52 = MapIcon("banner_52", mesh_name="map_flag_52", scale=0.3)

banner_53 = MapIcon("banner_53", mesh_name="map_flag_53", scale=0.3)

banner_54 = MapIcon("banner_54", mesh_name="map_flag_54", scale=0.3)

banner_55 = MapIcon("banner_55", mesh_name="map_flag_55", scale=0.3)

banner_56 = MapIcon("banner_56", mesh_name="map_flag_56", scale=0.3)

banner_57 = MapIcon("banner_57", mesh_name="map_flag_57", scale=0.3)

banner_58 = MapIcon("banner_58", mesh_name="map_flag_58", scale=0.3)

banner_59 = MapIcon("banner_59", mesh_name="map_flag_59", scale=0.3)

banner_60 = MapIcon("banner_60", mesh_name="map_flag_60", scale=0.3)

banner_61 = MapIcon("banner_61", mesh_name="map_flag_61", scale=0.3)

banner_62 = MapIcon("banner_62", mesh_name="map_flag_62", scale=0.3)

banner_63 = MapIcon("banner_63", mesh_name="map_flag_63", scale=0.3)

banner_64 = MapIcon("banner_64", mesh_name="map_flag_d01", scale=0.3)

banner_65 = MapIcon("banner_65", mesh_name="map_flag_d02", scale=0.3)

banner_66 = MapIcon("banner_66", mesh_name="map_flag_d03", scale=0.3)

banner_67 = MapIcon("banner_67", mesh_name="map_flag_d04", scale=0.3)

banner_68 = MapIcon("banner_68", mesh_name="map_flag_d05", scale=0.3)

banner_69 = MapIcon("banner_69", mesh_name="map_flag_d06", scale=0.3)

banner_70 = MapIcon("banner_70", mesh_name="map_flag_d07", scale=0.3)

banner_71 = MapIcon("banner_71", mesh_name="map_flag_d08", scale=0.3)

banner_72 = MapIcon("banner_72", mesh_name="map_flag_d09", scale=0.3)

banner_73 = MapIcon("banner_73", mesh_name="map_flag_d10", scale=0.3)

banner_74 = MapIcon("banner_74", mesh_name="map_flag_d11", scale=0.3)

banner_75 = MapIcon("banner_75", mesh_name="map_flag_d12", scale=0.3)

banner_76 = MapIcon("banner_76", mesh_name="map_flag_d13", scale=0.3)

banner_77 = MapIcon("banner_77", mesh_name="map_flag_d14", scale=0.3)

banner_78 = MapIcon("banner_78", mesh_name="map_flag_d15", scale=0.3)

banner_79 = MapIcon("banner_79", mesh_name="map_flag_d16", scale=0.3)

banner_80 = MapIcon("banner_80", mesh_name="map_flag_d17", scale=0.3)

banner_81 = MapIcon("banner_81", mesh_name="map_flag_d18", scale=0.3)

banner_82 = MapIcon("banner_82", mesh_name="map_flag_d19", scale=0.3)

banner_83 = MapIcon("banner_83", mesh_name="map_flag_d20", scale=0.3)

banner_84 = MapIcon("banner_84", mesh_name="map_flag_d21", scale=0.3)

banner_85 = MapIcon("banner_85", mesh_name="map_flag_e01", scale=0.3)

banner_86 = MapIcon("banner_86", mesh_name="map_flag_e02", scale=0.3)

banner_87 = MapIcon("banner_87", mesh_name="map_flag_e03", scale=0.3)

banner_88 = MapIcon("banner_88", mesh_name="map_flag_e04", scale=0.3)

banner_89 = MapIcon("banner_89", mesh_name="map_flag_e05", scale=0.3)

banner_90 = MapIcon("banner_90", mesh_name="map_flag_e06", scale=0.3)

banner_91 = MapIcon("banner_91", mesh_name="map_flag_e07", scale=0.3)

banner_92 = MapIcon("banner_92", mesh_name="map_flag_e08", scale=0.3)

banner_93 = MapIcon("banner_93", mesh_name="map_flag_e09", scale=0.3)

banner_94 = MapIcon("banner_94", mesh_name="map_flag_e10", scale=0.3)

banner_95 = MapIcon("banner_95", mesh_name="map_flag_e11", scale=0.3)

banner_96 = MapIcon("banner_96", mesh_name="map_flag_e12", scale=0.3)

banner_97 = MapIcon("banner_97", mesh_name="map_flag_e13", scale=0.3)

banner_98 = MapIcon("banner_98", mesh_name="map_flag_e14", scale=0.3)

banner_99 = MapIcon("banner_99", mesh_name="map_flag_e15", scale=0.3)

banner_100 = MapIcon("banner_100", mesh_name="map_flag_e16", scale=0.3)

banner_101 = MapIcon("banner_101", mesh_name="map_flag_e17", scale=0.3)

banner_102 = MapIcon("banner_102", mesh_name="map_flag_e18", scale=0.3)

banner_103 = MapIcon("banner_103", mesh_name="map_flag_e19", scale=0.3)

banner_104 = MapIcon("banner_104", mesh_name="map_flag_e20", scale=0.3)

banner_105 = MapIcon("banner_105", mesh_name="map_flag_e21", scale=0.3)

banner_106 = MapIcon("banner_106", mesh_name="map_flag_f01", scale=0.3)

banner_107 = MapIcon("banner_107", mesh_name="map_flag_f02", scale=0.3)

banner_108 = MapIcon("banner_108", mesh_name="map_flag_f03", scale=0.3)

banner_109 = MapIcon("banner_109", mesh_name="map_flag_f04", scale=0.3)

banner_110 = MapIcon("banner_110", mesh_name="map_flag_f05", scale=0.3)

banner_111 = MapIcon("banner_111", mesh_name="map_flag_f06", scale=0.3)

banner_112 = MapIcon("banner_112", mesh_name="map_flag_f07", scale=0.3)

banner_113 = MapIcon("banner_113", mesh_name="map_flag_f08", scale=0.3)

banner_114 = MapIcon("banner_114", mesh_name="map_flag_f09", scale=0.3)

banner_115 = MapIcon("banner_115", mesh_name="map_flag_f10", scale=0.3)

banner_116 = MapIcon("banner_116", mesh_name="map_flag_f11", scale=0.3)

banner_117 = MapIcon("banner_117", mesh_name="map_flag_f12", scale=0.3)

banner_118 = MapIcon("banner_118", mesh_name="map_flag_f13", scale=0.3)

banner_119 = MapIcon("banner_119", mesh_name="map_flag_f14", scale=0.3)

banner_120 = MapIcon("banner_120", mesh_name="map_flag_f15", scale=0.3)

banner_121 = MapIcon("banner_121", mesh_name="map_flag_f16", scale=0.3)

banner_122 = MapIcon("banner_122", mesh_name="map_flag_f17", scale=0.3)

banner_123 = MapIcon("banner_123", mesh_name="map_flag_f18", scale=0.3)

banner_124 = MapIcon("banner_124", mesh_name="map_flag_f19", scale=0.3)

banner_125 = MapIcon("banner_125", mesh_name="map_flag_f20", scale=0.3)

banner_126 = MapIcon("banner_126", mesh_name="map_flag_f01", scale=0.3)

banner_127 = MapIcon("banner_127", mesh_name="map_flag_f02", scale=0.3)

banner_128 = MapIcon("banner_128", mesh_name="map_flag_f03", scale=0.3)

banner_129 = MapIcon("banner_129", mesh_name="map_flag_f04", scale=0.3)

banner_130 = MapIcon("banner_130", mesh_name="map_flag_f05", scale=0.3)

banner_131 = MapIcon("banner_131", mesh_name="map_flag_f06", scale=0.3)

banner_132 = MapIcon("banner_132", mesh_name="map_flag_f07", scale=0.3)

banner_133 = MapIcon("banner_133", mesh_name="map_flag_f08", scale=0.3)

banner_134 = MapIcon("banner_134", mesh_name="map_flag_f09", scale=0.3)

banner_135 = MapIcon("banner_135", mesh_name="map_flag_f10", scale=0.3)

map_flag_kingdom_a = MapIcon("map_flag_kingdom_a", mesh_name="map_flag_kingdom_a", scale=0.3)

map_flag_kingdom_b = MapIcon("map_flag_kingdom_b", mesh_name="map_flag_kingdom_b", scale=0.3)

map_flag_kingdom_c = MapIcon("map_flag_kingdom_c", mesh_name="map_flag_kingdom_c", scale=0.3)

map_flag_kingdom_d = MapIcon("map_flag_kingdom_d", mesh_name="map_flag_kingdom_d", scale=0.3)

map_flag_kingdom_e = MapIcon("map_flag_kingdom_e", mesh_name="map_flag_kingdom_e", scale=0.3)

map_flag_kingdom_f = MapIcon("map_flag_kingdom_f", mesh_name="map_flag_kingdom_f", scale=0.3)

banner_136 = MapIcon("banner_136", mesh_name="map_flag_15", scale=0.3)

bandit_lair = MapIcon("bandit_lair", mesh_name="map_bandit_lair", scale=0.45, no_shadow=True)

