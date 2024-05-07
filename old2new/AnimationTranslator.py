# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../build_system/")
sys.path.append("../modules/")
sys.path.append("../data_objects/")

import header_animations as animHeader
import animation as animData

module_path = "/home/djaessel/warband/Modules/Native/"


def is_float(data):
    try:
        _ = float(data)
    except:
        return False
    return True


def readAnimations():
    animations = []
    with open(module_path + "actions.txt") as f:
        lineCount = 0
        for line in f:
            if lineCount > 0:
                tmp = line.strip().replace("  ", " ").split(' ')
                if not is_float(tmp[0]):
                    animations.append([tmp])
                else:
                    animations[len(animations)-1].append(tmp)
            lineCount += 1
    return animations


def processMasterFlags(x : int):
    flags = []
    final_flags = []
    if int(x) > 0:
        consts = dict()
        for i in vars(animHeader):
            if i.startswith("amf_"):
                consts[i] = getattr(animHeader,i)
        for t in consts:
            v = consts[t]
            if (v & animHeader.amf_priority_mask) > 0:
                if (x & animHeader.amf_priority_mask) == v:
                    flags.append(t)
            elif (v & 0xf000) > 0:
                if (x & 0xf000) == v:
                    flags.append(t)
            elif (x & v) == v:
                flags.append(t)

        mapx = None
        for tfx in vars(animData):
            if "AnimationMasterFlag" in tfx:
                atx = getattr(animData,tfx)
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
                    print("WARNING: Ignored amf >", y)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags


def processFlags(x : int):
    flags = []
    final_flags = []
    anim_length = 0
    if int(x) > 0:
        consts = dict()
        for i in vars(animHeader):
            if i.startswith("acf_") and not i == "acf_anim_length":
                consts[i] = getattr(animHeader,i)
        for t in consts:
            v = consts[t]
            if (v & animHeader.acf_rot_vertical_mask) > 0:
                if (x & animHeader.acf_rot_vertical_mask) == v:
                    flags.append(t)
            elif (x & v) == v:
                flags.append(t)

        if (x & animHeader.acf_anim_length_mask) > 0:
            anim_length = (x & animHeader.acf_anim_length_mask) >> animHeader.acf_anim_length_bits

        mapx = None
        for tfx in vars(animData):
            if "AnimationFlag" in tfx:
                atx = getattr(animData,tfx)
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
                    print("WARNING: Ignored acf >", y)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags, anim_length


def processAnimationSequenceFlags(x : int):
    flags = []
    final_flags = []
    if int(x) > 0:
        consts = dict()
        for i in vars(animHeader):
            if i.startswith("arf_"):
                consts[i] = getattr(animHeader,i)
        for t in consts:
            v = consts[t]
            if (v & 0x000000ff) > 0:
                if (x & 0x000000ff) == v:
                    flags.append(t)
            elif (x & v) == v:
                flags.append(t)

        mapx = None
        for tfx in vars(animData):
            if "AnimationSequenceFlag" in tfx:
                atx = getattr(animData,tfx)
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
                    print("WARNING: Ignored arf >", y)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags


def extract4f(x : int):
    di = (x >> 24) & 0xff
    ci = (x >> 16) & 0xff
    bi = (x >> 8) & 0xff
    ai = x & 0xff

    di = round(float(di / 255.0), 2)
    ci = round(float(ci / 255.0), 2)
    bi = round(float(bi / 255.0), 2)
    ai = round(float(ai / 255.0), 2)

    return ai, bi, ci, di



def writeAnimation(animation : list):
    with open("test_animations.py", "a") as f:
        mainVals = animation[0]
        idx = mainVals[0]

        f.write("# " + idx + " Animation\n")
        f.write(idx + " = Animation(\"" + idx + "\"")

        flagsx, anim_length = processFlags(int(mainVals[1]))
        if anim_length > 0:
            f.write(", " + str(anim_length))
        f.write(")\n")

        for fl in flagsx:
            f.write(idx + ".add_flag(" + fl + ")\n")

        masterFlags = processMasterFlags(int(mainVals[2]))
        for fl in masterFlags:
            f.write(idx + ".add_master_flag(" + fl + ")\n")

        sequenceCount = int(mainVals[3])
        if sequenceCount > 0:
            for i in range(sequenceCount):
                seqx = animation[i+1]
                f.write("# sequence " + str(i) + "\n")
                f.write("seq" + str(i) + " = AnimationSequence(" + str(float(seqx[0])) + ", \"" + seqx[1] + "\", " + seqx[2] + ", " + seqx[3] + ")\n")

                seqFlags = processAnimationSequenceFlags(int(seqx[4]))
                for fl in seqFlags:
                    f.write("seq" + str(i) + ".add_flag(" + fl + ")\n")

                extra0123 = int(seqx[5])
                if extra0123 > 0:
                    ai, bi, ci, di = extract4f(extra0123)
                    if ai != 0.000000:
                        f.write("seq" + str(i) + ".setExtraVals(0, " + str(ai) + ")\n")
                    if bi != 0.000000:
                        f.write("seq" + str(i) + ".setExtraVals(1, " + str(bi) + ")\n")
                    if ci != 0.000000:
                        f.write("seq" + str(i) + ".setExtraVals(2, " + str(ci) + ")\n")
                    if di != 0.000000:
                        f.write("seq" + str(i) + ".setExtraVals(3, " + str(di) + ")\n")

                extra4 = float(seqx[6])
                if extra4 != 0.000000:
                    f.write("seq" + str(i) + ".setExtraVals(4, " + str(extra4) + ")\n")

                extra5 = float(seqx[7])
                if extra5 != 0.000000:
                    f.write("seq" + str(i) + ".setExtraVals(5, " + str(extra5) + ")\n")

                extra6 = float(seqx[8])
                if extra6 != 0.000000:
                    f.write("seq" + str(i) + ".setExtraVals(6, " + str(extra6) + ")\n")

                extra7 = float(seqx[9])
                if extra7 != 0.000000:
                    f.write("seq" + str(i) + ".setExtraVals(7, " + str(extra7) + ")\n")

                f.write(idx + ".add_sequence(seq" + str(i) + ")\n")
        else:
            f.write("# ERROR: Now sequences found!\n")

        f.write("\n\n")


if __name__ == "__main__":
    animations = readAnimations()
    for anim in animations:
        writeAnimation(anim)




