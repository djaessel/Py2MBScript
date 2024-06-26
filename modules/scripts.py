# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")


from MBParty import MBParty

import ID_animations as animID
import module_constants as mconst
import header_common as mcom
import strings as gstr
import scene_props as spr
import sounds as snd
import troops as trp
import items as itm
import map_icons as icon
import game_menus as mnu
import animations as anim
import factions as fac
import meshes as mesh
#import info_pages as ip
import dialogs as dlg
import mission_templates as mt
import parties as p
import party_templates as pt
import particle_systems as psys
import presentations as prnst
import postfxs as pfx
import quests as qst
import scenes as scn
import skills as skl


def game_start():
    pass


# TODO: add comment
def game_get_use_string(instance_id):
    scene_prop_id = prop_instance_get_scene_prop_kind(instance_id)

    winches = [
        spr.winch_b,
        spr.winch,
    ]
    doors = [
        spr.door_destructible,
        spr.castle_f_door_b,
        spr.castle_e_sally_door_a,
        spr.castle_f_sally_door_a,
        spr.earth_sally_gate_left,
        spr.earth_sally_gate_right,
        spr.viking_keep_destroy_sally_door_left,
        spr.viking_keep_destroy_sally_door_right,
        spr.castle_f_door_a,
    ]
    ladders = [
        spr.siege_ladder_move_6m,
        spr.siege_ladder_move_8m,
        spr.siege_ladder_move_10m,
        spr.siege_ladder_move_12m,
        spr.siege_ladder_move_14m,
    ]

    if scene_prop_id in winches:
        effected_object = spr.portcullis
    elif scene_prop_id in doors or scene_prop_id in ladders:
        effected_object = scene_prop_id

    slot_openclose = mconst.scene_prop_open_or_close_slot
    item_situation = scene_prop_get_slot(instance_id, slot_openclose)

    if effected_object == spr.portcullis: #opening/closing portcullis
        if item_situation == 0:
            s0 = gstr.open_gate
        else:
            s0 = gstr.close_gate
        #end
    elif effected_object in doors: #opening/closing door
        if item_situation == 0:
            s0 = gstr.open_door
        else:
            s0 = gstr.close_door
        #end
    else: #raising/dropping ladder
        if item_situation == 0:
            s0 = gstr.raise_ladder
        else:
            s0 = gstr.drop_ladder
        #end


# This script is called from the game engine when a multiplayer map is ended in clients (not in server).
def game_set_multiplayer_mission_end():
    _g_multiplayer_mission_end_screen = 1


# This script is called from the game engine when user enters "cheatmenu from command console (ctrl+~).
def game_enable_cheat_menu(input):
    if input == 0:
        _cheat_mode = 0
    elif input == 1:
        _cheat_mode = 1


# This script is called from the game engine when a console command is entered from the dedicated server.
# INPUT: anything
# OUTPUT: s0 = result text
def game_get_console_command(input, val1, val2):
    #if input == 2:
    #    val2 = store_script_param(3)

    if input == 1:
        reg0 = val1
        if val1 == 1:
            reg1 = _g_multiplayer_num_bots_team_1
            s0 = gstr.team_reg0_bot_count_is_reg1
        elif val1 == 2:
            reg1 = _g_multiplayer_num_bots_team_2
            s0 = gstr.team_reg0_bot_count_is_reg1
        else:
            s0 = gstr.input_is_not_correct_for_the_command_type_help_for_more_information
        #end
    elif input == 2:
        reg0 = val1
        reg1 = val2
        if val1 == 1 and val2 >= 0:
            _g_multiplayer_num_bots_team_1 = val2
            s0 = gstr.team_reg0_bot_count_is_reg1
        elif val1 == 2 and val2 >= 0:
            _g_multiplayer_num_bots_team_2 = val2
            s0 = gstr.team_reg0_bot_count_is_reg1
        else:
            s0 = gstr.input_is_not_correct_for_the_command_type_help_for_more_information
        #end
    elif input == 3:
        reg0 = _g_multiplayer_round_max_seconds
        s0 = gstr.maximum_seconds_for_round_is_reg0
    elif input == 4:
        reg0 = val1
        mins = mcom.multiplayer_round_max_seconds_min
        maxs = mcom.multiplayer_round_max_seconds_max
        if is_between(val1, mins, maxs):
            _g_multiplayer_round_max_seconds = val1
            s0 = gstr.maximum_seconds_for_round_is_reg0
            num_players = get_max_players()
            for cur_player in range(1, num_players):
                if player_is_active(cur_player):
                    retx = mcom.multiplayer_event_return_round_max_seconds
                    multiplayer_send_int_to_player(cur_player, retx, val1)
            #end
        else:
            s0 = gstr.input_is_not_correct_for_the_command_type_help_for_more_information
        #end
    elif input == 5:
        reg0 = _g_multiplayer_respawn_period
        s0 = gstr.respawn_period_is_reg0_seconds
    else: # add more here
        s0 = "{!}DEBUG : SYSTEM ERROR!"


