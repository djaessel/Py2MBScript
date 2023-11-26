# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from TriggerConverter import TriggerConverter
from item import Item

import inspect
import test_items


class ItemConverter(ScriptConverter):

    def retrieveItems(self):
        items = []
        for i in vars(test_items):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_items,i)
                if not "<function" in str(attr) and not "<module" in str(attr) and not "ItemMesh" in str(attr) and not "SimpleTrigger" in str(attr):
                    items.append(attr)
        return items

    def writeScriptOutputFile(self, codeData : list[Item]):
        with open("./build_system/module_items.py", "w") as f:
            f.write("from module_constants import *\n")
            f.write("from ID_factions import *\n")
            f.write("from header_items import  *\n")
            f.write("from header_operations import *\n")
            f.write("from header_triggers import *\n\n")

            f.write("imodbits_none = 0\n")
            f.write("imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn\n")
            f.write("imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened\n")
            f.write("imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly\n")
            f.write("imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly\n")
            f.write("imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced\n")
            f.write("imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced\n")
            f.write("imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered\n")
            f.write("imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork\n")
            f.write("imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy\n")
            f.write("imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy\n")
            f.write("imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy\n")
            f.write("imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork\n")
            f.write("imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork\n")
            f.write("imodbits_missile   = imodbit_bent | imodbit_large_bag\n")
            f.write("imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag\n")
            f.write("imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag\n")

            f.write("imodbits_horse_good = imodbit_spirited|imodbit_heavy\n")
            f.write("imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced\n")
            f.write("imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent\n")


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
