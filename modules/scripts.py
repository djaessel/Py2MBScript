# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")


from MBParty import MBParty
import ID_animations as animID
import module_constants as mconst
import header_common as mcom


def game_start():
    pass


# TODO: add comment
def game_get_use_string(instance_id):
    scene_prop_id = prop_instance_get_scene_prop_kind(instance_id)

    winches = [
        "spr_winch_b",
        "spr_winch",
    ]
    doors = [
        "spr_door_destructible",
        "spr_castle_f_door_b",
        "spr_castle_e_sally_door_a",
        "spr_castle_f_sally_door_a",
        "spr_earth_sally_gate_left",
        "spr_earth_sally_gate_right",
        "spr_viking_keep_destroy_sally_door_left",
        "spr_viking_keep_destroy_sally_door_right",
        "spr_castle_f_door_a",
    ]
    ladders = [
        "spr_siege_ladder_move_6m",
        "spr_siege_ladder_move_8m",
        "spr_siege_ladder_move_10m",
        "spr_siege_ladder_move_12m",
        "spr_siege_ladder_move_14m",
    ]

    if scene_prop_id in winches:
        effected_object = "spr_portcullis"
    elif scene_prop_id in doors or scene_prop_id in ladders:
        effected_object = scene_prop_id

    slotx = mconst.scene_prop_open_or_close_slot
    item_situation = scene_prop_get_slot(instance_id, slotx)

    if effected_object == "spr_portcullis": #opening/closing portcullis
        if item_situation == 0:
            s0 = "str_open_gate"
        else:
            s0 = "str_close_gate"
        #end
    elif effected_object in doors: #opening/closing door
        if item_situation == 0:
            s0 = "str_open_door"
        else:
            s0 = "str_close_door"
        #end
    else: #raising/dropping ladder
        if item_situation == 0:
            s0 = "str_raise_ladder"
        else:
            s0 = "str_drop_ladder"
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
            s0 = "str_team_reg0_bot_count_is_reg1"
        elif val1 == 2:
            reg1 = _g_multiplayer_num_bots_team_2
            s0 = "str_team_reg0_bot_count_is_reg1"
        else:
            s0 = "str_input_is_not_correct_for_the_command_type_help_for_more_information"
        #end
    elif input == 2:
        reg0 = val1
        reg1 = val2
        if val1 == 1 and val2 >= 0:
            _g_multiplayer_num_bots_team_1 = val2
            s0 = "str_team_reg0_bot_count_is_reg1"
        elif val1 == 2 and val2 >= 0:
            _g_multiplayer_num_bots_team_2 = val2
            s0 = "str_team_reg0_bot_count_is_reg1"
        else:
            s0 = "str_input_is_not_correct_for_the_command_type_help_for_more_information"
        #end
    elif input == 3:
        reg0 = _g_multiplayer_round_max_seconds
        s0 = "str_maximum_seconds_for_round_is_reg0"
    elif input == 4:
        reg0 = val1
        mins = mcom.multiplayer_round_max_seconds_min
        maxs = mcom.multiplayer_round_max_seconds_max
        if is_between(val1, mins, maxs):
            _g_multiplayer_round_max_seconds = val1
            s0 = "str_maximum_seconds_for_round_is_reg0"
            num_players = get_max_players()
            for cur_player in range(1, num_players):
                if player_is_active(cur_player):
                    retx = mcom.multiplayer_event_return_round_max_seconds
                    multiplayer_send_int_to_player(cur_player, retx, val1)
            #end
        else:
            s0 = "str_input_is_not_correct_for_the_command_type_help_for_more_information"
        #end
    elif input == 5:
        reg0 = _g_multiplayer_respawn_period
        s0 = "str_respawn_period_is_reg0_seconds"
    else: # add more here
        s0 = "@{!}DEBUG : SYSTEM ERROR!"


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
        jump_to_menu("mnu_town")
    else:
        jump_to_menu("mnu_simple_encounter")


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


# INPUT: arg1 = agent_id, arg2 = instance_id
def use_item(agent_id, user_id):
    print("USE_ITEM:", agent_id, user_id)
    pass # todo add code


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




