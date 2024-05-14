# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from TriggerConverter import TriggerConverter
from scene_prop import SceneProp

import inspect
import scene_props

class ScenePropConverter(ScriptConverter):

    def createCode(self):
        ScriptConverter.is_trigger_code = True
        sceneProps = self.retrieveSceneProps()
        self.writeScriptOutputFile(sceneProps)

    def retrieveSceneProps(self):
        sceneProps = []
        for i in vars(scene_props):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(scene_props,i)
                if not "<function" in str(attr) and not "<module" in str(attr) and not "SimpleTrigger" in str(attr):
                    sceneProps.append(attr)
        return sceneProps

    def writeScriptOutputFile(self, codeData : list[SceneProp]):
        with open("./build_system/module_scene_props.py", "w") as f:
            f.write("# -*- coding: cp1252 -*-\n")
            f.write("from header_common import *\n")
            f.write("from header_scene_props import *\n")
            f.write("from header_operations import *\n")
            f.write("from header_triggers import *\n")
            f.write("from header_sounds import *\n")
            f.write("from module_constants import *\n")
            f.write("import string\n\n")

            f.write("scene_props = [\n\n")

            for sceneProp in codeData:
                f.write("(\"" + sceneProp.id + "\", ")

                if sceneProp.use_time > 0:
                    f.write("spr_use_time(" + str(sceneProp.use_time) + ")|")
                if sceneProp.hit_points > 0:
                    f.write("spr_hit_points(" + str(sceneProp.hit_points) + ")|")
                if len(sceneProp.flags) > 0:
                    f.write("|".join(sceneProp.flags) + ", ")
                else:
                    f.write("0, ")

                f.write("\"" + sceneProp.mesh_name + "\", \"" + sceneProp.physics_object_name + "\"")

                if len(sceneProp.triggers) > 0:
                    f.write(", [\n")
                    for trigger in sceneProp.triggers:
                        f.write("(" + TriggerConverter.retrieveCorrectTrigger(trigger.triggerInterval) + ", [\n")
                        codeLines = inspect.getsourcelines(trigger.codeBlock)[0]
                        for i in range(len(codeLines)):
                            codeLines[i] = codeLines[i][4:]
                        x = self.transformScriptLine(codeLines[0])
                        x.pop(0)
                        codeLines.pop(0)
                        codeLines = self.transformScriptBlock(codeLines)
                        if len(x) > 0:
                            y = []
                            y.extend(x)
                            y.extend(codeLines)
                            codeLines = y
                        self.writeScriptCode(f, codeLines)

                    f.write("]")
                else:
                    f.write(", []")
                f.write("),\n")

            f.write("\n] # SCENE PROPS END\n")

