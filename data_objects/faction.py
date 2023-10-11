# This Python file uses the following encoding: utf-8


class Faction:
    def __init__(self, id : str, name : str, coherence : float = 0.1, color : int = 0xaaaaaa, always_hide_label : bool = False, max_player_rating : int = 100):
        self.id = id
        self.name = name
        self.coherence = coherence
        self.color = color
        self.always_hide_label = always_hide_label
        self.max_player_rating = max_player_rating
        self.relations = []
        self.ranks = []


    def add_relation(self, faction, relation : float):
        self.relations.append((faction, relation))


    def add_rank(self, rank):
        self.ranks.append(rank)
        print("Not fully supported feature:")
        print(">> Faction > Ranks")


