# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from postfx import PostFX


default = PostFX("default")
default.set_parameters1(hdrRange=125.9922, hdrExposureScaler=1.0588, luminanceAverageScaler=1.451, luminanceMaxScaler=9.1765)
default.set_parameters2(brightpassTreshold=0.9608, brightpassPostPower=1.1373, blurStrenght=1.1373, blurAmount=0.1961)
default.set_parameters3(ambientColorCoef=1.0, sunColorCoef=1.0, specularCoef=1.0, reserved=1.0)


map_params = PostFX("map_params", tonemap_operator_type=3)
map_params.set_parameters1(hdrRange=128.0, hdrExposureScaler=1.04, luminanceAverageScaler=1.2941, luminanceMaxScaler=10.0)
map_params.set_parameters2(brightpassTreshold=2.3725, brightpassPostPower=2.1569, blurStrenght=1.8431, blurAmount=0.4863)
map_params.set_parameters3(ambientColorCoef=1.0, sunColorCoef=1.0, specularCoef=1.05, reserved=1.0)


indoors = PostFX("indoors")
indoors.set_parameters1(hdrRange=128.0, hdrExposureScaler=1.0, luminanceAverageScaler=1.2549, luminanceMaxScaler=10.0)
indoors.set_parameters2(brightpassTreshold=0.6471, brightpassPostPower=4.7843, blurStrenght=4.1616, blurAmount=0.00155)
indoors.set_parameters3(ambientColorCoef=0.9804, sunColorCoef=0.9804, specularCoef=1.5294, reserved=1.0)


sunset = PostFX("sunset")
sunset.set_parameters1(hdrRange=128.0, hdrExposureScaler=0.5882, luminanceAverageScaler=0.9804, luminanceMaxScaler=0.9804)
sunset.set_parameters2(brightpassTreshold=0.0784, brightpassPostPower=2.1176, blurStrenght=1.3725, blurAmount=0.1255)
sunset.set_parameters3(ambientColorCoef=0.9804, sunColorCoef=0.9804, specularCoef=1.7647, reserved=1.0)


night = PostFX("night")
night.set_parameters1(hdrRange=128.0, hdrExposureScaler=1.0, luminanceAverageScaler=1.2549, luminanceMaxScaler=10.0)
night.set_parameters2(brightpassTreshold=0.6471, brightpassPostPower=4.7843, blurStrenght=1.2157, blurAmount=0.0)
night.set_parameters3(ambientColorCoef=0.9804, sunColorCoef=0.9804, specularCoef=1.5294, reserved=1.0)


sunny = PostFX("sunny")
sunny.set_parameters1(hdrRange=128.0, hdrExposureScaler=0.5882, luminanceAverageScaler=0.9804, luminanceMaxScaler=0.9804)
sunny.set_parameters2(brightpassTreshold=0.0784, brightpassPostPower=2.1176, blurStrenght=1.3725, blurAmount=0.1255)
sunny.set_parameters3(ambientColorCoef=0.9804, sunColorCoef=0.9804, specularCoef=1.7647, reserved=1.0)


cloudy = PostFX("cloudy")
cloudy.set_parameters1(hdrRange=128.0, hdrExposureScaler=1.0, luminanceAverageScaler=0.9804, luminanceMaxScaler=0.0)
cloudy.set_parameters2(brightpassTreshold=0.3137, brightpassPostPower=2.6667, blurStrenght=2.0, blurAmount=0.4314)
cloudy.set_parameters3(ambientColorCoef=0.9804, sunColorCoef=0.9804, specularCoef=1.4314, reserved=1.0)


overcast = PostFX("overcast")
overcast.set_parameters1(hdrRange=128.0, hdrExposureScaler=1.0, luminanceAverageScaler=0.9804, luminanceMaxScaler=0.0)
overcast.set_parameters2(brightpassTreshold=0.3137, brightpassPostPower=2.6667, blurStrenght=2.0, blurAmount=0.0)
overcast.set_parameters3(ambientColorCoef=0.9804, sunColorCoef=0.9804, specularCoef=1.0314, reserved=1.0)


high_contrast = PostFX("high_contrast", tonemap_operator_type=3)
high_contrast.set_parameters1(hdrRange=128.0, hdrExposureScaler=1.0, luminanceAverageScaler=1.2941, luminanceMaxScaler=10.0)
high_contrast.set_parameters2(brightpassTreshold=0.4314, brightpassPostPower=2.0, blurStrenght=1.0588, blurAmount=0.0549)
high_contrast.set_parameters3(ambientColorCoef=2.0, sunColorCoef=0.7059, specularCoef=1.4902, reserved=1.0)


