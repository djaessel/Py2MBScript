# This Python file uses the following encoding: utf-8
from ScriptConverter import ScriptConverter
from dialog import Dialog

import inspect
import dialogs

class DialogConverter(ScriptConverter):

    def createCode(self):
        ScriptConverter.is_trigger_code = False
        dialogsx = self.retrieveDialogs()
        self.writeScriptOutputFile(dialogsx)

    def retrieveDialogs(self):
        dialogsx = []
        for i in vars(dialogs):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(dialogs,i)
                if not "<function" in str(attr) and not "<module" in str(attr) and not "ItemMesh" in str(attr) and not "SimpleTrigger" in str(attr):
                    dialogsx.append(attr)
        return dialogsx

    def writeScriptOutputFile(self, codeData : list[Dialog]):
        with open("./build_system/module_dialogs.py", "w") as f:
            f.write("# -*- coding: cp1254 -*-\n")
            f.write("from header_common import *\n")
            f.write("from header_dialogs import *\n")
            f.write("from header_operations import *\n")
            f.write("from header_parties import *\n")
            f.write("from header_item_modifiers import *\n")
            f.write("from header_skills import *\n")
            f.write("from header_triggers import *\n")
            f.write("from ID_troops import *\n")
            f.write("from ID_party_templates import *\n\n")
            f.write("from module_constants import *\n\n")

            f.write("dialogs = [\n\n")

            for dialog in codeData:
                f.write("[" + dialog.dialog_partner + ", \"" + dialog.starting_state + "\", [")

                codeLines = inspect.getsourcelines(dialog.conditionBlock)[0]
                for i in range(len(codeLines)):
                    codeLines[i] = codeLines[i][4:]
                codeLines.pop(0)
                codeLines = self.transformScriptBlock(codeLines)
                codeLines.pop()
                if len(codeLines) > 2:
                    codeLines.pop(0)
                    codeLines.pop()
                    f.write("\n")
                self.writeScriptCode(f, codeLines)
                f.write("], \"")

                f.write(dialog.text + "\", \"" + dialog.ending_state + "\", [")

                codeLines = inspect.getsourcelines(dialog.codeBlock)[0]
                for i in range(len(codeLines)):
                    codeLines[i] = codeLines[i][4:]
                codeLines.pop(0)
                codeLines = self.transformScriptBlock(codeLines)
                codeLines.pop()
                self.writeScriptCode(f, codeLines)
                f.write("]],\n")

            f.write("] # DIALOGS END\n")

