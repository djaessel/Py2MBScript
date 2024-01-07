# This Python file uses the following encoding: utf-8

from enum import Enum

from particle_system import ParticleSystem
from sound import Sound


class SkinFlag(Enum):
    USE_MORPH_KEY_10 = "skf_use_morph_key_10"
    USE_MORPH_KEY_20 = "skf_use_morph_key_20"
    USE_MORPH_KEY_30 = "skf_use_morph_key_30"
    USE_MORPH_KEY_40 = "skf_use_morph_key_40"
    USE_MORPH_KEY_50 = "skf_use_morph_key_50"
    USE_MORPH_KEY_60 = "skf_use_morph_key_60"
    USE_MORPH_KEY_70 = "skf_use_morph_key_70"



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



class FaceKey:
    def __init__(self, name : str, idVal : int, start : float, end : float, reserved : int = 0):
        self.name = name
        self.idVal = idVal
        self.start = start
        self.end = end
        self.reserved = reserved



class FaceField(Enum):
    chin_size = 0
    chin_shape = 1
    chin_forward = 2
    jaw_width = 3
    jaw_position = 4
    mouth_nose_distance = 5
    mouth_width = 6
    cheeks = 7
    nose_height = 8
    nose_width = 9
    nose_size = 10
    nose_shape = 11
    nose_bridge = 12
    cheek_bones = 13
    eye_width = 14
    eye_to_eye_dist = 15
    eye_shape = 16
    eye_depth = 17
    eyelids = 18
    eyebrow_position = 19
    eyebrow_height = 20
    eyebrow_depth = 21
    eyebrow_shape = 22
    temple_width = 23
    face_depth = 24
    face_ratio = 25
    face_width = 26



class FaceKeyConstraint:
    def __init__(self, val : float, lowerThan : bool, faceField1 : FaceField, faceField1Val : float, faceField2 : FaceField, faceField2Val : float):
        self.val = val
        self.lowerThan = lowerThan
        self.faceField1 = faceField1.value
        self.faceField1Val = faceField1Val
        self.faceField2 = faceField2.value
        self.faceField2Val = faceField2Val



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
        self.blood_particles_1 = ""
        self.blood_particles_2 = ""
        if blood_particles_1 != None:
            self.blood_particles_1 = blood_particles_1.id
        if blood_particles_2 != None:
            self.blood_particles_2 = blood_particles_2.id
        self.face_keys = []
        self.hair_meshes = []
        self.beard_meshes = []
        self.hair_textures = []
        self.beard_textures = []
        self.face_textures = []
        self.voices = []
        self.face_key_constraints = []


    def add_flag(self, flag : SkinFlag):
        if not self.contains_flag(flag):
            self.flags.append(flag.value)


    def contains_flag(self, flag : SkinFlag):
        contains = False
        for x in self.flags:
            if x == flag.value:
                contains = True
                break
        return contains


    def remove_flag(self, flag : SkinFlag):
        if self.contains_flag(flag):
            remi = -1
            for i, f in enumerate(self.flags):
                if f == flag.value:
                    remi = i
                    break
            if remi >= 0:
                del self.flags[remi]


    def addFaceKey(self, faceKey : FaceKey):
        if not faceKey in self.face_keys:
            self.face_keys.append(faceKey)


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


    def addFaceKeyConstraint(self, faceKeyConstraint : FaceKeyConstraint):
        self.face_key_constraints.append(faceKeyConstraint)

