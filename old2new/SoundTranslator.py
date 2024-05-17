# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../build_system/")
sys.path.append("../data_objects/")

import header_sounds as sndHeader
import sound as sndData


module_path = "/home/djaessel/warband/Modules/Native/"


def readSounds():
    sounds = []
    soundFiles = []
    with open(module_path + "sounds.txt") as f:
        lineCount = 0
        for line in f:
            if lineCount > 1:
                tmp = line.strip().split(' ')
                if line.startswith("snd_"):
                    sounds.append(tmp)
                else:
                    soundFiles.append(tmp)
            lineCount += 1
    return sounds, soundFiles


def processFlags(x : int):
    volume = 0
    priority = 0
    flags = []
    final_flags = []
    if int(x) >= 0:
        consts = dict()
        for i in vars(sndHeader):
            if i.startswith("sf_"):
                consts[i] = getattr(sndHeader,i)
        for t in consts:
            v = consts[t]
            if (v & sndHeader.sf_vol_15) > 0:
                if (x & sndHeader.sf_vol_15) == v:
                    volume = (x & sndHeader.sf_vol_15) >> 8
            elif (v & sndHeader.sf_priority_15) > 0:
                if (x & sndHeader.sf_priority_15) == v:
                    priority = (x & sndHeader.sf_priority_15) >> 4
            elif v > 0 and (x & v) == v:
                flags.append(t)

        mapx = None
        for tfx in vars(sndData):
            if "SoundFlag" in tfx:
                atx = getattr(sndData,tfx)
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
    return final_flags, volume, priority


def writeSound(f, sound : list, soundFiles : list):
    idx = sound[0][4:]

    f.write(idx + " = Sound(\"" + idx + "\")\n")

    flagsx, volume, priority = processFlags(int(sound[1]))
    for fl in flagsx:
        f.write(idx + ".add_flag(" + fl + ")\n")

    if volume > 0:
        f.write(idx + ".set_volume(" + str(volume) + ")\n")

    if priority > 0:
        f.write(idx + ".set_priority(" + str(priority) + ")\n")

    fileCount = int(sound[2]) * 2
    if fileCount > 0:
        for i in range(0, fileCount, 2):
            fileIndex = int(sound[3 + i])
            fileFlags = int(sound[4 + i])
            if fileFlags > 0:
                print("WARNING: Ignoring sound flags >", fileIndex, fileFlags)
            f.write(idx + ".add_file(\"" + soundFiles[fileIndex][0] + "\")\n")

    f.write("\n\n")



if __name__ == "__main__":
    sounds, soundFiles = readSounds()
    with open("test_sounds.py", "w") as f:
        for snd in sounds:
            writeSound(f, snd, soundFiles)



