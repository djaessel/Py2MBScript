# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from faction import Faction

import test_factions

class FactionConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveFactions(self):
        factions = []
        for i in vars(test_factions):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_factions,i)
                factions.append(attr)
        return factions

    def writeScriptOutputFile(self, codeData : list[Faction]):
        with open("./build_system/module_factions.py", "w") as f:
            f.write("from header_factions import *\n\n")
            f.write("factions = [\n\n")

            for faction in codeData:
                f.write("(\"" + faction.id + "\", \"" + faction.name + "\", ")

                if faction.always_hide_label and faction.max_player_rating != 100:
                    f.write("ff_always_hide_label|max_player_rating(" + str(faction.max_player_rating) + ")")
                elif faction.always_hide_label:
                    f.write("ff_always_hide_label")
                elif faction.max_player_rating != 100:
                    f.write("max_player_rating(" + str(faction.max_player_rating) + ")")
                else:
                    f.write("0")
                f.write(", ")

                f.write(str(faction.coherence) + ", ")

                f.write("[")
                for i, relation in enumerate(faction.relations):
                    f.write("(\"" + relation[0].id + "\"," + str(relation[1]) + ")")
                    if i < len(faction.relations) - 1:
                        f.write(",")
                f.write("], ")

                f.write("[")
                for i, rank in enumerate(faction.ranks):
                    f.write("(" + rank + ")")
                    if i < len(faction.relations) - 1:
                        f.write(",")
                f.write("]")

                if faction.color != 0xaaaaaa:
                    f.write(", " + str(faction.color))

                f.write("),\n")

            f.write("\n] # FACTIONS END\n")
