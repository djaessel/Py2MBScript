# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../build_system/")
sys.path.append("../data_objects/")

import header_particle_systems as psysHeader
import particle_system as psysData


module_path = "/home/djaessel/warband/Modules/Native/"


def readParticleSystems():
    particleSystems = []
    with open(module_path + "particle_systems.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("psys_"):
                tmp = line.strip().split(' ')
                particleSystems.append([tmp])
            elif lineCount > 2:
                particleSystems[len(particleSystems)-1].append(line.strip().split(' '))
            lineCount += 1
    return particleSystems


def processFlags(x : int):
    flags = []
    final_flags = []
    if int(x) >= 0:
        consts = dict()
        for i in vars(psysHeader):
            if i.startswith("psf_"):
                consts[i] = getattr(psysHeader,i)
        for t in consts:
            v = consts[t]
            if (x & v) == v:
                flags.append(t)

        mapx = None
        for tfx in vars(psysData):
            if "ParticleSystemFlag" in tfx:
                atx = getattr(psysData,tfx)
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
                    print("WARNING: Ignored psf >", y)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags


def writePsys(f, psys : list):
    mainVals = psys[0]
    idx = mainVals[0][5:]

    f.write(idx + " = ParticleSystem(\"" + idx + "\"")
    f.write(", mesh_name=\"" + mainVals[2] + "\"")
    f.write(", num_particles=" + mainVals[4])
    f.write(", life=" + str(float(mainVals[5])))
    f.write(", damping=" + str(float(mainVals[6])))
    f.write(", gravity_strength=" + str(float(mainVals[7])))
    f.write(", turbulance_size=" + str(float(mainVals[8])))
    f.write(", turbulance_strength=" + str(float(mainVals[9])))
    f.write(")\n")

    flagsx = processFlags(int(mainVals[1]))
    for fl in flagsx:
        f.write(idx + ".add_flag(" + fl + ")\n")

    # ALPHA KEYS
    alpha_keys0_x = float(psys[1][0])
    alpha_keys0_y = float(psys[1][1])
    if alpha_keys0_x != 0.000000 or alpha_keys0_y != 0.000000:
        f.write(idx + ".set_alpha_keys(0, time=" + str(alpha_keys0_x) + ", magnitude=" + str(alpha_keys0_y) + ")\n")

    alpha_keys1_x = float(psys[1][4])
    alpha_keys1_y = float(psys[1][5])
    if alpha_keys1_x != 0.000000 or alpha_keys1_y != 0.000000:
        f.write(idx + ".set_alpha_keys(1, time=" + str(alpha_keys1_x) + ", magnitude=" + str(alpha_keys1_y) + ")\n")

    # RED KEYS
    red_keys0_x = float(psys[2][0])
    red_keys0_y = float(psys[2][1])
    if red_keys0_x != 1.000000 or red_keys0_y != 1.000000:
        f.write(idx + ".set_red_keys(0, time=" + str(red_keys0_x) + ", magnitude=" + str(red_keys0_y) + ")\n")

    red_keys1_x = float(psys[2][4])
    red_keys1_y = float(psys[2][5])
    if red_keys1_x != 1.000000 or red_keys1_y != 1.000000:
        f.write(idx + ".set_red_keys(1, time=" + str(red_keys1_x) + ", magnitude=" + str(red_keys1_y) + ")\n")

    # GREEN KEYS
    green_keys0_x = float(psys[3][0])
    green_keys0_y = float(psys[3][1])
    if green_keys0_x != 1.000000 or green_keys0_y != 1.000000:
        f.write(idx + ".set_green_keys(0, time=" + str(green_keys0_x) + ", magnitude=" + str(green_keys0_y) + ")\n")

    green_keys1_x = float(psys[3][4])
    green_keys1_y = float(psys[3][5])
    if green_keys1_x != 1.000000 or green_keys1_y != 1.000000:
        f.write(idx + ".set_green_keys(1, time=" + str(green_keys1_x) + ", magnitude=" + str(green_keys1_y) + ")\n")

    # BLUE KEYS
    blue_keys0_x = float(psys[4][0])
    blue_keys0_y = float(psys[4][1])
    if blue_keys0_x != 1.000000 or blue_keys0_y != 1.000000:
        f.write(idx + ".set_blue_keys(0, time=" + str(blue_keys0_x) + ", magnitude=" + str(blue_keys0_y) + ")\n")

    blue_keys1_x = float(psys[4][4])
    blue_keys1_y = float(psys[4][5])
    if blue_keys1_x != 1.000000 or blue_keys1_y != 1.000000:
        f.write(idx + ".set_blue_keys(1, time=" + str(blue_keys1_x) + ", magnitude=" + str(blue_keys1_y) + ")\n")

    # SCALE KEYS
    scale_keys0_x = float(psys[5][0])
    scale_keys0_y = float(psys[5][1])
    if scale_keys0_x != 1.000000 or scale_keys0_y != 1.000000:
        f.write(idx + ".set_scale_keys(0, time=" + str(scale_keys0_x) + ", magnitude=" + str(scale_keys0_y) + ")\n")

    scale_keys1_x = float(psys[5][4])
    scale_keys1_y = float(psys[5][5])
    if scale_keys1_x != 1.000000 or scale_keys1_y != 1.000000:
        f.write(idx + ".set_scale_keys(1, time=" + str(scale_keys1_x) + ", magnitude=" + str(scale_keys1_y) + ")\n")

    # EMIT BOX
    emit_box_size_x = float(psys[6][0])
    emit_box_size_y = float(psys[6][1])
    emit_box_size_z = float(psys[6][2])
    if emit_box_size_x != 1.000000 or emit_box_size_y != 1.000000 or emit_box_size_z != 1.000000:
        f.write(idx + ".set_emit_box_size(" + str(emit_box_size_x) + ", " + str(emit_box_size_y) + ", " + str(emit_box_size_z) + ")\n")

    # EMIT VELOCITY
    emit_velocity_x = float(psys[6][5])
    emit_velocity_y = float(psys[6][6])
    emit_velocity_z = float(psys[6][7])
    if emit_velocity_x != 1.000000 or emit_velocity_y != 1.000000 or emit_velocity_z != 1.000000:
        f.write(idx + ".set_emit_velocity(" + str(emit_velocity_x) + ", " + str(emit_velocity_y) + ", " + str(emit_velocity_z) + ")\n")

    emit_dir_randomness = float(psys[6][10])
    if emit_dir_randomness != 0.000000:
        f.write(idx + ".set_emit_direction_randomness(" + str(emit_dir_randomness) + ")\n")

    rotation_speed = float(psys[7][0])
    rotation_damping = float(psys[7][1])
    if rotation_speed != 0.000000 or rotation_damping != 0.000000:
        f.write(idx + ".set_rotation(speed=" + str(rotation_speed) + ", damping=" + str(rotation_damping) + ")\n")

    f.write("\n\n")



if __name__ == "__main__":
    particleSystems = readParticleSystems()
    with open("test_particles_systems.py", "w") as f:
        for psys in particleSystems:
            writePsys(f, psys)
