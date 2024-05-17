# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../modules/")
sys.path.append("../build_system/")
sys.path.append("../data_objects/")

import header_triggers as triHeader
import header_items as itmHeader
import item as itmData
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

    consts = dict()
    for i in vars(triHeader):
        if i.startswith("ti_"):
            consts[i] = getattr(triHeader,i)
    for t in consts:
        v = consts[t]
        if intervalCode == v:
            intervalCode = "tri." + t
            break

    return str(intervalCode), data


def writeMapIcon(f, mapIcon : list):
    idx = mapIcon[0][0]
    meshName = mapIcon[0][2]
    scale = float(mapIcon[0][3])

    # player = MapIcon("player", mesh_name="player", scale=__avatar_scale__, sound=snd.footstep_grass)
    f.write(idx + " = MapIcon(\"" + idx + "\", mesh_name=\"" + meshName + "\", scale=" + str(scale))

    # flags
    if int(mapIcon[0][1]) == 1:
        f.write(", no_shadow=True")

    soundIndex = int(mapIcon[0][4])
    if soundIndex > 0:
        f.write(", sound=snd." + codeT.sounds[soundIndex][0][4:])

    offset_x = float(mapIcon[0][5])
    offset_y = float(mapIcon[0][6])
    offset_z = float(mapIcon[0][7])
    if offset_x != 0 or offset_y != 0 or offset_z != 0:
        f.write(", offset_x=" + str(offset_x))
        f.write(", offset_y=" + str(offset_y))
        f.write(", offset_z=" + str(offset_z))

    f.write(")\n")

    triggerCount = int(mapIcon[0][8])
    if triggerCount > 0:
        for i in range(triggerCount):
            intervalCode, datac = convertItemTrigger(" ".join(mapIcon[i+1]))
            f.write("# trigger" + str(i) + "\n")
            f.write("trigger" + str(i) + " = SimpleTrigger(" + intervalCode + ")\n")
            datap, scriptParams = codeT.convertToPy(datac)
            f.write("def code(" + ", ".join(scriptParams) + "):\n")
            txt = codeT.formatGoodText(datap, False, True)
            f.write(txt)
            f.write("trigger" + str(i) + ".codeBlock = code\n")
            f.write(idx + ".add_trigger(trigger" + str(i) + ")\n")
        f.write("\n")

    f.write("\n")


if __name__ == "__main__":
    with open("test_map_icons.py", "w") as f:
        for icon in codeT.icons:
            writeMapIcon(f, icon)
