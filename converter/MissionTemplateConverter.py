# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from TriggerConverter import TriggerConverter
from mission_template import MissionTemplate

import inspect
import test_mission_templates


class MissionTemplateConverter(ScriptConverter):

    def createCode(self):
        missionTemps = self.retrieveMissionTemplates()
        self.writeScriptOutputFile(missionTemps)

    def retrieveMissionTemplates(self):
        mts = []
        for i in vars(test_mission_templates):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_mission_templates,i)
                if not "<function" in str(attr) and not "<module" in str(attr) and not "MB" in str(attr)  and not "Item" in str(attr) and not "SpawnRecord" in str(attr) and not "Trigger" in str(attr):
                    mts.append(attr)
        return mts

    def writeScriptOutputFile(self, codeData : list[MissionTemplate]):
        with open("./build_system/module_mission_templates.py", "w") as f:
            f.write("from header_common import *\n")
            f.write("from header_operations import *\n")
            f.write("from header_mission_templates import *\n")
            f.write("from header_animations import *\n")
            f.write("from header_sounds import *\n")
            f.write("from header_music import *\n")
            f.write("from header_items import *\n")
            f.write("from module_constants import *\n\n")

            f.write("mission_templates = [\n\n")

            for mt in codeData:
                f.write("(\"" + mt.id + "\", ")

                if len(mt.flags) > 0:
                    f.write("|".join(mt.flags))
                else:
                    f.write("0")
                f.write(", ")

                f.write(str(mt.missionType) + ",\n") # TODO: later write out in text

                f.write("\"" + mt.description + "\",\n")

                f.write("[")
                for sr in mt.spawnRecords:
                    f.write("(" + str(sr.entry_no) + ", ")

                    if len(sr.spawnFlags) > 0:
                        f.write("|".join(sr.spawnFlags))
                    else:
                        f.write("0")
                    f.write(", ")

                    if len(sr.alterFlags) > 0:
                        f.write("|".join(sr.alterFlags))
                    else:
                        f.write("0")
                    f.write(", ")

                    if len(sr.aiFlags) > 0:
                        f.write("|".join(sr.aiFlags))
                    else:
                        f.write("0")
                    f.write(", ")

                    f.write(str(sr.number_of_troops) + ", ")

                    f.write("[")
                    if len(sr.equipment) > 0:
                        for item in sr.equipment:
                            f.write("itm_" + item.id + ",")
                    f.write("]),\n")

                f.write("],\n[")

                if len(mt.triggers) > 0:
                    f.write("\n")
                    for trigger in mt.triggers:
                        f.write("(" + TriggerConverter.retrieveCorrectTrigger(trigger.triggerInterval) + ", " + str(trigger.delay) + ", " + TriggerConverter.retrieveCorrectTrigger(trigger.triggerPause) + ", [\n")

                        codeLines = inspect.getsourcelines(trigger.conditionBlock)[0]
                        for i in range(len(codeLines)):
                            codeLines[i] = codeLines[i][4:]
                        codeLines.pop(0)
                        codeLines = self.transformScriptBlock(codeLines)
                        codeLines.pop()
                        if len(codeLines) > 2:
                            codeLines.pop(0)
                            codeLines.pop()
                        self.writeScriptCode(f, codeLines)
                        f.write("], [\n")

                        codeLines = inspect.getsourcelines(trigger.codeBlock)[0]
                        for i in range(len(codeLines)):
                            codeLines[i] = codeLines[i][4:]
                        codeLines.pop(0)
                        codeLines = self.transformScriptBlock(codeLines)
                        self.writeScriptCode(f, codeLines)

                f.write("]),\n")

            f.write("\n] # MISSION TEMPLATES END\n")
