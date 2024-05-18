# This Python file uses the following encoding: utf-8

import CodeTranslator as codeT


module_path = "/home/djaessel/warband/Modules/Native/"


def convertItemTrigger(triggerCode : str):
    tmpX = triggerCode.split("  ")
    intervalCode = float(tmpX[0])
    tmp = tmpX[1].split(' ')
    data = []
    codeT.localVarDict.clear()
    if len(tmp[0]) > 0:
        activeCount = -1
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

    return intervalCode, data


def writePresentation(f, presentation : list):
    idx = presentation[0][0][6:]

    f.write(idx + " = Presentation(\"" + idx + "\"")

    meshIndex = int(presentation[0][2])
    if meshIndex > 0:
        f.write(", mesh=mesh." + codeT.meshes[meshIndex][0][5:])
    f.write(")\n")

    flagsx = int(presentation[0][1])
    if (flagsx & 0x1) == 0x1:
        f.write(idx + ".set_read_only()\n")
    if (flagsx & 0x1) == 0x1:
        f.write(idx + ".set_manual_end_only()\n")

    triggerCount = int(presentation[0][3])
    if triggerCount > 0:
        for i in range(1, triggerCount + 1):
            intervalCode, datac = convertItemTrigger(" ".join(presentation[i]))
            f.write("event = ")
            if intervalCode == -60.0:
                f.write("Load")
            elif intervalCode == -61.0:
                f.write("Run")
            elif intervalCode == -62.0:
                f.write("StateChanged")
            elif intervalCode == -63.0:
                f.write("MouseEnterLeave")
            elif intervalCode == -64.0:
                f.write("MousePress")
            f.write("Event()\n")
            datap, scriptParams = codeT.convertToPy(datac)
            f.write("def code(" + ", ".join(scriptParams) + "):\n")
            txt = codeT.formatGoodText(datap, False, True)
            f.write(txt)
            f.write("event.codeBlock = code\n")
            f.write(idx + ".add_event(event)\n")

    f.write("\n\n")


if __name__ == "__main__":
    with open("test_presentations.py", "w") as f:
        for prnst in codeT.presentations:
            writePresentation(f, prnst)

