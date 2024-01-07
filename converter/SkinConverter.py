# This Python file uses the following encoding: utf-8
from ScriptConverter import ScriptConverter
from skin import Skin

import skins

class SkinConverter(ScriptConverter):
    def __init__(self):
        pass

    def createCode(self):
        skins = self.retrieveSkins()
        self.writeScriptOutputFile(skins)

    def retrieveSkins(self):
        skinsx = []
        for i in vars(skins):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(skins,i)
                if not "<function" in str(attr) and not "<module" in str(attr) and not "ParticleSystem" in str(attr) and not "Sound" in str(attr):
                    if not "FaceTexture" in str(attr):
                        skinsx.append(attr)
        return skinsx

    def writeScriptOutputFile(self, codeData : list[Skin]):
        with open("./build_system/module_skins.py", "w") as f:            
            f.write("from header_skins import *\n")
            f.write("from ID_particle_systems import *\n\n")
            f.write("skins = [\n\n")

            for skin in codeData:
                f.write("(\"" + skin.id + "\", ")

                if len(skin.flags) > 0:
                    f.write("|".join(skin.flags) + ",\n")
                else:
                    f.write("0,\n")

                f.write("\"" + skin.body_mesh + "\", \"" + skin.calf_mesh + "\", ")
                f.write("\"" + skin.hand_mesh + "\", \"" + skin.head_mesh + "\",\n")

                f.write("[\n")
                for faceKey in skin.face_keys:
                    f.write("  (" + str(faceKey.idVal) + "," + str(faceKey.reserved) + "," + str(faceKey.start) + "," + str(faceKey.end) + ", \"" + faceKey.name + "\"),\n")
                f.write("],\n")

                f.write("[")
                for hair in skin.hair_meshes:
                    f.write("\"" + hair + "\",")
                f.write("],\n")

                f.write("[")
                for beard in skin.beard_meshes:
                    f.write("\"" + beard + "\",")
                f.write("],\n")

                f.write("[")
                for hair in skin.hair_textures:
                    f.write("\"" + hair + "\",")
                f.write("],\n")

                f.write("[")
                for beard in skin.beard_textures:
                    f.write("\"" + beard + "\",")
                f.write("],\n")

                f.write("[\n")
                for face_texture in skin.face_textures:
                    f.write("(\"" + face_texture.name + "\", " + hex(face_texture.color) + ", [")
                    for mat in face_texture.hair_materials:
                        f.write("\"" + mat + "\",")
                    f.write("], [")
                    for c in face_texture.hair_colors:
                        f.write(hex(c) + ",")
                    f.write("]),\n")
                f.write("],\n")

                f.write("[")
                for voice in skin.voices:
                    f.write("(" + voice[0].value + ", \"snd_" + voice[1] + "\"),")
                f.write("],\n")

                f.write("\"" + skin.skeleton_name + "\", " + str(skin.scale) + ",\n")
                if skin.blood_particles_1 != "" and skin.blood_particles_2 != "":
                    f.write("psys_" + skin.blood_particles_1 + ", psys_" + skin.blood_particles_2 + ",\n")

                    if len(skin.face_key_constraints) > 0:
                        f.write("[")
                        for fkc in skin.face_key_constraints:
                            f.write("(" + str(fkc.val) + ", ")
                            if fkc.lowerThan:
                                f.write("comp_less_than, ")
                            else:
                                f.write("comp_greater_than, ")
                            f.write("(" + str(fkc.faceField1Val) + ","  + str(fkc.faceField1) + "),")
                            f.write("(" + str(fkc.faceField2Val) + ","  + str(fkc.faceField2) + ")),\n")
                        f.write("]")

                f.write("),\n")

            f.write("\n] # SKINS END\n")
