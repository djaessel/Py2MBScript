# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from scene import Scene

import test_scenes

class SceneConverter(ScriptConverter):
    def __init__(self):
        pass

    def createCode(self):
        scenes = self.retrieveScenes()
        self.writeScriptOutputFile(scenes)

    def retrieveScenes(self):
        scenes = []
        for i in vars(test_scenes):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_scenes,i)
                scenes.append(attr)
        return scenes

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
                    f.write("\"" + scenex + "\"")
                    if i < len(scene.accessible_scenes) - 1:
                        f.write(",")
                f.write("], ")

                f.write("[")
                for i, ct in enumerate(scene.chest_troops):
                    f.write("\"" + ct + "\"")
                    if i < len(scene.chest_troops) - 1:
                        f.write(",")
                f.write("]")

                if len(scene.extra_terrain) > 0:
                    f.write(", \"" + scene.extra_terrain + "\"")

                f.write("),\n")

            f.write("\n] # SCENES END\n")
