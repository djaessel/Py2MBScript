# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from particle_system import ParticleSystem

import particle_systems

class ParticleSystemConverter(ScriptConverter):
    def __init__(self):
        pass

    def createCode(self):
        psys = self.retrieveParticleSystems()
        self.writeScriptOutputFile(psys)

    def retrieveParticleSystems(self):
        psys = []
        for i in vars(particle_systems):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(particle_systems,i)
                if not "<function" in str(attr) and not "<module" in str(attr) and not "SimpleTrigger" in str(attr):
                    psys.append(attr)
        return psys

    def writeScriptOutputFile(self, codeData : list[ParticleSystem]):
        with open("./build_system/module_particle_systems.py", "w") as f:
            f.write("from header_particle_systems import *\n\n")
            f.write("particle_systems = [\n\n")

            for psys in codeData:
                f.write("(\"" + psys.id + "\", ")

                if len(psys.flags) > 0:
                    f.write("|".join(psys.flags) + ", ")
                else:
                    f.write("0, ")

                f.write("\"" + psys.mesh_name + "\",\n")

                f.write(str(psys.num_particles) + ", " + str(psys.life) + ", " + str(psys.damping) + ", ")
                f.write(str(psys.gravity_strength) + ", " + str(psys.turbulance_size) + ", " + str(psys.turbulance_strength) + ",\n")

                f.write("(" + str(psys.alpha_keys[0][0]) + ", " + str(psys.alpha_keys[0][1]) + "), (" + str(psys.alpha_keys[1][0]) + ", " + str(psys.alpha_keys[1][1]) + "),\n")
                f.write("(" + str(psys.red_keys[0][0]) + ", " + str(psys.red_keys[0][1]) + "), (" + str(psys.red_keys[1][0]) + ", " + str(psys.red_keys[1][1]) + "),\n")
                f.write("(" + str(psys.green_keys[0][0]) + ", " + str(psys.green_keys[0][1]) + "), (" + str(psys.green_keys[1][0]) + ", " + str(psys.green_keys[1][1]) + "),\n")
                f.write("(" + str(psys.blue_keys[0][0]) + ", " + str(psys.blue_keys[0][1]) + "), (" + str(psys.blue_keys[1][0]) + ", " + str(psys.blue_keys[1][1]) + "),\n")
                f.write("(" + str(psys.scale_keys[0][0]) + ", " + str(psys.scale_keys[0][1]) + "), (" + str(psys.scale_keys[1][0]) + ", " + str(psys.scale_keys[1][1]) + "),\n")

                f.write("(" + str(psys.emit_box_size[0]) + ", " + str(psys.emit_box_size[1]) + ", " + str(psys.emit_box_size[2]) + "),\n")
                f.write("(" + str(psys.emit_velocity[0]) + ", " + str(psys.emit_velocity[1]) + ", " + str(psys.emit_velocity[2]) + "),\n")

                f.write(str(psys.emit_dir_randomness) + ",\n")
                f.write(str(psys.rotation_speed) + ",\n")
                f.write(str(psys.rotation_damping) + ",\n")

                f.write("),\n")

            f.write("\n] # PARTICLE SYSTEMS END\n")
