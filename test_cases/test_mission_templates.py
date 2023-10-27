# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from test_items import *
from mission_template import MissionTemplate, SpawnRecord, AIFlag, AlterFlag, SpawnFlag, MissionTemplateFlag

from trigger import Trigger


mission1 = MissionTemplate("my_mission", description="My super mission!")
mission1.add_flag(MissionTemplateFlag.BATTLE_MODE)

sr = SpawnRecord(0, 24, [axe, master_shield])
sr.add_spawn_flag(SpawnFlag.TEAM_0)
sr.add_spawn_flag(SpawnFlag.DEFENDERS)
mission1.addSpawnRecord(sr)

sr = SpawnRecord(1, 24, [axe])
sr.add_spawn_flag(SpawnFlag.TEAM_1)
sr.add_spawn_flag(SpawnFlag.ATTACKERS)
mission1.addSpawnRecord(sr)

triggyx = Trigger(-20.0, 0, 0)
def code():
    reg0 = 30
    print(reg0)

triggyx.codeBlock = code
mission1.add_trigger(triggyx)