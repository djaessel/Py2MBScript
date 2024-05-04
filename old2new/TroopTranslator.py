

module_path = "/home/djaessel/warband/Modules/Native/"

MAIN_VALS = 0
NAME = 0
PLURAL_NAME = 1
DIALOG_IMAGE = 2
FLAGS = 3
SCENE_CODE = 4
RESERVED = 5
FACTION_ID = 6
UPGRADE_TROOP_1 = 7
UPGRADE_TROOP_2 = 8

ITEMS = 1

STATS = 2
STRENGTH = 0
AGILITY = 1
INTELLIGENCE = 2
CHARISMA = 3
LEVEL = 4

PROFICIENCIES = 3

SKILLS = 4

FACES = 5



factions = []
def readFactions():
    with open(module_path + "factions.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("fac_") or " fac_" in line:
                tmp = line.strip().split(' ')
                if not line.startswith("fac_"):
                    factions[len(factions)-1].append(tmp[0])
                    factions.append([tmp[1:]])
                else:
                    factions.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                factions[len(factions)-1].append(line.strip().split(' '))
            lineCount += 1


items = []
def readItems():
    with open(module_path + "item_kinds1.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith(" itm_"):
                tmp = line.strip().split(' ')
                tmp[0] = tmp[0].lstrip()
                items.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                items[len(items)-1].append(line.strip().split(' '))
            lineCount += 1


def readTroopsFile():
    troops = dict()
    with open(module_path + "troops.txt") as f:
        lineCount = 0
        curTroopId = ""
        for line in f:
            if lineCount > 1:
                tmp = line.strip().split(' ')
                if tmp[0].startswith("trp_"):
                    troops[tmp[0]] = [tmp[1:]]
                    curTroopId = tmp[0]
                else:
                    troops[curTroopId].append(tmp)
            lineCount += 1
    return troops


def getItems(troop : list):
    itemsx = []
    for i in range(0, len(troop[ITEMS]), 2):
        item_code = int(troop[ITEMS][i])
        item_points = int(troop[ITEMS][i+1])
        if item_code >= 0:
            itemsx.append((item_code, item_points))
    return itemsx
            

def getStats(troop : list):
    stats = troop[STATS]
    return stats


def getProficiencies(troop : list):
    profs = troop[PROFICIENCIES]
    return profs


def getFaceCodes(troop : list):
    faceCodes = ["",""]
    # TODO: convert data from troop[FACES]
    return faceCodes


def getSkills(troop : list):
    skillsx = []
    # TODO: convert data from troop[SKILLS]
    return skillsx


def writeTroop(idx : str, troop : list):
    with open("test_troop.py", "a") as f:
        mainVals = troop[MAIN_VALS]
        f.write(idx + " = Troop(\"" + idx + "\", \"" + mainVals[NAME] + "\", ") #"\", \"" + mainVals[PLURAL_NAME] + "\")")

        stats = getStats(troop)
        f.write("strength=" + stats[STRENGTH] + ", agility=" + stats[AGILITY] + ", intelligence=" + stats[INTELLIGENCE] + ", charisma=" + stats[CHARISMA] + ", level=" + stats[LEVEL] + ", ")

        faction = mainVals[FACTION_ID]
        f.write("faction=fac." + factions[int(faction)][0][0][4:] + ", ")

        faceCodes = getFaceCodes(troop)
        f.write("face_code_1=\"" + faceCodes[0] + "\", face_code_2=\"" + faceCodes[1] + "\")")
        f.write("\n")

        profs = getProficiencies(troop)
        f.write(idx + ".wpex(" + ",".join(profs[0:6]) + ")\n")
        if int(profs[6]) > 0:
            f.write(idx + ".set_firearm(" + profs[6] + ")\n")

        flags = mainVals[FLAGS]
        if int(flags) > 0:
            f.write(idx + ".add_flags(" + hex(int(flags)) + ")\n")

        itemsx = getItems(troop)
        for itm in itemsx:
            f.write(idx + ".add_item(itm." + items[itm[0]][0][0][4:])
            if itm[1] > 0:
                f.write(", " + str(itm[1]))
            f.write(")\n")

        # TODO: Skills

        f.write("\n")
        


# init
readFactions()
readItems()

# main
troops = readTroopsFile()
print("Troops:", len(troops))

archer = troops["trp_tutorial_archer"]

writeTroop("trp_tutorial_archer", archer)




