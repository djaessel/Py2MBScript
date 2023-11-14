# This Python file uses the following encoding: utf-8
from ScriptConverter import ScriptConverter
from game_menu import GameMenu

import inspect
import test_game_menus

class GameMenuConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveGameMenus(self):
        gameMenus = []
        for i in vars(test_game_menus):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_game_menus,i)
                if not "<function" in str(attr) and not "MenuOption" in str(attr):
                    gameMenus.append(attr)
        return gameMenus

    def writeScriptOutputFile(self, codeData : dict[GameMenu]):
        with open("./build_system/module_game_menus.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("game_menus = [\n\n")

            for gameMenu in codeData:
                f.write("(\"" + gameMenu.id + "\", " + str(gameMenu.flags) + ", \n")
                f.write("  \"" + gameMenu.text  + "\", \n")
                f.write("  \"" + gameMenu.meshName + "\", [\n")

                codeLines = inspect.getsourcelines(gameMenu.conditionBlock)[0]
                for i in range(len(codeLines)):
                    codeLines[i] = codeLines[i][4:]
                codeLines.pop(0)
                codeLines = self.transformScriptBlock(codeLines)
                codeLines.pop()
                self.writeScriptCode(f, codeLines)

                f.write("],\n[\n")

                for menuOption in gameMenu.menuOptions:
                    f.write("(\"" + menuOption.id + "\", [\n")

                    codeLines = inspect.getsourcelines(menuOption.conditionBlock)[0]
                    for i in range(len(codeLines)):
                        codeLines[i] = codeLines[i][4:]
                    codeLines.pop(0)
                    codeLines = self.transformScriptBlock(codeLines)
                    codeLines.pop()
                    if len(codeLines) > 2:
                        codeLines.pop(0)
                        codeLines.pop()
                    self.writeScriptCode(f, codeLines)

                    f.write("], \"" + menuOption.text + "\", [\n")

                    codeLines = inspect.getsourcelines(menuOption.consequenceBlock)[0]
                    for i in range(len(codeLines)):
                        codeLines[i] = codeLines[i][4:]
                    codeLines.pop(0)
                    codeLines = self.transformScriptBlock(codeLines)
                    self.writeScriptCode(f, codeLines)

                f.write("]),\n")

            f.write("]\n")
