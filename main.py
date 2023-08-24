# This Python file uses the following encoding: utf-8
import sys

codex = dict()
with open("header_operations.py") as f:
    for line in f:
        if "=" in line and "#" in line:
            code = line.split('=')[0].strip()
            codex[code] = line.split('#')[1].strip()

# print(codex)


registers = []
for i in range(66):
    registers.append("reg" + str(i))

str_registers = []
for i in range(68):
    registers.append("s" + str(i))

pos_registers = []
for i in range(64):
    registers.append("pos" + str(i))




def is_float(v):
    try:
      f=float(v)
    except ValueError:
      return False
    return True


cur_players = dict()


def transformCode(code):
    if len(code.strip()) == 0:
        return [""]

    if "=" in code:
        tmp = code.split('=')
        varName = tmp[0].strip()
        funcCall = tmp[1].strip()
        liny = getFuncCodeLine(funcCall)
        if liny.endswith("# ERROR 1"):
            if "." in liny:
                tmp = funcCall.split('.')
                curP = tmp[0].strip()
                if curP in cur_players:
                    player_func_name = "player_" + tmp[1].strip()
                    liny = getFuncCodeLine(player_func_name)
                    liny = replaceVarWithPlaceholder(liny, "<destination>", varName)
                    liny = replaceVarWithPlaceholder(liny, "<player_id>", cur_players[curP])
            elif funcCall.startswith("MBPlayer("):
                cur_players[varName] = funcCall.split(')')[0].split('(')[1]
                liny = ""
            else:
                liny = "(assign,<var1>,<var2>)"
                liny = replaceVarWithPlaceholder(liny, "<var1>", varName)
                liny = replaceVarWithPlaceholder(liny, "<var2>", funcCall)
        else:
            liny = replaceVarWithPlaceholder(liny, "<destination>", varName)
            liny = replaceFuncParams(liny, funcCall)
        return [liny]
    elif "." in code:
        tmp = code.split('.')
        curP = tmp[0].strip()
        if curP in cur_players:
            player_func_name = "player_" + tmp[1].strip()
            liny = getFuncCodeLine(player_func_name)
            liny = replaceVarWithPlaceholder(liny, "<player_id>", cur_players[curP])
            liny = replaceFuncParams(liny, player_func_name)
        return [liny]
    elif code.startswith("print("):
        if "print(\"" in code:
            text = code.split('"')[1]
            b = ["(display_message, \"@" + text + "\")"]
        else:
            pseudoCode = code.split('(')[1].split(')')[0]
            if pseudoCode in str_registers or pseudoCode in registers:
                b = ["(display_message, \"@{" + pseudoCode + "}\")"]
            else:
                b = [replaceVarWithPlaceholder("(assign, reg0, <placeholder>)", "<placeholder>", pseudoCode)]
                b.append("(display_message, \"@{reg0}\")")
        return b
    elif "(" in code and ")" in code:
        liny = getFuncCodeLine(code)
        return [liny]
    elif code.strip().startswith('#'):
        return [code.strip()]

    return [""] # ERROR 2 # ignored code


def findParams(funcCall, startIdx = 1):
    params = funcCall.rstrip('),').split(',')[startIdx:]
    idx = -1
    for i, param in enumerate(params):
        if ":" in param:
            idx = i
        params[i] = params[i].strip()
    if idx >= 0:
        del params[idx]
    return params


def replaceFuncParams(liny, funcCall):
    params = findParams(liny)
    actParams = findParams(funcCall.split('(')[1], 0)
    for i in range(len(params)):
        liny = replaceVarWithPlaceholder(liny, params[i], actParams[i])
    return liny

def getFuncCodeLine(funcCall):
    funcName = funcCall.split('(')[0].strip()
    liny = funcCall + " # ERROR 1"
    if funcName in codex:
        liny = codex[funcName]
    return liny


def resolveSimpleCondition(cond):
    b = []
    if "> " in cond:
        l = "(gt,<var1>,<var2>)"
        tmp = cond.split('>')
        l = replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
        l = replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
        b.append(l)
    elif "< " in cond:
        l = "(lt,<var1>,<var2>)"
        tmp = cond.split('<')
        l = replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
        l = replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
        b.append(l)
    elif "==" in cond:
        l = "(eq,<var1>,<var2>)"
        tmp = cond.split('==')
        l = replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
        l = replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
        b.append(l)
    elif "!=" in cond or "<>" in cond:
        l = "(neq,<var1>,<var2>)"
        tmp = cond.split('!=')
        l = replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
        l = replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
        b.append(l)
    elif "<=" in cond:
        l = "(le,<var1>,<var2>)"
        tmp = cond.split('<=')
        l = replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
        l = replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
        b.append(l)
    elif ">=" in cond:
        l = "(ge,<var1>,<var2>)"
        tmp = cond.split('>=')
        l = replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
        l = replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
        b.append(l)
    else:
        l = transformCode(cond)
        b.extend(l)
    return b


def replaceVarWithPlaceholder(line, placeholder, varname):
    if varname in registers or varname in pos_registers or varname in str_registers or is_float(varname):
        line = line.replace(placeholder, varname)
    elif '"' in varname and varname.startswith('"') and varname.endswith('"'):
        line = line.replace(placeholder, varname)
    else:
        line = line.replace(placeholder, "\":" + varname + "\"")
    return line


def resolveOr(cond):
    conds = cond.split('|')
    x = len(conds)
    b = []
    for i in range(x):
        l = resolveSimpleCondition(conds[i])
        if i < x - 1:
            l[0] = l[0].replace("(", "(this_or_next|")
        b.extend(l)
    return b


def transformScriptLine(scriptLine):
    scriptLine = scriptLine.strip()[4:]
    scriptName = scriptLine.split('(')[0]
    scriptParams = scriptLine.split('(')[1].split(')')[0].split(',')
    b = ["(\"" + scriptName + "\", ["]
    if len(scriptParams[0].strip()) > 0:
        for i, param in enumerate(scriptParams):
            b.append("(store_script_param, \":" + param.strip() + "\", " + str(i + 1) + ")")
    return b


def transformIfBlock(ifCode):
    b = ["(try_begin)"]
    conditionsLine = ifCode.lstrip()[3:].replace(" and ", " & ").replace(" or ", " | ")
    conditionsLine = conditionsLine.split(':')[0]

    conditions = conditionsLine.split('&')
    for cond in conditions:
        if "|" in cond:
            condx = resolveOr(cond)
        else:
            condx = resolveSimpleCondition(cond)
        b.extend(condx)
    return b


def transformScriptBlock(codeBlock : list):
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
            coy = transformIfBlock(code)
        elif code.startswith("def "):
            lastIndentCount = 1
            if len(allCodes) > 0 and lastScriptIdx >= 0:
                allCodes.append("])")
            coy = transformScriptLine(code)
            lastScriptIdx = curIdx
        else:
            coy = transformCode(code)

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




if __name__ == "__main__":

    lines = []
    with open("test_mbscript.py") as f:
        for line in f:
            lines.append(line)

    cody = transformScriptBlock(lines)

    with open("test_output.py", "w") as f:
        f.write("from header_operations import *\n")
        f.write("from header_common import *\n\n")
        f.write("scripts = [\n\n")
        for line in cody:
            f.write(line)
            if not line.endswith("["):
                f.write(",")
            if line == "])":
                f.write("\n")
            f.write("\n")
        f.write("]\n")

    sys.exit()
