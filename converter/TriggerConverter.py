# This Python file uses the following encoding: utf-8
from ScriptConverter import ScriptConverter

import inspect
import test_triggers
import header_triggers


class TriggerConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveTriggers(self):
        triggers = []
        for i in vars(test_triggers):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_triggers,i)
                triggers.append(attr)
        return triggers

    @staticmethod
    def retrieveCorrectTrigger(interval : float) -> str:
        for v in vars(header_triggers):
            if v.startswith("ti_"):
                attr = getattr(header_triggers,v)
                if attr == interval:
                    return v
        return str(interval)

    def writeScriptOutputFile(self, codeData):
        with open("./build_system/module_triggers.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
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
