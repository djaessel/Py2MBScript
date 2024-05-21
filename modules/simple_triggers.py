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


simple_trigger4 = SimpleTrigger(0.0)
def code():
    if _g_last_rest_center > 0:
        party_battle_opponent_001 = party_get_battle_opponent(_g_last_rest_center)
        if party_battle_opponent_001 > 0:
            party_faction_002 = store_faction_of_party(_g_last_rest_center)
            faction_relation_003 = store_relation(party_faction_002,fac.player_supporters_faction)
            party_faction_004 = store_faction_of_party(party_battle_opponent_001)
            faction_relation_005 = store_relation(party_faction_004,fac.player_supporters_faction)
            if faction_relation_003 >= 0 and faction_relation_005 < 0:
                start_encounter(_g_last_rest_center)
                rest_for_hours(0,0,0)
            else:
                cur_hours_006 = store_current_hours()
                var007 = 0
                if _g_check_autos_at_hour != 0 and cur_hours_006 >= _g_check_autos_at_hour:
                    var007 = 1
                    _g_check_autos_at_hour = 0
                #end
            #end
        #end
        if var007 == 1 or map_free():
            if _auto_menu >= 1:
                jump_to_menu(_auto_menu)
                _auto_menu = -1
            elif _auto_enter_town >= 1:
                start_encounter(_auto_enter_town)
            elif _auto_besiege_town >= 1:
                start_encounter(_auto_besiege_town)
            elif _g_camp_mode >= 1:
                _g_camp_mode = 0
                _g_infinite_camping = 0
                _g_player_icon_state = 0
                rest_for_hours(0,0,0)
                print("@Breaking camp...")
            #end
        #end
    #end
simple_trigger4.codeBlock = code


simple_trigger5 = SimpleTrigger(0.0)
def code():
    if troop_slot_ge(trp.notification_menu_types,0,1):
        troop_slot_001 = troop_get_slot(trp.notification_menu_types,0)
        _g_notification_menu_var1 = troop_get_slot(trp.notification_menu_var1,0)
        _g_notification_menu_var2 = troop_get_slot(trp.notification_menu_var2,0)
        jump_to_menu(troop_slot_001)
        var002 = 2
        for slot_no_003 in range(1, var002):
            if troop_slot_ge(trp.notification_menu_types,slot_no_003,1):
                var002 += 1
            #end
        #end
        slot_no_004 = slot_no_003 - 1
        troop_slot_005 = troop_get_slot(trp.notification_menu_types,slot_no_003)
        troop_set_slot(trp.notification_menu_types,slot_no_004,troop_slot_005)
        troop_slot_005 = troop_get_slot(trp.notification_menu_var1,slot_no_003)
        troop_set_slot(trp.notification_menu_var1,slot_no_004,troop_slot_005)
        troop_slot_005 = troop_get_slot(trp.notification_menu_var2,slot_no_003)
        troop_set_slot(trp.notification_menu_var2,slot_no_004,troop_slot_005)
    #end
simple_trigger5.codeBlock = code


simple_trigger6 = SimpleTrigger(1.0)
def code():
    if map_free():
        music_set_situation_with_culture(65536)
simple_trigger6.codeBlock = code


simple_trigger7 = SimpleTrigger(0.0)
def code():
    if _caravan_escort_state == 1 and party_is_active(_caravan_escort_party_id):
        distance_parties_001 = store_distance_to_party_from_party(_caravan_escort_destination_town,_caravan_escort_party_id)
        if distance_parties_001 < 2:
            distance_parties_002 = store_distance_to_party_from_party(p.main_party,_caravan_escort_party_id)
            if distance_parties_002 < 5:
                _talk_context = 2
                _g_encountered_party = _caravan_escort_party_id
                troop_id_003 = party_stack_get_troop_id(_caravan_escort_party_id,0)
                party_stack_troop_dna_004 = party_stack_get_troop_dna(_caravan_escort_party_id,0)
                start_map_conversation(troop_id_003,party_stack_troop_dna_004)
            #end
        #end
    #end
    if _g_reset_mission_participation > 1:
        for trp_005 in range(trp.npc1, trp.heroes_end):
            troop_set_slot(trp_005,149,0)
        #end
    #end
simple_trigger7.codeBlock = code


simple_trigger8 = SimpleTrigger(24.0)
def code():
    for fac_001 in range(fac.kingdom_1, fac.kingdoms_end):
        faction_slot_002 = faction_get_slot(fac_001,99)
        var003 = 140 - _player_right_to_rule
        var003 /= 14
        val_max(var003,1)
        var004 = faction_slot_002 / var003
        faction_slot_002 -= var004
        faction_set_slot(fac_001,99,faction_slot_002)
    #end
simple_trigger8.codeBlock = code


simple_trigger9 = SimpleTrigger(4.0)
def code():
    for trp_001 in range(trp.knight_1_1_wife, trp.heroes_end):
        if not troop_slot_ge(trp_001,8,0):
            get_kingdom_lady_social_determinants(trp_001)
            var002 = reg1
            troop_set_slot(trp_001,12,var002)
        #end
    #end
simple_trigger9.codeBlock = code


simple_trigger10 = SimpleTrigger(2.0)
def code():
    if _cheat_mode == 1:
        var001 = 0
        for cur_party in __all_parties__:
            if cur_party > p.spawn_points_end:
                troop_id_003 = party_stack_get_troop_id(cur_party,0)
                if is_between(troop_id_003,trp.npc1,trp.knight_1_1_wife):
                    troop_slot_004 = troop_get_slot(troop_id_003,10)
                    if cur_party != troop_slot_004:
                        reg4 = cur_party
                        reg5 = troop_slot_004
                        s3 = str_store_troop_name(troop_id_003)
                        print("@{!}{s3} commander of party #{reg4} which is not his troop leaded party {reg5}")
                        s65 = str_store_string(gstr.party_with_commander_mismatch__check_log_for_details_)
                        if var001 == 0:
                            add_notification_menu(mnu.debug_alert_from_s65,0,0)
                            var001 = 1
                        #end
                    #end
                #end
            #end
        #end
    #end
simple_trigger10.codeBlock = code


simple_trigger11 = SimpleTrigger(24.0)
def code():
    if not check_quest_active(qst.visit_lady) and not troop_slot_ge(trp.player,8,1) and not troop_slot_ge(trp.player,30,trp.npc1):
        var001 = -1
        var002 = 120
        for trp_003 in range(trp.knight_1_1_wife, trp.heroes_end):
            if troop_slot_ge(trp_003,5,2) and not troop_slot_eq(trp_003,5,4) and troop_slot_eq(trp_003,37,0) and troop_slot_eq(trp_003,30,-1):
                troop_slot_004 = troop_get_slot(trp_003,12)
                if is_between(troop_slot_004,p.town_1,p.village_1):
                    troop_get_relation_with_troop(trp.player,trp_003)
                    if reg0 > 1:
                        cur_hours_005 = store_current_hours()
                        troop_slot_006 = troop_get_slot(trp_003,4)
                        cur_hours_005 -= troop_slot_006
                        if cur_hours_005 > var002:
                            var002 = cur_hours_005
                            var001 = trp_003
                            var007 = troop_slot_004
                        #end
                    #end
                #end
            #end
        #end
        if var001 > 0:
            add_notification_menu(mnu.notification_lady_requests_visit,var001,var007)
        #end
    #end
simple_trigger11.codeBlock = code


simple_trigger12 = SimpleTrigger(1.0)
def code():
    if _g_player_raiding_village >= 1:
        if _g_player_is_captive != 0:
            _g_player_raiding_village = 0
        elif map_free():
            _g_player_raiding_village = 0
        elif party_slot_eq(_g_player_raiding_village,35,2) or party_slot_eq(_g_player_raiding_village,35,4):
            start_encounter(_g_player_raiding_village)
            rest_for_hours(0)
            _g_player_raiding_village = 0
            _g_player_raid_complete = 1
        elif party_slot_eq(_g_player_raiding_village,35,1):
            rest_for_hours(3,5,1)
        else:
            rest_for_hours(0,0,0)
            _g_player_raiding_village = 0
            _g_player_raid_complete = 0
        #end
    #end
simple_trigger12.codeBlock = code


simple_trigger13 = SimpleTrigger(168.0)
def code():
    _g_presentation_lines_to_display_begin = 0
    _g_presentation_lines_to_display_end = 15
    _g_apply_budget_report_to_gold = 1
    if _g_infinite_camping == 0:
        start_presentation(prsnt.budget_report)
    #end
simple_trigger13.codeBlock = code


simple_trigger14 = SimpleTrigger(24.0)
def code():
    if _auto_menu <= 0 and _players_kingdom > 0 and _players_kingdom != fac.player_supporters_faction and _player_has_homage == 0:
        troop_slot_001 = troop_get_slot(trp.player,30)
        var002 = 0
        if is_between(troop_slot_001,trp.npc1,trp.knight_1_1_wife):
            troop_faction_003 = store_faction_of_troop(troop_slot_001)
            if troop_faction_003 == _players_kingdom:
                var002 = 1
            #end
        #end
    #end
    if var002 == 0:
        cur_day_004 = store_current_day()
        if cur_day_004 > _mercenary_service_next_renew_day:
            jump_to_menu(mnu.oath_fulfilled)
simple_trigger14.codeBlock = code


simple_trigger15 = SimpleTrigger(180.0)
def code():
    _g_player_luck -= 1
    val_max(_g_player_luck,0)
simple_trigger15.codeBlock = code


simple_trigger16 = SimpleTrigger(72.0)
def code():
    _lady_flirtation_location = 0
simple_trigger16.codeBlock = code


simple_trigger17 = SimpleTrigger(4.0)
def code():
    _g_time_to_spare = 1
    if troop_slot_ge(trp.player,30,trp.npc1):
        _g_player_banner_granted = 1
    #end
simple_trigger17.codeBlock = code


simple_trigger18 = SimpleTrigger(24.0)
def code():
    if _g_player_banner_granted == 1 and troop_slot_eq(trp.player,13,0) and _auto_menu <= 0:
        start_presentation(prsnt.banner_selection)
simple_trigger18.codeBlock = code


simple_trigger19 = SimpleTrigger(24.0)
def code():
    get_player_party_morale_values()
    var001 = reg0
    party_morale_002 = party_get_morale(p.main_party)
    var003 = var001 - party_morale_002
    var004 = var003 / 5
    var005 = var004 * 5
    if var005 != var003:
        if var003 > 0:
            var004 += 1
        else:
            var004 -= 1
        #end
    #end
    party_morale_002 += var004
    party_set_morale(p.main_party,party_morale_002)
simple_trigger19.codeBlock = code


simple_trigger20 = SimpleTrigger(168.0)
def code():
    for p_001 in range(p.town_1, p.salt_mine):
        party_num_prisoners_stacks_002 = party_get_num_prisoner_stacks(p_001)
        for var003 in range(0, party_num_prisoners_stacks_002):
            party_prisoner_troop_id_004 = party_prisoner_stack_get_troop_id(p_001,var003)
            if not troop_is_hero(party_prisoner_troop_id_004):
                party_prisoner_stack_size_005 = party_prisoner_stack_get_size(p_001,var003)
                random_x_006 = store_random_in_range(0,40)
                party_prisoner_stack_size_005 *= random_x_006
                party_prisoner_stack_size_005 /= 100
                party_remove_prisoners(p_001,party_prisoner_troop_id_004,party_prisoner_stack_size_005)
            #end
        #end
    #end
simple_trigger20.codeBlock = code


simple_trigger21 = SimpleTrigger(168.0)
def code():
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        troop_slot_002 = troop_get_slot(trp_001,21)
        troop_slot_002 *= 101
        troop_slot_002 /= 100
        troop_set_slot(trp_001,21,troop_slot_002)
        calculate_hero_weekly_net_income_and_add_to_wealth(trp_001)
    #end
    for p_003 in range(p.town_1, p.village_1):
        if not party_slot_eq(p_003,7,trp.player) and party_slot_ge(p_003,7,1):
            party_slot_004 = party_get_slot(p_003,49)
            party_slot_005 = party_get_slot(p_003,50)
            var006 = party_slot_005 * 15
            var006 += 700
            if party_slot_eq(p_003,0,3):
                var006 *= 3
                var006 /= 2
            #end
        #end
        party_slot_004 += var006
        calculate_weekly_party_wage(p_003)
        party_slot_004 -= reg0
        val_max(party_slot_004,0)
        party_set_slot(p_003,49,party_slot_004)
    #end
simple_trigger21.codeBlock = code


simple_trigger22 = SimpleTrigger(24.0)
def code():
    party_faction_010_list1 = [
    _players_kingdom,
    fac.player_supporters_faction,
    ]
    party_faction_004_list1 = [
    _players_kingdom,
    fac.player_supporters_faction,
    ]
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        if troop_slot_eq(trp_001,2,2):
            troop_slot_002 = troop_get_slot(trp_001,10)
            if troop_slot_002 >= 1 and party_is_active(troop_slot_002):
                party_attached_003 = party_get_attached_to(troop_slot_002)
                if is_between(party_attached_003,p.town_1,p.salt_mine) and party_slot_eq(party_attached_003,54,-1):
                    party_faction_004 = store_faction_of_party(troop_slot_002)
                    if party_faction_004 in party_faction_004_list1:
                        random_x_005 = 1
                        random_x_006 = store_random_in_range(0,2)
                        random_x_005 += random_x_006
                    else:
                        campaign_ai = game_get_reduce_campaign_ai()
                        if campaign_ai == 0:
                            random_x_005 = 2
                        elif campaign_ai == 1:
                            random_x_005 = 1
                            random_x_006 = store_random_in_range(0,2)
                            random_x_005 += random_x_006
                        elif campaign_ai == 2:
                            random_x_005 = 1
                        #end
                    #end
                #end
            #end
        #end
        if faction_slot_eq(party_faction_004,8,trp_001):
            random_x_005 += 1
        #end
        for var008 in range(0, random_x_005):
            hire_men_to_kingdom_hero_party(trp_001)
        #end
    #end
    for p_009 in range(p.town_1, p.village_1):
        if not party_slot_eq(p_009,7,trp.player) and party_slot_ge(p_009,7,1) and party_slot_eq(p_009,54,-1):
            party_faction_010 = store_faction_of_party(p_009)
            if party_faction_010 in party_faction_010_list1:
                var011 = 450
            else:
                campaign_ai = game_get_reduce_campaign_ai()
                var011 = 450
                if campaign_ai == 0:
                    var011 = 300
                    random_x_005 = store_random_in_range(0,2)
                    random_x_005 += 1
                elif campaign_ai == 1:
                    var011 = 450
                    random_x_005 = 1
                elif campaign_ai == 2:
                    var011 = 600
                    random_x_005 = store_random_in_range(0,2)
                #end
            #end
        #end
        for var008 in range(0, random_x_005):
            party_slot_012 = party_get_slot(p_009,49)
            var013 = party_slot_012
            var013 /= 2
            if var013 > var011 and cf_reinforce_party(p_009):
                party_slot_012 -= var011
                party_set_slot(p_009,49,party_slot_012)
            #end
        #end
    #end
    for p_009 in range(p.town_1, p.salt_mine):
        random_x_014 = store_random_in_range(0,30)
        if random_x_014 <= 10:
            get_center_ideal_prosperity(p_009)
            var015 = reg0
            party_slot_016 = party_get_slot(p_009,50)
            if random_x_014 == 0:
                if True:
                    random_x_014 = store_random_in_range(0,2)
                    if random_x_014 == 0 and not is_between(p_009,p.castle_1,p.village_1):
                        change_center_prosperity(p_009,-10)
                        _newglob_total_prosperity_from_convergence += -10
                    else:
                        change_center_prosperity(p_009,10)
                        _newglob_total_prosperity_from_convergence += 10
                    #end
                #end
            #end
        elif party_slot_016 > var015:
            change_center_prosperity(p_009,-1)
            _newglob_total_prosperity_from_convergence += -1
        elif party_slot_016 < var015:
            change_center_prosperity(p_009,1)
            _newglob_total_prosperity_from_convergence += 1
        #end
    #end
