# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from skin import Skin, FaceTexture
from test_particle_systems import *
from test_sounds import *


# Woman - SKIN 2
woman = Skin("woman", "woman_body",  "woman_calf_l", "f_handL", "female_head", "skel_human", 1.0, blood_particles_1=game_rain, blood_particles_2=game_rain)
# Woman - Flags
# TODO: add morph key 10
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
