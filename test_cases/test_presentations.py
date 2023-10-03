# This Python file uses the following encoding: utf-8


import sys
sys.path.append("../data_objects/")

from presentation import Presentation, LoadEvent, MouseEnterLeaveEvent, RunEvent, MousePressEvent, StateChangedEvent
from simple_trigger import SimpleTrigger


presy1 = Presentation("test1")

qualcom = LoadEvent()
def event_code():
    print("Hello World! - {s0}")

qualcom.codeBlock = event_code
presy1.add_trigger(qualcom)

qualcom2 = StateChangedEvent()
def event_code():
    print("Hello World!!!")

qualcom2.codeBlock = event_code
presy1.add_trigger(qualcom2)