simple_trigger22.codeBlock = code


simple_trigger23 = SimpleTrigger(360.0)
def code():
    pass
simple_trigger23.codeBlock = code


simple_trigger24 = SimpleTrigger(6.0)
def code():
    cur_day_001 = store_current_day()
    if cur_day_001 != _g_last_half_payment_check_day:
        _g_last_half_payment_check_day = cur_day_001
        if _g_half_payment_checkpoint == 1:
            _g_cur_week_half_daily_wage_payments += 1
        #end
        _g_half_payment_checkpoint = 1
    #end
    var002 = 0
    if not map_free() and _g_last_rest_center >= 0 and party_slot_eq(_g_last_rest_center,130,1) or is_between(_g_last_rest_center,p.town_1,p.village_1):
        var002 = 1
    #end
    if var002 == 0:
        _g_half_payment_checkpoint = 0
simple_trigger24.codeBlock = code


simple_trigger25 = SimpleTrigger(24.0)
def code():
    randomly_start_war_peace_new(1)
    if True:
        random_x_001 = store_random_in_range(p.village_1,p.salt_mine)
        random_x_002 = store_random_in_range(p.village_1,p.salt_mine)
        party_faction_003 = store_faction_of_party(random_x_001)
        party_faction_004 = store_faction_of_party(random_x_002)
        if random_x_001 != random_x_002 and party_faction_003 != party_faction_004:
            diplomacy_faction_get_diplomatic_status_with_faction(party_faction_004,party_faction_003)
            if reg0 == 0:
                if party_slot_eq(random_x_001,61,party_faction_004):
                    add_notification_menu(mnu.notification_border_incident,random_x_001,-1)
                elif party_slot_eq(random_x_001,62,party_faction_004):
                    add_notification_menu(mnu.notification_border_incident,random_x_001,-1)
                else:
                    set_fixed_point_multiplier(1)
                    distance_parties_005 = store_distance_to_party_from_party(random_x_001,random_x_002)
                    if distance_parties_005 < 25:
                        add_notification_menu(mnu.notification_border_incident,random_x_001,random_x_002)
                    #end
                #end
            #end
        #end
    #end
    for fac_006 in range(fac.player_supporters_faction, fac.kingdoms_end):
        if faction_slot_eq(fac_006,21,0):
            for fac_007 in range(fac.player_supporters_faction, fac.kingdoms_end):
                if fac_006 != fac_007 and faction_slot_eq(fac_007,21,0):
                    slot_no_008 = fac_007 + 120
                    slot_no_008 = slot_no_008 - fac.player_supporters_faction
                    faction_slot_009 = faction_get_slot(fac_006,slot_no_008)
                    if faction_slot_009 >= 1:
                        if faction_slot_009 == 1:
                            update_faction_notes(fac_006)
                            if fac_006 < fac_007:
                                add_notification_menu(mnu.notification_truce_expired,fac_006,fac_007)
                            #end
                        #end
                    #end
                #end
                faction_slot_009 -= 1
                faction_set_slot(fac_006,slot_no_008,faction_slot_009)
            #end
            slot_no_010 = fac_007 + 130
            slot_no_010 = slot_no_010 - fac.player_supporters_faction
            faction_slot_011 = faction_get_slot(fac_006,slot_no_010)
            if faction_slot_011 >= 1:
                if True:
                    faction_relation_012 = store_relation(fac_006,fac_007)
                    if faction_relation_012 < 0:
                        faction_set_slot(fac_006,slot_no_010,0)
                    elif faction_slot_011 == 1:
                        add_notification_menu(mnu.notification_casus_belli_expired,fac_006,fac_007)
                        faction_set_slot(fac_006,slot_no_010,0)
                    else:
                        faction_slot_011 -= 1
                        faction_set_slot(fac_006,slot_no_010,faction_slot_011)
                    #end
                #end
            #end
            if True:
                faction_relation_012 = store_relation(fac_006,fac_007)
                if faction_relation_012 < 0:
                    slot_no_013 = fac_007 + 140
                    slot_no_013 = slot_no_013 - fac.player_supporters_faction
                    faction_slot_014 = faction_get_slot(fac_006,slot_no_013)
                    faction_slot_014 += 1
                    faction_set_slot(fac_006,slot_no_013,faction_slot_014)
                #end
            #end
        #end
        update_faction_notes(fac_006)
    #end
simple_trigger25.codeBlock = code


simple_trigger26 = SimpleTrigger(48.0)
def code():
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        if troop_slot_eq(trp_001,2,2):
            troop_slot_002 = troop_get_slot(trp_001,10)
            if troop_slot_002 > p.salt_mine and party_is_active(troop_slot_002):
                skill_lvl_003 = store_skill_level(17,trp_001)
                skill_lvl_003 += 5
                var004 = skill_lvl_003 * 1000
                var005 = 30
                if True:
                    troop_faction_006 = store_faction_of_troop(trp_001)
                    if troop_faction_006 != _players_kingdom:
                        campaign_ai = game_get_reduce_campaign_ai()
                        if campaign_ai == 0:
                            var005 = 35
                            var004 *= 3
                            var004 /= 2
                        elif campaign_ai == 2:
                            var005 = 25
                            var004 /= 2
                        #end
                    #end
                #end
            #end
        #end
        random_x_008 = store_random_in_range(0,100)
        if random_x_008 <= var005:
            party_upgrade_with_xp(troop_slot_002,var004)
        #end
    #end
    for p_009 in range(p.town_1, p.village_1):
        party_slot_010 = party_get_slot(p_009,7)
        if party_slot_010 != trp.player:
            var004 = 3000
            var005 = 30
            if True:
                troop_faction_011 = -1
                if party_slot_010 >= 0:
                    troop_faction_011 = store_faction_of_troop(party_slot_010)
                #end
            #end
            if troop_faction_011 != _players_kingdom:
                campaign_ai = game_get_reduce_campaign_ai()
                if campaign_ai == 0:
                    var005 = 35
                    var004 *= 3
                    var004 /= 2
                elif campaign_ai == 2:
                    var005 = 25
                    var004 /= 2
                #end
            #end
        #end
        random_x_008 = store_random_in_range(0,100)
        if random_x_008 <= var005:
            party_upgrade_with_xp(p_009,var004)
        #end
    #end
simple_trigger26.codeBlock = code


simple_trigger27 = SimpleTrigger(24.0)
def code():
    process_sieges()
simple_trigger27.codeBlock = code


simple_trigger28 = SimpleTrigger(2.0)
def code():
    process_village_raids()
simple_trigger28.codeBlock = code


simple_trigger29 = SimpleTrigger(7.0)
def code():
    init_ai_calculation()
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        if troop_slot_eq(trp_001,2,2):
            calculate_troop_ai(trp_001)
        #end
    #end
simple_trigger29.codeBlock = code


simple_trigger30 = SimpleTrigger(24.0)
def code():
    pass
simple_trigger30.codeBlock = code


simple_trigger31 = SimpleTrigger(24.0)
def code():
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        troop_slot_002 = troop_get_slot(trp_001,51)
        troop_slot_002 -= 5
        val_max(troop_slot_002,0)
        troop_set_slot(trp_001,51,troop_slot_002)
    #end
    random_x_003 = store_random_in_range(1,3)
    val_min(random_x_003,2)
    for trp_004 in range(trp.npc1, trp.knight_1_1_wife):
        troop_slot_005 = troop_get_slot(trp_004,150)
        if troop_slot_005 >= 1:
            troop_slot_005 -= random_x_003
            val_max(troop_slot_005,0)
            troop_set_slot(trp_004,150,troop_slot_005)
        #end
    #end
    troop_slot_005 = troop_get_slot(trp.player,150)
    troop_slot_005 -= random_x_003
    val_max(troop_slot_005,0)
    troop_set_slot(trp.player,150,troop_slot_005)
simple_trigger31.codeBlock = code


simple_trigger32 = SimpleTrigger(8.0)
def code():
    if call_script(script.cf_random_political_event) and call_script(script.cf_random_political_event):
        pass
simple_trigger32.codeBlock = code


simple_trigger33 = SimpleTrigger(0.5)
def code():
    troop_faction_007_list1 = [
    fac.player_supporters_faction,
    _players_kingdom,
    ]
    troop_slot_006_list1 = [
    5,
    4,
    3,
    2,
    ]
    _g_lord_long_term_count += 1
    if not is_between(_g_lord_long_term_count,trp.kingdom_heroes_including_player_begin,trp.knight_1_1_wife):
        _g_lord_long_term_count = trp.kingdom_heroes_including_player_begin
    #end
    troop_id_001 = _g_lord_long_term_count
    if troop_id_001 == trp.kingdom_heroes_including_player_begin:
        troop_id_001 = trp.player
    #end
    if _cheat_mode == 1:
        s9 = str_store_troop_name(troop_id_001)
        print("@{!}DEBUG -- Doing political calculations for {s9}")
    #end
    if troop_slot_eq(troop_id_001,2,2) and troop_id_001 != trp.player:
        var002 = -1
        for p_003 in range(p.town_1, p.salt_mine):
            if party_slot_eq(p_003,7,troop_id_001):
                var002 = p_003
            #end
        #end
        if var002 == -1:
            troop_faction_004 = store_faction_of_troop(troop_id_001)
            faction_slot_005 = faction_get_slot(troop_faction_004,11)
            troop_slot_006 = troop_get_slot(troop_id_001,52)
            if faction_slot_005 != troop_id_001:
                if troop_slot_006 in troop_slot_006_list1:
                    troop_change_relation_with_troop(troop_id_001,faction_slot_005,-4)
                    _total_no_fief_changes += -4
                elif troop_slot_006 == 1:
                    troop_change_relation_with_troop(troop_id_001,faction_slot_005,-2)
                    _total_no_fief_changes += -2
                #end
            #end
        #end
    #end
    if troop_slot_eq(troop_id_001,2,2) or troop_id_001 == trp.player:
        if troop_id_001 == trp.player:
            troop_faction_007 = _players_kingdom
        else:
            troop_faction_007 = store_faction_of_troop(troop_id_001)
        #end
        faction_slot_005 = faction_get_slot(troop_faction_007,11)
        if troop_id_001 != faction_slot_005 and not is_between(troop_id_001,trp.kingdom_1_lord,trp.knight_1_1) and not is_between(troop_id_001,trp.kingdom_1_pretender,trp.knight_1_1_wife):
            var008 = 0
            for p_009 in range(p.town_1, p.village_1):
                party_faction_010 = store_faction_of_party(p_009)
                if party_faction_010 == troop_faction_007:
                    var008 += 1
                #end
            #end
        #end
        if troop_faction_007 in troop_faction_007_list1:
            var008 += 1
        #end
        troop_get_relation_with_troop(troop_id_001,faction_slot_005)
        if reg0 > -50 or var008 == 0 and cf_troop_can_intrigue(troop_id_001,0):
            random_x_011 = store_random_in_range(0,2)
            if var008 == 0 or random_x_011 != 0 and troop_id_001 != trp.player:
                if var008 != 0:
                    _g_give_advantage_to_original_faction = 1
                #end
            #end
            troop_faction_012 = store_faction_of_troop(troop_id_001)
            lord_find_alternative_faction(troop_id_001)
            var013 = reg0
            _g_give_advantage_to_original_faction = 0
            if var013 != troop_faction_012 and is_between(var013,fac.player_supporters_faction,fac.kingdoms_end):
                s1 = str_store_troop_name_link(troop_id_001)
                s2 = str_store_faction_name_link(var013)
                s3 = str_store_faction_name_link(troop_faction_007)
                change_troop_faction(troop_id_001,var013)
                if _cheat_mode >= 1:
                    s4 = str_store_troop_name(troop_id_001)
                    print("@{!}DEBUG - {s4} faction changed in defection")
                #end
                reg4 = troop_get_type(troop_id_001)
                s4 = str_store_string(gstr.lord_defects_ordinary)
                display_log_message("@{!}{s4}")
                if _cheat_mode == 1 and var013 == _players_kingdom or troop_faction_007 == _players_kingdom:
                    add_notification_menu(mnu.notification_lord_defects,troop_id_001,troop_faction_007)
                #end
            #end
        elif faction_slot_005 != trp.player:
            troop_get_relation_with_troop(troop_id_001,faction_slot_005)
            if reg0 <= -50:
                indict_lord_for_treason(troop_id_001,troop_faction_007)
            #end
        #end
    elif troop_id_001 != trp.player:
        troop_faction_007 = store_faction_of_troop(troop_id_001)
        if faction_slot_ge(troop_faction_007,64,1) and not troop_slot_ge(troop_id_001,154,1) and troop_slot_eq(troop_id_001,154,-1) or _players_kingdom != troop_faction_007 and troop_slot_eq(troop_id_001,2,2):
            npc_decision_checklist_take_stand_on_issue(troop_id_001)
            troop_set_slot(troop_id_001,154,reg0)
        #end
    #end
    for trp_014 in range(trp.npc1, trp.knight_1_1_wife):
        troop_get_relation_with_troop(troop_id_001,trp_014)
        if reg0 < 0:
            var015 = reg0
            var016 = 0 - var015
            random_x_017 = store_random_in_range(0,300)
            if random_x_017 < var016:
                troop_change_relation_with_troop(troop_id_001,trp_014,1)
                _total_relation_changes_through_convergence += 1
            #end
        #end
    #end
