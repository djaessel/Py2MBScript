# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")


from faction import Faction


# Factions
no_faction = Faction("no_faction", "No Faction", 0.9)
commoners = Faction("commoners", "Commoners", 0.1)
neutral = Faction("neutral", "Neutral", 0.1)
outlaws = Faction("outlaws", "Outlaws", 0.1)
player_faction = Faction("player_faction", "Player Faction", 0.9)
player_supporters_faction = Faction("player_supporters_faction", "Player Supporters Faction", 0.9)


# Faction Relations
player_supporters_faction.add_relation(player_faction, 0.9)
player_faction.add_relation(player_supporters_faction, 0.9)

