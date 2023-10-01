# This Python file uses the following encoding: utf-8
from ScriptConverter import ScriptConverter

import inspect
import test_simple_triggers


class SimpleTriggerConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveTriggers(self):
        simpleTriggers = []
        for i in vars(test_simple_triggers):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_simple_triggers,i)
                simpleTriggers.append(attr)
        return simpleTriggers

    def writeScriptOutputFile(self, codeData):
        with open("./test_cases/test_simple_triggers_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("simple_triggers = [\n\n")

            for trigger in codeData:
                f.write("(" + str(trigger.triggerInterval) + ", [\n")
                codeLines = inspect.getsourcelines(trigger.codeBlock)[0]
                for i in range(len(codeLines)):
                    codeLines[i] = codeLines[i][4:]
                codeLines.pop(0)
                codeLines = self.transformScriptBlock(codeLines)
                self.writeScriptCode(f, codeLines)

            f.write("]\n")