simple_trigger33.codeBlock = code


simple_trigger34 = SimpleTrigger(2.0)
def code():
    pass
simple_trigger34.codeBlock = code


simple_trigger35 = SimpleTrigger(1.0)
def code():
    process_alarms()
    allow_vassals_to_join_indoor_battle()
    process_kingdom_parties_ai()
simple_trigger35.codeBlock = code


simple_trigger36 = SimpleTrigger(3.0)
def code():
    cur_hours_001 = store_current_hours()
    for p_002 in range(p.town_1, p.village_1):
        party_slot_003 = party_get_slot(p_002,54)
        if party_slot_003 > 0 and party_is_active(party_slot_003):
            party_faction_004 = store_faction_of_party(party_slot_003)
            if party_slot_ge(p_002,54,1):
                party_slot_005 = party_get_slot(p_002,64)
                party_slot_005 = cur_hours_001 - party_slot_005
                var006 = 0
                var007 = 0
                var008 = 0
                var009 = 0
                for trp_010 in range(trp.npc1, trp.knight_1_1_wife):
                    if troop_slot_eq(trp_010,2,2) and not troop_slot_ge(trp_010,8,0):
                        troop_slot_011 = troop_get_slot(trp_010,10)
                        if troop_slot_011 > 0 and party_is_active(troop_slot_011):
                            troop_faction_012 = store_faction_of_troop(trp_010)
                            if troop_faction_012 == party_faction_004:
                                var013 = 0
                                if party_slot_eq(troop_slot_011,4,1) and party_slot_eq(troop_slot_011,5,p_002):
                                    var013 = 1
                                elif party_slot_eq(troop_slot_011,4,11):
                                    party_slot_014 = party_get_slot(troop_slot_011,5)
                                    if party_slot_014 > 0 and party_is_active(party_slot_014) and party_slot_eq(party_slot_014,4,1) and party_slot_eq(party_slot_014,5,p_002):
                                        var013 = 1
                                    #end
                                #end
                            #end
                        #end
                    #end
                #end
            #end
            if var013 == 1:
                party_battle_opponent_015 = party_get_battle_opponent(troop_slot_011)
                if party_battle_opponent_015 >= 0 or party_battle_opponent_015 == p_002:
                    if faction_slot_eq(party_faction_004,8,trp_010):
                        var009 = 1
                    #end
                #end
            #end
            party_calculate_regular_strength(troop_slot_011)
            var008 += reg0
        #end
        if var008 > 0:
            party_collect_attachments_to_party(p_002,p.collective_enemy)
            party_calculate_regular_strength(p.collective_enemy)
            var016 = reg0
            if _auto_enter_town == p_002 and _g_player_is_captive == 0:
                party_calculate_regular_strength(p.main_party)
                var016 += reg0
                var008 *= 2
            #end
            party_slot_017 = party_get_slot(p_002,65)
            party_slot_017 += 100
            var016 *= party_slot_017
            var016 /= 100
            val_max(var016,1)
            if var009 == 1 and party_faction_004 == _players_kingdom and check_quest_active(qst.follow_army):
                var008 *= 2
            #end
            var018 = var008 * 100
            var018 /= var016
            var019 = var018 - 250
            if var019 > -100:
                var020 = party_slot_005 / 2
                var019 += var020
            #end
            var019 /= 5
            val_max(var019,0)
            var021 = 175 - var018
            val_max(var021,0)
            if True:
                random_x_022 = store_random_in_range(0,100)
                if random_x_022 < var019 and party_slot_005 > 24:
                    var006 = 1
                else:
                    random_x_022 = store_random_in_range(0,100)
                    if random_x_022 < var021:
                        var007 = 1
                    #end
                #end
            #end
        else:
            var007 = 1
        #end
        if var006 == 1:
            begin_assault_on_center(p_002)
        elif var007 == 1:
            for trp_010 in range(trp.npc1, trp.knight_1_1_wife):
                if troop_slot_eq(trp_010,2,2) and not troop_slot_ge(trp_010,8,0):
                    troop_slot_011 = troop_get_slot(trp_010,10)
                    if troop_slot_011 > 0 and party_is_active(troop_slot_011) and party_slot_eq(troop_slot_011,4,1) and party_slot_eq(troop_slot_011,5,p_002) and party_slot_eq(troop_slot_011,8,1):
                        party_set_ai_state(troop_slot_011,-1,-1)
                        party_set_ai_state(troop_slot_011,1,p_002)
                        party_set_slot(p_002,64,cur_hours_001)
                    #end
                #end
            #end
        #end
    #end
simple_trigger36.codeBlock = code


simple_trigger37 = SimpleTrigger(6.0)
def code():
    _g_recalculate_ais = 1
simple_trigger37.codeBlock = code


simple_trigger38 = SimpleTrigger(0.0)
def code():
    if _cheat_mode >= 1:
        for trp_001 in range(trp.kingdom_1_lord, trp.knight_1_1):
            var002 = trp_001 + fac.kingdom_1
            var002 = var002 - trp.kingdom_1_lord
            troop_faction_003 = store_faction_of_troop(trp_001)
            if var002 != troop_faction_003 and troop_faction_003 != fac.commoners and _cheat_mode >= 2 and trp_001 != trp.kingdom_2_lord:
                s4 = str_store_troop_name(trp_001)
                s5 = str_store_faction_name(troop_faction_003)
                s6 = str_store_faction_name(var002)
                s65 = str_store_string("@{!}DEBUG - {s4} is in {s5};;; should be in {s6};;; disabling political cheat mode")
                rest_for_hours(0,0,0)
                jump_to_menu(mnu.debug_alert_from_s65)
            #end
        #end
    #end
    if _g_recalculate_ais == 1:
        _g_recalculate_ais = 0
        recalculate_ais()
simple_trigger38.codeBlock = code


simple_trigger39 = SimpleTrigger(24.0)
def code():
    for fac_001 in range(fac.player_supporters_faction, fac.kingdoms_end):
        faction_recalculate_strength(fac_001)
    #end
    for trp_002 in range(trp.npc1, trp.knight_1_1_wife):
        troop_faction_003 = store_faction_of_troop(trp_002)
        if not faction_slot_eq(troop_faction_003,4,0) and not faction_slot_eq(troop_faction_003,4,6) and not faction_slot_eq(troop_faction_003,4,1):
            troop_slot_004 = troop_get_slot(trp_002,10)
            if party_is_active(troop_slot_004):
                _total_vassal_days_on_campaign += 1
                if party_slot_eq(troop_slot_004,4,11):
                    _total_vassal_days_responding_to_campaign += 1
                #end
            #end
        #end
    #end
simple_trigger39.codeBlock = code


simple_trigger40 = SimpleTrigger(36.0)
def code():
    for trp_001 in range(trp.npc1, trp.heroes_end):
        troop_set_slot(trp_001,20,0)
    #end
    for trp_001 in range(trp.village_1_elder, trp.merchants_end):
        troop_set_slot(trp_001,20,0)
    #end
simple_trigger40.codeBlock = code


simple_trigger41 = SimpleTrigger(168.0)
def code():
    for p_001 in range(p.village_1, p.salt_mine):
        refresh_village_merchant_inventory(p_001)
    #end
simple_trigger41.codeBlock = code


simple_trigger42 = SimpleTrigger(48.0)
def code():
    for p_001 in range(p.village_1, p.salt_mine):
        refresh_village_defenders(p_001)
        party_set_slot(p_001,46,0)
    #end
simple_trigger42.codeBlock = code


simple_trigger43 = SimpleTrigger(168.0)
def code():
    for p_001 in range(p.town_1, p.salt_mine):
        if not is_between(p_001,p.castle_1,p.village_1):
            party_slot_002 = party_get_slot(p_001,205)
            party_slot_003 = party_get_slot(p_001,206)
            party_slot_004 = party_get_slot(p_001,208)
            val_max(party_slot_004,1)
            var005 = party_slot_002 * 400
            var006 = party_slot_003 * 200
            var005 += var006
            var005 /= party_slot_004
            random_x_007 = store_random_in_range(0,100)
            if random_x_007 == 0:
                val_min(party_slot_002,10)
            elif var005 > 100:
                party_slot_003 *= 90
                party_slot_003 /= 100
                party_slot_002 *= 90
                party_slot_002 /= 100
            elif var005 < 30:
                party_slot_002 *= 120
                party_slot_002 /= 100
                party_slot_002 += 1
                party_slot_003 *= 120
                party_slot_003 /= 100
                party_slot_003 += 1
            elif var005 < 60:
                party_slot_002 *= 110
                party_slot_002 /= 100
                party_slot_002 += 1
                party_slot_003 *= 110
                party_slot_003 /= 100
                party_slot_003 += 1
            elif var005 < 100 and random_x_007 < 50:
                party_slot_002 *= 105
                party_slot_002 /= 100
                if party_slot_002 <= 20:
                    party_slot_002 += 1
                #end
            #end
            party_slot_003 *= 105
            party_slot_003 /= 100
            if party_slot_003 <= 20:
                party_slot_003 += 1
            #end
        #end
        party_set_slot(p_001,205,party_slot_002)
        party_set_slot(p_001,206,party_slot_003)
    #end
simple_trigger43.codeBlock = code


simple_trigger44 = SimpleTrigger(168.0)
def code():
    for p_001 in range(p.town_1, p.salt_mine):
        if party_slot_ge(p_001,7,0):
            party_slot_002 = party_get_slot(p_001,47)
            var003 = 0
            if party_slot_eq(p_001,0,4):
                if party_slot_eq(p_001,35,0):
                    var003 = 1200
                #end
            elif party_slot_eq(p_001,0,2):
                var003 = 1200
            elif party_slot_eq(p_001,0,3):
                var003 = 2400
            #end
            party_slot_004 = party_get_slot(p_001,50)
            var005 = 20 + party_slot_004
            var003 *= var005
            var003 /= 120
            if party_slot_eq(p_001,7,trp.player):
                campaign_ai = game_get_reduce_campaign_ai()
                if campaign_ai == 0:
                    var003 *= 3
                    var003 /= 4
                elif campaign_ai == 1:
                    pass
                elif campaign_ai == 2:
                    var003 *= 4
                    var003 /= 3
                #end
            #end
            party_slot_002 += var003
            party_set_slot(p_001,47,party_slot_002)
        #end
        if is_between(p_001,p.village_1,p.salt_mine):
            party_slot_007 = party_get_slot(p_001,120)
            if party_slot_ge(party_slot_007,7,0) and is_between(party_slot_007,p.castle_1,p.village_1):
                party_slot_002 = party_get_slot(party_slot_007,47)
                party_slot_002 += var003
                party_set_slot(party_slot_007,47,party_slot_002)
            #end
        #end
    #end
simple_trigger44.codeBlock = code


simple_trigger45 = SimpleTrigger(32.0)
def code():
    if _players_kingdom == 0 and _g_invite_faction <= 0 and _g_player_is_captive == 0:
        troop_type_001 = troop_get_type(trp.player)
        if troop_type_001 == 1 and _npc_with_sisterly_advice == 0:
            for trp_002 in range(trp.npc1, trp.kingdom_1_lord):
                if main_party_has_troop(trp_002):
                    troop_type_003 = troop_get_type(trp_002)
                    if troop_type_003 == 1 and troop_slot_ge(trp.player,7,150) and troop_slot_ge(trp_002,139,1):
                        _npc_with_sisterly_advice = trp_002
                    #end
                #end
            #end
        #end
    else:
        random_x_004 = store_random_in_range(fac.kingdom_1,fac.kingdoms_end)
        var005 = 999999
        for p_006 in range(p.town_1, p.village_1):
            party_faction_007 = store_faction_of_party(p_006)
            if party_faction_007 == random_x_004:
                distance_parties_008 = store_distance_to_party_from_party(p.main_party,p_006)
                val_min(var005,distance_parties_008)
            #end
        #end
        if var005 < 30:
            faction_relation_009 = store_relation(random_x_004,fac.player_supporters_faction)
            faction_slot_010 = faction_get_slot(random_x_004,11)
            troop_get_player_relation(faction_slot_010)
            var011 = reg0
            get_number_of_hero_centers(trp.player)
            var012 = reg0
            if _g_infinite_camping == 0:
                party_size_wo_prisoners_013 = 0
                if p.main_party >= 0:
                    party_size_wo_prisoners_013 = store_party_size_wo_prisoners(p.main_party)
                #end
            #end
        #end
        if var012 == 0:
            troop_slot_014 = troop_get_slot(trp.player,7)
            if troop_slot_014 >= 160 and faction_relation_009 >= 0 and var011 >= 0 and party_size_wo_prisoners_013 >= 45:
                random_x_015 = store_random_in_range(0,100)
                if random_x_015 < 50:
                    get_poorest_village_of_faction(random_x_004)
                    _g_invite_offered_center = reg0
                    if _g_invite_offered_center >= 0:
                        _g_invite_faction = random_x_004
                        jump_to_menu(mnu.invite_player_to_faction)
                    elif var012 > 0 and _players_oath_renounced_against_kingdom != random_x_004 and faction_relation_009 >= -40 and var011 >= -20 and party_size_wo_prisoners_013 >= 30:
                        random_x_015 = store_random_in_range(0,100)
                        if random_x_015 < 20:
                            _g_invite_faction = random_x_004
                            _g_invite_offered_center = -1
                            jump_to_menu(mnu.invite_player_to_faction_without_center)
                        #end
                    #end
                #end
            #end
        #end
    #end
simple_trigger45.codeBlock = code


simple_trigger46 = SimpleTrigger(168.0)
def code():
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        random_x_002 = store_random_in_range(0,9999)
        troop_set_slot(trp_001,49,random_x_002)
    #end
simple_trigger46.codeBlock = code


