# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")


from scene_prop import SceneProp, ScenePropFlag
from simple_trigger import SimpleTrigger
import header_triggers as tri
import header_common as mcom



# - - - - - - - - - - - - reusable triggers START - - - - - - - - - - - - - - - - - -
check_item_use_trigger = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(agent_id, instance_id):
    #for only server itself-----------------------------------------------------------------------------------------------
    use_item(instance_id, agent_id)
    #for only server itself-----------------------------------------------------------------------------------------------
    num_players = get_max_players()
    mevent = mcom.multiplayer_event_use_item
    for player_no in range(1, num_players):
        if player_is_active(player_no):
            multiplayer_send_2_int_to_player(player_no, mevent, instance_id, agent_id)
check_item_use_trigger.codeBlock = code


# - - - - - - - - - - - - reusable triggers END - - - - - - - - - - - - - - - - - - -

# - - - - - - - - - - - - scene props START - - - - - - - - - - - - - - - - - - - - -
invalid_object = SceneProp("invalid_object", "question_mark")


inventory = SceneProp("inventory", "package", "bobaggage")
inventory.add_flag(ScenePropFlag.TYPE_CONTAINER)
inventory.add_flag(ScenePropFlag.PLACE_AT_ORIGIN)


empty = SceneProp("empty")


chest_a = SceneProp("chest_a", "chest_gothic", "bochest_gothic")
chest_a.add_flag(ScenePropFlag.TYPE_CONTAINER)


container_small_chest = SceneProp("container_small_chest", "package", "bobaggage")
container_small_chest.add_flag(ScenePropFlag.TYPE_CONTAINER)


container_chest_b = SceneProp("container_chest_b", "chest_b", "bo_chest_b")
container_chest_b.add_flag(ScenePropFlag.TYPE_CONTAINER)


container_chest_c = SceneProp("container_chest_c", "chest_c", "bo_chest_c")
container_chest_c.add_flag(ScenePropFlag.TYPE_CONTAINER)


player_chest = SceneProp("player_chest", "player_chest", "bo_player_chest")
player_chest.add_flag(ScenePropFlag.TYPE_CONTAINER)


locked_player_chest = SceneProp("locked_player_chest", "player_chest", "bo_player_chest")


light_sun = SceneProp("light_sun", "light_sphere")
light_sun.add_flag(ScenePropFlag.INVISIBLE)
# trigger 0
triggy = SimpleTrigger(tri.ti_on_init_scene_prop)
def code():
    if not is_currently_night():
        prop_instance_no = store_trigger_param_1()
        set_fixed_point_multiplier(100)
        prop_instance_get_scale(pos5, prop_instance_no)
        position_get_scale_x(scale, pos5)
        store_time_of_day(reg12)
        if is_between(reg12, 5, 20):
            red = 1000 * scale
            green = 965 * scale
            blue = 900 * scale
        else:
            red = 450 * scale
            green = 575 * scale
            blue = 750 * scale
        red /= 100
        green /= 100
        blue /= 100
        set_current_color(red, green, blue)
        set_position_delta(0,0,0)
        add_point_light_to_entity(0, 0)
triggy.codeBlock = code
light_sun.add_trigger(triggy)


#("light",sokf_invisible,"light_sphere","0",  [
#   (ti_on_init_scene_prop,
#    [
#        (store_trigger_param_1, ":prop_instance_no"),
#        (set_fixed_point_multiplier, 100),
#        (prop_instance_get_scale, pos5, ":prop_instance_no"),
#        (position_get_scale_x, ":scale", pos5),
#        (store_mul, ":red", 3 * 200, ":scale"),
#        (store_mul, ":green", 3 * 145, ":scale"),
#        (store_mul, ":blue", 3 * 45, ":scale"),
#        (val_div, ":red", 100),
#        (val_div, ":green", 100),
#        (val_div, ":blue", 100),
#        (set_current_color,":red", ":green", ":blue"),
#        (set_position_delta,0,0,0),
#        (add_point_light_to_entity, 10, 30),
#    ]),
#  ]),


winch = SceneProp("winch", "winch", "bo_winch")
winch.add_flag(ScenePropFlag.MOVEABLE)


winch_b = SceneProp("winch_b", "winch_b", "bo_winch")
winch_b.add_flag(ScenePropFlag.MOVEABLE)
winch_b.set_use_time(5)
# trigger 0
winch_b.add_trigger(check_item_use_trigger)


