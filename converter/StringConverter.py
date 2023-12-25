# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from MBString import MBString

import test_strings


class StringConverter(ScriptConverter):
    def __init__(self):
        pass

    def createCode(self):
        strings = self.retrieveStrings()
        self.writeScriptOutputFile(strings)

    def retrieveStrings(self):
        strings = []
        for i in vars(test_strings):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_strings,i)
                strings.append(attr)
        return strings

    def writeScriptOutputFile(self, codeData : list[MBString]):
        with open("./build_system/module_strings.py", "w") as f:
            f.write("# -*- coding: cp1254 -*-\n\n")
            f.write("strings = [\n\n")

            for string in codeData:
                f.write("(\"" + string.id + "\",\"" + string.text + "\"),\n")

            f.write("\n] # STRINGS END\n")
