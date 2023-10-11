# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from MBString import MBString

import inspect
import test_strings


class StringConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveStrings(self):
        strings = []
        for i in vars(test_strings):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_strings,i)
                strings.append(attr)
        return strings

    def writeScriptOutputFile(self, codeData):
        with open("./test_cases/test_strings_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("strings = [\n\n")

            for string in codeData:
                f.write("(\"" + string.id + "\",\"" + string.text + "\"),\n")

            f.write("\n] # STRINGS END\n")
