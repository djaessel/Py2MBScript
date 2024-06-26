# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from TriggerConverter import TriggerConverter
from presentation import Presentation

import inspect
import presentations

class PresentationConverter(ScriptConverter):

    def createCode(self):
        ScriptConverter.is_trigger_code = True
        presentationsx = self.retrievePresentations()
        self.writeScriptOutputFile(presentationsx)

    def retrievePresentations(self):
        presentationsx = []
        for i in vars(presentations):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(presentations,i)
                sx = str(attr)
                if not "<function" in sx and not "<module" in sx and not "MB" in sx:
                    if not "SimpleTrigger" in sx and not "Event" in sx:
                        presentationsx.append(attr)
        return presentationsx


    def writeScriptOutputFile(self, codeData : list[Presentation]):
        with open("./build_system/module_presentations.py", "w") as f:
            f.write("from header_common import *\n")
            f.write("from header_presentations import *\n")
            f.write("from header_mission_templates import *\n")
            f.write("from ID_meshes import *\n")
            f.write("from header_operations import *\n")
            f.write("from header_triggers import *\n")
            f.write("from module_constants import *\n")
            f.write("import string\n\n")

            f.write("presentations = [\n\n")

            for presentation in codeData:
                f.write("(\"" + presentation.id + "\",")

                if presentation.is_read_only and presentation.has_manual_end_only:
                    f.write("prsntf_read_only|prsntf_manual_end_only")
                elif presentation.is_read_only:
                    f.write("prsntf_read_only")
                elif presentation.has_manual_end_only:
                    f.write("prsntf_manual_end_only")
                else:
                    f.write("0")
                f.write(",")

                f.write(presentation.mesh_id + ",[\n")

                if len(presentation.triggers) > 0:
                    f.write("\n")
                    for trigger in presentation.triggers:
                        f.write("(" + TriggerConverter.retrieveCorrectTrigger(trigger.triggerInterval) + ", [\n")
                        codeLines = inspect.getsourcelines(trigger.codeBlock)[0]
                        for i in range(len(codeLines)):
                            codeLines[i] = codeLines[i][4:]
                        x = self.transformScriptLine(codeLines[0])
                        x.pop(0)
                        codeLines.pop(0)
                        codeLines = self.transformScriptBlock(codeLines)
                        if len(x) > 0:
                            y = []
                            y.extend(x)
                            y.extend(codeLines)
                            codeLines = y
                        self.writeScriptCode(f, codeLines)

                f.write("]),\n")


            f.write("\n] # PRESENTATIONS END\n")
