# This Python file uses the following encoding: utf-8
from ScriptConverter import ScriptConverter
from TriggerConverter import TriggerConverter
from simple_trigger import SimpleTrigger

import inspect
import simple_triggers


class SimpleTriggerConverter(ScriptConverter):

    def createCode(self):
        simpleTriggers = self.retrieveTriggers()
        self.writeScriptOutputFile(simpleTriggers)

    def retrieveTriggers(self):
        simpleTriggers = []
        for i in vars(simple_triggers):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(simple_triggers,i)
                simpleTriggers.append(attr)
        return simpleTriggers


    def writeScriptOutputFile(self, codeData : list[SimpleTrigger]):
        with open("./build_system/module_simple_triggers.py", "w") as f:
            f.write("from __future__ import division\n")
            f.write("from past.utils import old_div\n")
            f.write("from header_common import *\n")
            f.write("from header_operations import *\n")
            f.write("from header_parties import *\n")
            f.write("from header_items import *\n")
            f.write("from header_skills import *\n")
            f.write("from header_triggers import *\n")
            f.write("from header_troops import *\n")
            f.write("from header_music import *\n\n")

            f.write("from module_constants import *\n\n")

            f.write("simple_triggers = [\n\n")

            for trigger in codeData:
                f.write("(" + TriggerConverter.retrieveCorrectTrigger(trigger.triggerInterval) + ", [\n")
                codeLines = inspect.getsourcelines(trigger.codeBlock)[0]
                for i in range(len(codeLines)):
                    codeLines[i] = codeLines[i][4:]
                codeLines.pop(0)
                codeLines = self.transformScriptBlock(codeLines)
                self.writeScriptCode(f, codeLines)

            f.write("]\n")
