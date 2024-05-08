# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../build_system/")
sys.path.append("../data_objects/")

import header_skills as sklHeader
import skill as sklData


module_path = "/home/djaessel/warband/Modules/Native/"


def readSkills():
    skills = []
    with open(module_path + "skills.txt") as f:
        for line in f:
            if line.startswith("skl_"):
                tmp = line.strip().split(' ')
                skills.append(tmp)
    return skills


def processFlags(x : int):
    flags = []
    final_flags = []
    found_one = False
    if int(x) >= 0:
        consts = dict()
        for i in vars(sklHeader):
            if i.startswith("sf_"):
                consts[i] = getattr(sklHeader,i)
        for t in consts:
            v = consts[t]
            if (v & 0x0000000f) > 0:
                if (x & 0x0000000f) == v:
                    flags.append(t)
                    found_one = True
            elif v > 0 and (x & v) == v:
                flags.append(t)

        if not found_one:
            for t in consts:
                v = consts[t]
                if v == 0:
                    flags.append(t)

        mapx = None
        for tfx in vars(sklData):
            if "SkillFlag" in tfx:
                atx = getattr(sklData,tfx)
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
                    print("WARNING: Ignored sf >", y)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags


def writeSkill(skill : list):
    with open("test_skills.py", "a") as f:
        idx = skill[0][4:]

        f.write(idx + " = Skill(\"" + idx + "\", \"" + skill[1].replace("_", " ") + "\", " + skill[3] + ")\n")

        f.write(idx + ".set_description(\"" + skill[4].replace("_", " ") + "\")\n")

        flags = int(skill[2])
        flagsx = processFlags(flags)
        for fl in flagsx:
            f.write(idx + ".add_flag(" + fl + ")\n")

        f.write("\n")



if __name__ == "__main__":
    skills = readSkills()
    # print("Skills:", len(skills))
    for skl in skills:
        writeSkill(skl)
