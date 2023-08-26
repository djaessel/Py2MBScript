# This Python file uses the following encoding: utf-8
from trigger import Trigger


class Trigger1(Trigger):
    def conditionBlock(self):
        is_edit_mode_enabled()
        water = 1
        if 1 == 1:
            water = 4

        print(water)

    def codeBlock(self):
        print("Hello World!")


class Trigger2(Trigger):
    def codeBlock(self):
        fishCount = 1
        waterLevel = 1
        versionx = get_operation_set_version()

        if versionx > 0 and versionx <= 1101:
            print(versionx)

        for waterLevel in range(waterLevel, 19):
            print(waterLevel)
            for fishCount in range(fishCount, 12):
                print(fishCount)



trigger1 = Trigger1(24, 0, 0)
trigger2 = Trigger2(12, 0, 0)

