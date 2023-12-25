# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter

from MBParty import MBParty
from mapicon import MapIcon

import test_parties


class PartyConverter(ScriptConverter):
    def __init__(self):
        pass

    def createCode(self):
        parties = self.retrieveParties()
        self.writeScriptOutputFile(parties)

    def retrieveParties(self):
        parties = []
        for i in vars(test_parties):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_parties,i)
                sx = str(attr)
                if not "<function" in sx and not "<module" in sx:
                    parties.append(attr)
        return parties

    def writeScriptOutputFile(self, codeData : list[MBParty]):
        with open("./build_system/module_parties.py", "w") as f:
            f.write("from header_common import *\n")
            f.write("from header_parties import *\n")
            f.write("from ID_troops import *\n")
            f.write("from ID_factions import *\n")
            f.write("from ID_party_templates import *\n")
            f.write("from ID_map_icons import *\n\n")

            f.write("no_menu = 0\n")
            f.write("pt_none = 0\n")
            f.write("pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large\n")
            f.write("pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium\n")
            f.write("pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small\n\n")

            f.write("parties = [\n\n")

            for party in codeData:
                f.write("(\"" + party.id + "\", \"" + party.name + "\", ")

                if party.icon != None and isinstance(party.icon, MapIcon):
                    f.write("icon_" + party.icon.id + "|")

                if len(party.flags) > 0:
                    f.write("|".join(party.flags) + ", ")
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

