# This Python file uses the following encoding: utf-8


class TableauMaterial:
    def __init__(self, id : str, sample_material_name : str, width : int, height : int, mesh_min_x : int = 0, mesh_min_y : int = 0, mesh_max_x : int = 0, mesh_max_y : int = 0):
        self.id = id
        self.flags = []
        self.sample_material_name = sample_material_name
        self.width = width
        self.height = height
        self.mesh_min_x = mesh_min_x
        self.mesh_min_y = mesh_min_y
        self.mesh_max_x = mesh_max_x
        self.mesh_max_y = mesh_max_y


    def codeBlock(self, param):
        pass
