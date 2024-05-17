# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../build_system/")
sys.path.append("../data_objects/")

import header_music as musHeader
import music as musData


module_path = "/home/djaessel/warband/Modules/Native/"


def readTracks():
    tracks = []
    with open(module_path + "music.txt") as f:
        lineCount = 0
        for line in f:
            if lineCount > 0:
                tmp = line.strip().split(' ')
                tracks.append(tmp)
            lineCount += 1
    return tracks


def processFlags(x : int):
    flags = []
    final_flags = []
    if int(x) >= 0:
        consts = dict()
        for i in vars(musHeader):
            if i.startswith("mtf_"):
                consts[i] = getattr(musHeader,i)
        for t in consts:
            v = consts[t]
            if (x & v) == v:
                flags.append(t)

        mapx = None
        for tfx in vars(musData):
            if "TrackFlag" in tfx:
                atx = getattr(musData,tfx)
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


def writeTrack(f, track : list):
    idx = track[0].split('.')[0]
    f.write(idx + " = MusicTrack(\"" + idx + "\", \"" + track[0] + "\")\n")

    flagsx = int(track[1])
    cflagsx = int(track[2]) ^ flagsx
    flags = processFlags(flagsx)
    continueFlags = processFlags(cflagsx)

    for fl in flags:
        f.write(idx + ".add_flag(" + fl + ")\n")

    for fl in continueFlags:
        f.write(idx + ".add_continue_flag(" + fl + ")\n")

    f.write("\n\n")


if __name__ == "__main__":
    tracks = readTracks()
    with open("test_music.py", "w") as f:
        for tr in tracks:
            writeTrack(f, tr)

