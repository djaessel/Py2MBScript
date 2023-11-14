from __future__ import print_function
import shutil
from module_info import *

def save_module_ini():
    filename = "module.ini"
    src = "./" + filename
    dst = export_dir + filename
    shutil.copyfile(src, dst)

print("Exporting module.ini ...")
save_module_ini()

