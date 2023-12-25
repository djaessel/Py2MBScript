# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from postfx import PostFX

import test_postfx

class PostFXConverter(ScriptConverter):
    def __init__(self):
        pass

    def createCode(self):
        postfx = self.retrievePostFX()
        self.writeScriptOutputFile(postfx)

    def retrievePostFX(self):
        post_fx = []
        for i in vars(test_postfx):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_postfx,i)
                if not "<function" in str(attr) and not "<module" in str(attr):
                    post_fx.append(attr)
        return post_fx

    def writeScriptOutputFile(self, codeData : list[PostFX]):
        with open("./build_system/module_postfx.py", "w") as f:
            f.write("from header_postfx import *\n\n")
            f.write("postfx_params = [\n\n")

            for post_fx in codeData:
                f.write("(\"" + post_fx.id + "\", ")

                if post_fx.has_high_hdr:
                    f.write("fxf_highhdr, ")
                else:
                    f.write("0, ")

                f.write(str(post_fx.tonemap_operator_type) + ", [")

                f.write(str(post_fx.hdrRange) + ", ")
                f.write(str(post_fx.hdrExposureScaler) + ", ")
                f.write(str(post_fx.luminanceAverageScaler) + ", ")
                f.write(str(post_fx.luminanceMaxScaler) + "], [")

                f.write(str(post_fx.brightpassTreshold) + ", ")
                f.write(str(post_fx.brightpassPostPower) + ", ")
                f.write(str(post_fx.blurStrenght) + ", ")
                f.write(str(post_fx.blurAmount) + "], [")

                f.write(str(post_fx.ambientColorCoef) + ", ")
                f.write(str(post_fx.sunColorCoef) + ", ")
                f.write(str(post_fx.specularCoef) + ", ")
                f.write(str(post_fx.reserved) + "]),\n")

            f.write("\n] # POSTFX END\n")

