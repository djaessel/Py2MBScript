# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from scene import Scene
from troop import Troop

import scenes

class SceneConverter(ScriptConverter):
    def __init__(self):
        pass

    def createCode(self):
        scenesx = self.retrieveScenes()
        self.writeScriptOutputFile(scenesx)

    def retrieveScenes(self):
        scenesx = []
        for i in vars(scenes):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(scenes,i)
                if not "<function" in str(attr) and not "<module" in str(attr):
                    scenesx.append(attr)
        return scenesx

    def writeScriptOutputFile(self, codeData : list[Scene]):
        with open("./build_system/module_scenes.py", "w") as f:
            f.write("from header_common import *\n")
            f.write("from header_operations import *\n")
            f.write("from header_triggers import *\n")
            f.write("from header_scenes import *\n")
            f.write("from module_constants import *\n\n")

            f.write("scenes = [\n\n")

            for scene in codeData:
                f.write("(\"" + scene.id + "\", ")

                if len(scene.flags) > 0:
                    f.write("|".join(scene.flags) + ", ")
                else:
                    f.write("0, ")

                f.write("\"" + scene.mesh_name + "\", ")
                f.write("\"" + scene.body_name + "\", ")

                f.write("(" + str(scene.min_pos[0]) + ", " + str(scene.min_pos[1]) + "), ")
                f.write("(" + str(scene.max_pos[0]) + ", " + str(scene.max_pos[1]) + "), ")

                f.write(str(scene.water_level) + ", ")
                f.write("\"" + scene.terrain_code + "\", ")

                f.write("[")
                for i, scenex in enumerate(scene.accessible_scenes):
                    ctx = scenex
                    if isinstance(scenex, Scene):
                        ctx = ct.id
                    f.write("\"" + ctx.strip('"') + "\"")
                    if i < len(scene.accessible_scenes) - 1:
                        f.write(",")
                f.write("], ")

                f.write("[")
                for i, ct in enumerate(scene.chest_troops):
                    ctx = ct
                    if isinstance(ct, Troop):
                        ctx = ct.id
                    f.write("\"" + ctx.strip('"') + "\"")
                    if i < len(scene.chest_troops) - 1:
                        f.write(",")
                f.write("]")

                if len(scene.extra_terrain) > 0:
                    f.write(", \"" + scene.extra_terrain + "\"")

                f.write("),\n")

            f.write("\n] # SCENES END\n")
