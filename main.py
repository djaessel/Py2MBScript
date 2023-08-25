# This Python file uses the following encoding: utf-8
import sys

from ScriptConverter import ScriptConverter
from SimpleTriggerConverter import SimpleTriggerConverter


if __name__ == "__main__":

    # Module Scripts
    scripter = ScriptConverter()
    lines = scripter.readScriptTestCode()
    codeLines = scripter.transformScriptBlock(lines)
    scripter.writeScriptOutputFile(codeLines)

    # Module Simple Triggers
    simpleTriggerer = SimpleTriggerConverter()
    lines = simpleTriggerer.readScriptTestCode()
    simpleTriggers = simpleTriggerer.transformSimpleTrigger(lines)
    simpleTriggerer.writeScriptOutputFile(simpleTriggers)

    sys.exit()

