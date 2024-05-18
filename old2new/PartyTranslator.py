# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../build_system/")
sys.path.append("../data_objects/")
sys.path.append("../modules/")

import header_parties as pHeader
import MBParty as pData
import CodeTranslator as codeT


module_path = "/home/djaessel/warband/Modules/Native/"

bignum = 0x400000000000000000000000000000000


def processFlags(x : int):
    flags = []
    final_flags = []
    icon = 0
    carry_goods = 0
    carry_gold = 0
    if int(x) >= 0:
        consts = dict()
        for i in vars(pHeader):
            if i.startswith("pf_"):
                consts[i] = getattr(pHeader,i)
        for t in consts:
            v = consts[t]
            if (x & v) == v and not "pf_carry_" in t:
                flags.append(t)

        if (x & pHeader.pf_icon_mask) > 0:
            icon = x & pHeader.pf_icon_mask

        if (x & pHeader.pf_carry_goods_mask) > 0:
            carry_goods = ((bignum | x) & pHeader.pf_carry_goods_mask) >> pHeader.pf_carry_goods_bits

        if (x & pHeader.pf_carry_gold_mask) > 0:
            carry_gold = ((bignum | x) & pHeader.pf_carry_gold_mask) >> pHeader.pf_carry_gold_bits
            carry_gold *= 20 # maybe old_mul

        mapx = None
        for tfx in vars(pData):
            if "PartyFlag" in tfx:
                atx = getattr(pData,tfx)
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
                    print("WARNING: Ignored pf >", y)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags, icon, carry_goods, carry_gold


def writeParty(f, party : list):
    idx = party[0][3][2:]
    name = party[0][4].replace("_"," ")

    f.write(idx + " = MBParty(\"" + idx + "\", name=\"" + name + "\"")

    menuIndex = int(party[0][6])
    if menuIndex > 0:
        f.write(", menu=mnu." + codeT.menus[menuIndex][0][0][4:])

    partTemplateIndex = int(party[0][7])
    if partTemplateIndex > 0:
        f.write(", template=pt." + codeT.partyTemplates[partTemplateIndex][0][0][3:])

    factionIndex = int(party[0][8])
    if factionIndex > 0:
        f.write(", faction=fac." + codeT.factions[factionIndex][0][0][4:])

    personality = int(party[0][9]) # and 10
    if personality > 0:
        # TODO: get actual personality "text"
        f.write(", personality=\"" + str(personality) + "\"")

    initialCordsX = float(party[0][18]) # 16, 14
    initialCordsY = float(party[0][19]) # 17, 15 + 0.0 at 20
    if initialCordsX != 0.000000 or initialCordsY != 0.000000:
        f.write(", initial_cords=(" + str(initialCordsX) + ", " + str(initialCordsY) + ")")

    direction = round(float(party[1][0]) / (3.1415926 / 180.0), 4)
    if direction != 0.000000:
        f.write(", direction=" + str(direction))

    f.write(")\n")

    flagsx, icon, carry_goods, carry_gold = processFlags(int(party[0][5]))
    for fl in flagsx:
        f.write(idx + ".add_flag(" + fl + ")\n")

    if icon > 0:
        f.write(idx + ".set_icon(icon." + codeT.icons[icon][0][0] + ")\n")

    if carry_gold > 0:
        print("WARNING! CARRY_GOLD:", carry_gold, "ignored!")

    if carry_goods > 0:
        print("WARNING! CARRY_GOODS:", carry_goods, "ignored!")

    ai_behavior = int(party[0][11])
    ai_target = int(party[0][12]) # and 13
    if ai_behavior > 0:
        f.write(idx + ".set_ai_behavior(" + str(ai_behavior) + ")\n")

    if ai_target > 0:
        f.write(idx + ".set_ai_object(" + str(ai_target) + ")\n")

    memberCount = int(party[0][21])
    if memberCount > 0:
        for i in range(22, memberCount * 4 + 22, 4):
            flagx = int(party[0][i + 3])
            troopIndex = int(party[0][i])
            troopCount = int(party[0][i + 1])
            if flagx == 0:
                f.write(idx + ".add_members(trp." + codeT.troops[troopIndex][0][0][4:] + ", " + str(troopCount))
            else:
                f.write(idx + ".add_prisoners(trp." + codeT.troops[troopIndex][0][0][4:] + ", " + str(troopCount))
            f.write(")\n")

    f.write("\n\n")



if __name__ == "__main__":
    with open("test_parties.py", "w") as f:
        for p in codeT.parties:
            writeParty(f, p)

