# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")

from party_template import PartyTemplate

from test_troops import *


partyTemp1 = PartyTemplate("hunters", "Hunters")
partyTemp1.addStack(npc1, 1)
partyTemp1.addStack(npc2, 1, 2)


