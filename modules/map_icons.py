# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from mapicon import MapIcon
import sounds as snd


__banner_scale__ = 0.3
__avatar_scale__ = 0.15


player = MapIcon("player", mesh_name="player", scale=__avatar_scale__, sound=snd.footstep_grass)
town = MapIcon("town", mesh_name="map_town_a", no_shadow=True, scale=0.35)
village = MapIcon("village", mesh_name="map_village_a", no_shadow=True, scale=0.45)

