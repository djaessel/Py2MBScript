# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from info_page import InfoPage

import inspect
import test_info_pages


class InfoPageConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveInfoPages(self):
        infoPages = []
        for i in vars(test_info_pages):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_info_pages,i)
                infoPages.append(attr)
        return infoPages

    def writeScriptOutputFile(self, codeData):
        with open("./test_cases/test_info_pages_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("info_pages = [\n\n")

            for infoPage in codeData:
                f.write("(\"" + infoPage.id + "\",\"" + infoPage.name + "\",\"" + infoPage.text + "\"),\n")

            f.write("\n] # INFO PAGES END\n")

