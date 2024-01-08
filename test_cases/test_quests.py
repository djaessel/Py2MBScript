# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from quest import Quest


quest1 = Quest("quest1", "Quest 1 here!", "You have to do nothing here for now.")


quests_end = Quest("quests_end", "Quests End", "{!}.")
