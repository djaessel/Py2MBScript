# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../modules/")
sys.path.append("../build_system/")
sys.path.append("../data_objects/")

import header_triggers as triHeader
import header_scene_props as scpHeader
import scene_prop as scpData
import CodeTranslator as codeT


module_path = "/home/djaessel/warband/Modules/Native/"




def readSceneProps():
    sceneProps = []
    with open(module_path + "scene_props.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("spr_"):
                tmp = line.strip().split(' ')
                sceneProps.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                sceneProps[len(sceneProps)-1].append(line.strip().split(' '))
            lineCount += 1
    return sceneProps


def getFlags(x: int):
    flagsx = []
    final_flags = []
    hit_points = 0
    use_time = 0
    if int(x) > 0:
        item_consts = dict()
        for i in vars(scpHeader):
            if i.startswith("sokf_"):
                item_consts[i] = getattr(scpHeader,i)
        for t in item_consts:
            v = item_consts[t]
            if (v & scpHeader.sokf_type_mask) > 0:
                if (x & scpHeader.sokf_type_mask) == v:
                    flagsx.append(t)
            elif (x & v) == v:
                flagsx.append(t)

        hit_points = (x >> scpHeader.spbf_hit_points_bits) & 0xff
        use_time = (x >> scpHeader.spbf_use_time_bits) & 0xff

        mapx = None
        for tfx in vars(scpData):
            if "ScenePropFlag" in tfx:
                atx = getattr(scpData,tfx)
                for lll in vars(atx):
                    if lll == "_value2member_map_":
                        mapx = getattr(atx, lll)
                        break
                break

        if mapx != None:
            for itcf in flagsx:
                if itcf in mapx:
                    final_flags.append(str(mapx[itcf]))
                else:
                    print("WARNING: Ignored sokf >", itcf)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags, hit_points, use_time


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


def writeSceneProp(f, scene_prop : list):
    idx = scene_prop[0][0][4:]

    f.write(idx + " = SceneProp(\"" + idx + "\", \"" + scene_prop[0][3] + "\", \"" + scene_prop[0][4] + "\")\n")

    flagsx, hit_points, use_time = getFlags(int(scene_prop[0][1]))
    for fl in flagsx:
        f.write(idx + ".add_flag(" + fl + ")\n")

    if hit_points > 0:
        f.write(idx + ".set_hit_points(" + str(hit_points) + ")\n")

    if use_time:
        f.write(idx + ".set_use_time(" + str(use_time) + ")\n")

    triggerCount = int(scene_prop[0][5])
    if triggerCount > 0:
        for tr in range(1, triggerCount + 1):
            intervalCode, datac = convertItemTrigger(" ".join(scene_prop[tr]))
            f.write("# trigger" + str(tr-1) + "\n")
            f.write("trigger" + str(tr-1) + " = SimpleTrigger(" + intervalCode + ")\n")
            datap, scriptParams = codeT.convertToPy(datac)
            f.write("def code(" + ", ".join(scriptParams) + "):\n")
            txt = codeT.formatGoodText(datap, False, True)
            f.write(txt)
            f.write("trigger" + str(tr-1) + ".codeBlock = code\n")
            f.write(idx + ".add_trigger(trigger" + str(tr-1) + ")\n")

    f.write("\n")


if __name__ == "__main__":
    sceneProps = readSceneProps()
    with open("test_scene_props.py", "w") as f:
        for scp in sceneProps:
            writeSceneProp(f, scp)



