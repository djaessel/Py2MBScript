# This Python file uses the following encoding: utf-8

from simple_trigger import SimpleTrigger


class Trigger(SimpleTrigger):
    def __init__(self, triggerInterval, delay, triggerPause):
        super().__init__(triggerInterval)
        self.delay = delay
        self.triggerPause = triggerPause

    def conditionBlock(self):
        pass

