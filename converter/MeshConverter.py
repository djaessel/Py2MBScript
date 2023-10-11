# This Python file uses the following encoding: utf-8

from ScriptConverter import ScriptConverter
from typing import List
from mesh import Mesh

import inspect
import test_meshes

class MeshConverter(ScriptConverter):
    def __init__(self):
        pass

    def retrieveMeshes(self):
        meshes = []
        for i in vars(test_meshes):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(test_meshes,i)
                meshes.append(attr)
        return meshes

    def writeScriptOutputFile(self, codeData : List[Mesh]):
        with open("./test_cases/test_meshes_output.py", "w") as f:
            f.write("from header_operations import *\n")
            f.write("from header_common import *\n\n")
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

