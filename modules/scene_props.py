# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")


from scene_prop import SceneProp, ScenePropFlag
from simple_trigger import SimpleTrigger
import header_triggers as tri
import header_common as mcom
import sounds as snd



invalid_object = SceneProp("invalid_object", "question_mark", "0")

inventory = SceneProp("inventory", "package", "bobaggage")
inventory.add_flag(ScenePropFlag.TYPE_CONTAINER)
inventory.add_flag(ScenePropFlag.PLACE_AT_ORIGIN)

empty = SceneProp("empty", "0", "0")

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

light_sun = SceneProp("light_sun", "light_sphere", "0")
light_sun.add_flag(ScenePropFlag.INVISIBLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    if not is_currently_night():
        set_fixed_point_multiplier(100)
        s5 = prop_instance_get_scale(var001)
        pos_scale_x_002 = position_get_scale_x(5)
        reg12 = store_time_of_day()
        if is_between(reg12,5,20):
            var003 = 1000 * pos_scale_x_002
            var004 = 965 * pos_scale_x_002
            var005 = 900 * pos_scale_x_002
        else:
            var003 = 450 * pos_scale_x_002
            var004 = 575 * pos_scale_x_002
            var005 = 750 * pos_scale_x_002
        #end
    #end
    var003 /= 100
    var004 /= 100
    var005 /= 100
    set_current_color(var003,var004,var005)
    set_position_delta(0,0,0)
    add_point_light_to_entity(0,0)
trigger0.codeBlock = code
light_sun.add_trigger(trigger0)

light = SceneProp("light", "light_sphere", "0")
light.add_flag(ScenePropFlag.INVISIBLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    set_fixed_point_multiplier(100)
    s5 = prop_instance_get_scale(var001)
    pos_scale_x_002 = position_get_scale_x(5)
    var003 = 600 * pos_scale_x_002
    var004 = 435 * pos_scale_x_002
    var005 = 135 * pos_scale_x_002
    var003 /= 100
    var004 /= 100
    var005 /= 100
    set_current_color(var003,var004,var005)
    set_position_delta(0,0,0)
    add_point_light_to_entity(10,30)
trigger0.codeBlock = code
light.add_trigger(trigger0)

light_red = SceneProp("light_red", "light_sphere", "0")
light_red.add_flag(ScenePropFlag.INVISIBLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    set_fixed_point_multiplier(100)
    s5 = prop_instance_get_scale(var001)
    pos_scale_x_002 = position_get_scale_x(5)
    var003 = 340 * pos_scale_x_002
    var004 = 200 * pos_scale_x_002
    var005 = 60 * pos_scale_x_002
    var003 /= 100
    var004 /= 100
    var005 /= 100
    set_current_color(var003,var004,var005)
    set_position_delta(0,0,0)
    add_point_light_to_entity(20,30)
trigger0.codeBlock = code
light_red.add_trigger(trigger0)

light_night = SceneProp("light_night", "light_sphere", "0")
light_night.add_flag(ScenePropFlag.INVISIBLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    if is_currently_night(0):
        set_fixed_point_multiplier(100)
        s5 = prop_instance_get_scale(var001)
        pos_scale_x_002 = position_get_scale_x(5)
        var003 = 480 * pos_scale_x_002
        var004 = 435 * pos_scale_x_002
        var005 = 300 * pos_scale_x_002
        var003 /= 100
        var004 /= 100
        var005 /= 100
        set_current_color(var003,var004,var005)
        set_position_delta(0,0,0)
        add_point_light_to_entity(10,30)
trigger0.codeBlock = code
light_night.add_trigger(trigger0)

torch = SceneProp("torch", "torch_a", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    set_position_delta(0,-35,48)
    particle_system_add_new(psys.torch_fire)
    particle_system_add_new(psys.torch_smoke)
    particle_system_add_new(psys.torch_fire_sparks)
    play_sound(snd.torch_loop,0)
    set_position_delta(0,-35,56)
    particle_system_add_new(psys.fire_glow_1)
    pos2 = get_trigger_object_position()
    set_position_delta(0,0,0)
    position_move_y(2,-35)
    position_move_z(2,55)
    particle_system_burst(psys.fire_glow_fixed,2,1)
trigger0.codeBlock = code
torch.add_trigger(trigger0)

torch_night = SceneProp("torch_night", "torch_a", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    if is_currently_night(0):
        set_position_delta(0,-35,48)
        particle_system_add_new(psys.torch_fire)
        particle_system_add_new(psys.torch_smoke)
        particle_system_add_new(psys.torch_fire_sparks)
        set_position_delta(0,-35,56)
        particle_system_add_new(psys.fire_glow_1)
        particle_system_emit(psys.fire_glow_1,9000000)
        play_sound(snd.torch_loop,0)
trigger0.codeBlock = code
torch_night.add_trigger(trigger0)

barrier_20m = SceneProp("barrier_20m", "barrier_20m", "bo_barrier_20m")
barrier_20m.add_flag(ScenePropFlag.TYPE_BARRIER)
barrier_20m.add_flag(ScenePropFlag.INVISIBLE)

barrier_16m = SceneProp("barrier_16m", "barrier_16m", "bo_barrier_16m")
barrier_16m.add_flag(ScenePropFlag.TYPE_BARRIER)
barrier_16m.add_flag(ScenePropFlag.INVISIBLE)

barrier_8m = SceneProp("barrier_8m", "barrier_8m", "bo_barrier_8m")
barrier_8m.add_flag(ScenePropFlag.TYPE_BARRIER)
barrier_8m.add_flag(ScenePropFlag.INVISIBLE)

barrier_4m = SceneProp("barrier_4m", "barrier_4m", "bo_barrier_4m")
barrier_4m.add_flag(ScenePropFlag.TYPE_BARRIER)
barrier_4m.add_flag(ScenePropFlag.INVISIBLE)

barrier_2m = SceneProp("barrier_2m", "barrier_2m", "bo_barrier_2m")
barrier_2m.add_flag(ScenePropFlag.TYPE_BARRIER)
barrier_2m.add_flag(ScenePropFlag.INVISIBLE)

exit_4m = SceneProp("exit_4m", "barrier_4m", "bo_barrier_4m")
exit_4m.add_flag(ScenePropFlag.TYPE_BARRIER_LEAVE)
exit_4m.add_flag(ScenePropFlag.INVISIBLE)

exit_8m = SceneProp("exit_8m", "barrier_8m", "bo_barrier_8m")
exit_8m.add_flag(ScenePropFlag.TYPE_BARRIER_LEAVE)
exit_8m.add_flag(ScenePropFlag.INVISIBLE)

exit_16m = SceneProp("exit_16m", "barrier_16m", "bo_barrier_16m")
exit_16m.add_flag(ScenePropFlag.TYPE_BARRIER_LEAVE)
exit_16m.add_flag(ScenePropFlag.INVISIBLE)

ai_limiter_2m = SceneProp("ai_limiter_2m", "barrier_2m", "bo_barrier_2m")
ai_limiter_2m.add_flag(ScenePropFlag.TYPE_AI_LIMITER)
ai_limiter_2m.add_flag(ScenePropFlag.INVISIBLE)

ai_limiter_4m = SceneProp("ai_limiter_4m", "barrier_4m", "bo_barrier_4m")
ai_limiter_4m.add_flag(ScenePropFlag.TYPE_AI_LIMITER)
ai_limiter_4m.add_flag(ScenePropFlag.INVISIBLE)

ai_limiter_8m = SceneProp("ai_limiter_8m", "barrier_8m", "bo_barrier_8m")
ai_limiter_8m.add_flag(ScenePropFlag.TYPE_AI_LIMITER)
ai_limiter_8m.add_flag(ScenePropFlag.INVISIBLE)

ai_limiter_16m = SceneProp("ai_limiter_16m", "barrier_16m", "bo_barrier_16m")
ai_limiter_16m.add_flag(ScenePropFlag.TYPE_AI_LIMITER)
ai_limiter_16m.add_flag(ScenePropFlag.INVISIBLE)

Shield = SceneProp("Shield", "0", "boshield")
Shield.add_flag(ScenePropFlag.DYNAMIC)

shelves = SceneProp("shelves", "shelves", "boshelves")

table_tavern = SceneProp("table_tavern", "table_tavern", "botable_tavern")

table_castle_a = SceneProp("table_castle_a", "table_castle_a", "bo_table_castle_a")

chair_castle_a = SceneProp("chair_castle_a", "chair_castle_a", "bo_chair_castle_a")

pillow_a = SceneProp("pillow_a", "pillow_a", "bo_pillow")

pillow_b = SceneProp("pillow_b", "pillow_b", "bo_pillow")

pillow_c = SceneProp("pillow_c", "pillow_c", "0")

interior_castle_g_square_keep_b = SceneProp("interior_castle_g_square_keep_b", "interior_castle_g_square_keep_b", "bo_interior_castle_g_square_keep_b")

carpet_with_pillows_a = SceneProp("carpet_with_pillows_a", "carpet_with_pillows_a", "bo_carpet_with_pillows")

carpet_with_pillows_b = SceneProp("carpet_with_pillows_b", "carpet_with_pillows_b", "bo_carpet_with_pillows")

table_round_a = SceneProp("table_round_a", "table_round_a", "bo_table_round_a")

table_round_b = SceneProp("table_round_b", "table_round_b", "bo_table_round_b")

fireplace_b = SceneProp("fireplace_b", "fireplace_b", "bo_fireplace_b")

fireplace_c = SceneProp("fireplace_c", "fireplace_c", "bo_fireplace_c")

sofa_a = SceneProp("sofa_a", "sofa_a", "bo_sofa")

sofa_b = SceneProp("sofa_b", "sofa_b", "bo_sofa")

ewer_a = SceneProp("ewer_a", "ewer_a", "bo_ewer_a")

end_table_a = SceneProp("end_table_a", "end_table_a", "bo_end_table_a")

fake_houses_steppe_a = SceneProp("fake_houses_steppe_a", "fake_houses_steppe_a", "0")

fake_houses_steppe_b = SceneProp("fake_houses_steppe_b", "fake_houses_steppe_b", "0")

fake_houses_steppe_c = SceneProp("fake_houses_steppe_c", "fake_houses_steppe_c", "0")

boat_destroy = SceneProp("boat_destroy", "boat_destroy", "bo_boat_destroy")

destroy_house_a = SceneProp("destroy_house_a", "destroy_house_a", "bo_destroy_house_a")

destroy_house_b = SceneProp("destroy_house_b", "destroy_house_b", "bo_destroy_house_b")

destroy_house_c = SceneProp("destroy_house_c", "destroy_house_c", "bo_destroy_house_c")

destroy_heap = SceneProp("destroy_heap", "destroy_heap", "bo_destroy_heap")

destroy_castle_a = SceneProp("destroy_castle_a", "destroy_castle_a", "bo_destroy_castle_a")

destroy_castle_b = SceneProp("destroy_castle_b", "destroy_castle_b", "bo_destroy_castle_b")

destroy_castle_c = SceneProp("destroy_castle_c", "destroy_castle_c", "bo_destroy_castle_c")

destroy_castle_d = SceneProp("destroy_castle_d", "destroy_castle_d", "bo_destroy_castle_d")

destroy_windmill = SceneProp("destroy_windmill", "destroy_windmill", "bo_destroy_windmill")

destroy_tree_a = SceneProp("destroy_tree_a", "destroy_tree_a", "bo_destroy_tree_a")

destroy_tree_b = SceneProp("destroy_tree_b", "destroy_tree_b", "bo_destroy_tree_b")

destroy_bridge_a = SceneProp("destroy_bridge_a", "destroy_bridge_a", "bo_destroy_bridge_a")

destroy_bridge_b = SceneProp("destroy_bridge_b", "destroy_bridge_b", "bo_destroy_bridge_b")

catapult = SceneProp("catapult", "Catapult", "bo_Catapult")

catapult_destructible = SceneProp("catapult_destructible", "Catapult", "bo_Catapult")
catapult_destructible.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
catapult_destructible.add_flag(ScenePropFlag.DESTRUCTIBLE)
catapult_destructible.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,1600)
trigger0.codeBlock = code
catapult_destructible.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var001):
    play_sound(snd.dummy_destroyed)
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        pos1 = prop_instance_get_position(var001)
        particle_system_burst(psys.dummy_smoke_big,1,100)
        particle_system_burst(psys.dummy_straw_big,1,100)
        position_move_z(1,-500)
        position_rotate_x(1,90)
        prop_instance_animate_to_position(var001,1,300)
        if _g_round_ended == 0:
            team_no_002 = scene_prop_get_team(var001)
            if team_no_002 == 0:
                var003 = -1
            else:
                var003 = 1
            #end
            if _g_number_of_targets_destroyed == 0:
                var004 = var003 * 1
                show_multiplayer_message(15,var004)
                max_players = get_max_players()
                for player_id_006 in range(1, max_players):
                    if player_is_active(player_id_006):
                        multiplayer_send_2_int_to_player(player_id_006,68,15,var004)
                    #end
                #end
                _g_number_of_targets_destroyed += 1
            else:
                var004 = var003 * 9
                show_multiplayer_message(15,var004)
                max_players = get_max_players()
                for player_id_006 in range(1, max_players):
                    if player_is_active(player_id_006):
                        multiplayer_send_2_int_to_player(player_id_006,68,15,var004)
                    #end
                #end
                _g_number_of_targets_destroyed += 1
            #end
        #end
        var007 = 0
        max_players = get_max_players()
        for player_id_006 in range(0, max_players):
            if player_is_active(player_id_006):
                if spr.catapult_destructible == _g_destructible_target_1:
                    player_slot_008 = player_get_slot(player_id_006,32)
                else:
                    player_slot_008 = player_get_slot(player_id_006,33)
                #end
            #end
            var007 += player_slot_008
        #end
        var009 = 0
        max_players = get_max_players()
        for player_id_006 in range(0, max_players):
            if player_is_active(player_id_006):
                var009 += 50
            #end
        #end
        if var009 >= 1500:
            var009 = 1500
        #end
        var009 *= _g_multiplayer_battle_earnings_multiplier
        var009 /= 100
        max_players = get_max_players()
        for player_id_006 in range(0, max_players):
            if player_is_active(player_id_006):
                if spr.catapult_destructible == _g_destructible_target_1:
                    player_slot_008 = player_get_slot(player_id_006,32)
                else:
                    player_slot_008 = player_get_slot(player_id_006,33)
                #end
            #end
            gold_010 = player_get_gold(player_id_006)
            player_slot_008 *= var009
            if var007 >= player_slot_008 and player_slot_008 > 0:
                var011 = player_slot_008 / var007
            else:
                var011 = 0
            #end
            gold_010 += var011
            player_set_gold(player_id_006,gold_010,15000)
        #end
    #end
trigger1.codeBlock = code
catapult_destructible.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
        set_fixed_point_multiplier(1)
        pos_x_004 = position_get_x(2)
        if pos_x_004 >= 0 and agent_is_alive(pos_x_004) and agent_is_human(pos_x_004) and not agent_is_non_player(pos_x_004):
            agent_player_id_005 = agent_get_player_id(pos_x_004)
            if agent_player_id_005 >= 0 and player_is_active(agent_player_id_005):
                if spr.catapult_destructible == _g_destructible_target_1:
                    player_slot_006 = player_get_slot(agent_player_id_005,32)
                    player_slot_006 += var002
                    player_set_slot(agent_player_id_005,32,player_slot_006)
                else:
                    player_slot_006 = player_get_slot(agent_player_id_005,33)
                    player_slot_006 += var002
                    player_set_slot(agent_player_id_005,33,player_slot_006)
                #end
            #end
        #end
    #end
trigger2.codeBlock = code
catapult_destructible.add_trigger(trigger2)

broom = SceneProp("broom", "broom", "0")

garlic = SceneProp("garlic", "garlic", "0")

garlic_b = SceneProp("garlic_b", "garlic_b", "0")

destroy_a = SceneProp("destroy_a", "destroy_a", "0")

destroy_b = SceneProp("destroy_b", "destroy_b", "0")

bridge_wooden = SceneProp("bridge_wooden", "bridge_wooden", "bo_bridge_wooden")

bridge_wooden_snowy = SceneProp("bridge_wooden_snowy", "bridge_wooden_snowy", "bo_bridge_wooden")

grave_a = SceneProp("grave_a", "grave_a", "bo_grave_a")

village_house_e = SceneProp("village_house_e", "village_house_e", "bo_village_house_e")

village_house_f = SceneProp("village_house_f", "village_house_f", "bo_village_house_f")

village_house_g = SceneProp("village_house_g", "village_house_g", "bo_village_house_g")

village_house_h = SceneProp("village_house_h", "village_house_h", "bo_village_house_h")

village_house_i = SceneProp("village_house_i", "village_house_i", "bo_village_house_i")

village_house_j = SceneProp("village_house_j", "village_house_j", "bo_village_house_j")

village_wall_a = SceneProp("village_wall_a", "village_wall_a", "bo_village_wall_a")

village_wall_b = SceneProp("village_wall_b", "village_wall_b", "bo_village_wall_b")

village_snowy_house_a = SceneProp("village_snowy_house_a", "village_snowy_house_a", "bo_village_snowy_house_a")

village_snowy_house_b = SceneProp("village_snowy_house_b", "village_snowy_house_b", "bo_village_snowy_house_b")

village_snowy_house_c = SceneProp("village_snowy_house_c", "village_snowy_house_c", "bo_village_snowy_house_c")

village_snowy_house_d = SceneProp("village_snowy_house_d", "village_snowy_house_d", "bo_village_snowy_house_d")

village_snowy_house_e = SceneProp("village_snowy_house_e", "village_snowy_house_e", "bo_village_snowy_house_e")

village_snowy_house_f = SceneProp("village_snowy_house_f", "village_snowy_house_f", "bo_village_snowy_house_f")

town_house_steppe_a = SceneProp("town_house_steppe_a", "town_house_steppe_a", "bo_town_house_steppe_a")

town_house_steppe_b = SceneProp("town_house_steppe_b", "town_house_steppe_b", "bo_town_house_steppe_b")

town_house_steppe_c = SceneProp("town_house_steppe_c", "town_house_steppe_c", "bo_town_house_steppe_c")

town_house_steppe_d = SceneProp("town_house_steppe_d", "town_house_steppe_d", "bo_town_house_steppe_d")

town_house_steppe_e = SceneProp("town_house_steppe_e", "town_house_steppe_e", "bo_town_house_steppe_e")

town_house_steppe_f = SceneProp("town_house_steppe_f", "town_house_steppe_f", "bo_town_house_steppe_f")

town_house_steppe_g = SceneProp("town_house_steppe_g", "town_house_steppe_g", "bo_town_house_steppe_g")

town_house_steppe_h = SceneProp("town_house_steppe_h", "town_house_steppe_h", "bo_town_house_steppe_h")

town_house_steppe_i = SceneProp("town_house_steppe_i", "town_house_steppe_i", "bo_town_house_steppe_i")

carpet_a = SceneProp("carpet_a", "carpet_a", "0")

carpet_b = SceneProp("carpet_b", "carpet_b", "0")

carpet_c = SceneProp("carpet_c", "carpet_c", "0")

carpet_d = SceneProp("carpet_d", "carpet_d", "0")

carpet_e = SceneProp("carpet_e", "carpet_e", "0")

carpet_f = SceneProp("carpet_f", "carpet_f", "0")

awning_a = SceneProp("awning_a", "awning_a", "bo_awning")

awning_b = SceneProp("awning_b", "awning_b", "bo_awning")

awning_c = SceneProp("awning_c", "awning_c", "bo_awning")

awning_long = SceneProp("awning_long", "awning_long", "bo_awning_long")

awning_long_b = SceneProp("awning_long_b", "awning_long_b", "bo_awning_long")

awning_d = SceneProp("awning_d", "awning_d", "bo_awning_d")

ship = SceneProp("ship", "ship", "bo_ship")

ship_b = SceneProp("ship_b", "ship_b", "bo_ship_b")

ship_c = SceneProp("ship_c", "ship_c", "bo_ship_c")

ship_d = SceneProp("ship_d", "ship_d", "bo_ship_d")

snowy_barrel_a = SceneProp("snowy_barrel_a", "snowy_barrel_a", "bo_snowy_barrel_a")

snowy_fence = SceneProp("snowy_fence", "snowy_fence", "bo_snowy_fence")

snowy_wood_heap = SceneProp("snowy_wood_heap", "snowy_wood_heap", "bo_snowy_wood_heap")

village_snowy_stable_a = SceneProp("village_snowy_stable_a", "village_snowy_stable_a", "bo_village_snowy_stable_a")

village_straw_house_a = SceneProp("village_straw_house_a", "village_straw_house_a", "bo_village_straw_house_a")

village_stable_a = SceneProp("village_stable_a", "village_stable_a", "bo_village_stable_a")

village_shed_a = SceneProp("village_shed_a", "village_shed_a", "bo_village_shed_a")

village_shed_b = SceneProp("village_shed_b", "village_shed_b", "bo_village_shed_b")

dungeon_door_cell_a = SceneProp("dungeon_door_cell_a", "dungeon_door_cell_a", "bo_dungeon_door_cell_a")

dungeon_door_cell_b = SceneProp("dungeon_door_cell_b", "dungeon_door_cell_b", "bo_dungeon_door_cell_b")

dungeon_door_entry_a = SceneProp("dungeon_door_entry_a", "dungeon_door_entry_a", "bo_dungeon_door_entry_a")

dungeon_door_entry_b = SceneProp("dungeon_door_entry_b", "dungeon_door_entry_b", "bo_dungeon_door_entry_a")

dungeon_door_entry_c = SceneProp("dungeon_door_entry_c", "dungeon_door_entry_c", "bo_dungeon_door_entry_a")

dungeon_door_direction_a = SceneProp("dungeon_door_direction_a", "dungeon_door_direction_a", "bo_dungeon_door_direction_a")

dungeon_door_direction_b = SceneProp("dungeon_door_direction_b", "dungeon_door_direction_b", "bo_dungeon_door_direction_a")

dungeon_door_stairs_a = SceneProp("dungeon_door_stairs_a", "dungeon_door_stairs_a", "bo_dungeon_door_stairs_a")

dungeon_door_stairs_b = SceneProp("dungeon_door_stairs_b", "dungeon_door_stairs_b", "bo_dungeon_door_stairs_a")

dungeon_bed_a = SceneProp("dungeon_bed_a", "dungeon_bed_a", "0")

dungeon_bed_b = SceneProp("dungeon_bed_b", "dungeon_bed_b", "bo_dungeon_bed_b")

torture_tool_a = SceneProp("torture_tool_a", "torture_tool_a", "bo_torture_tool_a")

torture_tool_b = SceneProp("torture_tool_b", "torture_tool_b", "0")

torture_tool_c = SceneProp("torture_tool_c", "torture_tool_c", "bo_torture_tool_c")

skeleton_head = SceneProp("skeleton_head", "skeleton_head", "0")

skeleton_bone = SceneProp("skeleton_bone", "skeleton_bone", "0")

skeleton_a = SceneProp("skeleton_a", "skeleton_a", "bo_skeleton_a")

dungeon_stairs_a = SceneProp("dungeon_stairs_a", "dungeon_stairs_a", "bo_dungeon_stairs_a")
dungeon_stairs_a.add_flag(ScenePropFlag.TYPE_LADDER)

dungeon_stairs_b = SceneProp("dungeon_stairs_b", "dungeon_stairs_b", "bo_dungeon_stairs_a")
dungeon_stairs_b.add_flag(ScenePropFlag.TYPE_LADDER)

dungeon_torture_room_a = SceneProp("dungeon_torture_room_a", "dungeon_torture_room_a", "bo_dungeon_torture_room_a")

dungeon_entry_a = SceneProp("dungeon_entry_a", "dungeon_entry_a", "bo_dungeon_entry_a")

dungeon_entry_b = SceneProp("dungeon_entry_b", "dungeon_entry_b", "bo_dungeon_entry_b")

dungeon_entry_c = SceneProp("dungeon_entry_c", "dungeon_entry_c", "bo_dungeon_entry_c")

dungeon_cell_a = SceneProp("dungeon_cell_a", "dungeon_cell_a", "bo_dungeon_cell_a")

dungeon_cell_b = SceneProp("dungeon_cell_b", "dungeon_cell_b", "bo_dungeon_cell_b")

dungeon_cell_c = SceneProp("dungeon_cell_c", "dungeon_cell_c", "bo_dungeon_cell_c")

dungeon_corridor_a = SceneProp("dungeon_corridor_a", "dungeon_corridor_a", "bo_dungeon_corridor_a")

dungeon_corridor_b = SceneProp("dungeon_corridor_b", "dungeon_corridor_b", "bo_dungeon_corridor_b")

dungeon_corridor_c = SceneProp("dungeon_corridor_c", "dungeon_corridor_c", "bo_dungeon_corridor_b")

dungeon_corridor_d = SceneProp("dungeon_corridor_d", "dungeon_corridor_d", "bo_dungeon_corridor_b")

dungeon_direction_a = SceneProp("dungeon_direction_a", "dungeon_direction_a", "bo_dungeon_direction_a")

dungeon_direction_b = SceneProp("dungeon_direction_b", "dungeon_direction_b", "bo_dungeon_direction_a")

dungeon_room_a = SceneProp("dungeon_room_a", "dungeon_room_a", "bo_dungeon_room_a")

dungeon_tower_stairs_a = SceneProp("dungeon_tower_stairs_a", "dungeon_tower_stairs_a", "bo_dungeon_tower_stairs_a")
dungeon_tower_stairs_a.add_flag(ScenePropFlag.TYPE_LADDER)

dungeon_tower_cell_a = SceneProp("dungeon_tower_cell_a", "dungeon_tower_cell_a", "bo_dungeon_tower_cell_a")

tunnel_a = SceneProp("tunnel_a", "tunnel_a", "bo_tunnel_a")

tunnel_salt = SceneProp("tunnel_salt", "tunnel_salt", "bo_tunnel_salt")

salt_a = SceneProp("salt_a", "salt_a", "bo_salt_a")

door_destructible = SceneProp("door_destructible", "tutorial_door_a", "bo_tutorial_door_a")
door_destructible.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
door_destructible.add_flag(ScenePropFlag.DESTRUCTIBLE)
door_destructible.add_flag(ScenePropFlag.MOVEABLE)
door_destructible.set_use_time(2)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, var002):
    use_item(var002,var001)
    max_players = get_max_players()
    for player_id_004 in range(1, max_players):
        if player_is_active(player_id_004):
            multiplayer_send_2_int_to_player(player_id_004,76,var002,var001)
        #end
    #end
trigger0.codeBlock = code
door_destructible.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,2000)
trigger1.codeBlock = code
door_destructible.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var002, var003):
    play_sound(snd.dummy_destroyed)
    var001 = 86
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        set_fixed_point_multiplier(100)
        pos1 = prop_instance_get_position(var002)
        if var003 >= 0:
            pos2 = agent_get_position(var003)
            if position_is_behind_position(2,1):
                var001 *= -1
            #end
        #end
        init_position(3)
        if var001 >= 0:
            position_move_y(3,-100)
        else:
            position_move_y(3,100)
        #end
        position_move_x(3,-50)
        position_transform_position_to_parent(4,1,3)
        position_move_z(4,100)
        distance_to_ground_level_004 = position_get_distance_to_ground_level(4)
        distance_to_ground_level_004 -= 100
        var005 = distance_to_ground_level_004
        var005 /= 3
        if var001 >= 0:
            var001 += var005
        else:
            var001 -= var005
        #end
        position_rotate_x(1,var001)
        prop_instance_animate_to_position(var002,1,70)
    #end
trigger2.codeBlock = code
door_destructible.add_trigger(trigger2)
# trigger3
trigger3 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code():
    play_sound(snd.dummy_hit)
    particle_system_burst(psys.dummy_smoke,1,3)
    particle_system_burst(psys.dummy_straw,1,10)
trigger3.codeBlock = code
door_destructible.add_trigger(trigger3)

tutorial_door_a = SceneProp("tutorial_door_a", "tutorial_door_a", "bo_tutorial_door_a")
tutorial_door_a.add_flag(ScenePropFlag.MOVEABLE)

tutorial_door_b = SceneProp("tutorial_door_b", "tutorial_door_b", "bo_tutorial_door_b")
tutorial_door_b.add_flag(ScenePropFlag.MOVEABLE)

tutorial_flag_yellow = SceneProp("tutorial_flag_yellow", "tutorial_flag_yellow", "0")
tutorial_flag_yellow.add_flag(ScenePropFlag.MOVEABLE)
tutorial_flag_yellow.add_flag(ScenePropFlag.FACE_PLAYER)

tutorial_flag_red = SceneProp("tutorial_flag_red", "tutorial_flag_red", "0")
tutorial_flag_red.add_flag(ScenePropFlag.MOVEABLE)
tutorial_flag_red.add_flag(ScenePropFlag.FACE_PLAYER)

tutorial_flag_blue = SceneProp("tutorial_flag_blue", "tutorial_flag_blue", "0")
tutorial_flag_blue.add_flag(ScenePropFlag.MOVEABLE)
tutorial_flag_blue.add_flag(ScenePropFlag.FACE_PLAYER)

interior_prison_a = SceneProp("interior_prison_a", "interior_prison_a", "bo_interior_prison_a")

interior_prison_b = SceneProp("interior_prison_b", "interior_prison_b", "bo_interior_prison_b")

interior_prison_cell_a = SceneProp("interior_prison_cell_a", "interior_prison_cell_a", "bo_interior_prison_cell_a")

interior_prison_d = SceneProp("interior_prison_d", "interior_prison_d", "bo_interior_prison_d")

arena_archery_target_a = SceneProp("arena_archery_target_a", "arena_archery_target_a", "bo_arena_archery_target_a")

archery_butt_a = SceneProp("archery_butt_a", "archery_butt", "bo_archery_butt")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001):
    pos2 = prop_instance_get_position(var001)
    agent_no_002 = get_player_agent_no()
    pos3 = agent_get_position(agent_no_002)
    distance_003 = get_distance_between_positions(3,2)
    position_transform_position_to_local(4,2,1)
    position_set_y(4,0)
    position_set_x(2,0)
    position_set_y(2,0)
    position_set_z(2,0)
    distance_004 = get_distance_between_positions(4,2)
    var005 = 43
    var005 -= distance_004
    var005 *= 1299
    var005 /= 4300
    if var005 < 0:
        var005 = 0
    #end
    distance_003 /= 91
    reg60 = var005
    reg61 = distance_003
    print(gstr.archery_target_hit)
