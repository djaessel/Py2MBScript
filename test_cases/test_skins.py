# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from skin import Skin, FaceTexture, FaceKey
from test_particle_systems import *
from test_sounds import *


# Woman - SKIN 2
woman = Skin("woman", "woman_body",  "woman_calf_l", "f_handL", "female_head", "skel_human", 1.0, blood_particles_1=game_rain, blood_particles_2=game_rain)
# Woman - Flags
# TODO: add morph key 10
# Woman - Face Keys
#woman_face_keys = [
#(230,0,0.8,-1.0, "Chin Size"),
#(220,0,-1.0,1.0, "Chin Shape"),
#(10,0,-1.2,1.0, "Chin Forward"),
#(20,0, -0.6, 1.2, "Jaw Width"),
#(40,0,-0.7,1.0, "Jaw Position"),
#(270,0,0.9,-0.9, "Mouth-Nose Distance"),
#(30,0,-0.5,1.0, "Mouth Width"),
#(50,0, -0.5,1.0, "Cheeks"),
#
#(60,0,-0.5,1.0, "Nose Height"),
#(70,0,-0.5,1.1, "Nose Width"),
#(80,0,1.5,-0.3, "Nose Size"),
#(240,0,-1.0,0.8, "Nose Shape"),
#(90,0, 0.0,1.1, "Nose Bridge"),
#
#(100,0,-0.5,1.5, "Cheek Bones"),
#(150,0,-0.4,1.0, "Eye Width"),
#(110,0,1.0,0.0, "Eye to Eye Dist"),
#(120,0,-0.2,1.0, "Eye Shape"),
#(130,0,-0.1,1.6, "Eye Depth"),
#(140,0,-0.2,1.0, "Eyelids"),
#
#
#(160,0,-0.2,1.2, "Eyebrow Position"),
#(170,0,-0.2,0.7, "Eyebrow Height"),
#(250,0,-0.4,0.9, "Eyebrow Depth"),
#(180,0,-1.5,1.2, "Eyebrow Shape"),
#(260,0,1.0,-0.7, "Temple Width"),
#
#(200,0,-0.5,1.0, "Face Depth"),
#(210,0,-0.5,0.9, "Face Ratio"),
#(190,0,-0.4,0.8, "Face Width"),
#
#(280,0,0.0,1.0, "Post-Edit"),
#]
woman.addFaceKey(FaceKey("Chin Size", 230, 0.8, -1.0))
woman.addFaceKey(FaceKey("Chin Shape", 220, -1.0, 1.0))
woman.addFaceKey(FaceKey("Chin Forward", 10, -1.2, 1.0))
# Woman - Hair Meshes
woman.addHairMesh("woman_hair_p")
woman.addHairMesh("woman_hair_n")
woman.addHairMesh("woman_hair_o")
woman.addHairMesh("woman_hair_q")
woman.addHairMesh("woman_hair_r")
woman.addHairMesh("woman_hair_s")
woman.addHairMesh("woman_hair_t")
# Woman - Hair Textures
woman.addHairTexture("hair_blonde")
woman.addHairTexture("hair_red")
woman.addHairTexture("hair_brunette")
woman.addHairTexture("hair_black")
woman.addHairTexture("hair_white")
# Woman - Face Textures
woman_young = FaceTexture("womanface_young", 0xffe3e8ef)
woman_young.addHairMaterial("hair_blonde")
woman_young.addHairColors(0xffffffff)
woman_young.addHairColors(0xffb04717)
woman_young.addHairColors(0xff502a19)
woman_young.addHairColors(0xff19100c)
woman.addFaceTexture(woman_young)
# Woman - Voices
woman.setVoiceDie(sound1)
woman.setVoiceHit(sound1)
woman.setVoiceYell(sound1)
