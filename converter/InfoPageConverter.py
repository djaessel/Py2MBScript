# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from info_page import InfoPage

import info_pages


class InfoPageConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveInfoPages(self):
        infoPages = []
        for i in vars(info_pages):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(info_pages,i)
                infoPages.append(attr)
        return infoPages

    def writeScriptOutputFile(self, codeData : list[InfoPage]):
        with open("./build_system/module_info_pages.py", "w") as f:
            f.write("info_pages = [\n\n")

            for infoPage in codeData:
                f.write("(\"" + infoPage.id + "\",\"" + infoPage.name + "\",\"" + infoPage.text + "\"),\n")

            f.write("\n] # INFO PAGES END\n")