trigger0.codeBlock = code
archery_butt_a.add_trigger(trigger0)

archery_target_with_hit_a = SceneProp("archery_target_with_hit_a", "arena_archery_target_a", "bo_arena_archery_target_a")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001):
    set_fixed_point_multiplier(100)
    pos_x_002 = position_get_x(2)
    pos_x_002 /= 100
    agent_no_003 = get_player_agent_no()
    if agent_no_003 == pos_x_002:
        pos2 = prop_instance_get_position(var001)
        pos3 = agent_get_position(agent_no_003)
        distance_004 = get_distance_between_positions(3,2)
        position_transform_position_to_local(4,2,1)
        position_set_y(4,0)
        position_set_x(2,0)
        position_set_y(2,0)
        position_set_z(2,0)
        distance_005 = get_distance_between_positions(4,2)
        var006 = 43
        var006 -= distance_005
        var006 *= 1299
        var006 /= 4300
        if var006 < 0:
            var006 = 0
        #end
        _g_last_archery_point_earned = var006
        distance_004 /= 91
        reg60 = var006
        reg61 = distance_004
        print(gstr.archery_target_hit)
        if _g_tutorial_training_ground_horseman_trainer_state == 6 and _g_tutorial_training_ground_horseman_trainer_completed_chapters == 2:
            prop_variation_id_2__007 = prop_instance_get_variation_id_2(var001)
            prop_variation_id_2__007 -= 1
            if _g_tutorial_training_ground_current_score == prop_variation_id_2__007:
                _g_tutorial_training_ground_current_score += 1
            #end
        #end
    #end
trigger0.codeBlock = code
archery_target_with_hit_a.add_trigger(trigger0)

dummy_a = SceneProp("dummy_a", "arena_archery_target_b", "bo_arena_archery_target_b")
dummy_a.add_flag(ScenePropFlag.DESTRUCTIBLE)
dummy_a.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var001):
    pos1 = prop_instance_get_starting_position(var001)
    agent_no_002 = get_player_agent_no()
    pos2 = agent_get_position(agent_no_002)
    var003 = 80
    if position_is_behind_position(2,1):
        var003 *= -1
    #end
    position_rotate_x(1,var003)
    prop_instance_animate_to_position(var001,1,70)
    _tutorial_num_total_dummies_destroyed += 1
    play_sound(snd.dummy_destroyed)
trigger0.codeBlock = code
dummy_a.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    reg60 = var002
    var002 /= 8
    pos2 = prop_instance_get_position(var001)
    agent_no_003 = get_player_agent_no()
    pos3 = agent_get_position(agent_no_003)
    if position_is_behind_position(3,2):
        var002 *= -1
    #end
    position_rotate_x(2,var002)
    print(gstr.delivered_damage)
    prop_instance_animate_to_position(var001,2,30)
    play_sound(snd.dummy_hit)
    particle_system_burst(psys.dummy_smoke,1,3)
    particle_system_burst(psys.dummy_straw,1,10)
trigger1.codeBlock = code
dummy_a.add_trigger(trigger1)

band_a = SceneProp("band_a", "band_a", "0")

arena_sign = SceneProp("arena_sign", "arena_arms", "0")

castle_h_battlement_a = SceneProp("castle_h_battlement_a", "castle_h_battlement_a", "bo_castle_h_battlement_a")

castle_h_battlement_b = SceneProp("castle_h_battlement_b", "castle_h_battlement_b", "bo_castle_h_battlement_b")

castle_h_battlement_c = SceneProp("castle_h_battlement_c", "castle_h_battlement_c", "bo_castle_h_battlement_c")

castle_h_battlement_a2 = SceneProp("castle_h_battlement_a2", "castle_h_battlement_a2", "bo_castle_h_battlement_a2")

castle_h_battlement_b2 = SceneProp("castle_h_battlement_b2", "castle_h_battlement_b2", "bo_castle_h_battlement_b2")

castle_h_corner_a = SceneProp("castle_h_corner_a", "castle_h_corner_a", "bo_castle_h_corner_a")

castle_h_corner_c = SceneProp("castle_h_corner_c", "castle_h_corner_c", "bo_castle_h_corner_c")

castle_h_stairs_a = SceneProp("castle_h_stairs_a", "castle_h_stairs_a", "bo_castle_h_stairs_a")
castle_h_stairs_a.add_flag(ScenePropFlag.TYPE_LADDER)

castle_h_stairs_b = SceneProp("castle_h_stairs_b", "castle_h_stairs_b", "bo_castle_h_stairs_b")

castle_h_gatehouse_a = SceneProp("castle_h_gatehouse_a", "castle_h_gatehouse_a", "bo_castle_h_gatehouse_a")

castle_h_keep_a = SceneProp("castle_h_keep_a", "castle_h_keep_a", "bo_castle_h_keep_a")

castle_h_keep_b = SceneProp("castle_h_keep_b", "castle_h_keep_b", "bo_castle_h_keep_b")

castle_h_house_a = SceneProp("castle_h_house_a", "castle_h_house_a", "bo_castle_h_house_a")

castle_h_house_b = SceneProp("castle_h_house_b", "castle_h_house_b", "bo_castle_h_house_b")

castle_h_house_c = SceneProp("castle_h_house_c", "castle_h_house_c", "bo_castle_h_house_b")

castle_h_battlement_barrier = SceneProp("castle_h_battlement_barrier", "castle_h_battlement_barrier", "bo_castle_h_battlement_barrier")

full_keep_b = SceneProp("full_keep_b", "full_keep_b", "bo_full_keep_b")

castle_f_keep_a = SceneProp("castle_f_keep_a", "castle_f_keep_a", "bo_castle_f_keep_a")

castle_f_battlement_a = SceneProp("castle_f_battlement_a", "castle_f_battlement_a", "bo_castle_f_battlement_a")

castle_f_battlement_a_destroyed = SceneProp("castle_f_battlement_a_destroyed", "castle_f_battlement_a_destroyed", "bo_castle_f_battlement_a_destroyed")

castle_f_battlement_b = SceneProp("castle_f_battlement_b", "castle_f_battlement_b", "bo_castle_f_battlement_b")

castle_f_battlement_c = SceneProp("castle_f_battlement_c", "castle_f_battlement_c", "bo_castle_f_battlement_c")

castle_f_battlement_d = SceneProp("castle_f_battlement_d", "castle_f_battlement_d", "bo_castle_f_battlement_d")

castle_f_battlement_e = SceneProp("castle_f_battlement_e", "castle_f_battlement_e", "bo_castle_f_battlement_e")

castle_f_sally_port_elevation = SceneProp("castle_f_sally_port_elevation", "castle_f_sally_port_elevation", "bo_castle_f_sally_port_elevation")

castle_f_battlement_corner_a = SceneProp("castle_f_battlement_corner_a", "castle_f_battlement_corner_a", "bo_castle_f_battlement_corner_a")

castle_f_battlement_corner_b = SceneProp("castle_f_battlement_corner_b", "castle_f_battlement_corner_b", "bo_castle_f_battlement_corner_b")

castle_f_battlement_corner_c = SceneProp("castle_f_battlement_corner_c", "castle_f_battlement_corner_c", "bo_castle_f_battlement_corner_c")

castle_f_door_a = SceneProp("castle_f_door_a", "castle_f_door_a", "bo_castle_f_door_a")
castle_f_door_a.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
castle_f_door_a.add_flag(ScenePropFlag.DESTRUCTIBLE)
castle_f_door_a.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, scene_prop_instance_id_002):
    pos1 = agent_get_position(var001)
    pos2 = prop_instance_get_starting_position(scene_prop_instance_id_002)
    scene_prop_slot_003 = scene_prop_get_slot(scene_prop_instance_id_002,1)
    if var001 >= 0:
        agent_team_no_004 = agent_get_team(var001)
        if agent_team_no_004 == 0 or scene_prop_slot_003 == 1:
            if True:
                use_item(scene_prop_instance_id_002,var001)
                max_players = get_max_players()
                for player_id_006 in range(1, max_players):
                    if player_is_active(player_id_006):
                        multiplayer_send_2_int_to_player(player_id_006,76,scene_prop_instance_id_002,var001)
                    #end
                #end
            #end
        #end
    #end
trigger0.codeBlock = code
castle_f_door_a.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,1000)
trigger1.codeBlock = code
castle_f_door_a.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var002, var003):
    play_sound(snd.dummy_destroyed)
    var001 = 86
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        set_fixed_point_multiplier(100)
        pos1 = prop_instance_get_position(var002)
        if var003 >= 0:
            pos2 = agent_get_position(var003)
            if position_is_behind_position(2,1):
                var001 *= -1
            #end
        #end
        init_position(3)
        if var001 >= 0:
            position_move_y(3,-100)
        else:
            position_move_y(3,100)
        #end
        position_move_x(3,-50)
        position_transform_position_to_parent(4,1,3)
        position_move_z(4,100)
        distance_to_ground_level_004 = position_get_distance_to_ground_level(4)
        distance_to_ground_level_004 -= 100
        var005 = distance_to_ground_level_004
        var005 /= 3
        if var001 >= 0:
            var001 += var005
        else:
            var001 -= var005
        #end
        position_rotate_x(1,var001)
        prop_instance_animate_to_position(var002,1,70)
    #end
trigger2.codeBlock = code
castle_f_door_a.add_trigger(trigger2)
# trigger3
trigger3 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
    #end
trigger3.codeBlock = code
castle_f_door_a.add_trigger(trigger3)

castle_f_doors_top_a = SceneProp("castle_f_doors_top_a", "castle_f_doors_top_a", "bo_castle_f_doors_top_a")

castle_f_sally_door_a = SceneProp("castle_f_sally_door_a", "castle_f_sally_door_a", "bo_castle_f_sally_door_a")
castle_f_sally_door_a.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
castle_f_sally_door_a.add_flag(ScenePropFlag.DESTRUCTIBLE)
castle_f_sally_door_a.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, scene_prop_instance_id_002):
    pos1 = agent_get_position(var001)
    pos2 = prop_instance_get_starting_position(scene_prop_instance_id_002)
    scene_prop_slot_003 = scene_prop_get_slot(scene_prop_instance_id_002,1)
    if position_is_behind_position(1,2) or scene_prop_slot_003 == 1:
        if True:
            use_item(scene_prop_instance_id_002,var001)
            max_players = get_max_players()
            for player_id_005 in range(1, max_players):
                if player_is_active(player_id_005):
                    multiplayer_send_2_int_to_player(player_id_005,76,scene_prop_instance_id_002,var001)
                #end
            #end
        #end
    #end
trigger0.codeBlock = code
castle_f_sally_door_a.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,1000)
trigger1.codeBlock = code
castle_f_sally_door_a.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var002, var003):
    play_sound(snd.dummy_destroyed)
    var001 = 86
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        set_fixed_point_multiplier(100)
        pos1 = prop_instance_get_position(var002)
        if var003 >= 0:
            pos2 = agent_get_position(var003)
            if position_is_behind_position(2,1):
                var001 *= -1
            #end
        #end
        init_position(3)
        if var001 >= 0:
            position_move_y(3,-100)
        else:
            position_move_y(3,100)
        #end
        position_move_x(3,-50)
        position_transform_position_to_parent(4,1,3)
        position_move_z(4,100)
        distance_to_ground_level_004 = position_get_distance_to_ground_level(4)
        distance_to_ground_level_004 -= 100
        var005 = distance_to_ground_level_004
        var005 /= 3
        if var001 >= 0:
            var001 += var005
        else:
            var001 -= var005
        #end
        position_rotate_x(1,var001)
        prop_instance_animate_to_position(var002,1,70)
    #end
trigger2.codeBlock = code
castle_f_sally_door_a.add_trigger(trigger2)
# trigger3
trigger3 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
    #end
trigger3.codeBlock = code
castle_f_sally_door_a.add_trigger(trigger3)

