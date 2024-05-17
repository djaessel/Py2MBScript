# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../modules/")
sys.path.append("../build_system/")
sys.path.append("../data_objects/")


import CodeTranslator as codeT


module_path = "/home/djaessel/warband/Modules/Native/"


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


def readTableaus():
    tableaus = []
    with open(module_path + "tableau_materials.txt") as f:
        for line in f:
            if line.startswith("tab_"):
                tmp = line.strip().split(' ')
                tableaus.append(tmp)
    return tableaus


def writeTableau(f, tableau : list):
    idx = tableau[0][4:]
    resourceName = tableau[2]

    f.write(idx + " = TableauMaterial(\"" + idx + "\", \"" + resourceName + "\"")
    f.write(", " + tableau[3])
    f.write(", " + tableau[4])
    f.write(", " + tableau[5])
    f.write(", " + tableau[6])
    f.write(", " + tableau[7])
    f.write(", " + tableau[8])
    f.write(")\n")

    code = tableau[9:]
    datac = decompileCode(code)
    datap, scriptParams = codeT.convertToPy(datac)
    txt = codeT.formatGoodText(datap, False, True)

    if len(txt.strip()) > 0:
        f.write("def code(" + ", ".join(scriptParams) + "):\n")
        f.write(txt)
        f.write(idx + ".codeBlock = code\n")

    f.write("\n\n")


if __name__ == "__main__":
    tableaus = readTableaus()
    with open("test_tableaus.py", "w") as f:
        for tab in tableaus:
            writeTableau(f, tab)
