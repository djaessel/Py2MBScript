# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from quest import Quest

import quests

class QuestConverter(ScriptConverter):
    def __init__(self):
        pass

    def createCode(self):
        questsx = self.retrieveQuests()
        self.writeScriptOutputFile(questsx)

    def retrieveQuests(self):
        questsx = []
        for i in vars(quests):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(quests,i)
                if not "<function" in str(attr) and not "<module" in str(attr):
                    questsx.append(attr)
        return questsx

    def writeScriptOutputFile(self, codeData : list[Quest]):
        with open("./build_system/module_quests.py", "w") as f:
            f.write("from header_quests import *\n\n")
            f.write("quests = [\n\n")

            for quest in codeData:
                f.write("(\"" + quest.id + "\", \"" + quest.name + "\", ")

                if quest.is_random and quest.show_progress:
                    f.write("qf_random_quest|qf_show_progression")
                elif quest.is_random:
                    f.write("qf_random_quest")
                elif quest.show_progress:
                    f.write("qf_show_progression")
                else:
                    f.write("0")

                f.write(",\n")

                f.write("\"" + quest.description + "\"),\n")

            f.write("\n] # QUESTS END\n")

