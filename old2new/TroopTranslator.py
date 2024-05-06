
import sys
sys.path.append("../build_system/")
sys.path.append("../data_objects/")
sys.path.append("../modules/")

import header_troops as trpHeader
import header_skills as sklHeader
import skills as sklModule
import troop as trpData


module_path = "/home/djaessel/warband/Modules/Native/"

MAIN_VALS = 0
NAME = 0
PLURAL_NAME = 1 # TODO: add this if needed
DIALOG_IMAGE = 2 # TODO: add this
FLAGS = 3
SCENE_CODE = 4 # TODO: add this
RESERVED = 5 # TODO: add this if needed
FACTION_ID = 6
UPGRADE_TROOP_1 = 7 # TODO: add this
UPGRADE_TROOP_2 = 8 # TODO: add this

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
    faceCodes = [0, 0]
    for i in range(4):
        faceCodes[0] |= int(troop[FACES][i]) << (i * 64)
    for i in range(4):
        faceCodes[1] |= int(troop[FACES][i+4]) << (i * 64)
    return faceCodes


def getSkillsPrepare(troop : list):
    skill_array = 0
    skillsx = troop[SKILLS]
    for i, sklVal in enumerate(skillsx):
        skill_array |= int(sklVal) << (i * 32)
    return skill_array


def containsSkillAlreadyCheck(skill_name : str, skill_val : int, skillsx : list):
    delx = []
    for i, s in enumerate(skillsx):
        if s[0] == skill_name:
            if int(s[1]) < skill_val:
                delx.append(i)
            else:
                return False

    delx.reverse()
    for i in delx:
        del skillsx[i]
    return True


def getSkills(troop : list):
    skillsx = []
    skill_array = getSkillsPrepare(troop)

    skill_consts = dict()
    for i in vars(sklHeader):
        if i.startswith("knows_"):
            skill_consts[i] = getattr(sklHeader,i)

    for s in skill_consts:
        v = skill_consts[s]
        if (skill_array & v) == v:
            tmp = s.split('_')
            skill_val = tmp[-1]
            tmp.pop()
            skill_name = "_".join(tmp)
            canAdd = containsSkillAlreadyCheck(skill_name, int(skill_val), skillsx)
            if canAdd:
                skillsx.append((skill_name, skill_val))

    final_skillx = []
    for skillx in vars(sklModule):
        ssss = getattr(sklModule, skillx)
        if "skill.Skill object" in str(ssss):
            for x in skillsx:
                if x[0] == "knows_" + ssss.id:
                    final_skillx.append(("skl." + skillx, x[1]))

    return final_skillx


def getFlags(troop : list):
    flagsx = []
    final_flags = []
    flags = int(troop[MAIN_VALS][FLAGS])
    if int(flags) > 0:
        troop_consts = dict()
        for i in vars(trpHeader):
            if i.startswith("tf_"):
                troop_consts[i] = getattr(trpHeader,i)
        for t in troop_consts:
            v = troop_consts[t]
            if (flags & v) == v:
                flagsx.append(t)

        mapx = None
        for tfx in vars(trpData):
            if "TroopFlag" in tfx:
                atx = getattr(trpData,tfx)
                for lll in vars(atx):
                    if lll == "_value2member_map_":
                        mapx = getattr(atx, lll)
                        break
                break

        if mapx != None:
            for tf in flagsx:
                if tf in mapx:
                    final_flags.append(str(mapx[tf]))
                else:
                    print("WARNING: Ignored tf >", tf)
        else:
            print("ERROR: MAPX EMPTY!")

    return final_flags


def writeTroop(idx : str, troop : list):
    with open("test_troop.py", "a") as f:
        mainVals = troop[MAIN_VALS]

        f.write("# " + mainVals[NAME] + "\n")
        f.write(idx + " = Troop(\"" + idx + "\", name=\"" + mainVals[NAME].replace("_"," ") + "\", ") #"\", plural_name=\"" + mainVals[PLURAL_NAME] + "\")")

        stats = getStats(troop)
        f.write("strength=" + stats[STRENGTH] + ", agility=" + stats[AGILITY] + ", intelligence=" + stats[INTELLIGENCE] + ", charisma=" + stats[CHARISMA] + ", level=" + stats[LEVEL] + ", ")

        faction = mainVals[FACTION_ID]
        f.write("faction=fac." + factions[int(faction)][0][0][4:] + ", ")

        faceCodes = getFaceCodes(troop)
        f.write("face_code_1=\"" + hex(faceCodes[0]) + "\", face_code_2=\"" + hex(faceCodes[1]) + "\")")
        f.write("\n")

        f.write("# proficiencies\n")
        profs = getProficiencies(troop)
        f.write(idx + ".wpex(" + ",".join(profs[0:6]) + ")\n")
        if int(profs[6]) > 0:
            f.write(idx + ".set_firearm(" + profs[6] + ")\n")

        f.write("# flags\n")
        flags = getFlags(troop)
        for fl in flags:
            f.write(idx + ".add_flag(" + fl + ")\n")

        f.write("# items\n")
        itemsx = getItems(troop)
        for itm in itemsx:
            f.write(idx + ".add_item(itm." + items[itm[0]][0][0][4:])
            if itm[1] > 0:
                f.write(", " + str(itm[1]))
            f.write(")\n")

        f.write("# skills\n")
        skillsx = getSkills(troop)
        for s in skillsx:
            f.write(idx + ".add_skill(" + s[0] + ", " + s[1] + ")\n")

        f.write("\n\n")
        


# main program
if __name__ == "__main__":
    # init
    readFactions()
    readItems()

    # main
    troops = readTroopsFile()
    print("Troops:", len(troops))

    troopx = ""
    if len(sys.argv) > 1:
        troopx = sys.argv[1]
        archer = troops[troopx]
        writeTroop(troopx, archer)
    else: # all
        for t in troops:
            writeTroop(t, troops[t])



