# This Python file uses the following encoding: utf-8


class ScriptConverter:
    registers = []
    str_registers = []
    pos_registers = []

    codex = dict()
    cur_players = dict()
    cur_options = dict()

    def __init__(self):
        with open("header_operations.py") as f:
            for line in f:
                if "=" in line and "#" in line:
                    code = line.split('=')[0].strip()
                    self.codex[code] = line.split('#')[1].strip()

        for i in range(66):
            self.registers.append("reg" + str(i))

        for i in range(68):
            self.str_registers.append("s" + str(i))

        for i in range(64):
            self.pos_registers.append("pos" + str(i))


    def is_float(self, v):
        try:
          f=float(v)
        except ValueError:
          return False
        return True


    def transformCode(self, code):
        if len(code.strip()) == 0:
            return [""]

        if code.strip().startswith('#'):
            # return [code.strip()]
            return [""]
        elif "=" in code:
            tmp = code.split('=')
            varName = tmp[0].strip()
            funcCall = tmp[1].strip()
            liny = self.getFuncCodeLine(funcCall)
            if liny.endswith("# ERROR 1"):
                if "." in liny:
                    tmp = funcCall.split('.')
                    curP = tmp[0].strip()
                    if curP in self.cur_players:
                        player_func_name = "player_" + tmp[1].strip()
                        liny = self.getFuncCodeLine(player_func_name)
                        liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
                        liny = self.replaceVarWithPlaceholder(liny, "<player_id>", self.cur_players[curP])
                    elif curP in self.cur_options:
                        player_func_name = "options_" + tmp[1].strip()
                        liny = self.getFuncCodeLine(player_func_name)
                        liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
                elif funcCall.startswith("MBPlayer("):
                    self.cur_players[varName] = funcCall.split(')')[0].split('(')[1]
                    liny = ""
                elif funcCall.startswith("MBOptions("):
                    self.cur_options[varName] = funcCall.split(')')[0].split('(')[1] # should be string empty here
                    liny = ""
                else:
                    liny = "(assign,<var1>,<var2>)"
                    liny = self.replaceVarWithPlaceholder(liny, "<var1>", varName)
                    liny = self.replaceVarWithPlaceholder(liny, "<var2>", funcCall)
            else:
                liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
                liny = self.replaceFuncParams(liny, funcCall)
            return [liny]
        elif "." in code:
            tmp = code.split('.')
            curP = tmp[0].strip()
            if curP in self.cur_players:
                player_func_name = "player_" + tmp[1].strip()
                liny = self.getFuncCodeLine(player_func_name)
                liny = self.replaceVarWithPlaceholder(liny, "<player_id>", self.cur_players[curP])
                liny = self.replaceFuncParams(liny, player_func_name)
            elif curP in self.cur_options:
                player_func_name = "options_" + tmp[1].strip()
                liny = self.getFuncCodeLine(player_func_name)
                liny = self.replaceFuncParams(liny, player_func_name)
            return [liny]
        elif code.startswith("print("):
            if "print(\"" in code:
                text = code.split('"')[1]
                b = ["(display_message, \"@" + text + "\")"]
            else:
                pseudoCode = code.split('(')[1].split(')')[0]
                if pseudoCode in self.str_registers or pseudoCode in self.registers:
                    b = ["(display_message, \"@{" + pseudoCode + "}\")"]
                else:
                    b = [self.replaceVarWithPlaceholder("(assign, reg0, <placeholder>)", "<placeholder>", pseudoCode)]
                    b.append("(display_message, \"@{reg0}\")")
            return b
        elif "(" in code and ")" in code:
            liny = self.getFuncCodeLine(code)
            return [liny]

        return [""] # ERROR 2 # ignored code


    def findParams(self, funcCall, startIdx = 1):
        params = funcCall.rstrip('),').split(',')[startIdx:]
        idx = -1
        for i, param in enumerate(params):
            if ":" in param:
                idx = i
            params[i] = params[i].strip()
        if idx >= 0:
            del params[idx]
        return params


    def replaceFuncParams(self, liny, funcCall):
        params = self.findParams(liny)
        actParams = self.findParams(funcCall.split('(')[1], 0)
        for i in range(len(params)):
            liny = self.replaceVarWithPlaceholder(liny, params[i], actParams[i])
        return liny


    def getFuncCodeLine(self, funcCall):
        funcName = funcCall.split('(')[0].strip()
        liny = funcCall + " # ERROR 1"
        if funcName in self.codex:
            liny = self.codex[funcName]
        return liny


    def resolveSimpleCondition(self, cond):
        b = []
        if "> " in cond:
            l = "(gt,<var1>,<var2>)"
            tmp = cond.split('>')
            l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
            l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
            b.append(l)
        elif "< " in cond:
            l = "(lt,<var1>,<var2>)"
            tmp = cond.split('<')
            l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
            l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
            b.append(l)
        elif "==" in cond:
            l = "(eq,<var1>,<var2>)"
            tmp = cond.split('==')
            l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
            l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
            b.append(l)
        elif "!=" in cond or "<>" in cond:
            l = "(neq,<var1>,<var2>)"
            tmp = cond.split('!=')
            l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
            l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
            b.append(l)
        elif "<=" in cond:
            l = "(le,<var1>,<var2>)"
            tmp = cond.split('<=')
            l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
            l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
            b.append(l)
        elif ">=" in cond:
            l = "(ge,<var1>,<var2>)"
            tmp = cond.split('>=')
            l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
            l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
            b.append(l)
        else:
            l = self.transformCode(cond)
            b.extend(l)
        return b


    def replaceVarWithPlaceholder(self, line, placeholder, varname):
        if varname in self.registers or varname in self.pos_registers or varname in self.str_registers or self.is_float(varname):
            line = line.replace(placeholder, varname)
        elif '"' in varname and varname.startswith('"') and varname.endswith('"'):
            line = line.replace(placeholder, varname)
        else:
            line = line.replace(placeholder, "\":" + varname + "\"")
        return line


    def resolveOr(self, cond):
        conds = cond.split('|')
        x = len(conds)
        b = []
        for i in range(x):
            l = self.resolveSimpleCondition(conds[i])
            if i < x - 1:
                l[0] = l[0].replace("(", "(this_or_next|")
            b.extend(l)
        return b


    def transformScriptLine(self, scriptLine):
        scriptLine = scriptLine.strip()[4:]
        scriptName = scriptLine.split('(')[0]
        scriptParams = scriptLine.split('(')[1].split(')')[0].split(',')
        b = ["(\"" + scriptName + "\", ["]
        if len(scriptParams[0].strip()) > 0:
            for i, param in enumerate(scriptParams):
                if param.strip() != "self":
                    if scriptParams[0].strip() == "self":
                        i += 1
                    b.append("(store_script_param, \":" + param.strip() + "\", " + str(i + 1) + ")")
        return b


    def transformIfBlock(self, ifCode):
        b = ["(try_begin)"]
        conditionsLine = ifCode.lstrip()[3:].replace(" and ", " & ").replace(" or ", " | ")
        conditionsLine = conditionsLine.split(':')[0]

        conditions = conditionsLine.split('&')
        for cond in conditions:
            if "|" in cond:
                condx = self.resolveOr(cond)
            else:
                condx = self.resolveSimpleCondition(cond)
            b.extend(condx)
        return b


    def transformElseIfBlock(self, ifCode):
        b = ["(else_try)"]
        conditionsLine = ifCode.lstrip()[5:].replace(" and ", " & ").replace(" or ", " | ")
        conditionsLine = conditionsLine.split(':')[0]

        conditions = conditionsLine.split('&')
        for cond in conditions:
            if "|" in cond:
                condx = self.resolveOr(cond)
            else:
                condx = self.resolveSimpleCondition(cond)
            b.extend(condx)
        return b


    def transformElseBlock(self, code):
        b = ["(else_try)"]
        return b


    def transformScriptBlock(self, codeBlock : list):
        lastIndentCount = 0
        lastScriptIdx = -1

        curIdx = -1
        allCodes = []
        for codeLine in codeBlock:
            code = codeLine
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
            elif code.startswith("def "):
                lastIndentCount = 1
                if len(allCodes) > 0 and lastScriptIdx >= 0:
                    allCodes.append("])")
                coy = self.transformScriptLine(code)
                lastScriptIdx = curIdx
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


    def writeScriptOutputFile(self, codeData):
        with open("test_scripts_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("scripts = [\n\n")

            curIndent = 0
            for line in codeData:
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


    def readScriptTestCode(self):
        lines = []
        with open("test_scripts.py") as f:
            for line in f:
                lines.append(line)
        return lines

