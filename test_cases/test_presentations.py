# This Python file uses the following encoding: utf-8


import sys
sys.path.append("../data_objects/")

from presentation import Presentation
from simple_trigger import SimpleTrigger


presy1 = Presentation("test1")

# TODO: create extra triggers here for events
qualcom = SimpleTrigger(-60.0)

def load_event():
    print("Hello World! - {s0}")

qualcom.codeBlock = load_event
presy1.add_trigger(qualcom)

qualcom2 = SimpleTrigger(-61.0)

def load_event():
    print("Hello World!!!")

qualcom2.codeBlock = load_event
presy1.add_trigger(qualcom2)
