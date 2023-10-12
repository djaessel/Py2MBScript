# This Python file uses the following encoding: utf-8

from enum import Enum


class SceneFlag(Enum):
    IS_INDOORS = "sf_indoors"           # = 0x00000001   #The scene shouldn't have a skybox and lighting by sun.
    FORCE_SKYBOX = "sf_force_skybox"      # = 0x00000002   #Force adding a skybox even if indoors flag is set.
    GENERATE = "sf_generate"          # = 0x00000100   #Generate terrain by terran-generator
    RANDOMIZE = "sf_randomize"         # = 0x00000200   #Randomize terrain generator key
    AUTO_ENTRY_POINTS = "sf_auto_entry_points" # = 0x00000400   #Automatically create entry points
    NO_HORSES = "sf_no_horses"         # = 0x00000800   #Horses are not avaible
    MUDDY_WATER = "sf_muddy_water"       # = 0x00001000   #Changes the shader of the river mesh



class Scene:
    #  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
    #  2) Scene flags {int}. See header_scenes.py for a list of available flags
    #  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
    #  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
    #  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
    #  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
    #  7) Water-level {float}.
    #  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
    #  9) List of other scenes accessible from this scene {list of strings}.
    #     (deprecated. This will probably be removed in future versions of the module system)
    #     (In the new system passages are used to travel between scenes and
    #     the passage's variation-no is used to select the game menu item that the passage leads to.)
    # 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
    #     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
    # 11) EXTRA TERRAIN ?

    def __init__(self, id : str, mesh_name : str = "none", body_name : str = "none", water_level : float = -100, terrain_code : str = "0", extra_terrain : str = ""):
        self.id = id
        self.flags = []
        self.mesh_name = mesh_name
        self.body_name = body_name
        self.water_level = water_level
        self.terrain_code = terrain_code
        self.min_pos = (0,0)
        self.max_pos = (100,100)
        self.accessible_scenes = []
        self.chest_troops = []
        self.extra_terrain = extra_terrain


    def set_min_pos(self, x : float, y : float):
        self.min_pos = (x, y)


    def set_max_pos(self, x : float, y : float):
        self.max_pos = (x, y)


    def add_accessible_scene(self, scene : str):
        self.accessible_scenes.append(scene)


    def add_chest_troop(self, chest_troop : str):
        self.chest_troops.append(chest_troop)


    def add_flag(self, flag : SceneFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : SceneFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : SceneFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]

