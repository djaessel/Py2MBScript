from __future__ import print_function
import os
import shutil

from module_info import *

def save_languages():
    langFolder = "languages"
    src = "./" + langFolder
    dst = export_dir + langFolder
    try:
        #if path already exists, remove it before copying with copytree()
        if os.path.exists(dst):
            shutil.rmtree(dst)
            shutil.copytree(src, dst)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        #if e.errno == errno.ENOTDIR:
        #    shutil.copy(source_dir_prompt, destination_dir_prompt)
        #else:
        #    print('Directory not copied. Error: %s' % e)
        print('Directory not copied. Error: %s' % e)

print("Exporting languages...")
save_languages()

