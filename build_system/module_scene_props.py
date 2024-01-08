# -*- coding: cp1252 -*-
from header_common import *
from header_scene_props import *
from header_operations import *
from header_triggers import *
from header_sounds import *
from module_constants import *
import string

scene_props = [

("invalid_object", 0, "question_mark", "0", []),
("inventory", sokf_type_container|sokf_place_at_origin, "package", "bobaggage", []),
("empty", 0, "0", "0", []),
("chest_a", sokf_type_container, "chest_gothic", "bochest_gothic", []),
("container_small_chest", sokf_type_container, "package", "bobaggage", []),
("container_chest_b", sokf_type_container, "chest_b", "bo_chest_b", []),
("container_chest_c", sokf_type_container, "chest_c", "bo_chest_c", []),
("player_chest", sokf_type_container, "player_chest", "bo_player_chest", []),
("locked_player_chest", 0, "player_chest", "bo_player_chest", []),
("light_sun", sokf_invisible, "light_sphere", "0", [
(ti_on_scene_prop_init, [
(try_begin),
    (neg|is_currently_night),
    (store_trigger_param_1,":prop_instance_no"),
    (set_fixed_point_multiplier, 100),
    (prop_instance_get_scale, pos5, ":prop_instance_no"),
    (position_get_scale_x,":scale",pos5),
    (store_time_of_day,reg12),
    (try_begin),
        (is_between,reg12,5,20),
        (store_mul, ":red", 1000, ":scale"),
        (store_mul, ":green", 965, ":scale"),
        (store_mul, ":blue", 900, ":scale"),
    (else_try),
        (store_mul, ":red", 450, ":scale"),
        (store_mul, ":green", 575, ":scale"),
        (store_mul, ":blue", 750, ":scale"),
    (try_end),
    (val_div, ":red", 100),
    (val_div, ":green", 100),
    (val_div, ":blue", 100),
    (set_current_color,":red",":red",":red"),
    (set_position_delta,0,0,0),
    (add_point_light_to_entity,0,0),
(try_end),
]),

]),

] # SCENE PROPS END
