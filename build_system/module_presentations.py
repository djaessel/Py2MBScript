from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

presentations = [

("game_custom_battle_designer",prsntf_manual_end_only,mesh_cb_ui_main,[

(ti_on_presentation_load, [
(set_fixed_point_multiplier, 1000),
(create_text_overlay, reg0, "@Press ESC to exit", tf_single_line),
(overlay_set_color, reg0, 0xFF000000),
(position_set_x, pos1, 2500),
(position_set_y, pos1, 2500),
(overlay_set_size, reg0, pos1),
(position_set_x, pos1, 100),
(position_set_y, pos1, 100),
(overlay_set_position, reg0, pos1),
(presentation_set_duration, 999999),
]),

(ti_on_presentation_mouse_enter_leave, [
]),

(ti_on_presentation_mouse_press, [
]),

(ti_on_presentation_run, [
(try_begin),
    (key_clicked, 0x01),
    (presentation_set_duration, 0),
(try_end),
]),

]),

] # PRESENTATIONS END