# This script is called from the game engine whenever player party encounters another party or a battle on the world map
# INPUT:
# param1: encountered_party
# param2: second encountered_party (if this was a battle
def game_event_party_encounter(_g_encountered_party, _g_encountered_party_2):
    _g_encountered_party_faction = store_faction_of_party(_g_encountered_party)
    _g_encountered_party_relation = store_relation(_g_encountered_party_faction, "fac_player_faction")

    _g_encountered_party = MBParty(_g_encountered_party)
    template_idx = _g_encountered_party.get_template_id()
    if template_idx == 0:
        jump_to_menu(mnu.town_menu)
    else:
        jump_to_menu(mnu.simple_encounter)


# This script is called whenever the game simulates the battle between two parties on the map.
# INPUT:
# param1: Defender Party
# param2: Attacker Party
def game_event_simulate_battle(root_defender_party, root_attacker_party):
    print("Battle simulation:")
    print("- Defender:", root_defender_party)
    print("- Attacker:", root_attacker_party)


# This script is called whenever the game ends the battle between two parties on the map.
# INPUT:
# param1: Defender Party
# param2: Attacker Party
def game_event_battle_end(root_defender_party, root_attacker_party):
    print("Battle ended:")
    print("- Defender:", root_defender_party)
    print("- Attacker:", root_attacker_party)


# This script is called from the game engine for calculating the buying price of any item.
# INPUT:
# param1: item_kind_id
# OUTPUT:
# trigger_result and reg0 = price_factor
def game_get_item_buy_price_factor(item_kind_id):
    price_factor = 100

    # ... some code ...

    price_factor /= 100

    reg0 = price_factor + item_kind_id
    set_trigger_result(reg0)


# This script is called from the game engine for calculating the selling price of any item.
# INPUT:
# param1: item_kind_id
# OUTPUT:
# trigger_result and reg0 = price_factor
def game_get_item_sell_price_factor(item_kind_id):
    price_factor = 100

    # ... some code ...

    price_factor /= 100

    reg0 = price_factor + item_kind_id
    set_trigger_result(reg0)



# TODO: add more game events


def superMaths(bul, bal, bil):
    x = 1 + 3 * 5 + 2 * 7 + 5 * 2 # 40
    print(x)

    y = 1 + 3 + x / 4 * 3 / 3 # 14
    print(y)

    z = 1 + 3 + (x + y) * 4 # 220
    print(z)

    z2 = (1+3) * (4+8) # 48
    print(z2)

    z3 = (3-1) * (8-4) # 8
    print(z3)

    z4 = z / (x + y) * z2 # 195,555555556 --> 192 (integer rounding after division!)
    print(z4)

    z5 = x - 4 - 5 + z3 # 39
    print(z5)

    x2 = (9 + 3 * 2) - (5 * 2) + (3 - 1) # 7
    print(x2)

    y2 = (9 + 6 * 2) - (8 / 2) - (3 - 1) # 15
    print(y2)

    qq = (bul * bal) / bil + bil
    print(qq)

    oo = 555 + 2 # 557
    oo /= 4 * 55 + 6 * 2 # 2,400862069 --> 2
    print(oo)

    oo += 6 / 2 + 4 # 9
    print(oo)

    oo -= 5 + 2 # 2
    print(oo)

    oo *= 18 - (2 * 6) # 12
    print(oo)

    oo %= 1 * 6 + 2
    print(oo) # 4


