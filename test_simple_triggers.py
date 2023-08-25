# This Python file uses the following encoding: utf-8
from simple_trigger import SimpleTrigger


class Trigger1(SimpleTrigger):
    def codeBlock(self):
        if is_edit_mode_enabled():
            print("Hello World")



class Trigger2(SimpleTrigger):
    def codeBlock(self):
        fishCount = 1
        waterLevel = 1
        versionx = get_operation_set_version()
        if versionx > 0 and versionx <= 1101:
            banner_id = profile_get_banner_id()
            if banner_id > 20 or banner_id == 0 or banner_id == 10:
                print(versionx)
                if versionx == 1011:
                    print("YES!")
                else:
                    print("Nope")
                    print("DOPE")



trigger1 = Trigger1(24)
trigger2 = Trigger2(12)

