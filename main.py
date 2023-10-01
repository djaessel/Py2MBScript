# This Python file uses the following encoding: utf-8
import sys

sys.path.append("./converter/")
sys.path.append("./data_objects/")
sys.path.append("./test_cases/")

from ScriptConverter import ScriptConverter
from SimpleTriggerConverter import SimpleTriggerConverter
from TriggerConverter import TriggerConverter
from GameMenuConverter import GameMenuConverter
from ItemConverter import ItemConverter


if __name__ == "__main__":

    # Module Scripts
    scripter = ScriptConverter()
    lines = scripter.readScriptTestCode()
    codeLines = scripter.transformScriptBlock(lines)
    scripter.writeScriptOutputFile(codeLines)

    # Module Simple Triggers
    simpleTriggerer = SimpleTriggerConverter()
    simpleTriggers = simpleTriggerer.retrieveTriggers()
    simpleTriggerer.writeScriptOutputFile(simpleTriggers)

    # Module Triggers
    triggerer = TriggerConverter()
    triggerers = triggerer.retrieveTriggers()
    triggerer.writeScriptOutputFile(triggerers)

    # Module Game Menus
    gameMenuer = GameMenuConverter()
    gameMenus = gameMenuer.retrieveGameMenus()
    gameMenuer.writeScriptOutputFile(gameMenus)

    # Items
    itemer = ItemConverter()
    items = itemer.retrieveItems()
    itemer.writeScriptOutputFile(items)

    sys.exit()