# INPUT: arg1 = agent_id, arg2 = instance_id
def use_item(instance_id, user_id):
    winches = [
        spr.winch_b,
        spr.winch,
    ]

    doors = [
        spr.door_destructible,
        spr.castle_f_door_b,
        spr.castle_e_sally_door_a,
        spr.castle_f_sally_door_a,
        spr.earth_sally_gate_left,
        spr.earth_sally_gate_right,
        spr.viking_keep_destroy_sally_door_left,
        spr.viking_keep_destroy_sally_door_right,
        spr.castle_f_door_a,
    ]

    ladders = [
        spr.siege_ladder_move_6m,
        spr.siege_ladder_move_8m,
        spr.siege_ladder_move_10m,
        spr.siege_ladder_move_12m,
        spr.siege_ladder_move_14m,
    ]

    slot_openclose = mconst.scene_prop_open_or_close_slot

    if game_in_multiplayer_mode():
        scene_prop_id = prop_instance_get_scene_prop_kind(instance_id)
        if scene_prop_id == spr.winch_b:
            my_player_no = multiplayer_get_my_player()
            if my_player_no > 0 or not multiplayer_is_dedicated_server() and my_player_no >= 0:
                my_agent_id = player_get_agent_id(my_player_no)
                if my_agent_id >= 0 and agent_is_active(my_agent_id):
                    my_team_no = agent_get_team(my_agent_id)
                    if my_team_no == 0:
                        opened_or_closed = scene_prop_get_slot(instance_id, slot_openclose)
                        if user_id >= 0 and agent_is_active(user_id):
                            user_player = agent_get_player_id(user_id)
                            str_store_player_username(s7, user_player)
                            if opened_or_closed == 0:
                                print("{s7} opened the gate")
                            else:
                                print("{s7} closed the gate")
                            #end
                        #end
                    #end
                #end
            #end
        #end
    #end

    scene_prop_id = prop_instance_get_scene_prop_kind(instance_id)

    if scene_prop_id in winches:
        effected_object = spr.portcullis
    elif scene_prop_id in doors or scene_prop_id in ladders:
        effected_object = scene_prop_id

    smallest_dist = -1
    prop_instance_get_position(pos0, instance_id)
    num_instances_of_effected_object = scene_prop_get_num_instances(effected_object)
    for cur_instance in range(num_instances_of_effected_object):
        cur_instance_id = scene_prop_get_instance(effected_object, cur_instance)
        prop_instance_get_position(pos1, cur_instance_id)
        dist = get_sq_distance_between_positions(pos0, pos1)
        if smallest_dist == -1 or dist < smallest_dist:
            smallest_dist = dist
            effected_object_instance_id = cur_instance_id
        #end
    #end

    if instance_id >= 0 and smallest_dist >= 0:
        if effected_object == spr.portcullis:
            opened_or_closed = scene_prop_get_slot(instance_id, slot_openclose)
            if opened_or_closed == 0: # open gate
                scene_prop_enable_after_time(instance_id, 400) #4 seconds
                if multiplayer_is_server() or not game_in_multiplayer_mode():
                    prop_instance_get_position(pos0, effected_object_instance_id)
                    position_move_z(pos0, 375)
                    prop_instance_animate_to_position(effected_object_instance_id, pos0, 400)
                #end
                scene_prop_set_slot(instance_id, slot_openclose, 1)

                if scene_prop_id == spr.winch_b and multiplayer_is_server() or not game_in_multiplayer_mode():
                    prop_instance_get_position(pos1, instance_id)
                    prop_instance_rotate_to_position(instance_id, pos1, 400, 72000)
                #end
            else: #close gate
                scene_prop_enable_after_time(instance_id, 400) #4 seconds
                if multiplayer_is_server() or not game_in_multiplayer_mode():
                    prop_instance_get_position(pos0, effected_object_instance_id)
                    position_move_z(pos0, -375)
                    prop_instance_animate_to_position(effected_object_instance_id, pos0, 400)
                #end
                scene_prop_set_slot(instance_id, slot_openclose, 0)

                if scene_prop_id == spr.winch_b and multiplayer_is_server() or not game_in_multiplayer_mode():
                    prop_instance_get_position(pos1, instance_id)
                    prop_instance_rotate_to_position(instance_id, pos1, 400, -72000)
                #end
            #end
        elif effected_object in ladders:
            if effected_object == spr.siege_ladder_move_6m:
                animation_time_drop = 120
                animation_time_elevate = 240
            elif effected_object == spr.siege_ladder_move_8m:
                animation_time_drop = 140
                animation_time_elevate = 280
            elif effected_object == spr.siege_ladder_move_10m:
                animation_time_drop = 160
                animation_time_elevate = 320
            elif effected_object == spr.siege_ladder_move_12m:
                animation_time_drop = 190
                animation_time_elevate = 360
            elif effected_object == spr.siege_ladder_move_14m:
                animation_time_drop = 230
                animation_time_elevate = 400
            #end

            opened_or_closed = scene_prop_get_slot(instance_id, slot_openclose)

            if opened_or_closed == 0: #ladder at ground
                scene_prop_enable_after_time(effected_object_instance_id, animation_time_elevate) #3 seconds in average
                prop_instance_get_starting_position(pos0, effected_object_instance_id)
                prop_instance_enable_physics(effected_object_instance_id, 0)
                prop_instance_animate_to_position(effected_object_instance_id, pos0, 300)
                scene_prop_set_slot(effected_object_instance_id, slot_openclose, 1)
            else: #ladder at wall
                scene_prop_enable_after_time(effected_object_instance_id, animation_time_drop) #1.5 seconds in anverage
                prop_instance_get_position(pos0, instance_id)

                smallest_dist = -1
                usable_items_start = mcom.multi_entry_points_for_usable_items_start
                usable_items_end = mcom.multi_entry_points_for_usable_items_end
                for entry_point_no in range(usable_items_start, usable_items_end):
                    entry_point_get_position(pos1, entry_point_no)
                    dist = get_sq_distance_between_positions(pos0, pos1)
                    if smallest_dist == -1 or dist < smallest_dist:
                        smallest_dist = dist
                        nearest_entry_point = entry_point_no
                    #end
                #end

                if smallest_dist >= 0 and smallest_dist < 22500: #max 15m distance
                    entry_point_get_position(pos1, nearest_entry_point)
                    position_rotate_x(pos1, -90)
                    slotSmokeEffectDone = mconst.scene_prop_smoke_effect_done
                    scene_prop_set_slot(effected_object_instance_id, slotSmokeEffectDone, 0)
                    prop_instance_enable_physics(effected_object_instance_id, 0)
                    prop_instance_animate_to_position(effected_object_instance_id, pos1, 130)
                #end

                scene_prop_set_slot(effected_object_instance_id, slot_openclose, 0)
            #end
        elif effected_object in doors:
            effected_object_instance_id = instance_id
            opened_or_closed = scene_prop_get_slot(effected_object_instance_id, slot_openclose)
            if opened_or_closed == 0:
                prop_instance_get_starting_position(pos0, effected_object_instance_id)
                scene_prop_enable_after_time(effected_object_instance_id, 100)
                if scene_prop_id != spr.viking_keep_destroy_sally_door_left and scene_prop_id != spr.earth_sally_gate_left:
                    position_rotate_z(pos0, -85)
                else:
                    position_rotate_z(pos0, 85)
                #end

                prop_instance_animate_to_position(effected_object_instance_id, pos0, 100)
                scene_prop_set_slot(effected_object_instance_id, slot_openclose, 1)
            else:
                prop_instance_get_starting_position(pos0, effected_object_instance_id)
                scene_prop_enable_after_time(effected_object_instance_id, 100)
                prop_instance_animate_to_position(effected_object_instance_id, pos0, 100)
                scene_prop_set_slot(effected_object_instance_id, slot_openclose, 0)
            #end
        #end
    #end