simple_trigger47 = SimpleTrigger(0.1)
def code():
    for trp_001 in range(trp.npc1, trp.heroes_end):
        if troop_slot_eq(trp_001,2,2):
            troop_slot_002 = troop_get_slot(trp_001,10)
            if troop_slot_002 >= 1 and party_is_active(troop_slot_002):
                party_attached_003 = party_get_attached_to(troop_slot_002)
                if party_attached_003 < 1:
                    party_cur_town_004 = party_get_cur_town(troop_slot_002)
                    if is_between(party_cur_town_004,p.town_1,p.salt_mine):
                        get_relation_between_parties(party_cur_town_004,troop_slot_002)
                        if reg0 >= 0:
                            party_attach_to_party(troop_slot_002,party_cur_town_004)
                        else:
                            party_set_ai_behavior(troop_slot_002,0)
                        #end
                    #end
                #end
            #end
        #end
        if party_slot_eq(party_cur_town_004,0,3) or party_slot_eq(party_cur_town_004,0,2):
            party_faction_005 = store_faction_of_party(troop_slot_002)
            party_faction_006 = store_faction_of_party(party_cur_town_004)
            if party_faction_005 == party_faction_006:
                party_num_prisoners_stacks_007 = party_get_num_prisoner_stacks(troop_slot_002)
                if party_num_prisoners_stacks_007 > 0:
                    _g_move_heroes = 1
                    party_prisoners_add_party_prisoners(party_cur_town_004,troop_slot_002)
                    _g_move_heroes = 1
                    party_remove_all_prisoners(troop_slot_002)
                #end
            #end
        #end
    #end
    for cur_party in __all_parties__:
        if cur_party > p.spawn_points_end:
            party_template_id_009 = party_get_template_id(cur_party)
            if party_template_id_009 >= pt.steppe_bandit_lair:
                distance_parties_010 = store_distance_to_party_from_party(p.main_party,cur_party)
                if distance_parties_010 < 3:
                    party_set_flags(cur_party,256,0)
                    party_set_flags(cur_party,16384,1)
                #end
            #end
        #end
    #end
simple_trigger47.codeBlock = code


simple_trigger48 = SimpleTrigger(48.0)
def code():
    randomly_make_prisoner_heroes_escape_from_party(p.main_party,50)
    for p_001 in range(p.town_1, p.village_1):
        var002 = 30
        if party_slot_eq(p_001,135,1):
            var002 = 5
        #end
        randomly_make_prisoner_heroes_escape_from_party(p_001,var002)
    #end
simple_trigger48.codeBlock = code


simple_trigger49 = SimpleTrigger(48.0)
def code():
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        if troop_slot_eq(trp_001,2,2):
            s1 = str_store_troop_name(trp_001)
            if not troop_slot_ge(trp_001,8,0) and not troop_slot_ge(trp_001,10,1):
                troop_faction_002 = store_faction_of_troop(trp_001)
                if troop_faction_002 == fac.outlaws:
                    pass
                else:
                    if _cheat_mode == 2:
                        s4 = str_store_troop_name(trp_001)
                        print(gstr.debug__attempting_to_spawn_s4)
                    #end
                #end
            #end
            if cf_select_random_walled_center_with_faction_and_owner_priority_no_siege(troop_faction_002,trp_001):
                var003 = reg0
                if _cheat_mode == 2:
                    s7 = str_store_party_name(var003)
                    s0 = str_store_troop_name(trp_001)
                    print(gstr.debug__s0_is_spawning_around_party__s7)
                #end
            #end
            create_kingdom_hero_party(trp_001,var003)
            if _g_there_is_no_avaliable_centers == 0:
                party_attach_to_party(_pout_party,var003)
            #end
            troop_slot_004 = troop_get_slot(trp_001,10)
            party_set_ai_state(troop_slot_004,7,var003)
        elif not faction_slot_eq(troop_faction_002,21,0):
            if is_between(trp_001,trp.kingdom_1_lord,trp.knight_1_1):
                troop_set_slot(trp_001,55,fac.commoners)
            else:
                random_x_005 = store_random_in_range(0,100)
                if random_x_005 < 10 and cf_get_random_active_faction_except_player_faction_and_faction(troop_faction_002):
                    troop_set_slot(trp_001,55,reg0)
                #end
            #end
        #end
    #end
simple_trigger49.codeBlock = code


simple_trigger50 = SimpleTrigger(24.0)
def code():
    for p_001 in range(p.village_1, p.salt_mine):
        if party_slot_eq(p_001,35,0):
            party_slot_002 = party_get_slot(p_001,122)
            if party_slot_002 == 0 or not party_is_active(party_slot_002):
                random_x_003 = store_random_in_range(0,100)
                if random_x_003 < 60:
                    create_village_farmer_party(p_001)
                    party_set_slot(p_001,122,reg0)
                #end
            #end
        #end
    #end
simple_trigger50.codeBlock = code


simple_trigger51 = SimpleTrigger(72.0)
def code():
    update_trade_good_prices()
    for p_001 in range(p.town_1, p.salt_mine):
        party_slot_002 = party_get_slot(p_001,51)
        if party_slot_002 > 1000:
            party_slot_002 *= 95
            party_slot_002 /= 100
            val_max(party_slot_002,1000)
        elif party_slot_002 < 1000:
            party_slot_002 *= 105
            party_slot_002 /= 100
            val_min(party_slot_002,1000)
        #end
        party_set_slot(p_001,51,party_slot_002)
    #end
simple_trigger51.codeBlock = code


simple_trigger52 = SimpleTrigger(8.0)
def code():
    for cur_party in __all_parties__:
        if party_slot_eq(cur_party,0,11) and party_is_in_any_town(cur_party):
            party_faction_002 = store_faction_of_party(cur_party)
            faction_slot_003 = faction_get_slot(party_faction_002,82)
            if faction_slot_003 <= 0:
                remove_party(cur_party)
            else:
                party_cur_town_004 = party_get_cur_town(cur_party)
                random_x_005 = store_random_in_range(0,100)
                if party_slot_eq(party_cur_town_004,7,trp.player):
                    campaign_ai = game_get_reduce_campaign_ai()
                    if campaign_ai == 0:
                        var007 = 35
                    elif campaign_ai == 1:
                        var007 = 45
                    elif campaign_ai == 2:
                        var007 = 60
                    #end
                else:
                    var007 = 45
                #end
            #end
            if random_x_005 < var007:
                var008 = 1
                if is_between(party_cur_town_004,p.town_1,p.village_1) and not party_slot_eq(party_cur_town_004,54,-1):
                    var008 = 0
                #end
            #end
            if var008 == 1:
                var009 = 0
                if True:
                    party_slot_010 = party_get_slot(cur_party,4)
                    if party_slot_010 == 13:
                        party_slot_011 = party_get_slot(cur_party,5)
                        if party_cur_town_004 == party_slot_011:
                            var009 = 1
                        #end
                    #end
                #end
            #end
            var012 = -1
            if _caravan_escort_party_id == cur_party and not party_is_in_town(cur_party,_caravan_escort_destination_town):
                var012 = _caravan_escort_destination_town
            elif cf_select_most_profitable_town_at_peace_with_faction_in_trade_route(party_cur_town_004,party_faction_002):
                var012 = reg0
            #end
            if is_between(var012,p.town_1,p.castle_1) and not party_is_in_town(cur_party,var012):
                if var009 == 1:
                    s7 = str_store_party_name(party_cur_town_004)
                    do_merchant_town_trade(cur_party,party_cur_town_004)
                #end
            #end
            party_set_ai_behavior(cur_party,1)
            party_set_ai_object(cur_party,var012)
            party_set_flags(cur_party,65536,0)
            party_set_slot(cur_party,4,13)
            party_set_slot(cur_party,5,var012)
        #end
    #end
simple_trigger52.codeBlock = code


simple_trigger53 = SimpleTrigger(8.0)
def code():
    for cur_party in __all_parties__:
        if party_slot_eq(cur_party,0,15) and party_is_in_any_town(cur_party):
            party_slot_002 = party_get_slot(cur_party,123)
            party_cur_town_003 = party_get_cur_town(cur_party)
            var004 = 1
            if is_between(party_cur_town_003,p.town_1,p.village_1) and not party_slot_eq(party_cur_town_003,54,-1):
                var004 = 0
            #end
        #end
        if var004 == 1:
            if party_cur_town_003 == party_slot_002:
                do_party_center_trade(cur_party,party_slot_002,3)
                party_faction_005 = store_faction_of_party(party_cur_town_003)
                party_set_faction(cur_party,party_faction_005)
                party_slot_006 = party_get_slot(party_slot_002,121)
                party_set_slot(cur_party,5,party_slot_006)
                party_set_slot(cur_party,4,13)
                party_set_ai_behavior(cur_party,1)
                party_set_ai_object(cur_party,party_slot_006)
            else:
                if True:
                    party_slot_007 = party_get_slot(cur_party,5)
                    if party_cur_town_003 == party_slot_007:
                        do_party_center_trade(cur_party,party_slot_007,3)
                        var008 = reg0
                        party_slot_009 = party_get_slot(party_slot_007,48)
                        party_slot_010 = party_get_slot(party_slot_007,50)
                        var011 = var008
                        var011 *= party_slot_010
                        var011 /= 100
                        var011 /= 20
                        party_slot_009 += var011
                        if _cheat_mode >= 3:
                            reg4 = var011
                            s4 = str_store_party_name(party_slot_007)
                            reg5 = party_slot_009
                            print("@{!}New tariffs at {s4} = {reg4};;; total = {reg5}")
                        #end
                    #end
                #end
                party_set_slot(party_slot_007,48,party_slot_009)
                party_slot_012 = party_get_slot(party_slot_007,53)
                center_get_food_store_limit(party_slot_007)
                var013 = reg0
                party_slot_012 += 1000
                val_min(party_slot_012,var013)
                party_set_slot(party_slot_007,53,party_slot_012)
                if True:
                    random_x_014 = store_random_in_range(0,100)
                    if random_x_014 < 5:
                        change_center_prosperity(party_slot_002,1)
                        _newglob_total_prosperity_from_village_trade += 1
                    #end
                #end
            #end
            party_set_slot(cur_party,5,party_slot_002)
            party_set_slot(cur_party,4,13)
            party_set_ai_behavior(cur_party,1)
            party_set_ai_object(cur_party,party_slot_002)
        #end
    #end
simple_trigger53.codeBlock = code


simple_trigger54 = SimpleTrigger(2.0)
def code():
    for p_001 in range(p.castle_1, p.village_1):
        if party_slot_eq(p_001,54,-1):
            party_slot_002 = party_get_slot(p_001,53)
            party_slot_002 += 100
            center_get_food_store_limit(p_001)
            var003 = reg0
            val_min(party_slot_002,var003)
            party_set_slot(p_001,53,party_slot_002)
        #end
    #end
simple_trigger54.codeBlock = code


simple_trigger55 = SimpleTrigger(0.5)
def code():
    for trp_001 in range(trp.npc1, trp.heroes_end):
        if troop_slot_eq(trp_001,2,2):
            troop_slot_002 = troop_get_slot(trp_001,10)
            if troop_slot_002 > 0:
                if party_is_active(troop_slot_002):
                    if True:
                        cur_party_ai_behavior_003 = get_party_ai_current_behavior(troop_slot_002)
                        if cur_party_ai_behavior_003 == 5:
                            var004 = 1
                            if troop_slot_eq(trp_001,52,7) or troop_slot_eq(trp_001,52,1):
                                cur_party_ai_object_005 = get_party_ai_current_object(troop_slot_002)
                                if party_is_active(cur_party_ai_object_005):
                                    party_battle_opponent_006 = party_get_battle_opponent(cur_party_ai_object_005)
                                    if party_is_active(party_battle_opponent_006):
                                        var004 = 0
                                    #end
                                #end
                            #end
                        #end
                    #end
                #end
                if var004 == 1:
                    party_faction_007 = store_faction_of_party(troop_slot_002)
                    party_slot_008 = party_get_slot(troop_slot_002,30)
                    faction_slot_009 = faction_get_slot(party_faction_007,8)
                    if faction_slot_009 != trp_001:
                        var004 = 1
                        if faction_slot_009 >= 0:
                            troop_slot_010 = troop_get_slot(faction_slot_009,10)
                            if party_is_active(troop_slot_010,0) and party_slot_008 == troop_slot_010:
                                var004 = 0
                            #end
                        #end
                    #end
                #end
                if var004 == 1:
                    var011 = 0
                    for p_012 in range(p.town_1, p.village_1):
                        if var011 == 0 and party_slot_eq(p_012,54,-1):
                            party_faction_013 = store_faction_of_party(p_012)
                            faction_relation_014 = store_relation(party_faction_013,party_faction_007)
                            if faction_relation_014 > 0:
                                distance_parties_015 = store_distance_to_party_from_party(troop_slot_002,p_012)
                                if distance_parties_015 < 20:
                                    pos1 = party_get_position(troop_slot_002)
                                    pos2 = party_get_position(p_012)
                                    if not position_is_behind_position(2,1):
                                        party_set_ai_state(troop_slot_002,14,p_012)
                                        var011 = 1
                                    #end
                                #end
                            #end
                        #end
                    #end
                #end
            #end
        else:
            troop_set_slot(trp_001,10,-1)
        #end
    #end
simple_trigger55.codeBlock = code


simple_trigger56 = SimpleTrigger(0.5)
def code():
    cur_hours_001 = store_current_hours()
    var002 = store_mod(cur_hours_001,11)
    var003 = cur_hours_001 - 5
    party_num_companions_004 = party_get_num_companions(p.main_party)
    party_num_prisioners_005 = party_get_num_prisoners(p.main_party)
    party_num_companions_004 += party_num_prisioners_005
    convert_to_fixed_point(party_num_companions_004)
    var006 = store_sqrt(party_num_companions_004)
    convert_from_fixed_point(var006)
    if var002 == 0:
        for fac_007 in range(fac.player_supporters_faction, fac.kingdoms_end):
            faction_slot_008 = faction_get_slot(fac_007,30)
            faction_slot_008 -= 1
            val_max(faction_slot_008,0)
            faction_set_slot(fac_007,30,faction_slot_008)
        #end
    #end
    if _g_player_is_captive == 0:
        for p_009 in range(p.town_1, p.salt_mine):
            fac_007 = store_faction_of_party(p_009)
            faction_relation_010 = store_relation(fac_007,fac.player_supporters_faction)
            if faction_relation_010 < 0:
                distance_parties_011 = store_distance_to_party_from_party(p.main_party,p_009)
                if distance_parties_011 < 5:
                    var012 = distance_parties_011 * distance_parties_011
                    var013 = 20 - var012
                    var014 = 20 - faction_relation_010
                    var015 = var013 * var014
                    var015 *= var006
                    var016 = var015 / 10
                    random_x_017 = store_random_in_range(0,1000)
                    if random_x_017 < var016:
                        faction_slot_008 = faction_get_slot(fac_007,30)
                        faction_slot_008 += 1
                        val_min(faction_slot_008,100)
                        faction_set_slot(fac_007,30,faction_slot_008)
                        if not party_slot_ge(p_009,42,var003):
                            s1 = str_store_party_name_link(p_009)
                            print("@Your party is spotted by {s1}.")
                            party_set_slot(p_009,42,cur_hours_001)
                        #end
                    #end
                #end
            #end
        #end
    #end
simple_trigger56.codeBlock = code


