# This Python file uses the following encoding: utf-8


class ScriptConverter:
    registers = []
    str_registers = []
    pos_registers = []

    codex = dict()

    cur_players = dict()
    cur_parties = dict()
    cur_options = dict()
    cur_items = dict()

    # presentation overlays (maybe separate)
    prsnt_text_overlays = dict()

    def __init__(self):
        with open("./test_cases/header_operations.py") as f:
            for line in f:
                if "=" in line and "#" in line:
                    code = line.split('=')[0].strip()
                    self.codex[code] = line.split('#')[1].strip()

        for i in range(66):#128
            self.registers.append("reg" + str(i))

        for i in range(68):#128
            self.str_registers.append("s" + str(i))

        for i in range(64):#128
            self.pos_registers.append("pos" + str(i))


    def is_float(self, v):
        try:
          f=float(v)
        except ValueError:
          return False
        return True


    def handleEqualsSign(self, code):
        tmp = code.split('=')
        varName = tmp[0].strip()
        funcCall = tmp[1].strip()
        liny = self.getFuncCodeLine(funcCall)
        if liny.endswith("# ERROR 1"):
            if "." in liny:
                liny = self.handleDotSignInEqualLine(liny, funcCall, varName)
            elif funcCall.startswith("MBParty("):
                self.cur_parties[varName] = funcCall.split(')')[0].split('(')[1]
                liny = ""
            elif funcCall.startswith("MBPlayer("):
                self.cur_players[varName] = funcCall.split(')')[0].split('(')[1]
                liny = ""
            elif funcCall.startswith("MBOptions("):
                self.cur_options[varName] = funcCall.split(')')[0].split('(')[1] # should be string empty here
                liny = ""
            elif funcCall.startswith("Item("):
                self.cur_items[varName] = funcCall.split(')')[0].split('(')[1] # should be string empty here
                liny = ""
            elif funcCall.startswith("MBTextOverlay("):
                tmp = funcCall.split(')')[0].split('(')[1]
                liny = "(create_text_overlay, <reg>, <str_text>, <text_flags>)"
                tmp = tmp.split(',')
                self.prsnt_text_overlays[varName] = tmp[0].strip()
                liny = liny.replace("<reg>", tmp[0].strip()).replace('<str_text>', tmp[1].strip()).replace("<text_flags>", tmp[2].strip())
            elif varName in self.str_registers:
                liny = "(str_store_string,<var1>,<var2>)"
                liny = self.replaceVarWithPlaceholder(liny, "<var1>", varName)
                if '"' in funcCall and not funcCall.strip('"').startswith("str_"):
                    liny = self.replaceVarWithPlaceholder(liny, "<var2>", funcCall.replace('"', '"@').rstrip('@'))
                else:
                    liny = self.replaceVarWithPlaceholder(liny, "<var2>", funcCall)
            else:
                liny = "(assign,<var1>,<var2>)"
                liny = self.replaceVarWithPlaceholder(liny, "<var1>", varName)
                liny = self.replaceVarWithPlaceholder(liny, "<var2>", funcCall)
        else:
            liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
            liny = self.replaceFuncParams(liny, funcCall)
        return [liny]


    def handleDotSignInEqualLine(self, liny, funcCall, varName):
        tmp = funcCall.split('.')
        curP = tmp[0].strip()
        if curP in self.cur_players:
            p_func_name = "player_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
            liny = self.replaceVarWithPlaceholder(liny, "<player_id>", self.cur_players[curP])
        elif curP in self.cur_parties:
            p_func_name = "party_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
            liny = self.replaceVarWithPlaceholder(liny, "<party_id>", self.cur_parties[curP])
        elif curP in self.cur_items:
            p_func_name = "item_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
            liny = self.replaceVarWithPlaceholder(liny, "<item_id>", self.cur_items[curP])
            liny = self.replaceVarWithPlaceholder(liny, "<item_kind_no>", self.cur_items[curP])
        elif curP in self.cur_options:
            p_func_name = "options_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
        return liny


    def handleDotSign(self, code):
        tmp = code.split('.')
        curP = tmp[0].strip()
        if curP in self.cur_players:
            p_func_name = "player_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<player_id>", self.cur_players[curP])
            liny = self.replaceFuncParams(liny, p_func_name)
        elif curP in self.cur_parties:
            p_func_name = "party_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<party_id>", self.cur_parties[curP])
            liny = self.replaceFuncParams(liny, p_func_name)
        elif curP in self.cur_items:
            p_func_name = "item_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<item_id>", self.cur_items[curP])
            liny = self.replaceVarWithPlaceholder(liny, "<item_kind_no>", self.cur_items[curP])
            liny = self.replaceFuncParams(liny, p_func_name)
        elif curP in self.cur_options:
            p_func_name = "options_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceFuncParams(liny, p_func_name)
        elif curP in self.prsnt_text_overlays:
            regi = self.prsnt_text_overlays[curP]
            if "set_position" in tmp[1]:
                pos = tmp[1].split(')')[0].split('(')[1].split(',')
                return ["(position_set_x, pos1, <pos_x>)".replace("<pos_x>", pos[0].strip()),
                        "(position_set_y, pos1, <pos_y>)".replace("<pos_y>", pos[1].strip()),
                        "(overlay_set_position, <reg>, pos1)".replace("<reg>", regi)]
            elif "set_size" in tmp[1]:
                pos = tmp[1].split(')')[0].split('(')[1].split(',')
                return ["(position_set_x, pos1, <pos_x>)".replace("<pos_x>", pos[0].strip()),
                        "(position_set_y, pos1, <pos_y>)".replace("<pos_y>", pos[1].strip()),
                        "(overlay_set_size, <reg>, pos1)".replace("<reg>", regi)]
            else:
                tmp[1] = tmp[1].replace("(", "(" + regi + ",")
                p_func_name = "overlay_" + tmp[1].strip()
                liny = self.getFuncCodeLine(p_func_name)
                #liny = self.replaceVarWithPlaceholder(liny, "<party_id>", self.cur_parties[curP])
                liny = self.replaceFuncParams(liny, p_func_name)
        return [liny]


    def handlePrint(self, code):
        if "print(" in code and "," in code:
            sx = ""
            b = []
            pseudoCode = code.split('(')[1].split(')')[0]
            data = [x.strip() for x in pseudoCode.split(',')]
            for i, d in enumerate(data):
                if d in self.str_registers or d in self.registers:
                    sx += "{" + d + "} "
                elif d.startswith('"') and d.endswith('"'):
                    sx += d.strip('"') + " "
                else:
                    b.append(self.replaceVarWithPlaceholder("(assign, reg" + str(i)+ ", <placeholder>)", "<placeholder>", d))
                    sx += "{reg" + str(i) + "} "

            sx = sx.rstrip()
            b.append("(display_message, \"@"+sx+"\")")
        elif "print(\"" in code:
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


    def handleValSub(self, code):
        liny = "(val_sub, <val1>, <val2>)"
        sx = code.split('-')[0].strip()
        sy = code.split('=')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        return [liny]


    def handleValAdd(self, code):
        liny = "(val_add, <val1>, <val2>)"
        sx = code.split('+')[0].strip()
        sy = code.split('=')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        return [liny]


    def handleValMul(self, code):
        liny = "(val_mul, <val1>, <val2>)"
        sx = code.split('*')[0].strip()
        sy = code.split('=')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        return [liny]


    def handleValDiv(self, code):
        liny = "(val_div, <val1>, <val2>)"
        sx = code.split('/')[0].strip()
        sy = code.split('=')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        return [liny]


    def handleStoreAdd(self, code):
        liny = "(store_add, <val1>, <val2>, <val3>)"
        sx = code.split('=')[0].strip()
        sy = code.split('=')[1].strip().split('+')[0].strip()
        sz = code.split('=')[1].strip().split('+')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        liny = self.replaceVarWithPlaceholder(liny, "<val3>", sz)
        return [liny]


    def handleStoreSub(self, code):
        liny = "(store_mul, <val1>, <val2>, <val3>)"
        sx = code.split('=')[0].strip()
        sy = code.split('=')[1].strip().split('-')[0].strip()
        sz = code.split('=')[1].strip().split('-')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        liny = self.replaceVarWithPlaceholder(liny, "<val3>", sz)
        return [liny]


    def handleStoreMul(self, code):
        liny = "(store_mul, <val1>, <val2>, <val3>)"
        sx = code.split('=')[0].strip()
        sy = code.split('=')[1].strip().split('*')[0].strip()
        sz = code.split('=')[1].strip().split('*')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        liny = self.replaceVarWithPlaceholder(liny, "<val3>", sz)
        return [liny]


    def handleStoreDiv(self, code):
        liny = "(store_div, <val1>, <val2>, <val3>)"
        sx = code.split('=')[0].strip()
        sy = code.split('=')[1].strip().split('/')[0].strip()
        sz = code.split('=')[1].strip().split('/')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        liny = self.replaceVarWithPlaceholder(liny, "<val3>", sz)
        return [liny]


    def transformCode(self, code):
        if len(code.strip()) == 0:
            return [""]

        if code.strip().startswith('#'):
            # return [code.strip()]
            return [""]
        elif code.startswith("print("):
            return self.handlePrint(code)
        elif "+=" in code:
            return self.handleValAdd(code)
        elif "-=" in code:
            return self.handleValSub(code)
        elif "*=" in code:
            return self.handleValMul(code)
        elif "/=" in code:
            return self.handleValDiv(code)
        elif "+" in code and "=" in code and code.index("=") < code.index("+"):
            return self.handleStoreAdd(code)
        elif "-" in code and "=" in code and code.index("=") < code.index("-"):
            return self.handleStoreSub(code)
        elif "*" in code and "=" in code and code.index("=") < code.index("*"):
            return self.handleStoreMul(code)
        elif "/" in code and "=" in code and code.index("=") < code.index("/"):
            return self.handleStoreDiv(code)
        elif "=" in code:
            return self.handleEqualsSign(code)
        elif "." in code:
            return self.handleDotSign(code)
        elif "(" in code and ")" in code:
            liny = self.getFuncCodeLine(code)
            liny = self.replaceFuncParams(liny, code.split(')')[0])
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
            if (not "[" in params[i] and not "]" in params[i]) or ("[" in params[i] and "]" in params[i] and len(actParams) > i):
                liny = self.replaceVarWithPlaceholder(liny, params[i], actParams[i])
            else:
                # print("Ignored optional parameter:", params[i], "|", funcCall, "|", liny)
                liny = liny.replace(", " + params[i], "")
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
        if "not" in b[0]:
            b[0] = b[0].replace("(", "(neg|").replace(":not ", ":")
        return b


    def replaceVarWithPlaceholder(self, line, placeholder, varname):
        if varname in self.registers or varname in self.pos_registers or varname in self.str_registers or self.is_float(varname) or varname.startswith("0x"):
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

    # TODO: actually count these and correctly check
    def transformTryBlock(self, tryCode):
        b = ["(try_begin)"]
        return b


    def transformExceptBlock(self, tryCode):
        b = ["(else_try)"]
        return b


    # TODO: actually count these and correctly check
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


    def transformForBlock(self, code):
        b = ["(try_for_range, <var1>, <var2>, <var3>)"]
        b[0] = self.replaceVarWithPlaceholder(b[0], "<var1>", code[4:code.index(' in range(')])
        tmp = code.split('(')[1].split(')')[0].split(',')
        if len(tmp) == 2:
            start = tmp[0].strip()
            end = tmp[1].strip()
        elif len(tmp) == 3 and int(tmp[2]) < 0:
            start = tmp[1].strip()
            end = tmp[0].strip()
            b[0] = b[0].replace("try_for_range", "try_for_range_backwards")
        else:
            start = 0
            end = tmp[0].strip()

        b[0] = self.replaceVarWithPlaceholder(b[0], "<var2>", str(start))
        b[0] = self.replaceVarWithPlaceholder(b[0], "<var3>", str(end))

        return b


    def transformScriptBlock(self, codeBlock : list):
        lastScriptIdx = -1

        ifCl = []

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
                self.fixIndentionProblem(allCodes, ifCl, inlineIndentCount, code)
                coy = self.transformIfBlock(code)
                ifCl.append((inlineIndentCount, code))
            elif code.startswith("elif "):
                coy = self.transformElseIfBlock(code)
            elif code.startswith("else:"):
                coy = self.transformElseBlock(code)
            elif code.startswith("for "):
                self.fixIndentionProblem(allCodes, ifCl, inlineIndentCount, code)
                coy = self.transformForBlock(code)
                ifCl.append((inlineIndentCount, code))
            elif code.startswith("try:"):
                self.fixIndentionProblem(allCodes, ifCl, inlineIndentCount, code)
                coy = self.transformTryBlock(code)
                ifCl.append((inlineIndentCount, code))
            elif code.startswith("except:"):
                coy = self.transformExceptBlock(code)
            elif code.startswith("while "):
                print("while is not supported yet!")
                # ifCl.append((inlineIndentCount, code))
            elif code.startswith("def "):
                for _ in ifCl:
                    allCodes.append("(try_end)")
                ifCl.clear()

                if len(allCodes) > 0 and lastScriptIdx >= 0:
                    allCodes.append("])")
                coy = self.transformScriptLine(code)
                lastScriptIdx = curIdx
            else:
                coy = self.transformCode(code)
                self.fixIndentionProblem(coy, ifCl, inlineIndentCount, code)

            allCodes.extend(coy)

        # TODO: check for try_ends more carefully

        for _ in ifCl:
            allCodes.append("(try_end)")
        ifCl.clear()

        allCodes = [x.rstrip(',') for x in allCodes if x]
        allCodes.append("])")

        return allCodes


    def fixIndentionProblem(self, c, ifCl, inlineIndentCount, code):
        xyz = []
        for i, ifx in enumerate(ifCl):
            if inlineIndentCount <= ifx[0] and code.strip() != "":
                xyz.append(i)

        if len(xyz) > 0:
            xyz.reverse()
            for x in xyz:
                del ifCl[x]
                c.append("(try_end)")


    def writeScriptCode(self, f, codeData):
        curIndent = 0
        for line in codeData:
            if "else_try" in line or "try_end" in line:
                curIndent -= 1

            for i in range(curIndent):
                f.write("    ")

            f.write(line)

            if "else_try" in line or "try_begin" in line or "try_for" in line:
                curIndent += 1

            if not line.endswith("["):
                f.write(",")
            if line == "])":
                f.write("\n")
            f.write("\n")


    def writeScriptOutputFile(self, codeData):
        with open("./test_cases/test_scripts_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("scripts = [\n\n")
            self.writeScriptCode(f, codeData)
            f.write("]\n")


    def readScriptTestCode(self):
        lines = []
        with open("./test_cases/test_scripts.py") as f:
            for line in f:
                lines.append(line)
        return lines

