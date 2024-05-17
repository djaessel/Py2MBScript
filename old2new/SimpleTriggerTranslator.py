# This Python file uses the following encoding: utf-8

import sys

from CodeTranslator import *



def codeconv(data : list, tmp : list):
    activeCount = -1
    for i in range(1, len(tmp)):
        if activeCount <= 0:
            itmp = int(tmp[i])

            if (itmp & 0x40000000) == 0x40000000: # this_or_next
                vv = str(itmp & 0xFFFF)
                if vv in operations:
                    newData = "this_or_next|" + operations[vv] + ","
                else:
                    newData = "this_or_next|UNKNOWN_OP_" + vv + ","
            elif (itmp & 0x80000000) == 0x80000000: # neg
                vv = str(itmp & 0xFFFF)
                if vv in operations:
                    newData = "neg|" + operations[vv] + ","
                else:
                    newData = "neg|UNKNOWN_OP_" + vv + ","
            elif tmp[i] in operations:
                newData = operations[tmp[i]] + ","
            else:
                newData = "UNKNOWN_OP_" + tmp[i] + ","

            activeCount = int(tmp[i+1]) + 1
            lll = 0
            stx = i + 2
            enx = i + 1 + activeCount
            for ix in range(stx, enx):
                newData += lookupData(newData.split(',')[0], tmp[ix], tmp[ix+1:enx], data, lll) + ","
                lll += 1
            newData = newData.rstrip(',')
            data.append(newData)
        else:
            activeCount -= 1



def decompileTriggers():
    data_all = []
    vals_all = []
    with open(module_path + "simple_triggers.txt") as f:
        found = False
        lineCount = 0
        for line in f:
            if lineCount > 1:
                tmp = line.strip().split("  ")

                vals = tmp[0].split(' ')
                tmp = tmp[1].split(' ')

                data = []
                localVarDict.clear()
                codeconv(data, tmp)

                data_all.append(data)
                vals_all.append(vals)
            lineCount += 1

    return data_all, vals_all




# main program
if __name__ == "__main__":
    datacB, valsB = decompileTriggers()
    with open("test_simple_triggers.py", "w") as f:
        for i, datac in enumerate(datacB):
            f.write("simple_trigger" + str(i) + " = SimpleTrigger(" + str(float(valsB[i][0])) + ")\n")

            datap, scriptParams = convertToPy(datac)
            txt = formatGoodText(datap, False, True)
            f.write("def code(" + ", ".join(scriptParams) + "):\n")
            if len(txt.strip()) > 0:
                f.write(txt)
            else:
                f.write("    pass\n")
            f.write("simple_trigger" + str(i) + ".codeBlock = code\n")
            f.write("\n\n")


