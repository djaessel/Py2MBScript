# This Python file uses the following encoding: utf-8

from MBParty import MBParty


main_party = MBParty("main_party", "Main Party", faction="fac_player_faction", initial_cords=(17,20))
main_party.set_icon("icon_player")
main_party.add_members("trp_player", 1)

temp_party = MBParty("temp_party", "{!}temp_party", faction="fac_commoners")
temp_party.set_icon("pf_disabled")

camp_bandits = MBParty("camp_bandits", "{!}camp_bandits", faction="fac_outlaws", initial_cords=(1,1))
camp_bandits.set_icon("pf_disabled")
#main_party.add_members("trp_temp_troop", 3)

#("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),


test1 = MBParty("test_town", "Test Town", initial_cords=(120.4,57.3))
test1.set_icon("icon_town")
test1.add_members("trp_looter", 20)
test1.add_prisoners("trp_npc1", 1)


