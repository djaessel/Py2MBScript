# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter

from MBParty import MBParty

import inspect
import test_parties


class PartyConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveParties(self):
        parties = []
        for i in vars(test_parties):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_parties,i)
                sx = str(attr)
                if not "<function" in sx and not "<module" in sx:
                    parties.append(attr)
        return parties

    def writeScriptOutputFile(self, codeData : dict[MBParty]):
        with open("./test_cases/test_parties_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("parties = [\n\n")

            for party in codeData:
                f.write("(\"" + party.id + "\", \"" + party.name + "\", ")

                if len(party.flags) > 0:
                    pass
                    # TODO: write flags
                else:
                    f.write("0, ")

                f.write(party.menu + ", ")
                f.write(party.template_id + ", ")
                f.write(party.faction + ", ")

                f.write(party.personality + ", ")
                f.write(party.ai_bhvr + ", ")
                f.write(party.target_party + ", ")

                f.write("(" + str(party.initial_cords[0]) + "," + str(party.initial_cords[1]) + "), ")

                if len(party.members) > 0 or len(party.prisoners) > 0 or len(party.companions) > 0:
                    f.write("[")
                    for companion in party.companions:
                        f.write("(" + companion[0] + "," + str(companion[1]) + ",0),")
                    for member in party.members:
                        f.write("(" + member[0] + "," + str(member[1]) + ",0),")
                    for prisoner in party.prisoners:
                        f.write("(" + prisoner[0] + "," + str(prisoner[1]) + ",pmf_is_prisoner),")
                    f.write("]")
                else:
                    f.write("[]")

                if party.direction > 0.0:
                    f.write(", " + str(party.direction))

                f.write("),\n")

            f.write("\n] # PARTIES END\n")

