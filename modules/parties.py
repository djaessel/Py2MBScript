# This Python file uses the following encoding: utf-8

from MBParty import MBParty, PartyFlag
import map_icons as icon
import factions as fac


main_party = MBParty("main_party", "Main Party", faction=fac.player_faction, initial_cords=(17,20))
main_party.set_icon(icon.player)
main_party.add_flag(PartyFlag.LIMIT_MEMBERS)
main_party.add_members("trp_player", 1)

temp_party = MBParty("temp_party", "{!}temp_party", faction=fac.commoners)
temp_party.add_flag(PartyFlag.IS_DISABLED)

camp_bandits = MBParty("camp_bandits", "{!}camp_bandits", faction=fac.outlaws, initial_cords=(1,1))
camp_bandits.add_flag(PartyFlag.IS_DISABLED)
#camp_bandits.add_members("trp_temp_troop", 3)

###################################################################
# Parties above this point are hardwired/hardcoded into the game! #
###################################################################

test1 = MBParty("test_town", "Test Town", initial_cords=(12,20))
test1.set_icon(icon.town)
test1.add_flag(PartyFlag.IS_TOWN)
test1.add_members("trp_looter", 20)
#test1.add_prisoners("trp_npc1", 1)