castle_f_stairs_a = SceneProp("castle_f_stairs_a", "castle_f_stairs_a", "bo_castle_f_stairs_a")
castle_f_stairs_a.add_flag(ScenePropFlag.TYPE_LADDER)

castle_f_tower_a = SceneProp("castle_f_tower_a", "castle_f_tower_a", "bo_castle_f_tower_a")

castle_f_wall_stairs_a = SceneProp("castle_f_wall_stairs_a", "castle_f_wall_stairs_a", "bo_castle_f_wall_stairs_a")
castle_f_wall_stairs_a.add_flag(ScenePropFlag.TYPE_LADDER)

castle_f_wall_stairs_b = SceneProp("castle_f_wall_stairs_b", "castle_f_wall_stairs_b", "bo_castle_f_wall_stairs_b")
castle_f_wall_stairs_b.add_flag(ScenePropFlag.TYPE_LADDER)

castle_f_wall_way_a = SceneProp("castle_f_wall_way_a", "castle_f_wall_way_a", "bo_castle_f_wall_way_a")

castle_f_wall_way_b = SceneProp("castle_f_wall_way_b", "castle_f_wall_way_b", "bo_castle_f_wall_way_b")

castle_f_gatehouse_a = SceneProp("castle_f_gatehouse_a", "castle_f_gatehouse_a", "bo_castle_f_gatehouse_a")

castle_g_battlement_a = SceneProp("castle_g_battlement_a", "castle_g_battlement_a", "bo_castle_g_battlement_a")

castle_g_battlement_a1 = SceneProp("castle_g_battlement_a1", "castle_g_battlement_a1", "bo_castle_g_battlement_a1")

castle_g_battlement_c = SceneProp("castle_g_battlement_c", "castle_g_battlement_c", "bo_castle_g_battlement_c")

castle_g_corner_a = SceneProp("castle_g_corner_a", "castle_g_corner_a", "bo_castle_g_corner_a")

castle_g_corner_c = SceneProp("castle_g_corner_c", "castle_g_corner_c", "bo_castle_g_corner_c")

castle_g_tower_a = SceneProp("castle_g_tower_a", "castle_g_tower_a", "bo_castle_g_tower_a")
castle_g_tower_a.add_flag(ScenePropFlag.TYPE_LADDER)

castle_g_gate_house = SceneProp("castle_g_gate_house", "castle_g_gate_house", "bo_castle_g_gate_house")

castle_g_gate_house_door_a = SceneProp("castle_g_gate_house_door_a", "castle_g_gate_house_door_a", "bo_castle_g_gate_house_door_a")

castle_g_gate_house_door_b = SceneProp("castle_g_gate_house_door_b", "castle_g_gate_house_door_b", "bo_castle_g_gate_house_door_b")

castle_g_square_keep_a = SceneProp("castle_g_square_keep_a", "castle_g_square_keep_a", "bo_castle_g_square_keep_a")

castle_i_battlement_a = SceneProp("castle_i_battlement_a", "castle_i_battlement_a", "bo_castle_i_battlement_a")

castle_i_battlement_a1 = SceneProp("castle_i_battlement_a1", "castle_i_battlement_a1", "bo_castle_i_battlement_a1")

castle_i_battlement_c = SceneProp("castle_i_battlement_c", "castle_i_battlement_c", "bo_castle_i_battlement_c")

castle_i_corner_a = SceneProp("castle_i_corner_a", "castle_i_corner_a", "bo_castle_i_corner_a")

castle_i_corner_c = SceneProp("castle_i_corner_c", "castle_i_corner_c", "bo_castle_i_corner_c")

castle_i_tower_a = SceneProp("castle_i_tower_a", "castle_i_tower_a", "bo_castle_i_tower_a")
castle_i_tower_a.add_flag(ScenePropFlag.TYPE_LADDER)

castle_i_gate_house = SceneProp("castle_i_gate_house", "castle_i_gate_house", "bo_castle_i_gate_house")

castle_i_gate_house_door_a = SceneProp("castle_i_gate_house_door_a", "castle_i_gate_house_door_a", "bo_castle_i_gate_house_door_a")

castle_i_gate_house_door_b = SceneProp("castle_i_gate_house_door_b", "castle_i_gate_house_door_b", "bo_castle_i_gate_house_door_b")

castle_i_square_keep_a = SceneProp("castle_i_square_keep_a", "castle_i_square_keep_a", "bo_castle_i_square_keep_a")

mosque_a = SceneProp("mosque_a", "mosque_a", "bo_mosque_a")

stone_minaret_a = SceneProp("stone_minaret_a", "stone_minaret_a", "bo_stone_minaret_a")

stone_house_a = SceneProp("stone_house_a", "stone_house_a", "bo_stone_house_a")

stone_house_b = SceneProp("stone_house_b", "stone_house_b", "bo_stone_house_b")

stone_house_c = SceneProp("stone_house_c", "stone_house_c", "bo_stone_house_c")

stone_house_d = SceneProp("stone_house_d", "stone_house_d", "bo_stone_house_d")

stone_house_e = SceneProp("stone_house_e", "stone_house_e", "bo_stone_house_e")

stone_house_f = SceneProp("stone_house_f", "stone_house_f", "bo_stone_house_f")

banner_pole = SceneProp("banner_pole", "banner_pole", "bo_banner_pole")
banner_pole.add_flag(ScenePropFlag.MOVEABLE)

