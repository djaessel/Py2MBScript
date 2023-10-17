# This Python file uses the following encoding: utf-8


class PostFX:
    #  1) id (string):
    #  2) flags (int).
    #  3) tonemap operator type (0,1,2,3)
    #  4) shader parameters1 [ HDRRange, HDRExposureScaler, LuminanceAverageScaler, LuminanceMaxScaler ]
    #  5) shader parameters2 [ BrightpassTreshold, BrightpassPostPower, BlurStrenght, BlurAmount ]
    #  6) shader parameters3 [ AmbientColorCoef, SunColorCoef, SpecularCoef, -reserved ]

    def __init__(self, id : str, tonemap_operator_type : int = 0, has_high_hdr : bool = False):
        self.id = id
        self.has_high_hdr = has_high_hdr

        if tonemap_operator_type < 0 or tonemap_operator_type > 3:
            tonemap_operator_type = 0
        self.tonemap_operator_type = tonemap_operator_type


    def set_parameters1(self, hdrRange : float, hdrExposureScaler : float, luminanceAverageScaler : float, luminanceMaxScaler : float):
        self.hdrRange = hdrRange
        self.hdrExposureScaler = hdrExposureScaler
        self.luminanceAverageScaler = luminanceAverageScaler
        self.luminanceMaxScaler = luminanceMaxScaler


    def set_parameters2(self, brightpassTreshold : float, brightpassPostPower : float, blurStrenght : float, blurAmount : float):
        self.brightpassTreshold = brightpassTreshold
        self.brightpassPostPower = brightpassPostPower
        self.blurStrenght = blurStrenght
        self.blurAmount = blurAmount


    def set_parameters3(self, ambientColorCoef : float, sunColorCoef : float, specularCoef : float, reserved : float = 1.0):
        self.ambientColorCoef = ambientColorCoef
        self.sunColorCoef = sunColorCoef
        self.specularCoef = specularCoef
        self.reserved = reserved

