# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from animation import Animation

import inspect
import test_animations


class AnimationConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveAnimations(self):
        anims = []
        for i in vars(test_animations):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_animations,i)
                if not "<function" in str(attr) and not "<module" in str(attr) and not "Sequence" in str(attr):
                    anims.append(attr)
        return anims

    def writeScriptOutputFile(self, codeData : dict[Animation]):
        with open("./test_cases/test_animations_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("animations = [\n\n")

            for anim in codeData:
                f.write("[\"" + anim.id + "\", ")

                if anim.animation_length > 0:
                    f.write("acf_anim_length(" + anim.animation_length + ")|")
                if len(anim.flags) > 0:
                    f.write("|".join(anim.flags) + ", ")
                else:
                    f.write("0, ")

                if len(anim.masterFlags) > 0:
                    f.write("|".join(anim.masterFlags))
                else:
                    f.write("0")
                f.write(",\n")


                for seq in anim.sequences:
                    f.write("  [" + str(seq.duration) + ", \"" + seq.resource_name + "\", ")
                    f.write(str(seq.beginning_frame) + ", " + str(seq.ending_frame) + ", ")

                    if len(seq.flags) > 0:
                        f.write("|".join(seq.flags) + ", ")
                    else:
                        f.write("0, ")

                    if seq.extra_vals[0] != 0 and seq.extra_vals[1] != 0:
                        if seq.extra_vals[2] != 0 and seq.extra_vals[3] != 0:
                            f.write("pack4f(" + str(seq.extra_vals[0]) + "," + str(seq.extra_vals[1]) + "," + str(seq.extra_vals[2]) + "," + str(seq.extra_vals[3]))
                        else:
                            f.write("pack2f(" + str(seq.extra_vals[0]) + "," + str(seq.extra_vals[1]))
                        f.write("), ")
                    elif seq.extra_vals[7] != 0:
                        f.write("0, ")

                    if seq.extra_vals[7] != 0 or seq.extra_vals[6] != 0 or seq.extra_vals[5] != 0 or seq.extra_vals[4] != 0:
                        f.write("(" + str(seq.extra_vals[4]) + "," + str(seq.extra_vals[5]) + "," + str(seq.extra_vals[6]) + "), ")

                    if seq.extra_vals[7] != 0:
                        f.write(str(seq.extra_vals[7]))

                    f.write("],\n")

                f.write("],\n")

            f.write("\n] # ANIMATIONS END\n")

