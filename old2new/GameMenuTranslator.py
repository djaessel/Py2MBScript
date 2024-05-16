# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../modules/")
sys.path.append("../build_system/")
sys.path.append("../data_objects/")

import header_game_menus as mnuHeader
import game_menu as mnuData
import CodeTranslator as codeT


module_path = "/home/djaessel/warband/Modules/Native/"


def readMenus():
    menus = []
    with open(module_path + "menus.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("menu_"):
                tmp = line.strip().split(' ')
                menus.append([tmp])
            elif lineCount > 2:
                menus[len(menus)-1].append(line.strip().split("mno_"))
            lineCount += 1
    return menus


def writeMenuOption(f, idx : str, mno : list):
    idx2 = idx + "_" + mno[0]
    conditionalCode = mno[1].split(' ')
    text = mno[2].replace("_"," ")
    codex = mno[3].split(' ')
    doorText = mno[4].replace("_"," ")

    f.write(idx2 + " = MenuOption(\"" + mno[0] + "\", \"" + text + "\")")
    if doorText.strip() != ".":
        f.write(" # " + doorText)
    f.write("\n")

    datac = decompileCode(conditionalCode)
    datap, scriptParams = codeT.convertToPy(datac)
    txt = codeT.formatGoodText(datap, False, True)

    if len(txt.strip()) > 0:
        f.write("def condition(" + ", ".join(scriptParams) + "):\n")
        f.write(txt)
        f.write(idx2 + ".conditionBlock = condition\n")

    datac = decompileCode(codex)
    datap, scriptParams = codeT.convertToPy(datac)
    txt = codeT.formatGoodText(datap, False, True)

    if len(txt.strip()) > 0:
        f.write("def code(" + ", ".join(scriptParams) + "):\n")
        f.write(txt)
        f.write(idx2 + ".codeBlock = code\n")

    f.write("\n")


def decompileCode(tmp : list):
    data = []
    activeCount = -1
    codeT.localVarDict.clear()
    for i in range(1, len(tmp)):
        if activeCount <= 0:
            itmp = int(tmp[i])

            if (itmp & 0x40000000) == 0x40000000: # this_or_next
                vv = str(itmp & 0xFFFF)
                if vv in codeT.operations:
                    newData = "this_or_next|" + codeT.operations[vv] + ","
                else:
                    newData = "this_or_next|UNKNOWN_OP_" + vv + ","
            elif (itmp & 0x80000000) == 0x80000000: # neg
                vv = str(itmp & 0xFFFF)
                if vv in codeT.operations:
                    newData = "neg|" + codeT.operations[vv] + ","
                else:
                    newData = "neg|UNKNOWN_OP_" + vv + ","
            elif tmp[i] in codeT.operations:
                newData = codeT.operations[tmp[i]] + ","
            else:
                newData = "UNKNOWN_OP_" + tmp[i] + ","

            activeCount = int(tmp[i+1]) + 1
            lll = 0
            stx = i + 2
            enx = i + 1 + activeCount
            for ix in range(stx, enx):
                newData += codeT.lookupData(newData.split(',')[0], tmp[ix], tmp[ix+1:enx], data, lll) + ","
                lll += 1
            newData = newData.rstrip(',')
            data.append(newData)
        else:
            activeCount -= 1
    return data


def writeMenu(f, menu : list):
    idx = menu[0][0]
    flagsx = menu[0][1]
    description = menu[0][2].replace("_"," ")
    meshName = menu[0][3]
    conditionalCode = menu[0][4:]
    conditionalCode.pop() # last is count for menu options

    f.write(idx + " = GameMenu(\"" + idx + "\", " + flagsx + ",\n\"" + description + "\"")

    if meshName.strip() != "none":
        f.write(",\n\"" + meshName + "\"")

    f.write("\n)\n")

    datac = decompileCode(conditionalCode)
    datap, scriptParams = codeT.convertToPy(datac)
    txt = codeT.formatGoodText(datap, False, True)

    if len(txt.strip()) > 0:
        f.write("def condition(" + ", ".join(scriptParams) + "):\n")
        f.write(txt)
        f.write(idx + ".conditionBlock = condition\n")

    f.write("\n")

    if len(menu[1]) > 1:
        menuOptions = menu[1][1:]
        for mno in menuOptions:
            writeMenuOption(f, idx, mno.split("  "))

    f.write("\n\n")


if __name__ == "__main__":
    menusx = readMenus()
    with open("test_menus.py", "w") as f:
        for mnu in menusx:
            writeMenu(f, mnu)


