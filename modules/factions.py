# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")


from faction import Faction


# Factions
no_faction = Faction("no_faction", "No_Faction", coherence=0.9)

commoners = Faction("commoners", "Commoners")

outlaws = Faction("outlaws", "Outlaws", coherence=0.5, color=0x888888, max_player_rating=130)

neutral = Faction("neutral", "Neutral", color=0xffffff)

innocents = Faction("innocents", "Innocents", coherence=0.5, always_hide_label=True)

merchants = Faction("merchants", "Merchants", coherence=0.5, always_hide_label=True)

dark_knights = Faction("dark_knights", "{!}Dark_Knights", coherence=0.5)

culture_1 = Faction("culture_1", "{!}culture_1", coherence=0.9)

culture_2 = Faction("culture_2", "{!}culture_2", coherence=0.9)

culture_3 = Faction("culture_3", "{!}culture_3", coherence=0.9)

culture_4 = Faction("culture_4", "{!}culture_4", coherence=0.9)

culture_5 = Faction("culture_5", "{!}culture_5", coherence=0.9)

culture_6 = Faction("culture_6", "{!}culture_6", coherence=0.9)

player_faction = Faction("player_faction", "Player_Faction", coherence=0.9)

player_supporters_faction = Faction("player_supporters_faction", "Player's_Supporters", coherence=0.9, color=0xff4433)

kingdom_1 = Faction("kingdom_1", "Kingdom_of_Swadia", coherence=0.9, color=0xee7744)

kingdom_2 = Faction("kingdom_2", "Kingdom_of_Vaegirs", coherence=0.9, color=0xccbb99)

kingdom_3 = Faction("kingdom_3", "Khergit_Khanate", coherence=0.9, color=0xcc99ff)

kingdom_4 = Faction("kingdom_4", "Kingdom_of_Nords", coherence=0.9, color=0x33dddd)

kingdom_5 = Faction("kingdom_5", "Kingdom_of_Rhodoks", coherence=0.9, color=0x33dd33)

kingdom_6 = Faction("kingdom_6", "Sarranid_Sultanate", coherence=0.9, color=0xdddd33)

kingdoms_end = Faction("kingdoms_end", "{!}kingdoms_end", coherence=0.0)

robber_knights = Faction("robber_knights", "{!}robber_knights")

khergits = Faction("khergits", "{!}Khergits", coherence=0.5)

black_khergits = Faction("black_khergits", "{!}Black_Khergits", coherence=0.5)

manhunters = Faction("manhunters", "Manhunters", coherence=0.5)

deserters = Faction("deserters", "Deserters", coherence=0.5, color=0x888888)

mountain_bandits = Faction("mountain_bandits", "Mountain_Bandits", coherence=0.5, color=0x888888)

forest_bandits = Faction("forest_bandits", "Forest_Bandits", coherence=0.5, color=0x888888)

undeads = Faction("undeads", "{!}Undeads", coherence=0.5, max_player_rating=130)

slavers = Faction("slavers", "{!}Slavers")

peasant_rebels = Faction("peasant_rebels", "{!}Peasant_Rebels", coherence=1.0)

noble_refugees = Faction("noble_refugees", "{!}Noble_Refugees", coherence=0.5)

ccoop_all_stars = Faction("ccoop_all_stars", "All_Stars", coherence=0.5)



# Relations

commoners.add_relation(outlaws, -0.6)
commoners.add_relation(player_faction, 0.1)
commoners.add_relation(mountain_bandits, -0.2)
commoners.add_relation(forest_bandits, -0.2)
commoners.add_relation(undeads, -0.7)

outlaws.add_relation(commoners, -0.6)
outlaws.add_relation(innocents, -0.05)
outlaws.add_relation(merchants, -0.5)
outlaws.add_relation(player_faction, -0.15)
outlaws.add_relation(player_supporters_faction, -0.05)
outlaws.add_relation(kingdom_1, -0.05)
outlaws.add_relation(kingdom_2, -0.05)
outlaws.add_relation(kingdom_3, -0.05)
outlaws.add_relation(kingdom_4, -0.05)
outlaws.add_relation(kingdom_5, -0.05)
outlaws.add_relation(kingdom_6, -0.05)
outlaws.add_relation(manhunters, -0.6)

innocents.add_relation(outlaws, -0.05)
innocents.add_relation(dark_knights, -0.9)

merchants.add_relation(outlaws, -0.5)
merchants.add_relation(deserters, -0.5)
merchants.add_relation(mountain_bandits, -0.5)
merchants.add_relation(forest_bandits, -0.5)

dark_knights.add_relation(innocents, -0.9)
dark_knights.add_relation(player_faction, -0.4)

player_faction.add_relation(commoners, 0.1)
player_faction.add_relation(outlaws, -0.15)
player_faction.add_relation(dark_knights, -0.4)
player_faction.add_relation(player_supporters_faction, 1.0)
player_faction.add_relation(black_khergits, -0.3)
player_faction.add_relation(manhunters, 0.1)
player_faction.add_relation(deserters, -0.1)
player_faction.add_relation(mountain_bandits, -0.15)
player_faction.add_relation(forest_bandits, -0.15)
player_faction.add_relation(undeads, -0.5)
player_faction.add_relation(peasant_rebels, -0.4)

