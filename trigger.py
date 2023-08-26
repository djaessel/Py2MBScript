# This Python file uses the following encoding: utf-8

from simple_trigger import SimpleTrigger


class Trigger(SimpleTrigger):
    triggerVal2 = 0.0
    triggerPause = 0.0

    def __init__(self, triggerInterval, triggerVal2, triggerPause):
        super().__init__(triggerInterval)
        self.triggerVal2 = triggerVal2
        self.triggerPause = triggerPause

    def conditionBlock(self):
        pass

