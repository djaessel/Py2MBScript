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


def writePartyTemplate(f, partyTemplate : list):
    idx = partyTemplate[0][3:]
    name = partyTemplate[1]

    f.write(idx + " = PartyTemplate(\"" + idx + "\", \"" + name + "\"")

    menuIndex = int(partyTemplate[3])
    if menuIndex > 0:
        f.write(", menu=mnu." + codeT.menus[menuIndex][0][0][4:])

    factionIndex = int(partyTemplate[4])
    if factionIndex > 0:
        f.write(", faction=fac." + codeT.factions[factionIndex][0][0][4:])

    personality = int(partyTemplate[5])
    if personality > 0:
        # TODO: get actual personality "text"
        f.write(", personality=\"" + str(personality) + "\"")

    f.write(")\n")

    flagsx, icon, carry_goods, carry_gold = processFlags(int(partyTemplate[2]))
    for fl in flagsx:
        f.write(idx + ".add_flag(" + fl + ")\n")

    if icon > 0:
        f.write(idx + ".set_icon(icon." + codeT.icons[icon][0][0] + ")\n")

    if carry_gold > 0:
        f.write(idx + ".setCarriesGold(" + str(carry_gold) + ")\n")

    if carry_goods > 0:
        f.write(idx + ".setCarriesGoods(" + str(carry_goods) + ")\n")

    currentIndex = 6
    while int(partyTemplate[currentIndex]) >= 0:
        troopIndex = int(partyTemplate[currentIndex])
        minCount = int(partyTemplate[currentIndex + 1])
        maxCount = int(partyTemplate[currentIndex + 2])
        flagx = int(partyTemplate[currentIndex + 3])
        f.write(idx + ".addStack(trp." + codeT.troops[troopIndex][0][0][4:] + ", min=" + str(minCount))
        if maxCount >= 0:
            f.write(", max=" + str(maxCount))
        if flagx != 0:
            f.write(", are_prisoners=True")
        f.write(")\n")
        currentIndex += 4


    f.write("\n\n")



if __name__ == "__main__":
    with open("test_party_templates.py", "w") as f:
        for pt in codeT.partyTemplates:
            writePartyTemplate(f, pt)


