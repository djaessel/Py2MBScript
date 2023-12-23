# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from skin import Skin, FaceTexture, FaceKey, SkinFlag
import particle_systems as psys
import test_sounds as snd


# Woman - SKIN 2
woman = Skin("woman", "woman_body",  "woman_calf_l", "f_handL", "female_head", "skel_human", 1.0, blood_particles_1=psys.game_blood, blood_particles_2=psys.game_blood_2)
# Woman - Flags
woman.add_flag(SkinFlag.USE_MORPH_KEY_10)
# Woman - Face Keys
woman.addFaceKey(FaceKey("Chin Size", 230, 0.8, -1.0))
woman.addFaceKey(FaceKey("Chin Shape", 220, -1.0, 1.0))
woman.addFaceKey(FaceKey("Chin Forward", 10, -1.2, 1.0))
woman.addFaceKey(FaceKey("Jaw Width", 20,0, -0.6, 1.2))
woman.addFaceKey(FaceKey("Jaw Position", 40,0,-0.7,1.0))
woman.addFaceKey(FaceKey("Mouth-Nose Distance", 270,0,0.9,-0.9))
woman.addFaceKey(FaceKey("Mouth Width", 30,0,-0.5,1.0))
woman.addFaceKey(FaceKey("Cheeks", 50,0, -0.5,1.0))
#
woman.addFaceKey(FaceKey("Nose Height", 60,0,-0.5,1.0))
woman.addFaceKey(FaceKey("Nose Width", 70,0,-0.5,1.1))
woman.addFaceKey(FaceKey("Nose Size", 80,0,1.5,-0.3))
woman.addFaceKey(FaceKey("Nose Shape", 240,0,-1.0,0.8))
woman.addFaceKey(FaceKey("Nose Bridge", 90,0, 0.0,1.1))
#
woman.addFaceKey(FaceKey("Cheek Bones", 100,0,-0.5,1.5))
woman.addFaceKey(FaceKey("Eye Width", 150,0,-0.4,1.0))
woman.addFaceKey(FaceKey("Eye to Eye Dist", 110,0,1.0,0.0))
woman.addFaceKey(FaceKey("Eye Shape", 120,0,-0.2,1.0))
woman.addFaceKey(FaceKey("Eye Depth", 130,0,-0.1,1.6))
woman.addFaceKey(FaceKey("Eyelids", 90,0, 0.0,1.1))#
#
woman.addFaceKey(FaceKey("Eyebrow Position", 160,0,-0.2,1.2))
woman.addFaceKey(FaceKey("Eyebrow Height", 170,0,-0.2,0.7))
woman.addFaceKey(FaceKey("Eyebrow Depth", 250,0,-0.4,0.9))
woman.addFaceKey(FaceKey("Eyebrow Shape", 180,0,-1.5,1.2))
woman.addFaceKey(FaceKey("Temple Width", 260,0,1.0,-0.7))
#
woman.addFaceKey(FaceKey("Face Depth", 200,0,-0.5,1.0))
woman.addFaceKey(FaceKey("Face Ratio", 210,0,-0.5,0.9))
woman.addFaceKey(FaceKey("Face Width", 190,0,-0.4,0.8))
#
woman.addFaceKey(FaceKey("Post-Edit", 280,0,0.0,1.0))
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
woman.setVoiceDie(snd.sound1)
woman.setVoiceHit(snd.sound1)
woman.setVoiceYell(snd.sound1)
