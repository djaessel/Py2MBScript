# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from party_template import PartyTemplate
from mapicon import MapIcon


import party_templates


class PartyTemplateConverter(ScriptConverter):
    def __init__(self):
        pass

    def createCode(self):
        partyTemps = self.retrievePartyTemplates()
        self.writeScriptOutputFile(partyTemps)

    def retrievePartyTemplates(self):
        parties = []
        for i in vars(party_templates):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(party_templates,i)
                sx = str(attr)
                if not "<function" in sx and not "<module" in sx and not "Troop" in sx:
                    parties.append(attr)
        return parties

    def writeScriptOutputFile(self, codeData : list[PartyTemplate]):
        with open("./build_system/module_party_templates.py", "w") as f:
            f.write("from header_common import *\n")
            f.write("from header_parties import *\n")
            f.write("from ID_troops import *\n")
            f.write("from ID_factions import *\n")
            f.write("from ID_menus import *\n")
            f.write("from ID_map_icons import *\n\n")

            f.write("no_menu = 0\n")
            f.write("pmf_is_prisoner = 0x0001\n\n")

            f.write("party_templates = [\n\n")

            for partyTemp in codeData:
                f.write("(\"" + partyTemp.id + "\", \"" + partyTemp.name + "\", ")

                if partyTemp.icon != None and isinstance(partyTemp.icon, MapIcon):
                    f.write("icon_" + partyTemp.icon.id + "|")

                if len(partyTemp.flags) > 0:
                    f.write("|".join(partyTemp.flags) + ", ")
                else:
                    f.write("0, ")

                if partyTemp.menu == None:
                    f.write("no_menu, ")
                else:
                    f.write("menu_" + partyTemp.menu.id + ", ")
                f.write("fac_" + partyTemp.faction.id + ", ")
                f.write(partyTemp.personality + ", ")

                f.write("[")
                for stack in partyTemp.stacks:
                    f.write("(trp_" + stack[0] + "," + str(stack[1]) + "," + str(stack[2]) + ",")
                    if stack[3]:
                        f.write("pmf_is_prisoner")
                    else:
                        f.write("0")
                    f.write("),")
                f.write("]),\n")

            f.write("\n] # PARTY TEMPLATES END\n")

