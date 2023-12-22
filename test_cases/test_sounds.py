# This Python file uses the following encoding: utf-8

from sound import Sound, SoundFlag


sound1 = Sound("click")
sound1.add_flag(SoundFlag.IS_2D)
sound1.add_file("drum_3.ogg")
sound1.set_volume(3)

sound2 = Sound("footstep_grass")
sound2.add_flag(SoundFlag.IS_2D)
sound2.add_file("drum_3.ogg")
sound2.set_volume(3)

sound3 = Sound("gallop")
sound3.add_flag(SoundFlag.IS_2D)
sound3.add_file("drum_3.ogg")
sound3.set_volume(3)