custom_banner_01 = SceneProp("custom_banner_01", "custom_banner_01", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    party_slot_001 = party_get_slot(_g_encountered_party,7)
    if party_slot_001 >= 0:
        bannerx = tableau.custom_banner_default
        cur_scene_prop_set_tableau_material(bannerx,party_slot_001)
    #end
trigger0.codeBlock = code
custom_banner_01.add_trigger(trigger0)

custom_banner_02 = SceneProp("custom_banner_02", "custom_banner_02", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    party_slot_001 = party_get_slot(_g_encountered_party,7)
    if party_slot_001 >= 0:
        bannerx = tableau.custom_banner_default
        cur_scene_prop_set_tableau_material(bannerx,party_slot_001)
    #end
trigger0.codeBlock = code
custom_banner_02.add_trigger(trigger0)

banner_a = SceneProp("banner_a", "banner_a01", "0")

banner_b = SceneProp("banner_b", "banner_a02", "0")

banner_c = SceneProp("banner_c", "banner_a03", "0")

banner_d = SceneProp("banner_d", "banner_a04", "0")

banner_e = SceneProp("banner_e", "banner_a05", "0")

banner_f = SceneProp("banner_f", "banner_a06", "0")

banner_g = SceneProp("banner_g", "banner_a07", "0")

banner_h = SceneProp("banner_h", "banner_a08", "0")

banner_i = SceneProp("banner_i", "banner_a09", "0")

banner_j = SceneProp("banner_j", "banner_a10", "0")

banner_k = SceneProp("banner_k", "banner_a11", "0")

banner_l = SceneProp("banner_l", "banner_a12", "0")

banner_m = SceneProp("banner_m", "banner_a13", "0")

banner_n = SceneProp("banner_n", "banner_a14", "0")

banner_o = SceneProp("banner_o", "banner_f21", "0")

banner_p = SceneProp("banner_p", "banner_a16", "0")

banner_q = SceneProp("banner_q", "banner_a17", "0")

banner_r = SceneProp("banner_r", "banner_a18", "0")

banner_s = SceneProp("banner_s", "banner_a19", "0")

banner_t = SceneProp("banner_t", "banner_a20", "0")

banner_u = SceneProp("banner_u", "banner_a21", "0")

banner_ba = SceneProp("banner_ba", "banner_b01", "0")

banner_bb = SceneProp("banner_bb", "banner_b02", "0")

banner_bc = SceneProp("banner_bc", "banner_b03", "0")

banner_bd = SceneProp("banner_bd", "banner_b04", "0")

banner_be = SceneProp("banner_be", "banner_b05", "0")

banner_bf = SceneProp("banner_bf", "banner_b06", "0")

banner_bg = SceneProp("banner_bg", "banner_b07", "0")

banner_bh = SceneProp("banner_bh", "banner_b08", "0")

banner_bi = SceneProp("banner_bi", "banner_b09", "0")

banner_bj = SceneProp("banner_bj", "banner_b10", "0")

banner_bk = SceneProp("banner_bk", "banner_b11", "0")

banner_bl = SceneProp("banner_bl", "banner_b12", "0")

banner_bm = SceneProp("banner_bm", "banner_b13", "0")

banner_bn = SceneProp("banner_bn", "banner_b14", "0")

banner_bo = SceneProp("banner_bo", "banner_b15", "0")

banner_bp = SceneProp("banner_bp", "banner_b16", "0")

banner_bq = SceneProp("banner_bq", "banner_b17", "0")

banner_br = SceneProp("banner_br", "banner_b18", "0")

banner_bs = SceneProp("banner_bs", "banner_b19", "0")

banner_bt = SceneProp("banner_bt", "banner_b20", "0")

banner_bu = SceneProp("banner_bu", "banner_b21", "0")

banner_ca = SceneProp("banner_ca", "banner_c01", "0")

banner_cb = SceneProp("banner_cb", "banner_c02", "0")

banner_cc = SceneProp("banner_cc", "banner_c03", "0")

banner_cd = SceneProp("banner_cd", "banner_c04", "0")

banner_ce = SceneProp("banner_ce", "banner_c05", "0")

banner_cf = SceneProp("banner_cf", "banner_c06", "0")

banner_cg = SceneProp("banner_cg", "banner_c07", "0")

banner_ch = SceneProp("banner_ch", "banner_c08", "0")

banner_ci = SceneProp("banner_ci", "banner_c09", "0")

banner_cj = SceneProp("banner_cj", "banner_c10", "0")

banner_ck = SceneProp("banner_ck", "banner_c11", "0")

banner_cl = SceneProp("banner_cl", "banner_c12", "0")

banner_cm = SceneProp("banner_cm", "banner_c13", "0")

banner_cn = SceneProp("banner_cn", "banner_c14", "0")

banner_co = SceneProp("banner_co", "banner_c15", "0")

banner_cp = SceneProp("banner_cp", "banner_c16", "0")

banner_cq = SceneProp("banner_cq", "banner_c17", "0")

banner_cr = SceneProp("banner_cr", "banner_c18", "0")

banner_cs = SceneProp("banner_cs", "banner_c19", "0")

banner_ct = SceneProp("banner_ct", "banner_c20", "0")

banner_cu = SceneProp("banner_cu", "banner_c21", "0")

banner_da = SceneProp("banner_da", "banner_d01", "0")

banner_db = SceneProp("banner_db", "banner_d02", "0")

banner_dc = SceneProp("banner_dc", "banner_d03", "0")

banner_dd = SceneProp("banner_dd", "banner_d04", "0")

banner_de = SceneProp("banner_de", "banner_d05", "0")

banner_df = SceneProp("banner_df", "banner_d06", "0")

banner_dg = SceneProp("banner_dg", "banner_d07", "0")

banner_dh = SceneProp("banner_dh", "banner_d08", "0")

banner_di = SceneProp("banner_di", "banner_d09", "0")

banner_dj = SceneProp("banner_dj", "banner_d10", "0")

banner_dk = SceneProp("banner_dk", "banner_d11", "0")

banner_dl = SceneProp("banner_dl", "banner_d12", "0")

banner_dm = SceneProp("banner_dm", "banner_d13", "0")

banner_dn = SceneProp("banner_dn", "banner_d14", "0")

banner_do = SceneProp("banner_do", "banner_d15", "0")

banner_dp = SceneProp("banner_dp", "banner_d16", "0")

banner_dq = SceneProp("banner_dq", "banner_d17", "0")

banner_dr = SceneProp("banner_dr", "banner_d18", "0")

banner_ds = SceneProp("banner_ds", "banner_d19", "0")

banner_dt = SceneProp("banner_dt", "banner_d20", "0")

banner_du = SceneProp("banner_du", "banner_d21", "0")

banner_ea = SceneProp("banner_ea", "banner_e01", "0")

banner_eb = SceneProp("banner_eb", "banner_e02", "0")

banner_ec = SceneProp("banner_ec", "banner_e03", "0")

banner_ed = SceneProp("banner_ed", "banner_e04", "0")

banner_ee = SceneProp("banner_ee", "banner_e05", "0")

banner_ef = SceneProp("banner_ef", "banner_e06", "0")

banner_eg = SceneProp("banner_eg", "banner_e07", "0")

banner_eh = SceneProp("banner_eh", "banner_e08", "0")

banner_ei = SceneProp("banner_ei", "banner_e09", "0")

banner_ej = SceneProp("banner_ej", "banner_e10", "0")

banner_ek = SceneProp("banner_ek", "banner_e11", "0")

banner_el = SceneProp("banner_el", "banner_e12", "0")

banner_em = SceneProp("banner_em", "banner_e13", "0")

banner_en = SceneProp("banner_en", "banner_e14", "0")

banner_eo = SceneProp("banner_eo", "banner_e15", "0")

banner_ep = SceneProp("banner_ep", "banner_e16", "0")

banner_eq = SceneProp("banner_eq", "banner_e17", "0")

banner_er = SceneProp("banner_er", "banner_e18", "0")

banner_es = SceneProp("banner_es", "banner_e19", "0")

banner_et = SceneProp("banner_et", "banner_e20", "0")

banner_eu = SceneProp("banner_eu", "banner_e21", "0")

banner_f01 = SceneProp("banner_f01", "banner_f01", "0")

banner_f02 = SceneProp("banner_f02", "banner_f02", "0")

banner_f03 = SceneProp("banner_f03", "banner_f03", "0")

banner_f04 = SceneProp("banner_f04", "banner_f04", "0")

banner_f05 = SceneProp("banner_f05", "banner_f05", "0")

banner_f06 = SceneProp("banner_f06", "banner_f06", "0")

banner_f07 = SceneProp("banner_f07", "banner_f07", "0")

banner_f08 = SceneProp("banner_f08", "banner_f08", "0")

banner_f09 = SceneProp("banner_f09", "banner_f09", "0")

banner_f10 = SceneProp("banner_f10", "banner_f10", "0")

banner_f11 = SceneProp("banner_f11", "banner_f11", "0")

banner_f12 = SceneProp("banner_f12", "banner_f12", "0")

banner_f13 = SceneProp("banner_f13", "banner_f13", "0")

banner_f14 = SceneProp("banner_f14", "banner_f14", "0")

banner_f15 = SceneProp("banner_f15", "banner_f15", "0")

banner_f16 = SceneProp("banner_f16", "banner_f16", "0")

banner_f17 = SceneProp("banner_f17", "banner_f17", "0")

banner_f18 = SceneProp("banner_f18", "banner_f18", "0")

banner_f19 = SceneProp("banner_f19", "banner_f19", "0")

banner_f20 = SceneProp("banner_f20", "banner_f20", "0")

banner_g01 = SceneProp("banner_g01", "banner_f01", "0")

banner_g02 = SceneProp("banner_g02", "banner_f02", "0")

banner_g03 = SceneProp("banner_g03", "banner_f03", "0")

banner_g04 = SceneProp("banner_g04", "banner_f04", "0")

banner_g05 = SceneProp("banner_g05", "banner_f05", "0")

banner_g06 = SceneProp("banner_g06", "banner_f06", "0")

banner_g07 = SceneProp("banner_g07", "banner_f07", "0")

banner_g08 = SceneProp("banner_g08", "banner_f08", "0")

banner_g09 = SceneProp("banner_g09", "banner_f09", "0")

banner_g10 = SceneProp("banner_g10", "banner_f10", "0")

banner_kingdom_a = SceneProp("banner_kingdom_a", "banner_kingdom_a", "0")

banner_kingdom_b = SceneProp("banner_kingdom_b", "banner_kingdom_b", "0")

banner_kingdom_c = SceneProp("banner_kingdom_c", "banner_kingdom_c", "0")

banner_kingdom_d = SceneProp("banner_kingdom_d", "banner_kingdom_d", "0")

banner_kingdom_e = SceneProp("banner_kingdom_e", "banner_kingdom_e", "0")

banner_kingdom_f = SceneProp("banner_kingdom_f", "banner_kingdom_f", "0")

banner_f21 = SceneProp("banner_f21", "banner_a15", "0")

tavern_chair_a = SceneProp("tavern_chair_a", "tavern_chair_a", "bo_tavern_chair_a")

tavern_chair_b = SceneProp("tavern_chair_b", "tavern_chair_b", "bo_tavern_chair_b")

tavern_table_a = SceneProp("tavern_table_a", "tavern_table_a", "bo_tavern_table_a")

tavern_table_b = SceneProp("tavern_table_b", "tavern_table_b", "bo_tavern_table_b")

fireplace_a = SceneProp("fireplace_a", "fireplace_a", "bo_fireplace_a")

barrel = SceneProp("barrel", "barrel", "bobarrel")

bench_tavern = SceneProp("bench_tavern", "bench_tavern", "bobench_tavern")

bench_tavern_b = SceneProp("bench_tavern_b", "bench_tavern_b", "bo_bench_tavern_b")

bowl_wood = SceneProp("bowl_wood", "bowl_wood", "0")

chandelier_table = SceneProp("chandelier_table", "chandelier_table", "0")

chandelier_tavern = SceneProp("chandelier_tavern", "chandelier_tavern", "0")

chest_gothic = SceneProp("chest_gothic", "chest_gothic", "bochest_gothic")

chest_b = SceneProp("chest_b", "chest_b", "bo_chest_b")

chest_c = SceneProp("chest_c", "chest_c", "bo_chest_c")

counter_tavern = SceneProp("counter_tavern", "counter_tavern", "bocounter_tavern")

cup = SceneProp("cup", "cup", "0")

dish_metal = SceneProp("dish_metal", "dish_metal", "0")

gothic_chair = SceneProp("gothic_chair", "gothic_chair", "bogothic_chair")

gothic_stool = SceneProp("gothic_stool", "gothic_stool", "bogothic_stool")

grate = SceneProp("grate", "grate", "bograte")

jug = SceneProp("jug", "jug", "0")

potlamp = SceneProp("potlamp", "potlamp", "0")

weapon_rack = SceneProp("weapon_rack", "weapon_rack", "boweapon_rack")

weapon_rack_big = SceneProp("weapon_rack_big", "weapon_rack_big", "boweapon_rack_big")

tavern_barrel = SceneProp("tavern_barrel", "barrel", "bobarrel")

tavern_barrel_b = SceneProp("tavern_barrel_b", "tavern_barrel_b", "bo_tavern_barrel_b")

merchant_sign = SceneProp("merchant_sign", "merchant_sign", "bo_tavern_sign")

tavern_sign = SceneProp("tavern_sign", "tavern_sign", "bo_tavern_sign")

sack = SceneProp("sack", "sack", "0")

skull_a = SceneProp("skull_a", "skull_a", "0")

skull_b = SceneProp("skull_b", "skull_b", "0")

skull_c = SceneProp("skull_c", "skull_c", "0")

skull_d = SceneProp("skull_d", "skull_d", "0")

skeleton_cow = SceneProp("skeleton_cow", "skeleton_cow", "0")

cupboard_a = SceneProp("cupboard_a", "cupboard_a", "bo_cupboard_a")

box_a = SceneProp("box_a", "box_a", "bo_box_a")

bucket_a = SceneProp("bucket_a", "bucket_a", "bo_bucket_a")

straw_a = SceneProp("straw_a", "straw_a", "0")

straw_b = SceneProp("straw_b", "straw_b", "0")

straw_c = SceneProp("straw_c", "straw_c", "0")

cloth_a = SceneProp("cloth_a", "cloth_a", "0")

cloth_b = SceneProp("cloth_b", "cloth_b", "0")

mat_a = SceneProp("mat_a", "mat_a", "0")

mat_b = SceneProp("mat_b", "mat_b", "0")

mat_c = SceneProp("mat_c", "mat_c", "0")

mat_d = SceneProp("mat_d", "mat_d", "0")

wood_a = SceneProp("wood_a", "wood_a", "bo_wood_a")

wood_b = SceneProp("wood_b", "wood_b", "bo_wood_b")

wood_heap = SceneProp("wood_heap", "wood_heap_a", "bo_wood_heap_a")

wood_heap_b = SceneProp("wood_heap_b", "wood_heap_b", "bo_wood_heap_b")

water_well_a = SceneProp("water_well_a", "water_well_a", "bo_water_well_a")

net_a = SceneProp("net_a", "net_a", "bo_net_a")

net_b = SceneProp("net_b", "net_b", "0")

meat_hook = SceneProp("meat_hook", "meat_hook", "0")

cooking_pole = SceneProp("cooking_pole", "cooking_pole", "0")

bowl_a = SceneProp("bowl_a", "bowl_a", "0")

bucket_b = SceneProp("bucket_b", "bucket_b", "0")

washtub_a = SceneProp("washtub_a", "washtub_a", "bo_washtub_a")

washtub_b = SceneProp("washtub_b", "washtub_b", "bo_washtub_b")

table_trunk_a = SceneProp("table_trunk_a", "table_trunk_a", "bo_table_trunk_a")

chair_trunk_a = SceneProp("chair_trunk_a", "chair_trunk_a", "bo_chair_trunk_a")

chair_trunk_b = SceneProp("chair_trunk_b", "chair_trunk_b", "bo_chair_trunk_b")

chair_trunk_c = SceneProp("chair_trunk_c", "chair_trunk_c", "bo_chair_trunk_c")

table_trestle_long = SceneProp("table_trestle_long", "table_trestle_long", "bo_table_trestle_long")

table_trestle_small = SceneProp("table_trestle_small", "table_trestle_small", "bo_table_trestle_small")

chair_trestle = SceneProp("chair_trestle", "chair_trestle", "bo_chair_trestle")

wheel = SceneProp("wheel", "wheel", "bo_wheel")

ladder = SceneProp("ladder", "ladder", "boladder")
ladder.add_flag(ScenePropFlag.TYPE_LADDER)

cart = SceneProp("cart", "cart", "bo_cart")

village_stand = SceneProp("village_stand", "village_stand", "bovillage_stand")

wooden_stand = SceneProp("wooden_stand", "wooden_stand", "bowooden_stand")

table_small = SceneProp("table_small", "table_small", "bo_table_small")

table_small_b = SceneProp("table_small_b", "table_small_b", "bo_table_small_b")

small_timber_frame_house_a = SceneProp("small_timber_frame_house_a", "small_timber_frame_house_a", "bo_small_timber_frame_house_a")

timber_frame_house_b = SceneProp("timber_frame_house_b", "tf_house_b", "bo_tf_house_b")

timber_frame_house_c = SceneProp("timber_frame_house_c", "tf_house_c", "bo_tf_house_c")

timber_frame_extension_a = SceneProp("timber_frame_extension_a", "timber_frame_extension_a", "bo_timber_frame_extension_a")

timber_frame_extension_b = SceneProp("timber_frame_extension_b", "timber_frame_extension_b", "bo_timber_frame_extension_b")

stone_stairs_a = SceneProp("stone_stairs_a", "stone_stairs_a", "bo_stone_stairs_a")
stone_stairs_a.add_flag(ScenePropFlag.TYPE_LADDER)

stone_stairs_b = SceneProp("stone_stairs_b", "stone_stairs_b", "bo_stone_stairs_b")
stone_stairs_b.add_flag(ScenePropFlag.TYPE_LADDER)

railing_a = SceneProp("railing_a", "railing_a", "bo_railing_a")

side_building_a = SceneProp("side_building_a", "side_building_a", "bo_side_building_a")

battlement_a = SceneProp("battlement_a", "battlement_a", "bo_battlement_a")

battlement_a_destroyed = SceneProp("battlement_a_destroyed", "battlement_a_destroyed", "bo_battlement_a_destroyed")

round_tower_a = SceneProp("round_tower_a", "round_tower_a", "bo_round_tower_a")

small_round_tower_a = SceneProp("small_round_tower_a", "small_round_tower_a", "bo_small_round_tower_a")

small_round_tower_roof_a = SceneProp("small_round_tower_roof_a", "small_round_tower_roof_a", "bo_small_round_tower_roof_a")

square_keep_a = SceneProp("square_keep_a", "square_keep_a", "bo_square_keep_a")

square_tower_roof_a = SceneProp("square_tower_roof_a", "square_tower_roof_a", "0")

gate_house_a = SceneProp("gate_house_a", "gate_house_a", "bo_gate_house_a")

gate_house_b = SceneProp("gate_house_b", "gate_house_b", "bo_gate_house_b")

small_wall_a = SceneProp("small_wall_a", "small_wall_a", "bo_small_wall_a")

small_wall_b = SceneProp("small_wall_b", "small_wall_b", "bo_small_wall_b")

small_wall_c = SceneProp("small_wall_c", "small_wall_c", "bo_small_wall_c")

small_wall_c_destroy = SceneProp("small_wall_c_destroy", "small_wall_c_destroy", "bo_small_wall_c_destroy")

small_wall_d = SceneProp("small_wall_d", "small_wall_d", "bo_small_wall_d")

small_wall_e = SceneProp("small_wall_e", "small_wall_e", "bo_small_wall_d")

small_wall_f = SceneProp("small_wall_f", "small_wall_f", "bo_small_wall_f")

small_wall_f2 = SceneProp("small_wall_f2", "small_wall_f2", "bo_small_wall_f2")

town_house_a = SceneProp("town_house_a", "town_house_a", "bo_town_house_a")

town_house_b = SceneProp("town_house_b", "town_house_b", "bo_town_house_b")

town_house_c = SceneProp("town_house_c", "town_house_c", "bo_town_house_c")

town_house_d = SceneProp("town_house_d", "town_house_d", "bo_town_house_d")

town_house_e = SceneProp("town_house_e", "town_house_e", "bo_town_house_e")

town_house_f = SceneProp("town_house_f", "town_house_f", "bo_town_house_f")

town_house_g = SceneProp("town_house_g", "town_house_g", "bo_town_house_g")

town_house_h = SceneProp("town_house_h", "town_house_h", "bo_town_house_h")

town_house_i = SceneProp("town_house_i", "town_house_i", "bo_town_house_i")

town_house_j = SceneProp("town_house_j", "town_house_j", "bo_town_house_j")

town_house_l = SceneProp("town_house_l", "town_house_l", "bo_town_house_l")

town_house_m = SceneProp("town_house_m", "town_house_m", "bo_town_house_m")

town_house_n = SceneProp("town_house_n", "town_house_n", "bo_town_house_n")

town_house_o = SceneProp("town_house_o", "town_house_o", "bo_town_house_o")

town_house_p = SceneProp("town_house_p", "town_house_p", "bo_town_house_p")

town_house_q = SceneProp("town_house_q", "town_house_q", "bo_town_house_q")

passage_house_a = SceneProp("passage_house_a", "passage_house_a", "bo_passage_house_a")

passage_house_b = SceneProp("passage_house_b", "passage_house_b", "bo_passage_house_b")

passage_house_c = SceneProp("passage_house_c", "passage_house_c", "bo_passage_house_c")

passage_house_d = SceneProp("passage_house_d", "passage_house_d", "bo_passage_house_d")

passage_house_c_door = SceneProp("passage_house_c_door", "passage_house_c_door", "bo_passage_house_c_door")

house_extension_a = SceneProp("house_extension_a", "house_extension_a", "bo_house_extension_a")

house_extension_b = SceneProp("house_extension_b", "house_extension_b", "bo_house_extension_b")

house_extension_c = SceneProp("house_extension_c", "house_extension_c", "bo_house_extension_a")

house_extension_d = SceneProp("house_extension_d", "house_extension_d", "bo_house_extension_d")

house_extension_e = SceneProp("house_extension_e", "house_extension_e", "bo_house_extension_e")

house_extension_f = SceneProp("house_extension_f", "house_extension_f", "bo_house_extension_f")

house_extension_f2 = SceneProp("house_extension_f2", "house_extension_f2", "bo_house_extension_f")

house_extension_g = SceneProp("house_extension_g", "house_extension_g", "bo_house_extension_g")

house_extension_g2 = SceneProp("house_extension_g2", "house_extension_g2", "bo_house_extension_g")

house_extension_h = SceneProp("house_extension_h", "house_extension_h", "bo_house_extension_h")

house_extension_i = SceneProp("house_extension_i", "house_extension_i", "bo_house_extension_i")

house_roof_door = SceneProp("house_roof_door", "house_roof_door", "bo_house_roof_door")

door_extension_a = SceneProp("door_extension_a", "door_extension_a", "bo_door_extension_a")

stairs_arch_a = SceneProp("stairs_arch_a", "stairs_arch_a", "bo_stairs_arch_a")
stairs_arch_a.add_flag(ScenePropFlag.TYPE_LADDER)

town_house_r = SceneProp("town_house_r", "town_house_r", "bo_town_house_r")

town_house_s = SceneProp("town_house_s", "town_house_s", "bo_town_house_s")

town_house_t = SceneProp("town_house_t", "town_house_t", "bo_town_house_t")

town_house_u = SceneProp("town_house_u", "town_house_u", "bo_town_house_u")

town_house_v = SceneProp("town_house_v", "town_house_v", "bo_town_house_v")

town_house_w = SceneProp("town_house_w", "town_house_w", "bo_town_house_w")

town_house_y = SceneProp("town_house_y", "town_house_y", "bo_town_house_y")

town_house_z = SceneProp("town_house_z", "town_house_z", "bo_town_house_z")

town_house_za = SceneProp("town_house_za", "town_house_za", "bo_town_house_za")

windmill = SceneProp("windmill", "windmill", "bo_windmill")

windmill_fan_turning = SceneProp("windmill_fan_turning", "windmill_fan_turning", "bo_windmill_fan_turning")
windmill_fan_turning.add_flag(ScenePropFlag.MOVEABLE)

windmill_fan = SceneProp("windmill_fan", "windmill_fan", "bo_windmill_fan")

fake_house_a = SceneProp("fake_house_a", "fake_house_a", "bo_fake_house_a")

fake_house_b = SceneProp("fake_house_b", "fake_house_b", "bo_fake_house_b")

fake_house_c = SceneProp("fake_house_c", "fake_house_c", "bo_fake_house_c")

fake_house_d = SceneProp("fake_house_d", "fake_house_d", "bo_fake_house_d")

fake_house_e = SceneProp("fake_house_e", "fake_house_e", "bo_fake_house_e")

fake_house_f = SceneProp("fake_house_f", "fake_house_f", "bo_fake_house_f")

fake_house_snowy_a = SceneProp("fake_house_snowy_a", "fake_house_snowy_a", "bo_fake_house_a")

fake_house_snowy_b = SceneProp("fake_house_snowy_b", "fake_house_snowy_b", "bo_fake_house_b")

fake_house_snowy_c = SceneProp("fake_house_snowy_c", "fake_house_snowy_c", "bo_fake_house_c")

fake_house_snowy_d = SceneProp("fake_house_snowy_d", "fake_house_snowy_d", "bo_fake_house_d")

fake_house_far_a = SceneProp("fake_house_far_a", "fake_house_far_a", "0")

fake_house_far_b = SceneProp("fake_house_far_b", "fake_house_far_b", "0")

fake_house_far_c = SceneProp("fake_house_far_c", "fake_house_far_c", "0")

fake_house_far_d = SceneProp("fake_house_far_d", "fake_house_far_d", "0")

fake_house_far_e = SceneProp("fake_house_far_e", "fake_house_far_e", "0")

fake_house_far_f = SceneProp("fake_house_far_f", "fake_house_far_f", "0")

fake_house_far_snowycrude_a = SceneProp("fake_house_far_snowycrude_a", "fake_house_far_snowy_a", "0")

fake_house_far_snowy_b = SceneProp("fake_house_far_snowy_b", "fake_house_far_snowy_b", "0")

fake_house_far_snowy_c = SceneProp("fake_house_far_snowy_c", "fake_house_far_snowy_c", "0")

fake_house_far_snowy_d = SceneProp("fake_house_far_snowy_d", "fake_house_far_snowy_d", "0")

earth_wall_a = SceneProp("earth_wall_a", "earth_wall_a", "bo_earth_wall_a")

earth_wall_a2 = SceneProp("earth_wall_a2", "earth_wall_a2", "bo_earth_wall_a2")

earth_wall_b = SceneProp("earth_wall_b", "earth_wall_b", "bo_earth_wall_b")

earth_wall_b2 = SceneProp("earth_wall_b2", "earth_wall_b2", "bo_earth_wall_b2")

earth_stairs_a = SceneProp("earth_stairs_a", "earth_stairs_a", "bo_earth_stairs_a")
earth_stairs_a.add_flag(ScenePropFlag.TYPE_LADDER)

earth_stairs_b = SceneProp("earth_stairs_b", "earth_stairs_b", "bo_earth_stairs_b")
earth_stairs_b.add_flag(ScenePropFlag.TYPE_LADDER)

earth_tower_small_a = SceneProp("earth_tower_small_a", "earth_tower_small_a", "bo_earth_tower_small_a")

earth_gate_house_a = SceneProp("earth_gate_house_a", "earth_gate_house_a", "bo_earth_gate_house_a")

earth_gate_a = SceneProp("earth_gate_a", "earth_gate_a", "bo_earth_gate_a")

earth_square_keep_a = SceneProp("earth_square_keep_a", "earth_square_keep_a", "bo_earth_square_keep_a")

earth_house_a = SceneProp("earth_house_a", "earth_house_a", "bo_earth_house_a")

earth_house_b = SceneProp("earth_house_b", "earth_house_b", "bo_earth_house_b")

earth_house_c = SceneProp("earth_house_c", "earth_house_c", "bo_earth_house_c")

earth_house_d = SceneProp("earth_house_d", "earth_house_d", "bo_earth_house_d")

village_steppe_a = SceneProp("village_steppe_a", "village_steppe_a", "bo_village_steppe_a")

village_steppe_b = SceneProp("village_steppe_b", "village_steppe_b", "bo_village_steppe_b")

village_steppe_c = SceneProp("village_steppe_c", "village_steppe_c", "bo_village_steppe_c")

village_steppe_d = SceneProp("village_steppe_d", "village_steppe_d", "bo_village_steppe_d")

village_steppe_e = SceneProp("village_steppe_e", "village_steppe_e", "bo_village_steppe_e")

village_steppe_f = SceneProp("village_steppe_f", "village_steppe_f", "bo_village_steppe_f")

town_house_aa = SceneProp("town_house_aa", "town_house_aa", "bo_town_house_aa")

snowy_house_a = SceneProp("snowy_house_a", "snowy_house_a", "bo_snowy_house_a")

snowy_house_b = SceneProp("snowy_house_b", "snowy_house_b", "bo_snowy_house_b")

snowy_house_c = SceneProp("snowy_house_c", "snowy_house_c", "bo_snowy_house_c")

snowy_house_d = SceneProp("snowy_house_d", "snowy_house_d", "bo_snowy_house_d")

snowy_house_e = SceneProp("snowy_house_e", "snowy_house_e", "bo_snowy_house_e")

snowy_house_f = SceneProp("snowy_house_f", "snowy_house_f", "bo_snowy_house_f")

snowy_house_g = SceneProp("snowy_house_g", "snowy_house_g", "bo_snowy_house_g")

snowy_house_h = SceneProp("snowy_house_h", "snowy_house_h", "bo_snowy_house_h")

snowy_house_i = SceneProp("snowy_house_i", "snowy_house_i", "bo_snowy_house_i")

snowy_wall_a = SceneProp("snowy_wall_a", "snowy_wall_a", "bo_snowy_wall_a")

snowy_stand = SceneProp("snowy_stand", "snowy_stand", "bo_snowy_stand")

snowy_heap_a = SceneProp("snowy_heap_a", "snowy_heap_a", "bo_snowy_heap_a")

snowy_trunks_a = SceneProp("snowy_trunks_a", "snowy_trunks_a", "bo_snowy_trunks_a")

snowy_castle_tower_a = SceneProp("snowy_castle_tower_a", "snowy_castle_tower_a", "bo_snowy_castle_tower_a")

snowy_castle_battlement_a = SceneProp("snowy_castle_battlement_a", "snowy_castle_battlement_a", "bo_snowy_castle_battlement_a")

snowy_castle_battlement_a_destroyed = SceneProp("snowy_castle_battlement_a_destroyed", "snowy_castle_battlement_a_destroyed", "bo_snowy_castle_battlement_a_destroyed")

snowy_castle_battlement_b = SceneProp("snowy_castle_battlement_b", "snowy_castle_battlement_b", "bo_snowy_castle_battlement_b")

snowy_castle_battlement_corner_a = SceneProp("snowy_castle_battlement_corner_a", "snowy_castle_battlement_corner_a", "bo_snowy_castle_battlement_corner_a")

snowy_castle_battlement_corner_b = SceneProp("snowy_castle_battlement_corner_b", "snowy_castle_battlement_corner_b", "bo_snowy_castle_battlement_corner_b")

snowy_castle_battlement_corner_c = SceneProp("snowy_castle_battlement_corner_c", "snowy_castle_battlement_corner_c", "bo_snowy_castle_battlement_corner_c")

snowy_castle_battlement_stairs_a = SceneProp("snowy_castle_battlement_stairs_a", "snowy_castle_battlement_stairs_a", "bo_snowy_castle_battlement_stairs_a")

snowy_castle_battlement_stairs_b = SceneProp("snowy_castle_battlement_stairs_b", "snowy_castle_battlement_stairs_b", "bo_snowy_castle_battlement_stairs_b")

snowy_castle_gate_house_a = SceneProp("snowy_castle_gate_house_a", "snowy_castle_gate_house_a", "bo_snowy_castle_gate_house_a")

snowy_castle_round_tower_a = SceneProp("snowy_castle_round_tower_a", "snowy_castle_round_tower_a", "bo_snowy_castle_round_tower_a")

snowy_castle_square_keep_a = SceneProp("snowy_castle_square_keep_a", "snowy_castle_square_keep_a", "bo_snowy_castle_square_keep_a")

snowy_castle_stairs_a = SceneProp("snowy_castle_stairs_a", "snowy_castle_stairs_a", "bo_snowy_castle_stairs_a")
snowy_castle_stairs_a.add_flag(ScenePropFlag.TYPE_LADDER)

square_keep_b = SceneProp("square_keep_b", "square_keep_b", "bo_square_keep_b")

square_keep_c = SceneProp("square_keep_c", "square_keep_c", "bo_square_keep_c")

square_keep_d = SceneProp("square_keep_d", "square_keep_d", "bo_square_keep_d")

square_keep_e = SceneProp("square_keep_e", "square_keep_e", "bo_square_keep_e")

square_keep_f = SceneProp("square_keep_f", "square_keep_f", "bo_square_keep_f")

square_extension_a = SceneProp("square_extension_a", "square_extension_a", "bo_square_extension_a")

square_stairs_a = SceneProp("square_stairs_a", "square_stairs_a", "bo_square_stairs_a")

castle_courtyard_house_a = SceneProp("castle_courtyard_house_a", "castle_courtyard_house_a", "bo_castle_courtyard_house_a")

castle_courtyard_house_b = SceneProp("castle_courtyard_house_b", "castle_courtyard_house_b", "bo_castle_courtyard_house_b")

castle_courtyard_house_c = SceneProp("castle_courtyard_house_c", "castle_courtyard_house_c", "bo_castle_courtyard_house_c")

castle_courtyard_a = SceneProp("castle_courtyard_a", "castle_courtyard_a", "bo_castle_courtyard_a")

gatehouse_b = SceneProp("gatehouse_b", "gatehouse_b", "bo_gatehouse_b")

castle_gaillard = SceneProp("castle_gaillard", "castle_gaillard", "bo_castle_gaillard")

castle_e_battlement_a = SceneProp("castle_e_battlement_a", "castle_e_battlement_a", "bo_castle_e_battlement_a")

castle_e_battlement_c = SceneProp("castle_e_battlement_c", "castle_e_battlement_c", "bo_castle_e_battlement_c")

castle_e_battlement_a_destroyed = SceneProp("castle_e_battlement_a_destroyed", "castle_e_battlement_a_destroyed", "bo_castle_e_battlement_a_destroyed")

castle_e_sally_door_a = SceneProp("castle_e_sally_door_a", "castle_e_sally_door_a", "bo_castle_e_sally_door_a")
castle_e_sally_door_a.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
castle_e_sally_door_a.add_flag(ScenePropFlag.DESTRUCTIBLE)
castle_e_sally_door_a.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, scene_prop_instance_id_002):
    pos1 = agent_get_position(var001)
    pos2 = prop_instance_get_starting_position(scene_prop_instance_id_002)
    scene_prop_slot_003 = scene_prop_get_slot(scene_prop_instance_id_002,1)
    if position_is_behind_position(1,2) or scene_prop_slot_003 == 1:
        if True:
            use_item(scene_prop_instance_id_002,var001)
            max_players = get_max_players()
            for player_id_005 in range(1, max_players):
                if player_is_active(player_id_005):
                    multiplayer_send_2_int_to_player(player_id_005,76,scene_prop_instance_id_002,var001)
                #end
            #end
        #end
    #end
trigger0.codeBlock = code
castle_e_sally_door_a.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,3000)
trigger1.codeBlock = code
castle_e_sally_door_a.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var002, var003):
    play_sound(snd.dummy_destroyed)
    var001 = 86
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        set_fixed_point_multiplier(100)
        pos1 = prop_instance_get_position(var002)
        if var003 >= 0:
            pos2 = agent_get_position(var003)
            if position_is_behind_position(2,1):
                var001 *= -1
            #end
        #end
        init_position(3)
        if var001 >= 0:
            position_move_y(3,-100)
        else:
            position_move_y(3,100)
        #end
        position_move_x(3,-50)
        position_transform_position_to_parent(4,1,3)
        position_move_z(4,100)
        distance_to_ground_level_004 = position_get_distance_to_ground_level(4)
        distance_to_ground_level_004 -= 100
        var005 = distance_to_ground_level_004
        var005 /= 3
        if var001 >= 0:
            var001 += var005
        else:
            var001 -= var005
        #end
        position_rotate_x(1,var001)
        prop_instance_animate_to_position(var002,1,70)
    #end
trigger2.codeBlock = code
castle_e_sally_door_a.add_trigger(trigger2)
# trigger3
trigger3 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
    #end
trigger3.codeBlock = code
castle_e_sally_door_a.add_trigger(trigger3)

castle_e_corner = SceneProp("castle_e_corner", "castle_e_corner", "bo_castle_e_corner")

