# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../build_system/")

import header_factions as facHeader


module_path = "/home/djaessel/warband/Modules/Native/"


def readFactions():
    factions = []
    with open(module_path + "factions.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("fac_") or " fac_" in line:
                tmp = line.strip().replace("  ", " ").split(' ')
                if not line.startswith("fac_"):
                    factions[len(factions)-1].append(tmp[0])
                    factions.append([tmp[1:]])
                else:
                    factions.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                factions[len(factions)-1].append(line.strip().replace("  ", " ").split(' '))
            lineCount += 1
    return factions


def writeFaction(faction : list, index : int):
    with open("test_factions.py", "a") as f:
        mainVals = faction[0]
        relations = faction[1]
        ranksCount = faction[2]

        idx = mainVals[0][4:]

        f.write(idx + " = Faction(\"" + idx + "\", \"" + mainVals[1] + "\"")

        coherence = float(relations[index])
        if coherence != 0.1:
            f.write(", coherence=" + str(coherence))

        color = int(mainVals[3])
        if color != 0xaaaaaa:
            f.write(", color=" + hex(color))

        flagsGZ = int(mainVals[2])
        if (flagsGZ & facHeader.ff_always_hide_label) == facHeader.ff_always_hide_label:
            f.write(", always_hide_label=True")

        if (flagsGZ & facHeader.ff_max_rating_mask) > 0:
            max_player_rating = (flagsGZ & facHeader.ff_max_rating_mask) >> facHeader.ff_max_rating_bits
            f.write(", max_player_rating=" + str(max_player_rating))

        f.write(")\n")

        f.write("\n")


if __name__ == "__main__":
    factions = readFactions()
    for i, fac in enumerate(factions):
        writeFaction(fac, i)

    # TODO: relations



