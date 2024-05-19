# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../modules/")
sys.path.append("../build_system/")
sys.path.append("../data_objects/")

import header_triggers as triHeader
import header_mission_templates as mtHeader
import mission_template as mtData
import CodeTranslator as codeT


module_path = "/home/djaessel/warband/Modules/Native/"


def processFlags(x : int):
    flags = []
    final_flags = []
    if int(x) >= 0:
        consts = dict()
        for i in vars(mtHeader):
            if i.startswith("mtf_"):
                consts[i] = getattr(mtHeader,i)
        for t in consts:
            v = consts[t]
            if (x & v) == v:
                flags.append(t)

        mapx = None
        for tfx in vars(mtData):
            if "MissionTemplateFlag" in tfx:
                atx = getattr(mtData,tfx)
                for lll in vars(atx):
                    if lll == "_value2member_map_":
                        mapx = getattr(atx, lll)
                        break
                break

        if mapx != None:
            for y in flags:
                if y in mapx:
                    final_flags.append(str(mapx[y]))
                else:
                    print("WARNING: Ignored mtf >", y)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags


def processSpawnFlags(x : int):
    flags = []
    final_flags = []
    if int(x) >= 0:
        consts = dict()
        for i in vars(mtHeader):
            if i.startswith("mtef_"):
                consts[i] = getattr(mtHeader,i)
        for t in consts:
            v = consts[t]
            if (x & v) == v:
                flags.append(t)

        mapx = None
        for tfx in vars(mtData):
            if "SpawnFlag" in tfx:
                atx = getattr(mtData,tfx)
                for lll in vars(atx):
                    if lll == "_value2member_map_":
                        mapx = getattr(atx, lll)
                        break
                break

        if mapx != None:
            for y in flags:
                if y in mapx:
                    final_flags.append(str(mapx[y]))
                else:
                    print("WARNING: Ignored mtef >", y)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags


def processAlterFlags(x : int):
    flags = []
    final_flags = []
    if int(x) >= 0:
        consts = dict()
        for i in vars(mtHeader):
            if i.startswith("af_"):
                consts[i] = getattr(mtHeader,i)
        for t in consts:
            v = consts[t]
            if (x & v) == v:
                flags.append(t)

        mapx = None
        for tfx in vars(mtData):
            if "AlterFlag" in tfx:
                atx = getattr(mtData,tfx)
                for lll in vars(atx):
                    if lll == "_value2member_map_":
                        mapx = getattr(atx, lll)
                        break
                break

        if mapx != None:
            for y in flags:
                if y in mapx:
                    final_flags.append(str(mapx[y]))
                else:
                    print("WARNING: Ignored af >", y)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags


def processAiFlags(x : int):
    flags = []
    final_flags = []
    if int(x) >= 0:
        consts = dict()
        for i in vars(mtHeader):
            if i.startswith("aif_") and not "_group_" in i:
                consts[i] = getattr(mtHeader,i)
        for t in consts:
            v = consts[t]
            if (x & v) == v:
                flags.append(t)

        mapx = None
        for tfx in vars(mtData):
            if "AIFlag" in tfx:
                atx = getattr(mtData,tfx)
                for lll in vars(atx):
                    if lll == "_value2member_map_":
                        mapx = getattr(atx, lll)
                        break
                break

        if mapx != None:
            for y in flags:
                if y in mapx:
                    final_flags.append(str(mapx[y]))
                else:
                    print("WARNING: Ignored aif >", y)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags


def writeSpawnRecord(f, id, spawnRecord : list):
    f.write("# spawn record " + str(id) + "\n")
    f.write("sr" + str(id) + " = SpawnRecord(entry_no=" + spawnRecord[0] + ", number_of_troops=" + spawnRecord[4] + ")\n")

    spawnflagsx = processSpawnFlags(int(spawnRecord[1]))
    for fl in spawnflagsx:
        f.write("sr" + str(id) + ".add_spawn_flag(" + fl + ")\n")

    alterflagsx = processAlterFlags(int(spawnRecord[2]))
    for fl in alterflagsx:
        f.write("sr" + str(id) + ".add_alter_flag(" + fl + ")\n")

    aiflagsx = processAiFlags(int(spawnRecord[3]))
    for fl in aiflagsx:
        f.write("sr" + str(id) + ".add_ai_flag(" + fl + ")\n")

    itemCount = int(spawnRecord[5])
    if itemCount > 0:
        for i in range(7, len(spawnRecord)):
            itemIndex = int(spawnRecord[i])
            f.write("sr" + str(id) + ".addItem(itm." + codeT.items[itemIndex][0][0][4:] + ")\n")


def codeconv(data : list, tmp : list):
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


def decompileTrigger(line : str):
    tmp = line.strip().split("  ")

    vals = tmp[0].split(' ')
    tmp2 = tmp[2].split(' ')
    tmp = tmp[1].split(' ')

    data = []
    data2 = []
    codeT.localVarDict.clear()
    codeconv(data, tmp)
    codeconv(data2, tmp2)

    return data, data2, vals


def writeMissionTemplate(f, mt : list):
    idx = mt[0][0][4:]
    description = mt[1][0].replace("_"," ")

    f.write(idx + " = MissionTemplate(\"" + idx + "\"")
    missionType = int(mt[0][4])
    if missionType >= 0:
        f.write(", missionType=" + str(missionType)) # TODO: later add actual type from headers
    if description != "":
        f.write(", description=\"" + description + "\"")
    f.write(")\n")

    flagsx = processFlags(int(mt[0][2]))
    for fl in flagsx:
        f.write(idx + ".add_flag(" + fl + ")\n")

    f.write("# ---\n")
    spawnRecordCount = int(mt[3][0])
    mt[3] = mt[3][1:]
    currentIndex = 3
    if spawnRecordCount > 0:
        currentIndex = spawnRecordCount + 3
        for i in range(3, currentIndex):
            writeSpawnRecord(f, i-3, mt[i])
        triggerCount = int(mt[currentIndex][0])
    else:
        triggerCount = int(mt[3][0])

    f.write("# ---\n")
    if triggerCount > 0:
        for i in range(currentIndex + 1, triggerCount + currentIndex + 1):
            datac, datac2, vals = decompileTrigger(" ".join(mt[i]))
            f.write("# trigger " + str(i - currentIndex - 1) + "\n")
            f.write("trigger" + str(i - currentIndex - 1) + " = Trigger(" + vals[0] + ", " + vals[1] + ", " + vals[2] + ")\n")

            datap, scriptParams = codeT.convertToPy(datac)
            txt = codeT.formatGoodText(datap, False, True)
            f.write("def condition(" + ", ".join(scriptParams) + "):\n")
            if len(txt.strip()) > 0:
                f.write(txt)
            else:
                f.write("    pass\n")
            f.write("trigger" + str(i - currentIndex - 1) + ".conditionBlock = condition\n")
            f.write("\n")

            datap, scriptParams = codeT.convertToPy(datac2)
            txt = codeT.formatGoodText(datap, False, True)
            f.write("def code(" + ", ".join(scriptParams) + "):\n")
            if len(txt.strip()) > 0:
                f.write(txt)
            else:
                f.write("    pass\n")
            f.write("trigger" + str(i - currentIndex - 1) + ".codeBlock = code\n")
            f.write(idx + ".add_trigger(trigger" + str(i - currentIndex - 1) + ")\n")

    f.write("\n\n")


if __name__ == "__main__":
    with open("test_mission_templates.py", "w") as f:
        for mt in codeT.missionTemplates:
            writeMissionTemplate(f, mt)

