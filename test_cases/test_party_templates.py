# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")

from party_template import PartyTemplate

import troops as trp


partyTempDummy = PartyTemplate("dummy", "Dummy")


partyTemp1 = PartyTemplate("hunters", "Hunters")
partyTemp1.addStack(trp.npc1, 1)
partyTemp1.addStack(trp.looter, 1, 2)


