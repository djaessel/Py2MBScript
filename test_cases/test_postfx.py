# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from postfx import PostFX


sunny = PostFX("sunny")
sunny.set_parameters1(128.0000, 0.5882, 0.9804, 0.9804)
sunny.set_parameters2(0.0784, 2.1176, 1.3725, 0.1255)
sunny.set_parameters3(0.9804, 0.9804, 1.7647)

