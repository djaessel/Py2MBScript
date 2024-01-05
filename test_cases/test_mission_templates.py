# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from test_items import *
from mission_template import MissionTemplate, SpawnRecord, AIFlag, AlterFlag, SpawnFlag, MissionTemplateFlag

from trigger import Trigger


mission1 = MissionTemplate("my_mission", description="My super mission!")
mission1.add_flag(MissionTemplateFlag.BATTLE_MODE)

sr = SpawnRecord(0, 1, [axe, master_shield])
sr.add_spawn_flag(SpawnFlag.TEAM_0)
sr.add_spawn_flag(SpawnFlag.DEFENDERS)
#sr.add_spawn_flag(SpawnFlag.SCENE_SOURCE)
sr.add_alter_flag(AlterFlag.OVERRIDE_ALL)
mission1.addSpawnRecord(sr)

sr = SpawnRecord(1, 4, [axe, master_shield])
sr.add_spawn_flag(SpawnFlag.TEAM_1)
sr.add_spawn_flag(SpawnFlag.ATTACKERS)
#sr.add_spawn_flag(SpawnFlag.SCENE_SOURCE)
sr.add_alter_flag(AlterFlag.OVERRIDE_ALL)
mission1.addSpawnRecord(sr)

triggyx = Trigger(-20.0, 0, 0)
def condition():
    if reg1 == 0 or reg1 == 2:
        if reg0 == 0:
            print("EXTRA SAFE!")

def code():
    reg0 = 30
    print(reg0)

triggyx.conditionBlock = condition
triggyx.codeBlock = code
mission1.add_trigger(triggyx)

triggyx = Trigger(-21.0,0,0)
def code():
    #finish_mission(0)
    #change_screen_return()
    set_trigger_result(1)

triggyx.codeBlock = code
mission1.add_trigger(triggyx)
