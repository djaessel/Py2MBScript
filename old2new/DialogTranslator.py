# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../modules/")
sys.path.append("../build_system/")
sys.path.append("../data_objects/")

import header_dialogs as dlgHeader
import dialog as dlgData
import CodeTranslator as codeT


module_path = "/home/djaessel/warband/Modules/Native/"


def readDialogs():
    dialogs = []
    with open(module_path + "conversation.txt") as f:
        lineCount = 0
        for line in f:
            if lineCount > 1:
                tmp = line.strip().replace(" NO_TEXT", "NO_TEXT").split("  ")
                dialogs.append(tmp)
            lineCount += 1
    return dialogs


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


def get_talking_troop(x : int):
    tt = ""

    matchingTroop = False
    matchingParty = False
    if (dlgHeader.anyone & x) == dlgHeader.anyone:
        tt += "anyone|"
    else:
        matchingTroop = True

    if (0x0000F000 & x) > 0:
        y = 0x0000F000 & x
        if y == dlgHeader.repeat_for_factions:
            tt += "repeat_for_factions|"
        elif y == dlgHeader.repeat_for_parties:
            tt += "repeat_for_parties|"
        elif y == dlgHeader.repeat_for_troops:
            tt += "repeat_for_troops|"
        elif y == dlgHeader.repeat_for_100:
            tt += "repeat_for_100|"
        elif y == dlgHeader.repeat_for_1000:
            tt += "repeat_for_1000|"

    if (dlgHeader.plyr & x) == dlgHeader.plyr:
        tt += "plyr|"

    if (dlgHeader.party_tpl & x) == dlgHeader.party_tpl:
        tt += "party_tpl|"
        matchingParty = True
        matchingTroop = False

    if (dlgHeader.auto_proceed & x) == dlgHeader.auto_proceed:
        tt += "auto_proceed|"

    if (dlgHeader.multi_line & x) == dlgHeader.multi_line:
        tt += "multi_line|"

    if matchingParty:
        tt += codeT.partyTemplates[dlgHeader.anyone & x][0]
    elif matchingTroop:
        tt += codeT.troops[dlgHeader.anyone & x][0][0]

    tt = tt.rstrip('|')

    return tt


def writeDialog(f, dx : list):
    d = dx[0].split(' ')
    tmp1 = d[0].split('.')[0].split(':')

    idx1 = d[0][5:].replace(".","_").replace(":","_")
    talkingTroop = int(d[1])

    code_plus_text = dx[1].split(' ')
    text1 = code_plus_text[-1]
    code_plus_text.pop()

    output_states = int(dx[2])

    code_plus_voice = dx[3].split(' ')
    voice_over = code_plus_voice[-1]
    code_plus_voice.pop()

    trp_talker = get_talking_troop(talkingTroop)

    f.write(idx1 + " = Dialog(\"" + trp_talker + "\", \"" + text1.replace("_"," ") + "\", starting_state=\"" + tmp1[0][5:] + "\", ending_state=\"" + tmp1[1] + "\")\n")

    datac = decompileCode(code_plus_text)
    datap, scriptParams = codeT.convertToPy(datac)
    txt = codeT.formatGoodText(datap, False, True)

    if len(txt.strip()) > 0:
        f.write("def condition(" + ", ".join(scriptParams) + "):\n")
        f.write(txt)
        f.write(idx1 + ".conditionBlock = condition\n")

    datac = decompileCode(code_plus_voice)
    datap, scriptParams = codeT.convertToPy(datac)
    txt = codeT.formatGoodText(datap, False, True)

    if len(txt.strip()) > 0:
        f.write("def code(" + ", ".join(scriptParams) + "):\n")
        f.write(txt)
        f.write(idx1 + ".codeBlock = code\n")

    f.write("\n\n")



if __name__ == "__main__":
    dlgs = readDialogs()
    with open("test_dialogs.py", "w") as f:
        for d in dlgs:
            writeDialog(f, d)

