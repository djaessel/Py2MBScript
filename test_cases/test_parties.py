# This Python file uses the following encoding: utf-8

from MBParty import MBParty, PartyFlag
import test_map_icons as icon


main_party = MBParty("main_party", "Main Party", faction="fac_player_faction", initial_cords=(17,20))
main_party.set_icon(icon.player)
main_party.add_flag(PartyFlag.LIMIT_MEMBERS)
main_party.add_members("trp_player", 1)

temp_party = MBParty("temp_party", "{!}temp_party", faction="fac_commoners")
temp_party.add_flag(PartyFlag.IS_DISABLED)

camp_bandits = MBParty("camp_bandits", "{!}camp_bandits", faction="fac_outlaws", initial_cords=(1,1))
camp_bandits.add_flag(PartyFlag.IS_DISABLED)
#camp_bandits.add_members("trp_temp_troop", 3)

test1 = MBParty("test_town", "Test Town", initial_cords=(120.4,57.3))
test1.set_icon(icon.town)
test1.add_flag(PartyFlag.IS_TOWN)
test1.add_members("trp_looter", 20)
test1.add_prisoners("trp_npc1", 1)


