from __future__ import division
from past.utils import old_div
from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *

from module_constants import *

simple_triggers = [

(ti_on_party_encounter, [
]),

(ti_simulate_battle, [
]),

(1.0, [
(try_begin),
    (eq,"$training_ground_position_changed",0),
    (assign,"$training_ground_position_changed",1),
    (set_fixed_point_multiplier, 100),
    (position_set_x,0,7050),
    (position_set_y,0,7200),
    (party_set_position,"p_training_ground_3",0),
(try_end),
(try_begin),
    (gt,"$auto_besiege_town",0),
    (gt,"$g_player_besiege_town",0),
    (ge,"$g_siege_method",1),
    (store_current_hours,":cur_hours_001"),
    (try_begin),
        (eq,"$g_siege_force_wait",0),
        (ge,":cur_hours_001","$g_siege_method_finish_hours"),
        (neg|is_currently_night),
        (rest_for_hours,0,0,0),
    (try_end),
(try_end),
]),

(0.0, [
(try_begin),
    (eq,"$bug_fix_version",0),
    (disable_party,"p_test_scene"),
    (party_set_slot,"p_town_1",27,0),
    (faction_set_note_available, "fac_player_faction", 0),
    (faction_set_note_available, "fac_no_faction", 0),
    (try_begin),
        (neg|check_quest_active,"qst_kidnapped_girl"),
        (party_remove_members,"p_main_party","trp_kidnapped_girl",1),
    (try_end),
    (try_for_range, ":trp_001", "trp_knight_1_1", "trp_kingdom_1_pretender"),
        (try_begin),
            (troop_slot_eq,":trp_001",2,0),
            (store_troop_faction,":troop_faction_002",":trp_001"),
            (try_begin),
                (is_between,":troop_faction_002","fac_kingdom_1","fac_kingdoms_end"),
                (troop_set_slot,":trp_001",2,2),
            (try_end),
        (try_end),
    (try_end),
    (call_script, "script_initialize_item_info"),
    (assign,"$bug_fix_version",1),
(try_end),
(try_begin),
    (eq,"$g_player_is_captive",1),
    (gt,"$capturer_party",0),
    (party_is_active,"$capturer_party"),
    (party_relocate_near_party,"p_main_party","$capturer_party",0),
(try_end),
]),

(24.0, [
(item_set_slot,"itm_bread",1,8),
(item_set_slot,"itm_grain",1,2),
(item_set_slot,"itm_smoked_fish",1,4),
(item_set_slot,"itm_dried_meat",1,5),
(item_set_slot,"itm_cheese",1,5),
(item_set_slot,"itm_sausages",1,5),
(item_set_slot,"itm_butter",1,4),
(item_set_slot,"itm_chicken",1,8),
(item_set_slot,"itm_cattle_meat",1,7),
(item_set_slot,"itm_pork",1,6),
(item_set_slot,"itm_raw_olives",1,1),
(item_set_slot,"itm_cabbages",1,2),
(item_set_slot,"itm_raw_grapes",1,3),
(item_set_slot,"itm_apples",1,4),
(item_set_slot,"itm_raw_date_fruit",1,4),
(item_set_slot,"itm_honey",1,6),
(item_set_slot,"itm_wine",1,5),
(item_set_slot,"itm_ale",1,4),
]),

(24.0, [
]),

(24.0, [
]),

(24.0, [
]),

(24.0, [
]),

(24.0, [
]),

(24.0, [
]),

(24.0, [
]),

(24.0, [
]),

(24.0, [
]),

]
