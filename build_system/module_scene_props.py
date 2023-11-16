# -*- coding: cp1252 -*-
from header_common import *
from header_scene_props import *
from header_operations import *
from header_triggers import *
from header_sounds import *
from module_constants import *
import string

scene_props = [

("my_first", spr_use_time(20)|spr_hit_points(1)|0, "my_first", "bo_my_first", [
(ti_tab_pressed, [
(display_message, "@{reg1}"),
]),

]),

] # SCENE PROPS END
