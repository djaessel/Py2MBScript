# This Python file uses the following encoding: utf-8
from ScriptConverter import ScriptConverter
from skin import Skin

import inspect
import test_skins

class SkinConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveSkins(self):
        skins = []
        for i in vars(test_skins):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_skins,i)
                if not "<function" in str(attr) and not "<module" in str(attr) and not "ParticleSystem" in str(attr) and not "Sound" in str(attr):
                    if not "FaceTexture" in str(attr):
                        skins.append(attr)
        return skins

    def writeScriptOutputFile(self, codeData : list[Skin]):
        with open("./test_cases/test_skins_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("strings = [\n\n")

            for skin in codeData:
                f.write("(\"" + skin.id + "\", ")

                if len(skin.flags) > 0:
                    print(skin.flags)
                else:
                    f.write("0,\n")

                f.write("\"" + skin.body_mesh + "\", \"" + skin.calf_mesh + "\", ")
                f.write("\"" + skin.hand_mesh + "\", \"" + skin.head_mesh + "\",\n")

                f.write("[], # face keys\n")

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
                f.write("psys_" + skin.blood_particles_1 + ", psys_" + skin.blood_particles_2 + ",\n")

                #TODO:
                #if face_key_constrains:
                #    bla bla

                f.write("),\n")

            f.write("\n] # SKINS END\n")
