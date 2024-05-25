# This Python file uses the following encoding: utf-8
from simple_trigger import SimpleTrigger


simple_trigger0 = SimpleTrigger(-6.0)
def code():
    pass
simple_trigger0.codeBlock = code


simple_trigger1 = SimpleTrigger(-5.0)
def code():
    pass
simple_trigger1.codeBlock = code


simple_trigger2 = SimpleTrigger(1.0)
def code():
    if _training_ground_position_changed == 0:
        _training_ground_position_changed = 1
        set_fixed_point_multiplier(100)
        position_set_x(0,7050)
        position_set_y(0,7200)
        party_set_position(p.training_ground_3,0)
    #end
    if _auto_besiege_town > 0 and _g_player_besiege_town > 0 and _g_siege_method >= 1:
        cur_hours_001 = store_current_hours()
        if _g_siege_force_wait == 0 and cur_hours_001 >= _g_siege_method_finish_hours and not is_currently_night():
            rest_for_hours(0,0,0)
simple_trigger2.codeBlock = code


simple_trigger3 = SimpleTrigger(0.0)
def code():
    if _bug_fix_version == 0:
        disable_party(p.test_scene)
        party_set_slot(p.town_1,27,0)
        faction_set_note_available(fac.player_faction,0)
        faction_set_note_available(fac.no_faction,0)
        if not check_quest_active(qst.kidnapped_girl):
            party_remove_members(p.main_party,trp.kidnapped_girl,1)
        #end
        for trp_001 in range(trp.knight_1_1, trp.kingdom_1_pretender):
            if troop_slot_eq(trp_001,2,0):
                troop_faction_002 = store_faction_of_troop(trp_001)
                if is_between(troop_faction_002,fac.kingdom_1,fac.kingdoms_end):
                    troop_set_slot(trp_001,2,2)
                #end
            #end
        #end
        initialize_item_info()
        _bug_fix_version = 1
    #end
    if _g_player_is_captive == 1 and _capturer_party > 0 and party_is_active(_capturer_party):
        party_relocate_near_party(p.main_party,_capturer_party,0)
simple_trigger3.codeBlock = code



simple_trigger100 = SimpleTrigger(24.0)
def code():
    item_set_slot(itm.bread,1,8)
    item_set_slot(itm.grain,1,2)
    item_set_slot(itm.smoked_fish,1,4)
    item_set_slot(itm.dried_meat,1,5)
    item_set_slot(itm.cheese,1,5)
    item_set_slot(itm.sausages,1,5)
    item_set_slot(itm.butter,1,4)
    item_set_slot(itm.chicken,1,8)
    item_set_slot(itm.cattle_meat,1,7)
    item_set_slot(itm.pork,1,6)
    item_set_slot(itm.raw_olives,1,1)
    item_set_slot(itm.cabbages,1,2)
    item_set_slot(itm.raw_grapes,1,3)
    item_set_slot(itm.apples,1,4)
    item_set_slot(itm.raw_date_fruit,1,4)
    item_set_slot(itm.honey,1,6)
    item_set_slot(itm.wine,1,5)
    item_set_slot(itm.ale,1,4)
simple_trigger100.codeBlock = code


simple_trigger101 = SimpleTrigger(24.0)
def code():
    pass
simple_trigger101.codeBlock = code


simple_trigger102 = SimpleTrigger(24.0)
def code():
    pass
simple_trigger102.codeBlock = code


simple_trigger103 = SimpleTrigger(24.0)
def code():
    pass
simple_trigger103.codeBlock = code


simple_trigger104 = SimpleTrigger(24.0)
def code():
    pass
simple_trigger104.codeBlock = code


simple_trigger105 = SimpleTrigger(24.0)
def code():
    pass
simple_trigger105.codeBlock = code


simple_trigger106 = SimpleTrigger(24.0)
def code():
    pass
simple_trigger106.codeBlock = code


simple_trigger107 = SimpleTrigger(24.0)
def code():
    pass
simple_trigger107.codeBlock = code


simple_trigger108 = SimpleTrigger(24.0)
def code():
    pass
simple_trigger108.codeBlock = code


simple_trigger109 = SimpleTrigger(24.0)
def code():
    pass
simple_trigger109.codeBlock = code


