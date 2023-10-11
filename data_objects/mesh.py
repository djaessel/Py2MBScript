# This Python file uses the following encoding: utf-8

class Mesh:
    def __init__(self, id, resource_name, render_order_plus_1=False):
        self.id = id
        self.render_order_plus_1 = render_order_plus_1
        self.resource_name = resource_name
        self.scale_x = 1
        self.scale_y = 1
        self.scale_z = 1
        self.rotation_x = 0
        self.rotation_y = 0
        self.rotation_z = 0
        self.translation_x = 0
        self.translation_y = 0
        self.translation_z = 0


    def set_axis_translation(self, x : float, y : float, z : float):
        self.translation_x = x
        self.translation_y = y
        self.translation_z = z


    def set_rotation(self, x : float, y : float, z : float):
        self.rotation_x = x
        self.rotation_y = y
        self.rotation_z = z


    def set_scale(self, x : float, y : float, z : float):
        self.scale_x = x
        self.scale_y = y
        self.scale_z = z


    def set_scale_whole(self, x : float):
        self.set_scale(x, x, x)

