# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from music import MusicTrack

import test_music


class MusicConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveTracks(self):
        tracks = []
        for i in vars(test_music):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_music,i)
                tracks.append(attr)
        return tracks

    def writeScriptOutputFile(self, codeData : list[MusicTrack]):
        with open("./build_system/module_music.py", "w") as f:
            f.write("from header_music import *\n\n")
            f.write("tracks = [\n\n")

            for track in codeData:
                f.write("(\"" + track.id + "\",\"" + track.file + "\",")

                if len(track.flags) > 0:
                    f.write("|".join(track.flags) + ",")
                else:
                    f.write("0,")

                if len(track.continue_flags) > 0:
                    f.write("|".join(track.continue_flags) + ",")
                else:
                    f.write("0")

                f.write("),\n")

            f.write("\n] # TRACKS END\n")


