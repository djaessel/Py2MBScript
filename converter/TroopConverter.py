# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from troop import Troop

import test_troops


class TroopConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveTroops(self):
        troops = []
        for i in vars(test_troops):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_troops,i)
                sx = str(attr)
                if not "<function" in sx and not "<module" in sx and not "Skill" in sx and not "MB" in sx and not "Item" in sx:
                    if not "SimpleTrigger" in sx:
                        troops.append(attr)
        return troops

    def writeScriptOutputFile(self, codeData : list[Troop]):
        with open("./build_system/module_troops.py", "w") as f:
            f.write("from __future__ import division\n")
            f.write("from past.utils import old_div\n")
            f.write("import random\n\n")

            f.write("from header_common import *\n")
            f.write("from header_items import *\n")
            f.write("from header_troops import *\n")
            f.write("from header_skills import *\n")
            f.write("from ID_factions import *\n")
            f.write("from ID_items import *\n")
            f.write("from ID_scenes import *\n\n")

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
                        f.write("(itm_" + item[0]+ ", " + str(item[1]) + ")")
                        if i == len(troop.inventory) - 1:
                            f.write(",")
                f.write("],\n")

                f.write(troop.get_attributes() + ",")
                f.write(troop.get_weapon_proficies() + ",\n")

                if len(troop.skills) > 0:
                    f.write(("|".join(troop.skills)).replace("knowns_riding_1|knowns_trade_2|knowns_inventory_management_2|knowns_prisoner_management_1|knowns_leadership_1", "knows_common"))
                else:
                    f.write("0")
                f.write(",\n")

                f.write(troop.face1 + ",")
                f.write(troop.face2)

                if len(troop.image) > 0:
                    f.write("," + troop.image)

                f.write("],\n\n")

            f.write("] # TROOPS END\n")
