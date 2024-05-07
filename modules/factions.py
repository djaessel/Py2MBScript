# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")


from faction import Faction


# Factions
fac_no_faction = Faction("fac_no_faction", "No_Faction", coherence=0.9)

fac_commoners = Faction("fac_commoners", "Commoners")

fac_outlaws = Faction("fac_outlaws", "Outlaws", coherence=0.5, color=0x888888, max_player_rating=130)

fac_neutral = Faction("fac_neutral", "Neutral", color=0xffffff)

fac_innocents = Faction("fac_innocents", "Innocents", coherence=0.5, always_hide_label=True)

fac_merchants = Faction("fac_merchants", "Merchants", coherence=0.5, always_hide_label=True)

fac_dark_knights = Faction("fac_dark_knights", "{!}Dark_Knights", coherence=0.5)

fac_culture_1 = Faction("fac_culture_1", "{!}culture_1", coherence=0.9)

fac_culture_2 = Faction("fac_culture_2", "{!}culture_2", coherence=0.9)

fac_culture_3 = Faction("fac_culture_3", "{!}culture_3", coherence=0.9)

fac_culture_4 = Faction("fac_culture_4", "{!}culture_4", coherence=0.9)

fac_culture_5 = Faction("fac_culture_5", "{!}culture_5", coherence=0.9)

fac_culture_6 = Faction("fac_culture_6", "{!}culture_6", coherence=0.9)

fac_player_faction = Faction("fac_player_faction", "Player_Faction", coherence=0.9)

fac_player_supporters_faction = Faction("fac_player_supporters_faction", "Player's_Supporters", coherence=0.9, color=0xff4433)

fac_kingdom_1 = Faction("fac_kingdom_1", "Kingdom_of_Swadia", coherence=0.9, color=0xee7744)

fac_kingdom_2 = Faction("fac_kingdom_2", "Kingdom_of_Vaegirs", coherence=0.9, color=0xccbb99)

fac_kingdom_3 = Faction("fac_kingdom_3", "Khergit_Khanate", coherence=0.9, color=0xcc99ff)

fac_kingdom_4 = Faction("fac_kingdom_4", "Kingdom_of_Nords", coherence=0.9, color=0x33dddd)

fac_kingdom_5 = Faction("fac_kingdom_5", "Kingdom_of_Rhodoks", coherence=0.9, color=0x33dd33)

fac_kingdom_6 = Faction("fac_kingdom_6", "Sarranid_Sultanate", coherence=0.9, color=0xdddd33)

fac_kingdoms_end = Faction("fac_kingdoms_end", "{!}kingdoms_end", coherence=0.0)

fac_robber_knights = Faction("fac_robber_knights", "{!}robber_knights")

fac_khergits = Faction("fac_khergits", "{!}Khergits", coherence=0.5)

fac_black_khergits = Faction("fac_black_khergits", "{!}Black_Khergits", coherence=0.5)

fac_manhunters = Faction("fac_manhunters", "Manhunters", coherence=0.5)

fac_deserters = Faction("fac_deserters", "Deserters", coherence=0.5, color=0x888888)

fac_mountain_bandits = Faction("fac_mountain_bandits", "Mountain_Bandits", coherence=0.5, color=0x888888)

fac_forest_bandits = Faction("fac_forest_bandits", "Forest_Bandits", coherence=0.5, color=0x888888)

fac_undeads = Faction("fac_undeads", "{!}Undeads", coherence=0.5, max_player_rating=130)

fac_slavers = Faction("fac_slavers", "{!}Slavers")

fac_peasant_rebels = Faction("fac_peasant_rebels", "{!}Peasant_Rebels", coherence=1.0)

fac_noble_refugees = Faction("fac_noble_refugees", "{!}Noble_Refugees", coherence=0.5)

fac_ccoop_all_stars = Faction("fac_ccoop_all_stars", "All_Stars", coherence=0.5)




# Faction Relations
player_supporters_faction.add_relation(player_faction, 0.9)
player_faction.add_relation(player_supporters_faction, 0.9)

# TODO: add relations

