# This Python file uses the following encoding: utf-8


import sys
sys.path.append("../data_objects/")

from presentation import Presentation, LoadEvent, MouseEnterLeaveEvent, RunEvent, MousePressEvent, StateChangedEvent
from simple_trigger import SimpleTrigger
import meshes as mesh



game_credits = Presentation("game_credits", mesh=mesh.load_window)
game_credits.set_read_only()
game_credits.set_manual_end_only()
event = LoadEvent()
def code():
    _g_presentation_credits_obj_1 = -1
    _g_presentation_credits_obj_2 = -1
    _g_presentation_credits_obj_3 = -1
    _g_presentation_credits_obj_4 = -1
    _g_presentation_credits_obj_5 = -1
    _g_presentation_credits_obj_6 = -1
    _g_presentation_credits_obj_7 = -1
    _g_presentation_credits_obj_8 = -1
    _g_presentation_credits_obj_9 = -1
    _g_presentation_credits_obj_10 = -1
    _g_presentation_credits_obj_11 = -1
    _g_presentation_credits_obj_12 = -1
    _g_presentation_credits_obj_1_alpha = 0
    _g_presentation_credits_obj_2_alpha = 0
    _g_presentation_credits_obj_3_alpha = 0
    _g_presentation_credits_obj_4_alpha = 0
    _g_presentation_credits_obj_5_alpha = 0
    _g_presentation_credits_obj_6_alpha = 0
    _g_presentation_credits_obj_7_alpha = 0
    _g_presentation_credits_obj_8_alpha = 0
    _g_presentation_credits_obj_9_alpha = 0
event.codeBlock = code
game_credits.add_event(event)
event = RunEvent()
def code(var001):
    set_fixed_point_multiplier(1000)
    presentation_set_duration(1000000)
    if key_clicked(57) or key_clicked(28) or key_clicked(1) or key_clicked(14) or key_clicked(224) or key_clicked(225) or key_clicked(252) or key_clicked(253):
        presentation_set_duration(0)
    #end
    if _g_presentation_credits_obj_1 < 0:
        s1 = str_store_string(gstr.credits_1)
        create_text_overlay(_g_presentation_credits_obj_1,1,6160)
        overlay_set_color(_g_presentation_credits_obj_1,0)
        overlay_set_alpha(_g_presentation_credits_obj_1,0)
        position_set_x(1,1500)
        position_set_y(1,1500)
        overlay_set_size(_g_presentation_credits_obj_1,1)
        position_set_x(1,500)
        position_set_y(1,375)
        overlay_set_position(_g_presentation_credits_obj_1,1)
        overlay_animate_to_alpha(_g_presentation_credits_obj_1,1000,255)
    elif var001 > 2000 and _g_presentation_credits_obj_1_alpha == 0:
        _g_presentation_credits_obj_1_alpha = 1
        overlay_animate_to_alpha(_g_presentation_credits_obj_1,1000,0)
    elif var001 > 3500 and _g_presentation_credits_obj_2 < 0:
        s1 = str_store_string(gstr.credits_2)
        create_text_overlay(_g_presentation_credits_obj_2,1,6160)
        overlay_set_color(_g_presentation_credits_obj_2,0)
        overlay_set_alpha(_g_presentation_credits_obj_2,0)
        position_set_x(1,1750)
        position_set_y(1,1750)
        overlay_set_size(_g_presentation_credits_obj_2,1)
        position_set_x(1,500)
        position_set_y(1,375)
        overlay_set_position(_g_presentation_credits_obj_2,1)
        overlay_animate_to_alpha(_g_presentation_credits_obj_2,1000,255)
    elif var001 > 5500 and _g_presentation_credits_obj_2_alpha == 0:
        _g_presentation_credits_obj_2_alpha = 1
        overlay_animate_to_alpha(_g_presentation_credits_obj_2,1000,0)
    elif var001 > 7000 and _g_presentation_credits_obj_3 < 0:
        s1 = str_store_string(gstr.credits_3)
        create_text_overlay(_g_presentation_credits_obj_3,1,6160)
        overlay_set_color(_g_presentation_credits_obj_3,0)
        overlay_set_alpha(_g_presentation_credits_obj_3,0)
        position_set_x(1,1750)
        position_set_y(1,1750)
        overlay_set_size(_g_presentation_credits_obj_3,1)
        position_set_x(1,500)
        position_set_y(1,375)
        overlay_set_position(_g_presentation_credits_obj_3,1)
        overlay_animate_to_alpha(_g_presentation_credits_obj_3,1000,255)
    elif var001 > 9000 and _g_presentation_credits_obj_3_alpha == 0:
        _g_presentation_credits_obj_3_alpha = 1
        overlay_animate_to_alpha(_g_presentation_credits_obj_3,1000,0)
    elif var001 > 10500 and _g_presentation_credits_obj_4 < 0:
        s1 = str_store_string(gstr.credits_4)
        create_text_overlay(_g_presentation_credits_obj_4,1,6160)
        overlay_set_color(_g_presentation_credits_obj_4,0)
        overlay_set_alpha(_g_presentation_credits_obj_4,0)
        position_set_x(1,1750)
        position_set_y(1,1750)
        overlay_set_size(_g_presentation_credits_obj_4,1)
        position_set_x(1,500)
        position_set_y(1,375)
        overlay_set_position(_g_presentation_credits_obj_4,1)
        overlay_animate_to_alpha(_g_presentation_credits_obj_4,1000,255)
    elif var001 > 12500 and _g_presentation_credits_obj_4_alpha == 0:
        _g_presentation_credits_obj_4_alpha = 1
        overlay_animate_to_alpha(_g_presentation_credits_obj_4,1000,0)
    elif var001 > 14000 and _g_presentation_credits_obj_5 < 0:
        s1 = str_store_string(gstr.credits_5)
        create_text_overlay(_g_presentation_credits_obj_5,1,6160)
        overlay_set_color(_g_presentation_credits_obj_5,0)
        overlay_set_alpha(_g_presentation_credits_obj_5,0)
        position_set_x(1,1750)
        position_set_y(1,1750)
        overlay_set_size(_g_presentation_credits_obj_5,1)
        position_set_x(1,500)
        position_set_y(1,375)
        overlay_set_position(_g_presentation_credits_obj_5,1)
        overlay_animate_to_alpha(_g_presentation_credits_obj_5,1000,255)
    elif var001 > 16000 and _g_presentation_credits_obj_5_alpha == 0:
        _g_presentation_credits_obj_5_alpha = 1
        overlay_animate_to_alpha(_g_presentation_credits_obj_5,1000,0)
    elif var001 > 17500 and _g_presentation_credits_obj_6 < 0:
        s1 = str_store_string(gstr.credits_6)
        create_text_overlay(_g_presentation_credits_obj_6,1,6160)
        overlay_set_color(_g_presentation_credits_obj_6,0)
        overlay_set_alpha(_g_presentation_credits_obj_6,0)
        position_set_x(1,1750)
        position_set_y(1,1750)
        overlay_set_size(_g_presentation_credits_obj_6,1)
        position_set_x(1,500)
        position_set_y(1,375)
        overlay_set_position(_g_presentation_credits_obj_6,1)
        overlay_animate_to_alpha(_g_presentation_credits_obj_6,1000,255)
    elif var001 > 19500 and _g_presentation_credits_obj_6_alpha == 0:
        _g_presentation_credits_obj_6_alpha = 1
        overlay_animate_to_alpha(_g_presentation_credits_obj_6,1000,0)
    elif var001 > 21000 and _g_presentation_credits_obj_7 < 0:
        s1 = str_store_string(gstr.credits_7)
        create_text_overlay(_g_presentation_credits_obj_7,1,6160)
        overlay_set_color(_g_presentation_credits_obj_7,0)
        overlay_set_alpha(_g_presentation_credits_obj_7,0)
        position_set_x(1,1750)
        position_set_y(1,1750)
        overlay_set_size(_g_presentation_credits_obj_7,1)
        position_set_x(1,500)
        position_set_y(1,375)
        overlay_set_position(_g_presentation_credits_obj_7,1)
        overlay_animate_to_alpha(_g_presentation_credits_obj_7,1000,255)
    elif var001 > 23000 and _g_presentation_credits_obj_7_alpha == 0:
        _g_presentation_credits_obj_7_alpha = 1
        overlay_animate_to_alpha(_g_presentation_credits_obj_7,1000,0)
    elif var001 > 24500 and _g_presentation_credits_obj_8 < 0:
        s1 = str_store_string(gstr.credits_8)
        create_text_overlay(_g_presentation_credits_obj_8,1,6160)
        overlay_set_color(_g_presentation_credits_obj_8,0)
        overlay_set_alpha(_g_presentation_credits_obj_8,0)
        position_set_x(1,1750)
        position_set_y(1,1750)
        overlay_set_size(_g_presentation_credits_obj_8,1)
        position_set_x(1,500)
        position_set_y(1,375)
        overlay_set_position(_g_presentation_credits_obj_8,1)
        overlay_animate_to_alpha(_g_presentation_credits_obj_8,1000,255)
    elif var001 > 26500 and _g_presentation_credits_obj_8_alpha == 0:
        _g_presentation_credits_obj_8_alpha = 1
        overlay_animate_to_alpha(_g_presentation_credits_obj_8,1000,0)
    elif var001 > 28000 and _g_presentation_credits_obj_9 < 0:
        s1 = str_store_string(gstr.credits_10)
        create_text_overlay(_g_presentation_credits_obj_9,1,6160)
        overlay_set_color(_g_presentation_credits_obj_9,0)
        overlay_set_alpha(_g_presentation_credits_obj_9,0)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(_g_presentation_credits_obj_9,1)
        position_set_x(1,250)
        position_set_y(1,485)
        overlay_set_position(_g_presentation_credits_obj_9,1)
        overlay_animate_to_alpha(_g_presentation_credits_obj_9,1000,255)
        s1 = str_store_string(gstr.credits_11)
        create_text_overlay(_g_presentation_credits_obj_10,1,6160)
        overlay_set_color(_g_presentation_credits_obj_10,0)
        overlay_set_alpha(_g_presentation_credits_obj_10,0)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(_g_presentation_credits_obj_10,1)
        position_set_x(1,750)
        position_set_y(1,470)
        overlay_set_position(_g_presentation_credits_obj_10,1)
        overlay_animate_to_alpha(_g_presentation_credits_obj_10,1000,255)
        s1 = str_store_string(gstr.credits_12)
        create_text_overlay(_g_presentation_credits_obj_11,1,6160)
        overlay_set_color(_g_presentation_credits_obj_11,0)
        overlay_set_alpha(_g_presentation_credits_obj_11,0)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(_g_presentation_credits_obj_11,1)
        position_set_x(1,500)
        position_set_y(1,105)
        overlay_set_position(_g_presentation_credits_obj_11,1)
        overlay_animate_to_alpha(_g_presentation_credits_obj_11,1000,255)
    elif var001 > 34000 and _g_presentation_credits_obj_9_alpha == 0:
        _g_presentation_credits_obj_9_alpha = 1
        overlay_animate_to_alpha(_g_presentation_credits_obj_9,1000,0)
        overlay_animate_to_alpha(_g_presentation_credits_obj_10,1000,0)
        overlay_animate_to_alpha(_g_presentation_credits_obj_11,1000,0)
    elif var001 > 35500 and _g_presentation_credits_obj_12 < 0:
        s1 = str_store_string(gstr.credits_9)
        create_text_overlay(_g_presentation_credits_obj_12,1,2064)
        overlay_set_color(_g_presentation_credits_obj_12,0)
        overlay_set_alpha(_g_presentation_credits_obj_12,255)
        position_set_x(1,1000)
        position_set_y(1,1000)
        overlay_set_size(_g_presentation_credits_obj_12,1)
        position_set_x(1,500)
        position_set_y(1,-4800)
        overlay_set_position(_g_presentation_credits_obj_12,1)
        position_set_x(1,500)
        position_set_y(1,760)
        overlay_animate_to_position(_g_presentation_credits_obj_12,70000,1)
    elif var001 > 105500:
        presentation_set_duration(0)
    #end
event.codeBlock = code
game_credits.add_event(event)


game_profile_banner_selection = Presentation("game_profile_banner_selection", mesh=mesh.load_window)
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    s1 = str_store_string(gstr.profile_banner_selection_text)
    create_text_overlay(reg1,1,16)
    position_set_x(1,500)
    position_set_y(1,600)
    overlay_set_position(reg1,1)
    overlay_set_text(reg1,1)
    create_button_overlay(_g_presentation_obj_profile_banner_selection_1,"@Next Page",16)
    position_set_x(1,700)
    position_set_y(1,50)
    overlay_set_position(_g_presentation_obj_profile_banner_selection_1,1)
    create_button_overlay(_g_presentation_obj_profile_banner_selection_2,gstr.use_default_banner,16)
    position_set_x(1,300)
    position_set_y(1,50)
    overlay_set_position(_g_presentation_obj_profile_banner_selection_2,1)
    var001 = 150
    var002 = 575
    var003 = 16 * _g_presentation_page_no
    var004 = var003 + 16
    _g_presentation_banner_start = _g_presentation_obj_profile_banner_selection_2 + 1
    var005 = 0
    for mesh_006 in range(mesh.banner_a01, mesh.banner_f21):
        var007 = 0
        for fac_008 in range(fac.kingdom_1, fac.kingdoms_end):
            if faction_slot_eq(fac_008,15,mesh_006):
                var007 = 1
            #end
        #end
        if var007 == 0:
            var005 += 1
            if var005 > var003 and var005 <= var004:
                create_image_button_overlay(reg1,mesh_006,mesh_006)
                position_set_x(1,var001)
                position_set_y(1,var002)
                overlay_set_position(reg1,1)
                position_set_x(1,100)
                position_set_y(1,100)
                overlay_set_size(reg1,1)
                var001 += 100
                if var001 >= 900:
                    var001 = 150
                    var002 -= 250
                #end
            #end
        #end
    #end
    presentation_set_duration(999999)
event.codeBlock = code
game_profile_banner_selection.add_event(event)
event = StateChangedEvent()
def code(var001):
    if var001 == _g_presentation_obj_profile_banner_selection_1:
        _g_presentation_page_no += 1
        _g_presentation_page_no %= 8
        presentation_set_duration(0)
        start_presentation(prsnt.game_profile_banner_selection)
    elif var001 == _g_presentation_obj_profile_banner_selection_2:
        profile_set_banner_id(-1)
        presentation_set_duration(0)
    else:
        var002 = var001 - _g_presentation_banner_start
        var003 = 16 * _g_presentation_page_no
        var002 += var003
        var004 = 0
        var005 = mesh.banner_f21
        for var006 in range(mesh.banner_a01, var005):
            var007 = 0
            for fac_008 in range(fac.kingdom_1, fac.kingdoms_end):
                if faction_slot_eq(fac_008,15,var006):
                    var007 = 1
                #end
            #end
            if var007 == 0:
                if var002 == var004:
                    var009 = var006 - mesh.banner_a01
                    profile_set_banner_id(var009)
                    var005 = 0
                #end
            #end
            var004 += 1
        #end
        presentation_set_duration(0)
    #end
event.codeBlock = code
game_profile_banner_selection.add_event(event)


game_custom_battle_designer = Presentation("game_custom_battle_designer", mesh=mesh.cb_ui_main)
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_text_overlay(reg0,gstr.player,98320)
    overlay_set_color(reg0,4294967295)
    position_set_x(1,1500)
    position_set_y(1,1500)
    overlay_set_size(reg0,1)
    position_set_x(1,175)
    position_set_y(1,700)
    overlay_set_position(reg0,1)
    create_text_overlay(reg0,gstr.enemy,98320)
    overlay_set_color(reg0,4294967295)
    position_set_x(1,1500)
    position_set_y(1,1500)
    overlay_set_size(reg0,1)
    position_set_x(1,820)
    position_set_y(1,700)
    overlay_set_position(reg0,1)
    create_text_overlay(reg0,gstr.character,16)
    position_set_x(1,175)
    position_set_y(1,670)
    overlay_set_position(reg0,1)
    create_combo_label_overlay(_g_presentation_obj_custom_battle_designer_18)
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_custom_battle_designer_18,1)
    position_set_x(1,175)
    position_set_y(1,635)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_18,1)
    for trp_001 in range(trp.quick_battle_troop_1, trp.quick_battle_troops_end):
        s0 = str_store_troop_name(trp_001)
        overlay_add_item(_g_presentation_obj_custom_battle_designer_18,0)
    #end
    trp_001 = _g_quick_battle_troop - trp.quick_battle_troop_1
    overlay_set_val(_g_presentation_obj_custom_battle_designer_18,trp_001)
    trp_001 = _g_quick_battle_troop * 2
    create_mesh_overlay_with_tableau_material(reg0,-1,tableau.game_party_window,trp_001)
    position_set_x(1,25)
    position_set_y(1,370)
    overlay_set_position(reg0,1)
    if _g_quick_battle_team_2_faction == fac.kingdom_1:
        trp_001 = trp.swadian_knight
    elif _g_quick_battle_team_2_faction == fac.kingdom_2:
        trp_001 = trp.vaegir_knight
    elif _g_quick_battle_team_2_faction == fac.kingdom_3:
        trp_001 = trp.khergit_veteran_horse_archer
    elif _g_quick_battle_team_2_faction == fac.kingdom_4:
        trp_001 = trp.nord_champion
    elif _g_quick_battle_team_2_faction == fac.kingdom_5:
        trp_001 = trp.rhodok_sergeant
    elif _g_quick_battle_team_2_faction == fac.kingdom_6:
        trp_001 = trp.sarranid_mamluke
    else:
        trp_001 = trp.taiga_bandit
    #end
    trp_001 *= 2
    create_mesh_overlay_with_tableau_material(reg0,-1,tableau.game_party_window,trp_001)
    position_set_x(1,670)
    position_set_y(1,370)
    overlay_set_position(reg0,1)
    create_text_overlay(reg0,gstr.biography,16)
    position_set_x(1,500)
    position_set_y(1,700)
    overlay_set_position(reg0,1)
    var002 = _g_quick_battle_troop - trp.quick_battle_troop_1
    var002 = var002 + gstr.quick_battle_troop_1
    create_text_overlay(reg0,var002,8192)
    position_set_x(1,850)
    position_set_y(1,850)
    overlay_set_size(reg0,1)
    position_set_x(1,320)
    position_set_y(1,560)
    overlay_set_position(reg0,1)
    position_set_x(1,360)
    position_set_y(1,130)
    overlay_set_area_size(reg0,1)
    create_text_overlay(reg0,gstr.map_basic,16)
    overlay_set_color(reg0,16777215)
    position_set_x(1,1500)
    position_set_y(1,1500)
    overlay_set_size(reg0,1)
    position_set_x(1,500)
    position_set_y(1,450)
    overlay_set_position(reg0,1)
    create_combo_label_overlay(_g_presentation_obj_custom_battle_designer_1)
    position_set_x(1,700)
    position_set_y(1,700)
    overlay_set_size(_g_presentation_obj_custom_battle_designer_1,1)
    position_set_x(1,500)
    position_set_y(1,415)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_1,1)
    if _g_quick_battle_game_type == 0:
        for scn_003 in range(scn.quick_battle_scene_1, scn.quick_battle_scene_4):
            var004 = scn_003 - scn.quick_battle_scene_1
            var004 = var004 + gstr.quick_battle_scene_1
            overlay_add_item(_g_presentation_obj_custom_battle_designer_1,var004)
        #end
        if is_between(_g_quick_battle_map,scn.quick_battle_scene_1,scn.quick_battle_scene_4):
            var005 = _g_quick_battle_map - scn.quick_battle_scene_1
            overlay_set_val(_g_presentation_obj_custom_battle_designer_1,var005)
        else:
            overlay_set_val(_g_presentation_obj_custom_battle_designer_1,0)
            _g_quick_battle_map = scn.quick_battle_scene_1
        #end
    else:
        for scn_003 in range(scn.quick_battle_scene_4, scn.quick_battle_maps_end):
            var004 = scn_003 - scn.quick_battle_scene_1
            var004 = var004 + gstr.quick_battle_scene_1
            overlay_add_item(_g_presentation_obj_custom_battle_designer_1,var004)
        #end
        if is_between(_g_quick_battle_map,scn.quick_battle_scene_4,scn.quick_battle_maps_end):
            var005 = _g_quick_battle_map - scn.quick_battle_scene_4
            overlay_set_val(_g_presentation_obj_custom_battle_designer_1,var005)
        else:
            overlay_set_val(_g_presentation_obj_custom_battle_designer_1,0)
            _g_quick_battle_map = scn.quick_battle_scene_4
        #end
    #end
    var006 = _g_quick_battle_map - scn.quick_battle_scene_1
    var006 = var006 + mesh.cb_ui_maps_scene_01
    create_mesh_overlay(reg0,var006)
    position_set_x(1,700)
    position_set_y(1,700)
    overlay_set_size(reg0,1)
    position_set_x(1,380)
    position_set_y(1,220)
    overlay_set_position(reg0,1)
    create_text_overlay(reg0,gstr.game_type_basic,16)
    overlay_set_color(reg0,16777215)
    position_set_x(1,1500)
    position_set_y(1,1500)
    overlay_set_size(reg0,1)
    position_set_x(1,500)
    position_set_y(1,180)
    overlay_set_position(reg0,1)
    create_combo_label_overlay(_g_presentation_obj_custom_battle_designer_23)
    position_set_x(1,700)
    position_set_y(1,700)
    overlay_set_size(_g_presentation_obj_custom_battle_designer_23,1)
    position_set_x(1,500)
    position_set_y(1,150)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_23,1)
    overlay_add_item(_g_presentation_obj_custom_battle_designer_23,gstr.battle)
    overlay_add_item(_g_presentation_obj_custom_battle_designer_23,gstr.siege_offense)
    overlay_add_item(_g_presentation_obj_custom_battle_designer_23,gstr.siege_defense)
    overlay_set_val(_g_presentation_obj_custom_battle_designer_23,_g_quick_battle_game_type)
    create_game_button_overlay(_g_presentation_obj_custom_battle_designer_24,gstr.randomize)
    position_set_x(1,500)
    position_set_y(1,60)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_24,1)
    var007 = 330
    var007 = 350
    var008 = 40
    create_text_overlay(reg0,gstr.faction,16)
    position_set_x(1,175)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    create_text_overlay(reg0,gstr.faction,16)
    position_set_x(1,820)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    var007 -= var008
    create_combo_label_overlay(_g_presentation_obj_custom_battle_designer_4)
    position_set_x(1,175)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_4,1)
    if is_trial_version():
        s0 = str_store_faction_name(fac.kingdom_1)
        overlay_add_item(_g_presentation_obj_custom_battle_designer_4,0)
        var009 = fac.kingdom_1
        var009 += 1
        s0 = str_store_faction_name(var009)
        overlay_add_item(_g_presentation_obj_custom_battle_designer_4,0)
    else:
        for fac_009 in range(fac.kingdom_1, fac.kingdoms_end):
            s0 = str_store_faction_name(fac_009)
            overlay_add_item(_g_presentation_obj_custom_battle_designer_4,0)
        #end
        s0 = str_store_faction_name(fac.outlaws)
        overlay_add_item(_g_presentation_obj_custom_battle_designer_4,0)
    #end
    if _g_quick_battle_team_1_faction == fac.outlaws:
        var010 = fac.kingdoms_end
        var010 = var010 - fac.kingdom_1
        overlay_set_val(_g_presentation_obj_custom_battle_designer_4,var010)
    else:
        var011 = _g_quick_battle_team_1_faction - fac.kingdom_1
        overlay_set_val(_g_presentation_obj_custom_battle_designer_4,var011)
    #end
    create_combo_label_overlay(_g_presentation_obj_custom_battle_designer_5)
    position_set_x(1,820)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_5,1)
    if is_trial_version():
        s0 = str_store_faction_name(fac.kingdom_1)
        overlay_add_item(_g_presentation_obj_custom_battle_designer_5,0)
        fac_009 = fac.kingdom_1
        fac_009 += 1
        s0 = str_store_faction_name(fac_009)
        overlay_add_item(_g_presentation_obj_custom_battle_designer_5,0)
    else:
        for fac_009 in range(fac.kingdom_1, fac.kingdoms_end):
            s0 = str_store_faction_name(fac_009)
            overlay_add_item(_g_presentation_obj_custom_battle_designer_5,0)
        #end
        s0 = str_store_faction_name(fac.outlaws)
        overlay_add_item(_g_presentation_obj_custom_battle_designer_5,0)
    #end
    if _g_quick_battle_team_2_faction == fac.outlaws:
        var010 = fac.kingdoms_end
        var010 = var010 - fac.kingdom_1
        overlay_set_val(_g_presentation_obj_custom_battle_designer_5,var010)
    else:
        var012 = _g_quick_battle_team_2_faction - fac.kingdom_1
        overlay_set_val(_g_presentation_obj_custom_battle_designer_5,var012)
    #end
    var007 -= var008
    create_text_overlay(reg0,gstr.army_composition,16)
    position_set_x(1,175)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    create_text_overlay(reg0,gstr.army_composition,16)
    position_set_x(1,820)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    var007 -= var008
    if _g_presentation_obj_custom_battle_designer_6_last_value == 0 and _g_presentation_obj_custom_battle_designer_7_last_value == 0 and _g_presentation_obj_custom_battle_designer_8_last_value == 0 and _g_presentation_obj_custom_battle_designer_9_last_value == 0 and _g_presentation_obj_custom_battle_designer_10_last_value == 0 and _g_presentation_obj_custom_battle_designer_11_last_value == 0:
        _g_presentation_obj_custom_battle_designer_6_last_value = 34
        _g_presentation_obj_custom_battle_designer_7_last_value = 33
        _g_presentation_obj_custom_battle_designer_8_last_value = 33
        _g_presentation_obj_custom_battle_designer_9_last_value = 34
        _g_presentation_obj_custom_battle_designer_10_last_value = 33
        _g_presentation_obj_custom_battle_designer_11_last_value = 33
        _g_presentation_obj_custom_battle_designer_6_locked = 0
        _g_presentation_obj_custom_battle_designer_7_locked = 0
        _g_presentation_obj_custom_battle_designer_8_locked = 0
        _g_presentation_obj_custom_battle_designer_9_locked = 0
        _g_presentation_obj_custom_battle_designer_10_locked = 0
        _g_presentation_obj_custom_battle_designer_11_locked = 0
    #end
    create_mesh_overlay(reg0,mesh.cb_ui_icon_infantry)
    position_set_x(1,5)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    position_set_x(1,400)
    position_set_y(1,400)
    overlay_set_size(reg0,1)
    create_mesh_overlay(reg0,mesh.cb_ui_icon_infantry)
    position_set_x(1,650)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    position_set_x(1,400)
    position_set_y(1,400)
    overlay_set_size(reg0,1)
    create_slider_overlay(_g_presentation_obj_custom_battle_designer_6,0,100)
    overlay_set_val(_g_presentation_obj_custom_battle_designer_6,_g_presentation_obj_custom_battle_designer_6_last_value)
    position_set_x(1,900)
    position_set_y(1,1000)
    overlay_set_size(_g_presentation_obj_custom_battle_designer_6,1)
    position_set_x(1,175)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_6,1)
    reg0 = _g_presentation_obj_custom_battle_designer_6_last_value
    create_text_overlay(_g_presentation_obj_custom_battle_designer_12,gstr.reg0_percent,0)
    position_set_x(1,295)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_12,1)
    create_slider_overlay(_g_presentation_obj_custom_battle_designer_9,0,100)
    overlay_set_val(_g_presentation_obj_custom_battle_designer_9,_g_presentation_obj_custom_battle_designer_9_last_value)
    position_set_x(1,900)
    position_set_y(1,1000)
    overlay_set_size(_g_presentation_obj_custom_battle_designer_9,1)
    position_set_x(1,820)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_9,1)
    reg0 = _g_presentation_obj_custom_battle_designer_9_last_value
    create_text_overlay(_g_presentation_obj_custom_battle_designer_15,gstr.reg0_percent,0)
    position_set_x(1,940)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_15,1)
    var007 -= var008
    create_mesh_overlay(reg0,mesh.cb_ui_icon_archer)
    position_set_x(1,15)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    position_set_x(1,400)
    position_set_y(1,400)
    overlay_set_size(reg0,1)
    create_mesh_overlay(reg0,mesh.cb_ui_icon_archer)
    position_set_x(1,660)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    position_set_x(1,400)
    position_set_y(1,400)
    overlay_set_size(reg0,1)
    create_slider_overlay(_g_presentation_obj_custom_battle_designer_7,0,100)
    overlay_set_val(_g_presentation_obj_custom_battle_designer_7,_g_presentation_obj_custom_battle_designer_7_last_value)
    position_set_x(1,900)
    position_set_y(1,1000)
    overlay_set_size(_g_presentation_obj_custom_battle_designer_7,1)
    position_set_x(1,175)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_7,1)
    reg0 = _g_presentation_obj_custom_battle_designer_7_last_value
    create_text_overlay(_g_presentation_obj_custom_battle_designer_13,gstr.reg0_percent,0)
    position_set_x(1,295)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_13,1)
    create_slider_overlay(_g_presentation_obj_custom_battle_designer_10,0,100)
    overlay_set_val(_g_presentation_obj_custom_battle_designer_10,_g_presentation_obj_custom_battle_designer_10_last_value)
    position_set_x(1,900)
    position_set_y(1,1000)
    overlay_set_size(_g_presentation_obj_custom_battle_designer_10,1)
    position_set_x(1,820)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_10,1)
    reg0 = _g_presentation_obj_custom_battle_designer_10_last_value
    create_text_overlay(_g_presentation_obj_custom_battle_designer_16,gstr.reg0_percent,0)
    position_set_x(1,940)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_16,1)
    var007 -= var008
    create_mesh_overlay(reg0,mesh.cb_ui_icon_horseman)
    position_set_x(1,10)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    position_set_x(1,400)
    position_set_y(1,400)
    overlay_set_size(reg0,1)
    create_mesh_overlay(reg0,mesh.cb_ui_icon_horseman)
    position_set_x(1,655)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    position_set_x(1,400)
    position_set_y(1,400)
    overlay_set_size(reg0,1)
    create_slider_overlay(_g_presentation_obj_custom_battle_designer_8,0,100)
    overlay_set_val(_g_presentation_obj_custom_battle_designer_8,_g_presentation_obj_custom_battle_designer_8_last_value)
    position_set_x(1,900)
    position_set_y(1,1000)
    overlay_set_size(_g_presentation_obj_custom_battle_designer_8,1)
    position_set_x(1,175)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_8,1)
    reg0 = _g_presentation_obj_custom_battle_designer_8_last_value
    create_text_overlay(_g_presentation_obj_custom_battle_designer_14,gstr.reg0_percent,0)
    position_set_x(1,295)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_14,1)
    create_slider_overlay(_g_presentation_obj_custom_battle_designer_11,0,100)
    overlay_set_val(_g_presentation_obj_custom_battle_designer_11,_g_presentation_obj_custom_battle_designer_11_last_value)
    position_set_x(1,900)
    position_set_y(1,1000)
    overlay_set_size(_g_presentation_obj_custom_battle_designer_11,1)
    position_set_x(1,820)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_11,1)
    reg0 = _g_presentation_obj_custom_battle_designer_11_last_value
    create_text_overlay(_g_presentation_obj_custom_battle_designer_17,gstr.reg0_percent,0)
    position_set_x(1,940)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_17,1)
    var007 -= var008
    create_text_overlay(reg0,gstr.army_size,16)
    position_set_x(1,175)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    create_text_overlay(reg0,gstr.army_size,16)
    position_set_x(1,820)
    position_set_y(1,var007)
    overlay_set_position(reg0,1)
    var007 -= var008
    if is_trial_version():
        val_min(_g_quick_battle_army_1_size,25)
        val_min(_g_quick_battle_army_2_size,25)
    #end
    create_slider_overlay(_g_presentation_obj_custom_battle_designer_2,0,100)
    overlay_set_boundaries(_g_presentation_obj_custom_battle_designer_2,1000,75000)
    overlay_set_val(_g_presentation_obj_custom_battle_designer_2,_g_quick_battle_army_1_size)
    position_set_x(1,900)
    position_set_y(1,1000)
    overlay_set_size(_g_presentation_obj_custom_battle_designer_2,1)
    position_set_x(1,135)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_2,1)
    get_army_size_from_slider_value(_g_quick_battle_army_1_size)
    create_text_overlay(_g_presentation_obj_custom_battle_designer_21,gstr.reg0_men,0)
    position_set_x(1,255)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_21,1)
    create_slider_overlay(_g_presentation_obj_custom_battle_designer_3,200)
    overlay_set_boundaries(_g_presentation_obj_custom_battle_designer_3,1000,75000)
    overlay_set_val(_g_presentation_obj_custom_battle_designer_3,_g_quick_battle_army_2_size)
    position_set_x(1,900)
    position_set_y(1,1000)
    overlay_set_size(_g_presentation_obj_custom_battle_designer_3,1)
    position_set_x(1,780)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_3,1)
    get_army_size_from_slider_value(_g_quick_battle_army_2_size)
    create_text_overlay(_g_presentation_obj_custom_battle_designer_22,gstr.reg0_men,0)
    position_set_x(1,900)
    position_set_y(1,var007)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_22,1)
    create_game_button_overlay(_g_presentation_obj_custom_battle_designer_19,gstr.start,0)
    position_set_x(1,415)
    position_set_y(1,10)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_19,1)
    create_game_button_overlay(_g_presentation_obj_custom_battle_designer_20,gstr.back,0)
    position_set_x(1,585)
    position_set_y(1,10)
    overlay_set_position(_g_presentation_obj_custom_battle_designer_20,1)
    presentation_set_duration(999999)
event.codeBlock = code
game_custom_battle_designer.add_event(event)
event = StateChangedEvent()
def code(var001, var002):
    if var001 == _g_presentation_obj_custom_battle_designer_1:
        if _g_quick_battle_game_type == 0:
            _g_quick_battle_map = var002 + scn.quick_battle_scene_1
        else:
            _g_quick_battle_map = var002 + scn.quick_battle_scene_4
        #end
        presentation_set_duration(0)
        start_presentation(prsnt.game_custom_battle_designer)
    elif var001 == _g_presentation_obj_custom_battle_designer_23:
        _g_quick_battle_game_type = var002
        presentation_set_duration(0)
        start_presentation(prsnt.game_custom_battle_designer)
    elif var001 == _g_presentation_obj_custom_battle_designer_24:
        _g_quick_battle_game_type = store_random_in_range(0,3)
        _g_quick_battle_troop = store_random_in_range(trp.quick_battle_troop_1,trp.quick_battle_troops_end)
        if is_trial_version():
            _g_quick_battle_team_1_faction = store_random_in_range(0,2)
            if _g_quick_battle_team_1_faction == 0:
                _g_quick_battle_team_2_faction = 1
            else:
                _g_quick_battle_team_2_faction = 0
            #end
            _g_quick_battle_team_1_faction = _g_quick_battle_team_1_faction + fac.kingdom_1
            _g_quick_battle_team_2_faction = _g_quick_battle_team_2_faction + fac.kingdom_1
            _g_quick_battle_army_1_size = store_random_in_range(10,16)
            random_x_003 = store_random_in_range(0,6)
            _g_quick_battle_army_1_size += random_x_003
            random_x_003 = store_random_in_range(0,6)
            _g_quick_battle_army_1_size += random_x_003
        else:
            var004 = fac.kingdoms_end
            var004 = var004 - fac.kingdom_1
            var004 += 1
            _g_quick_battle_team_1_faction = store_random_in_range(0,var004)
            if _g_quick_battle_team_1_faction == 0:
                _g_quick_battle_team_1_faction = fac.outlaws
            else:
                _g_quick_battle_team_1_faction = _g_quick_battle_team_1_faction + fac.kingdom_1
                _g_quick_battle_team_1_faction -= 1
            #end
            var005 = 1000
            for _ in range(0, var005):
                _g_quick_battle_team_2_faction = store_random_in_range(0,var004)
                if _g_quick_battle_team_2_faction == 0:
                    _g_quick_battle_team_2_faction = fac.outlaws
                else:
                    _g_quick_battle_team_2_faction = _g_quick_battle_team_2_faction + fac.kingdom_1
                    _g_quick_battle_team_2_faction -= 1
                #end
                if _g_quick_battle_team_1_faction != _g_quick_battle_team_2_faction:
                    var005 = 0
                #end
            #end
            _g_quick_battle_army_1_size = store_random_in_range(10,21)
            random_x_003 = store_random_in_range(0,11)
            _g_quick_battle_army_1_size += random_x_003
            random_x_003 = store_random_in_range(0,11)
            _g_quick_battle_army_1_size += random_x_003
        #end
        _g_quick_battle_army_2_size = _g_quick_battle_army_1_size
        if _g_quick_battle_game_type == 0:
            _g_quick_battle_map = store_random_in_range(scn.quick_battle_scene_1,scn.quick_battle_scene_4)
            random_x_007 = store_random_in_range(0,3)
            random_x_008 = store_random_in_range(0,2)
            random_x_009 = store_random_in_range(0,100)
            var010 = 100 - random_x_009
            random_x_011 = store_random_in_range(0,var010)
            var012 = var010 - random_x_011
            if random_x_007 == 0:
                _g_presentation_obj_custom_battle_designer_6_last_value = random_x_009
                if random_x_008 == 0:
                    _g_presentation_obj_custom_battle_designer_7_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_8_last_value = var012
                else:
                    _g_presentation_obj_custom_battle_designer_8_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_7_last_value = var012
                #end
            elif random_x_007 == 1:
                _g_presentation_obj_custom_battle_designer_7_last_value = random_x_009
                if random_x_008 == 0:
                    _g_presentation_obj_custom_battle_designer_6_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_8_last_value = var012
                else:
                    _g_presentation_obj_custom_battle_designer_8_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_6_last_value = var012
                #end
            else:
                _g_presentation_obj_custom_battle_designer_8_last_value = random_x_009
                if random_x_008 == 0:
                    _g_presentation_obj_custom_battle_designer_6_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_7_last_value = var012
                else:
                    _g_presentation_obj_custom_battle_designer_7_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_6_last_value = var012
                #end
            #end
            random_x_007 = store_random_in_range(0,3)
            random_x_008 = store_random_in_range(0,2)
            random_x_009 = store_random_in_range(0,100)
            var010 = 100 - random_x_009
            random_x_011 = store_random_in_range(0,var010)
            var012 = var010 - random_x_011
            if random_x_007 == 0:
                _g_presentation_obj_custom_battle_designer_9_last_value = random_x_009
                if random_x_008 == 0:
                    _g_presentation_obj_custom_battle_designer_10_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_11_last_value = var012
                else:
                    _g_presentation_obj_custom_battle_designer_11_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_10_last_value = var012
                #end
            elif random_x_007 == 1:
                _g_presentation_obj_custom_battle_designer_10_last_value = random_x_009
                if random_x_008 == 0:
                    _g_presentation_obj_custom_battle_designer_9_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_11_last_value = var012
                else:
                    _g_presentation_obj_custom_battle_designer_11_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_9_last_value = var012
                #end
            else:
                _g_presentation_obj_custom_battle_designer_11_last_value = random_x_009
                if random_x_008 == 0:
                    _g_presentation_obj_custom_battle_designer_9_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_10_last_value = var012
                else:
                    _g_presentation_obj_custom_battle_designer_10_last_value = random_x_011
                    _g_presentation_obj_custom_battle_designer_9_last_value = var012
                #end
            #end
        elif _g_quick_battle_game_type == 1:
            _g_quick_battle_map = store_random_in_range(scn.quick_battle_scene_4,scn.quick_battle_maps_end)
            _g_presentation_obj_custom_battle_designer_10_last_value = store_random_in_range(30,100)
            _g_presentation_obj_custom_battle_designer_9_last_value = 100 - _g_presentation_obj_custom_battle_designer_10_last_value
            _g_presentation_obj_custom_battle_designer_11_last_value = 0
            _g_presentation_obj_custom_battle_designer_6_last_value = store_random_in_range(20,100)
            _g_presentation_obj_custom_battle_designer_7_last_value = 100 - _g_presentation_obj_custom_battle_designer_6_last_value
            _g_presentation_obj_custom_battle_designer_8_last_value = 0
        else:
            _g_quick_battle_map = store_random_in_range(scn.quick_battle_scene_4,scn.quick_battle_maps_end)
            _g_presentation_obj_custom_battle_designer_7_last_value = store_random_in_range(30,100)
            _g_presentation_obj_custom_battle_designer_6_last_value = 100 - _g_presentation_obj_custom_battle_designer_7_last_value
            _g_presentation_obj_custom_battle_designer_8_last_value = 0
            _g_presentation_obj_custom_battle_designer_9_last_value = store_random_in_range(20,100)
            _g_presentation_obj_custom_battle_designer_10_last_value = 100 - _g_presentation_obj_custom_battle_designer_9_last_value
            _g_presentation_obj_custom_battle_designer_11_last_value = 0
        #end
        presentation_set_duration(0)
        start_presentation(prsnt.game_custom_battle_designer)
    elif var001 == _g_presentation_obj_custom_battle_designer_2:
        _g_quick_battle_army_1_size = var002
        if is_trial_version() and _g_quick_battle_army_1_size > 25:
            _g_quick_battle_army_1_size = 25
            overlay_set_val(_g_presentation_obj_custom_battle_designer_2,25)
        #end
        get_army_size_from_slider_value(_g_quick_battle_army_1_size)
        overlay_set_text(_g_presentation_obj_custom_battle_designer_21,gstr.reg0_men)
    elif var001 == _g_presentation_obj_custom_battle_designer_3:
        _g_quick_battle_army_2_size = var002
        if is_trial_version() and _g_quick_battle_army_2_size > 25:
            _g_quick_battle_army_2_size = 25
            overlay_set_val(_g_presentation_obj_custom_battle_designer_3,25)
        #end
        get_army_size_from_slider_value(_g_quick_battle_army_2_size)
        overlay_set_text(_g_presentation_obj_custom_battle_designer_22,gstr.reg0_men)
    elif var001 == _g_presentation_obj_custom_battle_designer_4:
        if True:
            var013 = fac.kingdoms_end
            var013 = var013 - fac.kingdom_1
            if var002 == var013:
                _g_quick_battle_team_1_faction = fac.outlaws
            else:
                _g_quick_battle_team_1_faction = var002 + fac.kingdom_1
            #end
        #end
    elif var001 == _g_presentation_obj_custom_battle_designer_5:
        if True:
            var013 = fac.kingdoms_end
            var013 = var013 - fac.kingdom_1
            if var002 == var013:
                _g_quick_battle_team_2_faction = fac.outlaws
            else:
                _g_quick_battle_team_2_faction = var002 + fac.kingdom_1
            #end
        #end
        presentation_set_duration(0)
        start_presentation(prsnt.game_custom_battle_designer)
    elif var001 == _g_presentation_obj_custom_battle_designer_18:
        _g_quick_battle_troop = var002 + trp.quick_battle_troop_1
        presentation_set_duration(0)
        start_presentation(prsnt.game_custom_battle_designer)
    elif var001 == _g_presentation_obj_custom_battle_designer_6:
        if _g_presentation_obj_custom_battle_designer_6_locked == 1 and var002 != _g_presentation_obj_custom_battle_designer_6_last_value:
            overlay_set_val(_g_presentation_obj_custom_battle_designer_6,_g_presentation_obj_custom_battle_designer_6_last_value)
        else:
            if var002 < _g_presentation_obj_custom_battle_designer_6_last_value:
                var014 = _g_presentation_obj_custom_battle_designer_6_last_value - var002
                if _g_presentation_obj_custom_battle_designer_7_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_8_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_6_last_value = var002
                _g_presentation_obj_custom_battle_designer_7_last_value += var015
                _g_presentation_obj_custom_battle_designer_8_last_value += var016
                if _g_presentation_obj_custom_battle_designer_7_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_7_last_value - 100
                    _g_presentation_obj_custom_battle_designer_8_last_value += var014
                    _g_presentation_obj_custom_battle_designer_7_last_value = 100
                elif _g_presentation_obj_custom_battle_designer_8_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_8_last_value - 100
                    _g_presentation_obj_custom_battle_designer_7_last_value += var014
                    _g_presentation_obj_custom_battle_designer_8_last_value = 100
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_7,_g_presentation_obj_custom_battle_designer_7_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_8,_g_presentation_obj_custom_battle_designer_8_last_value)
            elif var002 > _g_presentation_obj_custom_battle_designer_6_last_value:
                var014 = var002 - _g_presentation_obj_custom_battle_designer_6_last_value
                if _g_presentation_obj_custom_battle_designer_7_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_8_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_6_last_value = var002
                _g_presentation_obj_custom_battle_designer_7_last_value -= var015
                _g_presentation_obj_custom_battle_designer_8_last_value -= var016
                if _g_presentation_obj_custom_battle_designer_7_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_8_last_value += _g_presentation_obj_custom_battle_designer_7_last_value
                    _g_presentation_obj_custom_battle_designer_7_last_value = 0
                elif _g_presentation_obj_custom_battle_designer_8_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_7_last_value += _g_presentation_obj_custom_battle_designer_8_last_value
                    _g_presentation_obj_custom_battle_designer_8_last_value = 0
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_7,_g_presentation_obj_custom_battle_designer_7_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_8,_g_presentation_obj_custom_battle_designer_8_last_value)
            #end
            reg0 = _g_presentation_obj_custom_battle_designer_6_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_12,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_7_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_13,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_8_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_14,gstr.reg0_percent)
        #end
    elif var001 == _g_presentation_obj_custom_battle_designer_7:
        if _g_presentation_obj_custom_battle_designer_7_locked == 1 and var002 != _g_presentation_obj_custom_battle_designer_7_last_value:
            overlay_set_val(_g_presentation_obj_custom_battle_designer_7,_g_presentation_obj_custom_battle_designer_7_last_value)
        else:
            if var002 < _g_presentation_obj_custom_battle_designer_7_last_value:
                var014 = _g_presentation_obj_custom_battle_designer_7_last_value - var002
                if _g_presentation_obj_custom_battle_designer_6_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_8_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_7_last_value = var002
                _g_presentation_obj_custom_battle_designer_6_last_value += var015
                _g_presentation_obj_custom_battle_designer_8_last_value += var016
                if _g_presentation_obj_custom_battle_designer_6_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_6_last_value - 100
                    _g_presentation_obj_custom_battle_designer_8_last_value += var014
                    _g_presentation_obj_custom_battle_designer_6_last_value = 100
                elif _g_presentation_obj_custom_battle_designer_8_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_8_last_value - 100
                    _g_presentation_obj_custom_battle_designer_6_last_value += var014
                    _g_presentation_obj_custom_battle_designer_8_last_value = 100
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_6,_g_presentation_obj_custom_battle_designer_6_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_8,_g_presentation_obj_custom_battle_designer_8_last_value)
            elif var002 > _g_presentation_obj_custom_battle_designer_7_last_value:
                var014 = var002 - _g_presentation_obj_custom_battle_designer_7_last_value
                if _g_presentation_obj_custom_battle_designer_6_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_8_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_7_last_value = var002
                _g_presentation_obj_custom_battle_designer_6_last_value -= var015
                _g_presentation_obj_custom_battle_designer_8_last_value -= var016
                if _g_presentation_obj_custom_battle_designer_6_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_8_last_value += _g_presentation_obj_custom_battle_designer_6_last_value
                    _g_presentation_obj_custom_battle_designer_6_last_value = 0
                elif _g_presentation_obj_custom_battle_designer_8_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_6_last_value += _g_presentation_obj_custom_battle_designer_8_last_value
                    _g_presentation_obj_custom_battle_designer_8_last_value = 0
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_6,_g_presentation_obj_custom_battle_designer_6_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_8,_g_presentation_obj_custom_battle_designer_8_last_value)
            #end
            reg0 = _g_presentation_obj_custom_battle_designer_6_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_12,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_7_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_13,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_8_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_14,gstr.reg0_percent)
        #end
    elif var001 == _g_presentation_obj_custom_battle_designer_8:
        if _g_presentation_obj_custom_battle_designer_8_locked == 1 and var002 != _g_presentation_obj_custom_battle_designer_8_last_value:
            overlay_set_val(_g_presentation_obj_custom_battle_designer_8,_g_presentation_obj_custom_battle_designer_8_last_value)
        else:
            if var002 < _g_presentation_obj_custom_battle_designer_8_last_value:
                var014 = _g_presentation_obj_custom_battle_designer_8_last_value - var002
                if _g_presentation_obj_custom_battle_designer_7_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_6_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_8_last_value = var002
                _g_presentation_obj_custom_battle_designer_7_last_value += var015
                _g_presentation_obj_custom_battle_designer_6_last_value += var016
                if _g_presentation_obj_custom_battle_designer_7_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_7_last_value - 100
                    _g_presentation_obj_custom_battle_designer_6_last_value += var014
                    _g_presentation_obj_custom_battle_designer_7_last_value = 100
                elif _g_presentation_obj_custom_battle_designer_6_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_6_last_value - 100
                    _g_presentation_obj_custom_battle_designer_7_last_value += var014
                    _g_presentation_obj_custom_battle_designer_6_last_value = 100
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_7,_g_presentation_obj_custom_battle_designer_7_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_6,_g_presentation_obj_custom_battle_designer_6_last_value)
            elif var002 > _g_presentation_obj_custom_battle_designer_8_last_value:
                var014 = var002 - _g_presentation_obj_custom_battle_designer_8_last_value
                if _g_presentation_obj_custom_battle_designer_7_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_6_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_8_last_value = var002
                _g_presentation_obj_custom_battle_designer_7_last_value -= var015
                _g_presentation_obj_custom_battle_designer_6_last_value -= var016
                if _g_presentation_obj_custom_battle_designer_7_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_6_last_value += _g_presentation_obj_custom_battle_designer_7_last_value
                    _g_presentation_obj_custom_battle_designer_7_last_value = 0
                elif _g_presentation_obj_custom_battle_designer_6_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_7_last_value += _g_presentation_obj_custom_battle_designer_6_last_value
                    _g_presentation_obj_custom_battle_designer_6_last_value = 0
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_7,_g_presentation_obj_custom_battle_designer_7_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_6,_g_presentation_obj_custom_battle_designer_6_last_value)
            #end
            reg0 = _g_presentation_obj_custom_battle_designer_6_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_12,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_7_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_13,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_8_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_14,gstr.reg0_percent)
        #end
    elif var001 == _g_presentation_obj_custom_battle_designer_9:
        if _g_presentation_obj_custom_battle_designer_9_locked == 1 and var002 != _g_presentation_obj_custom_battle_designer_9_last_value:
            overlay_set_val(_g_presentation_obj_custom_battle_designer_9,_g_presentation_obj_custom_battle_designer_9_last_value)
        else:
            if var002 < _g_presentation_obj_custom_battle_designer_9_last_value:
                var014 = _g_presentation_obj_custom_battle_designer_9_last_value - var002
                if _g_presentation_obj_custom_battle_designer_10_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_11_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_9_last_value = var002
                _g_presentation_obj_custom_battle_designer_10_last_value += var015
                _g_presentation_obj_custom_battle_designer_11_last_value += var016
                if _g_presentation_obj_custom_battle_designer_10_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_10_last_value - 100
                    _g_presentation_obj_custom_battle_designer_11_last_value += var014
                    _g_presentation_obj_custom_battle_designer_10_last_value = 100
                elif _g_presentation_obj_custom_battle_designer_11_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_11_last_value - 100
                    _g_presentation_obj_custom_battle_designer_10_last_value += var014
                    _g_presentation_obj_custom_battle_designer_11_last_value = 100
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_10,_g_presentation_obj_custom_battle_designer_10_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_11,_g_presentation_obj_custom_battle_designer_11_last_value)
            elif var002 > _g_presentation_obj_custom_battle_designer_9_last_value:
                var014 = var002 - _g_presentation_obj_custom_battle_designer_9_last_value
                if _g_presentation_obj_custom_battle_designer_10_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_11_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_9_last_value = var002
                _g_presentation_obj_custom_battle_designer_10_last_value -= var015
                _g_presentation_obj_custom_battle_designer_11_last_value -= var016
                if _g_presentation_obj_custom_battle_designer_10_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_11_last_value += _g_presentation_obj_custom_battle_designer_10_last_value
                    _g_presentation_obj_custom_battle_designer_10_last_value = 0
                elif _g_presentation_obj_custom_battle_designer_11_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_10_last_value += _g_presentation_obj_custom_battle_designer_11_last_value
                    _g_presentation_obj_custom_battle_designer_11_last_value = 0
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_10,_g_presentation_obj_custom_battle_designer_10_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_11,_g_presentation_obj_custom_battle_designer_11_last_value)
            #end
            reg0 = _g_presentation_obj_custom_battle_designer_9_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_15,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_10_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_16,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_11_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_17,gstr.reg0_percent)
        #end
    elif var001 == _g_presentation_obj_custom_battle_designer_10:
        if _g_presentation_obj_custom_battle_designer_10_locked == 1 and var002 != _g_presentation_obj_custom_battle_designer_10_last_value:
            overlay_set_val(_g_presentation_obj_custom_battle_designer_10,_g_presentation_obj_custom_battle_designer_10_last_value)
        else:
            if var002 < _g_presentation_obj_custom_battle_designer_10_last_value:
                var014 = _g_presentation_obj_custom_battle_designer_10_last_value - var002
                if _g_presentation_obj_custom_battle_designer_9_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_11_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_10_last_value = var002
                _g_presentation_obj_custom_battle_designer_9_last_value += var015
                _g_presentation_obj_custom_battle_designer_11_last_value += var016
                if _g_presentation_obj_custom_battle_designer_9_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_9_last_value - 100
                    _g_presentation_obj_custom_battle_designer_11_last_value += var014
                    _g_presentation_obj_custom_battle_designer_9_last_value = 100
                elif _g_presentation_obj_custom_battle_designer_11_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_11_last_value - 100
                    _g_presentation_obj_custom_battle_designer_9_last_value += var014
                    _g_presentation_obj_custom_battle_designer_11_last_value = 100
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_9,_g_presentation_obj_custom_battle_designer_9_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_11,_g_presentation_obj_custom_battle_designer_11_last_value)
            elif var002 > _g_presentation_obj_custom_battle_designer_10_last_value:
                var014 = var002 - _g_presentation_obj_custom_battle_designer_10_last_value
                if _g_presentation_obj_custom_battle_designer_9_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_11_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_10_last_value = var002
                _g_presentation_obj_custom_battle_designer_9_last_value -= var015
                _g_presentation_obj_custom_battle_designer_11_last_value -= var016
                if _g_presentation_obj_custom_battle_designer_9_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_11_last_value += _g_presentation_obj_custom_battle_designer_9_last_value
                    _g_presentation_obj_custom_battle_designer_9_last_value = 0
                elif _g_presentation_obj_custom_battle_designer_11_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_9_last_value += _g_presentation_obj_custom_battle_designer_11_last_value
                    _g_presentation_obj_custom_battle_designer_11_last_value = 0
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_9,_g_presentation_obj_custom_battle_designer_9_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_11,_g_presentation_obj_custom_battle_designer_11_last_value)
            #end
            reg0 = _g_presentation_obj_custom_battle_designer_9_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_15,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_10_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_16,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_11_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_17,gstr.reg0_percent)
        #end
    elif var001 == _g_presentation_obj_custom_battle_designer_11:
        if _g_presentation_obj_custom_battle_designer_11_locked == 1 and var002 != _g_presentation_obj_custom_battle_designer_11_last_value:
            overlay_set_val(_g_presentation_obj_custom_battle_designer_11,_g_presentation_obj_custom_battle_designer_11_last_value)
        else:
            if var002 < _g_presentation_obj_custom_battle_designer_11_last_value:
                var014 = _g_presentation_obj_custom_battle_designer_11_last_value - var002
                if _g_presentation_obj_custom_battle_designer_10_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_9_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_11_last_value = var002
                _g_presentation_obj_custom_battle_designer_10_last_value += var015
                _g_presentation_obj_custom_battle_designer_9_last_value += var016
                if _g_presentation_obj_custom_battle_designer_10_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_10_last_value - 100
                    _g_presentation_obj_custom_battle_designer_9_last_value += var014
                    _g_presentation_obj_custom_battle_designer_10_last_value = 100
                elif _g_presentation_obj_custom_battle_designer_9_last_value > 100:
                    var014 = _g_presentation_obj_custom_battle_designer_9_last_value - 100
                    _g_presentation_obj_custom_battle_designer_10_last_value += var014
                    _g_presentation_obj_custom_battle_designer_9_last_value = 100
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_10,_g_presentation_obj_custom_battle_designer_10_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_9,_g_presentation_obj_custom_battle_designer_9_last_value)
            elif var002 > _g_presentation_obj_custom_battle_designer_11_last_value:
                var014 = var002 - _g_presentation_obj_custom_battle_designer_11_last_value
                if _g_presentation_obj_custom_battle_designer_10_locked == 1:
                    var015 = 0
                    var016 = var014
                elif _g_presentation_obj_custom_battle_designer_9_locked == 1:
                    var015 = var014
                    var016 = 0
                else:
                    var015 = var014 / 2
                    var016 = var014 - var015
                    if var015 != var016:
                        random_x_017 = store_random_in_range(0,2)
                        if random_x_017 == 0:
                            var016 -= 1
                            var015 += 1
                        #end
                    #end
                #end
                _g_presentation_obj_custom_battle_designer_11_last_value = var002
                _g_presentation_obj_custom_battle_designer_10_last_value -= var015
                _g_presentation_obj_custom_battle_designer_9_last_value -= var016
                if _g_presentation_obj_custom_battle_designer_10_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_9_last_value += _g_presentation_obj_custom_battle_designer_10_last_value
                    _g_presentation_obj_custom_battle_designer_10_last_value = 0
                elif _g_presentation_obj_custom_battle_designer_9_last_value < 0:
                    _g_presentation_obj_custom_battle_designer_10_last_value += _g_presentation_obj_custom_battle_designer_9_last_value
                    _g_presentation_obj_custom_battle_designer_9_last_value = 0
                #end
                overlay_set_val(_g_presentation_obj_custom_battle_designer_10,_g_presentation_obj_custom_battle_designer_10_last_value)
                overlay_set_val(_g_presentation_obj_custom_battle_designer_9,_g_presentation_obj_custom_battle_designer_9_last_value)
            #end
            reg0 = _g_presentation_obj_custom_battle_designer_9_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_15,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_10_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_16,gstr.reg0_percent)
            reg0 = _g_presentation_obj_custom_battle_designer_11_last_value
            overlay_set_text(_g_presentation_obj_custom_battle_designer_17,gstr.reg0_percent)
        #end
    elif var001 == _g_presentation_obj_custom_battle_designer_19:
        _g_is_quick_battle = 1
        scene_id_018 = _g_quick_battle_map
        if _g_quick_battle_game_type == 0:
            var019 = mt.quick_battle_battle
            modify_visitors_at_site(scene_id_018)
            spawn_quick_battle_army(0,_g_quick_battle_team_1_faction,_g_presentation_obj_custom_battle_designer_6_last_value,_g_presentation_obj_custom_battle_designer_7_last_value,_g_presentation_obj_custom_battle_designer_8_last_value,0,1)
            spawn_quick_battle_army(16,_g_quick_battle_team_2_faction,_g_presentation_obj_custom_battle_designer_9_last_value,_g_presentation_obj_custom_battle_designer_10_last_value,_g_presentation_obj_custom_battle_designer_11_last_value,0,0)
        elif _g_quick_battle_game_type == 1:
            var019 = mt.quick_battle_siege
            modify_visitors_at_site(scene_id_018)
            spawn_quick_battle_army(16,_g_quick_battle_team_1_faction,_g_presentation_obj_custom_battle_designer_6_last_value,_g_presentation_obj_custom_battle_designer_7_last_value,_g_presentation_obj_custom_battle_designer_8_last_value,0,1)
            spawn_quick_battle_army(0,_g_quick_battle_team_2_faction,_g_presentation_obj_custom_battle_designer_9_last_value,_g_presentation_obj_custom_battle_designer_10_last_value,_g_presentation_obj_custom_battle_designer_11_last_value,1,0)
        else:
            var019 = mt.quick_battle_siege
            modify_visitors_at_site(scene_id_018)
            spawn_quick_battle_army(0,_g_quick_battle_team_1_faction,_g_presentation_obj_custom_battle_designer_6_last_value,_g_presentation_obj_custom_battle_designer_7_last_value,_g_presentation_obj_custom_battle_designer_8_last_value,1,1)
            spawn_quick_battle_army(16,_g_quick_battle_team_2_faction,_g_presentation_obj_custom_battle_designer_9_last_value,_g_presentation_obj_custom_battle_designer_10_last_value,_g_presentation_obj_custom_battle_designer_11_last_value,0,0)
        #end
        set_jump_mission(var019)
        jump_to_menu(mnu.custom_battle_end)
        jump_to_scene(scene_id_018)
        change_screen_mission()
        presentation_set_duration(0)
    elif var001 == _g_presentation_obj_custom_battle_designer_20:
        presentation_set_duration(0)
    #end
event.codeBlock = code
game_custom_battle_designer.add_event(event)
event = MouseEnterLeaveEvent()
def code(var001, var002):
    var001_list1 = [
    _g_presentation_obj_custom_battle_designer_11,
    _g_presentation_obj_custom_battle_designer_10,
    _g_presentation_obj_custom_battle_designer_9,
    _g_presentation_obj_custom_battle_designer_8,
    _g_presentation_obj_custom_battle_designer_7,
    _g_presentation_obj_custom_battle_designer_6,
    ]
    if var001 in var001_list1:
        if var002 == 1:
            if var001 == _g_presentation_obj_custom_battle_last_mouse_over_object:
                _g_presentation_obj_custom_battle_last_mouse_over_object = -1
            #end
        #end
    else:
        _g_presentation_obj_custom_battle_last_mouse_over_object = var001
    #end
event.codeBlock = code
game_custom_battle_designer.add_event(event)
event = RunEvent()
def code():
    if key_clicked(1) or key_clicked(248):
        presentation_set_duration(0)
    elif key_clicked(225) and _g_presentation_obj_custom_battle_last_mouse_over_object != -1:
        if _g_presentation_obj_custom_battle_last_mouse_over_object == _g_presentation_obj_custom_battle_designer_6:
            if _g_presentation_obj_custom_battle_designer_6_locked == 0:
                _g_presentation_obj_custom_battle_designer_6_locked = 1
                _g_presentation_obj_custom_battle_designer_7_locked = 0
                _g_presentation_obj_custom_battle_designer_8_locked = 0
            else:
                _g_presentation_obj_custom_battle_designer_6_locked = 0
            #end
        elif _g_presentation_obj_custom_battle_last_mouse_over_object == _g_presentation_obj_custom_battle_designer_7:
            if _g_presentation_obj_custom_battle_designer_7_locked == 0:
                _g_presentation_obj_custom_battle_designer_6_locked = 0
                _g_presentation_obj_custom_battle_designer_7_locked = 1
                _g_presentation_obj_custom_battle_designer_8_locked = 0
            else:
                _g_presentation_obj_custom_battle_designer_7_locked = 0
            #end
        elif _g_presentation_obj_custom_battle_last_mouse_over_object == _g_presentation_obj_custom_battle_designer_8:
            if _g_presentation_obj_custom_battle_designer_8_locked == 0:
                _g_presentation_obj_custom_battle_designer_6_locked = 0
                _g_presentation_obj_custom_battle_designer_7_locked = 0
                _g_presentation_obj_custom_battle_designer_8_locked = 1
            else:
                _g_presentation_obj_custom_battle_designer_8_locked = 0
            #end
        elif _g_presentation_obj_custom_battle_last_mouse_over_object == _g_presentation_obj_custom_battle_designer_9:
            if _g_presentation_obj_custom_battle_designer_9_locked == 0:
                _g_presentation_obj_custom_battle_designer_9_locked = 1
                _g_presentation_obj_custom_battle_designer_10_locked = 0
                _g_presentation_obj_custom_battle_designer_11_locked = 0
            else:
                _g_presentation_obj_custom_battle_designer_9_locked = 0
            #end
        elif _g_presentation_obj_custom_battle_last_mouse_over_object == _g_presentation_obj_custom_battle_designer_10:
            if _g_presentation_obj_custom_battle_designer_10_locked == 0:
                _g_presentation_obj_custom_battle_designer_9_locked = 0
                _g_presentation_obj_custom_battle_designer_10_locked = 1
                _g_presentation_obj_custom_battle_designer_11_locked = 0
            else:
                _g_presentation_obj_custom_battle_designer_10_locked = 0
            #end
        elif _g_presentation_obj_custom_battle_last_mouse_over_object == _g_presentation_obj_custom_battle_designer_11:
            if _g_presentation_obj_custom_battle_designer_11_locked == 0:
                _g_presentation_obj_custom_battle_designer_9_locked = 0
                _g_presentation_obj_custom_battle_designer_10_locked = 0
                _g_presentation_obj_custom_battle_designer_11_locked = 1
            else:
                _g_presentation_obj_custom_battle_designer_11_locked = 0
            #end
        #end
    #end
event.codeBlock = code
game_custom_battle_designer.add_event(event)


game_multiplayer_admin_panel = Presentation("game_multiplayer_admin_panel")
event = LoadEvent()
def code():
    _g_multiplayer_game_type_list1 = [
    6,
    3,
    2,
    ]
    _g_multiplayer_game_type_list1 = [
    3,
    2,
    ]
    _g_multiplayer_game_type_list1 = [
    6,
    3,
    2,
    ]
    _g_multiplayer_game_type_list1 = [
    6,
    3,
    2,
    ]
    _g_multiplayer_game_type_list1 = [
    6,
    3,
    2,
    ]
    _g_multiplayer_game_type_list1 = [
    6,
    3,
    2,
    4,
    ]
    _g_multiplayer_game_type_list1 = [
    6,
    5,
    4,
    3,
    2,
    1,
    ]
    _g_multiplayer_selected_map_list2 = [
    scn.random_multi_steppe_large,
    scn.random_multi_steppe_medium,
    ]
    _g_multiplayer_selected_map_list2 = [
    scn.random_multi_plain_large,
    scn.random_multi_plain_medium,
    ]
    set_fixed_point_multiplier(1000)
    _g_presentation_obj_admin_panel_1 = -1
    _g_presentation_obj_admin_panel_2 = -1
    _g_presentation_obj_admin_panel_3 = -1
    _g_presentation_obj_admin_panel_4 = -1
    _g_presentation_obj_admin_panel_5 = -1
    _g_presentation_obj_admin_panel_6 = -1
    _g_presentation_obj_admin_panel_7 = -1
    _g_presentation_obj_admin_panel_8 = -1
    _g_presentation_obj_admin_panel_9 = -1
    _g_presentation_obj_admin_panel_10 = -1
    _g_presentation_obj_admin_panel_11 = -1
    _g_presentation_obj_admin_panel_12 = -1
    _g_presentation_obj_admin_panel_13 = -1
    _g_presentation_obj_admin_panel_14 = -1
    _g_presentation_obj_admin_panel_15 = -1
    _g_presentation_obj_admin_panel_16 = -1
    _g_presentation_obj_admin_panel_17 = -1
    _g_presentation_obj_admin_panel_18 = -1
    _g_presentation_obj_admin_panel_19 = -1
    _g_presentation_obj_admin_panel_20 = -1
    _g_presentation_obj_admin_panel_21 = -1
    _g_presentation_obj_admin_panel_22 = -1
    _g_presentation_obj_admin_panel_23 = -1
    _g_presentation_obj_admin_panel_24 = -1
    _g_presentation_obj_admin_panel_25 = -1
    _g_presentation_obj_admin_panel_26 = -1
    _g_presentation_obj_admin_panel_27 = -1
    _g_presentation_obj_admin_panel_28 = -1
    _g_presentation_obj_admin_panel_29 = -1
    _g_presentation_obj_admin_panel_30 = -1
    _g_presentation_obj_admin_panel_31 = -1
    _g_presentation_obj_admin_panel_32 = -1
    _g_presentation_obj_admin_panel_33 = -1
    _g_presentation_obj_admin_panel_34 = -1
    _g_presentation_obj_admin_panel_35 = -1
    _g_presentation_obj_admin_panel_36 = -1
    _g_presentation_obj_admin_panel_37 = -1
    _g_presentation_obj_admin_panel_38 = -1
    _g_presentation_obj_admin_panel_39 = -1
    _g_presentation_obj_admin_panel_40 = -1
    _g_presentation_obj_admin_panel_41 = -1
    _g_presentation_obj_admin_panel_42 = -1
    _g_presentation_obj_admin_panel_43 = -1
    if _g_multiplayer_selected_map == scn.multi_scene_1:
        var001 = mesh.mp_ui_host_maps_1
    elif _g_multiplayer_selected_map == scn.multi_scene_2:
        var001 = mesh.mp_ui_host_maps_2
    elif _g_multiplayer_selected_map == scn.multi_scene_3:
        var001 = mesh.mp_ui_host_maps_3
    elif _g_multiplayer_selected_map == scn.multi_scene_4:
        var001 = mesh.mp_ui_host_maps_4
    elif _g_multiplayer_selected_map == scn.multi_scene_5:
        var001 = mesh.mp_ui_host_maps_5
    elif _g_multiplayer_selected_map == scn.multi_scene_6:
        var001 = mesh.mp_ui_host_maps_6
    elif _g_multiplayer_selected_map == scn.multi_scene_7:
        var001 = mesh.mp_ui_host_maps_7
    elif _g_multiplayer_selected_map == scn.multi_scene_8:
        var001 = mesh.mp_ui_host_maps_8
    elif _g_multiplayer_selected_map == scn.multi_scene_9:
        var001 = mesh.mp_ui_host_maps_9
    elif _g_multiplayer_selected_map == scn.multi_scene_10:
        var001 = mesh.mp_ui_host_maps_10
    elif _g_multiplayer_selected_map == scn.multi_scene_11:
        var001 = mesh.mp_ui_host_maps_11
    elif _g_multiplayer_selected_map == scn.multi_scene_12:
        var001 = mesh.mp_ui_host_maps_12
    elif _g_multiplayer_selected_map == scn.multi_scene_13:
        var001 = mesh.mp_ui_host_maps_13
    elif _g_multiplayer_selected_map == scn.multi_scene_14:
        var001 = mesh.mp_ui_host_maps_14
    elif _g_multiplayer_selected_map == scn.multi_scene_15:
        var001 = mesh.mp_ui_host_maps_15
    elif _g_multiplayer_selected_map == scn.multi_scene_16:
        var001 = mesh.mp_ui_host_maps_16
    elif _g_multiplayer_selected_map == scn.multi_scene_17:
        var001 = mesh.mp_ui_host_maps_17
    elif _g_multiplayer_selected_map == scn.multi_scene_18:
        var001 = mesh.mp_ui_host_maps_18
    elif _g_multiplayer_selected_map == scn.multi_scene_19:
        var001 = mesh.mp_ui_host_maps_19
    elif _g_multiplayer_selected_map == scn.multi_scene_20:
        var001 = mesh.mp_ui_host_maps_20
    elif _g_multiplayer_selected_map == scn.multi_scene_21:
        var001 = mesh.mp_ui_host_maps_21
    elif _g_multiplayer_selected_map in _g_multiplayer_selected_map_list2:
        var001 = mesh.mp_ui_host_maps_randomp
    elif _g_multiplayer_selected_map in _g_multiplayer_selected_map_list2:
        var001 = mesh.mp_ui_host_maps_randoms
    else:
        var001 = mesh.mp_ui_host_maps_randomp
    #end
    create_mesh_overlay(reg0,var001)
    position_set_x(1,-1)
    position_set_y(1,550)
    overlay_set_position(reg0,1)
    position_set_x(1,1002)
    position_set_y(1,1002)
    overlay_set_size(reg0,1)
    create_mesh_overlay(reg0,mesh.mp_ui_host_main)
    position_set_x(1,-1)
    position_set_y(1,-1)
    overlay_set_position(reg0,1)
    position_set_x(1,1002)
    position_set_y(1,1002)
    overlay_set_size(reg0,1)
    var002 = 1240
    var003 = 40
    if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
        var002 += var003
        var002 += var003
        if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
            var002 += var003
            if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
                var002 += var003
                if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
                    var002 += var003
                #end
            #end
        #end
    #end
    if _g_multiplayer_is_game_type_captain == 1:
        var002 -= var003
    #end
    if _g_multiplayer_game_type == 8:
        var002 -= var003
        var002 -= var003
        var002 -= var003
    #end
    str_clear(0)
    create_text_overlay(_g_presentation_obj_admin_panel_container,0,8192)
    position_set_x(1,59)
    position_set_y(1,50)
    overlay_set_position(_g_presentation_obj_admin_panel_container,1)
    position_set_x(1,640)
    position_set_y(1,520)
    overlay_set_area_size(_g_presentation_obj_admin_panel_container,1)
    set_container_overlay(_g_presentation_obj_admin_panel_container)
    create_text_overlay(reg0,gstr.add_to_official_game_servers_list,0)
    position_set_x(1,30)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_check_box_overlay(_g_presentation_obj_admin_panel_14,mesh.checkbox_off,mesh.checkbox_on)
    position_set_x(1,7)
    var004 = var002 + 7
    position_set_y(1,var004)
    overlay_set_position(_g_presentation_obj_admin_panel_14,1)
    server_add_to_game_servers_list = server_get_add_to_game_servers_list()
    overlay_set_val(_g_presentation_obj_admin_panel_14,server_add_to_game_servers_list)
    var002 -= var003
    create_text_overlay(reg0,gstr.enable_valve_anti_cheat,0)
    position_set_x(1,30)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_check_box_overlay(_g_presentation_obj_admin_panel_41,mesh.checkbox_off,mesh.checkbox_on)
    position_set_x(1,7)
    var004 = var002 + 7
    position_set_y(1,var004)
    overlay_set_position(_g_presentation_obj_admin_panel_41,1)
    overlay_set_val(_g_presentation_obj_admin_panel_41,0)
    server_set_anti_cheat(0)
    var002 -= var003
    create_text_overlay(reg0,gstr.server_name,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    s0 = str_store_server_name()
    if _g_multiplayer_renaming_server_allowed == 1:
        create_simple_text_box_overlay(_g_presentation_obj_admin_panel_20)
        position_set_x(1,390)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_20,1)
        overlay_set_text(_g_presentation_obj_admin_panel_20,0)
    else:
        _g_presentation_obj_admin_panel_20 = -1
        create_text_overlay(reg0,0,0)
        position_set_x(1,385)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
    #end
    var002 -= var003
    create_text_overlay(reg0,gstr.game_password,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_simple_text_box_overlay(_g_presentation_obj_admin_panel_9)
    position_set_x(1,390)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_9,1)
    s0 = str_store_server_password()
    overlay_set_text(_g_presentation_obj_admin_panel_9,0)
    var002 -= var003
    create_text_overlay(reg0,gstr.welcome_message,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_simple_text_box_overlay(_g_presentation_obj_admin_panel_32)
    position_set_x(1,390)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_32,1)
    s0 = str_store_welcome_message()
    overlay_set_text(_g_presentation_obj_admin_panel_32,0)
    var002 -= var003
    create_text_overlay(reg0,gstr.map,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    multiplayer_fill_map_game_types(_g_multiplayer_game_type)
    var006 = reg0
    var007 = 0
    if var006 > 12:
        create_combo_label_overlay(_g_presentation_obj_admin_panel_1)
    else:
        create_combo_button_overlay(_g_presentation_obj_admin_panel_1)
    #end
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_admin_panel_1,1)
    if var006 > 14:
        position_set_x(1,465)
    else:
        position_set_x(1,490)
    #end
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_1,1)
    troop_slot_008 = troop_get_slot(trp.multiplayer_data,0)
    var009 = 0
    for var010 in range(0, var006):
        slot_no_011 = var010 + 0
        troop_slot_012 = troop_get_slot(trp.multiplayer_data,slot_no_011)
        var013 = troop_slot_012 - scn.multi_scene_1
        var013 = var013 + gstr.multi_scene_1
        s0 = str_store_string(var013)
        overlay_add_item(_g_presentation_obj_admin_panel_1,0)
        if troop_slot_012 == _g_multiplayer_selected_map:
            var007 = var010
            var009 = 1
        #end
    #end
    overlay_set_val(_g_presentation_obj_admin_panel_1,var007)
    var002 -= var003
    create_text_overlay(reg0,gstr.game_type,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    if _g_multiplayer_changing_game_type_allowed == 1:
        create_combo_button_overlay(_g_presentation_obj_admin_panel_10)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(_g_presentation_obj_admin_panel_10,1)
        position_set_x(1,490)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_10,1)
        for var014 in range(0, 9):
            var013 = var014 + gstr.multi_game_type_1
            s0 = str_store_string(var013)
            overlay_add_item(_g_presentation_obj_admin_panel_10,0)
        #end
        overlay_set_val(_g_presentation_obj_admin_panel_10,_g_multiplayer_game_type)
    else:
        _g_presentation_obj_admin_panel_10 = -1
        var013 = _g_multiplayer_game_type + gstr.multi_game_type_1
        s0 = str_store_string(var013)
        create_text_overlay(reg0,0,0)
        position_set_x(1,385)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
    #end
    var002 -= var003
    if _g_multiplayer_game_type == 8:
        create_text_overlay(reg0,gstr.ccoop_difficulty,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_combo_button_overlay(_g_presentation_obj_admin_panel_43)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(_g_presentation_obj_admin_panel_43,1)
        position_set_x(1,490)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_43,1)
        overlay_add_item(_g_presentation_obj_admin_panel_43,gstr.ccoop_easy)
        overlay_add_item(_g_presentation_obj_admin_panel_43,gstr.ccoop_normal)
        overlay_add_item(_g_presentation_obj_admin_panel_43,gstr.ccoop_endless)
        overlay_set_val(_g_presentation_obj_admin_panel_43,_g_multiplayer_ccoop_difficulty)
        var002 -= var003
    #end
    reg1 = 1
    create_text_overlay(reg0,gstr.team_reg1_faction,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_combo_button_overlay(_g_presentation_obj_admin_panel_11)
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_admin_panel_11,1)
    position_set_x(1,490)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_11,1)
    multiplayer_fill_available_factions_combo_button(_g_presentation_obj_admin_panel_11,_g_multiplayer_next_team_1_faction,_g_multiplayer_next_team_2_faction)
    var002 -= var003
    if True:
        reg1 = 2
        create_text_overlay(reg0,gstr.team_reg1_faction,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_combo_button_overlay(_g_presentation_obj_admin_panel_12)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(_g_presentation_obj_admin_panel_12,1)
        position_set_x(1,490)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_12,1)
        multiplayer_fill_available_factions_combo_button(_g_presentation_obj_admin_panel_12,_g_multiplayer_next_team_2_faction,_g_multiplayer_next_team_1_faction)
        var002 -= var003
    #end
    reg1 = 1
    create_text_overlay(reg0,gstr.max_number_of_players,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    if _g_multiplayer_game_type == 8:
        var015 = 12 + 1
        create_number_box_overlay(_g_presentation_obj_admin_panel_21,2,var015)
        if True:
            server_max_players = server_get_max_num_players()
            if server_max_players > 12:
                multiplayer_send_int_to_server(3,12)
            #end
        #end
    else:
        create_number_box_overlay(_g_presentation_obj_admin_panel_21,2,201)
    #end
    position_set_x(1,390)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_21,1)
    server_max_players = server_get_max_num_players()
    overlay_set_val(_g_presentation_obj_admin_panel_21,server_max_players)
    if _g_multiplayer_game_type != 8:
        var002 -= var003
        reg1 = 1
        create_text_overlay(reg0,gstr.number_of_bots_in_team_reg1,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_number_box_overlay(_g_presentation_obj_admin_panel_3,0,_g_multiplayer_max_num_bots)
        position_set_x(1,390)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_3,1)
        overlay_set_val(_g_presentation_obj_admin_panel_3,_g_multiplayer_num_bots_team_1)
        var002 -= var003
        reg1 = 2
        create_text_overlay(reg0,gstr.number_of_bots_in_team_reg1,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_number_box_overlay(_g_presentation_obj_admin_panel_4,0,_g_multiplayer_max_num_bots)
        position_set_x(1,390)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_4,1)
        overlay_set_val(_g_presentation_obj_admin_panel_4,_g_multiplayer_num_bots_team_2)
    #end
    if _g_multiplayer_game_type != 0 and _g_multiplayer_game_type != 7:
        var002 -= var003
        create_text_overlay(reg0,gstr.allow_friendly_fire,0)
        position_set_x(1,30)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_check_box_overlay(_g_presentation_obj_admin_panel_5,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(1,7)
        var004 = var002 + 7
        position_set_y(1,var004)
        overlay_set_position(_g_presentation_obj_admin_panel_5,1)
        server_friendly_fire = server_get_friendly_fire()
        overlay_set_val(_g_presentation_obj_admin_panel_5,server_friendly_fire)
        var002 -= var003
        create_text_overlay(reg0,gstr.allow_melee_friendly_fire,0)
        position_set_x(1,30)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_check_box_overlay(_g_presentation_obj_admin_panel_36,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(1,7)
        var004 = var002 + 7
        position_set_y(1,var004)
        overlay_set_position(_g_presentation_obj_admin_panel_36,1)
        server_melee_friendly_fire = server_get_melee_friendly_fire()
        overlay_set_val(_g_presentation_obj_admin_panel_36,server_melee_friendly_fire)
    #end
    var002 -= var003
    create_text_overlay(reg0,gstr.friendly_fire_damage_self_ratio,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_number_box_overlay(_g_presentation_obj_admin_panel_37,0,101)
    position_set_x(1,390)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_37,1)
    server_friendly_fire_damage_self_ratio = server_get_friendly_fire_damage_self_ratio()
    overlay_set_val(_g_presentation_obj_admin_panel_37,server_friendly_fire_damage_self_ratio)
    var002 -= var003
    create_text_overlay(reg0,gstr.friendly_fire_damage_friend_ratio,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_number_box_overlay(_g_presentation_obj_admin_panel_38,0,101)
    position_set_x(1,390)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_38,1)
    server_friendly_fire_damage_friend_ratio = server_get_friendly_fire_damage_friend_ratio()
    overlay_set_val(_g_presentation_obj_admin_panel_38,server_friendly_fire_damage_friend_ratio)
    var002 -= var003
    create_text_overlay(reg0,gstr.spectator_camera,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_combo_button_overlay(_g_presentation_obj_admin_panel_19)
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_admin_panel_19,1)
    position_set_x(1,490)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_19,1)
    overlay_add_item(_g_presentation_obj_admin_panel_19,gstr.free)
    overlay_add_item(_g_presentation_obj_admin_panel_19,gstr.stick_to_any_player)
    overlay_add_item(_g_presentation_obj_admin_panel_19,gstr.stick_to_team_members)
    overlay_add_item(_g_presentation_obj_admin_panel_19,gstr.stick_to_team_members_view)
    server_ghost_mode = server_get_ghost_mode()
    overlay_set_val(_g_presentation_obj_admin_panel_19,server_ghost_mode)
    var002 -= var003
    create_text_overlay(reg0,gstr.control_block_direction,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_combo_button_overlay(_g_presentation_obj_admin_panel_15)
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_admin_panel_15,1)
    position_set_x(1,490)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_15,1)
    overlay_add_item(_g_presentation_obj_admin_panel_15,gstr.automatic)
    overlay_add_item(_g_presentation_obj_admin_panel_15,gstr.by_mouse_movement)
    server_control_block_direction = server_get_control_block_dir()
    overlay_set_val(_g_presentation_obj_admin_panel_15,server_control_block_direction)
    var002 -= var003
    create_text_overlay(reg0,gstr.combat_speed,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_combo_button_overlay(_g_presentation_obj_admin_panel_26)
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_admin_panel_26,1)
    position_set_x(1,490)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_26,1)
    overlay_add_item(_g_presentation_obj_admin_panel_26,gstr.combat_speed_0)
    overlay_add_item(_g_presentation_obj_admin_panel_26,gstr.combat_speed_1)
    overlay_add_item(_g_presentation_obj_admin_panel_26,gstr.combat_speed_2)
    overlay_add_item(_g_presentation_obj_admin_panel_26,gstr.combat_speed_3)
    overlay_add_item(_g_presentation_obj_admin_panel_26,gstr.combat_speed_4)
    server_combat_speed = server_get_combat_speed()
    overlay_set_val(_g_presentation_obj_admin_panel_26,server_combat_speed)
    if _g_multiplayer_game_type != 5 and _g_multiplayer_game_type != 8:
        var002 -= var003
        create_text_overlay(reg0,gstr.map_time_limit,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_number_box_overlay(_g_presentation_obj_admin_panel_7,5,121)
        position_set_x(1,390)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_7,1)
        overlay_set_val(_g_presentation_obj_admin_panel_7,_g_multiplayer_game_max_minutes)
    else:
        _g_presentation_obj_admin_panel_7 = -1
    #end
    if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
        var002 -= var003
        create_text_overlay(reg0,gstr.round_time_limit,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_number_box_overlay(_g_presentation_obj_admin_panel_16,60,901)
        position_set_x(1,390)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_16,1)
        overlay_set_val(_g_presentation_obj_admin_panel_16,_g_multiplayer_round_max_seconds)
    else:
        _g_presentation_obj_admin_panel_16 = -1
    #end
    if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
        var002 -= var003
        create_text_overlay(reg0,gstr.players_take_control_of_a_bot_after_death,0)
        position_set_x(1,30)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_check_box_overlay(_g_presentation_obj_admin_panel_25,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(1,7)
        var004 = var002 + 7
        position_set_y(1,var004)
        overlay_set_position(_g_presentation_obj_admin_panel_25,1)
        overlay_set_val(_g_presentation_obj_admin_panel_25,_g_multiplayer_player_respawn_as_bot)
    else:
        _g_presentation_obj_admin_panel_25 = -1
    #end
    if _g_multiplayer_game_type == 6:
        var002 -= var003
        create_text_overlay(reg0,gstr.defender_spawn_count_limit,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_combo_button_overlay(_g_presentation_obj_admin_panel_27)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(_g_presentation_obj_admin_panel_27,1)
        position_set_x(1,490)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_27,1)
        reg0 = 5
        overlay_add_item(_g_presentation_obj_admin_panel_27,gstr.reg0)
        reg0 = 4
        overlay_add_item(_g_presentation_obj_admin_panel_27,gstr.reg0)
        reg0 = 3
        overlay_add_item(_g_presentation_obj_admin_panel_27,gstr.reg0)
        reg0 = 2
        overlay_add_item(_g_presentation_obj_admin_panel_27,gstr.reg0)
        reg0 = 1
        overlay_add_item(_g_presentation_obj_admin_panel_27,gstr.reg0)
        overlay_add_item(_g_presentation_obj_admin_panel_27,gstr.unlimited)
        var025 = 5 - _g_multiplayer_number_of_respawn_count
        overlay_set_val(_g_presentation_obj_admin_panel_27,var025)
    else:
        _g_presentation_obj_admin_panel_27 = -1
    #end
    if _g_multiplayer_game_type != 8:
        var002 -= var003
        create_text_overlay(reg0,gstr.team_points_limit,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_number_box_overlay(_g_presentation_obj_admin_panel_8,3,1001)
        position_set_x(1,390)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_8,1)
        overlay_set_val(_g_presentation_obj_admin_panel_8,_g_multiplayer_game_max_points)
    #end
    if _g_multiplayer_game_type == 5:
        var002 -= var003
        create_text_overlay(reg0,gstr.point_gained_from_flags,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_number_box_overlay(_g_presentation_obj_admin_panel_17,25,401)
        position_set_x(1,390)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_17,1)
        overlay_set_val(_g_presentation_obj_admin_panel_17,_g_multiplayer_point_gained_from_flags)
    else:
        _g_presentation_obj_admin_panel_17 = -1
    #end
    if _g_multiplayer_game_type == 4:
        var002 -= var003
        create_text_overlay(reg0,gstr.point_gained_from_capturing_flag,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_number_box_overlay(_g_presentation_obj_admin_panel_18,0,11)
        position_set_x(1,390)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_18,1)
        overlay_set_val(_g_presentation_obj_admin_panel_18,_g_multiplayer_point_gained_from_capturing_flag)
    else:
        _g_presentation_obj_admin_panel_18 = -1
    #end
    if _g_multiplayer_game_type != 8:
        var002 -= var003
        create_text_overlay(reg0,gstr.respawn_period,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_number_box_overlay(_g_presentation_obj_admin_panel_6,3,31)
        position_set_x(1,390)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_6,1)
        overlay_set_val(_g_presentation_obj_admin_panel_6,_g_multiplayer_respawn_period)
    #end
    var002 -= var003
    create_text_overlay(reg0,gstr.initial_gold_multiplier,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_number_box_overlay(_g_presentation_obj_admin_panel_33,0,1001)
    position_set_x(1,390)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_33,1)
    overlay_set_val(_g_presentation_obj_admin_panel_33,_g_multiplayer_initial_gold_multiplier)
    var002 -= var003
    create_text_overlay(reg0,gstr.battle_earnings_multiplier,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_number_box_overlay(_g_presentation_obj_admin_panel_34,0,1001)
    position_set_x(1,390)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_34,1)
    overlay_set_val(_g_presentation_obj_admin_panel_34,_g_multiplayer_battle_earnings_multiplier)
    if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
        var002 -= var003
        create_text_overlay(reg0,gstr.round_earnings_multiplier,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_number_box_overlay(_g_presentation_obj_admin_panel_35,0,1001)
        position_set_x(1,390)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_35,1)
        overlay_set_val(_g_presentation_obj_admin_panel_35,_g_multiplayer_round_earnings_multiplier)
    else:
        _g_presentation_obj_admin_panel_35 = -1
    #end
    var002 -= var003
    create_text_overlay(reg0,gstr.make_kick_voteable,0)
    position_set_x(1,30)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_check_box_overlay(_g_presentation_obj_admin_panel_28,mesh.checkbox_off,mesh.checkbox_on)
    position_set_x(1,7)
    var004 = var002 + 7
    position_set_y(1,var004)
    overlay_set_position(_g_presentation_obj_admin_panel_28,1)
    overlay_set_val(_g_presentation_obj_admin_panel_28,_g_multiplayer_kick_voteable)
    var002 -= var003
    create_text_overlay(reg0,gstr.make_ban_voteable,0)
    position_set_x(1,30)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_check_box_overlay(_g_presentation_obj_admin_panel_29,mesh.checkbox_off,mesh.checkbox_on)
    position_set_x(1,7)
    var004 = var002 + 7
    position_set_y(1,var004)
    overlay_set_position(_g_presentation_obj_admin_panel_29,1)
    overlay_set_val(_g_presentation_obj_admin_panel_29,_g_multiplayer_ban_voteable)
    var002 -= var003
    create_text_overlay(reg0,gstr.make_maps_voteable,0)
    position_set_x(1,30)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_check_box_overlay(_g_presentation_obj_admin_panel_24,mesh.checkbox_off,mesh.checkbox_on)
    position_set_x(1,7)
    var004 = var002 + 7
    position_set_y(1,var004)
    overlay_set_position(_g_presentation_obj_admin_panel_24,1)
    overlay_set_val(_g_presentation_obj_admin_panel_24,_g_multiplayer_maps_voteable)
    var002 -= var003
    create_text_overlay(reg0,gstr.make_factions_voteable,0)
    position_set_x(1,30)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_check_box_overlay(_g_presentation_obj_admin_panel_23,mesh.checkbox_off,mesh.checkbox_on)
    position_set_x(1,7)
    var004 = var002 + 7
    position_set_y(1,var004)
    overlay_set_position(_g_presentation_obj_admin_panel_23,1)
    overlay_set_val(_g_presentation_obj_admin_panel_23,_g_multiplayer_factions_voteable)
    if _g_multiplayer_game_type != 8:
        var002 -= var003
        create_text_overlay(reg0,gstr.bots_upper_limit_for_votes,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        var026 = 51
        val_min(var026,_g_multiplayer_max_num_bots)
        create_number_box_overlay(_g_presentation_obj_admin_panel_22,0,var026)
        position_set_x(1,390)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_22,1)
        overlay_set_val(_g_presentation_obj_admin_panel_22,_g_multiplayer_num_bots_voteable)
    #end
    var002 -= var003
    create_text_overlay(reg0,gstr.valid_vote_ratio,0)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_number_box_overlay(_g_presentation_obj_admin_panel_30,50,101)
    position_set_x(1,390)
    position_set_y(1,var002)
    overlay_set_position(_g_presentation_obj_admin_panel_30,1)
    overlay_set_val(_g_presentation_obj_admin_panel_30,_g_multiplayer_valid_vote_ratio)
    if _g_multiplayer_game_type != 8:
        var002 -= var003
        create_text_overlay(reg0,gstr.auto_team_balance_limit,0)
        position_set_x(1,0)
        position_set_y(1,var002)
        overlay_set_position(reg0,1)
        create_combo_button_overlay(_g_presentation_obj_admin_panel_31)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(_g_presentation_obj_admin_panel_31,1)
        position_set_x(1,490)
        position_set_y(1,var002)
        overlay_set_position(_g_presentation_obj_admin_panel_31,1)
        overlay_add_item(_g_presentation_obj_admin_panel_31,gstr.unlimited)
        reg0 = 6
        overlay_add_item(_g_presentation_obj_admin_panel_31,gstr.reg0)
        reg0 = 5
        overlay_add_item(_g_presentation_obj_admin_panel_31,gstr.reg0)
        reg0 = 4
        overlay_add_item(_g_presentation_obj_admin_panel_31,gstr.reg0)
        reg0 = 3
        overlay_add_item(_g_presentation_obj_admin_panel_31,gstr.reg0)
        reg0 = 2
        overlay_add_item(_g_presentation_obj_admin_panel_31,gstr.reg0)
        if _g_multiplayer_auto_team_balance_limit >= 1000:
            overlay_set_val(_g_presentation_obj_admin_panel_31,0)
        else:
            var027 = 7 - _g_multiplayer_auto_team_balance_limit
            overlay_set_val(_g_presentation_obj_admin_panel_31,var027)
        #end
    #end
    var002 -= var003
    create_text_overlay(reg0,gstr.allow_player_banners,0)
    position_set_x(1,30)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_check_box_overlay(_g_presentation_obj_admin_panel_39,mesh.checkbox_off,mesh.checkbox_on)
    position_set_x(1,7)
    var004 = var002 + 7
    position_set_y(1,var004)
    overlay_set_position(_g_presentation_obj_admin_panel_39,1)
    overlay_set_val(_g_presentation_obj_admin_panel_39,_g_multiplayer_allow_player_banners)
    var002 -= var003
    create_text_overlay(reg0,gstr.disallow_ranged_weapons,0)
    position_set_x(1,30)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_check_box_overlay(_g_presentation_obj_admin_panel_42,mesh.checkbox_off,mesh.checkbox_on)
    position_set_x(1,7)
    var004 = var002 + 7
    position_set_y(1,var004)
    overlay_set_position(_g_presentation_obj_admin_panel_42,1)
    overlay_set_val(_g_presentation_obj_admin_panel_42,_g_multiplayer_disallow_ranged_weapons)
    var002 -= var003
    create_text_overlay(reg0,gstr.force_default_armor,0)
    position_set_x(1,30)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    create_check_box_overlay(_g_presentation_obj_admin_panel_40,mesh.checkbox_off,mesh.checkbox_on)
    position_set_x(1,7)
    var004 = var002 + 7
    position_set_y(1,var004)
    overlay_set_position(_g_presentation_obj_admin_panel_40,1)
    overlay_set_val(_g_presentation_obj_admin_panel_40,_g_multiplayer_force_default_armor)
    set_container_overlay(-1)
    create_button_overlay(_g_presentation_obj_admin_panel_13,gstr.back,16)
    position_set_x(1,825)
    position_set_y(1,50)
    overlay_set_position(_g_presentation_obj_admin_panel_13,1)
    position_set_x(1,1500)
    position_set_y(1,1500)
    overlay_set_size(_g_presentation_obj_admin_panel_13,1)
    create_button_overlay(_g_presentation_obj_admin_panel_2,gstr.start_map,16)
    position_set_x(1,825)
    position_set_y(1,90)
    overlay_set_position(_g_presentation_obj_admin_panel_2,1)
    position_set_x(1,1500)
    position_set_y(1,1500)
    overlay_set_size(_g_presentation_obj_admin_panel_2,1)
    presentation_set_duration(999999)
    if var009 == 0:
        _g_multiplayer_selected_map = troop_slot_008
        presentation_set_duration(0)
        start_presentation(prsnt.game_multiplayer_admin_panel)
    #end
event.codeBlock = code
game_multiplayer_admin_panel.add_event(event)
event = StateChangedEvent()
def code(var001, var002):
    if var001 == _g_presentation_obj_admin_panel_1:
        slot_no_003 = var002 + 0
        _g_multiplayer_selected_map = troop_get_slot(trp.multiplayer_data,slot_no_003)
        presentation_set_duration(0)
        start_presentation(prsnt.game_multiplayer_admin_panel)
    elif var001 == _g_presentation_obj_admin_panel_2:
        multiplayer_send_2_int_to_server(2,_g_multiplayer_selected_map,_g_multiplayer_game_type)
    elif var001 == _g_presentation_obj_admin_panel_3:
        multiplayer_send_2_int_to_server(4,1,var002)
    elif var001 == _g_presentation_obj_admin_panel_4:
        multiplayer_send_2_int_to_server(4,2,var002)
    elif var001 == _g_presentation_obj_admin_panel_5:
        multiplayer_send_int_to_server(5,var002)
    elif var001 == _g_presentation_obj_admin_panel_6:
        multiplayer_send_int_to_server(9,var002)
    elif var001 == _g_presentation_obj_admin_panel_7:
        multiplayer_send_int_to_server(10,var002)
    elif var001 == _g_presentation_obj_admin_panel_8:
        multiplayer_send_int_to_server(12,var002)
    elif var001 == _g_presentation_obj_admin_panel_9:
        multiplayer_send_string_to_server(16,0)
    elif var001 == _g_presentation_obj_admin_panel_10:
        _g_multiplayer_game_type = var002
        multiplayer_set_g_multiplayer_is_game_type_captain()
        if _g_multiplayer_is_game_type_captain == 1:
            if _g_multiplayer_game_type == 8:
                pass
            #end
        elif _g_multiplayer_next_team_2_faction >= fac.kingdoms_end:
            _g_multiplayer_next_team_2_faction = fac.kingdom_2
            multiplayer_send_2_int_to_server(17,2,_g_multiplayer_next_team_2_faction)
        #end
        presentation_set_duration(0)
        start_presentation(prsnt.game_multiplayer_admin_panel)
    elif var001 == _g_presentation_obj_admin_panel_11:
        _g_multiplayer_next_team_1_faction = var002 + fac.kingdom_1
        multiplayer_send_2_int_to_server(17,1,_g_multiplayer_next_team_1_faction)
        presentation_set_duration(0)
        start_presentation(prsnt.game_multiplayer_admin_panel)
    elif var001 == _g_presentation_obj_admin_panel_12:
        if var002 == 6:
            _g_multiplayer_next_team_2_faction = fac.outlaws
        elif var002 == 7:
            _g_multiplayer_next_team_2_faction = fac.ccoop_all_stars
        else:
            _g_multiplayer_next_team_2_faction = var002 + fac.kingdom_1
        #end
        multiplayer_send_2_int_to_server(17,2,_g_multiplayer_next_team_2_faction)
        presentation_set_duration(0)
        start_presentation(prsnt.game_multiplayer_admin_panel)
    elif var001 == _g_presentation_obj_admin_panel_13:
        presentation_set_duration(0)
    elif var001 == _g_presentation_obj_admin_panel_14:
        multiplayer_send_int_to_server(8,var002)
    elif var001 == _g_presentation_obj_admin_panel_15:
        multiplayer_send_int_to_server(7,var002)
    elif var001 == _g_presentation_obj_admin_panel_16:
        multiplayer_send_int_to_server(11,var002)
    elif var001 == _g_presentation_obj_admin_panel_17:
        multiplayer_send_int_to_server(13,var002)
    elif var001 == _g_presentation_obj_admin_panel_18:
        multiplayer_send_int_to_server(14,var002)
    elif var001 == _g_presentation_obj_admin_panel_19:
        multiplayer_send_int_to_server(6,var002)
    elif var001 == _g_presentation_obj_admin_panel_20:
        multiplayer_send_string_to_server(15,0)
    elif var001 == _g_presentation_obj_admin_panel_21:
        multiplayer_send_int_to_server(3,var002)
        if _g_multiplayer_is_game_type_captain == 1:
            if _g_multiplayer_game_type == 8:
                pass
            #end
        #end
    elif var001 == _g_presentation_obj_admin_panel_22:
        multiplayer_send_int_to_server(25,var002)
    elif var001 == _g_presentation_obj_admin_panel_23:
        multiplayer_send_int_to_server(26,var002)
    elif var001 == _g_presentation_obj_admin_panel_24:
        multiplayer_send_int_to_server(27,var002)
    elif var001 == _g_presentation_obj_admin_panel_25:
        multiplayer_send_int_to_server(28,var002)
    elif var001 == _g_presentation_obj_admin_panel_26:
        multiplayer_send_int_to_server(29,var002)
    elif var001 == _g_presentation_obj_admin_panel_27:
        var004 = 5 - var002
        multiplayer_send_int_to_server(30,var004)
    elif var001 == _g_presentation_obj_admin_panel_28:
        multiplayer_send_int_to_server(31,var002)
    elif var001 == _g_presentation_obj_admin_panel_29:
        multiplayer_send_int_to_server(32,var002)
    elif var001 == _g_presentation_obj_admin_panel_30:
        multiplayer_send_int_to_server(33,var002)
    elif var001 == _g_presentation_obj_admin_panel_31:
        if var002 == 0:
            multiplayer_send_int_to_server(34,1000)
        else:
            var004 = 7 - var002
            multiplayer_send_int_to_server(34,var004)
        #end
    elif var001 == _g_presentation_obj_admin_panel_32:
        server_set_welcome_message(0)
        multiplayer_send_string_to_server(35,0)
    elif var001 == _g_presentation_obj_admin_panel_33:
        multiplayer_send_int_to_server(36,var002)
    elif var001 == _g_presentation_obj_admin_panel_34:
        multiplayer_send_int_to_server(37,var002)
    elif var001 == _g_presentation_obj_admin_panel_35:
        multiplayer_send_int_to_server(38,var002)
    elif var001 == _g_presentation_obj_admin_panel_36:
        multiplayer_send_int_to_server(39,var002)
    elif var001 == _g_presentation_obj_admin_panel_37:
        multiplayer_send_int_to_server(40,var002)
    elif var001 == _g_presentation_obj_admin_panel_38:
        multiplayer_send_int_to_server(41,var002)
    elif var001 == _g_presentation_obj_admin_panel_39:
        multiplayer_send_int_to_server(42,var002)
    elif var001 == _g_presentation_obj_admin_panel_40:
        multiplayer_send_int_to_server(43,var002)
    elif var001 == _g_presentation_obj_admin_panel_41:
        multiplayer_send_int_to_server(44,var002)
    elif var001 == _g_presentation_obj_admin_panel_42:
        multiplayer_send_int_to_server(47,var002)
    elif var001 == _g_presentation_obj_admin_panel_43:
        _g_multiplayer_ccoop_difficulty = var002
        multiplayer_send_2_int_to_server(48,14,var002)
    #end
event.codeBlock = code
game_multiplayer_admin_panel.add_event(event)
event = RunEvent()
def code():
    if key_clicked(1) or key_clicked(248):
        presentation_set_duration(0)
    #end
event.codeBlock = code
game_multiplayer_admin_panel.add_event(event)


multiplayer_welcome_message = Presentation("multiplayer_welcome_message")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    s0 = str_store_welcome_message()
    if not str_is_empty(0) and _g_multiplayer_welcome_message_shown == 0:
        create_mesh_overlay(reg0,mesh.mp_ui_welcome_panel)
        position_set_x(1,200)
        position_set_y(1,400)
        overlay_set_position(reg0,1)
        create_text_overlay(reg0,0,8192)
        overlay_set_color(reg0,16777215)
        position_set_x(1,230)
        position_set_y(1,425)
        overlay_set_position(reg0,1)
        position_set_x(1,540)
        position_set_y(1,150)
        overlay_set_area_size(reg0,1)
        presentation_set_duration(999999)
    elif _g_multiplayer_show_server_rules == 1:
        create_mesh_overlay(reg0,mesh.mp_ui_welcome_panel)
        position_set_x(1,200)
        position_set_y(1,400)
        overlay_set_position(reg0,1)
        if not str_is_empty(0):
            str_clear(3)
            s2 = str_store_string(0)
            s2 = str_store_string(gstr.s2_s3)
            s2 = str_store_string(gstr.s2_s3)
        else:
            str_clear(2)
        #end
        s3 = str_store_string("@Game Rules:^")
        s2 = str_store_string(gstr.s2_s3)
        var001 = 1000
        game_multiplayer_get_game_type_mission_template(_g_multiplayer_game_type)
        var002 = reg0
        s0 = str_store_server_name()
        s3 = str_store_string(gstr.server_name_s0)
        s2 = str_store_string(gstr.s2_s3)
        if _g_multiplayer_game_type == 0:
            s0 = str_store_string(gstr.multi_game_type_1)
        elif _g_multiplayer_game_type == 1:
            s0 = str_store_string(gstr.multi_game_type_2)
        elif _g_multiplayer_game_type == 2:
            s0 = str_store_string(gstr.multi_game_type_3)
        elif _g_multiplayer_game_type == 3:
            s0 = str_store_string(gstr.multi_game_type_4)
        elif _g_multiplayer_game_type == 4:
            s0 = str_store_string(gstr.multi_game_type_5)
        elif _g_multiplayer_game_type == 5:
            s0 = str_store_string(gstr.multi_game_type_6)
        elif _g_multiplayer_game_type == 6:
            s0 = str_store_string(gstr.multi_game_type_7)
        elif _g_multiplayer_game_type == 7:
            s0 = str_store_string(gstr.multi_game_type_8)
        elif _g_multiplayer_game_type == 8:
            s0 = str_store_string(gstr.multi_game_type_9)
        #end
        s3 = str_store_string(gstr.game_type_s0)
        s2 = str_store_string(gstr.s2_s3)
        if _g_multiplayer_game_type == 8:
            var003 = _g_multiplayer_ccoop_difficulty + gstr.ccoop_easy
            s0 = str_store_string(var003)
            s3 = str_store_string(gstr.ccoop_difficulty_s0)
            s2 = str_store_string(gstr.s2_s3)
        #end
        cur_scene_004 = store_current_scene()
        cur_scene_004 = cur_scene_004 - scn.multi_scene_1
        cur_scene_004 = cur_scene_004 + gstr.multi_scene_1
        s0 = str_store_string(cur_scene_004)
        s3 = str_store_string(gstr.map_name_s0)
        s2 = str_store_string(gstr.s2_s3)
        m_timer_a_005 = store_mission_timer_a()
        m_timer_a_005 += _server_mission_timer_while_player_joined
        reg0 = m_timer_a_005
        _g_multiplayer_game_max_seconds = _g_multiplayer_game_max_minutes * 60
        var006 = _g_multiplayer_game_max_seconds - m_timer_a_005
        reg0 = var006 / 60
        reg1 = store_mod(var006,60)
        if reg0 >= 10 and reg1 >= 10:
            str_clear(0)
            str_clear(1)
        elif reg0 >= 10:
            str_clear(0)
            s1 = str_store_string("@0")
        elif reg1 >= 10:
            s0 = str_store_string("@0")
            str_clear(1)
        else:
            s0 = str_store_string("@0")
            s1 = str_store_string("@0")
        #end
        s3 = str_store_string(gstr.remaining_time_s0reg0_s1reg1)
        s2 = str_store_string(gstr.s2_s3)
        for var007 in range(0, var001):
            reg0 = -12345
            game_get_multiplayer_server_option_for_mission_template(var002,var007)
            if reg0 == -12345:
                var001 = 0
            else:
                game_multiplayer_server_option_for_mission_template_to_string(var002,var007,reg0)
                s3 = str_store_string(0)
                s2 = str_store_string(gstr.s2_s3)
            #end
        #end
        create_text_overlay(reg0,2,8192)
        overlay_set_color(reg0,16777215)
        position_set_x(1,230)
        position_set_y(1,425)
        overlay_set_position(reg0,1)
        position_set_x(1,540)
        position_set_y(1,150)
        overlay_set_area_size(reg0,1)
        presentation_set_duration(999999)
    #end
event.codeBlock = code
multiplayer_welcome_message.add_event(event)
event = RunEvent()
def code():
    s0 = str_store_welcome_message()
    if _g_multiplayer_show_server_rules != 1 and str_is_empty(0) or _g_multiplayer_welcome_message_shown == 1:
        presentation_set_duration(0)
        if not is_presentation_active(prsnt.multiplayer_escape_menu) and not is_presentation_active(prsnt.multiplayer_team_select):
            start_presentation(prsnt.multiplayer_team_select)
        else:
            m_timer_a_001 = store_mission_timer_a()
            if m_timer_a_001 > 1 and key_clicked(1) or key_clicked(57) or key_clicked(28) or key_clicked(224) or key_clicked(225) or key_clicked(252) or key_clicked(253):
                _g_multiplayer_welcome_message_shown = 1
                presentation_set_duration(0)
                if not is_presentation_active(prsnt.multiplayer_escape_menu) and not is_presentation_active(prsnt.multiplayer_team_select):
                    if _g_multiplayer_show_server_rules == 1:
                        _g_multiplayer_show_server_rules = 0
                        start_presentation(prsnt.multiplayer_escape_menu)
                    else:
                        start_presentation(prsnt.multiplayer_team_select)
                    #end
                #end
            #end
        #end
    #end
event.codeBlock = code
multiplayer_welcome_message.add_event(event)


multiplayer_team_select = Presentation("multiplayer_team_select")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg0,mesh.mp_ingame_menu)
    position_set_x(1,250)
    position_set_y(1,80)
    overlay_set_position(reg0,1)
    position_set_x(1,1000)
    position_set_y(1,1000)
    overlay_set_size(reg0,1)
    str_clear(0)
    create_text_overlay(_g_presentation_obj_team_select_container,0,131072)
    position_set_x(1,285)
    position_set_y(1,125)
    overlay_set_position(_g_presentation_obj_team_select_container,1)
    position_set_x(1,405)
    position_set_y(1,500)
    overlay_set_area_size(_g_presentation_obj_team_select_container,1)
    set_container_overlay(_g_presentation_obj_team_select_container)
    var001 = 450
    create_text_overlay(reg0,gstr.choose_a_faction,0)
    overlay_set_color(reg0,16777215)
    position_set_x(1,0)
    position_set_y(1,var001)
    overlay_set_position(reg0,1)
    var001 -= 40
    position_set_y(1,var001)
    position_set_x(1,100)
    my_player = multiplayer_get_my_player()
    team_faction_003 = team_get_faction(0)
    s0 = str_store_faction_name(team_faction_003)
    create_button_overlay(_g_presentation_obj_team_select_1,0,0)
    if cf_multiplayer_team_is_available(my_player,0):
        overlay_set_color(_g_presentation_obj_team_select_1,16777215)
        overlay_set_hilight_color(_g_presentation_obj_team_select_1,5635920)
        _g_multiplayer_team_select_1_available = 1
    else:
        overlay_set_color(_g_presentation_obj_team_select_1,8947848)
        overlay_set_hilight_color(_g_presentation_obj_team_select_1,8947848)
        _g_multiplayer_team_select_1_available = 0
    #end
    position_set_y(1,var001)
    overlay_set_position(_g_presentation_obj_team_select_1,1)
    var001 -= 40
    position_set_y(1,var001)
    if True:
        team_faction_003 = team_get_faction(1)
        s0 = str_store_faction_name(team_faction_003)
        if _g_multiplayer_game_type != 8:
            create_button_overlay(_g_presentation_obj_team_select_2,0,0)
        else:
            _g_presentation_obj_team_select_2 = -1
        #end
        if cf_multiplayer_team_is_available(my_player,1):
            if _g_multiplayer_game_type != 8:
                overlay_set_color(_g_presentation_obj_team_select_2,16777215)
                overlay_set_hilight_color(_g_presentation_obj_team_select_2,5635920)
            #end
            _g_multiplayer_team_select_2_available = 1
        else:
            if _g_multiplayer_game_type != 8:
                overlay_set_color(_g_presentation_obj_team_select_2,8947848)
                overlay_set_hilight_color(_g_presentation_obj_team_select_2,8947848)
            #end
            _g_multiplayer_team_select_2_available = 0
        #end
        if _g_multiplayer_game_type != 8:
            overlay_set_position(_g_presentation_obj_team_select_2,1)
            var001 -= 40
            position_set_y(1,var001)
        #end
    #end
    create_button_overlay(_g_presentation_obj_team_select_3,gstr.spectator,0)
    overlay_set_color(_g_presentation_obj_team_select_3,16777215)
    overlay_set_position(_g_presentation_obj_team_select_3,1)
    var001 -= 40
    position_set_y(1,var001)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_team_select.add_event(event)
event = StateChangedEvent()
def code(var001):
    _g_multiplayer_game_type_list1 = [
    7,
    0,
    8,
    ]
    _g_multiplayer_game_type_list1 = [
    7,
    0,
    8,
    ]
    my_player = multiplayer_get_my_player()
    if _g_waiting_for_confirmation_to_terminate == 0:
        if var001 == _g_presentation_obj_team_select_1:
            if cf_multiplayer_team_is_available(my_player,0):
                if True:
                    team_no_003 = player_get_team_no(my_player)
                    if team_no_003 != 0:
                        _g_confirmation_result = 0
                        if _g_multiplayer_game_type != 8 and _g_multiplayer_game_type != 0 and _g_multiplayer_game_type != 7:
                            _g_waiting_for_confirmation_to_terminate = 1
                        #end
                    #end
                    _g_confirmation_troop_backup = player_get_troop_id(my_player)
                    _g_confirmation_team_backup = player_get_team_no(my_player)
                    player_set_troop_id(my_player,-1)
                    multiplayer_send_int_to_server(19,0)
                    player_set_team_no(my_player,0)
                    mp_set_player_team_no(my_player,0,1)
                    if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
                        presentation_set_duration(0)
                        start_presentation(prsnt.multiplayer_troop_select)
                    #end
                else:
                    presentation_set_duration(0)
                    start_presentation(prsnt.multiplayer_troop_select)
                #end
            #end
        elif var001 == _g_presentation_obj_team_select_2:
            if cf_multiplayer_team_is_available(my_player,1):
                if True:
                    team_no_003 = player_get_team_no(my_player)
                    if team_no_003 != 1:
                        _g_confirmation_result = 0
                        if _g_multiplayer_game_type != 8 and _g_multiplayer_game_type != 0 and _g_multiplayer_game_type != 7:
                            _g_waiting_for_confirmation_to_terminate = 1
                        #end
                    #end
                    _g_confirmation_troop_backup = player_get_troop_id(my_player)
                    _g_confirmation_team_backup = player_get_team_no(my_player)
                    player_set_troop_id(my_player,-1)
                    multiplayer_send_int_to_server(19,1)
                    player_set_team_no(my_player,1)
                    mp_set_player_team_no(my_player,1,1)
                    if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
                        presentation_set_duration(0)
                        start_presentation(prsnt.multiplayer_troop_select)
                    #end
                else:
                    presentation_set_duration(0)
                    start_presentation(prsnt.multiplayer_troop_select)
                #end
            #end
        elif var001 == _g_presentation_obj_team_select_3:
            player_set_troop_id(my_player,-1)
            multiplayer_send_int_to_server(19,2)
            player_set_team_no(my_player,2)
            presentation_set_duration(0)
        #end
    #end
event.codeBlock = code
multiplayer_team_select.add_event(event)
event = RunEvent()
def code():
    my_player = multiplayer_get_my_player()
    if key_clicked(1) or key_clicked(248) and _g_waiting_for_confirmation_to_terminate == 0:
        my_team_no = multiplayer_get_my_team()
        if my_team_no == 3:
            player_set_troop_id(my_player,-1)
            multiplayer_send_int_to_server(19,2)
            player_set_team_no(my_player,2)
        #end
        presentation_set_duration(0)
    elif _g_waiting_for_confirmation_to_terminate == 1 and _g_confirmation_result == 1:
        _g_waiting_for_confirmation_to_terminate = 0
        _g_confirmation_result = 0
        presentation_set_duration(0)
        start_presentation(prsnt.multiplayer_troop_select)
    elif _g_waiting_for_confirmation_to_terminate == 1 and _g_confirmation_result == -1:
        player_set_troop_id(my_player,_g_confirmation_troop_backup)
        player_set_team_no(my_player,_g_confirmation_team_backup)
        _g_waiting_for_confirmation_to_terminate = 0
        _g_confirmation_result = 0
        presentation_set_duration(0)
        start_presentation(prsnt.multiplayer_team_select)
    else:
        var003 = 0
        if cf_multiplayer_team_is_available(my_player,0):
            if _g_multiplayer_team_select_1_available == 0:
                var003 = 1
            #end
        else:
            if _g_multiplayer_team_select_1_available == 1:
                var003 = 1
            #end
        #end
        if cf_multiplayer_team_is_available(my_player,1):
            if _g_multiplayer_team_select_2_available == 0:
                var003 = 1
            #end
        else:
            if _g_multiplayer_team_select_2_available == 1:
                var003 = 1
            #end
        #end
        if var003 == 1:
            presentation_set_duration(0)
            start_presentation(prsnt.multiplayer_team_select)
        #end
    #end
event.codeBlock = code
multiplayer_team_select.add_event(event)


multiplayer_troop_select = Presentation("multiplayer_troop_select")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg0,mesh.mp_ingame_menu)
    position_set_x(1,250)
    position_set_y(1,80)
    overlay_set_position(reg0,1)
    position_set_x(1,1000)
    position_set_y(1,1000)
    overlay_set_size(reg0,1)
    str_clear(0)
    create_text_overlay(_g_presentation_obj_troop_select_container,0,131072)
    position_set_x(1,285)
    position_set_y(1,125)
    overlay_set_position(_g_presentation_obj_troop_select_container,1)
    position_set_x(1,405)
    position_set_y(1,500)
    overlay_set_area_size(_g_presentation_obj_troop_select_container,1)
    set_container_overlay(_g_presentation_obj_troop_select_container)
    var001 = 450
    create_text_overlay(reg0,gstr.choose_a_troop,0)
    overlay_set_color(reg0,16777215)
    position_set_x(1,0)
    position_set_y(1,var001)
    overlay_set_position(reg0,1)
    var001 -= 40
    position_set_y(1,var001)
    position_set_x(1,100)
    my_player = multiplayer_get_my_player()
    team_no_003 = player_get_team_no(my_player)
    team_faction_004 = team_get_faction(team_no_003)
    for slot_no_005 in range(30, 46):
        troop_set_slot(trp.multiplayer_data,slot_no_005,-1)
    #end
    var006 = 0
    for trp_007 in range(trp.swadian_crossbowman_multiplayer, trp.multiplayer_end):
        troop_faction_008 = store_faction_of_troop(trp_007)
        if troop_faction_008 == team_faction_004:
            s1 = str_store_troop_name(trp_007)
            create_button_overlay(reg0,1,0)
            overlay_set_color(reg0,16777215)
            slot_no_009 = var006 + 30
            troop_set_slot(trp.multiplayer_data,slot_no_009,reg0)
            position_set_y(1,var001)
            overlay_set_position(reg0,1)
            var001 -= 40
            position_set_y(1,var001)
            var006 += 1
        #end
    #end
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_troop_select.add_event(event)
event = StateChangedEvent()
def code(var001):
    my_player = multiplayer_get_my_player()
    team_no_003 = player_get_team_no(my_player)
    team_faction_004 = team_get_faction(team_no_003)
    troop_id_005 = -1
    var006 = 46
    for var007 in range(30, var006):
        if troop_slot_eq(trp.multiplayer_data,var007,var001):
            var008 = var007 - 30
            var009 = trp.multiplayer_end
            for troop_id_010 in range(trp.swadian_crossbowman_multiplayer, var009):
                troop_faction_011 = store_faction_of_troop(troop_id_010)
                if troop_faction_011 == team_faction_004:
                    var008 -= 1
                    if var008 < 0:
                        troop_id_005 = troop_id_010
                        var009 = 0
                    #end
                #end
            #end
        #end
        if True:
            troop_id_010 = multiplayer_get_my_troop()
            if troop_id_010 != troop_id_005:
                player_set_troop_id(my_player,troop_id_005)
                multiplayer_send_int_to_server(20,troop_id_005)
                multiplayer_set_default_item_selections_for_troop(troop_id_005)
                multiplayer_send_item_selections()
            #end
        #end
        presentation_set_duration(0)
        _g_presentation_state = 0
        if cf_multiplayer_can_buy_squad():
            _g_presentation_state = 10
        #end
        start_presentation(prsnt.multiplayer_item_select)
        var006 = 0
    #end
event.codeBlock = code
multiplayer_troop_select.add_event(event)
event = RunEvent()
def code():
    if key_clicked(1) or key_clicked(248):
        my_player = multiplayer_get_my_player()
        if is_between(my_player,0,1000):
            my_troop_id = multiplayer_get_my_troop()
            if _g_multiplayer_is_game_type_captain == 1 and not is_between(my_troop_id,trp.swadian_crossbowman_multiplayer,trp.multiplayer_end):
                mp_set_player_team_no(my_player,2,1)
            elif not is_between(my_troop_id,trp.swadian_crossbowman_multiplayer,trp.multiplayer_end):
                player_set_troop_id(my_player,-1)
                multiplayer_send_int_to_server(20,-1)
                multiplayer_send_int_to_server(19,2)
                player_set_team_no(my_player,2)
            #end
        #end
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_troop_select.add_event(event)


multiplayer_item_select = Presentation("multiplayer_item_select")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    my_player = multiplayer_get_my_player()
    _g_presentation_obj_item_select_1 = -1
    _g_presentation_obj_item_select_2 = -1
    _g_presentation_obj_item_select_3 = -1
    _g_presentation_obj_item_select_4 = -1
    _g_presentation_obj_item_select_5 = -1
    _g_presentation_obj_item_select_6 = -1
    _g_presentation_obj_item_select_7 = -1
    _g_presentation_obj_item_select_8 = -1
    _g_presentation_obj_item_select_9 = -1
    _g_presentation_obj_item_select_10 = -1
    _g_presentation_obj_item_select_11 = -1
    _g_presentation_obj_item_select_12 = -1
    _g_presentation_obj_item_select_13 = -1
    _g_presentation_obj_item_select_14 = -1
    _g_presentation_obj_item_select_15 = -1
    _g_presentation_obj_item_select_16 = -1
    _g_presentation_obj_item_select_17 = -1
    if _g_current_opened_item_details != -1:
        close_item_details()
        _g_current_opened_item_details = -1
    #end
    slot_no_002 = 2 + 0
    player_slot_003 = player_get_slot(my_player,slot_no_002)
    if player_slot_003 >= 0:
        create_image_button_overlay(_g_presentation_obj_item_select_1,mesh.mp_inventory_slot_empty,mesh.mp_inventory_slot_empty)
        create_mesh_overlay_with_item_id(reg0,player_slot_003)
        position_set_x(1,950)
        position_set_y(1,526)
        overlay_set_position(reg0,1)
        _g_inside_obj_1 = reg0
    else:
        create_image_button_overlay(_g_presentation_obj_item_select_1,mesh.mp_inventory_slot_equip,mesh.mp_inventory_slot_equip)
    #end
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_item_select_1,1)
    position_set_x(1,899)
    position_set_y(1,475)
    overlay_set_position(_g_presentation_obj_item_select_1,1)
    slot_no_002 = 2 + 1
    player_slot_003 = player_get_slot(my_player,slot_no_002)
    if player_slot_003 >= 0:
        create_image_button_overlay(_g_presentation_obj_item_select_2,mesh.mp_inventory_slot_empty,mesh.mp_inventory_slot_empty)
        create_mesh_overlay_with_item_id(reg0,player_slot_003)
        position_set_x(1,950)
        position_set_y(1,426)
        overlay_set_position(reg0,1)
        _g_inside_obj_2 = reg0
    else:
        create_image_button_overlay(_g_presentation_obj_item_select_2,mesh.mp_inventory_slot_equip,mesh.mp_inventory_slot_equip)
    #end
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_item_select_2,1)
    position_set_x(1,899)
    position_set_y(1,375)
    overlay_set_position(_g_presentation_obj_item_select_2,1)
    slot_no_002 = 2 + 2
    player_slot_003 = player_get_slot(my_player,slot_no_002)
    if player_slot_003 >= 0:
        create_image_button_overlay(_g_presentation_obj_item_select_3,mesh.mp_inventory_slot_empty,mesh.mp_inventory_slot_empty)
        create_mesh_overlay_with_item_id(reg0,player_slot_003)
        position_set_x(1,950)
        position_set_y(1,326)
        overlay_set_position(reg0,1)
        _g_inside_obj_3 = reg0
    else:
        create_image_button_overlay(_g_presentation_obj_item_select_3,mesh.mp_inventory_slot_equip,mesh.mp_inventory_slot_equip)
    #end
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_item_select_3,1)
    position_set_x(1,899)
    position_set_y(1,275)
    overlay_set_position(_g_presentation_obj_item_select_3,1)
    slot_no_002 = 2 + 3
    player_slot_003 = player_get_slot(my_player,slot_no_002)
    if player_slot_003 >= 0:
        create_image_button_overlay(_g_presentation_obj_item_select_4,mesh.mp_inventory_slot_empty,mesh.mp_inventory_slot_empty)
        create_mesh_overlay_with_item_id(reg0,player_slot_003)
        position_set_x(1,950)
        position_set_y(1,226)
        overlay_set_position(reg0,1)
        _g_inside_obj_4 = reg0
    else:
        create_image_button_overlay(_g_presentation_obj_item_select_4,mesh.mp_inventory_slot_equip,mesh.mp_inventory_slot_equip)
    #end
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_item_select_4,1)
    position_set_x(1,899)
    position_set_y(1,175)
    overlay_set_position(_g_presentation_obj_item_select_4,1)
    slot_no_002 = 2 + 4
    player_slot_003 = player_get_slot(my_player,slot_no_002)
    if player_slot_003 >= 0:
        create_image_button_overlay(_g_presentation_obj_item_select_5,mesh.mp_inventory_slot_empty,mesh.mp_inventory_slot_empty)
        create_mesh_overlay_with_item_id(reg0,player_slot_003)
        position_set_x(1,53)
        position_set_y(1,576)
        overlay_set_position(reg0,1)
        _g_inside_obj_5 = reg0
    else:
        create_image_button_overlay(_g_presentation_obj_item_select_5,mesh.mp_inventory_slot_helmet,mesh.mp_inventory_slot_helmet)
    #end
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_item_select_5,1)
    position_set_x(1,2)
    position_set_y(1,525)
    overlay_set_position(_g_presentation_obj_item_select_5,1)
    slot_no_002 = 2 + 5
    player_slot_003 = player_get_slot(my_player,slot_no_002)
    if player_slot_003 >= 0:
        create_image_button_overlay(_g_presentation_obj_item_select_6,mesh.mp_inventory_slot_empty,mesh.mp_inventory_slot_empty)
        create_mesh_overlay_with_item_id(reg0,player_slot_003)
        position_set_x(1,53)
        position_set_y(1,476)
        overlay_set_position(reg0,1)
        _g_inside_obj_6 = reg0
    else:
        create_image_button_overlay(_g_presentation_obj_item_select_6,mesh.mp_inventory_slot_armor,mesh.mp_inventory_slot_armor)
    #end
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_item_select_6,1)
    position_set_x(1,2)
    position_set_y(1,425)
    overlay_set_position(_g_presentation_obj_item_select_6,1)
    slot_no_002 = 2 + 6
    player_slot_003 = player_get_slot(my_player,slot_no_002)
    if player_slot_003 >= 0:
        create_image_button_overlay(_g_presentation_obj_item_select_7,mesh.mp_inventory_slot_empty,mesh.mp_inventory_slot_empty)
        create_mesh_overlay_with_item_id(reg0,player_slot_003)
        position_set_x(1,53)
        position_set_y(1,376)
        overlay_set_position(reg0,1)
        _g_inside_obj_7 = reg0
    else:
        create_image_button_overlay(_g_presentation_obj_item_select_7,mesh.mp_inventory_slot_boot,mesh.mp_inventory_slot_boot)
    #end
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_item_select_7,1)
    position_set_x(1,2)
    position_set_y(1,325)
    overlay_set_position(_g_presentation_obj_item_select_7,1)
    slot_no_002 = 2 + 7
    player_slot_003 = player_get_slot(my_player,slot_no_002)
    if player_slot_003 >= 0:
        create_image_button_overlay(_g_presentation_obj_item_select_8,mesh.mp_inventory_slot_empty,mesh.mp_inventory_slot_empty)
        create_mesh_overlay_with_item_id(reg0,player_slot_003)
        position_set_x(1,53)
        position_set_y(1,276)
        overlay_set_position(reg0,1)
        _g_inside_obj_8 = reg0
    else:
        create_image_button_overlay(_g_presentation_obj_item_select_8,mesh.mp_inventory_slot_glove,mesh.mp_inventory_slot_glove)
    #end
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_item_select_8,1)
    position_set_x(1,2)
    position_set_y(1,225)
    overlay_set_position(_g_presentation_obj_item_select_8,1)
    slot_no_002 = 2 + 8
    player_slot_003 = player_get_slot(my_player,slot_no_002)
    if player_slot_003 >= 0 and _g_horses_are_avaliable == 1:
        create_image_button_overlay(_g_presentation_obj_item_select_9,mesh.mp_inventory_slot_empty,mesh.mp_inventory_slot_empty)
        create_mesh_overlay_with_item_id(reg0,player_slot_003)
        position_set_x(1,53)
        position_set_y(1,176)
        overlay_set_position(reg0,1)
        _g_inside_obj_9 = reg0
    else:
        create_image_button_overlay(_g_presentation_obj_item_select_9,mesh.mp_inventory_slot_horse,mesh.mp_inventory_slot_horse)
    #end
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(_g_presentation_obj_item_select_9,1)
    position_set_x(1,2)
    position_set_y(1,125)
    overlay_set_position(_g_presentation_obj_item_select_9,1)
    create_mesh_overlay(reg0,mesh.mp_inventory_left)
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(reg0,1)
    position_set_x(1,0)
    position_set_y(1,14)
    overlay_set_position(reg0,1)
    create_mesh_overlay(reg0,mesh.mp_inventory_right)
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(reg0,1)
    position_set_x(1,894)
    position_set_y(1,65)
    overlay_set_position(reg0,1)
    create_in_game_button_overlay(_g_presentation_obj_item_select_10,gstr.reset_to_default,0)
    overlay_set_color(_g_presentation_obj_item_select_10,16777215)
    position_set_x(1,605)
    position_set_y(1,25)
    overlay_set_position(_g_presentation_obj_item_select_10,1)
    create_in_game_button_overlay(_g_presentation_obj_item_select_11,gstr.done,0)
    overlay_set_color(_g_presentation_obj_item_select_11,16777215)
    position_set_x(1,395)
    position_set_y(1,25)
    overlay_set_position(_g_presentation_obj_item_select_11,1)
    var004 = 725
    my_player = multiplayer_get_my_player()
    team_no_005 = player_get_team_no(my_player)
    var006 = 0
    if cf_multiplayer_can_buy_squad():
        var006 = 1
    elif _g_multiplayer_is_game_type_captain != 1 and team_no_005 == 0 and _g_multiplayer_num_bots_team_1 > 0:
        var006 = 1
    elif _g_multiplayer_is_game_type_captain != 1 and team_no_005 == 1 and _g_multiplayer_num_bots_team_2 > 0:
        var006 = 1
    #end
    team_faction_007 = team_get_faction(team_no_005)
    if var006 == 1 and _g_multiplayer_game_type != 0 and _g_multiplayer_game_type != 7:
        var008 = 0
        if var006 == 1:
            for trp_009 in range(trp.swadian_crossbowman_multiplayer_ai, trp.swadian_crossbowman_multiplayer):
                troop_faction_010 = store_faction_of_troop(trp_009)
                if troop_faction_010 == team_faction_007:
                    var008 += 1
                #end
            #end
        #end
        if _g_multiplayer_is_game_type_captain == 1:
            var008 = 3
        #end
        var011 = var008 * 20
        var011 += 40
        if _g_multiplayer_is_game_type_captain == 1:
            create_in_game_button_overlay(_g_presentation_obj_item_select_17,gstr.mp_add_troop)
            overlay_set_color(_g_presentation_obj_item_select_17,16777215)
            position_set_x(1,500)
            position_set_y(1,650)
            overlay_set_position(_g_presentation_obj_item_select_17,1)
        else:
            create_mesh_overlay(reg0,mesh.mp_ui_command_border_r)
            position_set_x(1,280)
            position_set_y(1,680)
            overlay_set_position(reg0,1)
            position_set_x(1,2500)
            position_set_y(1,2500)
            overlay_set_size(reg0,1)
            create_mesh_overlay(reg0,mesh.mp_ui_command_border_l)
            position_set_x(1,650)
            position_set_y(1,680)
            overlay_set_position(reg0,1)
            position_set_x(1,2500)
            position_set_y(1,2500)
            overlay_set_size(reg0,1)
            create_mesh_overlay(reg0,mesh.mp_ui_command_panel)
            position_set_x(1,350)
            var012 = 750 - var011
            position_set_y(1,var012)
            overlay_set_position(reg0,1)
            position_set_x(1,3000)
            position_set_y(1,3000)
            overlay_set_size(reg0,1)
            create_text_overlay(reg0,gstr.command,0)
            overlay_set_color(reg0,16777215)
            position_set_x(1,800)
            position_set_y(1,800)
            overlay_set_size(reg0,1)
            position_set_x(1,370)
            position_set_y(1,var004)
            overlay_set_position(reg0,1)
            var004 -= 20
        #end
        var013 = 0
        if _g_multiplayer_is_game_type_captain == 0:
            for trp_009 in range(trp.swadian_crossbowman_multiplayer_ai, trp.swadian_crossbowman_multiplayer):
                troop_faction_010 = store_faction_of_troop(trp_009)
                if troop_faction_010 == team_faction_007:
                    create_check_box_overlay(reg0,mesh.checkbox_off,mesh.checkbox_on)
                    position_set_x(1,800)
                    position_set_y(1,800)
                    overlay_set_size(reg0,1)
                    position_set_x(1,377)
                    var014 = var004 + 2
                    position_set_y(1,var014)
                    overlay_set_position(reg0,1)
                    if var013 == 0:
                        overlay_set_val(reg0,_g_multiplayer_bot_type_1_wanted)
                        _g_presentation_obj_item_select_13 = reg0
                    elif var013 == 1:
                        overlay_set_val(reg0,_g_multiplayer_bot_type_2_wanted)
                        _g_presentation_obj_item_select_14 = reg0
                    elif var013 == 2:
                        overlay_set_val(reg0,_g_multiplayer_bot_type_3_wanted)
                        _g_presentation_obj_item_select_15 = reg0
                    else:
                        overlay_set_val(reg0,_g_multiplayer_bot_type_4_wanted)
                        _g_presentation_obj_item_select_16 = reg0
                    #end
                #end
                s0 = str_store_troop_name(trp_009)
                create_text_overlay(reg0,gstr.s0,0)
                overlay_set_color(reg0,16777215)
                position_set_x(1,800)
                position_set_y(1,800)
                overlay_set_size(reg0,1)
                position_set_x(1,397)
                position_set_y(1,var004)
                overlay_set_position(reg0,1)
                var004 -= 20
                var013 += 1
            #end
        #end
        var004 -= 20
    #end
    my_player = multiplayer_get_my_player()
    gold_015 = player_get_gold(my_player)
    multiplayer_calculate_cur_selected_items_cost(my_player,1)
    create_text_overlay(_g_presentation_obj_item_select_12,gstr.total_item_cost_reg0,98308)
    if gold_015 >= reg0:
        overlay_set_color(_g_presentation_obj_item_select_12,16777215)
    else:
        overlay_set_color(_g_presentation_obj_item_select_12,16711680)
    #end
    position_set_x(1,680)
    position_set_y(1,652)
    overlay_set_position(_g_presentation_obj_item_select_12,1)
    _g_presentation_obj_item_select_next = _g_presentation_obj_item_select_12 + 1
    troop_id_016 = player_get_troop_id(my_player)
    if _g_presentation_state == 1:
        multiplayer_display_available_items_for_troop_and_item_classes(troop_id_016,1,18,781,474)
        create_mesh_overlay(reg0,mesh.mp_inventory_right_arrow)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(reg0,1)
        position_set_x(1,881)
        position_set_y(1,515)
        overlay_set_position(reg0,1)
    elif _g_presentation_state == 2:
        multiplayer_display_available_items_for_troop_and_item_classes(troop_id_016,1,18,781,374)
        create_mesh_overlay(reg0,mesh.mp_inventory_right_arrow)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(reg0,1)
        position_set_x(1,881)
        position_set_y(1,415)
        overlay_set_position(reg0,1)
    elif _g_presentation_state == 3:
        multiplayer_display_available_items_for_troop_and_item_classes(troop_id_016,1,18,781,274)
        create_mesh_overlay(reg0,mesh.mp_inventory_right_arrow)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(reg0,1)
        position_set_x(1,881)
        position_set_y(1,315)
        overlay_set_position(reg0,1)
    elif _g_presentation_state == 4:
        multiplayer_display_available_items_for_troop_and_item_classes(troop_id_016,1,18,781,174)
        create_mesh_overlay(reg0,mesh.mp_inventory_right_arrow)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(reg0,1)
        position_set_x(1,881)
        position_set_y(1,215)
        overlay_set_position(reg0,1)
    elif _g_presentation_state == 5:
        multiplayer_display_available_items_for_troop_and_item_classes(troop_id_016,22,24,117,524)
        create_mesh_overlay(reg0,mesh.mp_inventory_left_arrow)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(reg0,1)
        position_set_x(1,106)
        position_set_y(1,565)
        overlay_set_position(reg0,1)
    elif _g_presentation_state == 6:
        multiplayer_display_available_items_for_troop_and_item_classes(troop_id_016,19,22,117,424)
        create_mesh_overlay(reg0,mesh.mp_inventory_left_arrow)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(reg0,1)
        position_set_x(1,106)
        position_set_y(1,465)
        overlay_set_position(reg0,1)
    elif _g_presentation_state == 7:
        multiplayer_display_available_items_for_troop_and_item_classes(troop_id_016,24,26,117,324)
        create_mesh_overlay(reg0,mesh.mp_inventory_left_arrow)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(reg0,1)
        position_set_x(1,106)
        position_set_y(1,365)
        overlay_set_position(reg0,1)
    elif _g_presentation_state == 8:
        multiplayer_display_available_items_for_troop_and_item_classes(troop_id_016,26,27,117,224)
        create_mesh_overlay(reg0,mesh.mp_inventory_left_arrow)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(reg0,1)
        position_set_x(1,106)
        position_set_y(1,265)
        overlay_set_position(reg0,1)
    elif _g_presentation_state == 9 and _g_horses_are_avaliable == 1:
        multiplayer_display_available_items_for_troop_and_item_classes(troop_id_016,18,19,117,124)
        create_mesh_overlay(reg0,mesh.mp_inventory_left_arrow)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(reg0,1)
        position_set_x(1,106)
        position_set_y(1,165)
        overlay_set_position(reg0,1)
    elif _g_presentation_state == 10:
        mp_set_coop_companions(my_player)
        create_mesh_overlay(reg0,mesh.mp_score_b)
        position_set_x(1,205)
        position_set_y(1,150)
        overlay_set_position(reg0,1)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(reg0,1)
        my_player = multiplayer_get_my_player()
        player_slot_017 = player_get_slot(my_player,42)
        _g_presentation_obj_coop_companion_select_0 = -1
        _g_presentation_obj_coop_companion_select_1 = -1
        if player_slot_017 == 0:
            create_combo_label_overlay(_g_presentation_obj_coop_companion_select_0)
            position_set_x(1,700)
            position_set_y(1,700)
            overlay_set_size(_g_presentation_obj_coop_companion_select_0,1)
            position_set_x(1,360)
            position_set_y(1,265)
            overlay_set_position(_g_presentation_obj_coop_companion_select_0,1)
            create_combo_label_overlay(_g_presentation_obj_coop_companion_select_1)
            position_set_x(1,700)
            position_set_y(1,700)
            overlay_set_size(_g_presentation_obj_coop_companion_select_1,1)
            position_set_x(1,640)
            position_set_y(1,265)
            overlay_set_position(_g_presentation_obj_coop_companion_select_1,1)
            for trp_018 in range(trp.npc1_1, trp.npc1_2):
                s0 = str_store_troop_name(trp_018)
                overlay_add_item(_g_presentation_obj_coop_companion_select_0,0)
                overlay_add_item(_g_presentation_obj_coop_companion_select_1,0)
            #end
            var019 = _g_presentation_obj_coop_companion_0 - trp.npc1_1
            overlay_set_val(_g_presentation_obj_coop_companion_select_0,var019)
            var019 = _g_presentation_obj_coop_companion_1 - trp.npc1_1
            overlay_set_val(_g_presentation_obj_coop_companion_select_1,var019)
            create_text_overlay(reg0,gstr.ccoop_select_companion,0)
            overlay_set_color(reg0,16777215)
            position_set_x(1,222)
            position_set_y(1,550)
            overlay_set_position(reg0,1)
        else:
            s0 = str_store_troop_name(_g_presentation_obj_coop_companion_0)
            create_text_overlay(reg0,0,16)
            position_set_x(1,1000)
            position_set_y(1,1000)
            overlay_set_size(reg0,1)
            overlay_set_color(reg0,16777215)
            position_set_x(1,358)
            position_set_y(1,265)
            overlay_set_position(reg0,1)
            s0 = str_store_troop_name(_g_presentation_obj_coop_companion_1)
            create_text_overlay(reg0,0,16)
            position_set_x(1,1000)
            position_set_y(1,1000)
            overlay_set_size(reg0,1)
            overlay_set_color(reg0,16777215)
            position_set_x(1,638)
            position_set_y(1,265)
            overlay_set_position(reg0,1)
            create_text_overlay(reg0,gstr.ccoop_select_companion_class,0)
            overlay_set_color(reg0,16777215)
            position_set_x(1,222)
            position_set_y(1,550)
            overlay_set_position(reg0,1)
        #end
        player_slot_020 = player_get_slot(my_player,47)
        player_slot_020 += 1
        reg0 = player_slot_020
        s0 = str_store_string(gstr.ccoop_lvl_reg0)
        create_text_overlay(reg0,0,4)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(reg0,1)
        overlay_set_color(reg0,16777215)
        position_set_x(1,418)
        position_set_y(1,507)
        overlay_set_position(reg0,1)
        player_slot_021 = player_get_slot(my_player,48)
        player_slot_021 += 1
        reg0 = player_slot_021
        s0 = str_store_string("@Lv. {reg0}")
        create_text_overlay(reg0,0,4)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(reg0,1)
        overlay_set_color(reg0,16777215)
        position_set_x(1,698)
        position_set_y(1,507)
        overlay_set_position(reg0,1)
        var022 = _g_presentation_obj_coop_companion_0 - trp.npc1_1
        var022 = var022 + gstr.npc1_1
        s0 = str_store_string(var022)
        create_text_overlay(reg0,0,4)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(reg0,1)
        overlay_set_color(reg0,16777215)
        position_set_x(1,250)
        position_set_y(1,306)
        overlay_set_position(reg0,1)
        var022 = _g_presentation_obj_coop_companion_1 - trp.npc1_1
        var022 = var022 + gstr.npc1_1
        s0 = str_store_string(var022)
        create_text_overlay(reg0,0,4)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(reg0,1)
        overlay_set_color(reg0,16777215)
        position_set_x(1,530)
        position_set_y(1,306)
        overlay_set_position(reg0,1)
        create_image_button_overlay(_g_presentation_obj_coop_companion_random_select_0,mesh.ccoop_random_class,mesh.ccoop_random_class)
        position_set_x(1,60)
        position_set_y(1,80)
        overlay_set_size(_g_presentation_obj_coop_companion_random_select_0,1)
        position_set_x(1,259)
        position_set_y(1,341)
        overlay_set_position(_g_presentation_obj_coop_companion_random_select_0,1)
        create_image_button_overlay(_g_presentation_obj_coop_companion_random_select_1,mesh.ccoop_random_class,mesh.ccoop_random_class)
        position_set_x(1,60)
        position_set_y(1,80)
        overlay_set_size(_g_presentation_obj_coop_companion_random_select_1,1)
        position_set_x(1,539)
        position_set_y(1,341)
        overlay_set_position(_g_presentation_obj_coop_companion_random_select_1,1)
        create_image_button_overlay(_g_presentation_obj_coop_companion_class_select_0_default,mesh.ccoop_default_class,mesh.ccoop_default_class)
        create_image_button_overlay(_g_presentation_obj_coop_companion_class_select_1_default,mesh.ccoop_default_class,mesh.ccoop_default_class)
        create_image_button_overlay(_g_presentation_obj_coop_companion_class_select_0_infantry,mesh.ccoop_melee_class,mesh.ccoop_melee_class)
        create_image_button_overlay(_g_presentation_obj_coop_companion_class_select_1_infantry,mesh.ccoop_melee_class,mesh.ccoop_melee_class)
        create_image_button_overlay(_g_presentation_obj_coop_companion_class_select_0_ranged,mesh.ccoop_ranged_class,mesh.ccoop_ranged_class)
        create_image_button_overlay(_g_presentation_obj_coop_companion_class_select_1_ranged,mesh.ccoop_ranged_class,mesh.ccoop_ranged_class)
        create_image_button_overlay(_g_presentation_obj_coop_companion_class_select_0_mounted,mesh.ccoop_mounted_class,mesh.ccoop_mounted_class)
        create_image_button_overlay(_g_presentation_obj_coop_companion_class_select_1_mounted,mesh.ccoop_mounted_class,mesh.ccoop_mounted_class)
        position_set_x(1,90)
        position_set_y(1,120)
        overlay_set_size(_g_presentation_obj_coop_companion_class_select_0_default,1)
        overlay_set_size(_g_presentation_obj_coop_companion_class_select_1_default,1)
        overlay_set_size(_g_presentation_obj_coop_companion_class_select_0_infantry,1)
        overlay_set_size(_g_presentation_obj_coop_companion_class_select_1_infantry,1)
        overlay_set_size(_g_presentation_obj_coop_companion_class_select_0_ranged,1)
        overlay_set_size(_g_presentation_obj_coop_companion_class_select_1_ranged,1)
        overlay_set_size(_g_presentation_obj_coop_companion_class_select_0_mounted,1)
        overlay_set_size(_g_presentation_obj_coop_companion_class_select_1_mounted,1)
        overlay_set_tooltip(_g_presentation_obj_coop_companion_class_select_0_default,gstr.default)
        overlay_set_tooltip(_g_presentation_obj_coop_companion_class_select_1_default,gstr.default)
        position_set_y(1,208)
        var023 = 259
        position_set_x(1,var023)
        overlay_set_position(_g_presentation_obj_coop_companion_class_select_0_default,1)
        var023 += 55
        position_set_x(1,var023)
        overlay_set_position(_g_presentation_obj_coop_companion_class_select_0_infantry,1)
        var023 += 55
        position_set_x(1,var023)
        overlay_set_position(_g_presentation_obj_coop_companion_class_select_0_ranged,1)
        var023 += 55
        position_set_x(1,var023)
        overlay_set_position(_g_presentation_obj_coop_companion_class_select_0_mounted,1)
        var023 = 539
        position_set_x(1,var023)
        overlay_set_position(_g_presentation_obj_coop_companion_class_select_1_default,1)
        var023 += 55
        position_set_x(1,var023)
        overlay_set_position(_g_presentation_obj_coop_companion_class_select_1_infantry,1)
        var023 += 55
        position_set_x(1,var023)
        overlay_set_position(_g_presentation_obj_coop_companion_class_select_1_ranged,1)
        var023 += 55
        position_set_x(1,var023)
        overlay_set_position(_g_presentation_obj_coop_companion_class_select_1_mounted,1)
        team_faction_007 = team_get_faction(0)
        overlay_set_color(_g_presentation_obj_coop_companion_class_select_0_default,16777215)
        overlay_set_color(_g_presentation_obj_coop_companion_class_select_1_default,16777215)
        overlay_set_color(_g_presentation_obj_coop_companion_class_select_0_infantry,16777215)
        overlay_set_color(_g_presentation_obj_coop_companion_class_select_1_infantry,16777215)
        overlay_set_color(_g_presentation_obj_coop_companion_class_select_0_ranged,16777215)
        overlay_set_color(_g_presentation_obj_coop_companion_class_select_1_ranged,16777215)
        overlay_set_color(_g_presentation_obj_coop_companion_class_select_0_mounted,16777215)
        overlay_set_color(_g_presentation_obj_coop_companion_class_select_1_mounted,16777215)
        overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_0_default,170)
        overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_1_default,170)
        overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_0_infantry,170)
        overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_1_infantry,170)
        overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_0_ranged,170)
        overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_1_ranged,170)
        overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_0_mounted,170)
        overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_1_mounted,170)
        if _g_presentation_obj_coop_companion_class_0 == _g_presentation_obj_coop_companion_0:
            overlay_set_color(_g_presentation_obj_coop_companion_class_select_0_default,13750170)
            overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_0_default,16777215)
        #end
        if _g_presentation_obj_coop_companion_class_1 == _g_presentation_obj_coop_companion_1:
            overlay_set_color(_g_presentation_obj_coop_companion_class_select_1_default,13750170)
            overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_1_default,16777215)
        #end
        var024 = 0
        for trp_025 in range(trp.swadian_crossbowman_multiplayer_coop_tier_1, trp.coop_faction_troop_templates_end):
            troop_faction_026 = store_faction_of_troop(trp_025)
            if troop_faction_026 == team_faction_007:
                character_lvl_027 = store_character_level(trp_025)
                if character_lvl_027 == 4:
                    s0 = str_store_troop_name(trp_025)
                    var024 += 1
                    if var024 == 2:
                        reg0 = var024
                        overlay_set_tooltip(_g_presentation_obj_coop_companion_class_select_0_infantry,0)
                        overlay_set_tooltip(_g_presentation_obj_coop_companion_class_select_1_infantry,0)
                        if _g_presentation_obj_coop_companion_class_0 == trp_025:
                            overlay_set_color(_g_presentation_obj_coop_companion_class_select_0_infantry,3372352)
                            overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_0_infantry,255)
                        #end
                    #end
                #end
                if _g_presentation_obj_coop_companion_class_1 == trp_025:
                    overlay_set_color(_g_presentation_obj_coop_companion_class_select_1_infantry,3372352)
                    overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_1_infantry,255)
                #end
            elif var024 == 1:
                reg0 = var024
                overlay_set_tooltip(_g_presentation_obj_coop_companion_class_select_0_ranged,0)
                overlay_set_tooltip(_g_presentation_obj_coop_companion_class_select_1_ranged,0)
                if _g_presentation_obj_coop_companion_class_0 == trp_025:
                    overlay_set_color(_g_presentation_obj_coop_companion_class_select_0_ranged,11742754)
                    overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_0_ranged,255)
                #end
                if _g_presentation_obj_coop_companion_class_1 == trp_025:
                    overlay_set_color(_g_presentation_obj_coop_companion_class_select_1_ranged,11742754)
                    overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_1_ranged,255)
                #end
            elif var024 == 3:
                reg0 = var024
                overlay_set_tooltip(_g_presentation_obj_coop_companion_class_select_0_mounted,0)
                overlay_set_tooltip(_g_presentation_obj_coop_companion_class_select_1_mounted,0)
                if _g_presentation_obj_coop_companion_class_0 == trp_025:
                    overlay_set_color(_g_presentation_obj_coop_companion_class_select_0_mounted,5789635)
                    overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_0_mounted,255)
                #end
                if _g_presentation_obj_coop_companion_class_1 == trp_025:
                    overlay_set_color(_g_presentation_obj_coop_companion_class_select_1_mounted,5789635)
                    overlay_set_alpha(_g_presentation_obj_coop_companion_class_select_1_mounted,255)
                #end
            #end
        #end
        create_mesh_overlay_with_tableau_material(reg0,-1,tableau.coop_companion_select_0,_g_presentation_obj_coop_companion_0)
        position_set_x(1,230)
        position_set_y(1,349)
        overlay_set_position(reg0,1)
        position_set_x(1,750)
        position_set_y(1,1000)
        overlay_set_size(reg0,1)
        create_mesh_overlay_with_tableau_material(reg0,-1,tableau.coop_companion_select_0,_g_presentation_obj_coop_companion_1)
        position_set_x(1,510)
        position_set_y(1,349)
        overlay_set_position(reg0,1)
        position_set_x(1,750)
        position_set_y(1,1000)
        overlay_set_size(reg0,1)
        create_button_overlay(_g_presentation_obj_coop_companion_select_done,gstr.done)
        position_set_x(1,468)
        position_set_y(1,170)
        overlay_set_position(_g_presentation_obj_coop_companion_select_done,1)
        overlay_set_color(_g_presentation_obj_coop_companion_select_done,16777215)
    #end
    my_player = multiplayer_get_my_player()
    mp_set_coop_companions(my_player)
    multiplayer_send_item_selections()
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_item_select.add_event(event)
event = MouseEnterLeaveEvent()
def code(var001, var002):
    if _g_close_equipment_selection == 0 and _g_presentation_state == 10:
        pass
    elif _g_close_equipment_selection == 0:
        if var002 == 0:
            troop_slot_003 = -1
            if var001 >= _g_presentation_obj_item_select_next:
                var004 = var001 - _g_presentation_obj_item_select_next
                var005 = store_mod(var004,2)
                var005 = 1 - var005
                var004 /= 2
                slot_no_006 = 46 + var004
                troop_slot_003 = troop_get_slot(trp.multiplayer_data,slot_no_006)
                var007 = var001
                var007 += var005
            elif var001 == _g_presentation_obj_item_select_1:
                slot_no_008 = 2 + 1
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_1
            elif var001 == _g_presentation_obj_item_select_2:
                slot_no_008 = 2 + 2
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_2
            elif var001 == _g_presentation_obj_item_select_3:
                slot_no_008 = 2 + 3
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_3
            elif var001 == _g_presentation_obj_item_select_4:
                slot_no_008 = 2 + 4
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_4
            elif var001 == _g_presentation_obj_item_select_5:
                slot_no_008 = 2 + 5
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_5
            elif var001 == _g_presentation_obj_item_select_6:
                slot_no_008 = 2 + 6
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_6
            elif var001 == _g_presentation_obj_item_select_7:
                slot_no_008 = 2 + 7
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_7
            elif var001 == _g_presentation_obj_item_select_8:
                slot_no_008 = 2 + 8
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_8
            elif var001 == _g_presentation_obj_item_select_9 and _g_horses_are_avaliable == 1:
                slot_no_008 = 2 + 9
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_9
            #end
            if troop_slot_003 >= 0:
                pos0 = overlay_get_position(var007)
                my_player = multiplayer_get_my_player()
                troop_id_010 = player_get_troop_id(my_player)
                if cf_multiplayer_is_item_default_for_troop(troop_slot_003,troop_id_010):
                    show_item_details(troop_slot_003,0,0)
                else:
                    troop_faction_011 = store_faction_of_troop(troop_id_010)
                    slot_no_012 = troop_faction_011 - fac.kingdom_1
                    slot_no_012 += 30
                    item_slot_013 = item_get_slot(troop_slot_003,slot_no_012)
                    show_item_details(troop_slot_003,0,item_slot_013)
                #end
                _g_current_opened_item_details = troop_slot_003
            #end
        else:
            troop_slot_003 = -1
            if var001 >= _g_presentation_obj_item_select_next:
                var004 = var001 - _g_presentation_obj_item_select_next
                var004 /= 2
                slot_no_006 = 46 + var004
                troop_slot_003 = troop_get_slot(trp.multiplayer_data,slot_no_006)
            elif var001 == _g_presentation_obj_item_select_1:
                slot_no_008 = 2 + 1
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_1
            elif var001 == _g_presentation_obj_item_select_2:
                slot_no_008 = 2 + 2
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_2
            elif var001 == _g_presentation_obj_item_select_3:
                slot_no_008 = 2 + 3
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_3
            elif var001 == _g_presentation_obj_item_select_4:
                slot_no_008 = 2 + 4
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_4
            elif var001 == _g_presentation_obj_item_select_5:
                slot_no_008 = 2 + 5
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_5
            elif var001 == _g_presentation_obj_item_select_6:
                slot_no_008 = 2 + 6
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_6
            elif var001 == _g_presentation_obj_item_select_7:
                slot_no_008 = 2 + 7
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_7
            elif var001 == _g_presentation_obj_item_select_8:
                slot_no_008 = 2 + 8
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_8
            elif var001 == _g_presentation_obj_item_select_9 and _g_horses_are_avaliable == 1:
                slot_no_008 = 2 + 9
                slot_no_008 -= 1
                my_player = multiplayer_get_my_player()
                troop_slot_003 = player_get_slot(my_player,slot_no_008)
                var007 = _g_inside_obj_9
            #end
            if _g_current_opened_item_details == troop_slot_003:
                close_item_details()
                _g_current_opened_item_details = -1
            #end
        #end
    else:
        _g_close_equipment_selection = 0
        my_player = multiplayer_get_my_player()
        mp_set_coop_companions(my_player)
        multiplayer_send_item_selections()
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_item_select.add_event(event)
event = StateChangedEvent()
def code(var001, random_x_002):
    var001_list2 = [
    _g_presentation_obj_coop_companion_class_select_1_mounted,
    _g_presentation_obj_coop_companion_class_select_1_ranged,
    _g_presentation_obj_coop_companion_class_select_1_infantry,
    _g_presentation_obj_coop_companion_random_select_1,
    ]
    var001_list1 = [
    _g_presentation_obj_coop_companion_class_select_0_mounted,
    _g_presentation_obj_coop_companion_class_select_0_ranged,
    _g_presentation_obj_coop_companion_class_select_0_infantry,
    _g_presentation_obj_coop_companion_random_select_0,
    ]
    var001_list2 = [
    _g_presentation_obj_coop_companion_class_select_1_mounted,
    _g_presentation_obj_coop_companion_class_select_1_ranged,
    _g_presentation_obj_coop_companion_class_select_1_infantry,
    _g_presentation_obj_coop_companion_random_select_1,
    _g_presentation_obj_coop_companion_class_select_0_mounted,
    _g_presentation_obj_coop_companion_class_select_0_ranged,
    _g_presentation_obj_coop_companion_class_select_0_infantry,
    _g_presentation_obj_coop_companion_random_select_0,
    ]
    my_player = multiplayer_get_my_player()
    troop_id_004 = player_get_troop_id(my_player)
    team_no_005 = player_get_team_no(my_player)
    if _g_close_equipment_selection == 0:
        if _g_presentation_state == 0:
            if var001 == _g_presentation_obj_item_select_1:
                _g_presentation_state = 1
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 == _g_presentation_obj_item_select_2:
                _g_presentation_state = 2
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 == _g_presentation_obj_item_select_3:
                _g_presentation_state = 3
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 == _g_presentation_obj_item_select_4:
                _g_presentation_state = 4
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 == _g_presentation_obj_item_select_5:
                _g_presentation_state = 5
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 == _g_presentation_obj_item_select_6:
                _g_presentation_state = 6
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 == _g_presentation_obj_item_select_7:
                _g_presentation_state = 7
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 == _g_presentation_obj_item_select_8:
                _g_presentation_state = 8
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 == _g_presentation_obj_item_select_9 and _g_horses_are_avaliable == 1:
                _g_presentation_state = 9
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 == _g_presentation_obj_item_select_17:
                _g_presentation_state = 10
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            #end
        elif is_between(_g_presentation_state,0,10):
            var006 = var001 - _g_presentation_obj_item_select_next
            var006 /= 2
            var007 = 146
            for slot_no_008 in range(46, var007):
                if not troop_slot_eq(trp.multiplayer_data,slot_no_008,-1):
                    var009 = slot_no_008 - 46
                    if var006 == var009:
                        troop_slot_010 = troop_get_slot(trp.multiplayer_data,slot_no_008)
                        if True:
                            slot_no_011 = 2 + _g_presentation_state
                            slot_no_011 -= 1
                            player_set_slot(my_player,slot_no_011,troop_slot_010)
                            multiplayer_update_cost_labels()
                            var007 = 0
                        #end
                    #end
                #end
            #end
            presentation_set_duration(0)
            _g_presentation_state = 0
            start_presentation(prsnt.multiplayer_item_select)
        elif _g_presentation_state == 10:
            my_player = multiplayer_get_my_player()
            troop_id_004 = player_get_troop_id(my_player)
            team_faction_012 = team_get_faction(0)
            if var001 == _g_presentation_obj_coop_companion_select_done and _g_multiplayer_game_type == 8:
                mp_set_coop_companions(my_player)
                multiplayer_send_item_selections()
                presentation_set_duration(0)
                _g_presentation_state = 0
                start_presentation(prsnt.multiplayer_item_select)
            elif player_slot_eq(my_player,42,0) and var001 == _g_presentation_obj_coop_companion_random_select_0 or var001 == _g_presentation_obj_coop_companion_select_0:
                if var001 == _g_presentation_obj_coop_companion_random_select_0:
                    random_x_002 = store_random_in_range(trp.npc1_1,trp.npc1_2)
                else:
                    random_x_002 = random_x_002 + trp.npc1_1
                #end
                var013 = random_x_002 - _g_presentation_obj_coop_companion_0
                if random_x_002 == _g_presentation_obj_coop_companion_1:
                    if var013 != 15 and var013 > 0 or var013 == -15:
                        random_x_002 += 1
                        if random_x_002 >= trp.npc1_2:
                            random_x_002 = trp.npc1_1
                        #end
                    else:
                        random_x_002 -= 1
                        if random_x_002 < trp.npc1_1:
                            random_x_002 = trp.npc1_2
                            random_x_002 -= 1
                        #end
                    #end
                #end
                _g_presentation_obj_coop_companion_0 = random_x_002
                if is_between(_g_presentation_obj_coop_companion_class_0,trp.npc1_1,trp.coop_companion_equipment_sets_end):
                    random_x_002 = _g_presentation_obj_coop_companion_0 - trp.npc1_1
                    random_x_002 = random_x_002 + trp.npc1_1
                    _g_presentation_obj_coop_companion_class_0 = random_x_002
                #end
                mp_set_coop_companions(my_player)
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif player_slot_eq(my_player,42,0) and var001 == _g_presentation_obj_coop_companion_random_select_1 or var001 == _g_presentation_obj_coop_companion_select_1:
                if var001 == _g_presentation_obj_coop_companion_random_select_1:
                    random_x_002 = store_random_in_range(trp.npc1_1,trp.npc1_2)
                else:
                    random_x_002 = random_x_002 + trp.npc1_1
                #end
                var013 = random_x_002 - _g_presentation_obj_coop_companion_1
                if random_x_002 == _g_presentation_obj_coop_companion_0:
                    if var013 != 15 and var013 > 0 or var013 == -15:
                        random_x_002 += 1
                        if random_x_002 >= trp.npc1_2:
                            random_x_002 = trp.npc1_1
                        #end
                    else:
                        random_x_002 -= 1
                        if random_x_002 < trp.npc1_1:
                            random_x_002 = trp.npc1_2
                            random_x_002 -= 1
                        #end
                    #end
                #end
                _g_presentation_obj_coop_companion_1 = random_x_002
                if is_between(_g_presentation_obj_coop_companion_class_1,trp.npc1_1,trp.coop_companion_equipment_sets_end):
                    random_x_002 = _g_presentation_obj_coop_companion_1 - trp.npc1_1
                    random_x_002 = random_x_002 + trp.npc1_1
                    _g_presentation_obj_coop_companion_class_1 = random_x_002
                #end
                mp_set_coop_companions(my_player)
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 == _g_presentation_obj_coop_companion_class_select_0_default:
                _g_presentation_obj_coop_companion_class_0 = _g_presentation_obj_coop_companion_0
                mp_set_coop_companions(my_player)
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 == _g_presentation_obj_coop_companion_class_select_1_default:
                _g_presentation_obj_coop_companion_class_1 = _g_presentation_obj_coop_companion_1
                mp_set_coop_companions(my_player)
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 in var001_list2:
                pass
            else:
                presentation_set_duration(0)
                _g_presentation_state = 0
                start_presentation(prsnt.multiplayer_item_select)
            #end
            if var001 in var001_list1:
                if var001 == _g_presentation_obj_coop_companion_random_select_0:
                    random_x_014 = store_random_in_range(0,2)
                    random_x_015 = 0
                    if random_x_014 == 0:
                        _g_presentation_obj_coop_companion_class_0 = _g_presentation_obj_coop_companion_0
                    else:
                        random_x_015 = store_random_in_range(0,4)
                        if random_x_015 == 0:
                            _g_presentation_obj_coop_companion_class_0 = _g_presentation_obj_coop_companion_0
                        elif random_x_015 == 1:
                            var001 = _g_presentation_obj_coop_companion_class_select_0_infantry
                        elif random_x_015 == 2:
                            var001 = _g_presentation_obj_coop_companion_class_select_0_ranged
                        elif random_x_015 == 3:
                            var001 = _g_presentation_obj_coop_companion_class_select_0_mounted
                        #end
                    #end
                    if random_x_015 == 0:
                        pass
                    else:
                        var016 = 0
                        for trp_017 in range(trp.swadian_crossbowman_multiplayer_coop_tier_1, trp.coop_faction_troop_templates_end):
                            troop_faction_018 = store_faction_of_troop(trp_017)
                            if troop_faction_018 == team_faction_012:
                                character_lvl_019 = store_character_level(trp_017)
                                if character_lvl_019 == 4:
                                    s0 = str_store_troop_name(trp_017)
                                    var016 += 1
                                    reg0 = var016
                                    if var016 == 2 and var001 == _g_presentation_obj_coop_companion_class_select_0_infantry:
                                        _g_presentation_obj_coop_companion_class_0 = trp_017
                                    elif var016 == 1 and var001 == _g_presentation_obj_coop_companion_class_select_0_ranged:
                                        _g_presentation_obj_coop_companion_class_0 = trp_017
                                    elif var016 == 3 and var001 == _g_presentation_obj_coop_companion_class_select_0_mounted:
                                        _g_presentation_obj_coop_companion_class_0 = trp_017
                                    #end
                                #end
                            #end
                        #end
                    #end
                #end
                mp_set_coop_companions(my_player)
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            elif var001 in var001_list2:
                if var001 == _g_presentation_obj_coop_companion_random_select_1:
                    random_x_014 = store_random_in_range(0,2)
                    random_x_015 = 0
                    if random_x_014 == 0:
                        _g_presentation_obj_coop_companion_class_1 = _g_presentation_obj_coop_companion_1
                    else:
                        random_x_015 = store_random_in_range(0,4)
                        if random_x_015 == 0:
                            _g_presentation_obj_coop_companion_class_1 = _g_presentation_obj_coop_companion_1
                        elif random_x_015 == 1:
                            var001 = _g_presentation_obj_coop_companion_class_select_1_infantry
                        elif random_x_015 == 2:
                            var001 = _g_presentation_obj_coop_companion_class_select_1_ranged
                        elif random_x_015 == 3:
                            var001 = _g_presentation_obj_coop_companion_class_select_1_mounted
                        #end
                    #end
                    if random_x_015 == 0:
                        pass
                    else:
                        var016 = 0
                        for trp_017 in range(trp.swadian_crossbowman_multiplayer_coop_tier_1, trp.coop_faction_troop_templates_end):
                            troop_faction_018 = store_faction_of_troop(trp_017)
                            if troop_faction_018 == team_faction_012:
                                character_lvl_019 = store_character_level(trp_017)
                                if character_lvl_019 == 4:
                                    s0 = str_store_troop_name(trp_017)
                                    var016 += 1
                                    if var016 == 2 and var001 == _g_presentation_obj_coop_companion_class_select_1_infantry:
                                        _g_presentation_obj_coop_companion_class_1 = trp_017
                                    elif var016 == 1 and var001 == _g_presentation_obj_coop_companion_class_select_1_ranged:
                                        _g_presentation_obj_coop_companion_class_1 = trp_017
                                    elif var016 == 3 and var001 == _g_presentation_obj_coop_companion_class_select_1_mounted:
                                        _g_presentation_obj_coop_companion_class_1 = trp_017
                                    #end
                                #end
                            #end
                        #end
                    #end
                #end
                mp_set_coop_companions(my_player)
                presentation_set_duration(0)
                start_presentation(prsnt.multiplayer_item_select)
            #end
        #end
        if var001 == _g_presentation_obj_item_select_10:
            multiplayer_set_default_item_selections_for_troop(troop_id_004)
            presentation_set_duration(0)
            _g_presentation_state = 0
            start_presentation(prsnt.multiplayer_item_select)
        elif var001 == _g_presentation_obj_item_select_11:
            multiplayer_send_item_selections()
            presentation_set_duration(0)
            if True:
                if _g_multiplayer_game_type == 6 and _g_multiplayer_number_of_respawn_count > 0 and _g_my_spawn_count >= _g_multiplayer_number_of_respawn_count:
                    my_player = multiplayer_get_my_player()
                    team_no_005 = player_get_team_no(my_player)
                    if team_no_005 == 0 or _g_my_spawn_count >= 999:
                        _g_show_no_more_respawns_remained = 1
                    else:
                        _g_show_no_more_respawns_remained = 0
                    #end
                #end
                if _g_show_no_more_respawns_remained == 1:
                    _g_multiplayer_respawn_start_time = store_mission_timer_a()
                    start_presentation(prsnt.multiplayer_respawn_time_counter)
                #end
            #end
        elif var001 == _g_presentation_obj_item_select_13:
            _g_multiplayer_bot_type_1_wanted = random_x_002
            multiplayer_send_2_int_to_server(1,35,random_x_002)
        elif var001 == _g_presentation_obj_item_select_14:
            _g_multiplayer_bot_type_2_wanted = random_x_002
            multiplayer_send_2_int_to_server(1,36,random_x_002)
        elif var001 == _g_presentation_obj_item_select_15:
            _g_multiplayer_bot_type_3_wanted = random_x_002
            multiplayer_send_2_int_to_server(1,37,random_x_002)
        elif var001 == _g_presentation_obj_item_select_16:
            _g_multiplayer_bot_type_4_wanted = random_x_002
            multiplayer_send_2_int_to_server(1,38,random_x_002)
        #end
    else:
        _g_close_equipment_selection = 0
        multiplayer_send_item_selections()
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_item_select.add_event(event)
event = MousePressEvent()
def code(var001, var002):
    if _g_close_equipment_selection == 0:
        if var002 == 1:
            if _g_presentation_state == 0:
                my_player = multiplayer_get_my_player()
                if var001 == _g_presentation_obj_item_select_1:
                    slot_no_004 = 2 + 0
                    player_set_slot(my_player,slot_no_004,-1)
                    presentation_set_duration(0)
                    _g_presentation_state = 0
                    start_presentation(prsnt.multiplayer_item_select)
                elif var001 == _g_presentation_obj_item_select_2:
                    slot_no_004 = 2 + 1
                    player_set_slot(my_player,slot_no_004,-1)
                    presentation_set_duration(0)
                    _g_presentation_state = 0
                    start_presentation(prsnt.multiplayer_item_select)
                elif var001 == _g_presentation_obj_item_select_3:
                    slot_no_004 = 2 + 2
                    player_set_slot(my_player,slot_no_004,-1)
                    presentation_set_duration(0)
                    _g_presentation_state = 0
                    start_presentation(prsnt.multiplayer_item_select)
                elif var001 == _g_presentation_obj_item_select_4:
                    slot_no_004 = 2 + 3
                    player_set_slot(my_player,slot_no_004,-1)
                    presentation_set_duration(0)
                    _g_presentation_state = 0
                    start_presentation(prsnt.multiplayer_item_select)
                elif var001 == _g_presentation_obj_item_select_5:
                    slot_no_004 = 2 + 4
                    player_set_slot(my_player,slot_no_004,-1)
                    presentation_set_duration(0)
                    _g_presentation_state = 0
                    start_presentation(prsnt.multiplayer_item_select)
                elif var001 == _g_presentation_obj_item_select_6:
                    slot_no_004 = 2 + 5
                    player_set_slot(my_player,slot_no_004,-1)
                    presentation_set_duration(0)
                    _g_presentation_state = 0
                    start_presentation(prsnt.multiplayer_item_select)
                elif var001 == _g_presentation_obj_item_select_7:
                    slot_no_004 = 2 + 6
                    player_set_slot(my_player,slot_no_004,-1)
                    presentation_set_duration(0)
                    _g_presentation_state = 0
                    start_presentation(prsnt.multiplayer_item_select)
                elif var001 == _g_presentation_obj_item_select_8:
                    slot_no_004 = 2 + 7
                    player_set_slot(my_player,slot_no_004,-1)
                    presentation_set_duration(0)
                    _g_presentation_state = 0
                    start_presentation(prsnt.multiplayer_item_select)
                elif var001 == _g_presentation_obj_item_select_9 and _g_horses_are_avaliable == 1:
                    slot_no_004 = 2 + 8
                    player_set_slot(my_player,slot_no_004,-1)
                    presentation_set_duration(0)
                    _g_presentation_state = 0
                    start_presentation(prsnt.multiplayer_item_select)
                #end
            elif _g_presentation_state == 10:
                pass
            elif _g_presentation_state > 0:
                presentation_set_duration(0)
                _g_presentation_state = 0
                start_presentation(prsnt.multiplayer_item_select)
            #end
        #end
    else:
        _g_close_equipment_selection = 0
        multiplayer_send_item_selections()
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_item_select.add_event(event)
event = RunEvent()
def code(var001):
    if _g_close_equipment_selection == 0:
        if key_clicked(1) or key_clicked(248):
            if _g_current_opened_item_details != -1:
                close_item_details()
                _g_current_opened_item_details = -1
            #end
            if var001 > 200:
                my_player = multiplayer_get_my_player()
                mp_set_coop_companions(my_player)
                multiplayer_send_item_selections()
                presentation_set_duration(0)
            #end
        #end
    else:
        _g_close_equipment_selection = 0
        multiplayer_send_item_selections()
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_item_select.add_event(event)


multiplayer_message_1 = Presentation("multiplayer_message_1")
multiplayer_message_1.set_read_only()
multiplayer_message_1.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    if _g_multiplayer_message_type == 12:
        team_id_001 = _g_multiplayer_message_value_1
        if team_id_001 == -1:
            var002 = 4294967295
            s0 = str_store_string(gstr.round_draw_no_one_remained)
        else:
            if team_id_001 == 0:
                var002 = 4281589009
            else:
                var002 = 4294919202
            #end
            if _my_team_at_start_of_round < 2:
                if _my_team_at_start_of_round == team_id_001:
                    var002 = 4281589009
                else:
                    var002 = 4294919202
                #end
            #end
            team_faction_003 = team_get_faction(team_id_001)
            s1 = str_store_faction_name(team_faction_003)
            s0 = str_store_string(gstr.s1_won_round)
        #end
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        if team_id_001 != -1:
            position_set_x(1,375)
        else:
            position_set_x(1,400)
        #end
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(300)
    elif _g_multiplayer_message_type == 4:
        team_id_001 = agent_get_team(_g_multiplayer_message_value_1)
        team_faction_004 = team_get_faction(team_id_001)
        s1 = str_store_faction_name(team_faction_004)
        if team_id_001 == 0:
            var002 = 4281589009
        else:
            var002 = 4294919202
        #end
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            agent_id_006 = player_get_agent_id(my_player)
            if agent_id_006 >= 0:
                agent_team_no_007 = agent_get_team(agent_id_006)
                if agent_team_no_007 == team_id_001:
                    var002 = 4281589009
                    play_sound(snd.team_scored_a_point)
                else:
                    var002 = 4294919202
                    play_sound(snd.enemy_scored_a_point)
                #end
            #end
        #end
        s0 = str_store_string(gstr.s1_captured_flag)
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        position_set_x(1,350)
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    elif _g_multiplayer_message_type == 5:
        if _g_multiplayer_message_value_1 >= 0:
            agent_team_no_008 = agent_get_team(_g_multiplayer_message_value_1)
            team_faction_009 = team_get_faction(agent_team_no_008)
            s1 = str_store_faction_name(team_faction_009)
            s0 = str_store_string(gstr.s1_returned_flag)
        else:
            _g_multiplayer_message_value_1 += 1
            _g_multiplayer_message_value_1 *= -1
            agent_team_no_008 = _g_multiplayer_message_value_1
            team_faction_009 = team_get_faction(agent_team_no_008)
            s1 = str_store_faction_name(team_faction_009)
            s0 = str_store_string(gstr.s1_auto_returned_flag)
        #end
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            agent_id_006 = player_get_agent_id(my_player)
            if agent_id_006 >= 0:
                play_sound(snd.flag_returned)
            #end
        #end
        var002 = 4294967295
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        position_set_x(1,325)
        position_set_y(1,400)
        position_set_x(1,500)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    elif _g_multiplayer_message_type == 6:
        agent_team_no_010 = agent_get_team(_g_multiplayer_message_value_1)
        team_faction_011 = team_get_faction(agent_team_no_010)
        s1 = str_store_faction_name(team_faction_011)
        var002 = 4294967295
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            agent_id_006 = player_get_agent_id(my_player)
            if agent_id_006 >= 0:
                agent_team_no_007 = agent_get_team(agent_id_006)
                if agent_team_no_007 == agent_team_no_010:
                    play_sound(snd.enemy_flag_taken)
                else:
                    play_sound(snd.your_flag_taken)
                #end
            #end
        #end
        s0 = str_store_string(gstr.s1_taken_flag)
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        position_set_x(1,365)
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    elif _g_multiplayer_message_type == 9:
        team_id_001 = _g_multiplayer_message_value_1 / 100
        reg0 = store_mod(_g_multiplayer_message_value_1,100)
        team_id_001 -= 1
        if team_id_001 == 0:
            var002 = 4281589009
        else:
            var002 = 4294919202
        #end
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            agent_id_006 = player_get_agent_id(my_player)
            if agent_id_006 >= 0:
                agent_team_no_007 = agent_get_team(agent_id_006)
                if agent_team_no_007 == team_id_001:
                    var002 = 4281589009
                    play_sound(snd.team_scored_a_point)
                else:
                    var002 = 4294919202
                    play_sound(snd.enemy_scored_a_point)
                #end
            #end
        #end
        team_faction_004 = team_get_faction(team_id_001)
        s1 = str_store_faction_name(team_faction_004)
        s0 = str_store_string(gstr.s1_captured_flag_reg0)
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        position_set_x(1,345)
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    elif _g_multiplayer_message_type == 10:
        team_id_001 = _g_multiplayer_message_value_1 / 100
        reg0 = store_mod(_g_multiplayer_message_value_1,100)
        team_id_001 -= 1
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            agent_id_006 = player_get_agent_id(my_player)
            if agent_id_006 >= 0:
                agent_team_no_007 = agent_get_team(agent_id_006)
                if agent_team_no_007 == team_id_001:
                    play_sound(snd.enemy_flag_taken)
                else:
                    play_sound(snd.your_flag_taken)
                #end
            #end
        #end
        var002 = 4294967295
        team_faction_004 = team_get_faction(team_id_001)
        s1 = str_store_faction_name(team_faction_004)
        s0 = str_store_string(gstr.s1_pulling_flag_reg0)
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        position_set_x(1,345)
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    elif _g_multiplayer_message_type == 8:
        team_id_001 = _g_multiplayer_message_value_1 / 100
        reg0 = store_mod(_g_multiplayer_message_value_1,100)
        team_id_001 -= 1
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            agent_id_006 = player_get_agent_id(my_player)
            if agent_id_006 >= 0:
                play_sound(snd.flag_returned)
            #end
        #end
        if team_id_001 == 0:
            var002 = 4281589009
        else:
            var002 = 4294919202
        #end
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            agent_id_006 = player_get_agent_id(my_player)
            if agent_id_006 >= 0:
                agent_team_no_007 = agent_get_team(agent_id_006)
                if agent_team_no_007 == team_id_001:
                    var002 = 4281589009
                else:
                    var002 = 4294919202
                #end
            #end
        #end
        team_faction_004 = team_get_faction(team_id_001)
        s1 = str_store_faction_name(team_faction_004)
        s0 = str_store_string(gstr.s1_neutralized_flag_reg0)
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        position_set_x(1,345)
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    elif _g_multiplayer_message_type == 13:
        team_id_001 = _g_multiplayer_message_value_1
        if team_id_001 == 0:
            var002 = 4281589009
        else:
            var002 = 4294919202
        #end
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            agent_id_006 = player_get_agent_id(my_player)
            if agent_id_006 >= 0:
                agent_team_no_007 = agent_get_team(agent_id_006)
                if agent_team_no_007 == team_id_001:
                    var002 = 4281589009
                else:
                    var002 = 4294919202
                #end
            #end
        #end
        if _g_multiplayer_message_value_1 == 0:
            s0 = str_store_string(gstr.s1_defended_castle)
        elif _g_multiplayer_message_value_1 == 1:
            s0 = str_store_string(gstr.s1_captured_castle)
        else:
            s0 = str_store_string(gstr.round_draw)
            var002 = 4294967295
        #end
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        if _g_multiplayer_message_value_1 != -1:
            position_set_x(1,325)
        else:
            position_set_x(1,400)
        #end
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    elif _g_multiplayer_message_type == 14:
        var002 = 4294967295
        s0 = str_store_string(gstr.round_draw)
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        position_set_x(1,375)
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    elif _g_multiplayer_message_type == 18:
        var002 = 4294967295
        s0 = str_store_string(gstr.death_mode_started)
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        position_set_x(1,350)
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    elif _g_multiplayer_message_type == 15:
        if _g_multiplayer_message_value_1 < 0:
            _g_multiplayer_message_value_1 *= -1
            var012 = 0
            team_faction_003 = team_get_faction(1)
            s1 = str_store_faction_name(team_faction_003)
        else:
            var012 = 1
            team_faction_003 = team_get_faction(0)
            s1 = str_store_faction_name(team_faction_003)
        #end
        if _g_multiplayer_message_value_1 == 1:
            var002 = 4281589009
        else:
            var002 = 4294919202
        #end
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            if True:
                my_player = multiplayer_get_my_player()
                team_no_013 = player_get_team_no(my_player)
                if var012 != team_no_013:
                    var002 = 4281589009
                else:
                    var002 = 4294919202
                #end
            #end
        #end
        if _g_multiplayer_message_value_1 == 9:
            s0 = str_store_string(gstr.s1_destroyed_all_targets)
        elif _g_multiplayer_message_value_1 == 1:
            s0 = str_store_string(gstr.s1_destroyed_catapult)
        elif _g_multiplayer_message_value_1 == 2:
            s0 = str_store_string(gstr.s1_destroyed_trebuchet)
        #end
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        position_set_x(1,350)
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    elif _g_multiplayer_message_type == 16:
        if _g_defender_team == 0:
            var002 = 4281589009
        else:
            var002 = 4294919202
        #end
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            agent_id_006 = player_get_agent_id(my_player)
            if agent_id_006 >= 0:
                agent_team_no_007 = agent_get_team(agent_id_006)
                if agent_team_no_007 == _g_defender_team:
                    var002 = 4281589009
                else:
                    var002 = 4294919202
                #end
            #end
        #end
        var014 = _g_multiplayer_message_value_1
        team_faction_003 = team_get_faction(_g_defender_team)
        s1 = str_store_faction_name(team_faction_003)
        if var014 == 1:
            s0 = str_store_string(gstr.s1_saved_1_target)
        elif var014 == 2:
            s0 = str_store_string(gstr.s1_saved_2_targets)
        #end
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        position_set_x(1,350)
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    elif _g_multiplayer_message_type == 17:
        team_id_001 = _g_multiplayer_message_value_1
        if team_id_001 == 0:
            var002 = 4281589009
        else:
            var002 = 4294919202
        #end
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            agent_id_006 = player_get_agent_id(my_player)
            if agent_id_006 >= 0:
                agent_team_no_007 = agent_get_team(agent_id_006)
                if agent_team_no_007 == team_id_001:
                    var002 = 4281589009
                else:
                    var002 = 4294919202
                #end
            #end
        #end
        if _g_defender_team == 0:
            team_faction_003 = team_get_faction(1)
        else:
            team_faction_003 = team_get_faction(0)
        #end
        s1 = str_store_faction_name(team_faction_003)
        s0 = str_store_string(gstr.s1_won_round)
        create_text_overlay(_g_multiplayer_message_1,0,65552)
        overlay_set_color(_g_multiplayer_message_1,var002)
        position_set_x(1,350)
        position_set_x(1,500)
        position_set_y(1,400)
        overlay_set_position(_g_multiplayer_message_1,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_1,1)
        presentation_set_duration(400)
    #end
event.codeBlock = code
multiplayer_message_1.add_event(event)
event = RunEvent()
def code():
    pass
event.codeBlock = code
multiplayer_message_1.add_event(event)


multiplayer_message_2 = Presentation("multiplayer_message_2")
multiplayer_message_2.set_read_only()
multiplayer_message_2.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    if _g_multiplayer_message_type == 2:
        var001 = 4294967295
        s0 = str_store_string(gstr.auto_team_balance_done)
        create_text_overlay(_g_multiplayer_message_2,0,65552)
        overlay_set_color(_g_multiplayer_message_2,var001)
        position_set_x(1,375)
        position_set_x(1,500)
        position_set_y(1,550)
        overlay_set_position(_g_multiplayer_message_2,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_2,1)
        presentation_set_duration(300)
    elif _g_multiplayer_message_type == 3:
        var001 = 4294967295
        if _g_multiplayer_game_type != 2 and _g_multiplayer_game_type != 3 and _g_multiplayer_game_type != 6:
            s0 = str_store_string(gstr.auto_team_balance_in_20_seconds)
            position_set_x(1,375)
        else:
            s0 = str_store_string(gstr.auto_team_balance_next_round)
            position_set_x(1,375)
        #end
        create_text_overlay(_g_multiplayer_message_2,0,65552)
        overlay_set_color(_g_multiplayer_message_2,var001)
        position_set_y(1,550)
        position_set_x(1,500)
        overlay_set_position(_g_multiplayer_message_2,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_2,1)
        presentation_set_duration(300)
    #end
event.codeBlock = code
multiplayer_message_2.add_event(event)
event = RunEvent()
def code():
    pass
event.codeBlock = code
multiplayer_message_2.add_event(event)


multiplayer_message_3 = Presentation("multiplayer_message_3")
multiplayer_message_3.set_read_only()
multiplayer_message_3.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    if _g_multiplayer_message_type == 7:
        var001 = 4294967295
        if _g_multiplayer_message_value_3 == 1:
            s0 = str_store_string(gstr.poll_result_yes)
        else:
            s0 = str_store_string(gstr.poll_result_no)
        #end
        create_text_overlay(_g_multiplayer_message_3,0,65552)
        overlay_set_color(_g_multiplayer_message_3,var001)
        position_set_x(1,380)
        position_set_x(1,500)
        position_set_y(1,475)
        overlay_set_position(_g_multiplayer_message_3,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_message_3,1)
        presentation_set_duration(400)
    #end
event.codeBlock = code
multiplayer_message_3.add_event(event)
event = RunEvent()
def code():
    pass
event.codeBlock = code
multiplayer_message_3.add_event(event)


multiplayer_round_time_counter = Presentation("multiplayer_round_time_counter")
multiplayer_round_time_counter.set_read_only()
multiplayer_round_time_counter.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    _g_multiplayer_last_round_time_counter_value = -1
    str_clear(0)
    create_text_overlay(_g_multiplayer_round_time_counter_overlay,0,98308)
    overlay_set_color(_g_multiplayer_round_time_counter_overlay,16777215)
    position_set_x(1,900)
    position_set_y(1,690)
    overlay_set_position(_g_multiplayer_round_time_counter_overlay,1)
    position_set_x(1,2000)
    position_set_y(1,2000)
    overlay_set_size(_g_multiplayer_round_time_counter_overlay,1)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_round_time_counter.add_event(event)
event = RunEvent()
def code():
    m_timer_a_001 = store_mission_timer_a()
    var002 = m_timer_a_001 - _g_round_start_time
    var003 = _g_multiplayer_round_max_seconds - var002
    val_max(var003,0)
    if _g_multiplayer_last_round_time_counter_value != var003:
        _g_multiplayer_last_round_time_counter_value = var003
        reg0 = var003 / 60
        reg1 = var003 / 10
        reg1 %= 6
        reg2 = var003
        reg2 %= 10
        s0 = str_store_string(gstr.reg0_dd_reg1reg2)
        overlay_set_text(_g_multiplayer_round_time_counter_overlay,0)
    #end
event.codeBlock = code
multiplayer_round_time_counter.add_event(event)


multiplayer_team_score_display = Presentation("multiplayer_team_score_display")
multiplayer_team_score_display.set_read_only()
multiplayer_team_score_display.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    _g_multiplayer_team_1_last_displayed_score = -1
    _g_multiplayer_team_2_last_displayed_score = -1
    str_clear(0)
    create_text_overlay(_g_multiplayer_team_1_score_display_overlay,0,98308)
    overlay_set_color(_g_multiplayer_team_1_score_display_overlay,16777215)
    position_set_x(1,40)
    position_set_y(1,700)
    overlay_set_position(_g_multiplayer_team_1_score_display_overlay,1)
    position_set_x(1,1500)
    position_set_y(1,1500)
    overlay_set_size(_g_multiplayer_team_1_score_display_overlay,1)
    create_text_overlay(_g_multiplayer_team_2_score_display_overlay,0,98308)
    overlay_set_color(_g_multiplayer_team_2_score_display_overlay,16777215)
    position_set_x(1,40)
    position_set_y(1,645)
    overlay_set_position(_g_multiplayer_team_2_score_display_overlay,1)
    position_set_x(1,1500)
    position_set_y(1,1500)
    overlay_set_size(_g_multiplayer_team_2_score_display_overlay,1)
    if _g_multiplayer_team_1_faction == fac.kingdom_4:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_1)
    elif _g_multiplayer_team_1_faction == fac.kingdom_2:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_2)
    elif _g_multiplayer_team_1_faction == fac.kingdom_3:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_3)
    elif _g_multiplayer_team_1_faction == fac.kingdom_5:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_4)
    elif _g_multiplayer_team_1_faction == fac.kingdom_6:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_5)
    elif _g_multiplayer_team_1_faction == fac.kingdom_1:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_6)
    #end
    position_set_x(3,25)
    position_set_y(3,715)
    overlay_set_position(reg0,3)
    position_set_x(1,50)
    position_set_y(1,50)
    overlay_set_size(reg0,1)
    if _g_multiplayer_team_1_faction == _g_multiplayer_team_2_faction:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_7)
    elif _g_multiplayer_team_2_faction == fac.kingdom_4:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_1)
    elif _g_multiplayer_team_2_faction == fac.kingdom_2:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_2)
    elif _g_multiplayer_team_2_faction == fac.kingdom_3:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_3)
    elif _g_multiplayer_team_2_faction == fac.kingdom_5:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_4)
    elif _g_multiplayer_team_2_faction == fac.kingdom_6:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_5)
    elif _g_multiplayer_team_2_faction == fac.kingdom_1:
        create_mesh_overlay(reg0,mesh.ui_kingdom_shield_6)
    #end
    position_set_x(3,25)
    position_set_y(3,660)
    overlay_set_position(reg0,3)
    position_set_x(1,50)
    position_set_y(1,50)
    overlay_set_size(reg0,1)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_team_score_display.add_event(event)
event = RunEvent()
def code():
    team_score_001 = team_get_score(0)
    team_score_002 = team_get_score(1)
    if team_score_001 == _g_multiplayer_team_1_last_displayed_score or team_score_002 != _g_multiplayer_team_2_last_displayed_score:
        _g_multiplayer_team_1_last_displayed_score = team_score_001
        _g_multiplayer_team_2_last_displayed_score = team_score_002
        s0 = str_store_faction_name(_g_multiplayer_team_1_faction)
        reg0 = team_score_001
        overlay_set_text(_g_multiplayer_team_1_score_display_overlay,gstr.reg0)
        s0 = str_store_faction_name(_g_multiplayer_team_2_faction)
        reg0 = team_score_002
        overlay_set_text(_g_multiplayer_team_2_score_display_overlay,gstr.reg0)
    #end
event.codeBlock = code
multiplayer_team_score_display.add_event(event)


multiplayer_flag_projection_display = Presentation("multiplayer_flag_projection_display")
multiplayer_flag_projection_display.set_read_only()
multiplayer_flag_projection_display.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    var001 = _g_multiplayer_team_1_faction - fac.kingdom_1
    var001 = var001 + mesh.flag_project_sw
    create_mesh_overlay(_g_presentation_obj_flag_projection_display_1,var001)
    var001 = var001 - mesh.flag_project_sw
    var001 = var001 + mesh.flag_project_sw_miss
    create_mesh_overlay(_g_presentation_obj_flag_projection_display_2,var001)
    if _g_multiplayer_team_1_faction != _g_multiplayer_team_2_faction:
        var001 = _g_multiplayer_team_2_faction - fac.kingdom_1
        var001 = var001 + mesh.flag_project_sw
        create_mesh_overlay(_g_presentation_obj_flag_projection_display_3,var001)
        var001 = var001 - mesh.flag_project_sw
        var001 = var001 + mesh.flag_project_sw_miss
        create_mesh_overlay(_g_presentation_obj_flag_projection_display_4,var001)
    else:
        var001 = mesh.flag_project_rb
        create_mesh_overlay(_g_presentation_obj_flag_projection_display_3,var001)
        var001 = mesh.flag_project_rb_miss
        create_mesh_overlay(_g_presentation_obj_flag_projection_display_4,var001)
    #end
    position_set_x(1,250)
    position_set_y(1,250)
    overlay_set_size(_g_presentation_obj_flag_projection_display_1,1)
    overlay_set_size(_g_presentation_obj_flag_projection_display_2,1)
    overlay_set_size(_g_presentation_obj_flag_projection_display_3,1)
    overlay_set_size(_g_presentation_obj_flag_projection_display_4,1)
    overlay_set_display(_g_presentation_obj_flag_projection_display_1,0)
    overlay_set_display(_g_presentation_obj_flag_projection_display_2,0)
    overlay_set_display(_g_presentation_obj_flag_projection_display_3,0)
    overlay_set_display(_g_presentation_obj_flag_projection_display_4,0)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_flag_projection_display.add_event(event)
event = RunEvent()
def code():
    set_fixed_point_multiplier(1000)
    scp_instance_001 = scene_prop_get_instance(_team_1_flag_scene_prop,0)
    team_slot_002 = team_get_slot(0,0)
    if team_slot_002 != 1:
        pos1 = prop_instance_get_position(scp_instance_001)
    else:
        pos1 = entry_point_get_position(64)
    #end
    position_move_z(1,200,1)
    scp_instance_003 = scene_prop_get_instance(_team_2_flag_scene_prop,0)
    team_slot_004 = team_get_slot(1,0)
    if team_slot_004 != 1:
        pos2 = prop_instance_get_position(scp_instance_003)
    else:
        pos2 = entry_point_get_position(65)
    #end
    position_move_z(2,200,1)
    pos3 = position_get_screen_projection(1)
    pos_x_005 = position_get_x(3)
    pos_y_006 = position_get_y(3)
    position_set_y(3,pos_y_006)
    if is_between(pos_x_005,-100,1100) and is_between(pos_y_006,-100,850):
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            team_no_008 = player_get_team_no(my_player)
        else:
            team_no_008 = 2
        #end
        if team_no_008 != 1:
            if team_slot_002 != 1:
                overlay_set_position(_g_presentation_obj_flag_projection_display_1,3)
                overlay_set_display(_g_presentation_obj_flag_projection_display_1,1)
                overlay_set_display(_g_presentation_obj_flag_projection_display_2,0)
            else:
                if team_no_008 == 0:
                    var009 = 64
                else:
                    var009 = 65
                #end
                pos5 = entry_point_get_position(var009)
                pos3 = position_get_screen_projection(5)
                overlay_set_position(_g_presentation_obj_flag_projection_display_2,3)
                overlay_set_display(_g_presentation_obj_flag_projection_display_2,1)
                overlay_set_display(_g_presentation_obj_flag_projection_display_1,0)
            #end
        else:
            if team_slot_002 != 1:
                overlay_set_position(_g_presentation_obj_flag_projection_display_1,3)
                overlay_set_display(_g_presentation_obj_flag_projection_display_1,1)
                overlay_set_display(_g_presentation_obj_flag_projection_display_2,0)
            #end
        #end
    else:
        overlay_set_display(_g_presentation_obj_flag_projection_display_1,0)
        overlay_set_display(_g_presentation_obj_flag_projection_display_2,0)
    #end
    pos3 = position_get_screen_projection(2)
    pos_x_005 = position_get_x(3)
    pos_y_006 = position_get_y(3)
    position_set_y(3,pos_y_006)
    if is_between(pos_x_005,-100,1100) and is_between(pos_y_006,-100,850):
        team_slot_004 = team_get_slot(1,0)
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            team_no_008 = player_get_team_no(my_player)
        else:
            team_no_008 = 2
        #end
        if team_no_008 != 0:
            if team_slot_004 != 1:
                overlay_set_position(_g_presentation_obj_flag_projection_display_3,3)
                overlay_set_display(_g_presentation_obj_flag_projection_display_3,1)
                overlay_set_display(_g_presentation_obj_flag_projection_display_4,0)
            else:
                if team_no_008 == 0:
                    var009 = 64
                else:
                    var009 = 65
                #end
                pos5 = entry_point_get_position(var009)
                pos3 = position_get_screen_projection(5)
                overlay_set_position(_g_presentation_obj_flag_projection_display_4,3)
                overlay_set_display(_g_presentation_obj_flag_projection_display_4,1)
                overlay_set_display(_g_presentation_obj_flag_projection_display_3,0)
            #end
        else:
            if team_slot_004 != 1:
                overlay_set_position(_g_presentation_obj_flag_projection_display_3,3)
                overlay_set_display(_g_presentation_obj_flag_projection_display_3,1)
                overlay_set_display(_g_presentation_obj_flag_projection_display_4,0)
            #end
        #end
    else:
        overlay_set_display(_g_presentation_obj_flag_projection_display_3,0)
        overlay_set_display(_g_presentation_obj_flag_projection_display_4,0)
    #end
event.codeBlock = code
multiplayer_flag_projection_display.add_event(event)


multiplayer_flag_projection_display_bt = Presentation("multiplayer_flag_projection_display_bt")
multiplayer_flag_projection_display_bt.set_read_only()
multiplayer_flag_projection_display_bt.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    var001 = _g_multiplayer_team_1_faction - fac.kingdom_1
    var001 = var001 + mesh.flag_project_sw
    create_mesh_overlay(_g_presentation_obj_flag_projection_display_1,var001)
    if _g_multiplayer_team_1_faction != _g_multiplayer_team_2_faction:
        var001 = _g_multiplayer_team_2_faction - fac.kingdom_1
        var001 = var001 + mesh.flag_project_sw
    else:
        var001 = mesh.flag_project_rb
    #end
    create_mesh_overlay(_g_presentation_obj_flag_projection_display_3,var001)
    position_set_x(1,250)
    position_set_y(1,250)
    overlay_set_size(_g_presentation_obj_flag_projection_display_1,1)
    overlay_set_size(_g_presentation_obj_flag_projection_display_3,1)
    overlay_set_display(_g_presentation_obj_flag_projection_display_1,0)
    overlay_set_display(_g_presentation_obj_flag_projection_display_3,0)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_flag_projection_display_bt.add_event(event)
event = RunEvent()
def code():
    if _g_round_ended == 0:
        set_fixed_point_multiplier(1000)
        scp_instance_001 = scene_prop_get_instance(_team_1_flag_scene_prop,0)
        pos1 = prop_instance_get_position(scp_instance_001)
        position_move_z(1,250,1)
        scp_instance_002 = scene_prop_get_instance(_team_2_flag_scene_prop,0)
        pos2 = prop_instance_get_position(scp_instance_002)
        position_move_z(2,250,1)
        pos3 = position_get_screen_projection(1)
        pos_x_003 = position_get_x(3)
        pos_y_004 = position_get_y(3)
        position_set_y(3,pos_y_004)
        if is_between(pos_x_003,-100,1100) and is_between(pos_y_004,-100,850):
            overlay_set_position(_g_presentation_obj_flag_projection_display_1,3)
            overlay_set_display(_g_presentation_obj_flag_projection_display_1,1)
        else:
            overlay_set_display(_g_presentation_obj_flag_projection_display_1,0)
        #end
        pos3 = position_get_screen_projection(2)
        pos_x_003 = position_get_x(3)
        pos_y_004 = position_get_y(3)
        position_set_y(3,pos_y_004)
        if is_between(pos_x_003,-100,1100) and is_between(pos_y_004,-100,850):
            overlay_set_position(_g_presentation_obj_flag_projection_display_3,3)
            overlay_set_display(_g_presentation_obj_flag_projection_display_3,1)
        else:
            overlay_set_display(_g_presentation_obj_flag_projection_display_3,0)
        #end
    else:
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_flag_projection_display_bt.add_event(event)


multiplayer_destructible_targets_display = Presentation("multiplayer_destructible_targets_display")
multiplayer_destructible_targets_display.set_read_only()
multiplayer_destructible_targets_display.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    if _g_defender_team == 0:
        var001 = _g_multiplayer_team_1_faction - fac.kingdom_1
    else:
        var001 = _g_multiplayer_team_2_faction - fac.kingdom_1
    #end
    var001 = var001 + mesh.flag_project_sw
    create_mesh_overlay(_g_presentation_obj_flag_projection_display_1,var001)
    create_mesh_overlay(_g_presentation_obj_flag_projection_display_2,var001)
    position_set_x(1,250)
    position_set_y(1,250)
    overlay_set_size(_g_presentation_obj_flag_projection_display_1,1)
    overlay_set_size(_g_presentation_obj_flag_projection_display_2,1)
    overlay_set_display(_g_presentation_obj_flag_projection_display_1,0)
    overlay_set_display(_g_presentation_obj_flag_projection_display_2,0)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_destructible_targets_display.add_event(event)
event = RunEvent()
def code():
    if _g_round_ended == 0:
        set_fixed_point_multiplier(1000)
        scp_instance_001 = scene_prop_get_instance(_g_destructible_target_1,0)
        pos1 = prop_instance_get_position(scp_instance_001)
        pos1 = prop_instance_get_position(scp_instance_001)
        position_move_z(1,250,1)
        scp_instance_002 = scene_prop_get_instance(_g_destructible_target_2,0)
        pos2 = prop_instance_get_position(scp_instance_002)
        pos2 = prop_instance_get_position(scp_instance_002)
        position_move_z(2,250,1)
        pos3 = position_get_screen_projection(1)
        pos_x_003 = position_get_x(3)
        pos_y_004 = position_get_y(3)
        position_set_y(3,pos_y_004)
        if is_between(pos_x_003,-100,1100) and is_between(pos_y_004,-100,850):
            pos0 = prop_instance_get_starting_position(scp_instance_001)
            pos1 = prop_instance_get_position(scp_instance_001)
            sq_distance_005 = get_sq_distance_between_positions_in_meters(0,1)
            if sq_distance_005 <= 2:
                overlay_set_position(_g_presentation_obj_flag_projection_display_1,3)
                overlay_set_display(_g_presentation_obj_flag_projection_display_1,1)
            else:
                overlay_set_display(_g_presentation_obj_flag_projection_display_1,0)
            #end
        #end
        pos3 = position_get_screen_projection(2)
        pos_x_003 = position_get_x(3)
        pos_y_004 = position_get_y(3)
        position_set_y(3,pos_y_004)
        if is_between(pos_x_003,-100,1100) and is_between(pos_y_004,-100,850):
            pos0 = prop_instance_get_starting_position(scp_instance_002)
            pos1 = prop_instance_get_position(scp_instance_002)
            sq_distance_005 = get_sq_distance_between_positions_in_meters(0,1)
            if sq_distance_005 <= 2:
                overlay_set_position(_g_presentation_obj_flag_projection_display_2,3)
                overlay_set_display(_g_presentation_obj_flag_projection_display_2,1)
            else:
                overlay_set_display(_g_presentation_obj_flag_projection_display_2,0)
            #end
        #end
    else:
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_destructible_targets_display.add_event(event)


multiplayer_respawn_time_counter = Presentation("multiplayer_respawn_time_counter")
multiplayer_respawn_time_counter.set_read_only()
multiplayer_respawn_time_counter.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    _g_multiplayer_respawn_counter_overlay = -1
    _g_multiplayer_respawn_remained_overlay = -1
    var001 = 0
    if _g_multiplayer_message_type == 13 and _g_round_ended == 1 or _g_flag_is_not_ready == 1:
        var001 = 1
    #end
    if var001 == 0:
        _g_multiplayer_last_respawn_counter_value = -1
        str_clear(0)
        create_text_overlay(_g_multiplayer_respawn_counter_overlay,0,65552)
        overlay_set_color(_g_multiplayer_respawn_counter_overlay,16777215)
        position_set_x(1,500)
        position_set_y(1,600)
        overlay_set_position(_g_multiplayer_respawn_counter_overlay,1)
        position_set_x(1,2000)
        position_set_y(1,2000)
        overlay_set_size(_g_multiplayer_respawn_counter_overlay,1)
        str_clear(0)
        create_text_overlay(_g_multiplayer_respawn_remained_overlay,0,65552)
        overlay_set_color(_g_multiplayer_respawn_remained_overlay,16777215)
        position_set_x(1,500)
        position_set_y(1,570)
        overlay_set_position(_g_multiplayer_respawn_remained_overlay,1)
        position_set_x(1,1400)
        position_set_y(1,1400)
        overlay_set_size(_g_multiplayer_respawn_remained_overlay,1)
        presentation_set_duration(999999)
event.codeBlock = code
multiplayer_respawn_time_counter.add_event(event)
event = RunEvent()
def code():
    if _g_multiplayer_respawn_counter_overlay >= 0:
        my_player = multiplayer_get_my_player()
        if my_player >= 0:
            team_no_002 = player_get_team_no(my_player)
            m_timer_a_003 = store_mission_timer_a()
            var004 = m_timer_a_003 - _g_multiplayer_respawn_start_time
            if team_no_002 == 2:
                presentation_set_duration(0)
            elif _g_show_no_more_respawns_remained == 0:
                var005 = _g_multiplayer_respawn_period
                if _g_multiplayer_game_type == 6:
                    team_no_002 = player_get_team_no(my_player)
                    if team_no_002 == 0:
                        var005 += 27
                    #end
                #end
            else:
                var005 = 6
            #end
            var006 = var005 - var004
            if var006 <= 0:
                presentation_set_duration(0)
            elif _g_multiplayer_last_respawn_counter_value != var006:
                _g_multiplayer_last_respawn_counter_value = var006
                if _g_show_no_more_respawns_remained == 0:
                    reg0 = var006
                    s0 = str_store_string(gstr.respawning_in_reg0_seconds)
                    if _g_multiplayer_number_of_respawn_count > 0:
                        reg0 = _g_multiplayer_number_of_respawn_count - _g_my_spawn_count
                        my_player = multiplayer_get_my_player()
                        team_no_007 = player_get_team_no(my_player)
                        if team_no_007 == 0:
                            if reg0 > 1:
                                s1 = str_store_string(gstr.reg0_respawns_remained)
                            else:
                                s1 = str_store_string(gstr.this_is_your_last_respawn)
                            #end
                        #end
                    else:
                        str_clear(1)
                    #end
                elif _g_show_no_more_respawns_remained == 1:
                    s0 = str_store_string(gstr.no_more_respawns_remained_this_round)
                    str_clear(1)
                    s1 = str_store_string(gstr.wait_next_round)
                #end
                overlay_set_text(_g_multiplayer_respawn_counter_overlay,0)
                overlay_set_text(_g_multiplayer_respawn_remained_overlay,1)
            #end
        #end
    else:
        presentation_set_duration(0)
    #end
    if _g_multiplayer_message_type == 13 and _g_round_ended == 1 or _g_flag_is_not_ready == 1:
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_respawn_time_counter.add_event(event)


multiplayer_stats_chart = Presentation("multiplayer_stats_chart")
multiplayer_stats_chart.set_read_only()
multiplayer_stats_chart.set_manual_end_only()
event = LoadEvent()
def code():
    _g_multiplayer_game_type_list1 = [
    5,
    4,
    ]
    _g_multiplayer_game_type_list1 = [
    5,
    4,
    ]
    _g_multiplayer_game_type_list1 = [
    5,
    4,
    ]
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg0,mesh.mp_score_b)
    position_set_x(1,100)
    position_set_y(1,100)
    overlay_set_position(reg0,1)
    position_set_x(1,1000)
    position_set_y(1,1000)
    overlay_set_size(reg0,1)
    var001 = 0
    var002 = 0
    var003 = 0
    max_players = get_max_players()
    for player_id_005 in range(0, max_players):
        slot_no_006 = player_id_005 + 211
        if player_is_active(player_id_005):
            troop_set_slot(trp.multiplayer_data,slot_no_006,1)
            team_no_007 = player_get_team_no(player_id_005)
            if team_no_007 == 0:
                var001 += 1
            elif team_no_007 == 1:
                var002 += 1
            elif team_no_007 == 2:
                var003 += 1
            #end
        else:
            troop_set_slot(trp.multiplayer_data,slot_no_006,0)
        #end
    #end
    if _g_multiplayer_num_bots_team_1 > 0:
        var001 += 1
    #end
    if _g_multiplayer_num_bots_team_2 > 0:
        var002 += 1
    #end
    var008 = var001
    val_max(var008,var002)
    var008 += var003
    str_clear(0)
    create_text_overlay(_g_presentation_obj_stats_chart_container,0,131072)
    position_set_x(1,100)
    position_set_y(1,120)
    overlay_set_position(_g_presentation_obj_stats_chart_container,1)
    position_set_x(1,746)
    position_set_y(1,530)
    overlay_set_area_size(_g_presentation_obj_stats_chart_container,1)
    set_container_overlay(_g_presentation_obj_stats_chart_container)
    var009 = var008 * 20
    var009 += 100
    if var003 > 0:
        var009 += 70
    #end
    my_player = multiplayer_get_my_player()
    if var009 > 490:
        _g_stats_chart_update_period = 8
    else:
        _g_stats_chart_update_period = 1
    #end
    if _g_multiplayer_game_type == 5:
        get_headquarters_scores()
        var011 = reg0
        var012 = reg1
    #end
    for team_id_013 in range(0, 2):
        var014 = 0
        max_players = get_max_players()
        for player_id_005 in range(0, max_players):
            if player_is_active(player_id_005):
                team_no_015 = player_get_team_no(player_id_005)
                if team_no_015 == team_id_013:
                    var014 += 1
                #end
            #end
        #end
        reg0 = var014
        if var014 != 1:
            create_text_overlay(reg1,gstr.reg0_players,0)
        else:
            create_text_overlay(reg1,gstr.reg0_player,0)
        #end
        var016 = var009
        team_faction_017 = team_get_faction(team_id_013)
        s1 = str_store_faction_name(team_faction_017)
        create_text_overlay(reg0,1,0)
        if team_id_013 == 0:
            overlay_set_color(reg0,16711680)
            overlay_set_color(reg1,16711680)
        else:
            overlay_set_color(reg0,39423)
            overlay_set_color(reg1,39423)
        #end
        var018 = 373
        var019 = var018 * team_id_013
        var019 += 42
        var020 = var019 + 15
        position_set_x(3,var020)
        position_set_y(3,var016)
        var021 = var019 + 35
        position_set_x(1,var021)
        position_set_y(1,var016)
        copy_position(2,1)
        var022 = var016 - 10
        position_set_x(2,var021)
        position_set_y(2,var022)
        overlay_set_position(reg0,1)
        overlay_set_position(reg1,2)
        position_set_x(1,1000)
        position_set_y(1,1000)
        position_set_x(2,600)
        position_set_y(2,600)
        overlay_set_size(reg0,1)
        overlay_set_size(reg1,2)
        team_faction_023 = team_get_faction(0)
        team_faction_024 = team_get_faction(1)
        if team_faction_023 == team_faction_024 and team_id_013 == 1:
            create_mesh_overlay(reg0,mesh.ui_kingdom_shield_7)
        elif team_faction_017 == fac.kingdom_4:
            create_mesh_overlay(reg0,mesh.ui_kingdom_shield_1)
        elif team_faction_017 == fac.kingdom_2:
            create_mesh_overlay(reg0,mesh.ui_kingdom_shield_2)
        elif team_faction_017 == fac.kingdom_3:
            create_mesh_overlay(reg0,mesh.ui_kingdom_shield_3)
        elif team_faction_017 == fac.kingdom_5:
            create_mesh_overlay(reg0,mesh.ui_kingdom_shield_4)
        elif team_faction_017 == fac.kingdom_6:
            create_mesh_overlay(reg0,mesh.ui_kingdom_shield_5)
        elif team_faction_017 == fac.kingdom_1:
            create_mesh_overlay(reg0,mesh.ui_kingdom_shield_6)
        #end
        position_set_x(1,100)
        position_set_y(1,100)
        overlay_set_position(reg0,3)
        position_set_x(1,50)
        position_set_y(1,50)
        overlay_set_size(reg0,1)
        reg0 = team_get_score(team_id_013)
        create_text_overlay(reg0,gstr.score_reg0,8)
        overlay_set_color(reg0,16777215)
        var025 = var019 + 325
        var026 = var016 + 0
        position_set_x(1,var025)
        position_set_y(1,var026)
        overlay_set_position(reg0,1)
        position_set_x(1,1200)
        position_set_y(1,1200)
        overlay_set_size(reg0,1)
        if _g_multiplayer_game_type == 5:
            if team_id_013 == 0:
                reg0 = var011
            elif team_id_013 == 1:
                reg0 = var012
            #end
            create_text_overlay(reg0,gstr.flags_reg0,0)
            overlay_set_color(reg0,16777215)
            var025 = var019 + 258
            var026 = var016 + -10
            position_set_x(1,var025)
            position_set_y(1,var026)
            overlay_set_position(reg0,1)
            position_set_x(1,600)
            position_set_y(1,600)
            overlay_set_size(reg0,1)
        #end
        var016 -= 60
        create_text_overlay(reg0,gstr.player_name,0)
        overlay_set_color(reg0,16777215)
        position_set_x(1,var019)
        position_set_y(1,var016)
        overlay_set_position(reg0,1)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(reg0,1)
        if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
            create_text_overlay(reg0,gstr.score,0)
            overlay_set_color(reg0,16777215)
            var025 = var019 + 138
            position_set_x(1,var025)
            position_set_y(1,var016)
            overlay_set_position(reg0,1)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
        #end
        create_text_overlay(reg0,gstr.kills,16)
        overlay_set_color(reg0,16777215)
        var025 = var019 + 206
        position_set_x(1,var025)
        position_set_y(1,var016)
        overlay_set_position(reg0,1)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(reg0,1)
        create_text_overlay(reg0,gstr.deaths,16)
        overlay_set_color(reg0,16777215)
        var025 = var019 + 260
        position_set_x(1,var025)
        position_set_y(1,var016)
        overlay_set_position(reg0,1)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(reg0,1)
        create_text_overlay(reg0,gstr.ping,16)
        overlay_set_color(reg0,16777215)
        var025 = var019 + 308
        position_set_x(1,var025)
        position_set_y(1,var016)
        overlay_set_position(reg0,1)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(reg0,1)
        create_mesh_overlay(reg0,mesh.white_plane)
        overlay_set_color(reg0,16777215)
        overlay_set_alpha(reg0,208)
        var025 = var019 + 0
        position_set_x(1,var025)
        var026 = var016 + -10
        position_set_y(1,var026)
        overlay_set_position(reg0,1)
        position_set_x(1,16500)
        position_set_y(1,50)
        overlay_set_size(reg0,1)
        var016 -= 35
        var027 = max_players + 1
        for _ in range(0, var027):
            var029 = -30030
            player_id_030 = -1
            for player_id_005 in range(0, max_players):
                slot_no_006 = player_id_005 + 211
                if troop_slot_eq(trp.multiplayer_data,slot_no_006,1):
                    team_no_007 = player_get_team_no(player_id_005)
                    if team_no_007 == team_id_013:
                        if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
                            score_031 = player_get_score(player_id_005)
                        else:
                            score_031 = player_get_kill_count(player_id_005)
                        #end
                    #end
                #end
                death_count_032 = player_get_death_count(player_id_005)
                var033 = score_031 * 1000
                var033 -= death_count_032
                if var033 > var029 or var033 == -30030:
                    var029 = var033
                    player_id_030 = player_id_005
                #end
            #end
            if player_id_030 >= 0:
                slot_no_006 = player_id_030 + 211
                troop_set_slot(trp.multiplayer_data,slot_no_006,0)
                if my_player == player_id_030:
                    create_mesh_overlay(reg0,mesh.white_plane)
                    overlay_set_color(reg0,16777215)
                    overlay_set_alpha(reg0,53)
                    var025 = var019 + 0
                    position_set_x(1,var025)
                    var026 = var016 + 0
                    position_set_y(1,var026)
                    overlay_set_position(reg0,1)
                    position_set_x(1,16500)
                    position_set_y(1,1000)
                    overlay_set_size(reg0,1)
                #end
                if _g_multiplayer_game_type in _g_multiplayer_game_type_list1:
                    var034 = 16777215
                    agent_id_035 = player_get_agent_id(player_id_030)
                    if agent_id_035 >= 0 or not agent_is_alive(agent_id_035):
                        var034 = 16711680
                    #end
                    reg0 = player_get_score(player_id_030)
                    create_text_overlay(reg0,gstr.reg0,8)
                    overlay_set_color(reg0,var034)
                    position_set_x(1,750)
                    position_set_y(1,750)
                    overlay_set_size(reg0,1)
                    var025 = var019 + 165
                    position_set_x(1,var025)
                    position_set_y(1,var016)
                    overlay_set_position(reg0,1)
                else:
                    var034 = 16777215
                    agent_id_035 = player_get_agent_id(player_id_030)
                    if agent_id_035 >= 0 or not agent_is_alive(agent_id_035):
                        var034 = 16711680
                        create_text_overlay(reg0,gstr.dead,0)
                        overlay_set_color(reg0,var034)
                        position_set_x(1,750)
                        position_set_y(1,750)
                        overlay_set_size(reg0,1)
                        var025 = var019 + 130
                        position_set_x(1,var025)
                        position_set_y(1,var016)
                        overlay_set_position(reg0,1)
                    #end
                #end
                s1 = str_store_player_username(player_id_030)
                if _g_multiplayer_is_game_type_captain == 1:
                    create_text_overlay(reg0,gstr.s1_team,0)
                else:
                    create_text_overlay(reg0,1,0)
                #end
                overlay_set_color(reg0,var034)
                position_set_x(1,750)
                position_set_y(1,750)
                overlay_set_size(reg0,1)
                position_set_x(1,var019)
                position_set_y(1,var016)
                overlay_set_position(reg0,1)
                reg0 = player_get_kill_count(player_id_030)
                create_text_overlay(reg0,gstr.reg0,8)
                overlay_set_color(reg0,var034)
                position_set_x(1,750)
                position_set_y(1,750)
                overlay_set_size(reg0,1)
                var025 = var019 + 215
                position_set_x(1,var025)
                position_set_y(1,var016)
                overlay_set_position(reg0,1)
                reg0 = player_get_death_count(player_id_030)
                create_text_overlay(reg0,gstr.reg0,8)
                overlay_set_color(reg0,var034)
                position_set_x(1,750)
                position_set_y(1,750)
                overlay_set_size(reg0,1)
                var025 = var019 + 265
                position_set_x(1,var025)
                position_set_y(1,var016)
                overlay_set_position(reg0,1)
                reg0 = player_get_ping(player_id_030)
                create_text_overlay(reg0,gstr.reg0,8)
                overlay_set_color(reg0,var034)
                position_set_x(1,750)
                position_set_y(1,750)
                overlay_set_size(reg0,1)
                var025 = var019 + 315
                position_set_x(1,var025)
                position_set_y(1,var016)
                overlay_set_position(reg0,1)
                var016 -= 20
            else:
                if True:
                    if team_id_013 == 0:
                        var036 = _g_multiplayer_num_bots_team_1
                    else:
                        var036 = _g_multiplayer_num_bots_team_2
                    #end
                    reg0 = team_get_bot_kill_count(team_id_013)
                    reg1 = team_get_bot_death_count(team_id_013)
                    if reg0 == 0 or reg1 == 0 or var036 != 0:
                        var037 = 1
                    else:
                        var037 = 0
                    #end
                    if var037 == 1:
                        var038 = 0
                        for cur_agent in __all_agents__:
                            if agent_is_non_player(cur_agent) and agent_is_alive(cur_agent):
                                agent_team_no_040 = agent_get_team(cur_agent)
                                if agent_team_no_040 == team_id_013:
                                    var038 += 1
                                #end
                            #end
                        #end
                    #end
                    var041 = var036 - var038
                    if var038 == 0:
                        var034 = 16711680
                    else:
                        var034 = 13684944
                    #end
                    if var041 > 0:
                        if var036 == 1:
                            create_text_overlay(reg0,gstr.dead,0)
                            var025 = var019 + 130
                        else:
                            reg0 = var041
                            create_text_overlay(reg0,gstr.reg0_dead,0)
                            var025 = var019 + 123
                        #end
                        overlay_set_color(reg0,var034)
                        position_set_x(1,750)
                        position_set_y(1,750)
                        overlay_set_size(reg0,1)
                        position_set_x(1,var025)
                        position_set_y(1,var016)
                        overlay_set_position(reg0,1)
                    #end
                    if var036 > 1:
                        reg0 = var036
                        create_text_overlay(reg0,gstr.bots_reg0_agents,0)
                    else:
                        create_text_overlay(reg0,gstr.bot_1_agent,0)
                    #end
                    overlay_set_color(reg0,var034)
                    position_set_x(1,750)
                    position_set_y(1,750)
                    overlay_set_size(reg0,1)
                    position_set_x(1,var019)
                    position_set_y(1,var016)
                    overlay_set_position(reg0,1)
                    reg0 = team_get_bot_kill_count(team_id_013)
                    create_text_overlay(reg0,gstr.reg0,8)
                    overlay_set_color(reg0,var034)
                    position_set_x(1,750)
                    position_set_y(1,750)
                    overlay_set_size(reg0,1)
                    var025 = var019 + 215
                    position_set_x(1,var025)
                    position_set_y(1,var016)
                    overlay_set_position(reg0,1)
                    reg0 = team_get_bot_death_count(team_id_013)
                    create_text_overlay(reg0,gstr.reg0,8)
                    overlay_set_color(reg0,var034)
                    position_set_x(1,750)
                    position_set_y(1,750)
                    overlay_set_size(reg0,1)
                    var025 = var019 + 265
                    position_set_x(1,var025)
                    position_set_y(1,var016)
                    overlay_set_position(reg0,1)
                    var016 -= 20
                #end
                var027 = 0
            #end
        #end
        if team_id_013 == 0:
            var042 = var016
        #end
    #end
    if var042 <= var016:
        var016 = var042
    #end
    var019 = 42
    create_mesh_overlay(reg0,mesh.white_plane)
    overlay_set_color(reg0,16777215)
    overlay_set_alpha(reg0,208)
    var025 = var019 + 0
    position_set_x(1,var025)
    var026 = var016 + 10
    position_set_y(1,var026)
    overlay_set_position(reg0,1)
    position_set_x(1,36000)
    position_set_y(1,50)
    overlay_set_size(reg0,1)
    if var003 > 0:
        var019 = 280
        var016 -= 50
        create_text_overlay(reg0,gstr.spectators,0)
        overlay_set_color(reg0,16777215)
        position_set_x(1,var019)
        position_set_y(1,var016)
        overlay_set_position(reg0,1)
        position_set_x(1,1000)
        position_set_y(1,1000)
        overlay_set_size(reg0,1)
        create_text_overlay(reg0,gstr.ping,8)
        overlay_set_color(reg0,16777215)
        var025 = var019 + 215
        position_set_x(1,var025)
        position_set_y(1,var016)
        overlay_set_position(reg0,1)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(reg0,1)
        create_mesh_overlay(reg0,mesh.white_plane)
        overlay_set_color(reg0,16777215)
        overlay_set_alpha(reg0,208)
        var025 = var019 + 0
        position_set_x(1,var025)
        var026 = var016 + -10
        position_set_y(1,var026)
        overlay_set_position(reg0,1)
        position_set_x(1,12000)
        position_set_y(1,50)
        overlay_set_size(reg0,1)
        var016 -= 30
        var034 = 12632256
        var027 = max_players + 1
        for player_id_005 in range(0, var027):
            slot_no_006 = player_id_005 + 211
            if troop_slot_eq(trp.multiplayer_data,slot_no_006,1):
                team_no_007 = player_get_team_no(player_id_005)
                if team_no_007 == 2:
                    troop_set_slot(trp.multiplayer_data,slot_no_006,1)
                    if my_player == player_id_005:
                        create_mesh_overlay(reg0,mesh.white_plane)
                        overlay_set_color(reg0,16777215)
                        overlay_set_alpha(reg0,53)
                        var025 = var019 + 0
                        position_set_x(1,var025)
                        var026 = var016 + 0
                        position_set_y(1,var026)
                        overlay_set_position(reg0,1)
                        position_set_x(1,12000)
                        position_set_y(1,1000)
                        overlay_set_size(reg0,1)
                    #end
                #end
            #end
            s1 = str_store_player_username(player_id_005)
            create_text_overlay(reg0,1,0)
            overlay_set_color(reg0,var034)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            position_set_x(1,var019)
            position_set_y(1,var016)
            overlay_set_position(reg0,1)
            reg0 = player_get_ping(player_id_005)
            create_text_overlay(reg0,gstr.reg0,8)
            overlay_set_color(reg0,var034)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            var025 = var019 + 215
            position_set_x(1,var025)
            position_set_y(1,var016)
            overlay_set_position(reg0,1)
            var016 -= 20
        #end
    #end
    omit_key_once(238)
    omit_key_once(239)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_stats_chart.add_event(event)
event = RunEvent()
def code(var001):
    if key_clicked(238) or key_clicked(239):
        omit_key_once(238)
        omit_key_once(239)
    #end
    if _g_multiplayer_stats_chart_opened_manually == 1 and not game_key_is_down(18):
        _g_multiplayer_stats_chart_opened_manually = 0
        clear_omitted_keys()
        presentation_set_duration(0)
    #end
    if True:
        var002 = _g_stats_chart_update_period * 1000
        if var001 > var002:
            clear_omitted_keys()
            presentation_set_duration(0)
            start_presentation(prsnt.multiplayer_stats_chart)
        #end
    #end
event.codeBlock = code
multiplayer_stats_chart.add_event(event)


multiplayer_stats_chart_deathmatch = Presentation("multiplayer_stats_chart_deathmatch")
multiplayer_stats_chart_deathmatch.set_read_only()
multiplayer_stats_chart_deathmatch.set_manual_end_only()
event = LoadEvent()
def code():
    team_no_006_list1 = [
    1,
    0,
    ]
    team_no_006_list1 = [
    1,
    0,
    ]
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg0,mesh.mp_score_a)
    position_set_x(1,295)
    position_set_y(1,115)
    overlay_set_position(reg0,1)
    position_set_x(1,1000)
    position_set_y(1,1000)
    overlay_set_size(reg0,1)
    var001 = 0
    var002 = 0
    max_players = get_max_players()
    for player_id_004 in range(0, max_players):
        slot_no_005 = player_id_004 + 211
        if player_is_active(player_id_004):
            troop_set_slot(trp.multiplayer_data,slot_no_005,1)
            team_no_006 = player_get_team_no(player_id_004)
            if team_no_006 in team_no_006_list1:
                var001 += 1
            elif team_no_006 == 2:
                var002 += 1
            #end
        else:
            troop_set_slot(trp.multiplayer_data,slot_no_005,0)
        #end
    #end
    if _g_multiplayer_num_bots_team_1 > 0 or _g_multiplayer_num_bots_team_2 > 0:
        var001 += 1
    #end
    var007 = var001 + var002
    str_clear(0)
    create_text_overlay(_g_presentation_obj_stats_chart_deathmatch_container,0,131072)
    position_set_x(1,300)
    position_set_y(1,140)
    overlay_set_position(_g_presentation_obj_stats_chart_deathmatch_container,1)
    position_set_x(1,346)
    position_set_y(1,530)
    overlay_set_area_size(_g_presentation_obj_stats_chart_deathmatch_container,1)
    set_container_overlay(_g_presentation_obj_stats_chart_deathmatch_container)
    var008 = var007 * 20
    var008 += 80
    if var002 > 0:
        var008 += 70
    #end
    if var007 >= 17:
        _g_stats_chart_update_period = 10
    else:
        _g_stats_chart_update_period = 1
    #end
    my_player = multiplayer_get_my_player()
    var010 = var008
    var011 = 42
    if _g_multiplayer_game_type == 8:
        var012 = 0
        max_players = get_max_players()
        for player_id_004 in range(0, max_players):
            if player_is_active(player_id_004):
                team_no_013 = player_get_team_no(player_id_004)
                if team_no_013 == 0:
                    var012 = 1
                #end
            #end
        #end
        if var012 == 1:
            var011 = 40
            var010 -= 50
            create_text_overlay(reg0,gstr.wave_info,0)
            overlay_set_color(reg0,16777215)
            position_set_x(1,var011)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            position_set_x(1,850)
            position_set_y(1,850)
            overlay_set_size(reg0,1)
            var010 -= 22
            if _g_multiplayer_ccoop_wave_no > 0:
                var014 = 15790320
                reg1 = _g_multiplayer_ccoop_wave_no - _g_mp_coop_last_king_wave
                if _g_mp_coop_king_waves >= 1:
                    create_text_overlay(reg0,gstr.elite_wave_no_reg1,0)
                else:
                    create_text_overlay(reg0,gstr.wave_no_reg1,0)
                #end
            #end
            overlay_set_color(reg0,var014)
            position_set_x(1,var011)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            var010 -= 22
        #end
        multiplayer_ccoop_get_alive_enemy_count()
        var015 = reg0
        if _g_multiplayer_ccoop_enemy_respawn_secs <= 10000 and _g_multiplayer_ccoop_enemy_respawn_secs > 31 or var015 > 0 and _g_round_ended == 0:
            reg1 = _g_multiplayer_ccoop_enemy_respawn_secs
            if reg1 >= 60:
                reg2 = reg1 / 60
                reg1 %= 60
                create_text_overlay(reg0,gstr.time_left_reg2_mins_reg1_secs,0)
            else:
                create_text_overlay(reg0,gstr.time_left_reg1_secs,0)
            #end
            overlay_set_color(reg0,var014)
            position_set_x(1,var011)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            var010 -= 22
        #end
        var016 = 0
        troop_slot_017 = troop_get_slot(trp.multiplayer_data,186)
        for var018 in range(0, troop_slot_017):
            slot_no_019 = var018 * 3
            slot_no_019 += 188
            troop_slot_020 = troop_get_slot(trp.multiplayer_data,slot_no_019)
            var016 += troop_slot_020
        #end
        var021 = 0
        for var018 in range(0, troop_slot_017):
            slot_no_019 = var018 * 3
            slot_no_019 += 187
            troop_slot_022 = troop_get_slot(trp.multiplayer_data,slot_no_019)
            var023 = 0
            for var024 in range(0, var018):
                if var023 == 0:
                    slot_no_025 = var024 * 3
                    slot_no_025 += 187
                    troop_slot_026 = troop_get_slot(trp.multiplayer_data,slot_no_025)
                    if troop_slot_022 == troop_slot_026:
                        var023 = 1
                    #end
                #end
            #end
            if var023 == 0:
                slot_no_019 += 1
                troop_slot_020 = troop_get_slot(trp.multiplayer_data,slot_no_019)
                var027 = var018 + 1
                for var024 in range(var027, troop_slot_017):
                    slot_no_025 = var024 * 3
                    slot_no_025 += 187
                    troop_slot_026 = troop_get_slot(trp.multiplayer_data,slot_no_025)
                    if troop_slot_022 == troop_slot_026:
                        slot_no_025 += 1
                        troop_slot_028 = troop_get_slot(trp.multiplayer_data,slot_no_025)
                        troop_slot_020 += troop_slot_028
                    #end
                #end
                var029 = 0
                for cur_agent in __all_agents__:
                    if agent_is_human(cur_agent) and agent_is_alive(cur_agent):
                        agent_team_no_031 = agent_get_team(cur_agent)
                        if agent_team_no_031 == 1:
                            troop_id_032 = agent_get_troop_id(cur_agent)
                            if troop_id_032 == troop_slot_022:
                                var029 += 1
                            #end
                        #end
                    #end
                #end
                if troop_slot_020 > 0 or var029 > 0:
                    if var021 == 0:
                        var021 = 1
                        reg1 = var015
                        reg2 = var016
                        create_text_overlay(reg0,gstr.enemies_reg1_total_reg2_arriving,0)
                        overlay_set_color(reg0,var014)
                        position_set_x(1,var011)
                        position_set_y(1,var010)
                        overlay_set_position(reg0,1)
                        position_set_x(1,750)
                        position_set_y(1,750)
                        overlay_set_size(reg0,1)
                        var010 -= 20
                    #end
                    if var029 == 1 or is_between(troop_slot_022,trp.knight_1_1,trp.kingdom_1_pretender) or is_between(troop_slot_022,trp.kingdom_1_lord,trp.knight_1_1):
                        s0 = str_store_troop_name(troop_slot_022)
                    else:
                        s0 = str_store_troop_name_plural(troop_slot_022)
                    #end
                    reg3 = troop_slot_020
                    reg4 = var029
                    create_text_overlay(reg0,gstr.ccoop_enemy_info,0)
                    overlay_set_color(reg0,var014)
                    position_set_x(1,var011)
                    position_set_y(1,var010)
                    overlay_set_position(reg0,1)
                    position_set_x(1,750)
                    position_set_y(1,750)
                    overlay_set_size(reg0,1)
                    var010 -= 18
                #end
            #end
        #end
        var011 = 42
        create_mesh_overlay(reg0,mesh.white_plane)
        overlay_set_color(reg0,16777215)
        overlay_set_alpha(reg0,208)
        var033 = var011 + 0
        position_set_x(1,var033)
        var034 = var010 + 10
        position_set_y(1,var034)
        overlay_set_position(reg0,1)
        position_set_x(1,15250)
        position_set_y(1,50)
        overlay_set_size(reg0,1)
    #end
    var010 -= 13
    create_text_overlay(reg0,gstr.player_name,0)
    overlay_set_color(reg0,16777215)
    position_set_x(1,var011)
    position_set_y(1,var010)
    overlay_set_position(reg0,1)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg0,1)
    create_text_overlay(reg0,gstr.kills,16)
    overlay_set_color(reg0,16777215)
    var033 = var011 + 179
    position_set_x(1,var033)
    position_set_y(1,var010)
    overlay_set_position(reg0,1)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg0,1)
    create_text_overlay(reg0,gstr.deaths,16)
    overlay_set_color(reg0,16777215)
    var033 = var011 + 233
    position_set_x(1,var033)
    position_set_y(1,var010)
    overlay_set_position(reg0,1)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg0,1)
    create_text_overlay(reg0,gstr.ping,16)
    overlay_set_color(reg0,16777215)
    var033 = var011 + 282
    position_set_x(1,var033)
    position_set_y(1,var010)
    overlay_set_position(reg0,1)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg0,1)
    create_mesh_overlay(reg0,mesh.white_plane)
    overlay_set_color(reg0,16777215)
    overlay_set_alpha(reg0,208)
    var033 = var011 + 0
    position_set_x(1,var033)
    var034 = var010 + -10
    position_set_y(1,var034)
    overlay_set_position(reg0,1)
    position_set_x(1,15250)
    position_set_y(1,50)
    overlay_set_size(reg0,1)
    var010 -= 35
    var035 = max_players + 1
    for _ in range(0, var035):
        var037 = -30030
        player_id_038 = -1
        for player_id_004 in range(0, max_players):
            slot_no_005 = player_id_004 + 211
            if troop_slot_eq(trp.multiplayer_data,slot_no_005,1):
                team_no_006 = player_get_team_no(player_id_004)
                if team_no_006 in team_no_006_list1:
                    kill_count_039 = player_get_kill_count(player_id_004)
                    death_count_040 = player_get_death_count(player_id_004)
                    var041 = kill_count_039 * 1000
                    var041 -= death_count_040
                    if var041 > var037 or var041 == -30030:
                        var037 = var041
                        player_id_038 = player_id_004
                    #end
                #end
            #end
        #end
        var043 = _g_multiplayer_num_bots_team_1 + _g_multiplayer_num_bots_team_2
        if player_id_038 >= 0:
            slot_no_005 = player_id_038 + 211
            troop_set_slot(trp.multiplayer_data,slot_no_005,0)
            s1 = str_store_player_username(player_id_038)
            if my_player == player_id_038:
                create_mesh_overlay(reg0,mesh.white_plane)
                overlay_set_color(reg0,16777215)
                overlay_set_alpha(reg0,53)
                var033 = var011 + 0
                position_set_x(1,var033)
                var034 = var010 + 0
                position_set_y(1,var034)
                overlay_set_position(reg0,1)
                position_set_x(1,16000)
                position_set_y(1,1000)
                overlay_set_size(reg0,1)
            #end
            var014 = 16777215
            if _g_multiplayer_game_type == 8:
                agent_id_042 = player_get_agent_id(player_id_038)
                if agent_id_042 >= 0 or not agent_is_alive(agent_id_042):
                    var014 = 16711680
                    create_text_overlay(reg0,gstr.dead,0)
                    overlay_set_color(reg0,var014)
                    position_set_x(1,750)
                    position_set_y(1,750)
                    overlay_set_size(reg0,1)
                    var033 = var011 + 130
                    position_set_x(1,var033)
                    position_set_y(1,var010)
                    overlay_set_position(reg0,1)
                #end
            #end
            if _g_multiplayer_game_type == 8:
                create_text_overlay(reg0,gstr.s1_team,0)
            else:
                create_text_overlay(reg0,1,0)
            #end
            overlay_set_color(reg0,var014)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            position_set_x(1,var011)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            reg0 = player_get_kill_count(player_id_038)
            create_text_overlay(reg0,gstr.reg0,8)
            overlay_set_color(reg0,16777215)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            var033 = var011 + 188
            position_set_x(1,var033)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            reg0 = player_get_death_count(player_id_038)
            create_text_overlay(reg0,gstr.reg0,8)
            overlay_set_color(reg0,16777215)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            var033 = var011 + 238
            position_set_x(1,var033)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            reg0 = player_get_ping(player_id_038)
            create_text_overlay(reg0,gstr.reg0,8)
            overlay_set_color(reg0,16777215)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            var033 = var011 + 288
            position_set_x(1,var033)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            var010 -= 20
        elif var043 >= 1:
            if var043 > 1:
                reg0 = var043
                create_text_overlay(reg0,gstr.bots_reg0_agents,0)
            else:
                create_text_overlay(reg0,gstr.bot_1_agent,0)
            #end
            overlay_set_color(reg0,13684944)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            position_set_x(1,var011)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            reg0 = team_get_bot_kill_count(0)
            var044 = reg0
            reg0 = team_get_bot_kill_count(1)
            var044 += reg0
            reg0 = var044
            create_text_overlay(reg0,gstr.reg0,8)
            overlay_set_color(reg0,13684944)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            var033 = var011 + 188
            position_set_x(1,var033)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            reg0 = team_get_bot_death_count(0)
            var045 = reg0
            reg0 = team_get_bot_death_count(1)
            var045 += reg0
            reg0 = var045
            create_text_overlay(reg0,gstr.reg0,8)
            overlay_set_color(reg0,13684944)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            var033 = var011 + 238
            position_set_x(1,var033)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            var010 -= 20
            var035 = 0
        else:
            var035 = 0
        #end
    #end
    var011 = 42
    create_mesh_overlay(reg0,mesh.white_plane)
    overlay_set_color(reg0,16777215)
    overlay_set_alpha(reg0,208)
    var033 = var011 + 0
    position_set_x(1,var033)
    var034 = var010 + 10
    position_set_y(1,var034)
    overlay_set_position(reg0,1)
    position_set_x(1,15250)
    position_set_y(1,50)
    overlay_set_size(reg0,1)
    if var002 > 0:
        var011 = 75
        var010 -= 50
        create_text_overlay(reg0,gstr.spectators,0)
        overlay_set_color(reg0,16777215)
        position_set_x(1,var011)
        position_set_y(1,var010)
        overlay_set_position(reg0,1)
        position_set_x(1,1000)
        position_set_y(1,1000)
        overlay_set_size(reg0,1)
        create_text_overlay(reg0,gstr.ping,16)
        overlay_set_color(reg0,16777215)
        var033 = var011 + 218
        position_set_x(1,var033)
        position_set_y(1,var010)
        overlay_set_position(reg0,1)
        position_set_x(1,750)
        position_set_y(1,750)
        overlay_set_size(reg0,1)
        create_mesh_overlay(reg0,mesh.white_plane)
        overlay_set_color(reg0,16777215)
        overlay_set_alpha(reg0,208)
        var033 = var011 + 0
        position_set_x(1,var033)
        var034 = var010 + -10
        position_set_y(1,var034)
        overlay_set_position(reg0,1)
        position_set_x(1,12000)
        position_set_y(1,50)
        overlay_set_size(reg0,1)
        var010 -= 30
        var014 = 12632256
        var035 = max_players + 1
        for player_id_004 in range(0, var035):
            slot_no_005 = player_id_004 + 211
            if troop_slot_eq(trp.multiplayer_data,slot_no_005,1):
                team_no_006 = player_get_team_no(player_id_004)
                if team_no_006 == 2:
                    troop_set_slot(trp.multiplayer_data,slot_no_005,1)
                    if my_player == player_id_004:
                        create_mesh_overlay(reg0,mesh.white_plane)
                        overlay_set_color(reg0,16777215)
                        overlay_set_alpha(reg0,53)
                        var033 = var011 + 0
                        position_set_x(1,var033)
                        var034 = var010 + 0
                        position_set_y(1,var034)
                        overlay_set_position(reg0,1)
                        position_set_x(1,12000)
                        position_set_y(1,1000)
                        overlay_set_size(reg0,1)
                    #end
                #end
            #end
            s1 = str_store_player_username(player_id_004)
            create_text_overlay(reg0,1,0)
            overlay_set_color(reg0,var014)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            position_set_x(1,var011)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            reg0 = player_get_ping(player_id_004)
            create_text_overlay(reg0,gstr.reg0,8)
            overlay_set_color(reg0,var014)
            position_set_x(1,750)
            position_set_y(1,750)
            overlay_set_size(reg0,1)
            var033 = var011 + 215
            position_set_x(1,var033)
            position_set_y(1,var010)
            overlay_set_position(reg0,1)
            var010 -= 20
        #end
    #end
    omit_key_once(238)
    omit_key_once(239)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_stats_chart_deathmatch.add_event(event)
event = RunEvent()
def code(var001):
    if key_clicked(238) or key_clicked(239):
        omit_key_once(238)
        omit_key_once(239)
    #end
    if _g_multiplayer_stats_chart_opened_manually == 1 and not game_key_is_down(18):
        _g_multiplayer_stats_chart_opened_manually = 0
        clear_omitted_keys()
        presentation_set_duration(0)
    #end
    if True:
        var002 = _g_stats_chart_update_period * 1000
        if var001 > var002:
            clear_omitted_keys()
            presentation_set_duration(0)
            start_presentation(prsnt.multiplayer_stats_chart_deathmatch)
        #end
    #end
event.codeBlock = code
multiplayer_stats_chart_deathmatch.add_event(event)


multiplayer_escape_menu = Presentation("multiplayer_escape_menu")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg0,mesh.mp_ingame_menu)
    position_set_x(1,250)
    position_set_y(1,80)
    overlay_set_position(reg0,1)
    position_set_x(1,1000)
    position_set_y(1,1000)
    overlay_set_size(reg0,1)
    str_clear(0)
    create_text_overlay(_g_presentation_obj_escape_menu_container,0,131072)
    position_set_x(1,285)
    position_set_y(1,75)
    overlay_set_position(_g_presentation_obj_escape_menu_container,1)
    position_set_x(1,405)
    position_set_y(1,550)
    overlay_set_area_size(_g_presentation_obj_escape_menu_container,1)
    set_container_overlay(_g_presentation_obj_escape_menu_container)
    var001 = 500
    create_text_overlay(reg0,gstr.choose_an_option,0)
    overlay_set_color(reg0,16777215)
    position_set_x(1,0)
    position_set_y(1,var001)
    overlay_set_position(reg0,1)
    var001 -= 40
    create_button_overlay(_g_presentation_obj_escape_menu_1,gstr.choose_faction,0)
    overlay_set_color(_g_presentation_obj_escape_menu_1,16777215)
    my_team_no = multiplayer_get_my_team()
    _g_presentation_obj_escape_menu_2 = -1
    _g_presentation_obj_escape_menu_3 = -1
    _g_presentation_obj_escape_menu_6 = -1
    _g_presentation_obj_escape_menu_7 = -1
    _g_presentation_obj_escape_menu_8 = -1
    _g_presentation_obj_escape_menu_9 = -1
    _g_presentation_obj_escape_menu_10 = -1
    _g_presentation_obj_escape_menu_11 = -1
    _g_presentation_obj_escape_menu_12 = -1
    _g_presentation_obj_escape_menu_13 = -1
    if my_team_no < 2:
        create_button_overlay(_g_presentation_obj_escape_menu_2,gstr.choose_troop,0)
        overlay_set_color(_g_presentation_obj_escape_menu_2,16777215)
        my_troop_id = multiplayer_get_my_troop()
        if my_troop_id >= 0:
            create_button_overlay(_g_presentation_obj_escape_menu_3,gstr.choose_items,0)
            overlay_set_color(_g_presentation_obj_escape_menu_3,16777215)
        #end
    #end
    create_button_overlay(_g_presentation_obj_escape_menu_4,gstr.options,0)
    overlay_set_color(_g_presentation_obj_escape_menu_4,16777215)
    create_button_overlay(_g_presentation_obj_escape_menu_5,gstr.redefine_keys,0)
    overlay_set_color(_g_presentation_obj_escape_menu_5,16777215)
    create_button_overlay(_g_presentation_obj_escape_menu_13,"@Show game rules",0)
    overlay_set_color(_g_presentation_obj_escape_menu_13,16777215)
    my_player = multiplayer_get_my_player()
    if _g_multiplayer_maps_voteable == 1 or _g_multiplayer_factions_voteable == 1 or _g_multiplayer_num_bots_voteable > 0 or _g_multiplayer_kick_voteable == 1 or _g_multiplayer_ban_voteable == 1:
        create_button_overlay(_g_presentation_obj_escape_menu_6,gstr.submit_a_poll,0)
        overlay_set_color(_g_presentation_obj_escape_menu_6,16777215)
        _g_presentation_obj_escape_menu_6_available = 1
        if my_player >= 0:
            player_slot_005 = player_get_slot(my_player,26)
            m_timer_a_006 = store_mission_timer_a()
            if m_timer_a_006 < player_slot_005:
                overlay_set_color(_g_presentation_obj_escape_menu_6,8947848)
                overlay_set_hilight_color(_g_presentation_obj_escape_menu_6,8947848)
                _g_presentation_obj_escape_menu_6_available = 0
            #end
        #end
    #end
    if my_player >= 0 and player_is_admin(my_player):
        create_button_overlay(_g_presentation_obj_escape_menu_7,gstr.administrator_panel,0)
        overlay_set_color(_g_presentation_obj_escape_menu_7,16777215)
        create_button_overlay(_g_presentation_obj_escape_menu_8,gstr.kick_player,0)
        overlay_set_color(_g_presentation_obj_escape_menu_8,16777215)
        create_button_overlay(_g_presentation_obj_escape_menu_9,gstr.ban_player,0)
        overlay_set_color(_g_presentation_obj_escape_menu_9,16777215)
    #end
    create_button_overlay(_g_presentation_obj_escape_menu_11,gstr.mute_player,0)
    overlay_set_color(_g_presentation_obj_escape_menu_11,16777215)
    if True:
        _g_presentation_obj_escape_menu_12 = -1
        var007 = 0
        max_players = get_max_players()
        for player_id_009 in range(0, max_players):
            if player_is_active(player_id_009):
                is_muted_010 = player_get_is_muted(player_id_009)
                if is_muted_010 == 1:
                    var007 = 1
                #end
            #end
        #end
        if var007 == 1:
            create_button_overlay(_g_presentation_obj_escape_menu_12,gstr.unmute_player,0)
            overlay_set_color(_g_presentation_obj_escape_menu_12,16777215)
        #end
    #end
    create_button_overlay(_g_presentation_obj_escape_menu_10,gstr.quit,0)
    overlay_set_color(_g_presentation_obj_escape_menu_10,16777215)
    position_set_x(1,130)
    position_set_y(1,var001)
    overlay_set_position(_g_presentation_obj_escape_menu_1,1)
    if _g_presentation_obj_escape_menu_2 >= 0:
        var001 -= 40
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_escape_menu_2,1)
    #end
    if _g_presentation_obj_escape_menu_3 >= 0:
        var001 -= 40
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_escape_menu_3,1)
    #end
    var001 -= 40
    position_set_y(1,var001)
    overlay_set_position(_g_presentation_obj_escape_menu_4,1)
    var001 -= 40
    position_set_y(1,var001)
    overlay_set_position(_g_presentation_obj_escape_menu_5,1)
    var001 -= 40
    position_set_y(1,var001)
    overlay_set_position(_g_presentation_obj_escape_menu_13,1)
    if _g_presentation_obj_escape_menu_6 >= 0:
        var001 -= 40
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_escape_menu_6,1)
    #end
    if _g_presentation_obj_escape_menu_7 >= 0:
        var001 -= 40
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_escape_menu_7,1)
    #end
    if _g_presentation_obj_escape_menu_8 >= 0:
        var001 -= 40
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_escape_menu_8,1)
    #end
    if _g_presentation_obj_escape_menu_9 >= 0:
        var001 -= 40
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_escape_menu_9,1)
    #end
    var001 -= 40
    position_set_y(1,var001)
    overlay_set_position(_g_presentation_obj_escape_menu_11,1)
    if _g_presentation_obj_escape_menu_12 >= 0:
        var001 -= 40
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_escape_menu_12,1)
    #end
    var001 -= 40
    position_set_y(1,var001)
    overlay_set_position(_g_presentation_obj_escape_menu_10,1)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_escape_menu.add_event(event)
event = StateChangedEvent()
def code(var001):
    if var001 == _g_presentation_obj_escape_menu_1:
        presentation_set_duration(0)
        start_presentation(prsnt.multiplayer_team_select)
    elif var001 == _g_presentation_obj_escape_menu_2:
        presentation_set_duration(0)
        start_presentation(prsnt.multiplayer_troop_select)
    elif var001 == _g_presentation_obj_escape_menu_3:
        presentation_set_duration(0)
        _g_presentation_state = 0
        start_presentation(prsnt.multiplayer_item_select)
    elif var001 == _g_presentation_obj_escape_menu_4:
        presentation_set_duration(0)
        change_screen_options()
    elif var001 == _g_presentation_obj_escape_menu_5:
        presentation_set_duration(0)
        change_screen_controls()
    elif var001 == _g_presentation_obj_escape_menu_6 and _g_presentation_obj_escape_menu_6_available == 1:
        presentation_set_duration(0)
        start_presentation(prsnt.multiplayer_poll_menu)
    elif var001 == _g_presentation_obj_escape_menu_7:
        presentation_set_duration(0)
        multiplayer_send_message_to_server(18)
    elif var001 == _g_presentation_obj_escape_menu_8:
        presentation_set_duration(0)
        _g_multiplayer_players_list_action_type = 3
        start_presentation(prsnt.multiplayer_show_players_list)
    elif var001 == _g_presentation_obj_escape_menu_9:
        presentation_set_duration(0)
        _g_multiplayer_players_list_action_type = 4
        start_presentation(prsnt.multiplayer_show_players_list)
    elif var001 == _g_presentation_obj_escape_menu_10:
        presentation_set_duration(0)
        finish_mission(0)
    elif var001 == _g_presentation_obj_escape_menu_11:
        presentation_set_duration(0)
        _g_multiplayer_players_list_action_type = 5
        start_presentation(prsnt.multiplayer_show_players_list)
    elif var001 == _g_presentation_obj_escape_menu_12:
        presentation_set_duration(0)
        _g_multiplayer_players_list_action_type = 6
        start_presentation(prsnt.multiplayer_show_players_list)
    elif var001 == _g_presentation_obj_escape_menu_13:
        presentation_set_duration(0)
        multiplayer_send_message_to_server(45)
    #end
event.codeBlock = code
multiplayer_escape_menu.add_event(event)
event = RunEvent()
def code(var001):
    if key_clicked(1) or key_clicked(248) and var001 > 200:
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_escape_menu.add_event(event)


multiplayer_poll_menu = Presentation("multiplayer_poll_menu")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg0,mesh.mp_ingame_menu)
    position_set_x(1,250)
    position_set_y(1,80)
    overlay_set_position(reg0,1)
    position_set_x(1,1000)
    position_set_y(1,1000)
    overlay_set_size(reg0,1)
    str_clear(0)
    create_text_overlay(_g_presentation_obj_poll_menu_container,0,131072)
    position_set_x(1,285)
    position_set_y(1,125)
    overlay_set_position(_g_presentation_obj_poll_menu_container,1)
    position_set_x(1,405)
    position_set_y(1,500)
    overlay_set_area_size(_g_presentation_obj_poll_menu_container,1)
    set_container_overlay(_g_presentation_obj_poll_menu_container)
    _g_presentation_obj_poll_menu_1 = -1
    _g_presentation_obj_poll_menu_4 = -1
    _g_presentation_obj_poll_menu_5 = -1
    var001 = 450
    create_text_overlay(reg0,gstr.choose_a_poll_type,0)
    overlay_set_color(reg0,16777215)
    position_set_x(1,0)
    position_set_y(1,var001)
    overlay_set_position(reg0,1)
    var001 -= 40
    position_set_x(1,60)
    if _g_multiplayer_maps_voteable == 1:
        create_button_overlay(_g_presentation_obj_poll_menu_1,gstr.poll_for_changing_the_map,0)
        overlay_set_color(_g_presentation_obj_poll_menu_1,16777215)
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_poll_menu_1,1)
        var001 -= 40
    #end
    if _g_multiplayer_factions_voteable == 1:
        create_button_overlay(_g_presentation_obj_poll_menu_4,gstr.poll_for_changing_the_map_and_factions,0)
        overlay_set_color(_g_presentation_obj_poll_menu_4,16777215)
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_poll_menu_4,1)
        var001 -= 40
    #end
    if _g_multiplayer_num_bots_voteable > 0:
        create_button_overlay(_g_presentation_obj_poll_menu_5,gstr.poll_for_changing_number_of_bots,0)
        overlay_set_color(_g_presentation_obj_poll_menu_5,16777215)
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_poll_menu_5,1)
        var001 -= 40
    #end
    if _g_multiplayer_kick_voteable == 1:
        create_button_overlay(_g_presentation_obj_poll_menu_2,gstr.poll_for_kicking_a_player,0)
        overlay_set_color(_g_presentation_obj_poll_menu_2,16777215)
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_poll_menu_2,1)
        var001 -= 40
    #end
    if _g_multiplayer_ban_voteable == 1:
        create_button_overlay(_g_presentation_obj_poll_menu_3,gstr.poll_for_banning_a_player,0)
        overlay_set_color(_g_presentation_obj_poll_menu_3,16777215)
        position_set_y(1,var001)
        overlay_set_position(_g_presentation_obj_poll_menu_3,1)
    #end
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_poll_menu.add_event(event)
event = StateChangedEvent()
def code(var001):
    if var001 == _g_presentation_obj_poll_menu_1:
        presentation_set_duration(0)
        _g_multiplayer_maps_list_action_type = 1
        start_presentation(prsnt.multiplayer_show_maps_list)
    elif var001 == _g_presentation_obj_poll_menu_2:
        presentation_set_duration(0)
        _g_multiplayer_players_list_action_type = 1
        start_presentation(prsnt.multiplayer_show_players_list)
    elif var001 == _g_presentation_obj_poll_menu_3:
        presentation_set_duration(0)
        _g_multiplayer_players_list_action_type = 2
        start_presentation(prsnt.multiplayer_show_players_list)
    elif var001 == _g_presentation_obj_poll_menu_4:
        presentation_set_duration(0)
        _g_multiplayer_maps_list_action_type = 2
        start_presentation(prsnt.multiplayer_show_maps_list)
    elif var001 == _g_presentation_obj_poll_menu_5:
        presentation_set_duration(0)
        _g_multiplayer_number_of_bots_list_action_type = 1
        start_presentation(prsnt.multiplayer_show_number_of_bots_list)
    #end
event.codeBlock = code
multiplayer_poll_menu.add_event(event)
event = RunEvent()
def code(var001):
    if key_clicked(1) or key_clicked(248) and var001 > 200:
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_poll_menu.add_event(event)


multiplayer_show_players_list = Presentation("multiplayer_show_players_list")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg0,mesh.mp_ingame_menu)
    position_set_x(1,250)
    position_set_y(1,80)
    overlay_set_position(reg0,1)
    position_set_x(1,1000)
    position_set_y(1,1000)
    overlay_set_size(reg0,1)
    str_clear(0)
    create_text_overlay(_g_presentation_obj_show_players_1,0,131072)
    position_set_x(1,285)
    position_set_y(1,125)
    overlay_set_position(_g_presentation_obj_show_players_1,1)
    position_set_x(1,405)
    position_set_y(1,500)
    overlay_set_area_size(_g_presentation_obj_show_players_1,1)
    set_container_overlay(_g_presentation_obj_show_players_1)
    my_player = multiplayer_get_my_player()
    var002 = 10
    max_players = get_max_players()
    for player_id_004 in range(1, max_players):
        if player_is_active(player_id_004):
            var005 = 0
            if _g_multiplayer_players_list_action_type != 5 and _g_multiplayer_players_list_action_type != 6:
                var005 = 1
            elif _g_multiplayer_players_list_action_type == 5 and player_id_004 != my_player:
                is_muted_006 = player_get_is_muted(player_id_004)
                if is_muted_006 == 0:
                    var005 = 1
                elif _g_multiplayer_players_list_action_type == 6 and player_id_004 != my_player:
                    is_muted_006 = player_get_is_muted(player_id_004)
                    if is_muted_006 == 1:
                        var005 = 1
                    #end
                #end
            #end
        #end
        if var005 == 1:
            var002 += 40
        #end
    #end
    create_text_overlay(reg0,gstr.choose_a_player,0)
    overlay_set_color(reg0,16777215)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    var002 -= 40
    max_players = get_max_players()
    for player_id_004 in range(1, max_players):
        if player_is_active(player_id_004):
            player_set_slot(player_id_004,22,-1)
            var005 = 0
            if _g_multiplayer_players_list_action_type != 5 and _g_multiplayer_players_list_action_type != 6:
                var005 = 1
            elif _g_multiplayer_players_list_action_type == 5 and player_id_004 != my_player:
                is_muted_006 = player_get_is_muted(player_id_004)
                if is_muted_006 == 0:
                    var005 = 1
                elif _g_multiplayer_players_list_action_type == 6 and player_id_004 != my_player:
                    is_muted_006 = player_get_is_muted(player_id_004)
                    if is_muted_006 == 1:
                        var005 = 1
                    #end
                #end
            #end
        #end
        if var005 == 1:
            s0 = str_store_player_username(player_id_004)
            create_button_overlay(button_overlay_007,0,0)
            overlay_set_color(button_overlay_007,16777215)
            position_set_x(1,130)
            position_set_y(1,var002)
            overlay_set_position(button_overlay_007,1)
            var002 -= 40
            player_set_slot(player_id_004,22,button_overlay_007)
        #end
    #end
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_show_players_list.add_event(event)
event = StateChangedEvent()
def code(var001):
    max_players = get_max_players()
    for player_id_003 in range(1, max_players):
        if player_is_active(player_id_003) and player_slot_eq(player_id_003,22,var001):
            if is_between(_g_multiplayer_players_list_action_type,1,3):
                if True:
                    my_player = multiplayer_get_my_player()
                    if my_player >= 0:
                        multiplayer_send_2_int_to_server(21,_g_multiplayer_players_list_action_type,player_id_003)
                        m_timer_a_005 = store_mission_timer_a()
                        m_timer_a_005 += 900
                        player_set_slot(my_player,26,m_timer_a_005)
                    #end
                #end
            #end
        elif _g_multiplayer_players_list_action_type == 3:
            multiplayer_send_int_to_server(23,player_id_003)
        elif _g_multiplayer_players_list_action_type == 4:
            multiplayer_send_int_to_server(24,player_id_003)
        elif _g_multiplayer_players_list_action_type == 5:
            player_set_is_muted(player_id_003,1)
        elif _g_multiplayer_players_list_action_type == 6:
            player_set_is_muted(player_id_003,0)
        #end
        max_players = 0
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_show_players_list.add_event(event)
event = RunEvent()
def code(var001):
    if key_clicked(1) or key_clicked(248) and var001 > 200:
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_show_players_list.add_event(event)


multiplayer_show_maps_list = Presentation("multiplayer_show_maps_list")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg0,mesh.mp_ingame_menu)
    position_set_x(1,250)
    position_set_y(1,80)
    overlay_set_position(reg0,1)
    position_set_x(1,1000)
    position_set_y(1,1000)
    overlay_set_size(reg0,1)
    str_clear(0)
    create_text_overlay(_g_presentation_obj_show_maps_list_menu_container,0,131072)
    position_set_x(1,285)
    position_set_y(1,125)
    overlay_set_position(_g_presentation_obj_show_maps_list_menu_container,1)
    position_set_x(1,405)
    position_set_y(1,500)
    overlay_set_area_size(_g_presentation_obj_show_maps_list_menu_container,1)
    set_container_overlay(_g_presentation_obj_show_maps_list_menu_container)
    multiplayer_fill_map_game_types(_g_multiplayer_game_type)
    var001 = reg0
    var002 = var001 * 40
    var002 += 10
    create_text_overlay(reg0,gstr.choose_a_map,0)
    overlay_set_color(reg0,16777215)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    var002 -= 40
    button_overlay_003 = -1
    for var004 in range(0, var001):
        slot_no_005 = var004 + 0
        troop_slot_006 = troop_get_slot(trp.multiplayer_data,slot_no_005)
        var007 = troop_slot_006 - scn.multi_scene_1
        var007 = var007 + gstr.multi_scene_1
        s0 = str_store_string(var007)
        create_button_overlay(button_overlay_003,0,0)
        overlay_set_color(button_overlay_003,16777215)
        position_set_x(1,100)
        position_set_y(1,var002)
        overlay_set_position(button_overlay_003,1)
        var002 -= 40
    #end
    _g_show_maps_list_button_list_end_index = button_overlay_003 + 1
    _g_show_maps_list_button_list_first_index = _g_show_maps_list_button_list_end_index - var001
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_show_maps_list.add_event(event)
event = StateChangedEvent()
def code(var001):
    for var002 in range(_g_show_maps_list_button_list_first_index, _g_show_maps_list_button_list_end_index):
        if var001 == var002:
            multiplayer_fill_map_game_types(_g_multiplayer_game_type)
            slot_no_003 = var001 - _g_show_maps_list_button_list_first_index
            slot_no_003 += 0
            troop_slot_004 = troop_get_slot(trp.multiplayer_data,slot_no_003)
            presentation_set_duration(0)
            if _g_multiplayer_maps_list_action_type == 1:
                if True:
                    my_player = multiplayer_get_my_player()
                    if my_player >= 0:
                        multiplayer_send_2_int_to_server(21,0,troop_slot_004)
                        m_timer_a_006 = store_mission_timer_a()
                        m_timer_a_006 += 900
                        player_set_slot(my_player,26,m_timer_a_006)
                    #end
                #end
            #end
        else:
            _g_multiplayer_factions_list_action_type = 1
            _g_multiplayer_poll_for_map_and_faction_data_map = troop_slot_004
            start_presentation(prsnt.multiplayer_show_factions_list)
        #end
        _g_show_maps_list_button_list_end_index = 0
    #end
event.codeBlock = code
multiplayer_show_maps_list.add_event(event)
event = RunEvent()
def code(var001):
    if key_clicked(1) or key_clicked(248) and var001 > 200:
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_show_maps_list.add_event(event)


multiplayer_show_factions_list = Presentation("multiplayer_show_factions_list")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg0,mesh.mp_ingame_menu)
    position_set_x(1,250)
    position_set_y(1,80)
    overlay_set_position(reg0,1)
    position_set_x(1,1000)
    position_set_y(1,1000)
    overlay_set_size(reg0,1)
    str_clear(0)
    create_text_overlay(_g_presentation_obj_show_factions_list_menu_container,0,131072)
    position_set_x(1,285)
    position_set_y(1,125)
    overlay_set_position(_g_presentation_obj_show_factions_list_menu_container,1)
    position_set_x(1,405)
    position_set_y(1,500)
    overlay_set_area_size(_g_presentation_obj_show_factions_list_menu_container,1)
    set_container_overlay(_g_presentation_obj_show_factions_list_menu_container)
    var001 = fac.kingdoms_end
    var001 = var001 - fac.kingdom_1
    if _g_multiplayer_factions_list_action_type == 2:
        var001 -= 1
    #end
    var002 = var001 * 40
    var002 += 10
    reg0 = _g_multiplayer_factions_list_action_type
    create_text_overlay(reg0,gstr.choose_a_faction_for_team_reg0,0)
    overlay_set_color(reg0,16777215)
    position_set_x(1,0)
    position_set_y(1,var002)
    overlay_set_position(reg0,1)
    var002 -= 40
    button_overlay_003 = -1
    for fac_004 in range(fac.kingdom_1, fac.kingdoms_end):
        if _g_multiplayer_factions_list_action_type == 1 or _g_multiplayer_poll_for_map_and_faction_data_faction_1 != fac_004:
            s0 = str_store_faction_name(fac_004)
            create_button_overlay(button_overlay_003,0,0)
            overlay_set_color(button_overlay_003,16777215)
            position_set_x(1,100)
            position_set_y(1,var002)
            overlay_set_position(button_overlay_003,1)
            var002 -= 40
        #end
    #end
    _g_show_factions_list_button_list_end_index = button_overlay_003 + 1
    _g_show_factions_list_button_list_first_index = _g_show_factions_list_button_list_end_index - var001
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_show_factions_list.add_event(event)
event = StateChangedEvent()
def code(var001):
    for var002 in range(_g_show_factions_list_button_list_first_index, _g_show_factions_list_button_list_end_index):
        if var001 == var002:
            var003 = var001 - _g_show_factions_list_button_list_first_index
            var003 = var003 + fac.kingdom_1
            presentation_set_duration(0)
            if _g_multiplayer_factions_list_action_type == 2:
                if var003 >= _g_multiplayer_poll_for_map_and_faction_data_faction_1:
                    var003 += 1
                #end
            #end
            if True:
                my_player = multiplayer_get_my_player()
                if my_player >= 0:
                    multiplayer_send_4_int_to_server(21,3,_g_multiplayer_poll_for_map_and_faction_data_map,_g_multiplayer_poll_for_map_and_faction_data_faction_1,var003)
                    m_timer_a_005 = store_mission_timer_a()
                    m_timer_a_005 += 900
                    player_set_slot(my_player,26,m_timer_a_005)
                #end
            #end
        else:
            _g_multiplayer_factions_list_action_type = 2
            _g_multiplayer_poll_for_map_and_faction_data_faction_1 = var003
            start_presentation(prsnt.multiplayer_show_factions_list)
        #end
        _g_show_factions_list_button_list_end_index = 0
    #end
event.codeBlock = code
multiplayer_show_factions_list.add_event(event)
event = RunEvent()
def code(var001):
    if key_clicked(1) or key_clicked(248) and var001 > 200:
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_show_factions_list.add_event(event)


multiplayer_show_number_of_bots_list = Presentation("multiplayer_show_number_of_bots_list")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg0,mesh.mp_ingame_menu)
    position_set_x(1,250)
    position_set_y(1,80)
    overlay_set_position(reg0,1)
    position_set_x(1,1000)
    position_set_y(1,1000)
    overlay_set_size(reg0,1)
    str_clear(0)
    create_text_overlay(_g_presentation_obj_show_number_of_bots_list_menu_container,0,131072)
    position_set_x(1,285)
    position_set_y(1,125)
    overlay_set_position(_g_presentation_obj_show_number_of_bots_list_menu_container,1)
    position_set_x(1,405)
    position_set_y(1,500)
    overlay_set_area_size(_g_presentation_obj_show_number_of_bots_list_menu_container,1)
    set_container_overlay(_g_presentation_obj_show_number_of_bots_list_menu_container)
    var001 = 0
    var002 = _g_multiplayer_num_bots_voteable + 1
    for var003 in range(0, var002):
        var004 = var003
        var004 %= 5
        if var003 >= 10 or var004 == 0:
            var001 += 1
        #end
    #end
    var005 = var001 * 40
    var005 += 10
    reg0 = _g_multiplayer_number_of_bots_list_action_type
    create_text_overlay(reg0,gstr.choose_number_of_bots_for_team_reg0,0)
    overlay_set_color(reg0,16777215)
    position_set_x(1,0)
    position_set_y(1,var005)
    overlay_set_position(reg0,1)
    var005 -= 40
    button_overlay_006 = -1
    for var003 in range(0, var002):
        var004 = var003
        var004 %= 5
        if var003 >= 10 or var004 == 0:
            reg0 = var003
            s0 = str_store_string(gstr.reg0)
            create_button_overlay(button_overlay_006,0,0)
            overlay_set_color(button_overlay_006,16777215)
            position_set_x(1,100)
            position_set_y(1,var005)
            overlay_set_position(button_overlay_006,1)
            var005 -= 40
        #end
    #end
    _g_show_number_of_bots_list_button_list_end_index = button_overlay_006 + 1
    _g_show_number_of_bots_list_button_list_first_index = _g_show_number_of_bots_list_button_list_end_index - var001
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_show_number_of_bots_list.add_event(event)
event = StateChangedEvent()
def code(var001):
    for var002 in range(_g_show_number_of_bots_list_button_list_first_index, _g_show_number_of_bots_list_button_list_end_index):
        if var001 == var002:
            var003 = var001 - _g_show_number_of_bots_list_button_list_first_index
            if var003 < 10:
                var004 = var003
            else:
                var004 = var003 - 8
                var004 *= 5
            #end
        #end
        presentation_set_duration(0)
        if _g_multiplayer_number_of_bots_list_action_type == 2:
            if True:
                my_player = multiplayer_get_my_player()
                if my_player >= 0:
                    multiplayer_send_3_int_to_server(21,4,_g_multiplayer_poll_number_of_bots_team_1,var004)
                    m_timer_a_006 = store_mission_timer_a()
                    m_timer_a_006 += 900
                    player_set_slot(my_player,26,m_timer_a_006)
                #end
            #end
        else:
            _g_multiplayer_number_of_bots_list_action_type = 2
            _g_multiplayer_poll_number_of_bots_team_1 = var004
            start_presentation(prsnt.multiplayer_show_number_of_bots_list)
        #end
        _g_show_number_of_bots_list_button_list_end_index = 0
    #end
event.codeBlock = code
multiplayer_show_number_of_bots_list.add_event(event)
event = RunEvent()
def code(var001):
    if key_clicked(1) or key_clicked(248) and var001 > 200:
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_show_number_of_bots_list.add_event(event)


multiplayer_poll = Presentation("multiplayer_poll")
multiplayer_poll.set_read_only()
multiplayer_poll.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg0,mesh.white_plane)
    overlay_set_color(reg0,0)
    overlay_set_alpha(reg0,68)
    position_set_x(1,50)
    position_set_y(1,50)
    overlay_set_position(reg0,1)
    position_set_x(1,37500)
    position_set_y(1,4500)
    overlay_set_size(reg0,1)
    if _g_multiplayer_poll_to_show == 0:
        var001 = _g_multiplayer_poll_value_to_show - scn.multi_scene_1
        var001 = var001 + gstr.multi_scene_1
        s0 = str_store_string(var001)
        create_text_overlay(reg0,gstr.poll_change_map,16)
    elif _g_multiplayer_poll_to_show == 1:
        s0 = str_store_player_username(_g_multiplayer_poll_value_to_show)
        create_text_overlay(reg0,gstr.poll_kick_player,16)
    elif _g_multiplayer_poll_to_show == 2:
        s0 = str_store_player_username(_g_multiplayer_poll_value_to_show)
        create_text_overlay(reg0,gstr.poll_ban_player,16)
    elif _g_multiplayer_poll_to_show == 3:
        var001 = _g_multiplayer_poll_value_to_show - scn.multi_scene_1
        var001 = var001 + gstr.multi_scene_1
        s0 = str_store_string(var001)
        s1 = str_store_faction_name(_g_multiplayer_poll_value_2_to_show)
        s2 = str_store_faction_name(_g_multiplayer_poll_value_3_to_show)
        create_text_overlay(reg0,gstr.poll_change_map_with_faction,131088)
    else:
        reg0 = _g_multiplayer_poll_value_to_show
        reg1 = _g_multiplayer_poll_value_2_to_show
        s0 = str_store_faction_name(_g_multiplayer_team_1_faction)
        s1 = str_store_faction_name(_g_multiplayer_team_2_faction)
        create_text_overlay(reg0,gstr.poll_change_number_of_bots,131088)
    #end
    overlay_set_color(reg0,16777215)
    if _g_multiplayer_poll_to_show != 3 and _g_multiplayer_poll_to_show != 4:
        position_set_x(1,400)
        position_set_y(1,100)
        overlay_set_position(reg0,1)
    else:
        position_set_x(1,50)
        position_set_y(1,70)
        overlay_set_position(reg0,1)
        position_set_x(1,750)
        position_set_y(1,60)
        overlay_set_area_size(reg0,1)
    #end
    m_timer_a_002 = store_mission_timer_a()
    _g_multiplayer_poll_last_written_seconds_left = _g_multiplayer_poll_client_end_time - m_timer_a_002
    reg0 = _g_multiplayer_poll_last_written_seconds_left
    create_text_overlay(_g_presentation_obj_poll_1,gstr.poll_time_left,32776)
    overlay_set_color(_g_presentation_obj_poll_1,16777215)
    position_set_x(1,790)
    position_set_y(1,60)
    overlay_set_position(_g_presentation_obj_poll_1,1)
    omit_key_once(2)
    omit_key_once(3)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_poll.add_event(event)
event = RunEvent()
def code(var001):
    if key_clicked(1) or key_clicked(248) or key_clicked(3) and var001 > 500:
        multiplayer_send_int_to_server(22,0)
        clear_omitted_keys()
        presentation_set_duration(0)
    elif key_clicked(2) and var001 > 500:
        multiplayer_send_int_to_server(22,1)
        clear_omitted_keys()
        presentation_set_duration(0)
    #end
    m_timer_a_002 = store_mission_timer_a()
    var003 = _g_multiplayer_poll_client_end_time - m_timer_a_002
    if var003 != _g_multiplayer_poll_last_written_seconds_left:
        if var003 < 0:
            clear_omitted_keys()
            presentation_set_duration(0)
        else:
            _g_multiplayer_poll_last_written_seconds_left = var003
            reg0 = _g_multiplayer_poll_last_written_seconds_left
            overlay_set_text(_g_presentation_obj_poll_1,gstr.poll_time_left)
        #end
    #end
event.codeBlock = code
multiplayer_poll.add_event(event)


tutorial_show_mouse_movement = Presentation("tutorial_show_mouse_movement")
tutorial_show_mouse_movement.set_read_only()
tutorial_show_mouse_movement.set_manual_end_only()
event = LoadEvent()
def code():
    if _g_tutorial_mouse_dir == -1 or _g_tutorial_mouse_click == -1:
        presentation_set_duration(0)
    else:
        set_fixed_point_multiplier(1000)
        _g_tutorial_displayed_mouse_dir = _g_tutorial_mouse_dir
        _g_tutorial_displayed_mouse_click = _g_tutorial_mouse_click
        var001 = _g_tutorial_mouse_dir + mesh.mouse_arrow_down
        create_mesh_overlay(reg0,var001)
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(reg0,1)
        position_set_x(1,380)
        position_set_y(1,500)
        overlay_set_position(reg0,1)
        if _g_tutorial_mouse_click == 0:
            create_mesh_overlay(reg0,mesh.mouse_left_click)
        else:
            create_mesh_overlay(reg0,mesh.mouse_right_click)
        #end
        position_set_x(1,800)
        position_set_y(1,800)
        overlay_set_size(reg0,1)
        position_set_x(1,540)
        position_set_y(1,500)
        overlay_set_position(reg0,1)
        create_mesh_overlay(reg0,mesh.mouse_arrow_plus)
        overlay_set_color(reg0,16777215)
        position_set_x(1,600)
        position_set_y(1,600)
        overlay_set_size(reg0,1)
        position_set_x(1,470)
        position_set_y(1,510)
        overlay_set_position(reg0,1)
        presentation_set_duration(999999)
    #end
event.codeBlock = code
tutorial_show_mouse_movement.add_event(event)
event = RunEvent()
def code():
    if _g_tutorial_displayed_mouse_dir == _g_tutorial_mouse_dir or _g_tutorial_displayed_mouse_click != _g_tutorial_mouse_click:
        presentation_set_duration(0)
        if _g_tutorial_mouse_dir >= 0 and _g_tutorial_mouse_click >= 0:
            start_presentation(prsnt.tutorial_show_mouse_movement)
        #end
    #end
event.codeBlock = code
tutorial_show_mouse_movement.add_event(event)


name_kingdom = Presentation("name_kingdom", mesh=mesh.load_window)
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    s1 = str_store_string(gstr.name_kingdom_text)
    create_text_overlay(reg1,1,16)
    position_set_x(1,500)
    position_set_y(1,500)
    overlay_set_position(reg1,1)
    overlay_set_text(reg1,1)
    create_simple_text_box_overlay(_g_presentation_obj_name_kingdom_1)
    position_set_x(1,400)
    position_set_y(1,400)
    overlay_set_position(_g_presentation_obj_name_kingdom_1,1)
    if _players_kingdom_name_set == 1:
        s7 = str_store_faction_name(fac.player_supporters_faction)
        overlay_set_text(_g_presentation_obj_name_kingdom_1,7)
    else:
        s0 = str_store_troop_name(trp.player)
        overlay_set_text(_g_presentation_obj_name_kingdom_1,gstr.default_kingdom_name)
        s7 = str_store_string(gstr.default_kingdom_name)
    #end
    create_button_overlay(_g_presentation_obj_name_kingdom_2,"@Continue...",16)
    position_set_x(1,500)
    position_set_y(1,300)
    overlay_set_position(_g_presentation_obj_name_kingdom_2,1)
    presentation_set_duration(999999)
event.codeBlock = code
name_kingdom.add_event(event)
event = StateChangedEvent()
def code(var001):
    if var001 == _g_presentation_obj_name_kingdom_1:
        s7 = str_store_string(0)
    elif var001 == _g_presentation_obj_name_kingdom_2:
        faction_set_name(fac.player_supporters_faction,7)
        faction_set_color(fac.player_supporters_faction,16711680)
        _players_kingdom_name_set = 1
        presentation_set_duration(0)
    #end
event.codeBlock = code
name_kingdom.add_event(event)


banner_selection = Presentation("banner_selection", mesh=mesh.load_window)
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    s1 = str_store_string(gstr.banner_selection_text)
    create_text_overlay(reg1,1,16)
    position_set_x(1,500)
    position_set_y(1,600)
    overlay_set_position(reg1,1)
    overlay_set_text(reg1,1)
    create_button_overlay(_g_presentation_obj_banner_selection_1,"@Next Page",16)
    position_set_x(1,500)
    position_set_y(1,50)
    overlay_set_position(_g_presentation_obj_banner_selection_1,1)
    var001 = 150
    var002 = 575
    var003 = mesh.banner_f21
    var004 = fac.kingdoms_end
    var004 = var004 - fac.kingdom_1
    var003 -= var004
    var005 = 16 * _g_presentation_page_no
    var005 = var005 + mesh.banner_a01
    var006 = var005 + 16
    val_min(var003,var006)
    _g_presentation_banner_start = _g_presentation_obj_banner_selection_1 + 1
    for var007 in range(var005, var003):
        create_image_button_overlay(reg1,var007,var007)
        position_set_x(1,var001)
        position_set_y(1,var002)
        overlay_set_position(reg1,1)
        position_set_x(1,100)
        position_set_y(1,100)
        overlay_set_size(reg1,1)
        var001 += 100
        if var001 >= 900:
            var001 = 150
            var002 -= 250
        #end
    #end
    presentation_set_duration(999999)
event.codeBlock = code
banner_selection.add_event(event)
event = StateChangedEvent()
def code(var001):
    if var001 == _g_presentation_obj_banner_selection_1:
        _g_presentation_page_no += 1
        _g_presentation_page_no %= 8
        start_presentation(prsnt.banner_selection)
    else:
        var002 = var001 - _g_presentation_banner_start
        var003 = 16 * _g_presentation_page_no
        var002 += var003
        var004 = var002 + 1297036692682702894
        party_set_banner_icon(p.main_party,var004)
        var005 = var002 + spr.banner_a
        troop_set_slot(trp.player,13,var005)
        presentation_set_duration(0)
        var006 = 0
        var007 = trp.knight_1_1_wife
        for troop_id_008 in range(trp.npc1, var007):
            if troop_slot_eq(troop_id_008,13,var005):
                var006 = troop_id_008
                var007 = 0
                troop_set_slot(troop_id_008,13,spr.banner_f21)
                troop_slot_009 = troop_get_slot(troop_id_008,10)
                if troop_slot_009 > 0:
                    party_set_banner_icon(troop_slot_009,1297036692682703035)
                #end
            #end
        #end
        for p_010 in range(p.town_1, p.village_1):
            if party_slot_eq(p_010,7,trp.player):
                party_set_banner_icon(p_010,var004)
            elif party_slot_eq(p_010,7,var006):
                party_set_banner_icon(p_010,1297036692682703035)
            #end
        #end
    #end
event.codeBlock = code
banner_selection.add_event(event)
event = RunEvent()
def code():
    if key_clicked(57) or key_clicked(28) or key_clicked(1) or key_clicked(14) or key_clicked(252) or key_clicked(253):
        presentation_set_duration(0)
    #end
event.codeBlock = code
banner_selection.add_event(event)


custom_banner = Presentation("custom_banner", mesh=mesh.load_window)
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    troop_slot_001 = troop_get_slot(trp.player,96)
    val_max(troop_slot_001,0)
    troop_slot_001 = troop_slot_001 + mesh.custom_banner_01
    troop_slot_002 = troop_get_slot(trp.player,99)
    val_max(troop_slot_002,0)
    troop_slot_002 = troop_slot_002 + mesh.custom_map_banner_01
    troop_slot_003 = troop_get_slot(trp.player,85)
    troop_slot_004 = troop_get_slot(trp.player,86)
    create_text_overlay(reg1,gstr.color_no_1,0)
    position_set_x(1,40)
    position_set_y(1,550)
    overlay_set_position(reg1,1)
    create_text_overlay(reg1,gstr.color_no_2,0)
    position_set_x(1,40)
    position_set_y(1,500)
    overlay_set_position(reg1,1)
    create_image_button_overlay_with_tableau_material(_g_presentation_obj_custom_banner_22,mesh.color_picker,tableau.color_picker,troop_slot_003)
    create_image_button_overlay_with_tableau_material(_g_presentation_obj_custom_banner_23,mesh.color_picker,tableau.color_picker,troop_slot_004)
    position_set_x(1,200)
    position_set_y(1,565)
    overlay_set_position(_g_presentation_obj_custom_banner_22,1)
    position_set_y(1,515)
    overlay_set_position(_g_presentation_obj_custom_banner_23,1)
    position_set_x(1,250)
    position_set_y(1,250)
    overlay_set_size(_g_presentation_obj_custom_banner_22,1)
    overlay_set_size(_g_presentation_obj_custom_banner_23,1)
    create_button_overlay(_g_presentation_obj_custom_banner_2,gstr.change,16)
    create_button_overlay(_g_presentation_obj_custom_banner_3,gstr.change,16)
    create_button_overlay(_g_presentation_obj_custom_banner_4,gstr.change_background,16)
    create_button_overlay(_g_presentation_obj_custom_banner_5,gstr.change,16)
    create_button_overlay(_g_presentation_obj_custom_banner_19,gstr.change,16)
    create_button_overlay(_g_presentation_obj_custom_banner_20,gstr.accept,16)
    troop_slot_005 = troop_get_slot(trp.player,97)
    create_button_overlay(_g_presentation_obj_custom_banner_16,gstr.randomize,16)
    create_image_button_overlay_with_tableau_material(_g_presentation_obj_custom_banner_17,troop_slot_001,tableau.custom_banner_default,trp.player)
    if troop_slot_002 == mesh.custom_map_banner_01:
        create_image_button_overlay_with_tableau_material(_g_presentation_obj_custom_banner_18,troop_slot_002,tableau.custom_banner_square,trp.player)
    elif troop_slot_002 == mesh.custom_map_banner_02:
        create_image_button_overlay_with_tableau_material(_g_presentation_obj_custom_banner_18,troop_slot_002,tableau.custom_banner_short,trp.player)
    else:
        create_image_button_overlay_with_tableau_material(_g_presentation_obj_custom_banner_18,troop_slot_002,tableau.custom_banner_tall,trp.player)
    #end
    create_image_button_overlay_with_tableau_material(_g_presentation_obj_custom_banner_1,-1,tableau.custom_banner_square_no_mesh,trp.player)
    create_text_overlay(reg1,gstr.sample_banner,16)
    position_set_x(1,825)
    position_set_y(1,650)
    overlay_set_position(reg1,1)
    create_text_overlay(reg1,gstr.sample_map_banner,16)
    position_set_y(1,500)
    overlay_set_position(reg1,1)
    position_set_x(1,800)
    position_set_y(1,640)
    overlay_set_position(_g_presentation_obj_custom_banner_17,1)
    position_set_x(1,780)
    position_set_y(1,315)
    overlay_set_position(_g_presentation_obj_custom_banner_18,1)
    position_set_x(1,50)
    position_set_y(1,50)
    overlay_set_size(_g_presentation_obj_custom_banner_17,1)
    position_set_x(1,50)
    position_set_y(1,50)
    overlay_set_size(_g_presentation_obj_custom_banner_18,1)
    create_text_overlay(reg1,gstr.number_of_charges,0)
    position_set_x(1,40)
    position_set_y(1,350)
    overlay_set_position(reg1,1)
    reg1 = troop_slot_005
    create_text_overlay(reg2,gstr.reg1,16)
    position_set_x(1,350)
    position_set_y(1,350)
    overlay_set_position(reg2,1)
    if troop_slot_005 < 4:
        create_button_overlay(_g_presentation_obj_custom_banner_15,gstr.plus,16)
        position_set_x(1,385)
        position_set_y(1,350)
        overlay_set_position(_g_presentation_obj_custom_banner_15,1)
    else:
        _g_presentation_obj_custom_banner_15 = -1
    #end
    if troop_slot_005 > 0:
        create_button_overlay(_g_presentation_obj_custom_banner_21,gstr.minus,16)
        position_set_x(1,370)
        position_set_y(1,350)
        overlay_set_position(_g_presentation_obj_custom_banner_21,1)
    else:
        _g_presentation_obj_custom_banner_21 = -1
    #end
    if troop_slot_005 >= 1:
        create_text_overlay(reg1,gstr.charge,16)
        position_set_x(1,300)
        position_set_y(1,300)
        overlay_set_position(reg1,1)
        create_text_overlay(reg1,gstr.color,16)
        position_set_x(1,550)
        position_set_y(1,300)
        overlay_set_position(reg1,1)
        create_button_overlay(_g_presentation_obj_custom_banner_14,gstr.change_charge_position,16)
        position_set_y(1,350)
        position_set_x(1,550)
        overlay_set_position(_g_presentation_obj_custom_banner_14,1)
        create_text_overlay(reg1,gstr.charge_no_1,0)
        position_set_x(1,40)
        position_set_y(1,240)
        overlay_set_position(reg1,1)
        create_button_overlay(_g_presentation_obj_custom_banner_6,gstr.change,0)
        position_set_x(1,310)
        overlay_set_position(_g_presentation_obj_custom_banner_6,1)
        create_button_overlay(_g_presentation_obj_custom_banner_7,gstr.change,0)
        position_set_x(1,560)
        overlay_set_position(_g_presentation_obj_custom_banner_7,1)
        troop_slot_006 = troop_get_slot(trp.player,92)
        troop_slot_006 %= 256
        troop_slot_006 = troop_slot_006 + mesh.custom_banner_charge_01
        create_image_button_overlay(_g_presentation_obj_custom_banner_24,troop_slot_006,troop_slot_006)
        position_set_x(1,260)
        position_set_y(1,255)
        overlay_set_position(_g_presentation_obj_custom_banner_24,1)
        position_set_x(1,50)
        position_set_y(1,50)
        overlay_set_size(_g_presentation_obj_custom_banner_24,1)
        troop_slot_007 = troop_get_slot(trp.player,87)
        create_image_button_overlay_with_tableau_material(_g_presentation_obj_custom_banner_28,mesh.color_picker,tableau.color_picker,troop_slot_007)
        position_set_x(1,530)
        position_set_y(1,255)
        overlay_set_position(_g_presentation_obj_custom_banner_28,1)
        position_set_x(1,250)
        position_set_y(1,250)
        overlay_set_size(_g_presentation_obj_custom_banner_28,1)
        create_button_overlay(_g_presentation_obj_custom_banner_32,gstr.flip_horizontal,0)
        position_set_x(1,700)
        position_set_y(1,240)
        overlay_set_position(_g_presentation_obj_custom_banner_32,1)
        create_button_overlay(_g_presentation_obj_custom_banner_33,gstr.flip_vertical,0)
        position_set_x(1,800)
        overlay_set_position(_g_presentation_obj_custom_banner_33,1)
    #end
    if troop_slot_005 >= 2:
        create_text_overlay(reg1,gstr.charge_no_2,0)
        position_set_x(1,40)
        position_set_y(1,180)
        overlay_set_position(reg1,1)
        create_button_overlay(_g_presentation_obj_custom_banner_8,gstr.change,0)
        position_set_x(1,310)
        overlay_set_position(_g_presentation_obj_custom_banner_8,1)
        create_button_overlay(_g_presentation_obj_custom_banner_9,gstr.change,0)
        position_set_x(1,560)
        overlay_set_position(_g_presentation_obj_custom_banner_9,1)
        troop_slot_006 = troop_get_slot(trp.player,93)
        troop_slot_006 %= 256
        troop_slot_006 = troop_slot_006 + mesh.custom_banner_charge_01
        create_image_button_overlay(_g_presentation_obj_custom_banner_25,troop_slot_006,troop_slot_006)
        position_set_x(1,260)
        position_set_y(1,195)
        overlay_set_position(_g_presentation_obj_custom_banner_25,1)
        position_set_x(1,50)
        position_set_y(1,50)
        overlay_set_size(_g_presentation_obj_custom_banner_25,1)
        troop_slot_007 = troop_get_slot(trp.player,88)
        create_image_button_overlay_with_tableau_material(_g_presentation_obj_custom_banner_29,mesh.color_picker,tableau.color_picker,troop_slot_007)
        position_set_x(1,530)
        position_set_y(1,195)
        overlay_set_position(_g_presentation_obj_custom_banner_29,1)
        position_set_x(1,250)
        position_set_y(1,250)
        overlay_set_size(_g_presentation_obj_custom_banner_29,1)
        create_button_overlay(_g_presentation_obj_custom_banner_34,gstr.flip_horizontal,0)
        position_set_x(1,700)
        position_set_y(1,180)
        overlay_set_position(_g_presentation_obj_custom_banner_34,1)
        create_button_overlay(_g_presentation_obj_custom_banner_35,gstr.flip_vertical,0)
        position_set_x(1,800)
        overlay_set_position(_g_presentation_obj_custom_banner_35,1)
    #end
    if troop_slot_005 >= 3:
        create_text_overlay(reg1,gstr.charge_no_3,0)
        position_set_x(1,40)
        position_set_y(1,120)
        overlay_set_position(reg1,1)
        create_button_overlay(_g_presentation_obj_custom_banner_10,gstr.change,0)
        position_set_x(1,310)
        overlay_set_position(_g_presentation_obj_custom_banner_10,1)
        create_button_overlay(_g_presentation_obj_custom_banner_11,gstr.change,0)
        position_set_x(1,560)
        overlay_set_position(_g_presentation_obj_custom_banner_11,1)
        troop_slot_006 = troop_get_slot(trp.player,94)
        troop_slot_006 %= 256
        troop_slot_006 = troop_slot_006 + mesh.custom_banner_charge_01
        create_image_button_overlay(_g_presentation_obj_custom_banner_26,troop_slot_006,troop_slot_006)
        position_set_x(1,260)
        position_set_y(1,135)
        overlay_set_position(_g_presentation_obj_custom_banner_26,1)
        position_set_x(1,50)
        position_set_y(1,50)
        overlay_set_size(_g_presentation_obj_custom_banner_26,1)
        troop_slot_007 = troop_get_slot(trp.player,89)
        create_image_button_overlay_with_tableau_material(_g_presentation_obj_custom_banner_30,mesh.color_picker,tableau.color_picker,troop_slot_007)
        position_set_x(1,530)
        position_set_y(1,135)
        overlay_set_position(_g_presentation_obj_custom_banner_30,1)
        position_set_x(1,250)
        position_set_y(1,250)
        overlay_set_size(_g_presentation_obj_custom_banner_30,1)
        create_button_overlay(_g_presentation_obj_custom_banner_36,gstr.flip_horizontal,0)
        position_set_x(1,700)
        position_set_y(1,120)
        overlay_set_position(_g_presentation_obj_custom_banner_36,1)
        create_button_overlay(_g_presentation_obj_custom_banner_37,gstr.flip_vertical,0)
        position_set_x(1,800)
        overlay_set_position(_g_presentation_obj_custom_banner_37,1)
    #end
    if troop_slot_005 >= 4:
        create_text_overlay(reg1,gstr.charge_no_4,0)
        position_set_x(1,40)
        position_set_y(1,60)
        overlay_set_position(reg1,1)
        create_button_overlay(_g_presentation_obj_custom_banner_12,gstr.change,0)
        position_set_x(1,310)
        overlay_set_position(_g_presentation_obj_custom_banner_12,1)
        create_button_overlay(_g_presentation_obj_custom_banner_13,gstr.change,0)
        position_set_x(1,560)
        overlay_set_position(_g_presentation_obj_custom_banner_13,1)
        troop_slot_006 = troop_get_slot(trp.player,95)
        troop_slot_006 %= 256
        troop_slot_006 = troop_slot_006 + mesh.custom_banner_charge_01
        create_image_button_overlay(_g_presentation_obj_custom_banner_27,troop_slot_006,troop_slot_006)
        position_set_x(1,260)
        position_set_y(1,75)
        overlay_set_position(_g_presentation_obj_custom_banner_27,1)
        position_set_x(1,50)
        position_set_y(1,50)
        overlay_set_size(_g_presentation_obj_custom_banner_27,1)
        troop_slot_007 = troop_get_slot(trp.player,90)
        create_image_button_overlay_with_tableau_material(_g_presentation_obj_custom_banner_31,mesh.color_picker,tableau.color_picker,troop_slot_007)
        position_set_x(1,530)
        position_set_y(1,75)
        overlay_set_position(_g_presentation_obj_custom_banner_31,1)
        position_set_x(1,250)
        position_set_y(1,250)
        overlay_set_size(_g_presentation_obj_custom_banner_31,1)
        create_button_overlay(_g_presentation_obj_custom_banner_38,gstr.flip_horizontal,0)
        position_set_x(1,700)
        position_set_y(1,60)
        overlay_set_position(_g_presentation_obj_custom_banner_38,1)
        create_button_overlay(_g_presentation_obj_custom_banner_39,gstr.flip_vertical,0)
        position_set_x(1,800)
        overlay_set_position(_g_presentation_obj_custom_banner_39,1)
    #end
    position_set_x(1,350)
    position_set_y(1,400)
    overlay_set_position(_g_presentation_obj_custom_banner_1,1)
    position_set_x(1,275)
    position_set_y(1,550)
    overlay_set_position(_g_presentation_obj_custom_banner_2,1)
    position_set_y(1,500)
    overlay_set_position(_g_presentation_obj_custom_banner_3,1)
    position_set_x(1,175)
    position_set_y(1,600)
    overlay_set_position(_g_presentation_obj_custom_banner_4,1)
    position_set_x(1,880)
    position_set_y(1,575)
    overlay_set_position(_g_presentation_obj_custom_banner_5,1)
    position_set_y(1,400)
    overlay_set_position(_g_presentation_obj_custom_banner_19,1)
    position_set_y(1,650)
    position_set_x(1,175)
    overlay_set_position(_g_presentation_obj_custom_banner_16,1)
    position_set_y(1,150)
    position_set_x(1,850)
    overlay_set_position(_g_presentation_obj_custom_banner_20,1)
    presentation_set_duration(999999)
event.codeBlock = code
custom_banner.add_event(event)
event = StateChangedEvent()
def code(var001):
    var001_list2 = [
    _g_presentation_obj_custom_banner_1,
    _g_presentation_obj_custom_banner_4,
    ]
    var001_list2 = [
    _g_presentation_obj_custom_banner_23,
    _g_presentation_obj_custom_banner_3,
    ]
    var001_list1 = [
    _g_presentation_obj_custom_banner_22,
    _g_presentation_obj_custom_banner_2,
    ]
    troop_slot_002 = troop_get_slot(trp.player,97)
    if var001 in var001_list1:
        _g_presentation_next_presentation = prsnt.custom_banner
        _g_presentation_output_slot = 85
        start_presentation(prsnt.color_selection)
    elif var001 in var001_list2:
        _g_presentation_next_presentation = prsnt.custom_banner
        _g_presentation_output_slot = 86
        start_presentation(prsnt.color_selection)
    elif var001 in var001_list2:
        _g_presentation_next_presentation = prsnt.custom_banner
        start_presentation(prsnt.banner_background_selection)
    elif var001 == _g_presentation_obj_custom_banner_5:
        _g_presentation_next_presentation = prsnt.custom_banner
        start_presentation(prsnt.banner_flag_type_selection)
    elif troop_slot_002 >= 1 and var001 == _g_presentation_obj_custom_banner_6 or var001 == _g_presentation_obj_custom_banner_24:
        _g_presentation_next_presentation = prsnt.custom_banner
        _g_presentation_output_slot = 92
        start_presentation(prsnt.banner_charge_selection)
    elif troop_slot_002 >= 1 and var001 == _g_presentation_obj_custom_banner_7 or var001 == _g_presentation_obj_custom_banner_28:
        _g_presentation_next_presentation = prsnt.custom_banner
        _g_presentation_output_slot = 87
        start_presentation(prsnt.color_selection)
    elif troop_slot_002 >= 2 and var001 == _g_presentation_obj_custom_banner_8 or var001 == _g_presentation_obj_custom_banner_25:
        _g_presentation_next_presentation = prsnt.custom_banner
        _g_presentation_output_slot = 93
        start_presentation(prsnt.banner_charge_selection)
    elif troop_slot_002 >= 2 and var001 == _g_presentation_obj_custom_banner_9 or var001 == _g_presentation_obj_custom_banner_29:
        _g_presentation_next_presentation = prsnt.custom_banner
        _g_presentation_output_slot = 88
        start_presentation(prsnt.color_selection)
    elif troop_slot_002 >= 3 and var001 == _g_presentation_obj_custom_banner_10 or var001 == _g_presentation_obj_custom_banner_26:
        _g_presentation_next_presentation = prsnt.custom_banner
        _g_presentation_output_slot = 94
        start_presentation(prsnt.banner_charge_selection)
    elif troop_slot_002 >= 3 and var001 == _g_presentation_obj_custom_banner_11 or var001 == _g_presentation_obj_custom_banner_30:
        _g_presentation_next_presentation = prsnt.custom_banner
        _g_presentation_output_slot = 89
        start_presentation(prsnt.color_selection)
    elif troop_slot_002 >= 4 and var001 == _g_presentation_obj_custom_banner_12 or var001 == _g_presentation_obj_custom_banner_27:
        _g_presentation_next_presentation = prsnt.custom_banner
        _g_presentation_output_slot = 95
        start_presentation(prsnt.banner_charge_selection)
    elif troop_slot_002 >= 4 and var001 == _g_presentation_obj_custom_banner_13 or var001 == _g_presentation_obj_custom_banner_31:
        _g_presentation_next_presentation = prsnt.custom_banner
        _g_presentation_output_slot = 90
        start_presentation(prsnt.color_selection)
    elif troop_slot_002 >= 1 and var001 == _g_presentation_obj_custom_banner_14:
        _g_presentation_next_presentation = prsnt.custom_banner
        start_presentation(prsnt.banner_charge_positioning)
    elif var001 == _g_presentation_obj_custom_banner_15:
        troop_slot_002 = troop_get_slot(trp.player,97)
        troop_slot_002 += 1
        val_clamp(troop_slot_002,0,5)
        troop_set_slot(trp.player,97,troop_slot_002)
        start_presentation(prsnt.custom_banner)
    elif var001 == _g_presentation_obj_custom_banner_21:
        troop_slot_002 = troop_get_slot(trp.player,97)
        troop_slot_002 -= 1
        val_clamp(troop_slot_002,0,5)
        troop_set_slot(trp.player,97,troop_slot_002)
        start_presentation(prsnt.custom_banner)
    elif var001 == _g_presentation_obj_custom_banner_16:
        get_random_custom_banner(trp.player)
        start_presentation(prsnt.custom_banner)
    elif var001 == _g_presentation_obj_custom_banner_17:
        _g_presentation_next_presentation = prsnt.custom_banner
        start_presentation(prsnt.banner_flag_type_selection)
    elif var001 == _g_presentation_obj_custom_banner_18:
        _g_presentation_next_presentation = prsnt.custom_banner
        start_presentation(prsnt.banner_flag_map_type_selection)
    elif var001 == _g_presentation_obj_custom_banner_19:
        _g_presentation_next_presentation = prsnt.custom_banner
        start_presentation(prsnt.banner_flag_map_type_selection)
    elif var001 == _g_presentation_obj_custom_banner_32:
        troop_slot_003 = troop_get_slot(trp.player,92)
        var004 = store_mod(troop_slot_003,256)
        troop_slot_003 /= 256
        var005 = store_mod(troop_slot_003,2)
        troop_slot_003 /= 2
        var005 += 1
        var005 %= 2
        troop_slot_003 *= 2
        troop_slot_003 += var005
        troop_slot_003 *= 256
        troop_slot_003 += var004
        troop_set_slot(trp.player,92,troop_slot_003)
        start_presentation(prsnt.custom_banner)
    elif var001 == _g_presentation_obj_custom_banner_34:
        troop_slot_003 = troop_get_slot(trp.player,93)
        var004 = store_mod(troop_slot_003,256)
        troop_slot_003 /= 256
        var005 = store_mod(troop_slot_003,2)
        troop_slot_003 /= 2
        var005 += 1
        var005 %= 2
        troop_slot_003 *= 2
        troop_slot_003 += var005
        troop_slot_003 *= 256
        troop_slot_003 += var004
        troop_set_slot(trp.player,93,troop_slot_003)
        start_presentation(prsnt.custom_banner)
    elif var001 == _g_presentation_obj_custom_banner_36:
        troop_slot_003 = troop_get_slot(trp.player,94)
        var004 = store_mod(troop_slot_003,256)
        troop_slot_003 /= 256
        var005 = store_mod(troop_slot_003,2)
        troop_slot_003 /= 2
        var005 += 1
        var005 %= 2
        troop_slot_003 *= 2
        troop_slot_003 += var005
        troop_slot_003 *= 256
        troop_slot_003 += var004
        troop_set_slot(trp.player,94,troop_slot_003)
        start_presentation(prsnt.custom_banner)
    elif var001 == _g_presentation_obj_custom_banner_38:
        troop_slot_003 = troop_get_slot(trp.player,95)
        var004 = store_mod(troop_slot_003,256)
        troop_slot_003 /= 256
        var005 = store_mod(troop_slot_003,2)
        troop_slot_003 /= 2
        var005 += 1
        var005 %= 2
        troop_slot_003 *= 2
        troop_slot_003 += var005
        troop_slot_003 *= 256
        troop_slot_003 += var004
        troop_set_slot(trp.player,95,troop_slot_003)
        start_presentation(prsnt.custom_banner)
    elif var001 == _g_presentation_obj_custom_banner_33:
        troop_slot_003 = troop_get_slot(trp.player,92)
        var005 = troop_slot_003 / 512
        var005 += 1
        var005 %= 2
        var005 *= 512
        troop_slot_003 %= 512
        troop_slot_003 += var005
        troop_set_slot(trp.player,92,troop_slot_003)
        start_presentation(prsnt.custom_banner)
    elif var001 == _g_presentation_obj_custom_banner_35:
        troop_slot_003 = troop_get_slot(trp.player,93)
        var005 = troop_slot_003 / 512
        var005 += 1
        var005 %= 2
        var005 *= 512
        troop_slot_003 %= 512
        troop_slot_003 += var005
        troop_set_slot(trp.player,93,troop_slot_003)
        start_presentation(prsnt.custom_banner)
    elif var001 == _g_presentation_obj_custom_banner_37:
        troop_slot_003 = troop_get_slot(trp.player,94)
        var005 = troop_slot_003 / 512
        var005 += 1
        var005 %= 2
        var005 *= 512
        troop_slot_003 %= 512
        troop_slot_003 += var005
        troop_set_slot(trp.player,94,troop_slot_003)
        start_presentation(prsnt.custom_banner)
    elif var001 == _g_presentation_obj_custom_banner_39:
        troop_slot_003 = troop_get_slot(trp.player,95)
        var005 = troop_slot_003 / 512
        var005 += 1
        var005 %= 2
        var005 *= 512
        troop_slot_003 %= 512
        troop_slot_003 += var005
        troop_set_slot(trp.player,95,troop_slot_003)
        start_presentation(prsnt.custom_banner)
    elif var001 == _g_presentation_obj_custom_banner_20:
        troop_slot_006 = troop_get_slot(trp.player,99)
        if troop_slot_006 >= 0:
            troop_slot_006 += 1297036692682702891
            party_set_banner_icon(p.main_party,troop_slot_006)
        #end
        presentation_set_duration(0)
    #end
event.codeBlock = code
custom_banner.add_event(event)


banner_charge_positioning = Presentation("banner_charge_positioning", mesh=mesh.load_window)
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_text_overlay(reg1,gstr.choose_position,16)
    position_set_x(1,500)
    position_set_y(1,600)
    overlay_set_position(reg1,1)
    var001 = 125
    var002 = 400
    get_troop_custom_banner_num_positionings(trp.player)
    var003 = reg0
    var004 = var003 * 125
    var004 -= 25
    var001 = var004 / 2
    var001 = 500 - var001
    for slot_no_005 in range(0, var003):
        create_image_button_overlay_with_tableau_material(reg1,-1,tableau.positioning_selection,slot_no_005)
        position_set_x(1,var001)
        position_set_y(1,var002)
        var001 += 125
        overlay_set_position(reg1,1)
        troop_set_slot(trp.temp_array_a,slot_no_005,reg1)
    #end
    presentation_set_duration(999999)
event.codeBlock = code
banner_charge_positioning.add_event(event)
event = StateChangedEvent()
def code(var001):
    get_troop_custom_banner_num_positionings(trp.player)
    var002 = reg0
    for var003 in range(0, var002):
        if troop_slot_eq(trp.temp_array_a,var003,var001):
            troop_set_slot(trp.player,98,var003)
            var002 = 0
        #end
    #end
    if _g_presentation_next_presentation > 0:
        start_presentation(_g_presentation_next_presentation)
    else:
        presentation_set_duration(0)
    #end
event.codeBlock = code
banner_charge_positioning.add_event(event)


banner_charge_selection = Presentation("banner_charge_selection", mesh=mesh.load_window)
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_text_overlay(reg1,gstr.choose_charge,16)
    position_set_x(1,500)
    position_set_y(1,650)
    overlay_set_position(reg1,1)
    var001 = 100
    var002 = 600
    for mesh_003 in range(mesh.custom_banner_charge_01, mesh.tableau_mesh_custom_banner):
        create_image_button_overlay(reg1,mesh_003,mesh_003)
        position_set_x(1,var001)
        position_set_y(1,var002)
        var001 += 100
        if var001 > 900:
            var001 = 100
            var002 -= 100
        #end
        overlay_set_position(reg1,1)
        position_set_x(1,80)
        position_set_y(1,80)
        overlay_set_size(reg1,1)
        slot_no_004 = mesh_003 - mesh.custom_banner_charge_01
        troop_set_slot(trp.temp_array_a,slot_no_004,reg1)
    #end
    presentation_set_duration(999999)
event.codeBlock = code
banner_charge_selection.add_event(event)
event = StateChangedEvent()
def code(var001):
    var002 = mesh.tableau_mesh_custom_banner
    var002 = var002 - mesh.custom_banner_charge_01
    for var003 in range(0, var002):
        if troop_slot_eq(trp.temp_array_a,var003,var001):
            troop_set_slot(trp.player,_g_presentation_output_slot,var003)
            var002 = 0
        #end
    #end
    if _g_presentation_next_presentation > 0:
        start_presentation(_g_presentation_next_presentation)
    else:
        presentation_set_duration(0)
    #end
event.codeBlock = code
banner_charge_selection.add_event(event)


banner_background_selection = Presentation("banner_background_selection", mesh=mesh.load_window)
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_text_overlay(reg1,gstr.choose_background,16)
    position_set_x(1,500)
    position_set_y(1,600)
    overlay_set_position(reg1,1)
    var001 = 75
    var002 = 450
    for mesh_003 in range(mesh.custom_banner_bg, mesh.custom_banner_charge_01):
        slot_no_004 = mesh_003 - mesh.custom_banner_bg
        create_image_button_overlay_with_tableau_material(reg1,-1,tableau.background_selection,slot_no_004)
        position_set_x(1,var001)
        position_set_y(1,var002)
        var001 += 125
        if var001 > 900:
            var001 = 75
            var002 -= 125
        #end
        overlay_set_position(reg1,1)
        troop_set_slot(trp.temp_array_a,slot_no_004,reg1)
    #end
    presentation_set_duration(999999)
event.codeBlock = code
banner_background_selection.add_event(event)
event = StateChangedEvent()
def code(var001):
    var002 = mesh.custom_banner_charge_01
    var002 = var002 - mesh.custom_banner_bg
    for var003 in range(0, var002):
        if troop_slot_eq(trp.temp_array_a,var003,var001):
            troop_set_slot(trp.player,91,var003)
            var002 = 0
        #end
    #end
    if _g_presentation_next_presentation > 0:
        start_presentation(_g_presentation_next_presentation)
    else:
        presentation_set_duration(0)
    #end
event.codeBlock = code
banner_background_selection.add_event(event)


banner_flag_type_selection = Presentation("banner_flag_type_selection", mesh=mesh.load_window)
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_text_overlay(reg1,gstr.choose_flag_type,16)
    position_set_x(1,500)
    position_set_y(1,600)
    overlay_set_position(reg1,1)
    var001 = 435
    var002 = 450
    for mesh_003 in range(mesh.custom_banner_01, mesh.custom_banner_bg):
        slot_no_004 = mesh_003 - mesh.custom_banner_01
        troop_set_slot(trp.player,96,slot_no_004)
        create_image_button_overlay_with_tableau_material(reg1,mesh_003,tableau.custom_banner_default,trp.player)
        position_set_x(1,var001)
        position_set_y(1,var002)
        var001 += 130
        overlay_set_position(reg1,1)
        position_set_x(1,100)
        position_set_y(1,100)
        overlay_set_size(reg1,1)
        troop_set_slot(trp.temp_array_a,slot_no_004,reg1)
    #end
    presentation_set_duration(999999)
event.codeBlock = code
banner_flag_type_selection.add_event(event)
event = StateChangedEvent()
def code(var001):
    var002 = mesh.custom_banner_bg
    var002 = var002 - mesh.custom_banner_01
    for var003 in range(0, var002):
        if troop_slot_eq(trp.temp_array_a,var003,var001):
            troop_set_slot(trp.player,96,var003)
            var002 = 0
        #end
    #end
    if _g_presentation_next_presentation > 0:
        start_presentation(_g_presentation_next_presentation)
    else:
        presentation_set_duration(0)
    #end
event.codeBlock = code
banner_flag_type_selection.add_event(event)


banner_flag_map_type_selection = Presentation("banner_flag_map_type_selection", mesh=mesh.load_window)
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_text_overlay(reg1,gstr.choose_map_flag_type,16)
    position_set_x(1,500)
    position_set_y(1,600)
    overlay_set_position(reg1,1)
    troop_slot_001 = troop_get_slot(trp.player,91)
    troop_slot_001 = troop_slot_001 + mesh.custom_banner_bg
    var002 = 250
    var003 = 150
    for mesh_004 in range(mesh.custom_map_banner_01, mesh.custom_banner_01):
        slot_no_005 = mesh_004 - mesh.custom_map_banner_01
        troop_set_slot(trp.player,99,slot_no_005)
        if mesh_004 == mesh.custom_map_banner_01:
            create_image_button_overlay_with_tableau_material(reg1,mesh_004,tableau.custom_banner_square,trp.player)
        elif mesh_004 == mesh.custom_map_banner_02:
            create_image_button_overlay_with_tableau_material(reg1,mesh_004,tableau.custom_banner_short,trp.player)
        else:
            create_image_button_overlay_with_tableau_material(reg1,mesh_004,tableau.custom_banner_tall,trp.player)
        #end
        position_set_x(1,var002)
        position_set_y(1,var003)
        var002 += 200
        overlay_set_position(reg1,1)
        position_set_x(1,100)
        position_set_y(1,100)
        overlay_set_size(reg1,1)
        troop_set_slot(trp.temp_array_a,slot_no_005,reg1)
    #end
    presentation_set_duration(999999)
event.codeBlock = code
banner_flag_map_type_selection.add_event(event)
event = StateChangedEvent()
def code(var001):
    var002 = mesh.custom_banner_01
    var002 = var002 - mesh.custom_map_banner_01
    for var003 in range(0, var002):
        if troop_slot_eq(trp.temp_array_a,var003,var001):
            troop_set_slot(trp.player,99,var003)
            var002 = 0
        #end
    #end
    if _g_presentation_next_presentation > 0:
        start_presentation(_g_presentation_next_presentation)
    else:
        presentation_set_duration(0)
    #end
event.codeBlock = code
banner_flag_map_type_selection.add_event(event)


color_selection = Presentation("color_selection", mesh=mesh.load_window)
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_text_overlay(reg1,gstr.choose_color,16)
    position_set_x(1,500)
    position_set_y(1,600)
    overlay_set_position(reg1,1)
    var001 = 125
    var002 = 450
    for var003 in range(0, 42):
        get_custom_banner_color_from_index(var003)
        var004 = reg0
        create_image_button_overlay_with_tableau_material(reg1,mesh.color_picker,tableau.color_picker,var004)
        position_set_x(1,var001)
        position_set_y(1,var002)
        var001 += 50
        if True:
            var005 = store_mod(var003,7)
            if var005 == 6:
                var001 = 125
                var002 -= 50
            #end
        #end
        overlay_set_position(reg1,1)
        position_set_x(1,500)
        position_set_y(1,500)
        overlay_set_size(reg1,1)
        slot_no_006 = var003 * 2
        slot_no_007 = slot_no_006 + 1
        troop_set_slot(trp.temp_array_a,slot_no_006,reg1)
        troop_set_slot(trp.temp_array_a,slot_no_007,var004)
    #end
    presentation_set_duration(999999)
event.codeBlock = code
color_selection.add_event(event)
event = StateChangedEvent()
def code(var001):
    var002 = 64
    for var003 in range(0, var002):
        var004 = var003 * 2
        if troop_slot_eq(trp.temp_array_a,var004,var001):
            slot_no_005 = var004 + 1
            troop_slot_006 = troop_get_slot(trp.temp_array_a,slot_no_005)
            troop_set_slot(trp.player,_g_presentation_output_slot,troop_slot_006)
            var002 = 0
        #end
    #end
    if _g_presentation_next_presentation > 0:
        start_presentation(_g_presentation_next_presentation)
    else:
        presentation_set_duration(0)
    #end
event.codeBlock = code
color_selection.add_event(event)


marshall_selection = Presentation("marshall_selection", mesh=mesh.load_window)
event = LoadEvent()
def code():
    _g_presentation_obj_marshall_selection_1 = -1
    _g_presentation_obj_marshall_selection_2 = -1
    _g_presentation_obj_marshall_selection_3 = -1
    set_fixed_point_multiplier(1000)
    _g_presentation_next_presentation = -1
    var001 = _g_presentation_marshall_selection_max_renown_1 + _g_presentation_marshall_selection_max_renown_2
    faction_slot_002 = faction_get_slot(_players_kingdom,11)
    s1 = str_store_troop_name(_g_presentation_marshall_selection_max_renown_1_troop)
    create_text_overlay(reg1,"@Candidate #1: {s1}",16)
    position_set_x(1,200)
    position_set_y(1,600)
    overlay_set_position(reg1,1)
    s1 = str_store_troop_name(_g_presentation_marshall_selection_max_renown_2_troop)
    create_text_overlay(reg1,"@Candidate #2: {s1}",16)
    position_set_x(1,800)
    position_set_y(1,600)
    overlay_set_position(reg1,1)
    create_mesh_overlay_with_tableau_material(reg1,-1,tableau.troop_note_mesh,_g_presentation_marshall_selection_max_renown_1_troop)
    position_set_x(1,500)
    position_set_y(1,500)
    overlay_set_size(reg1,1)
    position_set_x(1,100)
    position_set_y(1,300)
    overlay_set_position(reg1,1)
    create_mesh_overlay_with_tableau_material(reg1,-1,tableau.troop_note_mesh,_g_presentation_marshall_selection_max_renown_2_troop)
    position_set_x(1,500)
    position_set_y(1,500)
    overlay_set_size(reg1,1)
    position_set_x(1,700)
    position_set_y(1,300)
    overlay_set_position(reg1,1)
    var003 = _g_presentation_input
    _g_presentation_input += 1
    if var003 < 0:
        s1 = str_store_troop_name(_g_presentation_marshall_selection_max_renown_1_troop)
        s2 = str_store_troop_name(_g_presentation_marshall_selection_max_renown_2_troop)
        s3 = str_store_troop_name(faction_slot_002)
        s4 = str_store_faction_name(_players_kingdom)
        create_text_overlay(reg1,"@{s3} of {s4} wishes to select a new marshall and invites his vassals for a counsel. {s1} and {s2} are the likely candidates.",16)
        position_set_x(1,500)
        position_set_y(1,200)
        overlay_set_position(reg1,1)
        create_button_overlay(_g_presentation_obj_marshall_selection_1,"@Continue...",16)
        position_set_x(1,500)
        position_set_y(1,100)
        overlay_set_position(_g_presentation_obj_marshall_selection_1,1)
        _g_presentation_next_presentation = prsnt.marshall_selection
    else:
        var004 = var003
        for trp_005 in range(trp.kingdom_heroes_including_player_begin, trp.knight_1_1_wife):
            if var004 >= 0:
                troop_id_006 = trp_005
                var007 = 0
                if trp_005 == trp.kingdom_heroes_including_player_begin:
                    troop_id_006 = trp.player
                    if _g_player_is_captive == 0:
                        var007 = 1
                    #end
                #end
            else:
                troop_faction_008 = store_faction_of_troop(troop_id_006)
                if _players_kingdom == troop_faction_008 and not troop_slot_ge(troop_id_006,8,0) and troop_slot_ge(troop_id_006,10,1) and troop_slot_eq(troop_id_006,2,2) and not faction_slot_eq(troop_faction_008,11,troop_id_006):
                    var007 = 1
                #end
            #end
            if var007 == 1 and _g_presentation_marshall_selection_max_renown_1_troop != troop_id_006 and _g_presentation_marshall_selection_max_renown_2_troop != troop_id_006:
                var004 -= 1
                if var004 < 0:
                    _g_presentation_next_presentation = prsnt.marshall_selection
                    create_mesh_overlay_with_tableau_material(reg1,-1,tableau.troop_note_mesh,troop_id_006)
                    position_set_x(1,300)
                    position_set_y(1,300)
                    overlay_set_size(reg1,1)
                    position_set_x(1,440)
                    position_set_y(1,400)
                    overlay_set_position(reg1,1)
                    if troop_id_006 == trp.player:
                        create_text_overlay(reg1,"@Who do you wish to support?",16)
                        position_set_x(1,500)
                        position_set_y(1,200)
                        overlay_set_position(reg1,1)
                        s1 = str_store_troop_name(_g_presentation_marshall_selection_max_renown_1_troop)
                        create_button_overlay(_g_presentation_obj_marshall_selection_2,"@{!}{s1}",16)
                        position_set_x(1,300)
                        position_set_y(1,100)
                        overlay_set_position(_g_presentation_obj_marshall_selection_2,1)
                        s1 = str_store_troop_name(_g_presentation_marshall_selection_max_renown_2_troop)
                        create_button_overlay(_g_presentation_obj_marshall_selection_3,"@{!}{s1}",16)
                        position_set_x(1,700)
                        position_set_y(1,100)
                        overlay_set_position(_g_presentation_obj_marshall_selection_3,1)
                    else:
                        s1 = str_store_troop_name(troop_id_006)
                        random_x_009 = store_random_in_range(0,var001)
                        random_x_009 -= _g_presentation_marshall_selection_max_renown_1
                        if random_x_009 < 0:
                            _g_presentation_marshall_selection_1_vote += 1
                            s2 = str_store_troop_name(_g_presentation_marshall_selection_max_renown_1_troop)
                        else:
                            _g_presentation_marshall_selection_2_vote += 1
                            s2 = str_store_troop_name(_g_presentation_marshall_selection_max_renown_2_troop)
                        #end
                    #end
                #end
                create_text_overlay(reg1,"@{s1} gives his support to {s2}.",16)
                position_set_x(1,500)
                position_set_y(1,200)
                overlay_set_position(reg1,1)
                create_button_overlay(_g_presentation_obj_marshall_selection_1,"@Continue...",16)
                position_set_x(1,500)
                position_set_y(1,100)
                overlay_set_position(_g_presentation_obj_marshall_selection_1,1)
            #end
        #end
    #end
    reg0 = _g_presentation_marshall_selection_1_vote
    create_text_overlay(reg1,"@Number of Supporters: {reg0}",16)
    position_set_x(1,200)
    position_set_y(1,550)
    overlay_set_position(reg1,1)
    reg0 = _g_presentation_marshall_selection_2_vote
    create_text_overlay(reg1,"@Number of Supporters: {reg0}",16)
    position_set_x(1,800)
    position_set_y(1,550)
    overlay_set_position(reg1,1)
    if _g_presentation_next_presentation < 0:
        if _g_presentation_marshall_selection_2_vote > _g_presentation_marshall_selection_1_vote:
            var010 = _g_presentation_marshall_selection_max_renown_1_troop
            _g_presentation_marshall_selection_max_renown_1_troop = _g_presentation_marshall_selection_max_renown_2_troop
            _g_presentation_marshall_selection_max_renown_2_troop = var010
        #end
        s1 = str_store_troop_name(_g_presentation_marshall_selection_max_renown_1_troop)
        s2 = str_store_troop_name(faction_slot_002)
        s3 = str_store_faction_name(_players_kingdom)
        create_text_overlay(reg1,"@{s2} has heard his vassals' counsel. He selects {s1} as the marshall of {s3}.",16)
        position_set_x(1,500)
        position_set_y(1,200)
        overlay_set_position(reg1,1)
        create_button_overlay(_g_presentation_obj_marshall_selection_1,"@Continue...",16)
        position_set_x(1,500)
        position_set_y(1,100)
        overlay_set_position(_g_presentation_obj_marshall_selection_1,1)
    #end
    presentation_set_duration(999999)
event.codeBlock = code
marshall_selection.add_event(event)
event = StateChangedEvent()
def code(var001):
    var001_list1 = [
    _g_presentation_obj_marshall_selection_3,
    _g_presentation_obj_marshall_selection_2,
    _g_presentation_obj_marshall_selection_1,
    ]
    if var001 == _g_presentation_obj_marshall_selection_2:
        _g_presentation_marshall_selection_1_vote += 1
        change_player_relation_with_troop(_g_presentation_marshall_selection_max_renown_1_troop,2)
        change_player_relation_with_troop(_g_presentation_marshall_selection_max_renown_2_troop,-2)
    elif var001 == _g_presentation_obj_marshall_selection_3:
        _g_presentation_marshall_selection_2_vote += 1
        change_player_relation_with_troop(_g_presentation_marshall_selection_max_renown_1_troop,-2)
        change_player_relation_with_troop(_g_presentation_marshall_selection_max_renown_2_troop,2)
    #end
    if var001 in var001_list1:
        if _g_presentation_next_presentation >= 0:
            start_presentation(_g_presentation_next_presentation)
        else:
            if not faction_slot_eq(_players_kingdom,8,_g_presentation_marshall_selection_max_renown_1_troop):
                check_and_finish_active_army_quests_for_faction(_players_kingdom)
            #end
            faction_slot_002 = faction_get_slot(_players_kingdom,8)
            if faction_slot_002 >= 0 and party_is_active(faction_slot_002):
                party_set_marshall(faction_slot_002,0)
            #end
            faction_set_slot(_players_kingdom,8,_g_presentation_marshall_selection_max_renown_1_troop)
            if _g_presentation_marshall_selection_max_renown_1_troop == trp.player:
                change_player_relation_with_troop(_g_presentation_marshall_selection_max_renown_2_troop,-3)
            #end
            _g_recalculate_ais = 1
            _g_presentation_marshall_selection_ended = 1
            presentation_set_duration(0)
        #end
    #end
event.codeBlock = code
marshall_selection.add_event(event)


battle = Presentation("battle")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    _g_formation_group0_selected = 0
    _g_formation_group1_selected = 0
    _g_formation_group2_selected = 0
    _g_formation_group3_selected = 0
    _g_formation_group4_selected = 0
    _g_formation_group5_selected = 0
    _g_formation_group6_selected = 0
    _g_formation_group7_selected = 0
    _g_formation_group8_selected = 0
    _g_presentation_obj_battle_but0 = -1
    _g_presentation_obj_battle_but1 = -1
    _g_presentation_obj_battle_but2 = -1
    _g_presentation_obj_battle_but3 = -1
    _g_presentation_obj_battle_but4 = -1
    _g_presentation_obj_battle_but5 = -1
    _g_presentation_obj_battle_but6 = -1
    _g_presentation_obj_battle_but7 = -1
    _g_presentation_obj_battle_but8 = -1
    str_clear(7)
    for cur_agent in __all_agents__:
        agent_set_slot(cur_agent,10,0)
    #end
    agent_no_002 = get_player_agent_no()
    troop_id_003 = agent_get_troop_id(agent_no_002)
    position_set_y(1,700)
    create_text_overlay(reg1,"@Action",98320)
    overlay_set_color(reg1,4289374890)
    position_set_x(1,270)
    overlay_set_position(reg1,1)
    create_text_overlay(reg1,"@Mount",98320)
    overlay_set_color(reg1,4289374890)
    position_set_x(1,410)
    overlay_set_position(reg1,1)
    create_text_overlay(reg1,"@Attack Type",98320)
    overlay_set_color(reg1,4289374890)
    position_set_x(1,550)
    overlay_set_position(reg1,1)
    _group0_has_troops = 0
    _group1_has_troops = 0
    _group2_has_troops = 0
    _group3_has_troops = 0
    _group4_has_troops = 0
    _group5_has_troops = 0
    _group6_has_troops = 0
    _group7_has_troops = 0
    _group8_has_troops = 0
    party_num_companions_stacks_004 = party_get_num_companion_stacks(p.main_party)
    _num_classes = 0
    for stack_no_005 in range(0, party_num_companions_stacks_004):
        troop_id_006 = party_stack_get_troop_id(p.main_party,stack_no_005)
        troop_class_007 = troop_get_class(troop_id_006)
        if troop_id_003 != troop_id_006:
            if troop_class_007 == 0:
                if _group0_has_troops != 1:
                    _num_classes += 1
                #end
            #end
            _group0_has_troops = 1
        elif troop_class_007 == 1:
            if _group1_has_troops != 1:
                _num_classes += 1
            #end
            _group1_has_troops = 1
        elif troop_class_007 == 2:
            if _group2_has_troops != 1:
                _num_classes += 1
            #end
            _group2_has_troops = 1
        elif troop_class_007 == 3:
            if _group3_has_troops != 1:
                _num_classes += 1
            #end
            _group3_has_troops = 1
        elif troop_class_007 == 4:
            if _group4_has_troops != 1:
                _num_classes += 1
            #end
            _group4_has_troops = 1
        elif troop_class_007 == 5:
            if _group5_has_troops != 1:
                _num_classes += 1
            #end
            _group5_has_troops = 1
        elif troop_class_007 == 6:
            if _group6_has_troops != 1:
                _num_classes += 1
            #end
            _group6_has_troops = 1
        elif troop_class_007 == 7:
            if _group7_has_troops != 1:
                _num_classes += 1
            #end
            _group7_has_troops = 1
        elif troop_class_007 == 8:
            if _group8_has_troops != 1:
                _num_classes += 1
            #end
            _group8_has_troops = 1
        #end
    #end
    var008 = 0
    var009 = 653
    var010 = 20
    var011 = 662
    var012 = 50
    var013 = 660
    if _group0_has_troops == 1:
        create_image_button_overlay(_g_presentation_obj_battle_but0,mesh.white_plane,mesh.white_plane)
        position_set_x(1,var008)
        position_set_y(1,var009)
        overlay_set_position(_g_presentation_obj_battle_but0,1)
        var009 += -40
        position_set_x(1,32500)
        position_set_y(1,2000)
        overlay_set_size(_g_presentation_obj_battle_but0,1)
        overlay_set_alpha(_g_presentation_obj_battle_but0,0)
        overlay_set_color(_g_presentation_obj_battle_but0,16776960)
        create_check_box_overlay(_g_presentation_obj_battle_check0,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(2,var010)
        position_set_y(2,var011)
        overlay_set_position(_g_presentation_obj_battle_check0,2)
        var011 += -40
        create_text_overlay(_g_presentation_obj_battle_name0,7,0)
        position_set_x(3,var012)
        position_set_y(3,var013)
        overlay_set_position(_g_presentation_obj_battle_name0,3)
        var013 += -40
        create_text_overlay(_g_presentation_but0_movement,7,16)
        create_text_overlay(_g_presentation_but0_riding,7,16)
        create_text_overlay(_g_presentation_but0_weapon_usage,7,16)
    #end
    if _group1_has_troops == 1:
        create_image_button_overlay(_g_presentation_obj_battle_but1,mesh.white_plane,mesh.white_plane)
        position_set_x(1,var008)
        position_set_y(1,var009)
        overlay_set_position(_g_presentation_obj_battle_but1,1)
        var009 += -40
        position_set_x(1,32500)
        position_set_y(1,2000)
        overlay_set_size(_g_presentation_obj_battle_but1,1)
        overlay_set_alpha(_g_presentation_obj_battle_but1,0)
        overlay_set_color(_g_presentation_obj_battle_but1,16776960)
        create_check_box_overlay(_g_presentation_obj_battle_check1,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(2,var010)
        position_set_y(2,var011)
        overlay_set_position(_g_presentation_obj_battle_check1,2)
        var011 += -40
        create_text_overlay(_g_presentation_obj_battle_name1,7,0)
        position_set_x(3,var012)
        position_set_y(3,var013)
        overlay_set_position(_g_presentation_obj_battle_name1,3)
        var013 += -40
        create_text_overlay(_g_presentation_but1_movement,7,16)
        create_text_overlay(_g_presentation_but1_riding,7,16)
        create_text_overlay(_g_presentation_but1_weapon_usage,7,16)
    #end
    if _group2_has_troops == 1:
        create_image_button_overlay(_g_presentation_obj_battle_but2,mesh.white_plane,mesh.white_plane)
        position_set_x(1,var008)
        position_set_y(1,var009)
        overlay_set_position(_g_presentation_obj_battle_but2,1)
        var009 += -40
        position_set_x(1,32500)
        position_set_y(1,2000)
        overlay_set_size(_g_presentation_obj_battle_but2,1)
        overlay_set_alpha(_g_presentation_obj_battle_but2,0)
        overlay_set_color(_g_presentation_obj_battle_but2,16776960)
        create_check_box_overlay(_g_presentation_obj_battle_check2,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(2,var010)
        position_set_y(2,var011)
        overlay_set_position(_g_presentation_obj_battle_check2,2)
        var011 += -40
        create_text_overlay(_g_presentation_obj_battle_name2,7,0)
        position_set_x(3,var012)
        position_set_y(3,var013)
        overlay_set_position(_g_presentation_obj_battle_name2,3)
        var013 += -40
        create_text_overlay(_g_presentation_but2_movement,7,16)
        create_text_overlay(_g_presentation_but2_riding,7,16)
        create_text_overlay(_g_presentation_but2_weapon_usage,7,16)
    #end
    if _group3_has_troops == 1:
        create_image_button_overlay(_g_presentation_obj_battle_but3,mesh.white_plane,mesh.white_plane)
        position_set_x(1,var008)
        position_set_y(1,var009)
        overlay_set_position(_g_presentation_obj_battle_but3,1)
        var009 += -40
        position_set_x(1,32500)
        position_set_y(1,2000)
        overlay_set_size(_g_presentation_obj_battle_but3,1)
        overlay_set_alpha(_g_presentation_obj_battle_but3,0)
        overlay_set_color(_g_presentation_obj_battle_but3,16776960)
        create_check_box_overlay(_g_presentation_obj_battle_check3,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(2,var010)
        position_set_y(2,var011)
        overlay_set_position(_g_presentation_obj_battle_check3,2)
        var011 += -40
        create_text_overlay(_g_presentation_obj_battle_name3,7,0)
        position_set_x(3,var012)
        position_set_y(3,var013)
        overlay_set_position(_g_presentation_obj_battle_name3,3)
        var013 += -40
        create_text_overlay(_g_presentation_but3_movement,7,16)
        create_text_overlay(_g_presentation_but3_riding,7,16)
        create_text_overlay(_g_presentation_but3_weapon_usage,7,16)
    #end
    if _group4_has_troops == 1:
        create_image_button_overlay(_g_presentation_obj_battle_but4,mesh.white_plane,mesh.white_plane)
        position_set_x(1,var008)
        position_set_y(1,var009)
        overlay_set_position(_g_presentation_obj_battle_but4,1)
        var009 += -40
        position_set_x(1,32500)
        position_set_y(1,2000)
        overlay_set_size(_g_presentation_obj_battle_but4,1)
        overlay_set_alpha(_g_presentation_obj_battle_but4,0)
        overlay_set_color(_g_presentation_obj_battle_but4,16776960)
        create_check_box_overlay(_g_presentation_obj_battle_check4,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(2,var010)
        position_set_y(2,var011)
        overlay_set_position(_g_presentation_obj_battle_check4,2)
        var011 += -40
        create_text_overlay(_g_presentation_obj_battle_name4,7,0)
        position_set_x(3,var012)
        position_set_y(3,var013)
        overlay_set_position(_g_presentation_obj_battle_name4,3)
        var013 += -40
        create_text_overlay(_g_presentation_but4_movement,7,16)
        create_text_overlay(_g_presentation_but4_riding,7,16)
        create_text_overlay(_g_presentation_but4_weapon_usage,7,16)
    #end
    if _group5_has_troops == 1:
        create_image_button_overlay(_g_presentation_obj_battle_but5,mesh.white_plane,mesh.white_plane)
        position_set_x(1,var008)
        position_set_y(1,var009)
        overlay_set_position(_g_presentation_obj_battle_but5,1)
        var009 += -40
        position_set_x(1,32500)
        position_set_y(1,2000)
        overlay_set_size(_g_presentation_obj_battle_but5,1)
        overlay_set_alpha(_g_presentation_obj_battle_but5,0)
        overlay_set_color(_g_presentation_obj_battle_but5,16776960)
        create_check_box_overlay(_g_presentation_obj_battle_check5,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(2,var010)
        position_set_y(2,var011)
        overlay_set_position(_g_presentation_obj_battle_check5,2)
        var011 += -40
        create_text_overlay(_g_presentation_obj_battle_name5,7,0)
        position_set_x(3,var012)
        position_set_y(3,var013)
        overlay_set_position(_g_presentation_obj_battle_name5,3)
        var013 += -40
        create_text_overlay(_g_presentation_but5_movement,7,16)
        create_text_overlay(_g_presentation_but5_riding,7,16)
        create_text_overlay(_g_presentation_but5_weapon_usage,7,16)
    #end
    if _group6_has_troops == 1:
        create_image_button_overlay(_g_presentation_obj_battle_but6,mesh.white_plane,mesh.white_plane)
        position_set_x(1,var008)
        position_set_y(1,var009)
        overlay_set_position(_g_presentation_obj_battle_but6,1)
        var009 += -40
        position_set_x(1,32500)
        position_set_y(1,2000)
        overlay_set_size(_g_presentation_obj_battle_but6,1)
        overlay_set_alpha(_g_presentation_obj_battle_but6,0)
        overlay_set_color(_g_presentation_obj_battle_but6,16776960)
        create_check_box_overlay(_g_presentation_obj_battle_check6,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(2,var010)
        position_set_y(2,var011)
        overlay_set_position(_g_presentation_obj_battle_check6,2)
        var011 += -40
        create_text_overlay(_g_presentation_obj_battle_name6,7,0)
        position_set_x(3,var012)
        position_set_y(3,var013)
        overlay_set_position(_g_presentation_obj_battle_name6,3)
        var013 += -40
        create_text_overlay(_g_presentation_but6_movement,7,16)
        create_text_overlay(_g_presentation_but6_riding,7,16)
        create_text_overlay(_g_presentation_but6_weapon_usage,7,16)
    #end
    if _group7_has_troops == 1:
        create_image_button_overlay(_g_presentation_obj_battle_but7,mesh.white_plane,mesh.white_plane)
        position_set_x(1,var008)
        position_set_y(1,var009)
        overlay_set_position(_g_presentation_obj_battle_but7,1)
        var009 += -40
        position_set_x(1,32500)
        position_set_y(1,2000)
        overlay_set_size(_g_presentation_obj_battle_but7,1)
        overlay_set_alpha(_g_presentation_obj_battle_but7,0)
        overlay_set_color(_g_presentation_obj_battle_but7,16776960)
        create_check_box_overlay(_g_presentation_obj_battle_check7,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(2,var010)
        position_set_y(2,var011)
        overlay_set_position(_g_presentation_obj_battle_check7,2)
        var011 += -40
        create_text_overlay(_g_presentation_obj_battle_name7,7,0)
        position_set_x(3,var012)
        position_set_y(3,var013)
        overlay_set_position(_g_presentation_obj_battle_name7,3)
        var013 += -40
        create_text_overlay(_g_presentation_but7_movement,7,16)
        create_text_overlay(_g_presentation_but7_riding,7,16)
        create_text_overlay(_g_presentation_but7_weapon_usage,7,16)
    #end
    if _group8_has_troops == 1:
        create_image_button_overlay(_g_presentation_obj_battle_but8,mesh.white_plane,mesh.white_plane)
        position_set_x(1,var008)
        position_set_y(1,var009)
        overlay_set_position(_g_presentation_obj_battle_but8,1)
        var009 += -40
        position_set_x(1,32500)
        position_set_y(1,2000)
        overlay_set_size(_g_presentation_obj_battle_but8,1)
        overlay_set_alpha(_g_presentation_obj_battle_but8,0)
        overlay_set_color(_g_presentation_obj_battle_but8,16776960)
        create_check_box_overlay(_g_presentation_obj_battle_check8,mesh.checkbox_off,mesh.checkbox_on)
        position_set_x(2,var010)
        position_set_y(2,var011)
        overlay_set_position(_g_presentation_obj_battle_check8,2)
        var011 += -40
        create_text_overlay(_g_presentation_obj_battle_name8,7,0)
        position_set_x(3,var012)
        position_set_y(3,var013)
        overlay_set_position(_g_presentation_obj_battle_name8,3)
        var013 += -40
        create_text_overlay(_g_presentation_but8_movement,7,16)
        create_text_overlay(_g_presentation_but8_riding,7,16)
        create_text_overlay(_g_presentation_but8_weapon_usage,7,16)
    #end
    agent_no_002 = get_player_agent_no()
    agent_team_no_014 = agent_get_team(agent_no_002)
    update_order_panel(agent_team_no_014)
    var015 = 640
    var016 = _num_classes
    var016 *= -40
    var015 += var016
    create_listbox_overlay(_g_presentation_obj_battle_10,gstr.space,0)
    create_listbox_overlay(_g_presentation_obj_battle_11,gstr.space,0)
    create_listbox_overlay(_g_presentation_obj_battle_12,gstr.space,0)
    create_listbox_overlay(_g_presentation_obj_battle_13,gstr.space,0)
    overlay_add_item(_g_presentation_obj_battle_10,"@Stand Ground")
    overlay_add_item(_g_presentation_obj_battle_10,"@Charge")
    overlay_add_item(_g_presentation_obj_battle_10,"@Follow Me")
    overlay_add_item(_g_presentation_obj_battle_10,"@Hold This Position")
    create_button_overlay(_g_presentation_obj_battle_14,"@Spread Out",98320)
    overlay_set_color(_g_presentation_obj_battle_14,4294967295)
    create_button_overlay(_g_presentation_obj_battle_15,"@Stand Closer",98320)
    overlay_set_color(_g_presentation_obj_battle_15,4294967295)
    create_button_overlay(_g_presentation_obj_battle_16,"@Fall Back",98320)
    overlay_set_color(_g_presentation_obj_battle_16,4294967295)
    create_button_overlay(_g_presentation_obj_battle_17,"@Advance",98320)
    overlay_set_color(_g_presentation_obj_battle_17,4294967295)
    position_set_x(1,600)
    position_set_y(1,600)
    overlay_set_size(_g_presentation_obj_battle_10,1)
    var015 += -35
    position_set_x(1,205)
    position_set_y(1,var015)
    var015 += 35
    overlay_set_position(_g_presentation_obj_battle_10,1)
    overlay_set_alpha(_g_presentation_obj_battle_10,96)
    overlay_set_val(_g_presentation_obj_battle_10,_g_latest_order_1)
    var015 += -40
    position_set_x(1,130)
    position_set_y(1,var015)
    var015 += 40
    overlay_set_position(_g_presentation_obj_battle_14,1)
    var015 += -20
    position_set_x(1,130)
    position_set_y(1,var015)
    var015 += 20
    overlay_set_position(_g_presentation_obj_battle_15,1)
    var015 += 0
    position_set_x(1,130)
    position_set_y(1,var015)
    var015 += 0
    overlay_set_position(_g_presentation_obj_battle_16,1)
    var015 += 20
    position_set_x(1,130)
    position_set_y(1,var015)
    var015 += -20
    overlay_set_position(_g_presentation_obj_battle_17,1)
    overlay_add_item(_g_presentation_obj_battle_11,"@Dismount")
    overlay_add_item(_g_presentation_obj_battle_11,"@Mount")
    position_set_x(1,600)
    position_set_y(1,600)
    overlay_set_size(_g_presentation_obj_battle_11,1)
    position_set_x(1,350)
    position_set_y(1,var015)
    overlay_set_position(_g_presentation_obj_battle_11,1)
    overlay_set_alpha(_g_presentation_obj_battle_11,96)
    overlay_set_val(_g_presentation_obj_battle_11,_g_latest_order_2)
    overlay_add_item(_g_presentation_obj_battle_12,"@Fire At Will")
    overlay_add_item(_g_presentation_obj_battle_12,"@Hold Your Fire")
    position_set_x(1,600)
    position_set_y(1,600)
    overlay_set_size(_g_presentation_obj_battle_12,1)
    position_set_x(1,495)
    position_set_y(1,var015)
    overlay_set_position(_g_presentation_obj_battle_12,1)
    overlay_set_alpha(_g_presentation_obj_battle_12,96)
    overlay_set_val(_g_presentation_obj_battle_12,_g_latest_order_3)
    overlay_add_item(_g_presentation_obj_battle_13,"@Use Blunt Weapons")
    overlay_add_item(_g_presentation_obj_battle_13,"@Use Any Weapon")
    position_set_x(1,600)
    position_set_y(1,600)
    overlay_set_size(_g_presentation_obj_battle_13,1)
    var015 += -35
    position_set_x(1,495)
    position_set_y(1,var015)
    var015 += 35
    overlay_set_position(_g_presentation_obj_battle_13,1)
    overlay_set_alpha(_g_presentation_obj_battle_13,96)
    overlay_set_val(_g_presentation_obj_battle_13,_g_latest_order_4)
    create_text_overlay(_g_presentation_obj_battle_22,gstr.us_,0)
    create_text_overlay(_g_presentation_obj_battle_23,gstr.allies_,0)
    create_text_overlay(_g_presentation_obj_battle_24,gstr.enemies_,0)
    create_text_overlay(_g_presentation_obj_battle_25,"@Ready",16)
    create_text_overlay(_g_presentation_obj_battle_26,"@Wounded",16)
    create_text_overlay(_g_presentation_obj_battle_28,gstr.routed,16)
    create_text_overlay(_g_presentation_obj_battle_27,"@Dead",16)
    create_text_overlay(_g_battle_us_ready,7,16)
    create_text_overlay(_g_battle_us_wounded,7,16)
    create_text_overlay(_g_battle_us_routed,7,16)
    create_text_overlay(_g_battle_us_dead,7,16)
    create_text_overlay(_g_battle_enemies_ready,7,16)
    create_text_overlay(_g_battle_enemies_wounded,7,16)
    create_text_overlay(_g_battle_enemies_routed,7,16)
    create_text_overlay(_g_battle_enemies_dead,7,16)
    create_text_overlay(_g_battle_allies_ready,7,16)
    create_text_overlay(_g_battle_allies_wounded,7,16)
    create_text_overlay(_g_battle_allies_routed,7,16)
    create_text_overlay(_g_battle_allies_dead,7,16)
    create_image_button_overlay(_g_battle_report_plane,mesh.white_plane,mesh.white_plane)
    overlay_set_color(_g_battle_report_plane,0)
    position_set_x(1,15500)
    position_set_y(1,6000)
    overlay_set_size(_g_battle_report_plane,1)
    position_set_x(1,672)
    position_set_y(1,275)
    overlay_set_position(_g_battle_report_plane,1)
    overlay_set_alpha(_g_battle_report_plane,68)
    overlay_set_color(_g_battle_report_plane,1140411)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(_g_presentation_obj_battle_14,1)
    overlay_set_size(_g_presentation_obj_battle_15,1)
    overlay_set_size(_g_presentation_obj_battle_16,1)
    overlay_set_size(_g_presentation_obj_battle_17,1)
    overlay_set_size(_g_presentation_obj_battle_22,1)
    overlay_set_size(_g_presentation_obj_battle_23,1)
    overlay_set_size(_g_presentation_obj_battle_24,1)
    overlay_set_size(_g_presentation_obj_battle_25,1)
    overlay_set_size(_g_presentation_obj_battle_26,1)
    overlay_set_size(_g_presentation_obj_battle_27,1)
    overlay_set_size(_g_presentation_obj_battle_28,1)
    overlay_set_size(_g_battle_us_ready,1)
    overlay_set_size(_g_battle_us_wounded,1)
    overlay_set_size(_g_battle_us_routed,1)
    overlay_set_size(_g_battle_us_dead,1)
    overlay_set_size(_g_battle_enemies_ready,1)
    overlay_set_size(_g_battle_enemies_wounded,1)
    overlay_set_size(_g_battle_enemies_routed,1)
    overlay_set_size(_g_battle_enemies_dead,1)
    overlay_set_size(_g_battle_allies_ready,1)
    overlay_set_size(_g_battle_allies_wounded,1)
    overlay_set_size(_g_battle_allies_routed,1)
    overlay_set_size(_g_battle_allies_dead,1)
    var008 = 675
    var009 = 280
    var008 += 70
    var009 += 90
    position_set_x(1,var008)
    position_set_y(1,var009)
    overlay_set_position(_g_presentation_obj_battle_25,1)
    var008 += 70
    position_set_x(1,var008)
    overlay_set_position(_g_presentation_obj_battle_26,1)
    var008 += 70
    position_set_x(1,var008)
    overlay_set_position(_g_presentation_obj_battle_28,1)
    var008 += 70
    position_set_x(1,var008)
    overlay_set_position(_g_presentation_obj_battle_27,1)
    var008 += -280
    var009 += -30
    position_set_x(1,var008)
    position_set_y(1,var009)
    overlay_set_position(_g_presentation_obj_battle_22,1)
    var009 += -30
    position_set_y(1,var009)
    overlay_set_position(_g_presentation_obj_battle_23,1)
    var009 += -30
    position_set_y(1,var009)
    overlay_set_position(_g_presentation_obj_battle_24,1)
    s2 = get_scene_boundaries(3)
    position_transform_position_to_local(4,2,3)
    set_fixed_point_multiplier(1000)
    pos_x_017 = position_get_x(4)
    pos_y_018 = position_get_y(4)
    set_fixed_point_multiplier(1000)
    var019 = pos_y_018 / 100
    var019 = pos_x_017 / var019
    if var019 > 100:
        _g_battle_map_width = 300
        _g_battle_map_scale = pos_x_017 / _g_battle_map_width
        _g_battle_map_height = pos_y_018 / _g_battle_map_scale
    else:
        _g_battle_map_height = 300
        _g_battle_map_scale = pos_y_018 / _g_battle_map_height
        _g_battle_map_width = pos_x_017 / _g_battle_map_scale
    #end
    create_image_button_overlay(_g_battle_map_plane,mesh.white_plane,mesh.white_plane)
    overlay_set_color(_g_battle_map_plane,0)
    var020 = _g_battle_map_width + 20
    var021 = _g_battle_map_height + 20
    var022 = var020 * 50
    var023 = var021 * 50
    position_set_x(1,var022)
    position_set_y(1,var023)
    overlay_set_size(_g_battle_map_plane,1)
    var024 = 990 - var020
    var025 = 740 - var021
    position_set_x(1,var024)
    position_set_y(1,var025)
    overlay_set_position(_g_battle_map_plane,1)
    overlay_set_alpha(_g_battle_map_plane,68)
    create_mesh_overlay(_g_battle_map_infantry_order_flag,mesh.flag_infantry)
    create_mesh_overlay(_g_battle_map_archers_order_flag,mesh.flag_archers)
    create_mesh_overlay(_g_battle_map_cavalry_order_flag,mesh.flag_cavalry)
    overlay_set_alpha(_g_battle_map_infantry_order_flag,0)
    overlay_set_alpha(_g_battle_map_archers_order_flag,0)
    overlay_set_alpha(_g_battle_map_cavalry_order_flag,0)
    update_order_panel_checked_classes()
    update_order_panel_statistics_and_map()
    presentation_set_duration(999999)
event.codeBlock = code
battle.add_event(event)
event = StateChangedEvent()
def code(var001, var002):
    agent_no_003 = get_player_agent_no()
    agent_team_no_004 = agent_get_team(agent_no_003)
    var005 = 0
    if _group0_has_troops == 1 and var001 == _g_presentation_obj_battle_check0:
        var005 = 1
        _g_formation_group0_selected = var002
        if var002 == 1:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but0,250,68)
        else:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but0,250,0)
        #end
    elif _group1_has_troops == 1 and var001 == _g_presentation_obj_battle_check1:
        var005 = 1
        _g_formation_group1_selected = var002
        if var002 == 1:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but1,250,68)
        else:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but1,250,0)
        #end
    elif _group2_has_troops == 1 and var001 == _g_presentation_obj_battle_check2:
        var005 = 1
        _g_formation_group2_selected = var002
        if var002 == 1:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but2,250,68)
        else:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but2,250,0)
        #end
    elif _group3_has_troops == 1 and var001 == _g_presentation_obj_battle_check3:
        var005 = 1
        _g_formation_group3_selected = var002
        if var002 == 1:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but3,250,68)
        else:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but3,250,0)
        #end
    elif _group4_has_troops == 1 and var001 == _g_presentation_obj_battle_check4:
        var005 = 1
        _g_formation_group4_selected = var002
        if var002 == 1:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but4,250,68)
        else:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but4,250,0)
        #end
    elif _group5_has_troops == 1 and var001 == _g_presentation_obj_battle_check5:
        var005 = 1
        _g_formation_group5_selected = var002
        if var002 == 1:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but5,250,68)
        else:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but5,250,0)
        #end
    elif _group6_has_troops == 1 and var001 == _g_presentation_obj_battle_check6:
        var005 = 1
        _g_formation_group6_selected = var002
        if var002 == 1:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but6,250,68)
        else:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but6,250,0)
        #end
    elif _group7_has_troops == 1 and var001 == _g_presentation_obj_battle_check7:
        var005 = 1
        _g_formation_group7_selected = var002
        if var002 == 1:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but7,250,68)
        else:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but7,250,0)
        #end
    elif _group8_has_troops == 1 and var001 == _g_presentation_obj_battle_check8:
        var005 = 1
        _g_formation_group8_selected = var002
        if var002 == 1:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but8,250,68)
        else:
            overlay_animate_to_alpha(_g_presentation_obj_battle_but8,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but0:
        var005 = 1
        _g_formation_group0_selected = 1
        overlay_animate_to_alpha(_g_presentation_obj_battle_but0,250,68)
        overlay_set_val(_g_presentation_obj_battle_check0,1)
        if _group1_has_troops == 1:
            _g_formation_group1_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check1,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but1,250,0)
        #end
        if _group2_has_troops == 1:
            _g_formation_group2_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check2,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but2,250,0)
        #end
        if _group3_has_troops == 1:
            _g_formation_group3_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check3,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but3,250,0)
        #end
        if _group4_has_troops == 1:
            _g_formation_group4_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check4,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but4,250,0)
        #end
        if _group5_has_troops == 1:
            _g_formation_group5_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check5,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but5,250,0)
        #end
        if _group6_has_troops == 1:
            _g_formation_group6_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check6,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but6,250,0)
        #end
        if _group7_has_troops == 1:
            _g_formation_group7_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check7,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but7,250,0)
        #end
        if _group8_has_troops == 1:
            _g_formation_group8_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check8,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but8,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but1:
        var005 = 1
        _g_formation_group1_selected = 1
        overlay_animate_to_alpha(_g_presentation_obj_battle_but1,250,68)
        overlay_set_val(_g_presentation_obj_battle_check1,1)
        if _group0_has_troops == 1:
            _g_formation_group0_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check0,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but0,250,0)
        #end
        if _group2_has_troops == 1:
            _g_formation_group2_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check2,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but2,250,0)
        #end
        if _group3_has_troops == 1:
            _g_formation_group3_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check3,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but3,250,0)
        #end
        if _group4_has_troops == 1:
            _g_formation_group4_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check4,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but4,250,0)
        #end
        if _group5_has_troops == 1:
            _g_formation_group5_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check5,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but5,250,0)
        #end
        if _group6_has_troops == 1:
            _g_formation_group6_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check6,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but6,250,0)
        #end
        if _group7_has_troops == 1:
            _g_formation_group7_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check7,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but7,250,0)
        #end
        if _group8_has_troops == 1:
            _g_formation_group8_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check8,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but8,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but2:
        var005 = 1
        _g_formation_group2_selected = 1
        overlay_animate_to_alpha(_g_presentation_obj_battle_but2,250,68)
        overlay_set_val(_g_presentation_obj_battle_check2,1)
        if _group0_has_troops == 1:
            _g_formation_group0_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check0,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but0,250,0)
        #end
        if _group1_has_troops == 1:
            _g_formation_group1_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check1,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but1,250,0)
        #end
        if _group3_has_troops == 1:
            _g_formation_group3_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check3,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but3,250,0)
        #end
        if _group4_has_troops == 1:
            _g_formation_group4_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check4,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but4,250,0)
        #end
        if _group5_has_troops == 1:
            _g_formation_group5_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check5,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but5,250,0)
        #end
        if _group6_has_troops == 1:
            _g_formation_group6_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check6,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but6,250,0)
        #end
        if _group7_has_troops == 1:
            _g_formation_group7_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check7,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but7,250,0)
        #end
        if _group8_has_troops == 1:
            _g_formation_group8_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check8,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but8,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but3:
        var005 = 1
        _g_formation_group3_selected = 1
        overlay_animate_to_alpha(_g_presentation_obj_battle_but3,250,68)
        overlay_set_val(_g_presentation_obj_battle_check3,1)
        if _group0_has_troops == 1:
            _g_formation_group0_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check0,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but0,250,0)
        #end
        if _group1_has_troops == 1:
            _g_formation_group1_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check1,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but1,250,0)
        #end
        if _group2_has_troops == 1:
            _g_formation_group2_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check2,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but2,250,0)
        #end
        if _group4_has_troops == 1:
            _g_formation_group4_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check4,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but4,250,0)
        #end
        if _group5_has_troops == 1:
            _g_formation_group5_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check5,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but5,250,0)
        #end
        if _group6_has_troops == 1:
            _g_formation_group6_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check6,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but6,250,0)
        #end
        if _group7_has_troops == 1:
            _g_formation_group7_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check7,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but7,250,0)
        #end
        if _group8_has_troops == 1:
            _g_formation_group8_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check8,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but8,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but4:
        var005 = 1
        _g_formation_group4_selected = 1
        overlay_animate_to_alpha(_g_presentation_obj_battle_but4,250,68)
        overlay_set_val(_g_presentation_obj_battle_check4,1)
        if _group0_has_troops == 1:
            _g_formation_group0_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check0,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but0,250,0)
        #end
        if _group1_has_troops == 1:
            _g_formation_group1_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check1,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but1,250,0)
        #end
        if _group2_has_troops == 1:
            _g_formation_group2_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check2,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but2,250,0)
        #end
        if _group3_has_troops == 1:
            _g_formation_group3_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check3,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but3,250,0)
        #end
        if _group5_has_troops == 1:
            _g_formation_group5_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check5,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but5,250,0)
        #end
        if _group6_has_troops == 1:
            _g_formation_group6_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check6,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but6,250,0)
        #end
        if _group7_has_troops == 1:
            _g_formation_group7_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check7,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but7,250,0)
        #end
        if _group8_has_troops == 1:
            _g_formation_group8_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check8,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but8,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but5:
        var005 = 1
        _g_formation_group5_selected = 1
        overlay_animate_to_alpha(_g_presentation_obj_battle_but5,250,68)
        overlay_set_val(_g_presentation_obj_battle_check5,1)
        if _group0_has_troops == 1:
            _g_formation_group0_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check0,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but0,250,0)
        #end
        if _group1_has_troops == 1:
            _g_formation_group1_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check1,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but1,250,0)
        #end
        if _group2_has_troops == 1:
            _g_formation_group2_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check2,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but2,250,0)
        #end
        if _group3_has_troops == 1:
            _g_formation_group3_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check3,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but3,250,0)
        #end
        if _group4_has_troops == 1:
            _g_formation_group4_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check4,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but4,250,0)
        #end
        if _group6_has_troops == 1:
            _g_formation_group6_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check6,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but6,250,0)
        #end
        if _group7_has_troops == 1:
            _g_formation_group7_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check7,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but7,250,0)
        #end
        if _group8_has_troops == 1:
            _g_formation_group8_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check8,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but8,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but6:
        var005 = 1
        _g_formation_group6_selected = 1
        overlay_animate_to_alpha(_g_presentation_obj_battle_but6,250,68)
        overlay_set_val(_g_presentation_obj_battle_check6,1)
        if _group0_has_troops == 1:
            _g_formation_group0_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check0,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but0,250,0)
        #end
        if _group1_has_troops == 1:
            _g_formation_group1_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check1,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but1,250,0)
        #end
        if _group2_has_troops == 1:
            _g_formation_group2_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check2,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but2,250,0)
        #end
        if _group3_has_troops == 1:
            _g_formation_group3_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check3,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but3,250,0)
        #end
        if _group4_has_troops == 1:
            _g_formation_group4_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check4,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but4,250,0)
        #end
        if _group5_has_troops == 1:
            _g_formation_group5_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check5,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but5,250,0)
        #end
        if _group7_has_troops == 1:
            _g_formation_group7_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check7,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but7,250,0)
        #end
        if _group8_has_troops == 1:
            _g_formation_group8_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check8,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but8,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but7:
        var005 = 1
        _g_formation_group7_selected = 1
        overlay_animate_to_alpha(_g_presentation_obj_battle_but7,250,68)
        overlay_set_val(_g_presentation_obj_battle_check7,1)
        if _group0_has_troops == 1:
            _g_formation_group0_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check0,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but0,250,0)
        #end
        if _group1_has_troops == 1:
            _g_formation_group1_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check1,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but1,250,0)
        #end
        if _group2_has_troops == 1:
            _g_formation_group2_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check2,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but2,250,0)
        #end
        if _group3_has_troops == 1:
            _g_formation_group3_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check3,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but3,250,0)
        #end
        if _group4_has_troops == 1:
            _g_formation_group4_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check4,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but4,250,0)
        #end
        if _group5_has_troops == 1:
            _g_formation_group5_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check5,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but5,250,0)
        #end
        if _group6_has_troops == 1:
            _g_formation_group6_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check6,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but6,250,0)
        #end
        if _group8_has_troops == 1:
            _g_formation_group8_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check8,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but8,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but8:
        var005 = 1
        _g_formation_group8_selected = 1
        overlay_animate_to_alpha(_g_presentation_obj_battle_but8,250,68)
        overlay_set_val(_g_presentation_obj_battle_check8,1)
        if _group0_has_troops == 1:
            _g_formation_group0_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check0,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but0,250,0)
        #end
        if _group1_has_troops == 1:
            _g_formation_group1_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check1,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but1,250,0)
        #end
        if _group2_has_troops == 1:
            _g_formation_group2_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check2,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but2,250,0)
        #end
        if _group3_has_troops == 1:
            _g_formation_group3_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check3,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but3,250,0)
        #end
        if _group4_has_troops == 1:
            _g_formation_group4_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check4,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but4,250,0)
        #end
        if _group5_has_troops == 1:
            _g_formation_group5_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check5,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but5,250,0)
        #end
        if _group6_has_troops == 1:
            _g_formation_group6_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check6,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but6,250,0)
        #end
        if _group7_has_troops == 1:
            _g_formation_group7_selected = 0
            overlay_set_val(_g_presentation_obj_battle_check7,0)
            overlay_animate_to_alpha(_g_presentation_obj_battle_but7,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_14:
        team_give_order_from_order_panel(agent_no_003,8)
    elif var001 == _g_presentation_obj_battle_15:
        team_give_order_from_order_panel(agent_no_003,7)
    elif var001 == _g_presentation_obj_battle_16:
        team_give_order_from_order_panel(agent_no_003,6)
    elif var001 == _g_presentation_obj_battle_17:
        team_give_order_from_order_panel(agent_no_003,5)
    elif var001 == _g_presentation_obj_battle_10:
        if var002 == 3:
            team_give_order_from_order_panel(agent_no_003,0)
            update_order_panel(agent_team_no_004)
            _g_latest_order_1 = 3
        elif var002 == 2:
            team_give_order_from_order_panel(agent_no_003,1)
            update_order_panel(agent_team_no_004)
            _g_latest_order_1 = 2
        elif var002 == 1:
            team_give_order_from_order_panel(agent_no_003,2)
            update_order_panel(agent_team_no_004)
            _g_latest_order_1 = 1
        elif var002 == 0:
            team_give_order_from_order_panel(agent_no_003,11)
            update_order_panel(agent_team_no_004)
            _g_latest_order_1 = 0
        #end
    elif var001 == _g_presentation_obj_battle_11:
        if var002 == 1:
            team_give_order_from_order_panel(agent_no_003,3)
            update_order_panel(agent_team_no_004)
            _g_latest_order_2 = 1
        elif var002 == 0:
            team_give_order_from_order_panel(agent_no_003,4)
            update_order_panel(agent_team_no_004)
            _g_latest_order_2 = 0
        #end
    elif var001 == _g_presentation_obj_battle_12:
        if var002 == 1:
            team_give_order_from_order_panel(agent_no_003,12)
            update_order_panel(agent_team_no_004)
            _g_latest_order_3 = 1
        elif var002 == 0:
            team_give_order_from_order_panel(agent_no_003,13)
            update_order_panel(agent_team_no_004)
            _g_latest_order_3 = 0
        #end
    elif var001 == _g_presentation_obj_battle_13:
        if var002 == 1:
            team_give_order_from_order_panel(agent_no_003,10)
            update_order_panel(agent_team_no_004)
            _g_latest_order_4 = 1
        elif var002 == 0:
            team_give_order_from_order_panel(agent_no_003,9)
            update_order_panel(agent_team_no_004)
            _g_latest_order_4 = 0
        #end
    elif var001 == _g_battle_map_plane:
        s2 = get_scene_boundaries(3)
        pos1 = mouse_get_position	()
        set_fixed_point_multiplier(1000)
        pos_x_006 = position_get_x(1)
        pos_y_007 = position_get_y(1)
        var008 = 980 - _g_battle_map_width
        var009 = 730 - _g_battle_map_height
        pos_x_006 -= var008
        pos_y_007 -= var009
        val_clamp(pos_x_006,0,_g_battle_map_width)
        val_clamp(pos_y_007,0,_g_battle_map_height)
        pos_x_006 *= _g_battle_map_scale
        pos_y_007 *= _g_battle_map_scale
        set_fixed_point_multiplier(1000)
        position_set_x(1,pos_x_006)
        position_set_y(1,pos_y_007)
        position_transform_position_to_parent(3,2,1)
        if _g_formation_group0_selected == 1:
            team_give_order(agent_team_no_004,0,0)
            team_set_order_position(agent_team_no_004,0,3)
        #end
        if _g_formation_group1_selected == 1:
            team_give_order(agent_team_no_004,1,0)
            team_set_order_position(agent_team_no_004,1,3)
        #end
        if _g_formation_group2_selected == 1:
            team_give_order(agent_team_no_004,2,0)
            team_set_order_position(agent_team_no_004,2,3)
        #end
        if _g_formation_group3_selected == 1:
            team_give_order(agent_team_no_004,3,0)
            team_set_order_position(agent_team_no_004,3,3)
        #end
        if _g_formation_group4_selected == 1:
            team_give_order(agent_team_no_004,4,0)
            team_set_order_position(agent_team_no_004,4,3)
        #end
        if _g_formation_group5_selected == 1:
            team_give_order(agent_team_no_004,5,0)
            team_set_order_position(agent_team_no_004,5,3)
        #end
        if _g_formation_group6_selected == 1:
            team_give_order(agent_team_no_004,6,0)
            team_set_order_position(agent_team_no_004,6,3)
        #end
        if _g_formation_group7_selected == 1:
            team_give_order(agent_team_no_004,7,0)
            team_set_order_position(agent_team_no_004,7,3)
        #end
        if _g_formation_group8_selected == 1:
            team_give_order(agent_team_no_004,8,0)
            team_set_order_position(agent_team_no_004,8,3)
        #end
        update_order_flags_on_map()
        update_order_panel(agent_team_no_004)
    #end
    if var005 == 1:
        team_set_order_listener(agent_team_no_004,-1)
        if _g_formation_group0_selected == 1 or _group0_has_troops == 0 and _g_formation_group1_selected == 1 or _group1_has_troops == 0 and _g_formation_group2_selected == 1 or _group2_has_troops == 0 and _g_formation_group3_selected == 1 or _group3_has_troops == 0 and _g_formation_group4_selected == 1 or _group4_has_troops == 0 and _g_formation_group5_selected == 1 or _group5_has_troops == 0 and _g_formation_group6_selected == 1 or _group6_has_troops == 0 and _g_formation_group7_selected == 1 or _group7_has_troops == 0 and _g_formation_group8_selected == 1 or _group8_has_troops == 0:
            team_set_order_listener(agent_team_no_004,9)
        elif _g_formation_group0_selected == 1:
            team_set_order_listener(agent_team_no_004,0,1)
        elif _g_formation_group1_selected == 1:
            team_set_order_listener(agent_team_no_004,1,1)
        elif _g_formation_group2_selected == 1:
            team_set_order_listener(agent_team_no_004,2,1)
        elif _g_formation_group3_selected == 1:
            team_set_order_listener(agent_team_no_004,3,1)
        elif _g_formation_group4_selected == 1:
            team_set_order_listener(agent_team_no_004,4,1)
        elif _g_formation_group5_selected == 1:
            team_set_order_listener(agent_team_no_004,5,1)
        elif _g_formation_group6_selected == 1:
            team_set_order_listener(agent_team_no_004,6,1)
        elif _g_formation_group7_selected == 1:
            team_set_order_listener(agent_team_no_004,7,1)
        elif _g_formation_group8_selected == 1:
            team_set_order_listener(agent_team_no_004,8,1)
        #end
    #end
event.codeBlock = code
battle.add_event(event)
event = MouseEnterLeaveEvent()
def code(var001, var002):
    if var001 == _g_presentation_obj_battle_but0:
        if var002 == 0:
            overlay_animate_to_color(_g_presentation_but0_movement,250,16777215)
            overlay_animate_to_color(_g_presentation_but0_riding,250,16777215)
            overlay_animate_to_color(_g_presentation_but0_weapon_usage,250,16777215)
            overlay_animate_to_color(_g_presentation_obj_battle_name0,250,16777215)
        else:
            overlay_animate_to_color(_g_presentation_but0_movement,250,0)
            overlay_animate_to_color(_g_presentation_but0_riding,250,0)
            overlay_animate_to_color(_g_presentation_but0_weapon_usage,250,0)
            overlay_animate_to_color(_g_presentation_obj_battle_name0,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but1:
        if var002 == 0:
            overlay_animate_to_color(_g_presentation_but1_movement,250,16777215)
            overlay_animate_to_color(_g_presentation_but1_riding,250,16777215)
            overlay_animate_to_color(_g_presentation_but1_weapon_usage,250,16777215)
            overlay_animate_to_color(_g_presentation_obj_battle_name1,250,16777215)
        else:
            overlay_animate_to_color(_g_presentation_but1_movement,250,0)
            overlay_animate_to_color(_g_presentation_but1_riding,250,0)
            overlay_animate_to_color(_g_presentation_but1_weapon_usage,250,0)
            overlay_animate_to_color(_g_presentation_obj_battle_name1,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but2:
        if var002 == 0:
            overlay_animate_to_color(_g_presentation_but2_movement,250,16777215)
            overlay_animate_to_color(_g_presentation_but2_riding,250,16777215)
            overlay_animate_to_color(_g_presentation_but2_weapon_usage,250,16777215)
            overlay_animate_to_color(_g_presentation_obj_battle_name2,250,16777215)
        else:
            overlay_animate_to_color(_g_presentation_but2_movement,250,0)
            overlay_animate_to_color(_g_presentation_but2_riding,250,0)
            overlay_animate_to_color(_g_presentation_but2_weapon_usage,250,0)
            overlay_animate_to_color(_g_presentation_obj_battle_name2,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but3:
        if var002 == 0:
            overlay_animate_to_color(_g_presentation_but3_movement,250,16777215)
            overlay_animate_to_color(_g_presentation_but3_riding,250,16777215)
            overlay_animate_to_color(_g_presentation_but3_weapon_usage,250,16777215)
            overlay_animate_to_color(_g_presentation_obj_battle_name3,250,16777215)
        else:
            overlay_animate_to_color(_g_presentation_but3_movement,250,0)
            overlay_animate_to_color(_g_presentation_but3_riding,250,0)
            overlay_animate_to_color(_g_presentation_but3_weapon_usage,250,0)
            overlay_animate_to_color(_g_presentation_obj_battle_name3,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but4:
        if var002 == 0:
            overlay_animate_to_color(_g_presentation_but4_movement,250,16777215)
            overlay_animate_to_color(_g_presentation_but4_riding,250,16777215)
            overlay_animate_to_color(_g_presentation_but4_weapon_usage,250,16777215)
            overlay_animate_to_color(_g_presentation_obj_battle_name4,250,16777215)
        else:
            overlay_animate_to_color(_g_presentation_but4_movement,250,0)
            overlay_animate_to_color(_g_presentation_but4_riding,250,0)
            overlay_animate_to_color(_g_presentation_but4_weapon_usage,250,0)
            overlay_animate_to_color(_g_presentation_obj_battle_name4,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but5:
        if var002 == 0:
            overlay_animate_to_color(_g_presentation_but5_movement,250,16777215)
            overlay_animate_to_color(_g_presentation_but5_riding,250,16777215)
            overlay_animate_to_color(_g_presentation_but5_weapon_usage,250,16777215)
            overlay_animate_to_color(_g_presentation_obj_battle_name5,250,16777215)
        else:
            overlay_animate_to_color(_g_presentation_but5_movement,250,0)
            overlay_animate_to_color(_g_presentation_but5_riding,250,0)
            overlay_animate_to_color(_g_presentation_but5_weapon_usage,250,0)
            overlay_animate_to_color(_g_presentation_obj_battle_name5,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but6:
        if var002 == 0:
            overlay_animate_to_color(_g_presentation_but6_movement,250,16777215)
            overlay_animate_to_color(_g_presentation_but6_riding,250,16777215)
            overlay_animate_to_color(_g_presentation_but6_weapon_usage,250,16777215)
            overlay_animate_to_color(_g_presentation_obj_battle_name6,250,16777215)
        else:
            overlay_animate_to_color(_g_presentation_but6_movement,250,0)
            overlay_animate_to_color(_g_presentation_but6_riding,250,0)
            overlay_animate_to_color(_g_presentation_but6_weapon_usage,250,0)
            overlay_animate_to_color(_g_presentation_obj_battle_name6,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but7:
        if var002 == 0:
            overlay_animate_to_color(_g_presentation_but7_movement,250,16777215)
            overlay_animate_to_color(_g_presentation_but7_riding,250,16777215)
            overlay_animate_to_color(_g_presentation_but7_weapon_usage,250,16777215)
            overlay_animate_to_color(_g_presentation_obj_battle_name7,250,16777215)
        else:
            overlay_animate_to_color(_g_presentation_but7_movement,250,0)
            overlay_animate_to_color(_g_presentation_but7_riding,250,0)
            overlay_animate_to_color(_g_presentation_but7_weapon_usage,250,0)
            overlay_animate_to_color(_g_presentation_obj_battle_name7,250,0)
        #end
    elif var001 == _g_presentation_obj_battle_but8:
        if var002 == 0:
            overlay_animate_to_color(_g_presentation_but8_movement,250,16777215)
            overlay_animate_to_color(_g_presentation_but8_riding,250,16777215)
            overlay_animate_to_color(_g_presentation_but8_weapon_usage,250,16777215)
            overlay_animate_to_color(_g_presentation_obj_battle_name8,250,16777215)
        else:
            overlay_animate_to_color(_g_presentation_but8_movement,250,0)
            overlay_animate_to_color(_g_presentation_but8_riding,250,0)
            overlay_animate_to_color(_g_presentation_but8_weapon_usage,250,0)
            overlay_animate_to_color(_g_presentation_obj_battle_name8,250,0)
        #end
    #end
event.codeBlock = code
battle.add_event(event)
event = RunEvent()
def code(var001):
    if game_key_clicked(30) or game_key_clicked(31) or game_key_clicked(32) or game_key_clicked(33) or game_key_clicked(34) or game_key_clicked(35) or game_key_clicked(36) or game_key_clicked(37) or game_key_clicked(38) or game_key_clicked(29) or game_key_clicked(39):
        update_order_panel_checked_classes()
    #end
    if game_key_clicked(23) or game_key_clicked(24) or game_key_clicked(25) or game_key_clicked(26) or game_key_clicked(27) or game_key_clicked(28):
        agent_no_002 = get_player_agent_no()
        agent_team_no_003 = agent_get_team(agent_no_002)
        update_order_panel(agent_team_no_003)
    #end
    if var001 > 200 and game_key_clicked(22):
        for cur_agent in __all_agents__:
            agent_set_slot(cur_agent,10,0)
        #end
        presentation_set_duration(0)
    #end
event.codeBlock = code
battle.add_event(event)


sliders = Presentation("sliders")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_slider_overlay(_g_presentation_obj_sliders_1,0,100)
    create_slider_overlay(_g_presentation_obj_sliders_2,0,100)
    create_slider_overlay(_g_presentation_obj_sliders_3,0,100)
    create_slider_overlay(_g_presentation_obj_sliders_4,0,100)
    reg1 = 25
    s1 = str_store_string(gstr.reg1)
    create_text_overlay(_g_presentation_obj_sliders_5,1)
    create_text_overlay(_g_presentation_obj_sliders_6,1)
    create_text_overlay(_g_presentation_obj_sliders_7,1)
    create_text_overlay(_g_presentation_obj_sliders_8,1)
    _g_presentation_obj_sliders_1_val = 25
    overlay_set_val(_g_presentation_obj_sliders_1,25)
    _g_presentation_obj_sliders_2_val = 25
    overlay_set_val(_g_presentation_obj_sliders_2,25)
    _g_presentation_obj_sliders_3_val = 25
    overlay_set_val(_g_presentation_obj_sliders_3,25)
    _g_presentation_obj_sliders_4_val = 25
    overlay_set_val(_g_presentation_obj_sliders_4,25)
    position_set_x(1,600)
    position_set_y(1,200)
    overlay_set_position(_g_presentation_obj_sliders_1,1)
    position_set_y(1,300)
    overlay_set_position(_g_presentation_obj_sliders_2,1)
    position_set_y(1,400)
    overlay_set_position(_g_presentation_obj_sliders_3,1)
    position_set_y(1,500)
    overlay_set_position(_g_presentation_obj_sliders_4,1)
    position_set_x(1,800)
    position_set_y(1,200)
    overlay_set_position(_g_presentation_obj_sliders_5,1)
    position_set_y(1,300)
    overlay_set_position(_g_presentation_obj_sliders_6,1)
    position_set_y(1,400)
    overlay_set_position(_g_presentation_obj_sliders_7,1)
    position_set_y(1,500)
    overlay_set_position(_g_presentation_obj_sliders_8,1)
    position_set_x(1,500)
    overlay_set_size(_g_presentation_obj_sliders_3,1)
event.codeBlock = code
sliders.add_event(event)
event = RunEvent()
def code():
    pass
event.codeBlock = code
sliders.add_event(event)
event = StateChangedEvent()
def code(var001, var002):
    var003 = 0
    if var001 == _g_presentation_obj_sliders_1:
        if _g_presentation_obj_sliders_1_val != var002:
            _g_presentation_obj_sliders_1_val = var002
            var003 = 1
        #end
    elif var001 == _g_presentation_obj_sliders_2:
        if _g_presentation_obj_sliders_2_val != var002:
            _g_presentation_obj_sliders_2_val = var002
            var003 = 1
        #end
    elif var001 == _g_presentation_obj_sliders_3:
        if _g_presentation_obj_sliders_3_val != var002:
            _g_presentation_obj_sliders_3_val = var002
            var003 = 1
        #end
    elif var001 == _g_presentation_obj_sliders_4:
        if _g_presentation_obj_sliders_4_val != var002:
            _g_presentation_obj_sliders_4_val = var002
            var003 = 1
        #end
    #end
    if var003 == 1:
        var004 = 0
        var004 += _g_presentation_obj_sliders_1_val
        var004 += _g_presentation_obj_sliders_2_val
        var004 += _g_presentation_obj_sliders_3_val
        var004 += _g_presentation_obj_sliders_4_val
        var005 = 100 - var004
        var006 = _g_presentation_obj_sliders_1_val
        var007 = _g_presentation_obj_sliders_2_val
        var008 = _g_presentation_obj_sliders_3_val
        var009 = _g_presentation_obj_sliders_4_val
        var010 = 1
        var011 = 0
        var012 = 100
        if var005 < 0:
            var005 *= -1
            var010 = -1
            var011 = 1
            var012 = 101
        #end
        var013 = var004 - var002
        var013 += 30
        for _ in range(0, var005):
            random_x_015 = store_random_in_range(0,var013)
            if var001 != _g_presentation_obj_sliders_1:
                random_x_015 -= _g_presentation_obj_sliders_1_val
                random_x_015 -= 10
                if random_x_015 < 0 and is_between(var006,var011,var012):
                    var006 += var010
                elif var001 != _g_presentation_obj_sliders_2:
                    random_x_015 -= _g_presentation_obj_sliders_2_val
                    random_x_015 -= 10
                    if random_x_015 < 0 and is_between(var007,var011,var012):
                        var007 += var010
                    elif var001 != _g_presentation_obj_sliders_3:
                        random_x_015 -= _g_presentation_obj_sliders_3_val
                        random_x_015 -= 10
                        if random_x_015 < 0 and is_between(var008,var011,var012):
                            var008 += var010
                        elif is_between(var009,var011,var012):
                            var009 += var010
                        else:
                            var005 += 1
                        #end
                    #end
                #end
            #end
        #end
        _g_presentation_obj_sliders_1_val = var006
        _g_presentation_obj_sliders_2_val = var007
        _g_presentation_obj_sliders_3_val = var008
        _g_presentation_obj_sliders_4_val = var009
    #end
    overlay_set_val(_g_presentation_obj_sliders_1,_g_presentation_obj_sliders_1_val)
    overlay_set_val(_g_presentation_obj_sliders_2,_g_presentation_obj_sliders_2_val)
    overlay_set_val(_g_presentation_obj_sliders_3,_g_presentation_obj_sliders_3_val)
    overlay_set_val(_g_presentation_obj_sliders_4,_g_presentation_obj_sliders_4_val)
    reg1 = _g_presentation_obj_sliders_1_val
    s1 = str_store_string(gstr.reg1)
    overlay_set_text(_g_presentation_obj_sliders_5,1)
    reg1 = _g_presentation_obj_sliders_2_val
    s1 = str_store_string(gstr.reg1)
    overlay_set_text(_g_presentation_obj_sliders_6,1)
    reg1 = _g_presentation_obj_sliders_3_val
    s1 = str_store_string(gstr.reg1)
    overlay_set_text(_g_presentation_obj_sliders_7,1)
    reg1 = _g_presentation_obj_sliders_4_val
    s1 = str_store_string(gstr.reg1)
    overlay_set_text(_g_presentation_obj_sliders_8,1)
event.codeBlock = code
sliders.add_event(event)


arena_training = Presentation("arena_training")
arena_training.set_read_only()
arena_training.set_manual_end_only()
event = LoadEvent()
def code():
    presentation_set_duration(999999)
    set_fixed_point_multiplier(1000)
    agent_no_001 = get_player_agent_no()
    reg1 = agent_get_kill_count(agent_no_001,1)
    s1 = str_store_string("@Number of men knocked down: {reg1}")
    create_text_overlay(_g_presentation_obj_arena_training_1,1)
    overlay_set_color(_g_presentation_obj_arena_training_1,16777215)
    position_set_x(1,10)
    position_set_y(1,700)
    overlay_set_position(_g_presentation_obj_arena_training_1,1)
    reg1 = 0
    s1 = str_store_string("@Number of men left: {reg1}")
    create_text_overlay(_g_presentation_obj_arena_training_2,1)
    overlay_set_color(_g_presentation_obj_arena_training_2,16777215)
    position_set_x(1,10)
    position_set_y(1,670)
    overlay_set_position(_g_presentation_obj_arena_training_2,1)
event.codeBlock = code
arena_training.add_event(event)
event = RunEvent()
def code():
    agent_no_001 = get_player_agent_no()
    reg1 = agent_get_kill_count(agent_no_001,1)
    s1 = str_store_string("@Opponents Beaten: {reg1}")
    overlay_set_text(_g_presentation_obj_arena_training_1,1)
    var002 = _g_arena_training_max_opponents
    for cur_agent in __all_agents__:
        if agent_is_human(cur_agent) and not agent_is_alive(cur_agent) and cur_agent != agent_no_001:
            var002 -= 1
        #end
    #end
    reg1 = var002
    s1 = str_store_string("@Opponents Remaining: {reg1}")
    overlay_set_text(_g_presentation_obj_arena_training_2,1)
event.codeBlock = code
arena_training.add_event(event)


retirement = Presentation("retirement", mesh=mesh.load_window)
event = LoadEvent()
def code():
    presentation_set_duration(999999)
    set_fixed_point_multiplier(1000)
    create_button_overlay(_g_presentation_obj_retirement_1,"@Remain in retirement.",16)
    create_button_overlay(_g_presentation_obj_retirement_2,"@Go back to the adventuring.",16)
    position_set_x(1,500)
    position_set_y(1,80)
    overlay_set_position(_g_presentation_obj_retirement_1,1)
    position_set_y(1,40)
    overlay_set_position(_g_presentation_obj_retirement_2,1)
    var001 = 0
    troop_gold_002 = store_troop_gold(trp.player)
    var003 = troop_gold_002 / 200
    var001 += var003
    var004 = 0
    var005 = 0
    var006 = 0
    var007 = 0
    var008 = 0
    var009 = 0
    var010 = 0
    for p_011 in range(p.town_1, p.salt_mine):
        party_slot_012 = party_get_slot(p_011,0)
        if party_slot_eq(p_011,7,trp.player):
            if party_slot_012 == 3:
                var004 += 1
            elif party_slot_012 == 2:
                var005 += 1
            else:
                var006 += 1
            #end
        #end
        party_slot_013 = party_get_slot(p_011,26)
        if party_slot_013 >= 40:
            if party_slot_012 == 3:
                var007 += 1
            elif party_slot_012 == 4:
                var008 += 1
            #end
        elif party_slot_013 <= -40:
            if party_slot_012 == 3:
                var009 += 1
            elif party_slot_012 == 4:
                var010 += 1
            #end
        #end
    #end
    var014 = var004 * 100
    var015 = var005 * 50
    var016 = var006 * 20
    var017 = var004 + var005
    var017 += var006
    var018 = var014 + var015
    var018 += var016
    var001 += var018
    var019 = var007 * 20
    var020 = var008 * 4
    var021 = var007 + var008
    var022 = var019 + var020
    var001 += var022
    var023 = var009 * -40
    var024 = var010 * -8
    var025 = var009 + var010
    var026 = var023 + var024
    var001 += var026
    var027 = 0
    troop_inv_capacity_028 = troop_get_inventory_capacity(trp.player)
    for inventory_slot_no_029 in range(0, troop_inv_capacity_028):
        troop_inv_slot_030 = troop_get_inventory_slot(trp.player,inventory_slot_no_029)
        if troop_inv_slot_030 >= 0:
            item_value_031 = store_item_value(troop_inv_slot_030)
            var027 += item_value_031
        #end
    #end
    var032 = var027 / 200
    var001 += var032
    troop_slot_033 = troop_get_slot(trp.player,7)
    var034 = troop_slot_033 / 1
    var001 += var034
    var035 = 0
    var036 = 0
    for trp_037 in range(trp.npc1, trp.heroes_end):
        if troop_slot_eq(trp_037,2,2) or troop_slot_eq(trp_037,2,6):
            troop_get_player_relation(trp_037)
            party_slot_013 = reg0
            if party_slot_013 >= 40:
                var036 += 1
            elif party_slot_013 <= -40:
                var035 += 1
            #end
        #end
    #end
    var038 = var036 * 10
    var001 += var038
    var039 = var035 * -10
    var001 += var039
    cur_day_040 = store_current_day()
    var041 = cur_day_040 / -1
    var001 += var041
    var042 = _g_total_victories * 2
    var001 += var042
    var043 = _g_total_defeats * -3
    var001 += var043
    var044 = _g_total_quests_completed * 4
    var001 += var044
    troop_xp_045 = troop_get_xp(trp.player)
    var046 = troop_xp_045 / 5000
    var001 += var046
    var047 = 0
    var048 = 0
    for trp_037 in range(trp.npc1, trp.kingdom_1_lord):
        if troop_slot_eq(trp_037,2,5):
            var047 += 1
        elif troop_slot_ge(trp_037,82,1):
            var048 += 1
        #end
    #end
    var049 = var047 / 2
    var001 += var049
    var050 = var048 / -4
    var001 += var050
    average_game_difficulty = get_average_game_difficulty()
    var052 = var001
    var001 *= average_game_difficulty
    var001 /= 75
    var001 *= average_game_difficulty
    var001 /= 75
    var052 = var001 - var052
    reg5 = cur_day_040
    reg4 = store_character_level(trp.player)
    create_text_overlay(reg1,"@You have retired at level {reg4} after {reg5} days of adventuring.",16)
    position_set_x(1,700)
    position_set_y(1,700)
    overlay_set_position(reg1,1)
    position_set_x(1,950)
    position_set_y(1,950)
    overlay_set_size(reg1,1)
    create_text_overlay(reg2,"@Effect on Score",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg2,1)
    position_set_x(1,850)
    position_set_y(1,670)
    overlay_set_position(reg2,1)
    reg0 = var017
    create_text_overlay(reg1,"@Settlements owned by you: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,650)
    overlay_set_position(reg1,1)
    reg0 = var018
    create_text_overlay(reg1,"@{!}{reg0?+:}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,650)
    overlay_set_position(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    #end
    reg0 = var021
    create_text_overlay(reg1,"@Friendly Settlements: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,630)
    overlay_set_position(reg1,1)
    reg0 = var022
    create_text_overlay(reg1,"@{!}{reg0?+:}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,630)
    overlay_set_position(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    #end
    reg0 = var025
    create_text_overlay(reg1,"@Hostile Settlements: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,610)
    overlay_set_position(reg1,1)
    reg0 = var026
    create_text_overlay(reg1,"@{!}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,610)
    overlay_set_position(reg1,1)
    if reg0 < 0:
        overlay_set_color(reg1,16711680)
    #end
    reg0 = var036
    create_text_overlay(reg1,"@Friendly Lords: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,590)
    overlay_set_position(reg1,1)
    reg0 = var038
    create_text_overlay(reg1,"@{!}{reg0?+:}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,590)
    overlay_set_position(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    #end
    reg0 = var035
    create_text_overlay(reg1,"@Enemy Lords: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,570)
    overlay_set_position(reg1,1)
    reg0 = var039
    create_text_overlay(reg1,"@{!}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,570)
    overlay_set_position(reg1,1)
    if reg0 < 0:
        overlay_set_color(reg1,16711680)
    #end
    reg0 = _g_total_victories
    create_text_overlay(reg1,"@Victories: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,550)
    overlay_set_position(reg1,1)
    reg0 = var042
    create_text_overlay(reg1,"@{!}{reg0?+:}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,550)
    overlay_set_position(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    #end
    reg0 = _g_total_defeats
    create_text_overlay(reg1,"@Defeats: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,530)
    overlay_set_position(reg1,1)
    reg0 = var043
    create_text_overlay(reg1,"@{!}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,530)
    overlay_set_position(reg1,1)
    if reg0 < 0:
        overlay_set_color(reg1,16711680)
    #end
    reg0 = _g_total_quests_completed
    create_text_overlay(reg1,"@Quests Completed: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,510)
    overlay_set_position(reg1,1)
    reg0 = var044
    create_text_overlay(reg1,"@{!}{reg0?+:}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,510)
    overlay_set_position(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    #end
    reg0 = var047
    create_text_overlay(reg1,"@Companions Found: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,490)
    overlay_set_position(reg1,1)
    reg0 = var049
    create_text_overlay(reg1,"@{!}{reg0?+:}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,490)
    overlay_set_position(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    #end
    reg0 = var048
    create_text_overlay(reg1,"@Companions Lost/Departed: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,470)
    overlay_set_position(reg1,1)
    reg0 = var050
    create_text_overlay(reg1,"@{!}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,470)
    overlay_set_position(reg1,1)
    if reg0 < 0:
        overlay_set_color(reg1,16711680)
    #end
    reg0 = troop_gold_002
    create_text_overlay(reg1,"@Wealth: {reg0} denars",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,450)
    overlay_set_position(reg1,1)
    reg0 = var003
    create_text_overlay(reg1,"@{!}{reg0?+:}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,450)
    overlay_set_position(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    #end
    reg0 = var027
    create_text_overlay(reg1,"@Inventory: {reg0} denars",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,430)
    overlay_set_position(reg1,1)
    reg0 = var032
    create_text_overlay(reg1,"@{!}{reg0?+:}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,430)
    overlay_set_position(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    #end
    reg0 = troop_slot_033
    create_text_overlay(reg1,"@Renown: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,410)
    overlay_set_position(reg1,1)
    reg0 = var034
    create_text_overlay(reg1,"@{!}{reg0?+:}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,410)
    overlay_set_position(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    #end
    reg0 = troop_xp_045
    create_text_overlay(reg1,"@Experience: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,390)
    overlay_set_position(reg1,1)
    reg0 = var046
    create_text_overlay(reg1,"@{!}{reg0?+:}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,390)
    overlay_set_position(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    #end
    reg0 = cur_day_040
    create_text_overlay(reg1,"@Days Passed: {reg0}",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,370)
    overlay_set_position(reg1,1)
    reg0 = var041
    create_text_overlay(reg1,"@{!}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,370)
    overlay_set_position(reg1,1)
    if reg0 < 0:
        overlay_set_color(reg1,16711680)
    #end
    reg0 = average_game_difficulty
    create_text_overlay(reg1,"@Difficulty: {reg0}%",0)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,600)
    position_set_y(1,350)
    overlay_set_position(reg1,1)
    reg0 = var052
    reg3 = reg0
    val_max(reg3,0)
    create_text_overlay(reg1,"@{!}{reg3?+:}{reg0}",16)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg1,1)
    position_set_x(1,850)
    position_set_y(1,350)
    overlay_set_position(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    elif reg0 < 0:
        overlay_set_color(reg1,16711680)
    #end
    reg0 = var001
    create_text_overlay(reg1,"@TOTAL SCORE: {reg0}",16)
    position_set_x(1,750)
    position_set_y(1,320)
    overlay_set_position(reg1,1)
    var053 = 0
    var054 = 0
    var055 = 0
    var056 = 0
    var057 = 0
    var058 = 0
    for p_059 in range(p.town_1, p.salt_mine):
        if party_slot_eq(p_059,7,trp.player):
            if party_slot_eq(p_059,0,3):
                var055 += 1
            elif party_slot_eq(p_059,0,2):
                var054 += 1
            else:
                var053 += 1
            #end
        else:
            party_slot_060 = party_get_slot(p_059,26)
            if party_slot_060 > 0:
                if party_slot_eq(p_059,0,3):
                    var058 += party_slot_060
                elif party_slot_eq(p_059,0,2):
                    var057 += party_slot_060
                else:
                    var056 += party_slot_060
                #end
            #end
        #end
    #end
    if var055 > 0:
        random_x_061 = store_random_in_range(0,var055)
        for p_059 in range(p.town_1, p.castle_1):
            if party_slot_eq(p_059,7,trp.player):
                random_x_061 -= 1
                if random_x_061 < 0:
                    s9 = str_store_party_name(p_059)
                #end
            #end
        #end
    elif var058 > 0:
        random_x_062 = store_random_in_range(0,var058)
        for p_059 in range(p.town_1, p.castle_1):
            party_slot_060 = party_get_slot(p_059,26)
            if party_slot_060 > 0:
                random_x_062 -= party_slot_060
                if random_x_062 < 0:
                    s9 = str_store_party_name(p_059)
                #end
            #end
        #end
    else:
        random_x_061 = store_random_in_range(p.town_1,p.castle_1)
        s9 = str_store_party_name(random_x_061)
    #end
    if var054 > 0:
        random_x_063 = store_random_in_range(0,var054)
        for p_059 in range(p.castle_1, p.village_1):
            if party_slot_eq(p_059,7,trp.player):
                random_x_063 -= 1
                if random_x_063 < 0:
                    s8 = str_store_party_name(p_059)
                #end
            #end
        #end
    elif var057 > 0:
        random_x_064 = store_random_in_range(0,var057)
        for p_059 in range(p.castle_1, p.village_1):
            party_slot_060 = party_get_slot(p_059,26)
            if party_slot_060 > 0:
                random_x_064 -= party_slot_060
                if random_x_064 < 0:
                    s8 = str_store_party_name(p_059)
                #end
            #end
        #end
    else:
        random_x_063 = store_random_in_range(p.castle_1,p.village_1)
        s8 = str_store_party_name(random_x_063)
    #end
    if var053 > 0:
        random_x_065 = store_random_in_range(0,var053)
        for p_059 in range(p.village_1, p.salt_mine):
            if party_slot_eq(p_059,7,trp.player):
                random_x_065 -= 1
                if random_x_065 < 0:
                    s7 = str_store_party_name(p_059)
                #end
            #end
        #end
    elif var056 > 0:
        random_x_066 = store_random_in_range(0,var056)
        for p_059 in range(p.village_1, p.salt_mine):
            party_slot_060 = party_get_slot(p_059,26)
            if party_slot_060 > 0:
                random_x_066 -= party_slot_060
                if random_x_066 < 0:
                    s7 = str_store_party_name(p_059)
                #end
            #end
        #end
    else:
        random_x_065 = store_random_in_range(p.village_1,p.salt_mine)
        s7 = str_store_party_name(random_x_065)
    #end
    if var001 < 100:
        create_mesh_overlay_with_tableau_material(reg1,-1,tableau.retirement_troop,0)
        s0 = str_store_string(gstr.retirement_text_1)
    elif var001 < 200:
        create_mesh_overlay_with_tableau_material(reg1,-1,tableau.retirement_troop,1)
        s0 = str_store_string(gstr.retirement_text_2)
    elif var001 < 400:
        create_mesh_overlay_with_tableau_material(reg1,-1,tableau.retirement_troop,2)
        s0 = str_store_string(gstr.retirement_text_3)
    elif var001 < 700:
        create_mesh_overlay_with_tableau_material(reg1,-1,tableau.retirement_troop,3)
        s0 = str_store_string(gstr.retirement_text_4)
    elif var001 < 1200:
        create_mesh_overlay_with_tableau_material(reg1,-1,tableau.retirement_troop,4)
        s0 = str_store_string(gstr.retirement_text_5)
    elif var001 < 1850:
        create_mesh_overlay_with_tableau_material(reg1,-1,tableau.retirement_troop,5)
        s0 = str_store_string(gstr.retirement_text_6)
    elif var001 < 2500:
        create_mesh_overlay_with_tableau_material(reg1,-1,tableau.retirement_troop,6)
        s0 = str_store_string(gstr.retirement_text_7)
    elif var001 < 3500:
        create_mesh_overlay_with_tableau_material(reg1,-1,tableau.retirement_troop,7)
        s0 = str_store_string(gstr.retirement_text_8)
    elif var001 < 5000:
        create_mesh_overlay_with_tableau_material(reg1,-1,tableau.retirement_troop,8)
        s0 = str_store_string(gstr.retirement_text_9)
    else:
        create_mesh_overlay_with_tableau_material(reg1,-1,tableau.retirement_troop,9)
        s0 = str_store_string(gstr.retirement_text_10)
    #end
    position_set_x(1,0)
    position_set_y(1,120)
    overlay_set_position(reg1,1)
    create_text_overlay(reg1,0,10240)
    position_set_x(1,600)
    position_set_y(1,120)
    overlay_set_position(reg1,1)
    position_set_x(1,360)
    position_set_y(1,190)
    overlay_set_area_size(reg1,1)
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(reg1,1)
event.codeBlock = code
retirement.add_event(event)
event = StateChangedEvent()
def code(var001):
    if var001 == _g_presentation_obj_retirement_1:
        jump_to_menu(mnu.end_game)
        start_presentation(prsnt.game_credits)
    elif var001 == _g_presentation_obj_retirement_2:
        presentation_set_duration(0)
        change_screen_return()
    #end
event.codeBlock = code
retirement.add_event(event)


budget_report = Presentation("budget_report", mesh=mesh.load_window)
event = LoadEvent()
def code():
    presentation_set_duration(999999)
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(reg1,mesh.pic_payment)
    position_set_x(1,800)
    position_set_y(1,800)
    overlay_set_size(reg1,1)
    position_set_x(1,170)
    position_set_y(1,0)
    overlay_set_position(reg1,1)
    create_text_overlay(reg1,gstr.weekly_budget,16)
    position_set_x(1,1500)
    position_set_y(1,1500)
    overlay_set_size(reg1,1)
    position_set_x(1,260)
    position_set_y(1,650)
    overlay_set_position(reg1,1)
    str_clear(0)
    create_text_overlay(_g_presentation_obj_bugdet_report_container,0,131072)
    position_set_x(1,0)
    position_set_y(1,100)
    overlay_set_position(_g_presentation_obj_bugdet_report_container,1)
    position_set_x(1,505)
    position_set_y(1,500)
    overlay_set_area_size(_g_presentation_obj_bugdet_report_container,1)
    set_container_overlay(_g_presentation_obj_bugdet_report_container)
    campaign_ai = game_get_reduce_campaign_ai()
    if campaign_ai == 0:
        var002 = 2
        var003 = 5
    elif campaign_ai == 1:
        var002 = 4
        var003 = 4
    elif campaign_ai == 2:
        var002 = 6
        var003 = 3
    #end
    var004 = 0
    var005 = 0
    var006 = 0
    var007 = 0
    for p_008 in range(p.town_1, p.salt_mine):
        if party_slot_ge(p_008,137,1):
            var004 += 1
        #end
        if party_slot_eq(p_008,7,trp.player):
            var004 += 1
            var005 += 1
            if is_between(p_008,p.town_1,p.castle_1):
                var004 += 1
                var005 += 1
            #end
        #end
    #end
    if _players_kingdom > 0 and _players_kingdom != fac.player_supporters_faction and _players_kingdom != fac.player_faction and _player_has_homage == 0:
        var004 += 1
    #end
    if var005 > var002:
        var004 += 1
    #end
    for cur_party in __all_parties__:
        var010 = 0
        if party_slot_eq(cur_party,0,3) or party_slot_eq(cur_party,0,2) and party_slot_eq(cur_party,7,trp.player):
            var010 = 1
        elif party_slot_eq(cur_party,0,3) or party_slot_eq(cur_party,0,2) and not party_slot_ge(cur_party,7,1):
            party_faction_011 = store_faction_of_party(cur_party)
            if party_faction_011 == fac.player_supporters_faction and faction_slot_eq(fac.player_supporters_faction,11,trp.player):
                var010 = 1
            #end
        #end
        if cur_party == p.main_party or var010 == 1:
            var004 += 1
        #end
    #end
    if _g_player_debt_to_party_members > 0:
        var004 += 2
    #end
    var004 += 3
    var012 = 27 * var004
    var013 = 0
    for p_008 in range(p.town_1, p.salt_mine):
        if True:
            party_slot_014 = party_get_slot(p_008,137)
            if party_slot_014 > 1 and not party_slot_ge(p_008,139,1):
                s0 = str_store_party_name(p_008)
                process_player_enterprise(party_slot_014,p_008)
                var015 = reg0
                var016 = reg4
                var017 = reg5
                var018 = reg10
                var019 = p_008 - p.town_1
                troop_id_020 = var019 + trp.town_1_master_craftsman
                item_slot_021 = item_get_slot(party_slot_014,55)
                add_amount_022 = 0
                if party_slot_eq(p_008,138,1):
                    var023 = 0
                    troop_inv_capacity_024 = troop_get_inventory_capacity(troop_id_020)
                    for inventory_slot_no_025 in range(0, troop_inv_capacity_024):
                        troop_inv_slot_026 = troop_get_inventory_slot(troop_id_020,inventory_slot_no_025)
                        if troop_inv_slot_026 < 1:
                            var023 += 1
                        #end
                    #end
                #end
                add_amount_022 = item_slot_021
                val_min(add_amount_022,var023)
                if add_amount_022 > 0:
                    var027 = var016 * add_amount_022
                    var015 -= var027
                    item_slot_021 -= add_amount_022
                #end
            #end
            if _g_apply_budget_report_to_gold == 1:
                troop_add_items(troop_id_020,party_slot_014,add_amount_022)
                slot_no_028 = party_slot_014 - itm.spice
                slot_no_028 += 250
                party_slot_029 = party_get_slot(p_008,slot_no_028)
                var030 = item_slot_021 * 15
                party_slot_029 -= var030
                party_set_slot(p_008,slot_no_028,party_slot_029)
                if _cheat_mode > 0:
                    s3 = str_store_troop_name(troop_id_020)
                    reg3 = add_amount_022
                    print("@{!}DEBUG -- Adding {reg3} items to {s3}")
                #end
            #end
            item_slot_031 = item_get_slot(party_slot_014,52)
            if item_slot_ge(party_slot_014,57,1):
                var032 = item_slot_031
            else:
                var032 = 0
            #end
            remove_amount_033 = 0
            remove_amount_034 = 0
            if True:
                troop_inv_capacity_024 = troop_get_inventory_capacity(troop_id_020)
                for inventory_slot_no_025 in range(0, troop_inv_capacity_024):
                    troop_inv_slot_035 = troop_get_inventory_slot(troop_id_020,inventory_slot_no_025)
                    if remove_amount_033 < item_slot_031 and item_slot_eq(party_slot_014,50,troop_inv_slot_035):
                        remove_amount_033 += 1
                    elif remove_amount_034 < var032 and item_slot_eq(party_slot_014,57,troop_inv_slot_035):
                        remove_amount_034 += 1
                    #end
                #end
                if remove_amount_033 > 0:
                    item_slot_031 -= remove_amount_033
                    var036 = var017 * remove_amount_033
                    var015 += var036
                #end
                if remove_amount_034 > 0:
                    var032 -= remove_amount_034
                    var036 = var018
                    var015 += var036
                #end
            #end
            if _g_apply_budget_report_to_gold == 1:
                item_slot_037 = item_get_slot(party_slot_014,50)
                troop_remove_items(troop_id_020,item_slot_037,remove_amount_033)
                item_slot_038 = item_get_slot(party_slot_014,57)
                troop_remove_items(troop_id_020,item_slot_038,remove_amount_034)
                slot_no_028 = item_slot_037 - itm.spice
                slot_no_028 += 250
                party_slot_029 = party_get_slot(p_008,slot_no_028)
                var030 = item_slot_021 * 15
                party_slot_029 += var030
                party_set_slot(p_008,slot_no_028,party_slot_029)
                if var032 > 0:
                    slot_no_028 = item_slot_038 - itm.spice
                    slot_no_028 += 250
                    party_slot_029 = party_get_slot(p_008,slot_no_028)
                    party_slot_029 += 15
                    party_set_slot(p_008,slot_no_028,party_slot_029)
                #end
            #end
            get_enterprise_name(party_slot_014)
            s5 = str_store_string(reg0)
            create_text_overlay(reg1,gstr.enterprise_s5_at_s0,0)
            position_set_x(1,900)
            position_set_y(1,900)
            overlay_set_size(reg1,1)
            position_set_x(1,25)
            position_set_y(1,var012)
            overlay_set_position(reg1,1)
            reg0 = var015
            if True:
                party_faction_039 = store_faction_of_party(p_008)
                faction_relation_040 = store_relation(party_faction_039,_players_kingdom)
                if faction_relation_040 < 0:
                    reg0 = 0
                    var015 = 0
                    create_text_overlay(reg1,gstr.under_sequestration,32776)
                    overlay_set_color(reg1,16711680)
                elif reg0 >= 0:
                    create_text_overlay(reg1,"@{!}{reg0}",32776)
                    overlay_set_color(reg1,43520)
                else:
                    create_text_overlay(reg1,"@{!}{reg0}",32776)
                    overlay_set_color(reg1,16711680)
                #end
            #end
            var006 += var015
            var013 += var015
            position_set_x(1,900)
            position_set_y(1,900)
            overlay_set_size(reg1,1)
            position_set_x(1,500)
            position_set_y(1,var012)
            overlay_set_position(reg1,1)
            var012 -= 27
        #end
        if party_slot_eq(p_008,7,trp.player):
            party_slot_041 = party_get_slot(p_008,47)
            party_slot_042 = party_get_slot(p_008,48)
            var043 = party_slot_041 + party_slot_042
            var006 += var043
            var007 += var043
            var013 += var043
            s0 = str_store_party_name(p_008)
            create_text_overlay(reg1,gstr.rents_from_s0,0)
            position_set_x(1,900)
            position_set_y(1,900)
            overlay_set_size(reg1,1)
            position_set_x(1,25)
            position_set_y(1,var012)
            overlay_set_position(reg1,1)
            if party_slot_041 > 0:
                reg0 = party_slot_041
                create_text_overlay(reg1,"@{!}{reg0}",32776)
                overlay_set_color(reg1,43520)
            else:
                create_text_overlay(reg1,"@None",32776)
            #end
        #end
        position_set_x(1,900)
        position_set_y(1,900)
        overlay_set_size(reg1,1)
        position_set_x(1,500)
        position_set_y(1,var012)
        overlay_set_position(reg1,1)
        var012 -= 27
        if is_between(p_008,p.town_1,p.castle_1):
            create_text_overlay(reg1,gstr.tariffs_from_s0,0)
            position_set_x(1,900)
            position_set_y(1,900)
            overlay_set_size(reg1,1)
            position_set_x(1,25)
            position_set_y(1,var012)
            overlay_set_position(reg1,1)
            if party_slot_042 > 0:
                reg0 = party_slot_042
                create_text_overlay(reg1,"@{!}{reg0}",32776)
                overlay_set_color(reg1,43520)
            else:
                create_text_overlay(reg1,"@None",32776)
            #end
            position_set_x(1,900)
            position_set_y(1,900)
            overlay_set_size(reg1,1)
            position_set_x(1,500)
            position_set_y(1,var012)
            overlay_set_position(reg1,1)
            var012 -= 27
        #end
    #end
    if _players_kingdom > 0 and _players_kingdom != fac.player_supporters_faction and _players_kingdom != fac.player_faction and _player_has_homage == 0:
        s0 = str_store_faction_name(_players_kingdom)
        create_text_overlay(reg1,gstr.mercenary_payment_from_s0,0)
        position_set_x(1,900)
        position_set_y(1,900)
        overlay_set_size(reg1,1)
        position_set_x(1,25)
        position_set_y(1,var012)
        overlay_set_position(reg1,1)
        party_calculate_strength(p.main_party,0)
        var044 = reg0
        var044 /= 2
        var044 += 30
        round_value(var044)
        var013 += reg0
        create_text_overlay(reg1,"@{!}{reg0}",32776)
        position_set_x(1,900)
        position_set_y(1,900)
        overlay_set_size(reg1,1)
        overlay_set_color(reg1,43520)
        position_set_x(1,500)
        position_set_y(1,var012)
        overlay_set_position(reg1,1)
        var012 -= 27
    #end
    if var005 > var002 and var006 > 0:
        var045 = var005 - var002
        var045 *= var003
        val_min(var045,65)
        var046 = var007 * var045
        var046 /= 100
        var013 -= var046
        create_text_overlay(reg1,gstr.loss_due_to_tax_inefficiency,0)
        position_set_x(1,25)
        position_set_y(1,var012)
        overlay_set_position(reg1,1)
        position_set_x(1,900)
        position_set_y(1,900)
        overlay_set_size(reg1,1)
        reg0 = var046 * -1
        create_text_overlay(reg1,"@{!}{reg0}",32776)
        position_set_x(1,900)
        position_set_y(1,900)
        overlay_set_size(reg1,1)
        overlay_set_color(reg1,16711680)
        position_set_x(1,500)
        position_set_y(1,var012)
        overlay_set_position(reg1,1)
        var012 -= 27
    #end
    for cur_party in __all_parties__:
        var010 = 0
        if party_slot_eq(cur_party,0,3) or party_slot_eq(cur_party,0,2) and party_slot_eq(cur_party,7,trp.player):
            var010 = 1
        elif party_slot_eq(cur_party,0,3) or party_slot_eq(cur_party,0,2) and not party_slot_ge(cur_party,7,1):
            party_faction_011 = store_faction_of_party(cur_party)
            if party_faction_011 == fac.player_supporters_faction and faction_slot_eq(fac.player_supporters_faction,11,trp.player):
                var010 = 1
            #end
        #end
        if cur_party == p.main_party or var010 == 1:
            var047 = 0
            party_num_companions_stacks_048 = party_get_num_companion_stacks(cur_party)
            for stack_no_049 in range(0, party_num_companions_stacks_048):
                troop_id_050 = party_stack_get_troop_id(cur_party,stack_no_049)
                party_stack_size_051 = party_stack_get_size(cur_party,stack_no_049)
                game_get_troop_wage(troop_id_050,cur_party)
                var052 = reg0
                var052 *= party_stack_size_051
                var047 += var052
            #end
        #end
        if var010 == 1:
            var047 /= 2
        elif cur_party == p.main_party:
            var053 = 14 - _g_cur_week_half_daily_wage_payments
            var047 *= var053
            var047 /= 14
        #end
        var047 *= -1
        var013 += var047
        s0 = str_store_party_name(cur_party)
        if cur_party == p.main_party:
            s0 = str_store_string(gstr.s0s_party)
        #end
        create_text_overlay(reg1,gstr.wages_for_s0,0)
        position_set_x(1,900)
        position_set_y(1,900)
        overlay_set_size(reg1,1)
        position_set_x(1,25)
        position_set_y(1,var012)
        overlay_set_position(reg1,1)
        if var047 < 0:
            reg0 = var047
            create_text_overlay(reg1,"@{!}{reg0}",32776)
            overlay_set_color(reg1,16711680)
        else:
            create_text_overlay(reg1,"@None",32776)
        #end
        position_set_x(1,900)
        position_set_y(1,900)
        overlay_set_size(reg1,1)
        position_set_x(1,500)
        position_set_y(1,var012)
        overlay_set_position(reg1,1)
        var012 -= 27
    #end
    if _g_player_debt_to_party_members > 0:
        var013 -= _g_player_debt_to_party_members
        create_text_overlay(reg1,gstr.earlier_debts,0)
        position_set_x(1,900)
        position_set_y(1,900)
        overlay_set_size(reg1,1)
        position_set_x(1,25)
        position_set_y(1,var012)
        overlay_set_position(reg1,1)
        reg0 = _g_player_debt_to_party_members * -1
        create_text_overlay(reg1,"@{!}{reg0}",32776)
        position_set_x(1,900)
        position_set_y(1,900)
        overlay_set_size(reg1,1)
        overlay_set_color(reg1,16711680)
        position_set_x(1,500)
        position_set_y(1,var012)
        overlay_set_position(reg1,1)
        var012 -= 27
    #end
    create_mesh_overlay(reg1,mesh.white_plane)
    overlay_set_color(reg1,0)
    position_set_x(1,24000)
    position_set_y(1,50)
    overlay_set_size(reg1,1)
    position_set_x(1,25)
    var054 = var012 + 25
    position_set_y(1,var054)
    overlay_set_position(reg1,1)
    create_text_overlay(reg1,gstr.net_change,0)
    position_set_x(1,900)
    position_set_y(1,900)
    overlay_set_size(reg1,1)
    position_set_x(1,25)
    position_set_y(1,var012)
    overlay_set_position(reg1,1)
    reg0 = var013
    create_text_overlay(reg1,"@{!}{reg0}",32776)
    position_set_x(1,900)
    position_set_y(1,900)
    overlay_set_size(reg1,1)
    if reg0 > 0:
        overlay_set_color(reg1,43520)
    elif reg0 < 0:
        overlay_set_color(reg1,16711680)
    #end
    position_set_x(1,500)
    position_set_y(1,var012)
    overlay_set_position(reg1,1)
    var012 -= 27
    create_text_overlay(reg1,gstr.earlier_wealth,0)
    position_set_x(1,900)
    position_set_y(1,900)
    overlay_set_size(reg1,1)
    position_set_x(1,25)
    position_set_y(1,var012)
    overlay_set_position(reg1,1)
    troop_gold_055 = store_troop_gold(trp.player)
    reg0 = troop_gold_055
    create_text_overlay(reg1,"@{!}{reg0}",32776)
    position_set_x(1,900)
    position_set_y(1,900)
    overlay_set_size(reg1,1)
    position_set_x(1,500)
    position_set_y(1,var012)
    overlay_set_position(reg1,1)
    var012 -= 27
    var013 *= -1
    if troop_gold_055 >= var013:
        gold_056 = var013
        var057 = 0
    else:
        gold_056 = troop_gold_055
        var057 = var013 - troop_gold_055
    #end
    create_text_overlay(reg1,gstr.new_wealth,0)
    position_set_x(1,900)
    position_set_y(1,900)
    overlay_set_size(reg1,1)
    position_set_x(1,25)
    position_set_y(1,var012)
    overlay_set_position(reg1,1)
    reg0 = troop_gold_055 - gold_056
    create_text_overlay(reg1,"@{!}{reg0}",32776)
    position_set_x(1,900)
    position_set_y(1,900)
    overlay_set_size(reg1,1)
    position_set_x(1,500)
    position_set_y(1,var012)
    overlay_set_position(reg1,1)
    var012 -= 27
    if var057 > 0:
        create_text_overlay(reg1,gstr.new_debts,0)
        position_set_x(1,900)
        position_set_y(1,900)
        overlay_set_size(reg1,1)
        position_set_x(1,25)
        position_set_y(1,var012)
        overlay_set_position(reg1,1)
        reg0 = var057
        create_text_overlay(reg1,"@{!}{reg0}",32776)
        position_set_x(1,900)
        position_set_y(1,900)
        overlay_set_size(reg1,1)
        position_set_x(1,500)
        position_set_y(1,var012)
        overlay_set_position(reg1,1)
        var012 -= 27
        if _g_apply_budget_report_to_gold != 0:
            objectionable_action(2,gstr.men_unpaid)
        #end
    #end
    set_container_overlay(-1)
    create_button_overlay(_g_presentation_obj_budget_report_1,"@Continue...")
    position_set_x(1,225)
    position_set_y(1,60)
    overlay_set_position(_g_presentation_obj_budget_report_1,1)
    if _g_apply_budget_report_to_gold == 1:
        _g_player_debt_to_party_members = var057
        if gold_056 > 0:
            troop_remove_gold(trp.player,gold_056)
        else:
            gold_056 *= -1
            troop_add_gold(trp.player,gold_056)
        #end
        for p_008 in range(p.town_1, p.salt_mine):
            if party_slot_eq(p_008,7,trp.player):
                party_set_slot(p_008,47,0)
                party_set_slot(p_008,48,0)
            #end
        #end
        _g_cur_week_half_daily_wage_payments = 0
    #end
event.codeBlock = code
budget_report.add_event(event)
event = StateChangedEvent()
def code(var001):
    if var001 == _g_presentation_obj_budget_report_1:
        presentation_set_duration(0)
    #end
event.codeBlock = code
budget_report.add_event(event)


game_before_quit = Presentation("game_before_quit", mesh=mesh.load_window)
event = LoadEvent()
def code():
    if is_trial_version():
        set_fixed_point_multiplier(1000)
        create_mesh_overlay(reg0,mesh.quit_adv)
        position_set_x(1,-1)
        position_set_y(1,-1)
        overlay_set_position(reg0,1)
        position_set_x(1,1002)
        position_set_y(1,1002)
        overlay_set_size(reg0,1)
        _g_game_before_quit_state = 0
        presentation_set_duration(999999)
    #end
event.codeBlock = code
game_before_quit.add_event(event)
event = RunEvent()
def code(var001):
    if var001 > 500:
        if key_clicked(57) or key_clicked(28) or key_clicked(1) or key_clicked(14) or key_clicked(224) or key_clicked(225) or key_clicked(252) or key_clicked(253):
            if _g_game_before_quit_state == 0:
                _g_game_before_quit_state += 1
                create_mesh_overlay(reg0,mesh.quit_adv_b)
                position_set_x(1,-1)
                position_set_y(1,-1)
                overlay_set_position(reg0,1)
                position_set_x(1,1002)
                position_set_y(1,1002)
                overlay_set_size(reg0,1)
            else:
                presentation_set_duration(0)
            #end
        #end
    #end
event.codeBlock = code
game_before_quit.add_event(event)


multiplayer_duel_start_counter = Presentation("multiplayer_duel_start_counter")
multiplayer_duel_start_counter.set_read_only()
multiplayer_duel_start_counter.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    _g_multiplayer_duel_start_counter_overlay = -1
    _g_multiplayer_last_duel_start_counter_value = -1
    str_clear(0)
    create_text_overlay(_g_multiplayer_duel_start_counter_overlay,0,65552)
    overlay_set_color(_g_multiplayer_duel_start_counter_overlay,16777215)
    position_set_x(1,500)
    position_set_y(1,600)
    overlay_set_position(_g_multiplayer_duel_start_counter_overlay,1)
    position_set_x(1,2000)
    position_set_y(1,2000)
    overlay_set_size(_g_multiplayer_duel_start_counter_overlay,1)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_duel_start_counter.add_event(event)
event = RunEvent()
def code():
    if _g_multiplayer_duel_start_counter_overlay >= 0:
        m_timer_a_001 = store_mission_timer_a()
        var002 = m_timer_a_001 - _g_multiplayer_duel_start_time
        var003 = 3 - var002
        if var003 <= 0:
            presentation_set_duration(0)
        elif _g_multiplayer_last_duel_start_counter_value != var003:
            _g_multiplayer_last_duel_start_counter_value = var003
            reg0 = var003
            s0 = str_store_string(gstr.duel_starts_in_reg0_seconds)
            overlay_set_text(_g_multiplayer_duel_start_counter_overlay,0)
        #end
    #end
event.codeBlock = code
multiplayer_duel_start_counter.add_event(event)


multiplayer_flag_projection_display_ccoop = Presentation("multiplayer_flag_projection_display_ccoop")
multiplayer_flag_projection_display_ccoop.set_read_only()
multiplayer_flag_projection_display_ccoop.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    create_mesh_overlay(_g_presentation_obj_flag_projection_display_1,mesh.prison_cart_pos)
    position_set_x(1,69)
    position_set_y(1,92)
    overlay_set_size(_g_presentation_obj_flag_projection_display_1,1)
    overlay_set_display(_g_presentation_obj_flag_projection_display_1,0)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_flag_projection_display_ccoop.add_event(event)
event = RunEvent()
def code():
    if True:
        overlay_set_display(_g_presentation_obj_flag_projection_display_1,0)
        if _g_prison_cart_point > 0:
            scp_instance_001 = scene_prop_get_instance(spr.prison_cart_door_left,0)
            scp_instance_002 = scene_prop_get_instance(spr.prison_cart_door_right,0)
            pos1 = prop_instance_get_position(scp_instance_001)
            pos2 = prop_instance_get_position(scp_instance_002)
            avarage_of_two_points()
            position_move_z(1,50,1)
            pos3 = position_get_screen_projection(1)
            pos_x_003 = position_get_x(3)
            pos_y_004 = position_get_y(3)
            if is_between(pos_x_003,-100,1100) and is_between(pos_y_004,-100,850):
                overlay_set_position(_g_presentation_obj_flag_projection_display_1,3)
                overlay_set_display(_g_presentation_obj_flag_projection_display_1,1)
            #end
        #end
    #end
event.codeBlock = code
multiplayer_flag_projection_display_ccoop.add_event(event)


multiplayer_flag_projection_display_ccoop_wave = Presentation("multiplayer_flag_projection_display_ccoop_wave")
multiplayer_flag_projection_display_ccoop_wave.set_read_only()
multiplayer_flag_projection_display_ccoop_wave.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    var001 = -1
    var002 = -1
    troop_slot_003 = troop_get_slot(trp.multiplayer_data,186)
    for var004 in range(0, troop_slot_003):
        slot_no_005 = var004 * 3
        slot_no_005 += 188
        troop_slot_006 = troop_get_slot(trp.multiplayer_data,slot_no_005)
        slot_no_005 += 1
        troop_slot_007 = troop_get_slot(trp.multiplayer_data,slot_no_005)
        if troop_slot_006 > 0:
            if var001 != -1 and var001 != troop_slot_007:
                var002 = troop_slot_007
            else:
                var001 = troop_slot_007
            #end
        #end
    #end
    if var001 > 0:
        create_mesh_overlay(_g_presentation_obj_flag_projection_display_1,mesh.incoming_enemy)
        position_set_x(1,250)
        position_set_y(1,250)
        overlay_set_size(_g_presentation_obj_flag_projection_display_1,1)
        overlay_set_display(_g_presentation_obj_flag_projection_display_1,0)
    #end
    if var002 > 0:
        create_mesh_overlay(_g_presentation_obj_flag_projection_display_2,mesh.incoming_enemy)
        position_set_x(1,250)
        position_set_y(1,250)
        overlay_set_size(_g_presentation_obj_flag_projection_display_2,1)
        overlay_set_display(_g_presentation_obj_flag_projection_display_2,0)
    #end
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_flag_projection_display_ccoop_wave.add_event(event)
event = RunEvent()
def code():
    var001 = -1
    var002 = -1
    troop_slot_003 = troop_get_slot(trp.multiplayer_data,186)
    for var004 in range(0, troop_slot_003):
        slot_no_005 = var004 * 3
        slot_no_005 += 188
        troop_slot_006 = troop_get_slot(trp.multiplayer_data,slot_no_005)
        slot_no_005 += 1
        troop_slot_007 = troop_get_slot(trp.multiplayer_data,slot_no_005)
        if troop_slot_006 > 0:
            if var001 != -1 and var001 != troop_slot_007:
                var002 = troop_slot_007
            else:
                var001 = troop_slot_007
            #end
        #end
    #end
    if var001 > 0 or var002 > 0:
        if var001 > 0:
            overlay_set_display(_g_presentation_obj_flag_projection_display_1,0)
            pos1 = entry_point_get_position(var001)
            position_move_z(1,150,1)
            pos3 = position_get_screen_projection(1)
            pos_x_008 = position_get_x(3)
            pos_y_009 = position_get_y(3)
            if is_between(pos_x_008,-100,1100) and is_between(pos_y_009,-100,850):
                overlay_set_position(_g_presentation_obj_flag_projection_display_1,3)
                overlay_set_display(_g_presentation_obj_flag_projection_display_1,1)
            #end
        #end
        if var002 > 0:
            overlay_set_display(_g_presentation_obj_flag_projection_display_2,0)
            pos1 = entry_point_get_position(var002)
            position_move_z(1,50,1)
            pos3 = position_get_screen_projection(1)
            pos_x_008 = position_get_x(3)
            pos_y_009 = position_get_y(3)
            if is_between(pos_x_008,-100,1100) and is_between(pos_y_009,-100,850):
                overlay_set_position(_g_presentation_obj_flag_projection_display_2,3)
                overlay_set_display(_g_presentation_obj_flag_projection_display_2,1)
            #end
        #end
    else:
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_flag_projection_display_ccoop_wave.add_event(event)


coop_assign_drop_to_group_member = Presentation("coop_assign_drop_to_group_member")
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    var001 = reg0
    var002 = reg1
    var003 = reg2
    play_sound(snd.draw_shield)
    create_mesh_overlay(reg0,mesh.mp_ingame_menu)
    position_set_x(1,250)
    position_set_y(1,80)
    overlay_set_position(reg0,1)
    position_set_x(1,1000)
    position_set_y(1,1000)
    overlay_set_size(reg0,1)
    create_mesh_overlay(reg0,mesh.ccoop_drop_chest_top)
    position_set_x(1,387)
    position_set_y(1,474)
    overlay_set_position(reg0,1)
    position_set_x(1,562)
    position_set_y(1,374)
    overlay_set_size(reg0,1)
    create_mesh_overlay_with_item_id(reg0,var001)
    position_set_x(1,500)
    position_set_y(1,450)
    overlay_set_position(reg0,1)
    position_set_y(1,528)
    overlay_animate_to_position(reg0,400,1)
    position_set_x(1,900)
    position_set_y(1,1200)
    overlay_set_size(reg0,1)
    position_set_x(1,900)
    position_set_y(1,1200)
    create_mesh_overlay(reg0,mesh.ccoop_drop_chest_bottom)
    position_set_x(1,387)
    position_set_y(1,375)
    overlay_set_position(reg0,1)
    position_set_x(1,562)
    position_set_y(1,250)
    overlay_set_size(reg0,1)
    str_clear(0)
    create_text_overlay(_g_presentation_obj_assign_drop_container,0,131072)
    position_set_x(1,285)
    position_set_y(1,75)
    overlay_set_position(_g_presentation_obj_assign_drop_container,1)
    position_set_x(1,405)
    position_set_y(1,550)
    overlay_set_area_size(_g_presentation_obj_assign_drop_container,1)
    set_container_overlay(_g_presentation_obj_assign_drop_container)
    create_text_overlay(reg0,gstr.ccoop_assign_drop,0)
    overlay_set_color(reg0,16777215)
    position_set_x(1,0)
    position_set_y(1,500)
    overlay_set_position(reg0,1)
    set_container_overlay(-1)
    var004 = 355
    s0 = str_store_item_name_plural(var001)
    var004 -= 3
    create_text_overlay(reg0,0,16)
    overlay_set_color(reg0,16777215)
    position_set_x(1,500)
    position_set_y(1,var004)
    overlay_set_position(reg0,1)
    var004 -= 25
    var005 = var001 - itm.javelin_bow
    var005 = var005 + gstr.javelin_bow
    if is_between(var005,gstr.javelin_bow,gstr.npc1_1):
        s0 = str_store_string(var005)
    else:
        str_clear(0)
    #end
    create_text_overlay(reg0,0,16)
    overlay_set_color(reg0,16777215)
    position_set_x(1,750)
    position_set_y(1,750)
    overlay_set_size(reg0,1)
    position_set_x(1,500)
    position_set_y(1,var004)
    overlay_set_position(reg0,1)
    my_player = multiplayer_get_my_player()
    s0 = str_store_player_username(my_player)
    var004 -= 176
    if var002 >= 0 and var003 >= 0:
        var007 = 270
    elif var002 >= 0 or var003 >= 0:
        var007 = 331
    else:
        var007 = 393
    #end
    create_image_button_overlay_with_tableau_material(_g_presentation_obj_coop_assign_drop_player,-1,tableau.coop_companion_select_0,-1)
    overlay_set_tooltip(_g_presentation_obj_coop_assign_drop_player,0)
    overlay_set_color(_g_presentation_obj_coop_assign_drop_player,16777215)
    position_set_x(1,var007)
    position_set_y(1,var004)
    overlay_set_position(_g_presentation_obj_coop_assign_drop_player,1)
    position_set_x(1,563)
    position_set_y(1,750)
    overlay_set_size(_g_presentation_obj_coop_assign_drop_player,1)
    if var002 >= 0:
        var007 += 123
        _g_coop_assign_drop_companion_1 = var002
        troop_id_008 = agent_get_troop_id(var002)
        s0 = str_store_troop_name(troop_id_008)
        create_image_button_overlay_with_tableau_material(_g_presentation_obj_coop_assign_drop_companion_1,-1,tableau.coop_companion_select_0,troop_id_008)
        overlay_set_tooltip(_g_presentation_obj_coop_assign_drop_companion_1,0)
        position_set_x(1,var007)
        position_set_y(1,var004)
        overlay_set_position(_g_presentation_obj_coop_assign_drop_companion_1,1)
        position_set_x(1,563)
        position_set_y(1,750)
        overlay_set_size(_g_presentation_obj_coop_assign_drop_companion_1,1)
    #end
    if var003 >= 0:
        var007 += 123
        _g_coop_assign_drop_companion_2 = var003
        troop_id_008 = agent_get_troop_id(var003)
        s0 = str_store_troop_name(troop_id_008)
        create_image_button_overlay_with_tableau_material(_g_presentation_obj_coop_assign_drop_companion_2,-1,tableau.coop_companion_select_0,troop_id_008)
        overlay_set_tooltip(_g_presentation_obj_coop_assign_drop_companion_2,0)
        position_set_x(1,var007)
        position_set_y(1,var004)
        overlay_set_position(_g_presentation_obj_coop_assign_drop_companion_2,1)
        position_set_x(1,563)
        position_set_y(1,750)
        overlay_set_size(_g_presentation_obj_coop_assign_drop_companion_2,1)
    #end
    var004 -= 40
    var004 -= 2
    create_button_overlay(_g_presentation_obj_coop_assign_drop_noone,gstr.noone,0)
    overlay_set_color(_g_presentation_obj_coop_assign_drop_noone,16777215)
    position_set_x(1,645)
    position_set_y(1,var004)
    overlay_set_position(_g_presentation_obj_coop_assign_drop_noone,1)
    presentation_set_duration(999999)
event.codeBlock = code
coop_assign_drop_to_group_member.add_event(event)
event = StateChangedEvent()
def code(var001):
    if var001 == _g_presentation_obj_coop_assign_drop_player:
        multiplayer_send_2_int_to_server(48,17,0)
        presentation_set_duration(0)
    elif var001 == _g_presentation_obj_coop_assign_drop_companion_1:
        multiplayer_send_2_int_to_server(48,17,_g_coop_assign_drop_companion_1)
        presentation_set_duration(0)
    elif var001 == _g_presentation_obj_coop_assign_drop_companion_2:
        multiplayer_send_2_int_to_server(48,17,_g_coop_assign_drop_companion_2)
        presentation_set_duration(0)
    elif var001 == _g_presentation_obj_coop_assign_drop_noone:
        multiplayer_send_2_int_to_server(48,17,-1)
        presentation_set_duration(0)
    #end
event.codeBlock = code
coop_assign_drop_to_group_member.add_event(event)
event = RunEvent()
def code(var001):
    close_item_details()
    if key_clicked(1) or key_clicked(248) and var001 > 200:
        presentation_set_duration(0)
        multiplayer_send_2_int_to_server(48,17,-1)
    #end
event.codeBlock = code
coop_assign_drop_to_group_member.add_event(event)


multiplayer_ccoop_next_wave_time_counter = Presentation("multiplayer_ccoop_next_wave_time_counter")
multiplayer_ccoop_next_wave_time_counter.set_read_only()
multiplayer_ccoop_next_wave_time_counter.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    _g_multiplayer_respawn_counter_overlay = -1
    _g_multiplayer_respawn_remained_overlay = -1
    _g_multiplayer_last_respawn_counter_value = -1
    str_clear(0)
    create_text_overlay(_g_multiplayer_respawn_counter_overlay,0,65552)
    overlay_set_color(_g_multiplayer_respawn_counter_overlay,16777215)
    position_set_x(1,500)
    position_set_y(1,600)
    overlay_set_position(_g_multiplayer_respawn_counter_overlay,1)
    position_set_x(1,2000)
    position_set_y(1,2000)
    overlay_set_size(_g_multiplayer_respawn_counter_overlay,1)
    str_clear(0)
    create_text_overlay(_g_multiplayer_respawn_remained_overlay,0,65552)
    overlay_set_color(_g_multiplayer_respawn_remained_overlay,16777215)
    position_set_x(1,500)
    position_set_y(1,570)
    overlay_set_position(_g_multiplayer_respawn_remained_overlay,1)
    position_set_x(1,1400)
    position_set_y(1,1400)
    overlay_set_size(_g_multiplayer_respawn_remained_overlay,1)
    str_clear(0)
    create_text_overlay(_g_multiplayer_respawn_wave_hint_overlay,0,65552)
    overlay_set_color(_g_multiplayer_respawn_wave_hint_overlay,16777215)
    position_set_x(1,500)
    position_set_y(1,480)
    overlay_set_position(_g_multiplayer_respawn_wave_hint_overlay,1)
    position_set_x(1,1400)
    position_set_y(1,1400)
    overlay_set_size(_g_multiplayer_respawn_wave_hint_overlay,1)
    presentation_set_duration(999999)
event.codeBlock = code
multiplayer_ccoop_next_wave_time_counter.add_event(event)
event = RunEvent()
def code():
    my_player = multiplayer_get_my_player()
    if _g_multiplayer_respawn_counter_overlay >= 0:
        m_timer_a_001 = store_mission_timer_a()
        var002 = _g_multiplayer_ccoop_next_wave_start_time - m_timer_a_001
        if var002 > 0 and _g_multiplayer_ccoop_wave_no > 0:
            reg0 = var002
            reg1 = _g_multiplayer_ccoop_wave_no - _g_mp_coop_last_king_wave
            s1 = str_store_string(gstr.blank_string)
            if True:
                troop_slot_003 = troop_get_slot(trp.multiplayer_data,187)
                if is_between(troop_slot_003,trp.knight_1_1,trp.kingdom_1_pretender) or is_between(troop_slot_003,trp.quick_battle_troop_1,trp.quick_battle_troops_end):
                    s0 = str_store_troop_name(troop_slot_003)
                    s1 = str_store_string(gstr.ccoop_lord_s0_wave_hint)
                elif is_between(troop_slot_003,trp.kingdom_1_lord,trp.knight_1_1):
                    s0 = str_store_troop_name(troop_slot_003)
                    s1 = str_store_string(gstr.ccoop_king_s0_wave_hint)
                #end
            #end
            s0 = str_store_string(gstr.ccoop_wave_reg1_is_coming_in_reg0_seconds)
        elif _g_mp_coop_king_waves >= 1:
            reg2 = _g_mp_coop_king_waves
            s0 = str_store_string(gstr.ccoop_elite_wave_reg1_is_coming_in_reg0_seconds)
            if reg1 > 0 and reg1 < 4:
                s1 = str_store_string(gstr.elite_wave_hint)
            #end
        #end
        overlay_set_text(_g_multiplayer_respawn_counter_overlay,0)
        overlay_set_text(_g_multiplayer_respawn_wave_hint_overlay,1)
    elif player_is_active(my_player):
        agent_id_005 = player_get_agent_id(my_player)
        if agent_id_005 >= 0:
            agent_team_no_006 = agent_get_team(agent_id_005)
            if agent_team_no_006 < 2 and not agent_is_alive(agent_id_005):
                player_slot_007 = player_get_slot(my_player,24)
                if player_slot_007 >= 0:
                    s0 = str_store_string(gstr.ask_for_help_to_respawn_hint)
                else:
                    s0 = str_store_string(gstr.wait_for_next_turn_to_respawn_hint)
                #end
            #end
        #end
        overlay_set_text(_g_multiplayer_respawn_counter_overlay,0)
    else:
        presentation_set_duration(0)
    #end
event.codeBlock = code
multiplayer_ccoop_next_wave_time_counter.add_event(event)


multiplayer_ccoop_victory_message = Presentation("multiplayer_ccoop_victory_message")
multiplayer_ccoop_victory_message.set_read_only()
multiplayer_ccoop_victory_message.set_manual_end_only()
event = LoadEvent()
def code():
    set_fixed_point_multiplier(1000)
    team_faction_001 = team_get_faction(1)
    s0 = str_store_faction_name(team_faction_001)
    if is_between(team_faction_001,fac.player_supporters_faction,fac.kingdoms_end):
        reg1 = 0
    else:
        reg1 = 1
    #end
    if _g_multiplayer_ccoop_difficulty_string_i >= 0:
        s1 = str_store_string(_g_multiplayer_ccoop_difficulty_string_i)
        s2 = str_store_string(gstr.ccoop_s0_enemy_defeated_s1)
    else:
        s2 = str_store_string(gstr.ccoop_s0_enemy_defeated_endless_reg0)
    #end
    create_text_overlay(_g_multiplayer_ccoop_victory_overlay,gstr.ccoop_victory,65552)
    overlay_set_color(_g_multiplayer_ccoop_victory_overlay,6875982)
    position_set_x(1,500)
    position_set_y(1,600)
    overlay_set_position(_g_multiplayer_ccoop_victory_overlay,1)
    position_set_x(1,2000)
    position_set_y(1,2000)
    overlay_set_size(_g_multiplayer_ccoop_victory_overlay,1)
    create_text_overlay(_g_multiplayer_ccoop_victory_subtitle_overlay,2,65552)
    overlay_set_color(_g_multiplayer_ccoop_victory_subtitle_overlay,6875982)
    position_set_x(1,500)
    position_set_y(1,480)
    overlay_set_position(_g_multiplayer_ccoop_victory_subtitle_overlay,1)
    position_set_x(1,1400)
    position_set_y(1,1400)
    overlay_set_size(_g_multiplayer_ccoop_victory_subtitle_overlay,1)
    presentation_set_duration(2000)
event.codeBlock = code
multiplayer_ccoop_victory_message.add_event(event)
event = RunEvent()
def code():
    if is_presentation_active(prsnt.multiplayer_ccoop_next_wave_time_counter):
        presentation_set_duration(0)
event.codeBlock = code
multiplayer_ccoop_victory_message.add_event(event)


