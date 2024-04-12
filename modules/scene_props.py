# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")


from scene_prop import SceneProp, ScenePropFlag
from simple_trigger import SimpleTrigger
import header_triggers as tri




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
triggy = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(agent_id, instance_id):
    pass
triggy.codeBlock = code
winch_b.add_trigger(triggy)

# ("winch_b",sokf_moveable|spr_use_time(5),"winch_b","bo_winch", [
#  (ti_on_scene_prop_use,
#   [
#     (store_trigger_param_1, ":agent_id"),
#     (store_trigger_param_2, ":instance_id"),
#
#     #for only server itself-----------------------------------------------------------------------------------------------
#     (call_script, "script_use_item", ":instance_id", ":agent_id"),
#     #for only server itself-----------------------------------------------------------------------------------------------
#     (get_max_players, ":num_players"),
#     (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
#       (player_is_active, ":player_no"),
#       (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_use_item, ":instance_id", ":agent_id"),
#     (try_end),
#   ]),
# ]),




