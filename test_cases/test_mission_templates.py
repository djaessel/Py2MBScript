# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from items import *
from mission_template import MissionTemplate, SpawnRecord, AIFlag, AlterFlag, SpawnFlag, MissionTemplateFlag

import header_triggers as tri
from trigger import Trigger


mission1 = MissionTemplate("my_mission", description="My super mission!")
mission1.add_flag(MissionTemplateFlag.BATTLE_MODE)
#---
# spawn record 0
sr = SpawnRecord(0, 1, [])
sr.add_spawn_flag(SpawnFlag.TEAM_1)
sr.add_spawn_flag(SpawnFlag.DEFENDERS)
#sr.add_spawn_flag(SpawnFlag.SCENE_SOURCE)
sr.add_alter_flag(AlterFlag.OVERRIDE_ALL)
mission1.addSpawnRecord(sr)
# spawn record 1
sr2 = SpawnRecord(1, 1, [])
sr2.add_spawn_flag(SpawnFlag.TEAM_0)
sr2.add_spawn_flag(SpawnFlag.ATTACKERS)
#sr2.add_spawn_flag(SpawnFlag.SCENE_SOURCE)
sr2.add_alter_flag(AlterFlag.OVERRIDE_ALL)
mission1.addSpawnRecord(sr2)
#---
# trigger 1
triggyx = Trigger(tri.ti_tab_pressed,0,0)
def code():
    set_trigger_result(1)
triggyx.codeBlock = code
mission1.add_trigger(triggyx)
#---
# trigger 2
triggyx = Trigger(tri.ti_on_agent_knocked_down,0,0)
def code():
    print("One down!")
triggyx.codeBlock = code
mission1.add_trigger(triggyx)
