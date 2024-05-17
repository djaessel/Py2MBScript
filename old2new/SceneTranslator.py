# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../build_system/")
sys.path.append("../data_objects/")

import header_scenes as scnHeader
import scene as scnData


module_path = "/home/djaessel/warband/Modules/Native/"


troops = []
def readTroops():
    with open(module_path + "troops.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("trp_"):
                tmp = line.strip().split(' ')
                troops.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                troops[len(troops)-1].append(line.strip().split(' '))
            lineCount += 1


def readScenes():
    scenes = []
    with open(module_path + "scenes.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("scn_"):
                tmp = line.strip().split(' ')
                scenes.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                scenes[len(scenes)-1].append(line.strip().split("  "))
            lineCount += 1
    return scenes


def processFlags(x : int):
    flags = []
    final_flags = []
    if x >= 0:
        consts = dict()
        for i in vars(scnHeader):
            if i.startswith("sf_"):
                consts[i] = getattr(scnHeader,i)
        for t in consts:
            v = consts[t]
            if (x & v) == v:
                flags.append(t)

        mapx = None
        for tfx in vars(scnData):
            if "SceneFlag" in tfx:
                atx = getattr(scnData,tfx)
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


def writeScene(f, scene : list, scenes : list):
    idx = scene[0][0][4:]

    f.write(idx + " = Scene(\"" + idx + "\"")

    meshName = scene[0][3]
    bodyName = scene[0][4]
    water_level = float(scene[0][9])
    terrain_code = scene[0][10]
    extra_terrain = scene[3][0]

    if meshName != "none":
        f.write(", mesh_name=\"" + meshName + "\"")

    if bodyName != "none":
        f.write(", body_name=\"" + bodyName + "\"")

    if water_level != -100.000000:
        f.write(", water_level=" + str(water_level))

    if terrain_code != "0":
        f.write(", terrain_code=\"" + terrain_code + "\"")

    if extra_terrain != "0":
        f.write(", extra_terrain=\"" + extra_terrain + "\"")

    f.write(")\n")


    flags = processFlags(int(scene[0][2]))
    for fl in flags:
        f.write(idx + ".add_flag(" + fl + ")\n")

    minPosX = float(scene[0][5])
    minPosY = float(scene[0][6])
    if minPosX != 0.000000 or minPosY != 0.000000:
        f.write(idx + ".set_min_pos(" + str(minPosX) + ", " + str(minPosY) + ")\n")

    maxPosX = float(scene[0][7])
    maxPosY = float(scene[0][8])
    if maxPosX != 100.000000 or maxPosY != 100.000000:
        f.write(idx + ".set_min_pos(" + str(maxPosX) + ", " + str(maxPosY) + ")\n")

    x = int(scene[1][0])
    if x > 0:
        for i in range(1, x + 1):
            y = int(scene[1][i])
            if y > 0:
                if y == 100000:
                    z = "\"exit\""
                else:
                    z = "scn." + scenes[y][0][0][4:]
                f.write(idx + ".add_accessible_scene(" + z + ")\n")

    x = int(scene[2][0])
    if x > 0:
        for i in range(1, x + 1):
            y = int(scene[2][i])
            if y > 0:
                f.write(idx + ".add_chest_troop(trp." + troops[y][0][0][4:] + ")\n")

    f.write("\n\n")



if __name__ == "__main__":
    readTroops()
    scenes = readScenes()
    with open("test_scenes.py", "w") as f:
        for scn in scenes:
            writeScene(f, scn, scenes)
