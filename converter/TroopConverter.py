# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from troop import Troop

import troops


class TroopConverter(ScriptConverter):
    def __init__(self):
        pass

    def createCode(self):
        troopsx = self.retrieveTroops()
        self.writeScriptOutputFile(troopsx)

    def retrieveTroops(self):
        troopsx = []
        for i in vars(troops):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(troops,i)
                sx = str(attr)
                if not "<function" in sx and not "<module" in sx and not "Skill" in sx and not "MB" in sx and not "Item" in sx:
                    if not "SimpleTrigger" in sx:
                        troopsx.append(attr)
        return troopsx

    def writeScriptOutputFile(self, codeData : list[Troop]):
        with open("./build_system/module_troops.py", "w") as f:
            f.write("from __future__ import division\n")
            f.write("from past.utils import old_div\n")
            f.write("import random\n\n")

            f.write("from header_common import *\n")
            f.write("from header_items import *\n")
            f.write("from header_troops import *\n")
            f.write("from header_skills import *\n")
            f.write("from module_items import *\n")
            f.write("from ID_factions import *\n")
            f.write("from ID_items import *\n")
            f.write("from ID_scenes import *\n\n")

            f.write("def wp(x):\n")
            f.write("  n = 0\n")
            f.write("  r = 10 + int(old_div(x, 10))\n")
            f.write("  n |= wp_one_handed(x)\n")
            f.write("  n |= wp_two_handed(x)\n")
            f.write("  n |= wp_polearm(x)\n")
            f.write("  n |= wp_archery(x)\n")
            f.write("  n |= wp_crossbow(x)\n")
            f.write("  n |= wp_throwing(x)\n")
            f.write("  return n\n")
            f.write("\n")
            f.write("def wpe(m,a,c,t):\n")
            f.write("   n = 0\n")
            f.write("   n |= wp_one_handed(m)\n")
            f.write("   n |= wp_two_handed(m)\n")
            f.write("   n |= wp_polearm(m)\n")
            f.write("   n |= wp_archery(a)\n")
            f.write("   n |= wp_crossbow(c)\n")
            f.write("   n |= wp_throwing(t)\n")
            f.write("   return n\n")
            f.write("\n")
            f.write("def wpex(o,w,p,a,c,t):\n")
            f.write("   n = 0\n")
            f.write("   n |= wp_one_handed(o)\n")
            f.write("   n |= wp_two_handed(w)\n")
            f.write("   n |= wp_polearm(p)\n")
            f.write("   n |= wp_archery(a)\n")
            f.write("   n |= wp_crossbow(c)\n")
            f.write("   n |= wp_throwing(t)\n")
            f.write("   return n\n")
            f.write("\n")
            f.write("def wp_melee(x):\n")
            f.write("  n = 0\n")
            f.write("  r = 10 + int(old_div(x, 10))\n")
            f.write("  n |= wp_one_handed(x + 20)\n")
            f.write("  n |= wp_two_handed(x)\n")
            f.write("  n |= wp_polearm(x + 10)\n")
            f.write("  return n\n")
            f.write("\n")

            f.write("knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1\n")
            f.write("knows_common_multiplayer = knows_trade_10|knows_inventory_management_10|knows_prisoner_management_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10\n")
            f.write("def_attrib = str_7 | agi_5 | int_4 | cha_4\n")
            f.write("def_attrib_multiplayer = int_30 | cha_30\n\n")

            f.write("tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged\n")
            f.write("tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield\n\n")

            f.write("reserved = 0\n")
            f.write("no_scene = 0\n\n")

            f.write("man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000\n\n")

            f.write("troops = [\n\n")

            for troop in codeData:
                f.write("[\"" + troop.id + "\",\"" + troop.name + "\",\"" + troop.plural_name + "\",\n")

                if len(troop.flags) > 0:
                    f.write("|".join(troop.flags))
                else:
                    f.write("0")
                f.write(",\n")

                f.write(troop.scene + "," + troop.reserved + ",fac_" + troop.faction.id + ",\n")

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
                    f.write(("|".join(troop.skills)).replace("knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1", "knows_common"))
                else:
                    f.write("0")
                f.write(",\n")

                f.write(troop.face1)
                if len(troop.face2) > 0:
                    f.write("," + troop.face2)

                if len(troop.image) > 0:
                    f.write("," + troop.image)

                f.write("],\n\n")

            f.write("] # TROOPS END\n")
