# This Python file uses the following encoding: utf-8


module_path = "/home/djaessel/warband/Modules/Native/"


def readPostFX():
    postfx = []
    with open(module_path + "postfx.txt") as f:
        for line in f:
            if line.startswith("pfx_"):
                tmp = line.strip().split("  ")
                postfx.append(tmp)
    return postfx


def writePostFX(f, postfx : list):
    tmp = postfx[0].split(' ')
    idx = tmp[0][4:]
    flagx = int(tmp[1])
    tonemapOperator = int(tmp[2])

    f.write(idx + " = PostFX(\"" + idx + "\"")

    if tonemapOperator != 0:
        f.write(", tonemap_operator_type=" + str(tonemapOperator))

    if flagx == 1:
        f.write(", has_high_hdr=True")

    f.write(")\n")

    tmp = postfx[1].split(' ')
    f.write(idx + ".set_parameters1(")
    f.write("hdrRange=" + str(float(tmp[0])))
    f.write(", hdrExposureScaler=" + str(float(tmp[1])))
    f.write(", luminanceAverageScaler=" + str(float(tmp[2])))
    f.write(", luminanceMaxScaler=" + str(float(tmp[3])) + ")\n")

    tmp = postfx[2].split(' ')
    f.write(idx + ".set_parameters2(")
    f.write("brightpassTreshold=" + str(float(tmp[0])))
    f.write(", brightpassPostPower=" + str(float(tmp[1])))
    f.write(", blurStrenght=" + str(float(tmp[2])))
    f.write(", blurAmount=" + str(float(tmp[3])) + ")\n")

    tmp = postfx[3].split(' ')
    f.write(idx + ".set_parameters3(")
    f.write("ambientColorCoef=" + str(float(tmp[0])))
    f.write(", sunColorCoef=" + str(float(tmp[1])))
    f.write(", specularCoef=" + str(float(tmp[2])))
    f.write(", reserved=" + str(float(tmp[3])) + ")\n")

    f.write("\n\n")



if __name__ == "__main__":
    postfx = readPostFX()
    with open("test_postfx.py", "w") as f:
        for pfx in postfx:
            writePostFX(f, pfx)

