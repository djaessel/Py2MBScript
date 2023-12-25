# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from typing import List
from mesh import Mesh

import meshes

class MeshConverter(ScriptConverter):
    def __init__(self):
        pass

    def createCode(self):
        meshesx = self.retrieveMeshes()
        self.writeScriptOutputFile(meshesx)

    def retrieveMeshes(self):
        meshesx = []
        for i in vars(meshes):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(meshes,i)
                meshesx.append(attr)
        return meshesx

    def writeScriptOutputFile(self, codeData : List[Mesh]):
        with open("./build_system/module_meshes.py", "w") as f:
            f.write("from header_meshes import *\n\n")
            f.write("meshes = [\n\n")

            for mesh in codeData:
                f.write("(\"" + mesh.id + "\", ")

                if mesh.render_order_plus_1:
                    f.write("render_order_plus_1, ")
                else:
                    f.write("0, ")

                f.write("\"" + mesh.resource_name + "\", ")

                f.write(str(mesh.translation_x) + ", " + str(mesh.translation_y) + ", " + str(mesh.translation_z) + ", ")
                f.write(str(mesh.rotation_x) + ", " + str(mesh.rotation_y) + ", " + str(mesh.rotation_z) + ", ")
                f.write(str(mesh.scale_x) + ", " + str(mesh.scale_y) + ", " + str(mesh.scale_z))

                f.write("),\n")

            f.write("\n] # INFO PAGES END\n")

