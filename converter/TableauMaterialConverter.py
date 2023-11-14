# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from typing import List
from tableau_material import TableauMaterial

import inspect
import test_tableau_materials

class TableauMaterialConverter(ScriptConverter):

    def retrieveTableauMaterials(self):
        tabMats = []
        for i in vars(test_tableau_materials):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_tableau_materials,i)
                if not "<function" in str(attr) and not "<module" in str(attr):
                    tabMats.append(attr)
        return tabMats

    def writeScriptOutputFile(self, codeData : List[TableauMaterial]):
        with open("./build_system/module_tableau_materials.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
            f.write("tableau_materials = [\n\n")

            # ("game_character_sheet", 0, "tableau_with_transparency", 1024, 1024, 0, 0, 266, 532,

            for tabMat in codeData:
                f.write("(\"" + tabMat.id + "\", ")

                if len(tabMat.flags) > 0:
                    print("NOT SUPPORED!")
                    print(tabMat.id, ">", tabMat.flags)
                else:
                    f.write("0, ")

                f.write("\"" + tabMat.sample_material_name + "\", ")
                f.write(str(tabMat.width) + ", " + str(tabMat.height) + ", ")
                f.write(str(tabMat.mesh_min_x) + ", " + str(tabMat.mesh_min_y) + ", ")
                f.write(str(tabMat.mesh_max_x) + ", " + str(tabMat.mesh_max_y) + ", ")

                f.write("[\n")

                codeLines = inspect.getsourcelines(tabMat.codeBlock)[0]
                #for i in range(len(codeLines)):
                #    codeLines[i] = codeLines[i][4:]
                #codeLines.pop(0)
                codeLines = self.transformScriptBlock(codeLines)
                codeLines.pop(0)
                self.writeScriptCode(f, codeLines)

            f.write("\n] # TABLEAU MATERIALS END\n")
