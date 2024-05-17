# This Python file uses the following encoding: utf-8


module_path = "/home/djaessel/warband/Modules/Native/"


def readMeshes():
    meshes = []
    with open(module_path + "meshes.txt") as f:
        for line in f:
            if line.startswith("mesh_"):
                tmp = line.strip().split(' ')
                meshes.append(tmp)
    return meshes


def writeMesh(f, mesh : list):
    idx = mesh[0][5:]

    f.write(idx + " = Mesh(\"" + idx + "\", \"" + mesh[2] + "\"")

    if int(mesh[1]) == 1:
        f.write(", render_order_plus_1=True")
    f.write(")\n")

    translation_x = float(mesh[3])
    translation_y = float(mesh[4])
    translation_z = float(mesh[5])
    if translation_x != 0.000000 or translation_y != 0.000000 or translation_z != 0.000000:
        f.write(idx + ".set_axis_translation(" + str(translation_x) + ", " + str(translation_y) + ", " + str(translation_z) + ")\n")

    rotation_x = float(mesh[6])
    rotation_y = float(mesh[7])
    rotation_z = float(mesh[8])
    if rotation_x != 0.000000 or rotation_y != 0.000000 or rotation_z != 0.000000:
        f.write(idx + ".set_rotation(" + str(rotation_x) + ", " + str(rotation_y) + ", " + str(rotation_z) + ")\n")

    scale_x = float(mesh[9])
    scale_y = float(mesh[10])
    scale_z = float(mesh[11])
    if scale_x != 1.000000 or scale_y != 1.000000 or scale_z != 1.000000:
        if scale_x == scale_y and scale_x == scale_z:
            f.write(idx + ".set_scale_whole(" + str(scale_x) + ")\n")
        else:
            f.write(idx + ".set_scale(" + str(scale_x) + ", " + str(scale_y) + ", " + str(scale_z) + ")\n")

    f.write("\n")


if __name__ == "__main__":
    meshes = readMeshes()
    with open("test_meshes.py", "w") as f:
        for m in meshes:
            writeMesh(f, m)





