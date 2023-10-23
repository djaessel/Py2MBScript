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
        with open("./test_cases/test_party_templates_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("parties = [\n\n")

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
                    f.write("(" + stack[0] + "," + str(stack[1]) + "," + str(stack[2]) + ",")
                    if stack[3]:
                        f.write("pmf_is_prisoner")
                    else:
                        f.write("0")
                    f.write("),")
                f.write("]),\n")

            f.write("\n] # PARTY TEMPLATES END\n")