simple_trigger57 = SimpleTrigger(14.0)
def code():
    if _g_player_is_captive == 0:
        party_num_companions_stacks_001 = party_get_num_companion_stacks(p.main_party)
        var002 = 0
        for var003 in range(0, party_num_companions_stacks_001):
            party_stack_size_004 = party_stack_get_size(p.main_party,var003)
            var002 += party_stack_size_004
        #end
    #end
    var002 /= 3
    if var002 == 0:
        var002 += 1
    #end
    if True:
        var005 = 0
        for itm_006 in range(itm.smoked_fish, itm.siege_supply):
            if cf_player_has_item_without_modifier(itm_006,41):
                var005 += 1
            #end
        #end
        if var005 >= 6:
            unlock_achievement(36)
        #end
    #end
    var007 = var002
    var008 = 0
    for var009 in range(0, var007):
        var010 = 0
        for itm_011 in range(itm.smoked_fish, itm.siege_supply):
            item_set_slot(itm_011,0,0)
            if cf_player_has_item_without_modifier(itm_011,41):
                var010 += 1
            #end
        #end
        if var010 > 0:
            random_x_012 = store_random_in_range(0,var010)
            consume_food(random_x_012)
        elif var008 == 0:
            print("@Party has nothing to eat!",16711680)
            change_player_party_morale(-3)
            var008 = 1
            if True:
                party_count_fit_regulars(p.main_party)
                if reg0 > 0:
                    objectionable_action(2,gstr.men_hungry)
                #end
            #end
        #end
    #end
simple_trigger57.codeBlock = code


simple_trigger58 = SimpleTrigger(24.0)
def code():
    troop_inv_slot_003_list1 = [
    itm.pork,
    itm.chicken,
    itm.cattle_meat,
    ]
    troop_inv_capacity_001 = troop_get_inventory_capacity(trp.player)
    for inventory_slot_no_002 in range(0, troop_inv_capacity_001):
        troop_inv_slot_003 = troop_get_inventory_slot(trp.player,inventory_slot_no_002)
        if troop_inv_slot_003 in troop_inv_slot_003_list1:
            troop_inv_slot_modifier_004 = troop_get_inventory_slot_modifier(trp.player,inventory_slot_no_002)
            if troop_inv_slot_modifier_004 >= 37 and troop_inv_slot_modifier_004 < 41:
                troop_inv_slot_modifier_004 += 1
                troop_set_inventory_slot_modifier(trp.player,inventory_slot_no_002,troop_inv_slot_modifier_004)
            elif troop_inv_slot_modifier_004 < 37:
                troop_set_inventory_slot_modifier(trp.player,inventory_slot_no_002,37)
            #end
        #end
    #end
simple_trigger58.codeBlock = code


simple_trigger59 = SimpleTrigger(72.0)
def code():
    pass
simple_trigger59.codeBlock = code


simple_trigger60 = SimpleTrigger(0.0)
def code():
    troop_inv_slot_001 = troop_get_inventory_slot(trp.player,8)
    var002 = -1
    if _g_player_icon_state == 0:
        if troop_inv_slot_001 >= 0:
            var002 = 1297036692682702849
        else:
            var002 = 1297036692682702848
        #end
    elif _g_player_icon_state == 1:
        var002 = 1297036692682702875
    elif _g_player_icon_state == 2:
        var002 = 1297036692682702876
    #end
    if var002 != _g_player_party_icon:
        _g_player_party_icon = var002
        party_set_icon(p.main_party,var002)
simple_trigger60.codeBlock = code


simple_trigger61 = SimpleTrigger(2.0)
def code():
    troop_gold_001 = store_troop_gold(trp.player)
    var002 = troop_gold_001 / 100
    troop_inv_capacity_003 = troop_get_inventory_capacity(trp.player)
    for inventory_slot_no_004 in range(0, troop_inv_capacity_003):
        troop_inv_slot_005 = troop_get_inventory_slot(trp.player,inventory_slot_no_004)
        if troop_inv_slot_005 >= 0:
            if is_between(troop_inv_slot_005,itm.spice,itm.siege_supply):
                item_value_006 = store_item_value(troop_inv_slot_005)
                troop_gold_001 += item_value_006
            #end
        #end
    #end
    val_clamp(var002,0,100)
    party_set_bandit_attraction(p.main_party,var002)
simple_trigger61.codeBlock = code


simple_trigger62 = SimpleTrigger(3.0)
def code():
    for p_001 in range(p.town_1, p.village_1):
        if faction_slot_eq(fac.player_supporters_faction,21,2):
            party_faction_002 = store_faction_of_party(p_001)
            if party_faction_002 == fac.player_supporters_faction:
                activate_player_faction(trp.player)
            #end
        #end
    #end
simple_trigger62.codeBlock = code


simple_trigger63 = SimpleTrigger(6.0)
def code():
    if _g_prisoner_recruit_troop_id > 0 and _g_prisoner_recruit_size > 0 and _g_prisoner_recruit_last_time > 0 and is_currently_night():
        if True:
            skill_lvl_001 = store_skill_level(skl.leadership,trp.player)
            skill_lvl_001 *= 5
            var002 = 66 - skill_lvl_001
            if var002 > 0:
                var003 = 0
                for var004 in range(0, _g_prisoner_recruit_size):
                    random_x_005 = store_random_in_range(0,100)
                    if random_x_005 < var002:
                        var003 += 1
                    #end
                #end
            #end
        #end
        party_remove_members(p.main_party,_g_prisoner_recruit_troop_id,var003)
        var003 = reg0
        if var003 > 0:
            if var003 > 1:
                reg2 = 1
            else:
                reg2 = 0
            #end
        #end
        reg1 = var003
        s1 = str_store_troop_name_by_count(_g_prisoner_recruit_troop_id,var003)
        display_log_message("@{reg1} {s1} {reg2?have:has} escaped from your party during the night.")
    #end
    _g_prisoner_recruit_troop_id = 0
    _g_prisoner_recruit_size = 0
simple_trigger63.codeBlock = code


simple_trigger64 = SimpleTrigger(24.0)
def code():
    if _g_ransom_offer_rejected != 1:
        offer_ransom_amount_to_player_for_prisoners_in_party(p.main_party)
        if reg0 == 0:
            var001 = p.village_1
            for var002 in range(p.town_1, var001):
                if party_slot_eq(var002,7,trp.player):
                    offer_ransom_amount_to_player_for_prisoners_in_party(var002)
                    if reg0 == 1:
                        var001 = 0
                    #end
                #end
            #end
        #end
    #end
simple_trigger64.codeBlock = code


simple_trigger65 = SimpleTrigger(72.0)
def code():
    _g_ransom_offer_rejected = 0
    for p_001 in range(p.town_1, p.village_1):
        party_slot_002 = party_get_slot(p_001,7)
        if party_slot_002 > 0:
            party_num_prisoners_stacks_003 = party_get_num_prisoner_stacks(p_001)
            for var004 in range(0, party_num_prisoners_stacks_003):
                party_prisoner_troop_id_005 = party_prisoner_stack_get_troop_id(p_001,var004)
                if troop_is_hero(party_prisoner_troop_id_005) and troop_slot_eq(party_prisoner_troop_id_005,2,2):
                    random_x_006 = store_random_in_range(0,100)
                    if random_x_006 <= 10:
                        calculate_ransom_amount_for_troop(party_prisoner_troop_id_005)
                        var007 = reg0
                        troop_slot_008 = troop_get_slot(party_slot_002,11)
                        troop_slot_008 += var007
                        troop_set_slot(party_slot_002,11,troop_slot_008)
                        party_remove_prisoners(p_001,party_prisoner_troop_id_005,1)
                        remove_troop_from_prison(party_prisoner_troop_id_005)
                        troop_faction_009 = store_faction_of_troop(party_slot_002)
                        troop_faction_010 = store_faction_of_troop(party_prisoner_troop_id_005)
                        s1 = str_store_troop_name(party_prisoner_troop_id_005)
                        s2 = str_store_faction_name(troop_faction_009)
                        s3 = str_store_faction_name(troop_faction_010)
                        display_log_message("@{s1} of {s3} has been released from captivity.")
                    #end
                #end
            #end
        #end
    #end
simple_trigger65.codeBlock = code


simple_trigger66 = SimpleTrigger(72.0)
def code():
    update_mercenary_units_of_towns()
    update_ransom_brokers()
    update_tavern_travellers()
    update_tavern_minstrels()
    update_booksellers()
    update_villages_infested_by_bandits()
    for p_001 in range(p.village_1, p.salt_mine):
        update_volunteer_troops_in_village(p_001)
        update_npc_volunteer_troops_in_village(p_001)
    #end
simple_trigger66.codeBlock = code


simple_trigger67 = SimpleTrigger(24.0)
def code():
    update_other_taverngoers()
simple_trigger67.codeBlock = code


simple_trigger68 = SimpleTrigger(36.0)
def code():
    for p_001 in range(p.town_1, p.salt_mine):
        if party_slot_eq(p_001,0,3) or party_slot_eq(p_001,0,4):
            center_remove_walker_type_from_walkers(p_001,1)
            center_remove_walker_type_from_walkers(p_001,2)
            random_x_002 = store_random_in_range(0,100)
            if random_x_002 < 70 and not party_slot_ge(p_001,50,60) and cf_center_get_free_walker(p_001):
                center_set_walker_to_type(p_001,reg0,1)
            #end
        #end
    #end
simple_trigger68.codeBlock = code


simple_trigger69 = SimpleTrigger(12.0)
def code():
    for p_001 in range(p.town_1, p.salt_mine):
        party_slot_002 = party_get_slot(p_001,124)
        if party_slot_002 > 0:
            party_slot_003 = party_get_slot(p_001,125)
            cur_hours_004 = store_current_hours()
            if cur_hours_004 >= party_slot_003:
                party_set_slot(p_001,party_slot_002,1)
                party_set_slot(p_001,124,0)
                get_improvement_details(party_slot_002)
                if party_slot_eq(p_001,7,trp.player):
                    s4 = str_store_party_name(p_001)
                    display_log_message("@Building of {s0} in {s4} has been completed.")
                #end
            #end
        #end
        if is_between(p_001,p.village_1,p.salt_mine) and party_slot_002 == 131:
            change_center_prosperity(p_001,5)
        #end
    #end
simple_trigger69.codeBlock = code


simple_trigger70 = SimpleTrigger(24.0)
def code():
    var001 = 0
    for p_002 in range(p.town_1, p.castle_1):
        party_slot_003 = party_get_slot(p_002,156)
        if party_slot_003 == 1:
            fill_tournament_participants_troop(p_002,0)
            sort_tournament_participant_troops()
            get_num_tournament_participants()
            var004 = reg0 - 1
            remove_tournament_participants_randomly(var004)
            sort_tournament_participant_troops()
            troop_slot_005 = troop_get_slot(trp.tournament_participants,0)
            if is_between(troop_slot_005,trp.npc1,trp.knight_1_1_wife):
                s1 = str_store_troop_name_link(troop_slot_005)
                s2 = str_store_party_name_link(p_002)
                print("@{s1} has won the tournament at {s2}.")
                change_troop_renown(troop_slot_005,20)
            #end
        #end
        party_slot_003 -= 1
        val_max(party_slot_003,0)
        party_set_slot(p_002,156,party_slot_003)
        if party_slot_003 > 0:
            var001 += 1
        #end
    #end
    for p_002 in range(p.town_1, p.salt_mine):
        if party_slot_eq(p_002,0,3) or party_slot_eq(p_002,0,4):
            party_slot_006 = party_get_slot(p_002,155)
            if party_slot_006 <= 0:
                var007 = 0
                if check_quest_active(qst.deal_with_night_bandits) and quest_slot_eq(qst.deal_with_night_bandits,1,p_002) and not check_quest_succeeded(qst.deal_with_night_bandits):
                    var007 = 1
                else:
                    random_x_008 = store_random_in_range(0,100)
                    if random_x_008 < 3:
                        var007 = 1
                    #end
                #end
            #end
            if var007 == 1:
                random_x_008 = store_random_in_range(0,3)
                if random_x_008 == 0:
                    var009 = trp.bandit
                elif random_x_008 == 1:
                    var009 = trp.mountain_bandit
                else:
                    var009 = trp.forest_bandit
                #end
                party_set_slot(p_002,155,var009)
                if _cheat_mode == 1:
                    s1 = str_store_party_name(p_002)
                    print("@{!}{s1} is infested by bandits [[[at night]]].")
                #end
            #end
        else:
            if True:
                var010 = 40
                if party_slot_eq(p_002,0,3):
                    var010 = 20
                #end
                random_x_008 = store_random_in_range(0,100)
                if random_x_008 < var010:
                    party_set_slot(p_002,155,0)
                    if _cheat_mode == 1:
                        s1 = str_store_party_name(p_002)
                        print("@{s1} is no longer infested by bandits [[[at night]]].")
                    #end
                #end
            #end
        #end
    #end
    for fac_011 in range(fac.player_supporters_faction, fac.kingdoms_end):
        if faction_slot_eq(fac_011,4,6):
            faction_slot_012 = faction_get_slot(fac_011,5)
            if is_between(faction_slot_012,p.town_1,p.castle_1) and party_slot_ge(faction_slot_012,156,1):
                party_set_slot(faction_slot_012,156,2)
            #end
        #end
    #end
    if var001 < 3:
        random_x_008 = store_random_in_range(0,100)
        if random_x_008 < 30:
            random_x_013 = store_random_in_range(p.town_1,p.castle_1)
            random_x_014 = store_random_in_range(12,15)
            party_set_slot(random_x_013,156,random_x_014)
            if _cheat_mode == 1:
                s1 = str_store_party_name(random_x_013)
                print("@{!}{s1} is holding a tournament.")
            #end
        #end
    #end
simple_trigger70.codeBlock = code


simple_trigger71 = SimpleTrigger(3.0)
def code():
    _g_player_tournament_placement = 0
simple_trigger71.codeBlock = code


simple_trigger72 = SimpleTrigger(8.0)
def code():
    pass
simple_trigger72.codeBlock = code


simple_trigger73 = SimpleTrigger(1.0)
def code():
    if not map_free() and is_currently_night() and is_between(_g_last_rest_center,p.town_1,p.salt_mine) and not party_slot_eq(_g_last_rest_center,7,trp.player):
        party_faction_001 = store_faction_of_party(_g_last_rest_center)
        if party_faction_001 != fac.player_supporters_faction:
            cur_hours_002 = store_current_hours()
            if cur_hours_002 >= _g_last_rest_payment_until:
                _g_last_rest_payment_until = cur_hours_002 + 24
                troop_gold_003 = store_troop_gold(trp.player)
                party_num_companions_004 = party_get_num_companions(p.main_party)
                gold_005 = party_num_companions_004 / 4
                gold_005 += 1
                if troop_gold_003 >= gold_005:
                    print("@You pay for accommodation.")
                    troop_remove_gold(trp.player,gold_005)
                elif troop_gold_003 > 0:
                    troop_remove_gold(trp.player,troop_gold_003)
                #end
            #end
        #end
    #end
