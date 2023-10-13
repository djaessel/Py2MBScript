# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from mapicon import MapIcon
import test_sounds as snd


__banner_scale__ = 0.3
__avatar_scale__ = 0.15


mapicon1 = MapIcon("player", mesh_name="player", scale=0.15, sound=snd.sound1)

