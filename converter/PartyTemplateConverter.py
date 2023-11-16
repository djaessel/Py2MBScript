# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from party_template import PartyTemplate


import test_party_templates


class PartyTemplateConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrievePartyTemplates(self):
        parties = []
        for i in vars(test_party_templates):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_party_templates,i)
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
            f.write("from ID_map_icons import *\n\n")

            f.write("no_menu = 0\n")
            f.write("pmf_is_prisoner = 0x0001\n\n")

            f.write("party_templates = [\n\n")

            for partyTemp in codeData:
                f.write("(\"" + partyTemp.id + "\", \"" + partyTemp.name + "\", ")

                if len(partyTemp.flags) > 0:
                    pass
                    # TODO: write flags
                else:
                    f.write("0, ")

                f.write(partyTemp.menu + ", ")
                f.write(partyTemp.faction + ", ")
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

