# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from TriggerConverter import TriggerConverter
from item import Item

import inspect
import test_items


class ItemConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveItems(self):
        items = []
        for i in vars(test_items):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_items,i)
                if not "<function" in str(attr) and not "<module" in str(attr) and not "ItemMesh" in str(attr) and not "SimpleTrigger" in str(attr):
                    items.append(attr)
        return items

    def writeScriptOutputFile(self, codeData : dict[Item]):
        with open("./build_system/module_items.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("items = [\n\n")

            for item in codeData:
                f.write("[\"" + item.id + "\",\"" + item.name + "\",[")

                for i, mesh in enumerate(item.meshes):
                    f.write("(\"" + mesh.id + "\"," + mesh.modifier + ")")
                    if i < len(item.meshes) - 1:
                        f.write(",")
                f.write("],\n")

                for i, flag in enumerate(item.flags):
                    f.write(flag)
                    if i < len(item.flags) - 1:
                        f.write("|")
                if len(item.flags) == 0:
                    f.write("0")
                f.write(",\n")

                for i, cap in enumerate(item.capabilities):
                    f.write(cap)
                    if i < len(item.capabilities) - 1:
                        f.write("|")
                if len(item.capabilities) == 0:
                    f.write("0")
                f.write(",\n")

                f.write(str(item.price) + ",\n")


                #if len(item.stats) == 0:
                #    f.write("0")
                f.write(item.get_stats_string())
                f.write(",\n")

                for i, modifier in enumerate(item.modifiers):
                    f.write(modifier)
                    if i < len(item.modifiers) - 1:
                        f.write("|")
                if len(item.modifiers) == 0:
                    f.write("imodbits_none")

                if len(item.factions) > 0 or len(item.triggers) > 0:
                    f.write(",\n[")

                    if len(item.triggers) > 0:
                        f.write("\n")
                        for trigger in item.triggers:
                            f.write("(" + TriggerConverter.retrieveCorrectTrigger(trigger.triggerInterval) + ", [\n")
                            codeLines = inspect.getsourcelines(trigger.codeBlock)[0]
                            for i in range(len(codeLines)):
                                codeLines[i] = codeLines[i][4:]
                            codeLines.pop(0)
                            codeLines = self.transformScriptBlock(codeLines)
                            self.writeScriptCode(f, codeLines)

                    f.write("]")
                    if len(item.factions) > 0:
                        f.write(",\n[")

                        for i, faction in enumerate(item.factions):
                            f.write("\"" + faction + "\"")
                            if i < len(item.factions) - 1:
                                f.write(",")

                        f.write("]")

                f.write("],\n")

            f.write("\n] # ITEMS END\n")
