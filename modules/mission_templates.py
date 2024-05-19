# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

import items as itm
from mission_template import MissionTemplate, SpawnRecord, AIFlag, AlterFlag, SpawnFlag, MissionTemplateFlag

import header_triggers as tri
from trigger import Trigger


# COMMON TRIGGERS

common_arena_fight_tab_press = Trigger(tri.ti_tab_pressed, 0, 0)
def code():
    question_box(gstr.give_up_fight)
common_arena_fight_tab_press.codeBlock = code


common_inventory_not_available = Trigger(tri.ti_inventory_key_pressed, 0, 0)
def code():
    print(gstr.cant_use_inventory_now)
common_inventory_not_available.codeBlock = code



# MISSION TEMPLATES

village_training = MissionTemplate("village_training", description="village_training")
village_training.add_flag(MissionTemplateFlag.ARENA_FIGHT)
#---
# spawn record 0
sr = SpawnRecord(2, 1, []) # itm_practice_staff, itm_practice_boots
sr.add_spawn_flag(SpawnFlag.TEAM_0)
sr.add_spawn_flag(SpawnFlag.VISITOR_SOURCE)
sr.add_alter_flag(AlterFlag.OVERRIDE_EVERYTHING)
sr.addItem(itm.practice_boots)
sr.addItem(itm.practice_staff)
village_training.addSpawnRecord(sr)
# spawn record 1
sr2 = SpawnRecord(4, 1, []) # itm_practice_staff, itm_practice_boots
sr2.add_spawn_flag(SpawnFlag.TEAM_1)
sr2.add_spawn_flag(SpawnFlag.VISITOR_SOURCE)
sr2.add_alter_flag(AlterFlag.OVERRIDE_EVERYTHING)
sr2.addItem(itm.practice_boots)
sr2.addItem(itm.practice_staff)
village_training.addSpawnRecord(sr2)
#---
# trigger 1
triggyx = Trigger(tri.ti_before_mission_start,0,0)
def code():
    pass
triggyx.codeBlock = code
village_training.add_trigger(triggyx)
#---
# trigger 3
village_training.add_trigger(common_arena_fight_tab_press)
#---
# trigger 3
triggyx = Trigger(tri.ti_question_answered,0,0)
def code():
    answer = store_trigger_param_1()
    if answer == 0:
        finish_mission(0)
triggyx.codeBlock = code
village_training.add_trigger(triggyx)
#---
# trigger 4
village_training.add_trigger(common_inventory_not_available)
#---
# trigger 5
triggyx = Trigger(1, 4, tri.ti_once)
def condition():
    if main_hero_fallen() or num_active_teams_le(1):
        pass
triggyx.conditionBlock = condition
def code():
    if not main_hero_fallen():
        pass
    finish_mission(0)
triggyx.codeBlock = code
village_training.add_trigger(triggyx)




