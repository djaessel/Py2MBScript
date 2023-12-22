# This Python file uses the following encoding: utf-8

from simple_trigger import SimpleTrigger


class MapIcon:
    def __init__(self, id : str, mesh_name : str, no_shadow : bool = False, scale : float = 0.15, sound = None, offset_x : float = 0, offset_y : float = 0, offset_z : float = 0):
        self.id = id
        self.no_shadow = no_shadow
        self.mesh_name = mesh_name
        self.scale = scale
        self.sound = sound
        self.triggers = []
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.offset_z = offset_z


    def add_trigger(self, trigger : SimpleTrigger):
        if not trigger in self.triggers:
            self.triggers.append(trigger)