simple_trigger73.codeBlock = code


simple_trigger74 = SimpleTrigger(36.0)
def code():
    spawn_bandits()
simple_trigger74.codeBlock = code


simple_trigger75 = SimpleTrigger(24.0)
def code():
    update_party_creation_random_limits()
simple_trigger75.codeBlock = code


simple_trigger76 = SimpleTrigger(24.0)
def code():
    var001 = 0
    for fac_002 in range(fac.player_supporters_faction, fac.kingdoms_end):
        faction_set_slot(fac_002,20,0)
    #end
    for cur_party in __all_parties__:
        party_faction_004 = store_faction_of_party(cur_party)
        if is_between(party_faction_004,fac.player_supporters_faction,fac.kingdoms_end) and is_between(cur_party,p.town_1,p.salt_mine) or party_slot_eq(cur_party,0,13):
            faction_slot_005 = faction_get_slot(party_faction_004,20)
            faction_slot_005 += 1
            faction_set_slot(party_faction_004,20,faction_slot_005)
        #end
    #end
    for fac_002 in range(fac.player_supporters_faction, fac.kingdoms_end):
        if faction_slot_eq(fac_002,21,0):
            var001 += 1
            if faction_slot_eq(fac_002,20,0):
                var006 = 0
                if fac_002 == fac.player_supporters_faction:
                    if _supported_pretender <= 0:
                        faction_set_slot(fac_002,21,2)
                        var006 = 1
                    #end
                #end
            #end
        elif _players_kingdom != fac_002:
            faction_set_slot(fac_002,21,1)
            for cur_party in __all_parties__:
                party_faction_004 = store_faction_of_party(cur_party)
                if party_faction_004 == fac_002:
                    party_slot_007 = party_get_slot(cur_party,123)
                    party_faction_008 = store_faction_of_party(party_slot_007)
                    party_set_faction(cur_party,party_faction_008)
                #end
            #end
            troop_id_009 = -1
            for trp_010 in range(trp.kingdom_1_pretender, trp.knight_1_1_wife):
                if troop_slot_eq(trp_010,14,fac_002):
                    troop_id_009 = trp_010
                #end
            #end
            if is_between(troop_id_009,trp.kingdom_1_pretender,trp.knight_1_1_wife) and troop_id_009 != _supported_pretender:
                troop_set_slot(troop_id_009,12,0)
            #end
            var006 = 1
            if _players_oath_renounced_against_kingdom == fac_002:
                _players_oath_renounced_against_kingdom = 0
                _players_oath_renounced_given_center = 0
                _players_oath_renounced_begin_time = 0
                add_notification_menu(mnu.notification_oath_renounced_faction_defeated,fac_002,0)
            #end
            add_notification_menu(mnu.notification_faction_defeated,fac_002,0)
        #end
        if var006 == 1:
            var001 -= 1
        #end
        for fac_011 in range(fac.player_supporters_faction, fac.kingdoms_end):
            update_faction_notes(fac_011)
        #end
    #end
    if var001 == 1 and _g_one_faction_left_notification_shown == 0:
        _g_one_faction_left_notification_shown = 1
        for fac_002 in range(fac.player_supporters_faction, fac.kingdoms_end):
            if faction_slot_eq(fac_002,21,0):
                add_notification_menu(mnu.notification_one_faction_left,fac_002,0)
            #end
        #end
    #end
simple_trigger76.codeBlock = code


simple_trigger77 = SimpleTrigger(3.0)
def code():
    if is_between(_g_player_court,p.town_1,p.salt_mine):
        party_faction_001 = store_faction_of_party(_g_player_court)
        if party_faction_001 != fac.player_supporters_faction:
            add_notification_menu(mnu.notification_court_lost,0,0)
        elif _g_player_court < p.town_1 and faction_slot_eq(fac.player_supporters_faction,11,trp.player) or _g_player_minister > 0:
            var002 = 0
            for p_003 in range(p.town_1, p.village_1):
                if var002 == 0:
                    party_faction_001 = store_faction_of_party(p_003)
                    if party_faction_001 == fac.player_supporters_faction:
                        var002 = p_003
                    #end
                #end
            #end
        #end
        if var002 >= 1:
            add_notification_menu(mnu.notification_court_lost,0,0)
        #end
    #end
    for cur_party in __all_parties__:
        if cur_party > p.spawn_points_end:
            party_template_id_005 = party_get_template_id(cur_party)
            if is_between(party_template_id_005,pt.steppe_bandits,pt.deserters):
                party_template_slot_006 = party_template_get_slot(party_template_id_005,4)
                if party_template_slot_006 > p.spawn_points_end:
                    distance_parties_007 = store_distance_to_party_from_party(cur_party,party_template_slot_006)
                    if distance_parties_007 > 30:
                        party_set_ai_behavior(cur_party,6)
                        pos5 = party_get_position(party_template_slot_006)
                        party_set_ai_target_position(cur_party,5)
                    else:
                        party_ai_behavior_008 = get_party_ai_behavior(cur_party)
                        if party_ai_behavior_008 == 6:
                            if party_template_slot_006 > p.spawn_points_end:
                                distance_parties_007 = store_distance_to_party_from_party(cur_party,party_template_slot_006)
                                if distance_parties_007 < 3:
                                    party_set_ai_behavior(cur_party,3)
                                    party_template_slot_009 = party_template_get_slot(party_template_id_005,5)
                                    party_set_ai_object(cur_party,party_template_slot_009)
                                    party_set_ai_patrol_radius(cur_party,45)
                                elif party_template_slot_006 < p.spawn_points_end:
                                    party_set_ai_behavior(cur_party,3)
                                    party_template_slot_009 = party_template_get_slot(party_template_id_005,5)
                                    party_set_ai_object(cur_party,party_template_slot_009)
                                    party_set_ai_patrol_radius(cur_party,45)
                                #end
                            #end
                        #end
                    #end
                #end
            #end
        #end
    #end
    if True:
        troop_slot_010 = troop_get_slot(trp.player,34)
        if troop_slot_010 > 0 and not check_quest_active(qst.wed_betrothed) and not check_quest_active(qst.wed_betrothed_female):
            s5 = str_store_troop_name(troop_slot_010)
            print("@Betrothal to {s5} expires")
            troop_set_slot(trp.player,34,-1)
            troop_set_slot(troop_slot_010,34,-1)
        #end
    #end
simple_trigger77.codeBlock = code


simple_trigger78 = SimpleTrigger(168.0)
def code():
    troop_slot_001 = troop_get_slot(trp.player,7)
    var002 = troop_slot_001 / 200
    troop_slot_001 -= var002
    troop_set_slot(trp.player,7,troop_slot_001)
simple_trigger78.codeBlock = code


simple_trigger79 = SimpleTrigger(1.0)
def code():
    if not map_free() and _g_player_reading_book > 0 and player_has_item(_g_player_reading_book):
        attribute_lvl_001 = store_attribute_level(trp.player,2)
        item_slot_002 = item_get_slot(_g_player_reading_book,4)
        if item_slot_002 <= attribute_lvl_001:
            item_slot_003 = item_get_slot(_g_player_reading_book,2)
            item_slot_004 = item_get_slot(_g_player_reading_book,3)
            if item_slot_004 == 0:
                item_slot_003 += 7
                item_set_slot(_g_player_reading_book,2,item_slot_003)
                if item_slot_003 >= 1000:
                    item_set_slot(_g_player_reading_book,3,1)
                    s1 = str_store_item_name(_g_player_reading_book)
                    str_clear(2)
                    if _g_player_reading_book == itm.book_tactics:
                        troop_raise_skill(trp.player,skl.tactics,1)
                        s2 = str_store_string("@ Your tactics skill has increased by 1.")
                    elif _g_player_reading_book == itm.book_persuasion:
                        troop_raise_skill(trp.player,skl.persuasion,1)
                        s2 = str_store_string("@ Your persuasion skill has increased by 1.")
                    elif _g_player_reading_book == itm.book_leadership:
                        troop_raise_skill(trp.player,skl.leadership,1)
                        s2 = str_store_string("@ Your leadership skill has increased by 1.")
                    elif _g_player_reading_book == itm.book_intelligence:
                        troop_raise_attribute(trp.player,2,1)
                        s2 = str_store_string("@ Your intelligence has increased by 1.")
                    elif _g_player_reading_book == itm.book_trade:
                        troop_raise_skill(trp.player,skl.trade,1)
                        s2 = str_store_string("@ Your trade skill has increased by 1.")
                    elif _g_player_reading_book == itm.book_weapon_mastery:
                        troop_raise_skill(trp.player,skl.weapon_master,1)
                        s2 = str_store_string("@ Your weapon master skill has increased by 1.")
                    elif _g_player_reading_book == itm.book_engineering:
                        troop_raise_skill(trp.player,skl.engineer,1)
                        s2 = str_store_string("@ Your engineer skill has increased by 1.")
                    #end
                #end
            #end
        #end
    #end
    unlock_achievement(37)
    if _g_infinite_camping == 0:
        dialog_box("@You have finished reading {s1}.{s2}","@Book Read")
    #end
    _g_player_reading_book = 0
simple_trigger79.codeBlock = code


simple_trigger80 = SimpleTrigger(12.0)
def code():
    for cur_party in __all_parties__:
        if party_slot_eq(cur_party,0,17):
            distance_parties_002 = store_distance_to_party_from_party(cur_party,p.main_party)
            if distance_parties_002 > 30:
                remove_party(cur_party)
                if check_quest_active(qst.move_cattle_herd) and not check_quest_concluded(qst.move_cattle_herd) and quest_slot_eq(qst.move_cattle_herd,8,cur_party):
                    fail_quest(qst.move_cattle_herd)
                #end
            #end
        elif distance_parties_002 > 10:
            party_set_slot(cur_party,7,0)
            party_set_ai_behavior(cur_party,0)
        #end
    #end
simple_trigger80.codeBlock = code


simple_trigger81 = SimpleTrigger(720.0)
def code():
    for p_001 in range(p.village_1, p.salt_mine):
        if party_slot_eq(p_001,7,trp.player) and party_slot_eq(p_001,133,1):
            party_slot_002 = party_get_slot(p_001,26)
            party_slot_002 += 1
            val_min(party_slot_002,100)
            party_set_slot(p_001,26,party_slot_002)
        #end
    #end
simple_trigger81.codeBlock = code


simple_trigger82 = SimpleTrigger(24.0)
def code():
    for quest_id_001 in range(0, qst.quests_end):
        if check_quest_active(quest_id_001):
            if not check_quest_concluded(quest_id_001) and quest_slot_ge(quest_id_001,23,1):
                quest_slot_002 = quest_get_slot(quest_id_001,23)
                quest_slot_002 -= 1
                if quest_slot_002 == 0:
                    abort_quest(quest_id_001,1)
                else:
                    quest_set_slot(quest_id_001,23,quest_slot_002)
                    reg0 = quest_slot_002
                    add_quest_note_from_sreg(quest_id_001,7,"@You have {reg0} days to finish this quest.",0)
                #end
            #end
        elif quest_slot_ge(quest_id_001,25,1):
            quest_slot_003 = quest_get_slot(quest_id_001,25)
            quest_slot_003 -= 1
            quest_set_slot(quest_id_001,25,quest_slot_003)
        #end
    #end
simple_trigger82.codeBlock = code


simple_trigger83 = SimpleTrigger(2.0)
def code():
    if _g_infinite_camping == 0 and is_between(_players_kingdom,fac.player_supporters_faction,fac.kingdoms_end) and _g_player_is_captive == 0:
        if check_quest_active(qst.report_to_army) and faction_slot_eq(_players_kingdom,8,-1):
            abort_quest(qst.report_to_army,0)
        #end
    #end
    faction_slot_001 = faction_get_slot(_players_kingdom,5)
    if not faction_slot_eq(_players_kingdom,4,0) and not faction_slot_eq(_players_kingdom,4,6):
        var002 = 1
        if faction_slot_eq(_players_kingdom,4,5) or faction_slot_eq(_players_kingdom,4,2) or faction_slot_eq(_players_kingdom,4,3) and not is_between(faction_slot_001,p.town_1,p.village_1):
            var002 = 0
        #end
    #end
    if var002 == 1:
        var003 = 0
        for fac_004 in range(fac.player_supporters_faction, fac.kingdoms_end):
            if fac_004 != _players_kingdom:
                faction_relation_005 = store_relation(fac_004,_players_kingdom)
                if faction_relation_005 < 0:
                    var003 = 1
                #end
            #end
        #end
    #end
    if var003 == 1 and not check_quest_active(qst.report_to_army) and not check_quest_active(qst.follow_army) and not quest_slot_ge(qst.report_to_army,25,1):
        faction_slot_006 = faction_get_slot(_players_kingdom,8)
        if faction_slot_006 > 0:
            troop_slot_007 = troop_get_slot(faction_slot_006,10)
            if troop_slot_007 > 0 and party_is_active(troop_slot_007):
                distance_parties_008 = store_distance_to_party_from_party(troop_slot_007,p.main_party)
                if distance_parties_008 <= 96:
                    var009 = 1
                    for qst_010 in range(qst.deliver_message, qst.follow_army):
                        if check_quest_active(qst_010) and quest_slot_eq(qst_010,6,faction_slot_006):
                            var009 = 0
                        #end
                    #end
                #end
            #end
        #end
    #end
    if var009 == 1:
        for qst_010 in range(qst.destroy_bandit_lair, qst.blank_quest_2):
            if check_quest_active(qst_010) and quest_slot_eq(qst_010,6,faction_slot_006):
                var009 = 0
            #end
        #end
    #end
    if var009 == 1:
        for qst_010 in range(qst.deliver_cattle_to_army, qst.rescue_lord_by_replace):
            if check_quest_active(qst_010):
                var009 = 0
            #end
        #end
    #end
    if var009 == 1:
        character_lvl_011 = store_character_level(trp.player)
        if character_lvl_011 >= 8:
            var012 = 2
            for p_013 in range(p.town_1, p.salt_mine):
                if party_slot_eq(p_013,7,trp.player):
                    if party_slot_eq(p_013,0,3):
                        var012 += 3
                    elif party_slot_eq(p_013,0,2):
                        var012 += 1
                    else:
                        var012 += 1
                    #end
                #end
            #end
        #end
    #end
    var012 *= 4
    val_min(var012,60)
    quest_set_slot(qst.report_to_army,6,faction_slot_006)
    quest_set_slot(qst.report_to_army,2,faction_slot_006)
    quest_set_slot(qst.report_to_army,10,var012)
    quest_set_slot(qst.report_to_army,23,4)
    quest_set_slot(qst.report_to_army,24,22)
    jump_to_menu(mnu.kingdom_army_quest_report_to_army)