player_supporters_faction.add_relation(outlaws, -0.05)
player_supporters_faction.add_relation(player_faction, 1.0)
player_supporters_faction.add_relation(deserters, -0.02)
player_supporters_faction.add_relation(mountain_bandits, -0.05)
player_supporters_faction.add_relation(forest_bandits, -0.05)
player_supporters_faction.add_relation(peasant_rebels, -0.1)

kingdom_1.add_relation(outlaws, -0.05)
kingdom_1.add_relation(black_khergits, -0.02)
kingdom_1.add_relation(deserters, -0.02)
kingdom_1.add_relation(mountain_bandits, -0.05)
kingdom_1.add_relation(forest_bandits, -0.05)
kingdom_1.add_relation(peasant_rebels, -0.1)

kingdom_2.add_relation(outlaws, -0.05)
kingdom_2.add_relation(black_khergits, -0.02)
kingdom_2.add_relation(deserters, -0.02)
kingdom_2.add_relation(mountain_bandits, -0.05)
kingdom_2.add_relation(forest_bandits, -0.05)
kingdom_2.add_relation(peasant_rebels, -0.1)

kingdom_3.add_relation(outlaws, -0.05)
kingdom_3.add_relation(deserters, -0.02)
kingdom_3.add_relation(mountain_bandits, -0.05)
kingdom_3.add_relation(forest_bandits, -0.05)
kingdom_3.add_relation(peasant_rebels, -0.1)

kingdom_4.add_relation(outlaws, -0.05)
kingdom_4.add_relation(deserters, -0.02)
kingdom_4.add_relation(mountain_bandits, -0.05)
kingdom_4.add_relation(forest_bandits, -0.05)
kingdom_4.add_relation(peasant_rebels, -0.1)

kingdom_5.add_relation(outlaws, -0.05)
kingdom_5.add_relation(deserters, -0.02)
kingdom_5.add_relation(mountain_bandits, -0.05)
kingdom_5.add_relation(forest_bandits, -0.05)
kingdom_5.add_relation(peasant_rebels, -0.1)

kingdom_6.add_relation(outlaws, -0.05)
kingdom_6.add_relation(deserters, -0.02)
kingdom_6.add_relation(mountain_bandits, -0.05)
kingdom_6.add_relation(forest_bandits, -0.05)
kingdom_6.add_relation(peasant_rebels, -0.1)

black_khergits.add_relation(player_faction, -0.3)
black_khergits.add_relation(kingdom_1, -0.02)
black_khergits.add_relation(kingdom_2, -0.02)

manhunters.add_relation(outlaws, -0.6)
manhunters.add_relation(player_faction, 0.1)
manhunters.add_relation(deserters, -0.6)
manhunters.add_relation(mountain_bandits, -0.6)
manhunters.add_relation(forest_bandits, -0.6)

deserters.add_relation(merchants, -0.5)
deserters.add_relation(player_faction, -0.1)
deserters.add_relation(player_supporters_faction, -0.02)
deserters.add_relation(kingdom_1, -0.02)
deserters.add_relation(kingdom_2, -0.02)
deserters.add_relation(kingdom_3, -0.02)
deserters.add_relation(kingdom_4, -0.02)
deserters.add_relation(kingdom_5, -0.02)
deserters.add_relation(kingdom_6, -0.02)
deserters.add_relation(manhunters, -0.6)

mountain_bandits.add_relation(commoners, -0.2)
mountain_bandits.add_relation(merchants, -0.5)
mountain_bandits.add_relation(player_faction, -0.15)
mountain_bandits.add_relation(player_supporters_faction, -0.05)
mountain_bandits.add_relation(kingdom_1, -0.05)
mountain_bandits.add_relation(kingdom_2, -0.05)
mountain_bandits.add_relation(kingdom_3, -0.05)
mountain_bandits.add_relation(kingdom_4, -0.05)
mountain_bandits.add_relation(kingdom_5, -0.05)
mountain_bandits.add_relation(kingdom_6, -0.05)
mountain_bandits.add_relation(manhunters, -0.6)

forest_bandits.add_relation(commoners, -0.2)
forest_bandits.add_relation(merchants, -0.5)
forest_bandits.add_relation(player_faction, -0.15)
forest_bandits.add_relation(player_supporters_faction, -0.05)
forest_bandits.add_relation(kingdom_1, -0.05)
forest_bandits.add_relation(kingdom_2, -0.05)
forest_bandits.add_relation(kingdom_3, -0.05)
forest_bandits.add_relation(kingdom_4, -0.05)
forest_bandits.add_relation(kingdom_5, -0.05)
forest_bandits.add_relation(kingdom_6, -0.05)
forest_bandits.add_relation(manhunters, -0.6)

undeads.add_relation(commoners, -0.7)
undeads.add_relation(player_faction, -0.5)

peasant_rebels.add_relation(player_faction, -0.4)
peasant_rebels.add_relation(player_supporters_faction, -0.1)
peasant_rebels.add_relation(kingdom_1, -0.1)
peasant_rebels.add_relation(kingdom_2, -0.1)
peasant_rebels.add_relation(kingdom_3, -0.1)
peasant_rebels.add_relation(kingdom_4, -0.1)
peasant_rebels.add_relation(kingdom_5, -0.1)
peasant_rebels.add_relation(kingdom_6, -0.1)
peasant_rebels.add_relation(noble_refugees, -1.0)

noble_refugees.add_relation(peasant_rebels, -1.0)