castle_e_corner_b = SceneProp("castle_e_corner_b", "castle_e_corner_b", "bo_castle_e_corner_b")

castle_e_corner_c = SceneProp("castle_e_corner_c", "castle_e_corner_c", "bo_castle_e_corner_c")

castle_e_stairs_a = SceneProp("castle_e_stairs_a", "castle_e_stairs_a", "bo_castle_e_stairs_a")

castle_e_tower = SceneProp("castle_e_tower", "castle_e_tower", "bo_castle_e_tower")

castle_e_gate_house_a = SceneProp("castle_e_gate_house_a", "castle_e_gate_house_a", "bo_castle_e_gate_house_a")

castle_e_keep_a = SceneProp("castle_e_keep_a", "castle_e_keep_a", "bo_castle_e_keep_a")

stand_thatched = SceneProp("stand_thatched", "stand_thatched", "bo_stand_thatched")

stand_cloth = SceneProp("stand_cloth", "stand_cloth", "bo_stand_cloth")

castle_e_house_a = SceneProp("castle_e_house_a", "castle_e_house_a", "bo_castle_e_house_a")

castle_e_house_b = SceneProp("castle_e_house_b", "castle_e_house_b", "bo_castle_e_house_b")

arena_block_a = SceneProp("arena_block_a", "arena_block_a", "bo_arena_block_ab")

arena_block_b = SceneProp("arena_block_b", "arena_block_b", "bo_arena_block_ab")

arena_block_c = SceneProp("arena_block_c", "arena_block_c", "bo_arena_block_c")

arena_block_d = SceneProp("arena_block_d", "arena_block_d", "bo_arena_block_def")

arena_block_e = SceneProp("arena_block_e", "arena_block_e", "bo_arena_block_def")

arena_block_f = SceneProp("arena_block_f", "arena_block_f", "bo_arena_block_def")

arena_block_g = SceneProp("arena_block_g", "arena_block_g", "bo_arena_block_ghi")

arena_block_h = SceneProp("arena_block_h", "arena_block_h", "bo_arena_block_ghi")

arena_block_i = SceneProp("arena_block_i", "arena_block_i", "bo_arena_block_ghi")

arena_block_j = SceneProp("arena_block_j", "arena_block_j", "bo_arena_block_j")

arena_block_j_awning = SceneProp("arena_block_j_awning", "arena_block_j_awning", "bo_arena_block_j_awning")

arena_palisade_a = SceneProp("arena_palisade_a", "arena_palisade_a", "bo_arena_palisade_a")

arena_wall_a = SceneProp("arena_wall_a", "arena_wall_a", "bo_arena_wall_ab")

arena_wall_b = SceneProp("arena_wall_b", "arena_wall_b", "bo_arena_wall_ab")

arena_barrier_a = SceneProp("arena_barrier_a", "arena_barrier_a", "bo_arena_barrier_a")

arena_barrier_b = SceneProp("arena_barrier_b", "arena_barrier_b", "bo_arena_barrier_bc")

arena_barrier_c = SceneProp("arena_barrier_c", "arena_barrier_c", "bo_arena_barrier_bc")

arena_tower_a = SceneProp("arena_tower_a", "arena_tower_a", "bo_arena_tower_abc")

arena_tower_b = SceneProp("arena_tower_b", "arena_tower_b", "bo_arena_tower_abc")

arena_tower_c = SceneProp("arena_tower_c", "arena_tower_c", "bo_arena_tower_abc")

arena_spectator_a = SceneProp("arena_spectator_a", "arena_spectator_a", "0")

arena_spectator_b = SceneProp("arena_spectator_b", "arena_spectator_b", "0")

arena_spectator_c = SceneProp("arena_spectator_c", "arena_spectator_c", "0")

arena_spectator_sitting_a = SceneProp("arena_spectator_sitting_a", "arena_spectator_sitting_a", "0")

arena_spectator_sitting_b = SceneProp("arena_spectator_sitting_b", "arena_spectator_sitting_b", "0")

arena_spectator_sitting_c = SceneProp("arena_spectator_sitting_c", "arena_spectator_sitting_c", "0")

courtyard_gate_a = SceneProp("courtyard_gate_a", "courtyard_entry_a", "bo_courtyard_entry_a")

courtyard_gate_b = SceneProp("courtyard_gate_b", "courtyard_entry_b", "bo_courtyard_entry_b")

courtyard_gate_c = SceneProp("courtyard_gate_c", "courtyard_entry_c", "bo_courtyard_entry_c")

courtyard_gate_snowy = SceneProp("courtyard_gate_snowy", "courtyard_entry_snowy", "bo_courtyard_entry_a")

castle_tower_a = SceneProp("castle_tower_a", "castle_tower_a", "bo_castle_tower_a")

castle_battlement_a = SceneProp("castle_battlement_a", "castle_battlement_a", "bo_castle_battlement_a")

castle_battlement_b = SceneProp("castle_battlement_b", "castle_battlement_b", "bo_castle_battlement_b")

castle_battlement_c = SceneProp("castle_battlement_c", "castle_battlement_c", "bo_castle_battlement_c")

castle_battlement_a_destroyed = SceneProp("castle_battlement_a_destroyed", "castle_battlement_a_destroyed", "bo_castle_battlement_a_destroyed")

castle_battlement_b_destroyed = SceneProp("castle_battlement_b_destroyed", "castle_battlement_b_destroyed", "bo_castle_battlement_b_destroyed")

castle_battlement_corner_a = SceneProp("castle_battlement_corner_a", "castle_battlement_corner_a", "bo_castle_battlement_corner_a")

castle_battlement_corner_b = SceneProp("castle_battlement_corner_b", "castle_battlement_corner_b", "bo_castle_battlement_corner_b")

castle_battlement_corner_c = SceneProp("castle_battlement_corner_c", "castle_battlement_corner_c", "bo_castle_battlement_corner_c")

castle_battlement_stairs_a = SceneProp("castle_battlement_stairs_a", "castle_battlement_stairs_a", "bo_castle_battlement_stairs_a")

castle_battlement_stairs_b = SceneProp("castle_battlement_stairs_b", "castle_battlement_stairs_b", "bo_castle_battlement_stairs_b")

castle_gate_house_a = SceneProp("castle_gate_house_a", "castle_gate_house_a", "bo_castle_gate_house_a")

castle_round_tower_a = SceneProp("castle_round_tower_a", "castle_round_tower_a", "bo_castle_round_tower_a")

castle_square_keep_a = SceneProp("castle_square_keep_a", "castle_square_keep_a", "bo_castle_square_keep_a")

castle_stairs_a = SceneProp("castle_stairs_a", "castle_stairs_a", "bo_castle_stairs_a")
castle_stairs_a.add_flag(ScenePropFlag.TYPE_LADDER)

castle_drawbridge_open = SceneProp("castle_drawbridge_open", "castle_drawbridges_open", "bo_castle_drawbridges_open")

castle_drawbridge_closed = SceneProp("castle_drawbridge_closed", "castle_drawbridges_closed", "bo_castle_drawbridges_closed")

spike_group_a = SceneProp("spike_group_a", "spike_group_a", "bo_spike_group_a")

spike_a = SceneProp("spike_a", "spike_a", "bo_spike_a")

belfry_a = SceneProp("belfry_a", "belfry_a", "bo_belfry_a")
belfry_a.add_flag(ScenePropFlag.MOVEABLE)

belfry_b = SceneProp("belfry_b", "belfry_b", "bo_belfry_b")
belfry_b.add_flag(ScenePropFlag.MOVEABLE)

belfry_b_platform_a = SceneProp("belfry_b_platform_a", "belfry_b_platform_a", "bo_belfry_b_platform_a")
belfry_b_platform_a.add_flag(ScenePropFlag.MOVEABLE)

belfry_old = SceneProp("belfry_old", "belfry_a", "bo_belfry_a")

belfry_platform_a = SceneProp("belfry_platform_a", "belfry_platform_a", "bo_belfry_platform_a")
belfry_platform_a.add_flag(ScenePropFlag.MOVEABLE)

belfry_platform_b = SceneProp("belfry_platform_b", "belfry_platform_b", "bo_belfry_platform_b")
belfry_platform_b.add_flag(ScenePropFlag.MOVEABLE)

belfry_platform_old = SceneProp("belfry_platform_old", "belfry_platform_b", "bo_belfry_platform_b")

belfry_wheel = SceneProp("belfry_wheel", "belfry_wheel", "0")
belfry_wheel.add_flag(ScenePropFlag.MOVEABLE)

belfry_wheel_old = SceneProp("belfry_wheel_old", "belfry_wheel", "0")

mangonel = SceneProp("mangonel", "mangonel", "bo_mangonel")

trebuchet_old = SceneProp("trebuchet_old", "trebuchet_old", "bo_trebuchet_old")

trebuchet_new = SceneProp("trebuchet_new", "trebuchet_new", "bo_trebuchet_old")

trebuchet_destructible = SceneProp("trebuchet_destructible", "trebuchet_new", "bo_trebuchet_old")
trebuchet_destructible.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
trebuchet_destructible.add_flag(ScenePropFlag.DESTRUCTIBLE)
trebuchet_destructible.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,2400)
trigger0.codeBlock = code
trebuchet_destructible.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var001):
    play_sound(snd.dummy_destroyed)
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        pos1 = prop_instance_get_position(var001)
        particle_system_burst(psys.dummy_smoke_big,1,100)
        particle_system_burst(psys.dummy_straw_big,1,100)
        position_move_z(1,-500)
        position_rotate_x(1,90)
        prop_instance_animate_to_position(var001,1,300)
        if _g_round_ended == 0:
            team_no_002 = scene_prop_get_team(var001)
            if team_no_002 == 0:
                var003 = -1
            else:
                var003 = 1
            #end
            if _g_number_of_targets_destroyed == 0:
                var004 = var003 * 2
                show_multiplayer_message(15,var004)
                max_players = get_max_players()
                for player_id_006 in range(1, max_players):
                    if player_is_active(player_id_006):
                        multiplayer_send_2_int_to_player(player_id_006,68,15,var004)
                    #end
                #end
                _g_number_of_targets_destroyed += 1
            else:
                var004 = var003 * 9
                show_multiplayer_message(15,var004)
                max_players = get_max_players()
                for player_id_006 in range(1, max_players):
                    if player_is_active(player_id_006):
                        multiplayer_send_2_int_to_player(player_id_006,68,15,var004)
                    #end
                #end
                _g_number_of_targets_destroyed += 1
            #end
        #end
        var007 = 0
        max_players = get_max_players()
        for player_id_006 in range(0, max_players):
            if player_is_active(player_id_006):
                if spr.trebuchet_destructible == _g_destructible_target_1:
                    player_slot_008 = player_get_slot(player_id_006,32)
                else:
                    player_slot_008 = player_get_slot(player_id_006,33)
                #end
            #end
            var007 += player_slot_008
        #end
        var009 = 0
        max_players = get_max_players()
        for player_id_006 in range(0, max_players):
            if player_is_active(player_id_006):
                var009 += 50
            #end
        #end
        if var009 >= 1500:
            var009 = 1500
        #end
        var009 *= _g_multiplayer_battle_earnings_multiplier
        var009 /= 100
        max_players = get_max_players()
        for player_id_006 in range(0, max_players):
            if player_is_active(player_id_006):
                if spr.trebuchet_destructible == _g_destructible_target_1:
                    player_slot_008 = player_get_slot(player_id_006,32)
                else:
                    player_slot_008 = player_get_slot(player_id_006,33)
                #end
            #end
            gold_010 = player_get_gold(player_id_006)
            player_slot_008 *= var009
            var011 = player_slot_008 / var007
            gold_010 += var011
            player_set_gold(player_id_006,gold_010,15000)
        #end
    #end
trigger1.codeBlock = code
trebuchet_destructible.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
        set_fixed_point_multiplier(1)
        pos_x_004 = position_get_x(2)
        if pos_x_004 >= 0 and agent_is_alive(pos_x_004) and agent_is_human(pos_x_004) and not agent_is_non_player(pos_x_004):
            agent_player_id_005 = agent_get_player_id(pos_x_004)
            if agent_player_id_005 >= 0 and player_is_active(agent_player_id_005):
                if spr.trebuchet_destructible == _g_destructible_target_1:
                    player_slot_006 = player_get_slot(agent_player_id_005,32)
                    player_slot_006 += var002
                    player_set_slot(agent_player_id_005,32,player_slot_006)
                else:
                    player_slot_006 = player_get_slot(agent_player_id_005,33)
                    player_slot_006 += var002
                    player_set_slot(agent_player_id_005,33,player_slot_006)
                #end
            #end
        #end
    #end
trigger2.codeBlock = code
trebuchet_destructible.add_trigger(trigger2)

stone_ball = SceneProp("stone_ball", "stone_ball", "0")

village_house_a = SceneProp("village_house_a", "village_house_a", "bo_village_house_a")

village_house_b = SceneProp("village_house_b", "village_house_b", "bo_village_house_b")

village_house_c = SceneProp("village_house_c", "village_house_c", "bo_village_house_c")

village_house_d = SceneProp("village_house_d", "village_house_d", "bo_village_house_d")

farm_house_a = SceneProp("farm_house_a", "farm_house_a", "bo_farm_house_a")

farm_house_b = SceneProp("farm_house_b", "farm_house_b", "bo_farm_house_b")

farm_house_c = SceneProp("farm_house_c", "farm_house_c", "bo_farm_house_c")

mountain_house_a = SceneProp("mountain_house_a", "mountain_house_a", "bo_mountain_house_a")

mountain_house_b = SceneProp("mountain_house_b", "mountain_house_b", "bo_mountain_house_b")

village_hut_a = SceneProp("village_hut_a", "village_hut_a", "bo_village_hut_a")

crude_fence = SceneProp("crude_fence", "fence", "bo_fence")

crude_fence_small = SceneProp("crude_fence_small", "crude_fence_small", "bo_crude_fence_small")

crude_fence_small_b = SceneProp("crude_fence_small_b", "crude_fence_small_b", "bo_crude_fence_small_b")

ramp_12m = SceneProp("ramp_12m", "ramp_12m", "bo_ramp_12m")

ramp_14m = SceneProp("ramp_14m", "ramp_14m", "bo_ramp_14m")

siege_ladder_6m = SceneProp("siege_ladder_6m", "siege_ladder_move_6m", "bo_siege_ladder_move_6m")
siege_ladder_6m.add_flag(ScenePropFlag.TYPE_LADDER)

siege_ladder_8m = SceneProp("siege_ladder_8m", "siege_ladder_move_8m", "bo_siege_ladder_move_8m")
siege_ladder_8m.add_flag(ScenePropFlag.TYPE_LADDER)

siege_ladder_10m = SceneProp("siege_ladder_10m", "siege_ladder_move_10m", "bo_siege_ladder_move_10m")
siege_ladder_10m.add_flag(ScenePropFlag.TYPE_LADDER)

siege_ladder_12m = SceneProp("siege_ladder_12m", "siege_ladder_12m", "bo_siege_ladder_12m")
siege_ladder_12m.add_flag(ScenePropFlag.TYPE_LADDER)

siege_ladder_14m = SceneProp("siege_ladder_14m", "siege_ladder_14m", "bo_siege_ladder_14m")
siege_ladder_14m.add_flag(ScenePropFlag.TYPE_LADDER)

siege_ladder_move_6m = SceneProp("siege_ladder_move_6m", "siege_ladder_move_6m", "bo_siege_ladder_move_6m")
siege_ladder_move_6m.add_flag(ScenePropFlag.TYPE_LADDER)
siege_ladder_move_6m.add_flag(ScenePropFlag.MOVEABLE)
siege_ladder_move_6m.set_use_time(2)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, var002):
    use_item(var002,var001)
    max_players = get_max_players()
    for player_id_004 in range(1, max_players):
        if player_is_active(player_id_004):
            multiplayer_send_2_int_to_player(player_id_004,76,var002,var001)
        #end
    #end
trigger0.codeBlock = code
siege_ladder_move_6m.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_is_animating)
def code(var001, var002):
    check_creating_ladder_dust_effect(var001,var002)
trigger1.codeBlock = code
siege_ladder_move_6m.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_animation_finished)
def code(var001):
    prop_instance_enable_physics(var001,1)
trigger2.codeBlock = code
siege_ladder_move_6m.add_trigger(trigger2)

siege_ladder_move_8m = SceneProp("siege_ladder_move_8m", "siege_ladder_move_8m", "bo_siege_ladder_move_8m")
siege_ladder_move_8m.add_flag(ScenePropFlag.TYPE_LADDER)
siege_ladder_move_8m.add_flag(ScenePropFlag.MOVEABLE)
siege_ladder_move_8m.set_use_time(2)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, var002):
    use_item(var002,var001)
    max_players = get_max_players()
    for player_id_004 in range(1, max_players):
        if player_is_active(player_id_004):
            multiplayer_send_2_int_to_player(player_id_004,76,var002,var001)
        #end
    #end
trigger0.codeBlock = code
siege_ladder_move_8m.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_is_animating)
def code(var001, var002):
    check_creating_ladder_dust_effect(var001,var002)
trigger1.codeBlock = code
siege_ladder_move_8m.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_animation_finished)
def code(var001):
    prop_instance_enable_physics(var001,1)
trigger2.codeBlock = code
siege_ladder_move_8m.add_trigger(trigger2)

siege_ladder_move_10m = SceneProp("siege_ladder_move_10m", "siege_ladder_move_10m", "bo_siege_ladder_move_10m")
siege_ladder_move_10m.add_flag(ScenePropFlag.TYPE_LADDER)
siege_ladder_move_10m.add_flag(ScenePropFlag.MOVEABLE)
siege_ladder_move_10m.set_use_time(3)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, var002):
    use_item(var002,var001)
    max_players = get_max_players()
    for player_id_004 in range(1, max_players):
        if player_is_active(player_id_004):
            multiplayer_send_2_int_to_player(player_id_004,76,var002,var001)
        #end
    #end
trigger0.codeBlock = code
siege_ladder_move_10m.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_is_animating)
def code(var001, var002):
    check_creating_ladder_dust_effect(var001,var002)
trigger1.codeBlock = code
siege_ladder_move_10m.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_animation_finished)
def code(var001):
    prop_instance_enable_physics(var001,1)
trigger2.codeBlock = code
siege_ladder_move_10m.add_trigger(trigger2)

siege_ladder_move_12m = SceneProp("siege_ladder_move_12m", "siege_ladder_move_12m", "bo_siege_ladder_move_12m")
siege_ladder_move_12m.add_flag(ScenePropFlag.TYPE_LADDER)
siege_ladder_move_12m.add_flag(ScenePropFlag.MOVEABLE)
siege_ladder_move_12m.set_use_time(3)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, var002):
    use_item(var002,var001)
    max_players = get_max_players()
    for player_id_004 in range(1, max_players):
        if player_is_active(player_id_004):
            multiplayer_send_2_int_to_player(player_id_004,76,var002,var001)
        #end
    #end
trigger0.codeBlock = code
siege_ladder_move_12m.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_is_animating)
def code(var001, var002):
    check_creating_ladder_dust_effect(var001,var002)
trigger1.codeBlock = code
siege_ladder_move_12m.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_animation_finished)
def code(var001):
    prop_instance_enable_physics(var001,1)
trigger2.codeBlock = code
siege_ladder_move_12m.add_trigger(trigger2)

siege_ladder_move_14m = SceneProp("siege_ladder_move_14m", "siege_ladder_move_14m", "bo_siege_ladder_move_14m")
siege_ladder_move_14m.add_flag(ScenePropFlag.TYPE_LADDER)
siege_ladder_move_14m.add_flag(ScenePropFlag.MOVEABLE)
siege_ladder_move_14m.set_use_time(4)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, var002):
    use_item(var002,var001)
    max_players = get_max_players()
    for player_id_004 in range(1, max_players):
        if player_is_active(player_id_004):
            multiplayer_send_2_int_to_player(player_id_004,76,var002,var001)
        #end
    #end
trigger0.codeBlock = code
siege_ladder_move_14m.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_is_animating)
def code(var001, var002):
    check_creating_ladder_dust_effect(var001,var002)
trigger1.codeBlock = code
siege_ladder_move_14m.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_animation_finished)
def code(var001):
    prop_instance_enable_physics(var001,1)
trigger2.codeBlock = code
siege_ladder_move_14m.add_trigger(trigger2)

portcullis = SceneProp("portcullis", "portcullis_a", "bo_portcullis_a")
portcullis.add_flag(ScenePropFlag.MOVEABLE)

bed_a = SceneProp("bed_a", "bed_a", "bo_bed_a")

bed_b = SceneProp("bed_b", "bed_b", "bo_bed_b")

bed_c = SceneProp("bed_c", "bed_c", "bo_bed_c")

bed_d = SceneProp("bed_d", "bed_d", "bo_bed_d")

bed_e = SceneProp("bed_e", "bed_e", "bo_bed_e")

bed_f = SceneProp("bed_f", "bed_f", "bo_bed_f")

towngate_door_left = SceneProp("towngate_door_left", "door_g_left", "bo_door_left")
towngate_door_left.add_flag(ScenePropFlag.MOVEABLE)

towngate_door_right = SceneProp("towngate_door_right", "door_g_right", "bo_door_right")
towngate_door_right.add_flag(ScenePropFlag.MOVEABLE)

