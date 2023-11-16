# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from sound import Sound

import test_sounds

class SoundConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveSounds(self):
        sounds = []
        for i in vars(test_sounds):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_sounds,i)
                sounds.append(attr)
        return sounds

    def writeScriptOutputFile(self, codeData : list[Sound]):
        with open("./build_system/module_sounds.py", "w") as f:
            f.write("from header_sounds import *\n")
            f.write("sounds = [\n\n")

            for sound in codeData:
                f.write("(\"" + sound.id + "\", ")

                if len(sound.flags) > 0:
                    f.write("|".join(sound.flags))
                else:
                    f.write("0")

                if sound.volume > 0:
                    f.write("|sf_vol_" + str(sound.volume))

                if sound.priority > 0:
                    f.write("|sf_priority_" + str(sound.priority))

                f.write(", ")

                f.write("[")
                for i, file in enumerate(sound.files):
                    f.write("\"" + file + "\"")
                    if i < len(sound.files) - 1:
                        f.write(",")

                f.write("]),\n")

            f.write("\n] # SOUNDS END\n")

