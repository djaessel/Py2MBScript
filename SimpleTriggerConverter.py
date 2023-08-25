# This Python file uses the following encoding: utf-8
from ScriptConverter import ScriptConverter

class SimpleTriggerConverter(ScriptConverter):
    triggers = dict()

    def __init__(self):
        pass

    def readScriptTestCode(self):
        lines = []
        with open("test_simple_triggers.py") as f:
            for line in f:
                lines.append(line)
        return lines

    def transformScriptBlock(self, codeBlock : list):
        lastIndentCount = 0

        curIdx = -1
        allCodes = []
        for codeLine in codeBlock:
            code = codeLine[4:]
            inlineIndentCount = 0
            curIdx += 1

            coy = []
            while code.startswith("    "):
                code = code[4:]
                inlineIndentCount += 1
            if code.startswith("if "):
                coy = self.transformIfBlock(code)
            elif code.startswith("elif "):
                coy = self.transformElseIfBlock(code)
            elif code.startswith("else:"):
                coy = self.transformElseBlock(code)
            else:
                coy = self.transformCode(code)

            if lastIndentCount > inlineIndentCount:
                xyz = inlineIndentCount
                xyz += 1
                while lastIndentCount > xyz:
                    xyz += 1
                    coy.append("(try_end)")

            lastIndentCount = inlineIndentCount
            allCodes.extend(coy)

        if lastIndentCount > 0:
            xyz = 0
            while lastIndentCount > xyz:
                xyz += 1
                allCodes.append("(try_end)")

        allCodes = [x.rstrip(',') for x in allCodes if x]
        allCodes.append("])")

        return allCodes

    def transformSimpleTrigger(self, codeLines):
        for i, line in enumerate(codeLines):
            if line.startswith("class ") and "(SimpleTrigger)" in line:
                triggerName = line[6:].split('(')[0]
                self.triggers[triggerName] = []
                curCodeBlock = []
                line = "     "
                while line.startswith("    "):
                    i += 1
                    line = codeLines[i]
                    curCodeBlock.append(line)

                cody = self.transformScriptBlock(curCodeBlock)
                self.triggers[triggerName].append(cody)
            elif "=" in line:
                tmp = line.split('=')
                triggerInit = tmp[1].strip()
                if "(" in triggerInit and ")" in triggerInit:
                    triggerName = triggerInit.split('(')[0]
                    triggerInterval = triggerInit.split('(')[1].split(')')[0]
                    if triggerName in self.triggers:
                        self.triggers[triggerName].append(triggerInterval)
                        self.triggers[triggerName].append(tmp[0].strip())

        return self.triggers

    def writeScriptOutputFile(self, codeData):
        with open("test_simple_triggers_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("simple_triggers = [\n\n")

            for triggerName in codeData:
                if len(codeData[triggerName]) >= 3:
                    codeLines = codeData[triggerName][0]
                    codeLines[0] = "(" + str(codeData[triggerName][1]) + ", ["
                    # del codeLines[len(codeLines)-2]
                    curIndent = 0
                    for line in codeLines:
                        if "else_try" in line or "try_end" in line:
                            curIndent -= 1

                        for i in range(curIndent):
                            f.write("    ")

                        f.write(line)

                        if "else_try" in line or "try_begin" in line:
                            curIndent += 1

                        if not line.endswith("["):
                            f.write(",")
                        if line == "])":
                            f.write("\n")
                        f.write("\n")

            f.write("]\n")