towngate_rectangle_door_left = SceneProp("towngate_rectangle_door_left", "towngate_rectangle_door_left", "bo_towngate_rectangle_door_left")
towngate_rectangle_door_left.add_flag(ScenePropFlag.MOVEABLE)

towngate_rectangle_door_right = SceneProp("towngate_rectangle_door_right", "towngate_rectangle_door_right", "bo_towngate_rectangle_door_right")
towngate_rectangle_door_right.add_flag(ScenePropFlag.MOVEABLE)

door_screen = SceneProp("door_screen", "door_screen", "0")
door_screen.add_flag(ScenePropFlag.MOVEABLE)

door_a = SceneProp("door_a", "door_a", "bo_door_a")
door_a.add_flag(ScenePropFlag.MOVEABLE)

door_b = SceneProp("door_b", "door_b", "bo_door_a")
door_b.add_flag(ScenePropFlag.MOVEABLE)

door_c = SceneProp("door_c", "door_c", "bo_door_a")
door_c.add_flag(ScenePropFlag.MOVEABLE)

door_d = SceneProp("door_d", "door_d", "bo_door_a")
door_d.add_flag(ScenePropFlag.MOVEABLE)

tavern_door_a = SceneProp("tavern_door_a", "tavern_door_a", "bo_tavern_door_a")
tavern_door_a.add_flag(ScenePropFlag.MOVEABLE)

tavern_door_b = SceneProp("tavern_door_b", "tavern_door_b", "bo_tavern_door_a")
tavern_door_b.add_flag(ScenePropFlag.MOVEABLE)

door_e_left = SceneProp("door_e_left", "door_e_left", "bo_door_left")
door_e_left.add_flag(ScenePropFlag.MOVEABLE)

door_e_right = SceneProp("door_e_right", "door_e_right", "bo_door_right")
door_e_right.add_flag(ScenePropFlag.MOVEABLE)

door_f_left = SceneProp("door_f_left", "door_f_left", "bo_door_left")
door_f_left.add_flag(ScenePropFlag.MOVEABLE)

door_f_right = SceneProp("door_f_right", "door_f_right", "bo_door_right")
door_f_right.add_flag(ScenePropFlag.MOVEABLE)

door_h_left = SceneProp("door_h_left", "door_g_left", "bo_door_left")
door_h_left.add_flag(ScenePropFlag.MOVEABLE)

door_h_right = SceneProp("door_h_right", "door_g_right", "bo_door_right")
door_h_right.add_flag(ScenePropFlag.MOVEABLE)

draw_bridge_a = SceneProp("draw_bridge_a", "draw_bridge_a", "bo_draw_bridge_a")

chain_1m = SceneProp("chain_1m", "chain_1m", "0")

chain_2m = SceneProp("chain_2m", "chain_2m", "0")

chain_5m = SceneProp("chain_5m", "chain_5m", "0")

chain_10m = SceneProp("chain_10m", "chain_10m", "0")

bridge_modular_a = SceneProp("bridge_modular_a", "bridge_modular_a", "bo_bridge_modular_a")

bridge_modular_b = SceneProp("bridge_modular_b", "bridge_modular_b", "bo_bridge_modular_b")

church_a = SceneProp("church_a", "church_a", "bo_church_a")

church_tower_a = SceneProp("church_tower_a", "church_tower_a", "bo_church_tower_a")

stone_step_a = SceneProp("stone_step_a", "floor_stone_a", "bo_floor_stone_a")

stone_step_b = SceneProp("stone_step_b", "stone_step_b", "0")

stone_step_c = SceneProp("stone_step_c", "stone_step_c", "0")

stone_heap = SceneProp("stone_heap", "stone_heap", "bo_stone_heap")

stone_heap_b = SceneProp("stone_heap_b", "stone_heap_b", "bo_stone_heap")

panel_door_a = SceneProp("panel_door_a", "house_door_a", "bo_house_door_a")

panel_door_b = SceneProp("panel_door_b", "house_door_b", "bo_house_door_a")

smoke_stain = SceneProp("smoke_stain", "soot_a", "0")

brazier_with_fire = SceneProp("brazier_with_fire", "brazier", "bo_brazier")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    set_position_delta(0,0,85)
    particle_system_add_new(psys.brazier_fire_1)
    particle_system_add_new(psys.fire_sparks_1)
    set_position_delta(0,0,100)
    particle_system_add_new(psys.fire_glow_1)
    particle_system_emit(psys.fire_glow_1,9000000)
trigger0.codeBlock = code
brazier_with_fire.add_trigger(trigger0)

cooking_fire = SceneProp("cooking_fire", "fire_floor", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    set_position_delta(0,0,12)
    particle_system_add_new(psys.cooking_fire_1)
    particle_system_add_new(psys.fire_sparks_1)
    particle_system_add_new(psys.cooking_smoke)
    set_position_delta(0,0,50)
    particle_system_add_new(psys.fire_glow_1)
    particle_system_emit(psys.fire_glow_1,9000000)
trigger0.codeBlock = code
cooking_fire.add_trigger(trigger0)

cauldron_a = SceneProp("cauldron_a", "cauldron_a", "bo_cauldron_a")

fry_pan_a = SceneProp("fry_pan_a", "fry_pan_a", "0")

tripod_cauldron_a = SceneProp("tripod_cauldron_a", "tripod_cauldron_a", "bo_tripod_cauldron_a")

tripod_cauldron_b = SceneProp("tripod_cauldron_b", "tripod_cauldron_b", "bo_tripod_cauldron_b")

open_stable_a = SceneProp("open_stable_a", "open_stable_a", "bo_open_stable_a")

open_stable_b = SceneProp("open_stable_b", "open_stable_b", "bo_open_stable_b")

plate_a = SceneProp("plate_a", "plate_a", "0")

plate_b = SceneProp("plate_b", "plate_b", "0")

plate_c = SceneProp("plate_c", "plate_c", "0")

lettuce = SceneProp("lettuce", "lettuce", "0")

hanger = SceneProp("hanger", "hanger", "0")

knife_eating = SceneProp("knife_eating", "knife_eating", "0")

colander = SceneProp("colander", "colander", "0")

ladle = SceneProp("ladle", "ladle", "0")

spoon = SceneProp("spoon", "spoon", "0")

skewer = SceneProp("skewer", "skewer", "0")

grape_a = SceneProp("grape_a", "grape_a", "0")

grape_b = SceneProp("grape_b", "grape_b", "0")

apple_a = SceneProp("apple_a", "apple_a", "0")

apple_b = SceneProp("apple_b", "apple_b", "0")

maize_a = SceneProp("maize_a", "maize_a", "0")

maize_b = SceneProp("maize_b", "maize_b", "0")

cabbage = SceneProp("cabbage", "cabbage", "0")

flax_bundle = SceneProp("flax_bundle", "raw_flax", "0")

olive_plane = SceneProp("olive_plane", "olive_plane", "0")

grapes_plane = SceneProp("grapes_plane", "grapes_plane", "0")

date_fruit_plane = SceneProp("date_fruit_plane", "date_fruit_plane", "0")

bowl = SceneProp("bowl", "bowl_big", "0")

bowl_small = SceneProp("bowl_small", "bowl_small", "0")

dye_blue = SceneProp("dye_blue", "raw_dye_blue", "0")

dye_red = SceneProp("dye_red", "raw_dye_red", "0")

dye_yellow = SceneProp("dye_yellow", "raw_dye_yellow", "0")

basket = SceneProp("basket", "basket_small", "0")

basket_big = SceneProp("basket_big", "basket_large", "0")

basket_big_green = SceneProp("basket_big_green", "basket_big", "0")

leatherwork_frame = SceneProp("leatherwork_frame", "leatherwork_frame", "0")

cabbage_b = SceneProp("cabbage_b", "cabbage_b", "0")

bean = SceneProp("bean", "bean", "0")

basket_a = SceneProp("basket_a", "basket_a", "bo_basket_a")

feeding_trough_a = SceneProp("feeding_trough_a", "feeding_trough_a", "bo_feeding_trough_a")

marrow_a = SceneProp("marrow_a", "marrow_a", "0")

marrow_b = SceneProp("marrow_b", "marrow_b", "0")

squash_plant = SceneProp("squash_plant", "marrow_c", "0")

gatehouse_new_a = SceneProp("gatehouse_new_a", "gatehouse_new_a", "bo_gatehouse_new_a")

gatehouse_new_b = SceneProp("gatehouse_new_b", "gatehouse_new_b", "bo_gatehouse_new_b")

gatehouse_new_snowy_a = SceneProp("gatehouse_new_snowy_a", "gatehouse_new_snowy_a", "bo_gatehouse_new_b")

winch = SceneProp("winch", "winch", "bo_winch")
winch.add_flag(ScenePropFlag.MOVEABLE)

winch_b = SceneProp("winch_b", "winch_b", "bo_winch")
winch_b.add_flag(ScenePropFlag.MOVEABLE)
winch_b.set_use_time(5)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, var002):
    use_item(var002,var001)
    max_players = get_max_players()
    for player_id_004 in range(1, max_players):
        if player_is_active(player_id_004):
            multiplayer_send_2_int_to_player(player_id_004,76,var002,var001)
        #end
    #end
trigger0.codeBlock = code
winch_b.add_trigger(trigger0)

drawbridge = SceneProp("drawbridge", "drawbridge", "bo_drawbridge")

gatehouse_door_left = SceneProp("gatehouse_door_left", "gatehouse_door_left", "bo_gatehouse_door_left")
gatehouse_door_left.add_flag(ScenePropFlag.MOVEABLE)

gatehouse_door_right = SceneProp("gatehouse_door_right", "gatehouse_door_right", "bo_gatehouse_door_right")
gatehouse_door_right.add_flag(ScenePropFlag.MOVEABLE)

cheese_a = SceneProp("cheese_a", "cheese_a", "0")

cheese_b = SceneProp("cheese_b", "cheese_b", "0")

cheese_slice_a = SceneProp("cheese_slice_a", "cheese_slice_a", "0")

bread_a = SceneProp("bread_a", "bread_a", "0")

bread_b = SceneProp("bread_b", "bread_b", "0")

bread_slice_a = SceneProp("bread_slice_a", "bread_slice_a", "0")

fish_a = SceneProp("fish_a", "fish_a", "0")

fish_roasted_a = SceneProp("fish_roasted_a", "fish_roasted_a", "0")

chicken_roasted = SceneProp("chicken_roasted", "chicken", "0")

