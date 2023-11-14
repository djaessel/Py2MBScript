# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from TriggerConverter import TriggerConverter
from mapicon import MapIcon

import inspect
import test_map_icons

class MapIconConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveMapIcons(self):
        mapIcons = []
        for i in vars(test_map_icons):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_map_icons,i)
                if not "<function" in str(attr) and not "<module" in str(attr) and not "SimpleTrigger" in str(attr):
                    mapIcons.append(attr)
        return mapIcons

    def writeScriptOutputFile(self, codeData : dict[MapIcon]):
        with open("./build_system/module_map_icons.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("map_icons = [\n\n")

            for mapIcon in codeData:
                f.write("(\"" + mapIcon.id + "\", ")

                if mapIcon.no_shadow:
                    f.write("\"mcn_no_shadow\", ")
                else:
                    f.write("0, ")

                f.write("\"" + mapIcon.mesh_name + "\", ")
                f.write(str(mapIcon.scale) + ", ")

                if mapIcon.sound != None:
                    f.write("snd_" + mapIcon.sound.id + "")
                else:
                    f.write("0")

                if len(mapIcon.triggers) > 0:
                    f.write(", [\n")
                    for trigger in mapIcon.triggers:
                        f.write("(" + TriggerConverter.retrieveCorrectTrigger(trigger.triggerInterval) + ", [\n")
                        codeLines = inspect.getsourcelines(trigger.codeBlock)[0]
                        for i in range(len(codeLines)):
                            codeLines[i] = codeLines[i][4:]
                        codeLines.pop(0)
                        codeLines = self.transformScriptBlock(codeLines)
                        self.writeScriptCode(f, codeLines)
                    f.write("]")
                elif mapIcon.offset_x != 0.0 or mapIcon.offset_y != 0.0 or mapIcon.offset_z != 0.0:
                    f.write(", " + str(mapIcon.offset_x) + ", " + str(mapIcon.offset_x) + ", " + str(mapIcon.offset_x))

                f.write("),\n")

            f.write("] # MAP ICONS END\n")