door_destructible = SceneProp("door_destructible", "tutorial_door_a","bo_tutorial_door_a")
door_destructible.add_flag(ScenePropFlag.MOVEABLE)
door_destructible.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
door_destructible.add_flag(ScenePropFlag.DESTRUCTIBLE)
door_destructible.set_use_time(2)
# trigger 0
door_destructible.add_trigger(check_item_use_trigger)
# trigger 1
triggy = SimpleTrigger(tri.ti_on_init_scene_prop)
def code(instance_no):
    scene_prop_set_hit_points(instance_no, 2000)
triggy.codeBlock = code
door_destructible.add_trigger(triggy)
# trigger 2
triggy = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(instance_no, attacker_agent_no):
    play_sound("snd_dummy_destroyed")
    rotate_side = 86

    if multiplayer_is_server() or not game_in_multiplayer_mode():
        set_fixed_point_multiplier(100)
        prop_instance_get_position(pos1, instance_no)

        if attacker_agent_no >= 0:
            agent_get_position(pos2, attacker_agent_no)
            if position_is_behind_position(pos2, pos1):
                rotate_side *= -1
            #end
        #end

        init_position(pos3)

        if rotate_side >= 0:
            position_move_y(pos3, -100)
        else:
            position_move_y(pos3, 100)

        position_move_x(pos3, -50)
        position_transform_position_to_parent(pos4, pos1, pos3)
        position_move_z(pos4, 100)
        height_to_terrain = position_get_distance_to_ground_level(pos4)

        height_to_terrain -= 100
        z_difference = height_to_terrain
        z_difference /= 3

        if rotate_side >= 0:
            rotate_side += z_difference
        else:
            rotate_side -= z_difference

        position_rotate_x(pos1, rotate_side)
        prop_instance_animate_to_position(instance_no, pos1, 70) #animate to position 1 in 0.7 second
    #end
triggy.codeBlock = code
door_destructible.add_trigger(triggy)
# trigger 3
triggy = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code():
    play_sound("snd_dummy_hit")
    particle_system_burst("psys_dummy_smoke", pos1, 3),
    particle_system_burst("psys_dummy_straw", pos1, 10),
triggy.codeBlock = code
door_destructible.add_trigger(triggy)


# TODO: doors
portcullis = SceneProp("portcullis")
castle_e_sally_door_a = SceneProp("castle_e_sally_door_a")
castle_f_sally_door_a = SceneProp("castle_f_sally_door_a")
earth_sally_gate_left = SceneProp("earth_sally_gate_left")
earth_sally_gate_right = SceneProp("earth_sally_gate_right")
viking_keep_destroy_sally_door_left = SceneProp("viking_keep_destroy_sally_door_left")
viking_keep_destroy_sally_door_right = SceneProp("viking_keep_destroy_sally_door_right")
castle_f_door_a = SceneProp("castle_f_door_a")


# TODO: ladders
siege_ladder_move_6m = SceneProp("siege_ladder_move_6m")
siege_ladder_move_8m = SceneProp("siege_ladder_move_8m")
siege_ladder_move_10m = SceneProp("siege_ladder_move_10m")
siege_ladder_move_12m = SceneProp("siege_ladder_move_12m")
siege_ladder_move_14m = SceneProp("siege_ladder_move_14m")


castle_f_door_b = SceneProp("castle_f_door_b", "castle_e_sally_door_a", "bo_castle_e_sally_door_a")
castle_f_door_b.add_flag(ScenePropFlag.MOVEABLE)
castle_f_door_b.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
castle_f_door_b.add_flag(ScenePropFlag.DESTRUCTIBLE)
castle_f_door_b.set_use_time(0)
# trigger 0
#castle_f_door_b.add_trigger(check_castle_door_use_trigger)
# trigger 1
triggy = SimpleTrigger(tri.ti_on_init_scene_prop)
def code(instance_no):
    scene_prop_set_hit_points(instance_no, 1000)
triggy.codeBlock = code
castle_f_door_b.add_trigger(triggy)

#("castle_f_door_b",sokf_moveable|sokf_show_hit_point_bar|sokf_destructible|spr_use_time(0),"castle_e_sally_door_a","bo_castle_e_sally_door_a", [