food_steam = SceneProp("food_steam", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    set_position_delta(0,0,0)
    particle_system_add_new(psys.food_steam)
trigger0.codeBlock = code
food_steam.add_trigger(trigger0)

city_smoke = SceneProp("city_smoke", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    reg12 = store_time_of_day()
    if not is_between(reg12,5,20):
        set_position_delta(0,0,0)
        particle_system_add_new(psys.night_smoke_1)
trigger0.codeBlock = code
city_smoke.add_trigger(trigger0)

city_fire_fly_night = SceneProp("city_fire_fly_night", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    reg12 = store_time_of_day()
    if not is_between(reg12,5,20):
        set_position_delta(0,0,0)
        particle_system_add_new(psys.fire_fly_1)
trigger0.codeBlock = code
city_fire_fly_night.add_trigger(trigger0)

city_fly_day = SceneProp("city_fly_day", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    particle_system_add_new(psys.bug_fly_1)
trigger0.codeBlock = code
city_fly_day.add_trigger(trigger0)

flue_smoke_tall = SceneProp("flue_smoke_tall", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    particle_system_add_new(psys.flue_smoke_tall)
trigger0.codeBlock = code
flue_smoke_tall.add_trigger(trigger0)

flue_smoke_short = SceneProp("flue_smoke_short", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    particle_system_add_new(psys.flue_smoke_short)
trigger0.codeBlock = code
flue_smoke_short.add_trigger(trigger0)

moon_beam = SceneProp("moon_beam", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    particle_system_add_new(psys.moon_beam_1)
    particle_system_add_new(psys.moon_beam_paricle_1)
trigger0.codeBlock = code
moon_beam.add_trigger(trigger0)

fire_small = SceneProp("fire_small", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    particle_system_add_new(psys.fireplace_fire_small)
trigger0.codeBlock = code
fire_small.add_trigger(trigger0)

fire_big = SceneProp("fire_big", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    particle_system_add_new(psys.fireplace_fire_big)
trigger0.codeBlock = code
fire_big.add_trigger(trigger0)

battle_field_smoke = SceneProp("battle_field_smoke", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    particle_system_add_new(psys.war_smoke_tall)
trigger0.codeBlock = code
battle_field_smoke.add_trigger(trigger0)

Village_fire_big = SceneProp("village_fire_big", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    particle_system_add_new(psys.village_fire_big)
    set_position_delta(0,0,100)
    particle_system_add_new(psys.village_fire_smoke_big)
trigger0.codeBlock = code
Village_fire_big.add_trigger(trigger0)

candle_a = SceneProp("candle_a", "candle_a", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    set_position_delta(0,0,27)
    particle_system_add_new(psys.candle_light)
trigger0.codeBlock = code
candle_a.add_trigger(trigger0)

candle_b = SceneProp("candle_b", "candle_b", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    set_position_delta(0,0,25)
    particle_system_add_new(psys.candle_light)
trigger0.codeBlock = code
candle_b.add_trigger(trigger0)

candle_c = SceneProp("candle_c", "candle_c", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    set_position_delta(0,0,10)
    particle_system_add_new(psys.candle_light_small)
trigger0.codeBlock = code
candle_c.add_trigger(trigger0)

lamp_a = SceneProp("lamp_a", "lamp_a", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    set_position_delta(66,0,2)
    particle_system_add_new(psys.candle_light)
trigger0.codeBlock = code
lamp_a.add_trigger(trigger0)

lamp_b = SceneProp("lamp_b", "lamp_b", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    set_position_delta(65,0,-7)
    particle_system_add_new(psys.lamp_fire)
    set_position_delta(70,0,-5)
    particle_system_add_new(psys.fire_glow_1)
    particle_system_emit(psys.fire_glow_1,9000000)
    play_sound(snd.fire_loop,0)
trigger0.codeBlock = code
lamp_b.add_trigger(trigger0)

hook_a = SceneProp("hook_a", "hook_a", "0")

window_night = SceneProp("window_night", "window_night", "0")

fried_pig = SceneProp("fried_pig", "pork", "0")

village_oven = SceneProp("village_oven", "village_oven", "bo_village_oven")

dungeon_water_drops = SceneProp("dungeon_water_drops", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    particle_system_add_new(psys.dungeon_water_drops)
trigger0.codeBlock = code
dungeon_water_drops.add_trigger(trigger0)

shadow_circle_1 = SceneProp("shadow_circle_1", "shadow_circle_1", "0")

shadow_circle_2 = SceneProp("shadow_circle_2", "shadow_circle_2", "0")

shadow_square_1 = SceneProp("shadow_square_1", "shadow_square_1", "0")

shadow_square_2 = SceneProp("shadow_square_2", "shadow_square_2", "0")

wheelbarrow = SceneProp("wheelbarrow", "wheelbarrow", "bo_wheelbarrow")

gourd = SceneProp("gourd", "gourd", "bo_gourd")
gourd.add_flag(ScenePropFlag.DESTRUCTIBLE)
gourd.add_flag(ScenePropFlag.MOVEABLE)
gourd.add_flag(ScenePropFlag.ENFORCE_SHADOWS)
gourd.set_hit_points(1)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var001):
    _g_last_destroyed_gourds += 1
    pos1 = prop_instance_get_position(var001)
    copy_position(2,1)
    position_set_z(2,-100000)
    particle_system_burst(psys.gourd_smoke,1,2)
    particle_system_burst(psys.gourd_piece_1,1,1)
    particle_system_burst(psys.gourd_piece_2,1,5)
    prop_instance_animate_to_position(var001,2,1)
    play_sound(snd.gourd_destroyed)
trigger0.codeBlock = code
gourd.add_trigger(trigger0)

gourd_spike = SceneProp("gourd_spike", "gourd_spike", "bo_gourd_spike")
gourd_spike.add_flag(ScenePropFlag.MOVEABLE)

obstacle_fence_1 = SceneProp("obstacle_fence_1", "fence", "bo_fence")

obstacle_fallen_tree_a = SceneProp("obstacle_fallen_tree_a", "destroy_tree_a", "bo_destroy_tree_a")

obstacle_fallen_tree_b = SceneProp("obstacle_fallen_tree_b", "destroy_tree_b", "bo_destroy_tree_b")

siege_wall_a = SceneProp("siege_wall_a", "siege_wall_a", "bo_siege_wall_a")

siege_large_shield_a = SceneProp("siege_large_shield_a", "siege_large_shield_a", "bo_siege_large_shield_a")

granary_a = SceneProp("granary_a", "granary_a", "bo_granary_a")

small_wall_connect_a = SceneProp("small_wall_connect_a", "small_wall_connect_a", "bo_small_wall_connect_a")

full_stable_a = SceneProp("full_stable_a", "full_stable_a", "bo_full_stable_a")

full_stable_b = SceneProp("full_stable_b", "full_stable_b", "bo_full_stable_b")

full_stable_c = SceneProp("full_stable_c", "full_stable_c", "bo_full_stable_c")

full_stable_d = SceneProp("full_stable_d", "full_stable_d", "bo_full_stable_d")

arabian_house_a = SceneProp("arabian_house_a", "arabian_house_a", "bo_arabian_house_a")

arabian_house_b = SceneProp("arabian_house_b", "arabian_house_b", "bo_arabian_house_b")

arabian_house_c = SceneProp("arabian_house_c", "arabian_house_c", "bo_arabian_house_c")

arabian_house_d = SceneProp("arabian_house_d", "arabian_house_d", "bo_arabian_house_d")

arabian_house_e = SceneProp("arabian_house_e", "arabian_house_e", "bo_arabian_house_e")

arabian_house_f = SceneProp("arabian_house_f", "arabian_house_f", "bo_arabian_house_f")

arabian_house_g = SceneProp("arabian_house_g", "arabian_house_g", "bo_arabian_house_g")

arabian_house_h = SceneProp("arabian_house_h", "arabian_house_h", "bo_arabian_house_h")

arabian_house_i = SceneProp("arabian_house_i", "arabian_house_i", "bo_arabian_house_i")

arabian_square_keep_a = SceneProp("arabian_square_keep_a", "arabian_square_keep_a", "bo_arabian_square_keep_a")

arabian_passage_house_a = SceneProp("arabian_passage_house_a", "arabian_passage_house_a", "bo_arabian_passage_house_a")

arabian_wall_a = SceneProp("arabian_wall_a", "arabian_wall_a", "bo_arabian_wall_a")

arabian_wall_b = SceneProp("arabian_wall_b", "arabian_wall_b", "bo_arabian_wall_b")

arabian_ground_a = SceneProp("arabian_ground_a", "arabian_ground_a", "bo_arabian_ground_a")

arabian_parterre_a = SceneProp("arabian_parterre_a", "arabian_parterre_a", "bo_arabian_parterre_a")

well_shaft = SceneProp("well_shaft", "well_shaft", "bo_well_shaft")

horse_mill = SceneProp("horse_mill", "horse_mill", "bo_horse_mill")

horse_mill_collar = SceneProp("horse_mill_collar", "horse_mill_collar", "bo_horse_mill_collar")

arabian_stable = SceneProp("arabian_stable", "arabian_stable", "bo_arabian_stable")

arabian_tent = SceneProp("arabian_tent", "arabian_tent", "bo_arabian_tent")

arabian_tent_b = SceneProp("arabian_tent_b", "arabian_tent_b", "bo_arabian_tent_b")

desert_plant_a = SceneProp("desert_plant_a", "desert_plant_a", "0")

arabian_castle_battlement_a = SceneProp("arabian_castle_battlement_a", "arabian_castle_battlement_a", "bo_arabian_castle_battlement_a")

arabian_castle_battlement_b_destroyed = SceneProp("arabian_castle_battlement_b_destroyed", "arabian_castle_battlement_b_destroyed", "bo_arabian_castle_battlement_b_destroyed")

arabian_castle_battlement_c = SceneProp("arabian_castle_battlement_c", "arabian_castle_battlement_c", "bo_arabian_castle_battlement_c")

arabian_castle_battlement_d = SceneProp("arabian_castle_battlement_d", "arabian_castle_battlement_d", "bo_arabian_castle_battlement_d")

arabian_castle_corner_a = SceneProp("arabian_castle_corner_a", "arabian_castle_corner_a", "bo_arabian_castle_corner_a")

arabian_castle_stairs = SceneProp("arabian_castle_stairs", "arabian_castle_stairs", "bo_arabian_castle_stairs")
arabian_castle_stairs.add_flag(ScenePropFlag.TYPE_LADDER)

arabian_castle_stairs_b = SceneProp("arabian_castle_stairs_b", "arabian_castle_stairs_b", "bo_arabian_castle_stairs_b")
arabian_castle_stairs_b.add_flag(ScenePropFlag.TYPE_LADDER)

arabian_castle_stairs_c = SceneProp("arabian_castle_stairs_c", "arabian_castle_stairs_c", "bo_arabian_castle_stairs_c")
arabian_castle_stairs_c.add_flag(ScenePropFlag.TYPE_LADDER)

arabian_castle_battlement_section_a = SceneProp("arabian_castle_battlement_section_a", "arabian_castle_battlement_section_a", "bo_arabian_castle_battlement_section_a")

arabian_castle_gate_house_a = SceneProp("arabian_castle_gate_house_a", "arabian_castle_gate_house_a", "bo_arabian_castle_gate_house_a")

arabian_castle_house_a = SceneProp("arabian_castle_house_a", "arabian_castle_house_a", "bo_arabian_castle_house_a")

arabian_castle_house_b = SceneProp("arabian_castle_house_b", "arabian_castle_house_b", "bo_arabian_castle_house_b")

arabian_castle_keep_a = SceneProp("arabian_castle_keep_a", "arabian_castle_keep_a", "bo_arabian_castle_keep_a")

arabian_house_a2 = SceneProp("arabian_house_a2", "arabian_house_a2", "bo_arabian_house_a2")

arabian_village_house_a = SceneProp("arabian_village_house_a", "arabian_village_house_a", "bo_arabian_village_house_a")

arabian_village_house_b = SceneProp("arabian_village_house_b", "arabian_village_house_b", "bo_arabian_village_house_b")

arabian_village_house_c = SceneProp("arabian_village_house_c", "arabian_village_house_c", "bo_arabian_village_house_c")

arabian_village_house_d = SceneProp("arabian_village_house_d", "arabian_village_house_d", "bo_arabian_village_house_d")

arabian_village_stable = SceneProp("arabian_village_stable", "arabian_village_stable", "bo_arabian_village_stable")

arabian_village_hut = SceneProp("arabian_village_hut", "arabian_village_hut", "bo_arabian_village_hut")

arabian_village_stairs = SceneProp("arabian_village_stairs", "arabian_village_stairs", "bo_arabian_village_stairs")
arabian_village_stairs.add_flag(ScenePropFlag.TYPE_LADDER)

tree_a01 = SceneProp("tree_a01", "tree_a01", "bo_tree_a01")

stairs_a = SceneProp("stairs_a", "stairs_a", "bo_stairs_a")
stairs_a.add_flag(ScenePropFlag.TYPE_LADDER)

headquarters_flag_red = SceneProp("headquarters_flag_red", "tutorial_flag_red", "0")
headquarters_flag_red.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_red.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_flag_blue = SceneProp("headquarters_flag_blue", "tutorial_flag_blue", "0")
headquarters_flag_blue.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_blue.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_flag_gray = SceneProp("headquarters_flag_gray", "tutorial_flag_yellow", "0")
headquarters_flag_gray.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_gray.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_flag_red_code_only = SceneProp("headquarters_flag_red_code_only", "mp_flag_red", "0")
headquarters_flag_red_code_only.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_red_code_only.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_flag_blue_code_only = SceneProp("headquarters_flag_blue_code_only", "mp_flag_blue", "0")
headquarters_flag_blue_code_only.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_blue_code_only.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_flag_gray_code_only = SceneProp("headquarters_flag_gray_code_only", "mp_flag_white", "0")
headquarters_flag_gray_code_only.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_gray_code_only.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_pole_code_only = SceneProp("headquarters_pole_code_only", "mp_flag_pole", "0")
headquarters_pole_code_only.add_flag(ScenePropFlag.MOVEABLE)

headquarters_flag_swadian = SceneProp("headquarters_flag_swadian", "flag_swadian", "0")
headquarters_flag_swadian.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_swadian.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_flag_vaegir = SceneProp("headquarters_flag_vaegir", "flag_vaegir", "0")
headquarters_flag_vaegir.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_vaegir.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_flag_khergit = SceneProp("headquarters_flag_khergit", "flag_khergit", "0")
headquarters_flag_khergit.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_khergit.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_flag_nord = SceneProp("headquarters_flag_nord", "flag_nord", "0")
headquarters_flag_nord.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_nord.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_flag_rhodok = SceneProp("headquarters_flag_rhodok", "flag_rhodok", "0")
headquarters_flag_rhodok.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_rhodok.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_flag_sarranid = SceneProp("headquarters_flag_sarranid", "flag_sarranid", "0")
headquarters_flag_sarranid.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_sarranid.add_flag(ScenePropFlag.FACE_PLAYER)

glow_a = SceneProp("glow_a", "glow_a", "0")

glow_b = SceneProp("glow_b", "glow_b", "0")

arabian_castle_corner_b = SceneProp("arabian_castle_corner_b", "arabian_castle_corner_b", "bo_arabian_castle_corner_b")

dummy_a_undestructable = SceneProp("dummy_a_undestructable", "arena_archery_target_b", "bo_arena_archery_target_b")
dummy_a_undestructable.add_flag(ScenePropFlag.DESTRUCTIBLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,10000000)
trigger0.codeBlock = code
dummy_a_undestructable.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        set_fixed_point_multiplier(1)
        pos_x_003 = position_get_x(2)
        agent_no_004 = get_player_agent_no()
        if agent_no_004 == pos_x_003:
            reg60 = var002
            print(gstr.delivered_damage)
            if _g_tutorial_training_ground_horseman_trainer_state == 6 and _g_tutorial_training_ground_horseman_trainer_completed_chapters == 1:
                prop_variation_id_2__005 = prop_instance_get_variation_id_2(var001)
                prop_variation_id_2__005 -= 1
                if _g_tutorial_training_ground_current_score == prop_variation_id_2__005:
                    _g_tutorial_training_ground_current_score += 1
                #end
            #end
        #end
    #end
    play_sound(snd.dummy_hit)
    particle_system_burst(psys.dummy_smoke,1,3)
    particle_system_burst(psys.dummy_straw,1,10)
trigger1.codeBlock = code
dummy_a_undestructable.add_trigger(trigger1)

cave_entrance_1 = SceneProp("cave_entrance_1", "cave_entrance_1", "bo_cave_entrance_1")

pointer_arrow = SceneProp("pointer_arrow", "pointer_arrow", "0")

fireplace_d_interior = SceneProp("fireplace_d_interior", "fireplace_d", "bo_fireplace_d")

ship_sail_off = SceneProp("ship_sail_off", "ship_sail_off", "bo_ship_sail_off")

ship_sail_off_b = SceneProp("ship_sail_off_b", "ship_sail_off_b", "bo_ship_sail_off")

ship_c_sail_off = SceneProp("ship_c_sail_off", "ship_c_sail_off", "bo_ship_c_sail_off")

ramp_small_a = SceneProp("ramp_small_a", "ramp_small_a", "bo_ramp_small_a")

castle_g_battlement_b = SceneProp("castle_g_battlement_b", "castle_g_battlement_b", "bo_castle_g_battlement_b")

box_a_dynamic = SceneProp("box_a_dynamic", "box_a", "bo_box_a")
box_a_dynamic.add_flag(ScenePropFlag.MOVEABLE)
box_a_dynamic.add_flag(ScenePropFlag.DYNAMIC_PHYSICS)

desert_field = SceneProp("desert_field", "desert_field", "bo_desert_field")

water_river = SceneProp("water_river", "water_plane", "0")

viking_house_a = SceneProp("viking_house_a", "viking_house_a", "bo_viking_house_a")

viking_house_b = SceneProp("viking_house_b", "viking_house_b", "bo_viking_house_b")

viking_house_c = SceneProp("viking_house_c", "viking_house_c", "bo_viking_house_c")

viking_house_d = SceneProp("viking_house_d", "viking_house_d", "bo_viking_house_d")

viking_house_e = SceneProp("viking_house_e", "viking_house_e", "bo_viking_house_e")

viking_stable_a = SceneProp("viking_stable_a", "viking_stable_a", "bo_viking_stable_a")

viking_keep = SceneProp("viking_keep", "viking_keep", "bo_viking_keep")

viking_house_c_destroy = SceneProp("viking_house_c_destroy", "viking_house_c_destroy", "bo_viking_house_c_destroy")

viking_house_b_destroy = SceneProp("viking_house_b_destroy", "viking_house_b_destroy", "bo_viking_house_b_destroy")

harbour_a = SceneProp("harbour_a", "harbour_a", "bo_harbour_a")

sea_foam_a = SceneProp("sea_foam_a", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    particle_system_add_new(psys.sea_foam_a)
trigger0.codeBlock = code
sea_foam_a.add_trigger(trigger0)

viking_keep_destroy = SceneProp("viking_keep_destroy", "viking_keep_destroy", "bo_viking_keep_destroy")

viking_keep_destroy_door = SceneProp("viking_keep_destroy_door", "viking_keep_destroy_door", "bo_viking_keep_destroy_door")

earth_tower_small_b = SceneProp("earth_tower_small_b", "earth_tower_small_b", "bo_earth_tower_small_b")

earth_gate_house_b = SceneProp("earth_gate_house_b", "earth_gate_house_b", "bo_earth_gate_house_b")

earth_tower_a = SceneProp("earth_tower_a", "earth_tower_a", "bo_earth_tower_a")

earth_stairs_c = SceneProp("earth_stairs_c", "earth_stairs_c", "bo_earth_stairs_c")

earth_sally_gate_left = SceneProp("earth_sally_gate_left", "earth_sally_gate_left", "bo_earth_sally_gate_left")
earth_sally_gate_left.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
earth_sally_gate_left.add_flag(ScenePropFlag.DESTRUCTIBLE)
earth_sally_gate_left.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, scene_prop_instance_id_002):
    pos1 = agent_get_position(var001)
    pos2 = prop_instance_get_starting_position(scene_prop_instance_id_002)
    scene_prop_slot_003 = scene_prop_get_slot(scene_prop_instance_id_002,1)
    if True:
        scene_prop_kind_004 = prop_instance_get_scene_prop_kind(scene_prop_instance_id_002)
        var005 = 0
        if scene_prop_kind_004 != spr.viking_keep_destroy_sally_door_right and scene_prop_kind_004 != spr.viking_keep_destroy_sally_door_left and scene_prop_kind_004 != spr.earth_sally_gate_right and scene_prop_kind_004 != spr.earth_sally_gate_left and position_is_behind_position(1,2):
            var005 = 1
        elif scene_prop_kind_004 == spr.viking_keep_destroy_sally_door_right or scene_prop_kind_004 == spr.viking_keep_destroy_sally_door_left or scene_prop_kind_004 == spr.earth_sally_gate_right or scene_prop_kind_004 == spr.earth_sally_gate_left and not position_is_behind_position(1,2):
            var005 = 1
        #end
        if var005 == 1 or scene_prop_slot_003 == 1:
            if True:
                use_item(scene_prop_instance_id_002,var001)
                max_players = get_max_players()
                for player_id_007 in range(1, max_players):
                    if player_is_active(player_id_007):
                        multiplayer_send_2_int_to_player(player_id_007,76,scene_prop_instance_id_002,var001)
                    #end
                #end
            #end
        #end
    #end
trigger0.codeBlock = code
earth_sally_gate_left.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,2000)
trigger1.codeBlock = code
earth_sally_gate_left.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var002, var003):
    play_sound(snd.dummy_destroyed)
    var001 = 86
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        set_fixed_point_multiplier(100)
        pos1 = prop_instance_get_position(var002)
        if var003 >= 0:
            pos2 = agent_get_position(var003)
            if position_is_behind_position(2,1):
                var001 *= -1
            #end
        #end
        init_position(3)
        if var001 >= 0:
            position_move_y(3,-100)
        else:
            position_move_y(3,100)
        #end
        position_move_x(3,-50)
        position_transform_position_to_parent(4,1,3)
        position_move_z(4,100)
        distance_to_ground_level_004 = position_get_distance_to_ground_level(4)
        distance_to_ground_level_004 -= 100
        var005 = distance_to_ground_level_004
        var005 /= 3
        if var001 >= 0:
            var001 += var005
        else:
            var001 -= var005
        #end
        position_rotate_x(1,var001)
        prop_instance_animate_to_position(var002,1,70)
    #end
trigger2.codeBlock = code
earth_sally_gate_left.add_trigger(trigger2)
# trigger3
trigger3 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
    #end
trigger3.codeBlock = code
earth_sally_gate_left.add_trigger(trigger3)

earth_sally_gate_right = SceneProp("earth_sally_gate_right", "earth_sally_gate_right", "bo_earth_sally_gate_right")
earth_sally_gate_right.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
earth_sally_gate_right.add_flag(ScenePropFlag.DESTRUCTIBLE)
earth_sally_gate_right.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, scene_prop_instance_id_002):
    pos1 = agent_get_position(var001)
    pos2 = prop_instance_get_starting_position(scene_prop_instance_id_002)
    scene_prop_slot_003 = scene_prop_get_slot(scene_prop_instance_id_002,1)
    if True:
        scene_prop_kind_004 = prop_instance_get_scene_prop_kind(scene_prop_instance_id_002)
        var005 = 0
        if scene_prop_kind_004 != spr.viking_keep_destroy_sally_door_right and scene_prop_kind_004 != spr.viking_keep_destroy_sally_door_left and scene_prop_kind_004 != spr.earth_sally_gate_right and scene_prop_kind_004 != spr.earth_sally_gate_left and position_is_behind_position(1,2):
            var005 = 1
        elif scene_prop_kind_004 == spr.viking_keep_destroy_sally_door_right or scene_prop_kind_004 == spr.viking_keep_destroy_sally_door_left or scene_prop_kind_004 == spr.earth_sally_gate_right or scene_prop_kind_004 == spr.earth_sally_gate_left and not position_is_behind_position(1,2):
            var005 = 1
        #end
        if var005 == 1 or scene_prop_slot_003 == 1:
            if True:
                use_item(scene_prop_instance_id_002,var001)
                max_players = get_max_players()
                for player_id_007 in range(1, max_players):
                    if player_is_active(player_id_007):
                        multiplayer_send_2_int_to_player(player_id_007,76,scene_prop_instance_id_002,var001)
                    #end
                #end
            #end
        #end
    #end
trigger0.codeBlock = code
earth_sally_gate_right.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,2000)
trigger1.codeBlock = code
earth_sally_gate_right.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var002, var003):
    play_sound(snd.dummy_destroyed)
    var001 = 86
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        set_fixed_point_multiplier(100)
        pos1 = prop_instance_get_position(var002)
        if var003 >= 0:
            pos2 = agent_get_position(var003)
            if position_is_behind_position(2,1):
                var001 *= -1
            #end
        #end
        init_position(3)
        if var001 >= 0:
            position_move_y(3,-100)
        else:
            position_move_y(3,100)
        #end
        position_move_x(3,-50)
        position_transform_position_to_parent(4,1,3)
        position_move_z(4,100)
        distance_to_ground_level_004 = position_get_distance_to_ground_level(4)
        distance_to_ground_level_004 -= 100
        var005 = distance_to_ground_level_004
        var005 /= 3
        if var001 >= 0:
            var001 += var005
        else:
            var001 -= var005
        #end
        position_rotate_x(1,var001)
        prop_instance_animate_to_position(var002,1,70)
    #end
trigger2.codeBlock = code
earth_sally_gate_right.add_trigger(trigger2)
# trigger3
trigger3 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
    #end
trigger3.codeBlock = code
earth_sally_gate_right.add_trigger(trigger3)

barrier_box = SceneProp("barrier_box", "barrier_box", "bo_barrier_box")
barrier_box.add_flag(ScenePropFlag.TYPE_BARRIER_3D)
barrier_box.add_flag(ScenePropFlag.INVISIBLE)

barrier_capsule = SceneProp("barrier_capsule", "barrier_capsule", "bo_barrier_capsule")
barrier_capsule.add_flag(ScenePropFlag.TYPE_BARRIER_3D)
barrier_capsule.add_flag(ScenePropFlag.INVISIBLE)

barrier_cone = SceneProp("barrier_cone", "barrier_cone", "bo_barrier_cone")
barrier_cone.add_flag(ScenePropFlag.TYPE_BARRIER_3D)
barrier_cone.add_flag(ScenePropFlag.INVISIBLE)

barrier_sphere = SceneProp("barrier_sphere", "barrier_sphere", "bo_barrier_sphere")
barrier_sphere.add_flag(ScenePropFlag.TYPE_BARRIER_3D)
barrier_sphere.add_flag(ScenePropFlag.INVISIBLE)

viking_keep_destroy_sally_door_right = SceneProp("viking_keep_destroy_sally_door_right", "viking_keep_destroy_sally_door_right", "bo_viking_keep_destroy_sally_door_right")
viking_keep_destroy_sally_door_right.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
viking_keep_destroy_sally_door_right.add_flag(ScenePropFlag.DESTRUCTIBLE)
viking_keep_destroy_sally_door_right.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, scene_prop_instance_id_002):
    pos1 = agent_get_position(var001)
    pos2 = prop_instance_get_starting_position(scene_prop_instance_id_002)
    scene_prop_slot_003 = scene_prop_get_slot(scene_prop_instance_id_002,1)
    if True:
        scene_prop_kind_004 = prop_instance_get_scene_prop_kind(scene_prop_instance_id_002)
        var005 = 0
        if scene_prop_kind_004 != spr.viking_keep_destroy_sally_door_right and scene_prop_kind_004 != spr.viking_keep_destroy_sally_door_left and scene_prop_kind_004 != spr.earth_sally_gate_right and scene_prop_kind_004 != spr.earth_sally_gate_left and position_is_behind_position(1,2):
            var005 = 1
        elif scene_prop_kind_004 == spr.viking_keep_destroy_sally_door_right or scene_prop_kind_004 == spr.viking_keep_destroy_sally_door_left or scene_prop_kind_004 == spr.earth_sally_gate_right or scene_prop_kind_004 == spr.earth_sally_gate_left and not position_is_behind_position(1,2):
            var005 = 1
        #end
        if var005 == 1 or scene_prop_slot_003 == 1:
            if True:
                use_item(scene_prop_instance_id_002,var001)
                max_players = get_max_players()
                for player_id_007 in range(1, max_players):
                    if player_is_active(player_id_007):
                        multiplayer_send_2_int_to_player(player_id_007,76,scene_prop_instance_id_002,var001)
                    #end
                #end
            #end
        #end
    #end
trigger0.codeBlock = code
viking_keep_destroy_sally_door_right.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,3000)
trigger1.codeBlock = code
viking_keep_destroy_sally_door_right.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var002, var003):
    play_sound(snd.dummy_destroyed)
    var001 = 86
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        set_fixed_point_multiplier(100)
        pos1 = prop_instance_get_position(var002)
        if var003 >= 0:
            pos2 = agent_get_position(var003)
            if position_is_behind_position(2,1):
                var001 *= -1
            #end
        #end
        init_position(3)
        if var001 >= 0:
            position_move_y(3,-100)
        else:
            position_move_y(3,100)
        #end
        position_move_x(3,-50)
        position_transform_position_to_parent(4,1,3)
        position_move_z(4,100)
        distance_to_ground_level_004 = position_get_distance_to_ground_level(4)
        distance_to_ground_level_004 -= 100
        var005 = distance_to_ground_level_004
        var005 /= 3
        if var001 >= 0:
            var001 += var005
        else:
            var001 -= var005
        #end
        position_rotate_x(1,var001)
        prop_instance_animate_to_position(var002,1,70)
    #end
trigger2.codeBlock = code
viking_keep_destroy_sally_door_right.add_trigger(trigger2)
# trigger3
trigger3 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
    #end
trigger3.codeBlock = code
viking_keep_destroy_sally_door_right.add_trigger(trigger3)

viking_keep_destroy_sally_door_left = SceneProp("viking_keep_destroy_sally_door_left", "viking_keep_destroy_sally_door_left", "bo_viking_keep_destroy_sally_door_left")
viking_keep_destroy_sally_door_left.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
viking_keep_destroy_sally_door_left.add_flag(ScenePropFlag.DESTRUCTIBLE)
viking_keep_destroy_sally_door_left.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, scene_prop_instance_id_002):
    pos1 = agent_get_position(var001)
    pos2 = prop_instance_get_starting_position(scene_prop_instance_id_002)
    scene_prop_slot_003 = scene_prop_get_slot(scene_prop_instance_id_002,1)
    if True:
        scene_prop_kind_004 = prop_instance_get_scene_prop_kind(scene_prop_instance_id_002)
        var005 = 0
        if scene_prop_kind_004 != spr.viking_keep_destroy_sally_door_right and scene_prop_kind_004 != spr.viking_keep_destroy_sally_door_left and scene_prop_kind_004 != spr.earth_sally_gate_right and scene_prop_kind_004 != spr.earth_sally_gate_left and position_is_behind_position(1,2):
            var005 = 1
        elif scene_prop_kind_004 == spr.viking_keep_destroy_sally_door_right or scene_prop_kind_004 == spr.viking_keep_destroy_sally_door_left or scene_prop_kind_004 == spr.earth_sally_gate_right or scene_prop_kind_004 == spr.earth_sally_gate_left and not position_is_behind_position(1,2):
            var005 = 1
        #end
        if var005 == 1 or scene_prop_slot_003 == 1:
            if True:
                use_item(scene_prop_instance_id_002,var001)
                max_players = get_max_players()
                for player_id_007 in range(1, max_players):
                    if player_is_active(player_id_007):
                        multiplayer_send_2_int_to_player(player_id_007,76,scene_prop_instance_id_002,var001)
                    #end
                #end
            #end
        #end
    #end
trigger0.codeBlock = code
viking_keep_destroy_sally_door_left.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,3000)
trigger1.codeBlock = code
viking_keep_destroy_sally_door_left.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var002, var003):
    play_sound(snd.dummy_destroyed)
    var001 = 86
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        set_fixed_point_multiplier(100)
        pos1 = prop_instance_get_position(var002)
        if var003 >= 0:
            pos2 = agent_get_position(var003)
            if position_is_behind_position(2,1):
                var001 *= -1
            #end
        #end
        init_position(3)
        if var001 >= 0:
            position_move_y(3,-100)
        else:
            position_move_y(3,100)
        #end
        position_move_x(3,-50)
        position_transform_position_to_parent(4,1,3)
        position_move_z(4,100)
        distance_to_ground_level_004 = position_get_distance_to_ground_level(4)
        distance_to_ground_level_004 -= 100
        var005 = distance_to_ground_level_004
        var005 /= 3
        if var001 >= 0:
            var001 += var005
        else:
            var001 -= var005
        #end
        position_rotate_x(1,var001)
        prop_instance_animate_to_position(var002,1,70)
    #end
trigger2.codeBlock = code
viking_keep_destroy_sally_door_left.add_trigger(trigger2)
# trigger3
trigger3 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
    #end
trigger3.codeBlock = code
viking_keep_destroy_sally_door_left.add_trigger(trigger3)

castle_f_door_b = SceneProp("castle_f_door_b", "castle_e_sally_door_a", "bo_castle_e_sally_door_a")
castle_f_door_b.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
castle_f_door_b.add_flag(ScenePropFlag.DESTRUCTIBLE)
castle_f_door_b.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code(var001, scene_prop_instance_id_002):
    pos1 = agent_get_position(var001)
    pos2 = prop_instance_get_starting_position(scene_prop_instance_id_002)
    scene_prop_slot_003 = scene_prop_get_slot(scene_prop_instance_id_002,1)
    if var001 >= 0:
        agent_team_no_004 = agent_get_team(var001)
        if agent_team_no_004 == 0 or scene_prop_slot_003 == 1:
            if True:
                use_item(scene_prop_instance_id_002,var001)
                max_players = get_max_players()
                for player_id_006 in range(1, max_players):
                    if player_is_active(player_id_006):
                        multiplayer_send_2_int_to_player(player_id_006,76,scene_prop_instance_id_002,var001)
                    #end
                #end
            #end
        #end
    #end
trigger0.codeBlock = code
castle_f_door_b.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,1000)
trigger1.codeBlock = code
castle_f_door_b.add_trigger(trigger1)
# trigger2
trigger2 = SimpleTrigger(tri.ti_on_scene_prop_destroy)
def code(var002, var003):
    play_sound(snd.dummy_destroyed)
    var001 = 86
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        set_fixed_point_multiplier(100)
        pos1 = prop_instance_get_position(var002)
        if var003 >= 0:
            pos2 = agent_get_position(var003)
            if position_is_behind_position(2,1):
                var001 *= -1
            #end
        #end
        init_position(3)
        if var001 >= 0:
            position_move_y(3,-100)
        else:
            position_move_y(3,100)
        #end
        position_move_x(3,-50)
        position_transform_position_to_parent(4,1,3)
        position_move_z(4,100)
        distance_to_ground_level_004 = position_get_distance_to_ground_level(4)
        distance_to_ground_level_004 -= 100
        var005 = distance_to_ground_level_004
        var005 /= 3
        if var001 >= 0:
            var001 += var005
        else:
            var001 -= var005
        #end
        position_rotate_x(1,var001)
        prop_instance_animate_to_position(var002,1,70)
    #end
trigger2.codeBlock = code
castle_f_door_b.add_trigger(trigger2)
# trigger3
trigger3 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
    #end
trigger3.codeBlock = code
castle_f_door_b.add_trigger(trigger3)

ctf_flag_kingdom_1 = SceneProp("ctf_flag_kingdom_1", "ctf_flag_kingdom_1", "0")
ctf_flag_kingdom_1.add_flag(ScenePropFlag.MOVEABLE)
ctf_flag_kingdom_1.add_flag(ScenePropFlag.FACE_PLAYER)

ctf_flag_kingdom_2 = SceneProp("ctf_flag_kingdom_2", "ctf_flag_kingdom_2", "0")
ctf_flag_kingdom_2.add_flag(ScenePropFlag.MOVEABLE)
ctf_flag_kingdom_2.add_flag(ScenePropFlag.FACE_PLAYER)

ctf_flag_kingdom_3 = SceneProp("ctf_flag_kingdom_3", "ctf_flag_kingdom_3", "0")
ctf_flag_kingdom_3.add_flag(ScenePropFlag.MOVEABLE)
ctf_flag_kingdom_3.add_flag(ScenePropFlag.FACE_PLAYER)

ctf_flag_kingdom_4 = SceneProp("ctf_flag_kingdom_4", "ctf_flag_kingdom_4", "0")
ctf_flag_kingdom_4.add_flag(ScenePropFlag.MOVEABLE)
ctf_flag_kingdom_4.add_flag(ScenePropFlag.FACE_PLAYER)

ctf_flag_kingdom_5 = SceneProp("ctf_flag_kingdom_5", "ctf_flag_kingdom_5", "0")
ctf_flag_kingdom_5.add_flag(ScenePropFlag.MOVEABLE)
ctf_flag_kingdom_5.add_flag(ScenePropFlag.FACE_PLAYER)

ctf_flag_kingdom_6 = SceneProp("ctf_flag_kingdom_6", "ctf_flag_kingdom_6", "0")
ctf_flag_kingdom_6.add_flag(ScenePropFlag.MOVEABLE)
ctf_flag_kingdom_6.add_flag(ScenePropFlag.FACE_PLAYER)

ctf_flag_kingdom_7 = SceneProp("ctf_flag_kingdom_7", "ctf_flag_kingdom_7", "0")
ctf_flag_kingdom_7.add_flag(ScenePropFlag.MOVEABLE)
ctf_flag_kingdom_7.add_flag(ScenePropFlag.FACE_PLAYER)

headquarters_flag_rebel = SceneProp("headquarters_flag_rebel", "flag_rebel", "0")
headquarters_flag_rebel.add_flag(ScenePropFlag.MOVEABLE)
headquarters_flag_rebel.add_flag(ScenePropFlag.FACE_PLAYER)

arabian_lighthouse_a = SceneProp("arabian_lighthouse_a", "arabian_lighthouse_a", "bo_arabian_lighthouse_a")

arabian_ramp_a = SceneProp("arabian_ramp_a", "arabian_ramp_a", "bo_arabian_ramp_a")

arabian_ramp_b = SceneProp("arabian_ramp_b", "arabian_ramp_b", "bo_arabian_ramp_b")

winery_interior = SceneProp("winery_interior", "winery_interior", "bo_winery_interior")

winery_barrel_shelf = SceneProp("winery_barrel_shelf", "winery_barrel_shelf", "bo_winery_barrel_shelf")

winery_wall_shelf = SceneProp("winery_wall_shelf", "winery_wall_shelf", "bo_winery_wall_shelf")

winery_huge_barrel = SceneProp("winery_huge_barrel", "winery_huge_barrel", "bo_winery_huge_barrel")

winery_wine_press = SceneProp("winery_wine_press", "winery_wine_press", "bo_winery_wine_press")

winery_middle_barrel = SceneProp("winery_middle_barrel", "winery_middle_barrel", "bo_winery_middle_barrel")

winery_wine_cart_small_loaded = SceneProp("winery_wine_cart_small_loaded", "winery_wine_cart_small_loaded", "bo_winery_wine_cart_small_loaded")

winery_wine_cart_small_empty = SceneProp("winery_wine_cart_small_empty", "winery_wine_cart_small_empty", "bo_winery_wine_cart_small_empty")

winery_wine_cart_empty = SceneProp("winery_wine_cart_empty", "winery_wine_cart_empty", "bo_winery_wine_cart_empty")

winery_wine_cart_loaded = SceneProp("winery_wine_cart_loaded", "winery_wine_cart_loaded", "bo_winery_wine_cart_loaded")

weavery_interior = SceneProp("weavery_interior", "weavery_interior", "bo_weavery_interior")

weavery_loom_a = SceneProp("weavery_loom_a", "weavery_loom_a", "bo_weavery_loom_a")

weavery_spinning_wheel = SceneProp("weavery_spinning_wheel", "weavery_spinning_wheel", "bo_weavery_spinning_wheel")

mill_interior = SceneProp("mill_interior", "mill_interior", "bo_mill_interior")

mill_flour_sack = SceneProp("mill_flour_sack", "mill_flour_sack", "bo_mill_flour_sack")

mill_flour_sack_desk_a = SceneProp("mill_flour_sack_desk_a", "mill_flour_sack_desk_a", "bo_mill_flour_sack_desk_a")

mill_flour_sack_desk_b = SceneProp("mill_flour_sack_desk_b", "mill_flour_sack_desk_b", "bo_mill_flour_sack_desk_b")

smithy_interior = SceneProp("smithy_interior", "smithy_interior", "bo_smithy_interior")

smithy_grindstone_wheel = SceneProp("smithy_grindstone_wheel", "smithy_grindstone_wheel", "bo_smithy_grindstone_wheel")

smithy_forge_bellows = SceneProp("smithy_forge_bellows", "smithy_forge_bellows", "bo_smithy_forge_bellows")

smithy_forge = SceneProp("smithy_forge", "smithy_forge", "bo_smithy_forge")

smithy_anvil = SceneProp("smithy_anvil", "smithy_anvil", "bo_smithy_anvil")

tannery_hide_a = SceneProp("tannery_hide_a", "tannery_hide_a", "bo_tannery_hide_a")

tannery_hide_b = SceneProp("tannery_hide_b", "tannery_hide_b", "bo_tannery_hide_b")

tannery_pools_a = SceneProp("tannery_pools_a", "tannery_pools_a", "bo_tannery_pools_a")

tannery_pools_b = SceneProp("tannery_pools_b", "tannery_pools_b", "bo_tannery_pools_b")

fountain = SceneProp("fountain", "fountain", "bo_fountain")

rhodok_houses_a = SceneProp("rhodok_houses_a", "rhodok_houses_a", "bo_rhodok_houses_a")

rhodok_houses_b = SceneProp("rhodok_houses_b", "rhodok_houses_b", "bo_rhodok_houses_b")

rhodok_houses_c = SceneProp("rhodok_houses_c", "rhodok_houses_c", "bo_rhodok_houses_c")

rhodok_houses_d = SceneProp("rhodok_houses_d", "rhodok_houses_d", "bo_rhodok_houses_d")

rhodok_houses_e = SceneProp("rhodok_houses_e", "rhodok_houses_e", "bo_rhodok_houses_e")

rhodok_house_passage_a = SceneProp("rhodok_house_passage_a", "rhodok_house_passage_a", "bo_rhodok_house_passage_a")

bridge_b = SceneProp("bridge_b", "bridge_b", "bo_bridge_b")

brewery_pool = SceneProp("brewery_pool", "brewery_pool", "bo_brewery_pool")

brewery_big_bucket = SceneProp("brewery_big_bucket", "brewery_big_bucket", "bo_brewery_big_bucket")

brewery_interior = SceneProp("brewery_interior", "brewery_interior", "bo_brewery_interior")

brewery_bucket_platform_a = SceneProp("brewery_bucket_platform_a", "brewery_bucket_platform_a", "bo_brewery_bucket_platform_a")

brewery_bucket_platform_b = SceneProp("brewery_bucket_platform_b", "brewery_bucket_platform_b", "bo_brewery_bucket_platform_b")

weavery_dye_pool_r = SceneProp("weavery_dye_pool_r", "weavery_dye_pool_r", "bo_weavery_dye_pool_r")

weavery_dye_pool_y = SceneProp("weavery_dye_pool_y", "weavery_dye_pool_y", "bo_weavery_dye_pool_y")

weavery_dye_pool_b = SceneProp("weavery_dye_pool_b", "weavery_dye_pool_b", "bo_weavery_dye_pool_b")

weavery_dye_pool_p = SceneProp("weavery_dye_pool_p", "weavery_dye_pool_p", "bo_weavery_dye_pool_p")

weavery_dye_pool_g = SceneProp("weavery_dye_pool_g", "weavery_dye_pool_g", "bo_weavery_dye_pool_g")

oil_press_interior = SceneProp("oil_press_interior", "oil_press_interior", "bo_oil_press_interior")

city_swad_01 = SceneProp("city_swad_01", "city_swad_01", "bo_city_swad_01")

city_swad_02 = SceneProp("city_swad_02", "city_swad_02", "bo_city_swad_02")

city_swad_03 = SceneProp("city_swad_03", "city_swad_03", "bo_city_swad_03")

city_swad_04 = SceneProp("city_swad_04", "city_swad_04", "bo_city_swad_04")

city_swad_passage_01 = SceneProp("city_swad_passage_01", "city_swad_passage_01", "bo_city_swad_passage_01")

city_swad_05 = SceneProp("city_swad_05", "city_swad_05", "bo_city_swad_05")

arena_block_j_a = SceneProp("arena_block_j_a", "arena_block_j_a", "bo_arena_block_j_a")

arena_underway_a = SceneProp("arena_underway_a", "arena_underway_a", "bo_arena_underway_a")

arena_circle_a = SceneProp("arena_circle_a", "arena_circle_a", "bo_arena_circle_a")

rope_bridge_15m = SceneProp("rope_bridge_15m", "rope_bridge_15m", "bo_rope_bridge_15m")

tree_house_a = SceneProp("tree_house_a", "tree_house_a", "bo_tree_house_a")

tree_house_guard_a = SceneProp("tree_house_guard_a", "tree_house_guard_a", "bo_tree_house_guard_a")

tree_house_guard_b = SceneProp("tree_house_guard_b", "tree_house_guard_b", "bo_tree_house_guard_b")

tree_shelter_a = SceneProp("tree_shelter_a", "tree_shelter_a", "bo_tree_shelter_a")

yellow_fall_leafs_a = SceneProp("yellow_fall_leafs_a", "0", "0")
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code():
    particle_system_add_new(psys.fall_leafs_a)
trigger0.codeBlock = code
yellow_fall_leafs_a.add_trigger(trigger0)

rock_bridge_a = SceneProp("rock_bridge_a", "rock_bridge_a", "bo_rock_bridge_a")

suspension_bridge_a = SceneProp("suspension_bridge_a", "suspension_bridge_a", "bo_suspension_bridge_a")

mine_a = SceneProp("mine_a", "mine_a", "bo_mine_a")

snowy_destroy_house_a = SceneProp("snowy_destroy_house_a", "snowy_destroy_house_a", "bo_snowy_destroy_house_a")

snowy_destroy_house_b = SceneProp("snowy_destroy_house_b", "snowy_destroy_house_b", "bo_snowy_destroy_house_b")

snowy_destroy_house_c = SceneProp("snowy_destroy_house_c", "snowy_destroy_house_c", "bo_snowy_destroy_house_c")

snowy_destroy_heap = SceneProp("snowy_destroy_heap", "snowy_destroy_heap", "bo_snowy_destroy_heap")

snowy_destroy_castle_a = SceneProp("snowy_destroy_castle_a", "snowy_destroy_castle_a", "bo_snowy_destroy_castle_a")

snowy_destroy_castle_b = SceneProp("snowy_destroy_castle_b", "snowy_destroy_castle_b", "bo_snowy_destroy_castle_b")

snowy_destroy_castle_c = SceneProp("snowy_destroy_castle_c", "snowy_destroy_castle_c", "bo_snowy_destroy_castle_c")

snowy_destroy_castle_d = SceneProp("snowy_destroy_castle_d", "snowy_destroy_castle_d", "bo_snowy_destroy_castle_d")

snowy_destroy_windmill = SceneProp("snowy_destroy_windmill", "snowy_destroy_windmill", "bo_snowy_destroy_windmill")

snowy_destroy_tree_a = SceneProp("snowy_destroy_tree_a", "snowy_destroy_tree_a", "bo_snowy_destroy_tree_a")

snowy_destroy_tree_b = SceneProp("snowy_destroy_tree_b", "snowy_destroy_tree_b", "bo_snowy_destroy_tree_b")

snowy_destroy_bridge_a = SceneProp("snowy_destroy_bridge_a", "snowy_destroy_bridge_a", "bo_snowy_destroy_bridge_a")

snowy_destroy_bridge_b = SceneProp("snowy_destroy_bridge_b", "snowy_destroy_bridge_b", "bo_snowy_destroy_bridge_b")

prison_cart = SceneProp("prison_cart", "prison_cart", "bo_prison_cart")
prison_cart.add_flag(ScenePropFlag.MOVEABLE)

prison_cart_door_right = SceneProp("prison_cart_door_right", "prison_cart_door_right", "bo_prison_cart_door_right")
prison_cart_door_right.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
prison_cart_door_right.add_flag(ScenePropFlag.DESTRUCTIBLE)
prison_cart_door_right.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,300)
trigger0.codeBlock = code
prison_cart_door_right.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
        set_fixed_point_multiplier(1)
    #end
trigger1.codeBlock = code
prison_cart_door_right.add_trigger(trigger1)

prison_cart_door_left = SceneProp("prison_cart_door_left", "prison_cart_door_left", "bo_prison_cart_door_left")
prison_cart_door_left.add_flag(ScenePropFlag.SHOW_HIT_POINT_BAR)
prison_cart_door_left.add_flag(ScenePropFlag.DESTRUCTIBLE)
prison_cart_door_left.add_flag(ScenePropFlag.MOVEABLE)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_init)
def code(var001):
    scene_prop_set_hit_points(var001,300)
trigger0.codeBlock = code
prison_cart_door_left.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_hit)
def code(var001, var002):
    if True:
        scp_hit_points_003 = scene_prop_get_hit_points(var001)
        scp_hit_points_003 -= var002
        if scp_hit_points_003 > 0:
            play_sound(snd.dummy_hit)
        elif not multiplayer_is_server():
            play_sound(snd.dummy_destroyed)
        #end
    #end
    if multiplayer_is_server() or not game_in_multiplayer_mode():
        particle_system_burst(psys.dummy_smoke,1,3)
        particle_system_burst(psys.dummy_straw,1,10)
        set_fixed_point_multiplier(1)
    #end
trigger1.codeBlock = code
prison_cart_door_left.add_trigger(trigger1)

multiplayer_coop_item_drop = SceneProp("multiplayer_coop_item_drop", "package", "bobaggage")
multiplayer_coop_item_drop.add_flag(ScenePropFlag.TYPE_PLAYER_LIMITER)
multiplayer_coop_item_drop.add_flag(ScenePropFlag.MOVEABLE)
multiplayer_coop_item_drop.set_use_time(1)
# trigger0
trigger0 = SimpleTrigger(tri.ti_on_scene_prop_use)
def code():
    pass
trigger0.codeBlock = code
multiplayer_coop_item_drop.add_trigger(trigger0)
# trigger1
trigger1 = SimpleTrigger(tri.ti_on_scene_prop_start_use)
def code(cur_agent, var002):
    agent_player_id_003 = agent_get_player_id(cur_agent)
    if player_is_active(agent_player_id_003):
        var004 = -1
        var005 = -1
        for cur_agent in __all_agents__:
            if agent_is_active(cur_agent) and agent_is_alive(cur_agent) and agent_is_human(cur_agent) and agent_is_non_player(cur_agent):
                agent_team_no_006 = agent_get_team(cur_agent)
                if agent_team_no_006 == 0:
                    agent_group_007 = agent_get_group(cur_agent)
                    if agent_group_007 == agent_player_id_003:
                        troop_id_008 = agent_get_troop_id(cur_agent)
                        if player_slot_eq(agent_player_id_003,43,troop_id_008) or player_slot_eq(agent_player_id_003,44,troop_id_008):
                            if var004 == -1:
                                var004 = cur_agent
                            elif var005 == -1:
                                var005 = cur_agent
                            #end
                        #end
                    #end
                #end
            #end
        #end
    #end
    var009 = 1
    slot_no_010 = -1
    for slot_no_011 in range(50, 60):
        if var009 == 1:
            player_slot_012 = player_get_slot(agent_player_id_003,slot_no_011)
            if player_slot_012 == var002:
                var009 = 0
            #end
        #end
    #end
    for slot_no_011 in range(50, 60):
        if var009 == 1:
            player_slot_012 = player_get_slot(agent_player_id_003,slot_no_011)
            if player_slot_012 == 0 and slot_no_010 == -1:
                slot_no_010 = slot_no_011
            #end
        #end
    #end
    if var009 == 1:
        coop_generate_item_drop(agent_player_id_003)
        if slot_no_010 != -1:
            player_set_slot(agent_player_id_003,slot_no_010,var002)
            multiplayer_send_2_int_to_player(agent_player_id_003,121,slot_no_010,var002)
        #end
    #end
    reg1 = var009
    if var009 == 1:
        if agent_player_id_003 != 0:
            multiplayer_send_3_int_to_player(agent_player_id_003,120,_g_ccoop_currently_dropping_item,var004,var005)
        else:
            coop_drop_item(_g_ccoop_currently_dropping_item,var004,var005)
        #end
    #end
    _g_ccoop_currently_dropping_item = -1
trigger1.codeBlock = code
multiplayer_coop_item_drop.add_trigger(trigger1)

