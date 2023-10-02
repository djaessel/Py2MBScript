# This Python file uses the following encoding: utf-8



from ScriptConverter import ScriptConverter
from troop import Troop

import inspect
import test_troops


class TroopConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveTroops(self):
        items = []
        for i in vars(test_troops):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_troops,i)
                if not "<function" in str(attr) and not "<module" in str(attr):
                    items.append(attr)
        return items

    def writeScriptOutputFile(self, codeData : dict[Troop]):
        with open("./test_cases/test_troops_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("troops = [\n\n")

            for troop in codeData:
                f.write("[\"" + troop.id + "\",\"" + troop.name + "\",\"" + troop.plural_name + "\",\n")

                if len(troop.flags) > 0:
                    f.write("|".join(troop.flags))
                else:
                    f.write("0")
                f.write(",\n")

                f.write(troop.scene + "," + troop.reserved + "," + troop.faction + ",\n")

                f.write("[")
                if len(troop.inventory) > 0:
                    for i, item in enumerate(troop.inventory):
                        f.write(str(item))
                        if i == len(troop.inventory) - 1:
                            f.write(",")
                f.write("],\n")

                f.write(troop.get_attributes() + ",")
                f.write(troop.get_weapon_proficies() + ",\n")

                if len(troop.skills) > 0:
                    f.write("|".join(troop.skills))
                else:
                    f.write("0")
                f.write(",\n")

                f.write(troop.face1 + ",")
                f.write(troop.face2)

                if len(troop.image) > 0:
                    f.write("," + troop.image)

                f.write("],\n\n")

            f.write("] # TROOPS END\n")
