# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from skill import Skill

import inspect
import test_skills


class SkillConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveSkills(self):
        triggers = []
        for i in vars(test_skills):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_skills,i)
                triggers.append(attr)
        return triggers

    def writeScriptOutputFile(self, codeData):
        with open("./test_cases/test_skills_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("skills = [\n\n")

            for skill in codeData:
                f.write("(\"" + skill.id + "\",\"" + skill.name + "\",")

                if len(skill.flags) > 0:
                    f.write("|".join(skill.flags))
                else:
                    f.write("0")
                f.write(",")

                f.write(str(skill.max_level) + ",\"" + skill.description + "\"),\n\n")

            f.write("]\n")