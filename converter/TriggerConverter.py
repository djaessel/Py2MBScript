# This Python file uses the following encoding: utf-8
from ScriptConverter import ScriptConverter
from trigger import Trigger

import inspect
import triggers
import header_triggers


class TriggerConverter(ScriptConverter):

    def createCode(self):
        ScriptConverter.is_trigger_code = True
        triggersx = self.retrieveTriggers()
        self.writeScriptOutputFile(triggersx)

    def retrieveTriggers(self):
        triggersx = []
        for i in vars(triggers):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(triggers,i)
                sAttr = str(attr)
                if not "function" in sAttr:
                    triggersx.append(attr)
        return triggersx

    @staticmethod
    def retrieveCorrectTrigger(interval : float) -> str:
        for v in vars(header_triggers):
            if v.startswith("ti_"):
                attr = getattr(header_triggers,v)
                if attr == interval:
                    return v
        return str(interval)

    def writeScriptOutputFile(self, codeData : list[Trigger]):
        with open("./build_system/module_triggers.py", "w") as f:
            f.write("from header_common import *\n")
            f.write("from header_operations import *\n")
            f.write("from header_parties import *\n")
            f.write("from header_items import *\n")
            f.write("from header_skills import *\n")
            f.write("from header_triggers import *\n")
            f.write("from header_troops import *\n\n")

            f.write("from module_constants import *\n\n")

            f.write("triggers = [\n\n")

            for trigger in codeData:
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

            f.write("]\n")
