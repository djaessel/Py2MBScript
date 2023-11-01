# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")


from scene_prop import SceneProp
from simple_trigger import SimpleTrigger


scp1 = SceneProp("my_first", "my_first", "bo_my_first")
scp1.set_hit_points(1)
scp1.set_use_time(20)

triggy = SimpleTrigger(-21)
def code():
    print(reg1)

triggy.codeBlock = code
scp1.add_trigger(triggy)


