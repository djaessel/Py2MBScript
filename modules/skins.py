# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from skin import Skin, FaceTexture, FaceKey, SkinFlag
import particle_systems as psys
import sounds as snd


# Man - Skin 1
man = Skin("man", "man_body",  "man_calf_l", "m_handL", "male_head", "skel_human", 1.0, blood_particles_1=psys.game_blood, blood_particles_2=psys.game_blood_2)
# Man - Flags
# ...
# Man - Face Keys
man.addFaceKey(FaceKey("Chin Size", 230, 0.8, -1.0))
man.addFaceKey(FaceKey("Chin Shape", 220, -1.0, 1.0))
man.addFaceKey(FaceKey("Chin Forward", 10, -1.2, 1.0))
man.addFaceKey(FaceKey("Jaw Width", 20,0, -0.6, 1.2))
man.addFaceKey(FaceKey("Jaw Position", 40,0,-0.7,1.0))
man.addFaceKey(FaceKey("Mouth-Nose Distance", 270,0,0.9,-0.9))
man.addFaceKey(FaceKey("Mouth Width", 30,0,-0.5,1.0))
man.addFaceKey(FaceKey("Cheeks", 50,0, -0.5,1.0))
#
man.addFaceKey(FaceKey("Nose Height", 60,0,-0.5,1.0))
man.addFaceKey(FaceKey("Nose Width", 70,0,-0.5,1.1))
man.addFaceKey(FaceKey("Nose Size", 80,0,1.5,-0.3))
man.addFaceKey(FaceKey("Nose Shape", 240,0,-1.0,0.8))
man.addFaceKey(FaceKey("Nose Bridge", 90,0, 0.0,1.1))
#
man.addFaceKey(FaceKey("Cheek Bones", 100,0,-0.5,1.5))
man.addFaceKey(FaceKey("Eye Width", 150,0,-0.4,1.0))
man.addFaceKey(FaceKey("Eye to Eye Dist", 110,0,1.0,0.0))
man.addFaceKey(FaceKey("Eye Shape", 120,0,-0.2,1.0))
man.addFaceKey(FaceKey("Eye Depth", 130,0,-0.1,1.6))
man.addFaceKey(FaceKey("Eyelids", 90,0, 0.0,1.1))#
#
man.addFaceKey(FaceKey("Eyebrow Position", 160,0,-0.2,1.2))
man.addFaceKey(FaceKey("Eyebrow Height", 170,0,-0.2,0.7))
man.addFaceKey(FaceKey("Eyebrow Depth", 250,0,-0.4,0.9))
man.addFaceKey(FaceKey("Eyebrow Shape", 180,0,-1.5,1.2))
man.addFaceKey(FaceKey("Temple Width", 260,0,1.0,-0.7))
#
man.addFaceKey(FaceKey("Face Depth", 200,0,-0.5,1.0))
man.addFaceKey(FaceKey("Face Ratio", 210,0,-0.5,0.9))
man.addFaceKey(FaceKey("Face Width", 190,0,-0.4,0.8))
#
man.addFaceKey(FaceKey("Post-Edit", 280,0,0.0,1.0))
# man - Hair Meshes
man.addHairMesh("man_hair_s")
man.addHairMesh("man_hair_m")
man.addHairMesh("man_hair_n")
man.addHairMesh("man_hair_o")
man.addHairMesh("man_hair_y10")
man.addHairMesh("man_hair_y12")
man.addHairMesh("man_hair_p")
man.addHairMesh("man_hair_r")
man.addHairMesh("man_hair_q")
man.addHairMesh("man_hair_v")
man.addHairMesh("man_hair_t")
man.addHairMesh("man_hair_y6")
man.addHairMesh("man_hair_y3")
man.addHairMesh("man_hair_y7")
man.addHairMesh("man_hair_y9")
man.addHairMesh("man_hair_y11")
man.addHairMesh("man_hair_u")
man.addHairMesh("man_hair_y")
man.addHairMesh("man_hair_y2")
man.addHairMesh("man_hair_y4")
# man - Hair Textures
man.addHairTexture("hair_blonde")
man.addHairTexture("hair_red")
man.addHairTexture("hair_brunette")
man.addHairTexture("hair_black")
man.addHairTexture("hair_white")
# man - Beard Meshes
man.addBeardMesh("beard_e")
man.addBeardMesh("beard_d")
man.addBeardMesh("beard_k")
man.addBeardMesh("beard_l")
man.addBeardMesh("beard_i")
man.addBeardMesh("beard_j")
man.addBeardMesh("beard_z")
man.addBeardMesh("beard_m")
man.addBeardMesh("beard_n")
man.addBeardMesh("beard_y")
man.addBeardMesh("beard_p")
man.addBeardMesh("beard_o")
man.addBeardMesh("beard_v")
man.addBeardMesh("beard_f")
man.addBeardMesh("beard_b")
man.addBeardMesh("beard_c")
man.addBeardMesh("beard_t")
man.addBeardMesh("beard_u")
man.addBeardMesh("beard_r")
man.addBeardMesh("beard_s")
man.addBeardMesh("beard_a")
man.addBeardMesh("beard_h")
man.addBeardMesh("beard_g")
#man.addBeardMesh("beard_q")
# man - Beard Textures
man.addBeardTexture("beard_blonde")
man.addBeardTexture("beard_red")
man.addBeardTexture("beard_brunette")
man.addBeardTexture("beard_black")
man.addBeardTexture("beard_white")
# man - Face Textures
# manface_young_2
man_young_2 = FaceTexture("manface_young_2", 0xffcbe0e0)
man_young_2.addHairMaterial("hair_blonde")
man_young_2.addHairColors(0xffffffff) # blonde
man_young_2.addHairColors(0xffb04717) # red
man_young_2.addHairColors(0xff502a19) # brunette
man.addFaceTexture(man_young_2)
# manface_midage
man_midage = FaceTexture("manface_midage", 0xffdfefe1)
man_midage.addHairMaterial("hair_blonde")
man_midage.addHairColors(0xffffffff) # blonde
man_midage.addHairColors(0xffb04717) # red
man_midage.addHairColors(0xff632e18) #
man_midage.addHairColors(0xff502a19) # brunette
man_midage.addHairColors(0xff19100c) # black
man.addFaceTexture(man_midage)
# manface_young
manface_young = FaceTexture("manface_young", 0xffd0e0e0)
manface_young.addHairMaterial("hair_blonde")
manface_young.addHairColors(0xff83301a) #
manface_young.addHairColors(0xff502a19) # brunette
manface_young.addHairColors(0xff19100c) # black
manface_young.addHairColors(0xff0c0d19) #
man.addFaceTexture(manface_young)
# manface_young_3
manface_young_3 = FaceTexture("manface_young_3", 0xffdceded)
manface_young_3.addHairMaterial("hair_blonde")
manface_young_3.addHairColors(0xff2f180e) #
manface_young_3.addHairColors(0xff171313) #
manface_young_3.addHairColors(0xff007080c) # c
man.addFaceTexture(manface_young_3)
# manface_7
manface_7 = FaceTexture("manface_7", 0xffc0c8c8)
manface_7.addHairMaterial("hair_blonde")
manface_7.addHairColors(0xff171313) #
manface_7.addHairColors(0xff007080c) # c
man.addFaceTexture(manface_7)
# manface_midage_2
manface_midage_2 = FaceTexture("manface_midage_2", 0xfde4c8d8)
manface_midage_2.addHairMaterial("hair_blonde")
manface_midage_2.addHairColors(0xff502a19) #
manface_midage_2.addHairColors(0xff19100c) #
manface_midage_2.addHairColors(0xff0c0d19) #
man.addFaceTexture(manface_midage_2)
# manface_rugged
manface_rugged = FaceTexture("manface_rugged", 0xfde4c8d8)
manface_rugged.addHairMaterial("hair_blonde")
manface_rugged.addHairColors(0xff171313) #
manface_rugged.addHairColors(0xff007080c) # c
man.addFaceTexture(manface_rugged)
# manface_african
manface_african = FaceTexture("manface_african", 0xff807c8a)
manface_african.addHairMaterial("hair_blonde")
manface_african.addHairColors(0xff120808) #
manface_african.addHairColors(0xff007080c) # c
man.addFaceTexture(manface_african)
# man - Voices
man.setVoiceDie(snd.man_die)
man.setVoiceHit(snd.man_hit)
man.setVoiceYell(snd.man_yell)
man.setVoiceGrunt(snd.man_grunt)
man.setVoiceGruntLong(snd.man_grunt_long)
man.setVoiceWarCry(snd.man_warcry)
man.setVoiceStun(snd.man_stun)
man.setVoiceVictory(snd.man_victory)
# man - Constraints
#  [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
#   [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
#   [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
#   [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
#   [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
#   [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
#   [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
#   [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
#   ]
#),




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
woman_young.addHairColors(0xffffffff) # blonde
woman_young.addHairColors(0xffb04717) # red
woman_young.addHairColors(0xff502a19) # brunette
woman_young.addHairColors(0xff19100c) # black
woman.addFaceTexture(woman_young)
# Woman - Voices
woman.setVoiceDie(snd.woman_die)
woman.setVoiceHit(snd.woman_hit)
woman.setVoiceYell(snd.woman_yell)




## undead - Skin 3
#undead = Skin("undead", "undead_body", "undead_calf_l", "undead_handL", "undead_head", "skel_human", 1.0)
## undead - Face Textures
#undeadface_a = FaceTexture("undeadface_a", 0xffffffff)
#undead.addFaceTexture(undeadface_a)
#undeadface_b = FaceTexture("undeadface_b", 0xffcaffc0)
#undead.addFaceTexture(undeadface_b)


