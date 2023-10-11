# This Python file uses the following encoding: utf-8

from sound import Sound, SoundFlag


sound1 = Sound("click")
sound1.add_flag(SoundFlag.IS_2D)
sound1.add_file("drum_3.ogg")
sound1.set_volume(3)
