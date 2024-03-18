#!/usr/bin/python3
# This Python file uses the following encoding: utf-8

import sys
import os


# Import all directories
sys.path.append("./converter/")
sys.path.append("./data_objects/")
sys.path.append("./test_cases/")
sys.path.append("./modules/")
sys.path.append("./build_system/")
sys.path.append("./translation/")


from ScriptConverter import ScriptConverter
from SimpleTriggerConverter import SimpleTriggerConverter
from TriggerConverter import TriggerConverter
from GameMenuConverter import GameMenuConverter
from ItemConverter import ItemConverter
from TroopConverter import TroopConverter
from SkillConverter import SkillConverter
from PresentationConverter import PresentationConverter
from PartyConverter import PartyConverter
from InfoPageConverter import InfoPageConverter
from StringConverter import StringConverter
from MusicConverter import MusicConverter
from MeshConverter import MeshConverter
from SoundConverter import SoundConverter
from FactionConverter import FactionConverter
from SceneConverter import SceneConverter
from MapIconConverter import MapIconConverter
from ParticleSystemConverter import ParticleSystemConverter
from TableauMaterialConverter import TableauMaterialConverter
from QuestConverter import QuestConverter
from PostFXConverter import PostFXConverter
from PartyTemplateConverter import PartyTemplateConverter
from MissionTemplateConverter import MissionTemplateConverter
from AnimationConverter import AnimationConverter
from ScenePropConverter import ScenePropConverter
from DialogConverter import DialogConverter
from SkinConverter import SkinConverter



def handle_pre_module_arguments(args):
    # TODO: create pre module creation console arguments
    pass



def handle_post_module_arguments(args):
    if len(args) > 1:
        if args[1] == "-b" or args[1] == "--build" or args[1] == "--build-and-run":
            cwd = os.getcwd()
            os.chdir(os.path.join(cwd, "build_system"))
            cwd = os.getcwd()
            print("Starting build process! ->", cwd)

            is_windows = sys.platform.startswith('win')
            is_linux = sys.platform.startswith('linux')
            if is_windows:
                os.system("start build_module.bat")
            elif is_linux:
                os.system("bash build_module_py3.sh")
                if args[1] == "--build-and-run":
                    modPath = ""
                    with open("module_info.py") as f:
                        for line in f:
                            if line.startswith("export_dir"):
                                modPath = line.split('=')[1].strip().strip('"').strip("'")
                    if len(modPath.strip()) > 0:
                        pathxs = modPath.split('/')
                        gamePath = ""
                        for i in range(len(pathxs)-3):
                            gamePath += pathxs[i] + "/"
                        gamePath += "mb_warband.sh"
                        print("Running Warband now! ->", gamePath)
                        os.system('"' + gamePath + '"')
                    else:
                        print("Warband not found!")
            else:
                print("OS not supported for auto-build!")




def create_modules():
    # Module InfoPage
    InfoPageConverter().createCode()

    # Module Strings
    StringConverter().createCode()

    # Module Music
    MusicConverter().createCode()

    # Module Meshes
    MeshConverter().createCode()

    # Module Sounds
    SoundConverter().createCode()

    # Module Factions
    FactionConverter().createCode()

    # Module Scenes
    SceneConverter().createCode()

    # Module Particle System
    ParticleSystemConverter().createCode()

    # Module Skins
    SkinConverter().createCode()

    # Module Animations
    AnimationConverter().createCode()

    # Module PostFX
    PostFXConverter().createCode()

    # Module Quests
    QuestConverter().createCode()

    # Module Tableau Materials
    TableauMaterialConverter().createCode()

    # Module Scripts
    ScriptConverter().createCode()

    # Module Simple Triggers
    SimpleTriggerConverter().createCode()

    # Module Triggers
    TriggerConverter().createCode()

    # Module Map Icons
    MapIconConverter().createCode()

    # Module Party Templates
    PartyTemplateConverter().createCode()

    # Module Parties
    PartyConverter().createCode()

    # Module Game Menus
    GameMenuConverter().createCode()

    # Module Skills
    SkillConverter().createCode()

    # Module Items
    ItemConverter().createCode()

    # Module Troops
    TroopConverter().createCode()

    # Module Mission Template
    MissionTemplateConverter().createCode()

    # Module Dialogs
    DialogConverter().createCode()

    # Module Scene Props
    ScenePropConverter().createCode()

    # Module Presentations
    PresentationConverter().createCode()



import trans_items as transItems
def create_translations():
    transItems.createTranslations()



if __name__ == "__main__":
    handle_pre_module_arguments(sys.argv)

    create_translations()
    create_modules()

    handle_post_module_arguments(sys.argv)
    sys.exit()