simple_trigger83.codeBlock = code


simple_trigger84 = SimpleTrigger(3.0)
def code():
    _g_random_army_quest = -1
    if check_quest_active(qst.follow_army,1) and is_between(_players_kingdom,fac.player_supporters_faction,fac.kingdoms_end) and not faction_slot_eq(_players_kingdom,4,0):
        faction_slot_001 = faction_get_slot(_players_kingdom,8)
        if faction_slot_001 != trp.player and faction_slot_001 > 0:
            troop_slot_002 = troop_get_slot(faction_slot_001,10)
            if troop_slot_002 > 0 and party_is_active(troop_slot_002):
                distance_parties_003 = store_distance_to_party_from_party(troop_slot_002,p.main_party)
                if distance_parties_003 < 15:
                    _g_player_follow_army_warnings = 0
                    cur_hours_004 = store_current_hours()
                    faction_slot_005 = faction_get_slot(_players_kingdom,95)
                    var006 = cur_hours_004 - faction_slot_005
                    quest_id_007 = -1
                    if True:
                        random_x_008 = store_random_in_range(0,100)
                        if random_x_008 < 30 and troop_slot_eq(faction_slot_001,20,0):
                            for var009 in range(0, 20):
                                if quest_id_007 == -1:
                                    random_x_010 = store_random_in_range(qst.deliver_cattle_to_army,qst.rescue_lord_by_replace)
                                    if not quest_slot_ge(random_x_010,25,1):
                                        if random_x_010 == qst.deliver_cattle_to_army:
                                            if faction_slot_eq(_players_kingdom,4,2) and var006 > 120:
                                                random_x_011 = store_random_in_range(5,10)
                                                quest_id_007 = qst.deliver_cattle_to_army
                                                quest_set_slot(quest_id_007,10,random_x_011)
                                                quest_set_slot(quest_id_007,23,10)
                                                quest_set_slot(quest_id_007,24,30)
                                            #end
                                        #end
                                    #end
                                #end
                            #end
                        #end
                    #end
                elif random_x_010 == qst.join_siege_with_army and 1 == 0:
                    if faction_slot_eq(_players_kingdom,4,2):
                        faction_slot_012 = faction_get_slot(_players_kingdom,5)
                        if is_between(faction_slot_012,p.town_1,p.village_1):
                            party_battle_opponent_013 = party_get_battle_opponent(troop_slot_002)
                            if party_battle_opponent_013 == faction_slot_012:
                                quest_id_007 = random_x_010
                                quest_set_slot(quest_id_007,1,faction_slot_012)
                                quest_set_slot(quest_id_007,23,2)
                                quest_set_slot(quest_id_007,24,15)
                            #end
                        #end
                    #end
                elif random_x_010 == qst.scout_waypoints:
                    if True:
                        var014 = 100
                        _qst_scout_waypoints_wp_1 = -1
                        _qst_scout_waypoints_wp_2 = -1
                        _qst_scout_waypoints_wp_3 = -1
                        var015 = 0
                        for var009 in range(0, var014):
                            if _qst_scout_waypoints_wp_1 < 0 and cf_get_random_enemy_center_within_range(troop_slot_002,50):
                                _qst_scout_waypoints_wp_1 = reg0
                            #end
                            if _qst_scout_waypoints_wp_2 < 0 and cf_get_random_enemy_center_within_range(troop_slot_002,50) and _qst_scout_waypoints_wp_1 != reg0:
                                _qst_scout_waypoints_wp_2 = reg0
                            #end
                            if _qst_scout_waypoints_wp_3 < 0 and cf_get_random_enemy_center_within_range(troop_slot_002,50) and _qst_scout_waypoints_wp_1 != reg0 and _qst_scout_waypoints_wp_2 != reg0:
                                _qst_scout_waypoints_wp_3 = reg0
                            #end
                            if _qst_scout_waypoints_wp_1 != _qst_scout_waypoints_wp_2 and _qst_scout_waypoints_wp_1 != _qst_scout_waypoints_wp_2 and _qst_scout_waypoints_wp_2 != _qst_scout_waypoints_wp_3 and _qst_scout_waypoints_wp_1 >= 0 and _qst_scout_waypoints_wp_2 >= 0 and _qst_scout_waypoints_wp_3 >= 0:
                                var014 = 0
                                var015 = 1
                            #end
                        #end
                        if var015 == 1:
                            _qst_scout_waypoints_wp_1_visited = 0
                            _qst_scout_waypoints_wp_2_visited = 0
                            _qst_scout_waypoints_wp_3_visited = 0
                            quest_id_007 = qst.scout_waypoints
                            quest_set_slot(quest_id_007,23,7)
                            quest_set_slot(quest_id_007,24,25)
                        #end
                    #end
                #end
            #end
            if quest_id_007 != -1:
                quest_set_slot(quest_id_007,11,0)
                quest_set_slot(quest_id_007,6,faction_slot_001)
                if quest_id_007 == qst.join_siege_with_army:
                    jump_to_menu(mnu.kingdom_army_quest_join_siege_order)
                else:
                    _g_random_army_quest = quest_id_007
                    quest_set_slot(_g_random_army_quest,6,faction_slot_001)
                    jump_to_menu(mnu.kingdom_army_quest_messenger)
                #end
            #end
        #end
    else:
        _g_player_follow_army_warnings += 1
        if _g_player_follow_army_warnings < 15:
            if True:
                var016 = store_mod(_g_player_follow_army_warnings,3)
                if var016 == 0:
                    s1 = str_store_troop_name_link(faction_slot_001)
                    if _g_player_follow_army_warnings < 8:
                        pass
                    else:
                        print(gstr.marshal_warning)
                    #end
                #end
            #end
        else:
            jump_to_menu(mnu.kingdom_army_follow_failed)
        #end
    #end
simple_trigger84.codeBlock = code


simple_trigger85 = SimpleTrigger(0.5)
def code():
    if check_quest_active(qst.move_cattle_herd) and not check_quest_concluded(qst.move_cattle_herd):
        quest_slot_001 = quest_get_slot(qst.move_cattle_herd,8)
        quest_slot_002 = quest_get_slot(qst.move_cattle_herd,1)
        distance_parties_003 = store_distance_to_party_from_party(quest_slot_001,quest_slot_002)
        if distance_parties_003 < 3:
            remove_party(quest_slot_001)
            succeed_quest(qst.move_cattle_herd)
simple_trigger85.codeBlock = code


simple_trigger86 = SimpleTrigger(2.0)
def code():
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        if troop_slot_eq(trp_001,2,2):
            troop_slot_002 = troop_get_slot(trp_001,10)
            if troop_slot_002 >= 1 and party_is_active(troop_slot_002) and party_slot_eq(troop_slot_002,31,1):
                cur_hours_003 = store_current_hours()
                if not party_slot_ge(troop_slot_002,32,cur_hours_003):
                    party_set_slot(troop_slot_002,30,-1)
                    party_set_slot(troop_slot_002,31,0)
                    var004 = 200
                    var005 = cur_hours_003 + var004
                    party_set_slot(troop_slot_002,33,var005)
                #end
            #end
        #end
    #end
simple_trigger86.codeBlock = code


simple_trigger87 = SimpleTrigger(0.5)
def code():
    if check_quest_active(qst.deliver_cattle) and not check_quest_succeeded(qst.deliver_cattle):
        quest_slot_001 = quest_get_slot(qst.deliver_cattle,1)
        quest_slot_002 = quest_get_slot(qst.deliver_cattle,10)
        quest_slot_003 = quest_get_slot(qst.deliver_cattle,11)
        var004 = quest_slot_002 - quest_slot_003
        remove_cattles_if_herd_is_close_to_party(quest_slot_001,var004)
        quest_slot_003 += reg0
        quest_set_slot(qst.deliver_cattle,11,quest_slot_003)
        if quest_slot_002 <= quest_slot_003:
            succeed_quest(qst.deliver_cattle)
        #end
    #end
    if check_quest_active(qst.deliver_cattle_to_army) and not check_quest_succeeded(qst.deliver_cattle_to_army):
        quest_slot_005 = quest_get_slot(qst.deliver_cattle_to_army,6)
        troop_slot_006 = troop_get_slot(quest_slot_005,10)
        if troop_slot_006 > 0:
            quest_slot_002 = quest_get_slot(qst.deliver_cattle_to_army,10)
            quest_slot_003 = quest_get_slot(qst.deliver_cattle_to_army,11)
            var004 = quest_slot_002 - quest_slot_003
            remove_cattles_if_herd_is_close_to_party(troop_slot_006,var004)
            quest_slot_003 += reg0
            quest_set_slot(qst.deliver_cattle_to_army,11,quest_slot_003)
            if quest_slot_002 <= quest_slot_003:
                succeed_quest(qst.deliver_cattle_to_army)
            #end
        else:
            abort_quest(qst.deliver_cattle_to_army,0)
        #end
    #end
simple_trigger87.codeBlock = code


simple_trigger88 = SimpleTrigger(1.0)
def code():
    if not map_free() and check_quest_active(qst.train_peasants_against_bandits) and not check_quest_concluded(qst.train_peasants_against_bandits) and _qst_train_peasants_against_bandits_currently_training == 1:
        _qst_train_peasants_against_bandits_num_hours_trained += 1
        get_max_skill_of_player_party(skl.trainer)
        var001 = reg0
        var002 = 20 - var001
        var002 *= 3
        var002 /= 5
        if _qst_train_peasants_against_bandits_num_hours_trained >= var002:
            _qst_train_peasants_against_bandits_num_hours_trained = 0
            rest_for_hours(0,0,0)
            jump_to_menu(mnu.train_peasants_against_bandits_ready)
simple_trigger88.codeBlock = code


simple_trigger89 = SimpleTrigger(1.0)
def code():
    if check_quest_active(qst.scout_waypoints) and not check_quest_succeeded(qst.scout_waypoints):
        if _qst_scout_waypoints_wp_1_visited == 0:
            distance_parties_001 = store_distance_to_party_from_party(_qst_scout_waypoints_wp_1,p.main_party)
            if distance_parties_001 <= 3:
                _qst_scout_waypoints_wp_1_visited = 1
                s1 = str_store_party_name_link(_qst_scout_waypoints_wp_1)
                print("@{s1} is scouted.")
            #end
        #end
    #end
    if _qst_scout_waypoints_wp_2_visited == 0:
        distance_parties_001 = store_distance_to_party_from_party(_qst_scout_waypoints_wp_2,p.main_party)
        if distance_parties_001 <= 3:
            _qst_scout_waypoints_wp_2_visited = 1
            s1 = str_store_party_name_link(_qst_scout_waypoints_wp_2)
            print("@{s1} is scouted.")
        #end
    #end
    if _qst_scout_waypoints_wp_3_visited == 0:
        distance_parties_001 = store_distance_to_party_from_party(_qst_scout_waypoints_wp_3,p.main_party)
        if distance_parties_001 <= 3:
            _qst_scout_waypoints_wp_3_visited = 1
            s1 = str_store_party_name_link(_qst_scout_waypoints_wp_3)
            print("@{s1} is scouted.")
        #end
    #end
    if _qst_scout_waypoints_wp_1_visited == 1 and _qst_scout_waypoints_wp_2_visited == 1 and _qst_scout_waypoints_wp_3_visited == 1:
        succeed_quest(qst.scout_waypoints)
simple_trigger89.codeBlock = code


simple_trigger90 = SimpleTrigger(3.0)
def code():
    if not map_free() and check_quest_active(qst.kill_local_merchant) and quest_slot_eq(qst.kill_local_merchant,11,0):
        quest_set_slot(qst.kill_local_merchant,11,1)
        rest_for_hours(0,0,0)
        _auto_enter_town = _qst_kill_local_merchant_center
        _quest_auto_menu = mnu.kill_local_merchant_begin
simple_trigger90.codeBlock = code


simple_trigger91 = SimpleTrigger(1.0)
def code():
    quest_slot_001_list1 = [
    3,
    2,
    1,
    ]
    if not map_free() and check_quest_active(qst.collect_taxes) and _g_player_is_captive == 0 and _qst_collect_taxes_currently_collecting == 1:
        quest_slot_001 = quest_get_slot(qst.collect_taxes,11)
        if quest_slot_001 in quest_slot_001_list1:
            quest_slot_002 = quest_get_slot(qst.collect_taxes,10)
            quest_slot_002 -= 1
            quest_set_slot(qst.collect_taxes,10,quest_slot_002)
            get_max_skill_of_player_party(skl.trade)
            if quest_slot_002 < 0:
                quest_slot_001 = 4
                quest_set_slot(qst.collect_taxes,11,4)
                rest_for_hours(0,0,0)
                jump_to_menu(mnu.collect_taxes_complete)
            else:
                var003 = _qst_collect_taxes_hourly_income
                party_slot_004 = party_get_slot(_g_encountered_party,50)
                var005 = 30 + party_slot_004
                var003 *= var005
                var003 /= 80
                if _qst_collect_taxes_halve_taxes == 1:
                    var003 /= 2
                #end
            #end
        #end
        val_max(var003,2)
        random_x_006 = store_random_in_range(1,var003)
        quest_slot_007 = quest_get_slot(qst.collect_taxes,22)
        quest_slot_007 += random_x_006
        quest_set_slot(qst.collect_taxes,22,quest_slot_007)
        troop_add_gold(trp.player,random_x_006)
    #end
    if quest_slot_001 == 1:
        _qst_collect_taxes_menu_counter -= 1
        if _qst_collect_taxes_menu_counter <= 0:
            quest_set_slot(qst.collect_taxes,11,2)
            jump_to_menu(mnu.collect_taxes_revolt_warning)
        elif quest_slot_001 == 2:
            _qst_collect_taxes_unrest_counter -= 1
            if _qst_collect_taxes_unrest_counter <= 0 and _qst_collect_taxes_halve_taxes == 0:
                quest_set_slot(qst.collect_taxes,11,3)
                var008 = 10000 / _qst_collect_taxes_total_hours
                var008 += 30
                random_x_009 = store_random_in_range(0,1000)
                if random_x_009 < var008:
                    jump_to_menu(mnu.collect_taxes_revolt)
                #end
            #end
        #end
    #end
simple_trigger91.codeBlock = code


simple_trigger92 = SimpleTrigger(72.0)
def code():
    if _g_force_peace_faction_1 > 0 and _g_force_peace_faction_2 > 0:
        if True:
            faction_relation_001 = store_relation(_g_force_peace_faction_1,_g_force_peace_faction_2)
            if faction_relation_001 < 0:
                diplomacy_start_peace_between_kingdoms(_g_force_peace_faction_1,_g_force_peace_faction_2,1)
            #end
        #end
    #end
    _g_force_peace_faction_1 = 0
    _g_force_peace_faction_2 = 0
