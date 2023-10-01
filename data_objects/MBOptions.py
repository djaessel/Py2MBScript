# This Python file uses the following encoding: utf-8


class MBOptions:
    damageToPlayer = 0
    damageToFriends = 0
    combatAI = 0
    campaignAI = 0
    combatSpeed = 0
    battleSize = 200

    def __init__(self):
        pass

    def get_damage_to_player(self):
        return self.damageToPlayer

    def set_damage_to_player(self, value):
        self.damageToPlayer = value

    def get_damage_to_friends(self):
        return self.damageToFriends

    def set_damage_to_friends(self, value):
        self.damageToFriends = value

    def get_combat_ai(self):
        return self.combatAI

    def set_combat_ai(self, value):
        self.combatAI = value

    def get_campaign_ai(self):
        return self.campaignAI

    def set_campaign_ai(self, value):
        self.campaignAI = value

    def get_combat_speed(self):
        return self.combatSpeed

    def set_combat_speed(self, value):
        self.combatSpeed = value

    def get_battle_size(self):
        return self.battleSize

    def set_battle_size(self, value):
        self.battleSize = value

