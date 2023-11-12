# This Python file uses the following encoding: utf-8

from enum import Enum

from particle_system import ParticleSystem
from sound import Sound


class Voice(Enum):
    DIE = "voice_die"       # = 0
    HIT = "voice_hit"       # = 1
    GRUNT = "voice_grunt"     # = 2
    GRUNT_LONG = "voice_grunt_long" # = 3
    YELL = "voice_yell"      # = 4
    WARCRY = "voice_warcry"    # = 5
    VICTORY = "voice_victory"   # = 6
    STUN = "voice_stun"      # = 7



class FaceTexture:
    def __init__(self, name : str, color : int):
        self.name = name
        self.color = color
        self.hair_materials = []
        self.hair_colors = []


    def addHairMaterial(self, hairMaterial : str):
        if not hairMaterial in self.hair_materials:
            self.hair_materials.append(hairMaterial)


    def addHairColors(self, hairColor : int):
        if not hairColor in self.hair_colors:
            self.hair_colors.append(hairColor)




class Skin:
    #  Each skin record contains the following fields:
    #  1) Skin id: used for referencing skins.
    #  2) Skin flags. Not used yet. Should be 0.
    #  3) Body mesh.
    #  4) Calf mesh (left one).
    #  5) Hand mesh (left one).
    #  6) Head mesh.
    #  7) Face keys (list)
    #  8) List of hair meshes.
    #  9) List of beard meshes.
    # 10) List of hair textures.
    # 11) List of beard textures.
    # 12) List of face textures.
    # 13) List of voices.
    # 14) Skeleton name
    # 15) Scale (doesn't fully work yet)
    # 16) Blood particles 1 (do not add this if you wish to use the default particles)
    # 17) Blood particles 2 (do not add this if you wish to use the default particles)
    # 17) Face key constraints (do not add this if you do not wish to use it)

    def __init__(self, id : str, body_mesh : str, calf_mesh : str, hand_mesh : str, head_mesh : str, skeleton_name : str, scale : float, blood_particles_1 : ParticleSystem = None, blood_particles_2 : ParticleSystem = None):
        self.id = id
        self.flags = []
        self.body_mesh = body_mesh
        self.calf_mesh = calf_mesh
        self.hand_mesh = hand_mesh
        self.head_mesh = head_mesh
        self.skeleton_name = skeleton_name
        self.scale = scale
        self.blood_particles_1 = blood_particles_1.id
        self.blood_particles_2 = blood_particles_2.id
        self.face_keys = []
        self.hair_meshes = []
        self.beard_meshes = []
        self.hair_textures = []
        self.beard_textures = []
        self.face_textures = []
        self.voices = []
        self.face_key_constraints = []


    def addHairMesh(self, hair_mesh : str):
        if not hair_mesh in self.hair_meshes:
            self.hair_meshes.append(hair_mesh)
        else:
            print("SKIN:", self.id, ">", "Hair mesh already set! >", hair_mesh)


    def addHairTexture(self, hair_texture : str):
        if not hair_texture in self.hair_textures:
            self.hair_textures.append(hair_texture)
        else:
            print("SKIN:", self.id, ">", "Hair texture already set! >", hair_texture)


    def addBeardMesh(self, beard_mesh : str):
        if not beard_mesh in self.beard_meshes:
            self.beard_meshes.append(beard_mesh)
        else:
            print("SKIN:", self.id, ">",  "Beard mesh already set! >", beard_mesh)


    def addBeardTexture(self, beard_texture : str):
        if not beard_texture in self.beard_textures:
            self.beard_textures.append(beard_texture)
        else:
            print("SKIN:", self.id, ">",  "Beard texture already set! >", beard_texture)


    def addFaceTexture(self, face_texture : FaceTexture):
        if not face_texture in self.face_textures:
            self.face_textures.append(face_texture)
        else:
            print("SKIN:", self.id, ">",  "Face texture already set! >", face_texture)


    def removeVoice(self, voice : Voice):
        remi = -1
        for i, v in enumerate(self.voices):
            if v[0] == voice:
                remi = i
                break
        if remi >= 0:
            self.voices.pop(remi)


    def setVoice(self, voice : Voice, sound : Sound):
        self.removeVoice(voice)
        voicex = (voice, sound.id)
        self.voices.append(voicex)


    def setVoiceDie(self, sound : Sound):
        self.setVoice(Voice.DIE, sound)


    def setVoiceHit(self, sound : Sound):
        self.setVoice(Voice.HIT, sound)


    def setVoiceGrunt(self, sound : Sound):
        self.setVoice(Voice.GRUNT, sound)


    def setVoiceGruntLong(self, sound : Sound):
        self.setVoice(Voice.GRUNT_LONG, sound)


    def setVoiceYell(self, sound : Sound):
        self.setVoice(Voice.YELL, sound)


    def setVoiceWarCry(self, sound : Sound):
        self.setVoice(Voice.WARCRY, sound)


    def setVoiceVictory(self, sound : Sound):
        self.setVoice(Voice.VICTORY, sound)


    def setVoiceStun(self, sound : Sound):
        self.setVoice(Voice.STUN, sound)