simple_trigger92.codeBlock = code


simple_trigger93 = SimpleTrigger(1.0)
def code():
    s51 = str_store_string(gstr.no_trigger_noted)
    if _npc_to_rejoin_party > 0 and _g_infinite_camping == 0:
        if not main_party_has_troop(_npc_to_rejoin_party) and _g_player_is_captive != 1:
            s51 = str_store_string(gstr.triggered_by_npc_to_rejoin_party)
            _npc_map_talk_context = 150
            start_map_conversation(_npc_to_rejoin_party,-1)
        else:
            troop_set_slot(_npc_to_rejoin_party,151,8)
            _npc_to_rejoin_party = 0
        #end
    elif _npc_is_quitting > 0 and _g_infinite_camping == 0:
        if main_party_has_troop(_npc_is_quitting) and _g_player_is_captive != 1:
            s51 = str_store_string(gstr.triggered_by_npc_is_quitting)
            start_map_conversation(_npc_is_quitting,-1)
        else:
            _npc_is_quitting = 0
        #end
    elif _npc_with_grievance > 0 and _g_infinite_camping == 0 and _disable_npc_complaints == 0:
        if main_party_has_troop(_npc_with_grievance) and _g_player_is_captive != 1:
            s51 = str_store_string(gstr.triggered_by_npc_has_grievance)
            _npc_map_talk_context = 61
            start_map_conversation(_npc_with_grievance,-1)
        else:
            _npc_with_grievance = 0
        #end
    elif _npc_with_personality_clash > 0 and _g_infinite_camping == 0 and _disable_npc_complaints == 0:
        troop_slot_001 = troop_get_slot(_npc_with_personality_clash,71)
        if main_party_has_troop(_npc_with_personality_clash) and main_party_has_troop(troop_slot_001) and _g_player_is_captive != 1:
            _npc_map_talk_context = 72
            s51 = str_store_string(gstr.triggered_by_npc_has_personality_clash)
            start_map_conversation(_npc_with_personality_clash,-1)
        else:
            _npc_with_personality_clash = 0
        #end
    elif _npc_with_political_grievance > 0 and _g_infinite_camping == 0 and _disable_npc_complaints == 0:
        if main_party_has_troop(_npc_with_political_grievance) and _g_player_is_captive != 1:
            s51 = str_store_string(gstr.triggered_by_npc_has_political_grievance)
            _npc_map_talk_context = 145
            start_map_conversation(_npc_with_political_grievance,-1)
        else:
            _npc_with_political_grievance = 0
        #end
    elif _disable_sisterly_advice == 0 and _g_infinite_camping == 0 and _npc_with_sisterly_advice > 0:
        if main_party_has_troop(_npc_with_sisterly_advice) and _g_player_is_captive != 1:
            _npc_map_talk_context = 139
            start_map_conversation(_npc_with_sisterly_advice,-1)
        else:
            _npc_with_sisterly_advice = 0
        #end
    elif _disable_local_histories == 0 and _g_infinite_camping == 0:
        for trp_002 in range(trp.npc1, trp.kingdom_1_lord):
            if main_party_has_troop(trp_002) and troop_slot_eq(trp_002,78,0):
                troop_slot_003 = troop_get_slot(trp_002,60)
                if troop_slot_003 > 0:
                    distance_parties_004 = store_distance_to_party_from_party(troop_slot_003,p.main_party)
                    if distance_parties_004 < 7:
                        _npc_map_talk_context = 60
                        s51 = str_store_string(gstr.triggered_by_local_histories)
                        start_map_conversation(trp_002,-1)
                    #end
                #end
            #end
        #end
    #end
    if check_quest_active(qst.rebel_against_kingdom) and is_between(_supported_pretender,trp.kingdom_1_pretender,trp.knight_1_1_wife) and not main_party_has_troop(_supported_pretender) and not troop_slot_eq(_supported_pretender,2,2):
        party_add_members(p.main_party,_supported_pretender,1)
    #end
    if check_quest_active(qst.rebel_against_kingdom) and is_between(_supported_pretender,trp.kingdom_1_pretender,trp.knight_1_1_wife) and main_party_has_troop(_supported_pretender) and not faction_slot_eq(fac.player_supporters_faction,8,trp.player):
        appoint_faction_marshall(fac.player_supporters_faction,trp.player)
    #end
simple_trigger93.codeBlock = code


simple_trigger94 = SimpleTrigger(4.0)
def code():
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        if troop_slot_ge(trp_001,55,1):
            troop_faction_002 = store_faction_of_troop(trp_001)
            troop_slot_003 = troop_get_slot(trp_001,55)
            troop_slot_004 = troop_get_slot(trp_001,10)
            var005 = 0
            if troop_slot_004 <= 0 and not troop_slot_ge(trp_001,8,0):
                var005 = 1
            elif troop_slot_004 > 0:
                party_attached_006 = party_get_attached_to(troop_slot_004)
                if party_attached_006 < 0:
                    party_attached_006 = party_get_cur_town(troop_slot_004)
                #end
            #end
            if is_between(party_attached_006,p.town_1,p.salt_mine) or party_slot_eq(party_attached_006,7,trp_001):
                var007 = trp.knight_1_1_wife
                for troop_id_008 in range(trp.npc1, var007):
                    if troop_slot_eq(troop_id_008,2,2):
                        troop_slot_009 = troop_get_slot(troop_id_008,10)
                        if party_is_active(troop_slot_009):
                            party_faction_010 = store_faction_of_party(troop_slot_009)
                            if party_faction_010 == troop_faction_002:
                                distance_parties_011 = store_distance_to_party_from_party(troop_slot_004,troop_slot_009)
                                if distance_parties_011 < 4:
                                    var007 = 0
                                #end
                            #end
                        #end
                    #end
                #end
            #end
            if var007 != 0:
                var005 = 1
            #end
        #end
        if var005 == 1:
            if _cheat_mode >= 1:
                s4 = str_store_troop_name(trp_001)
                print("@{!}DEBUG - {s4} faction changed from slot troop change to faction")
            #end
        #end
        change_troop_faction(trp_001,troop_slot_003)
        troop_set_slot(trp_001,55,0)
        if is_between(troop_slot_003,fac.player_supporters_faction,fac.kingdoms_end):
            s1 = str_store_troop_name_link(trp_001)
            s2 = str_store_faction_name_link(troop_faction_002)
            s3 = str_store_faction_name_link(troop_slot_003)
            print("@{s1} has switched from {s2} to {s3}.")
            if troop_faction_002 == _players_kingdom:
                add_notification_menu(mnu.notification_troop_left_players_faction,trp_001,troop_slot_003)
            elif troop_slot_003 == _players_kingdom:
                add_notification_menu(mnu.notification_troop_joined_players_faction,trp_001,troop_faction_002)
            #end
        #end
    #end
simple_trigger94.codeBlock = code


simple_trigger95 = SimpleTrigger(1.0)
def code():
    if _cheat_mode == 1:
        for p_001 in range(p.town_1, p.salt_mine):
            party_battle_opponent_002 = party_get_battle_opponent(p_001)
            if party_battle_opponent_002 > 0:
                s2 = str_store_party_name(p_001)
                s3 = str_store_party_name(party_battle_opponent_002)
                print("@{!}DEBUG : {s2} is besieging by {s3}")
            #end
        #end
    #end
simple_trigger95.codeBlock = code


simple_trigger96 = SimpleTrigger(1.0)
def code():
    cur_day_001 = store_current_day()
    if cur_day_001 > _g_last_report_control_day:
        cur_time_of_day_002 = store_time_of_day()
        if cur_time_of_day_002 >= 18:
            random_x_003 = store_random_in_range(0,4)
            if cur_time_of_day_002 >= 22 or random_x_003 == 0:
                _g_last_report_control_day = cur_day_001
                troop_gold_004 = store_troop_gold(trp.player)
                if troop_gold_004 < 0:
                    gold_005 = 0 - troop_gold_004
                    troop_add_gold(trp.player,gold_005)
                #end
            #end
        #end
    #end
    party_morale_006 = party_get_morale(p.main_party)
    if True:
        s1 = str_store_string(gstr.party_morale_is_low)
        str_clear(2)
        party_num_companions_stacks_007 = party_get_num_companion_stacks(p.main_party)
        var008 = 0
        for stack_no_009 in range(0, party_num_companions_stacks_007):
            troop_id_010 = party_stack_get_troop_id(p.main_party,stack_no_009)
            if not troop_is_hero(troop_id_010):
                party_stack_size_011 = party_stack_get_size(p.main_party,stack_no_009)
                troop_faction_012 = store_faction_of_troop(troop_id_010)
                var013 = party_morale_006
                if troop_faction_012 >= fac.kingdom_1 and troop_faction_012 < fac.kingdoms_end:
                    faction_slot_014 = faction_get_slot(troop_faction_012,99)
                    faction_slot_014 /= 100
                    var013 += faction_slot_014
                #end
            #end
            if var013 < 32:
                var015 = 36 - var013
                var015 /= 4
                var016 = 0
                for var017 in range(0, party_stack_size_011):
                    random_x_003 = store_random_in_range(0,100)
                    if random_x_003 < var015:
                        var016 += 1
                        remove_member_from_party(troop_id_010,p.main_party)
                    #end
                #end
            #end
            if var016 >= 1:
                s2 = str_store_troop_name(troop_id_010)
                reg0 = var016
                if var008 >= 1:
                    s1 = str_store_string(gstr.s1_reg0_s2)
                else:
                    s3 = str_store_string(1)
                    s1 = str_store_string(gstr.s3_reg0_s2)
                #end
                var008 += var016
            #end
        #end
        if var008 >= 1:
            if var008 >= 2:
                s2 = str_store_string(gstr.have_deserted_the_party)
            else:
                s2 = str_store_string(gstr.has_deserted_the_party)
            #end
            s1 = str_store_string(gstr.s1_s2)
            if _g_infinite_camping == 0:
                dialog_box(1,gstr.weekly_report)
            #end
        #end
    #end
simple_trigger96.codeBlock = code


simple_trigger97 = SimpleTrigger(1.0)
def code():
    calculate_castle_prosperities_by_using_its_villages()
    var001 = fac.kingdom_6
    var001 += 1
    for var002 in range(fac.kingdom_1, var001):
        for var003 in range(fac.kingdom_1, var001):
            faction_relation_004 = store_relation(var002,var003)
            s7 = str_store_faction_name(var002)
            s8 = str_store_faction_name(var003)
            if var002 != var003:
                reg1 = faction_relation_004
            #end
        #end
    #end
simple_trigger97.codeBlock = code


simple_trigger98 = SimpleTrigger(1.0)
def code():
    if _g_player_is_captive == 1 and not party_is_active(_capturer_party):
        rest_for_hours(0,0,0)
    #end
    party_id_001 = _next_center_will_be_fired
    party_slot_002 = party_get_slot(party_id_001,38)
    if party_slot_002 == 0:
        if True:
            party_slot_003 = party_get_slot(party_id_001,120)
            party_slot_004 = party_get_slot(party_slot_003,240)
            cur_hours_005 = store_current_hours()
            if _cheat_mode == 1 and is_between(party_id_001,p.town_1,p.salt_mine) and is_between(party_slot_003,p.town_1,p.salt_mine):
                s4 = str_store_party_name(party_id_001)
                s5 = str_store_party_name(party_slot_003)
                reg3 = store_current_hours()
                reg4 = party_get_slot(party_slot_003,240)
                print("@{!}DEBUG - Checking fire at {s4} for {s5} - current time {reg3};;; last nearby fire {reg4}")
            #end
        #end
        if cur_hours_005 == party_slot_004:
            party_add_particle_system(party_id_001,psys.map_village_fire)
            party_add_particle_system(party_id_001,psys.map_village_fire_smoke)
        else:
            var006 = party_slot_004 + 4
            if var006 == cur_hours_005:
                party_clear_particle_systems(party_id_001)
            #end
        #end
    #end
simple_trigger98.codeBlock = code


simple_trigger99 = SimpleTrigger(24.0)
def code():
    _g_dont_give_fief_to_player_days -= 1
    val_max(_g_dont_give_fief_to_player_days,-1)
    _g_dont_give_marshalship_to_player_days -= 1
    val_max(_g_dont_give_marshalship_to_player_days,-1)
    party_set_name(p.steppe_bandit_spawn_point,gstr.the_steppes)
    party_set_name(p.taiga_bandit_spawn_point,gstr.the_tundra)
    party_set_name(p.forest_bandit_spawn_point,gstr.the_forests)
    party_set_name(p.mountain_bandit_spawn_point,gstr.the_highlands)
    party_set_name(p.sea_raider_spawn_point_1,gstr.the_coast)
    party_set_name(p.sea_raider_spawn_point_2,gstr.the_coast)
    party_set_name(p.desert_bandit_spawn_point,gstr.the_deserts)
    troop_set_slot(trp.npc11,60,p.town_7)
    troop_set_slot(trp.npc8,60,p.village_35)
    troop_set_slot(trp.npc15,67,p.town_20)
    party_set_slot(p.village_93,225,0)
    party_set_slot(p.village_94,225,0)
    party_set_slot(p.village_95,225,0)
    party_set_slot(p.village_96,225,0)
    party_set_slot(p.village_97,225,0)
    party_set_slot(p.village_102,225,0)
    party_set_slot(p.village_109,225,0)
    party_set_slot(p.village_67,214,0)
    party_set_slot(p.village_5,214,15)
    if check_quest_active(qst.formal_marriage_proposal) and check_quest_failed(qst.formal_marriage_proposal):
        end_quest(qst.formal_marriage_proposal)
    #end
    if check_quest_active(qst.lend_companion):
        quest_slot_001 = quest_get_slot(qst.lend_companion,6)
        troop_faction_002 = store_faction_of_troop(quest_slot_001)
        faction_relation_003 = store_relation(troop_faction_002,_players_kingdom)
        if faction_relation_003 >= 0 or not is_between(troop_faction_002,fac.player_supporters_faction,fac.kingdoms_end):
            abort_quest(qst.lend_companion,0)
        #end
    #end
    if is_between(_players_kingdom,fac.player_supporters_faction,fac.kingdoms_end) and _players_kingdom != fac.player_supporters_faction and faction_slot_eq(_players_kingdom,8,trp.player):
        _g_player_days_as_marshal += 1
    else:
        _g_player_days_as_marshal = 0
    #end
    for p_004 in range(p.town_1, p.castle_1):
        party_slot_005 = party_get_slot(p_004,139)
        if party_slot_005 >= 1:
            party_slot_005 -= 1
            party_set_slot(p_004,139,party_slot_005)
        #end
    #end
simple_trigger99.codeBlock = code


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