def add_troop_to_cur_tableau_for_character(troop_no):
    set_fixed_point_multiplier(100)

    cur_tableau_clear_override_items()
    #cur_tableau_set_override_flags(af_override_fullhelm)

    init_position(pos2)
    cur_tableau_set_camera_parameters(1, 4, 8, 10, 10000)

    init_position(pos5)
    cam_height = 150
    camera_distance = 360
    camera_yaw = -15
    camera_pitch = -18
    animation = animID.anim_stand_man

    position_set_z(pos5, cam_height)

    # camera looks towards -z axis
    position_rotate_x(pos5, -90)
    position_rotate_z(pos5, 180,0)

    # now apply yaw and pitch
    position_rotate_y(pos5, camera_yaw)
    position_rotate_x(pos5, camera_pitch)
    position_move_z(pos5, camera_distance, 0)
    position_move_x(pos5, 5, 0)

    if troop_is_hero(troop_no):
        cur_tableau_add_troop(troop_no, pos2, animation, -1)
    else:
        random_seed = troop_no * 126233
        random_seed %= 1000
        random_seed += 1
        cur_tableau_add_troop(troop_no, pos2, animation, random_seed)

    cur_tableau_set_camera_position(pos5)

    copy_position(pos8, pos5)
    #y axis aligned with camera now. z is up
    position_rotate_x(pos8, -90)
    position_rotate_z(pos8, 30,0)
    position_rotate_x(pos8, -60)
    cur_tableau_add_sun_light(0, pos8, 175,150,125)




