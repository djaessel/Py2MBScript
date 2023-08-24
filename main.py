# This Python file uses the following encoding: utf-8
import sys
from ScriptConverter import ScriptConverter


if __name__ == "__main__":

    # Module Scripts
    scripter = ScriptConverter()
    lines = scripter.readScriptTestCode()
    codeLines = scripter.transformScriptBlock(lines)
    scripter.writeScriptOutputFile(codeLines)

    sys.exit()

