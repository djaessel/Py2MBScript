# This Python file uses the following encoding: utf-8


class MBPlayer:
    id = ""
    active = True
    isMuted = False
    teamNo = 0
    troopId = 0
    agentId = 1
    gold = 0
    score = 0
    killCount = 0
    deathCount = 0
    isAdmin = False
    itemSlots = [0,0,0,0,0,0,0,0,0,0]

    def __init__(self, player_id):
        self.id = player_id

    def is_active(self):
        return self.active

    def get_team_no(self):
        return self.teamNo

    def set_team_no(self, teamNo):
        self.teamNo = teamNo

    def get_troop_id(self):
        return self.troopId

    def set_troop_id(self, troopId):
        self.troopId = troopId

    def get_agent_id(self):
        return self.agentId

    def get_gold(self):
        return self.gold

    def set_gold(self, gold, maxValue):
        if gold > maxValue and maxValue > 0:
            gold = maxValue
        self.gold = gold

    def spawn_new_agent(self, entryPoint):
        print("Spawn at", entryPoint)

    def add_spawn_item(self, itemSlotNo, itemId):
        print("Add", itemId, "for slot", itemSlotNo)

    def control_agent(self, agentId):
        print("Control agent", agentId)

    def get_item_id(self, itemSlotNo): # only for server
        return self.itemSlots[itemSlotNo]

    def get_banner_id(self):
        return 0

    def set_is_admin(self, value):
        self.isAdmin = value

    def is_admin(self):
        return self.isAdmin

    def get_score(self):
        return self.score

    def set_score(self, value):
        self.score = value

    def get_kill_count(self):
        return self.killCount

    def set_kill_count(self, value):
        self.killCount = value

    def get_death_count(self):
        return self.deathCount

    def set_death_count(self, value):
        self.deathCount = value

    def get_ping():
        return 23

    def is_busy_with_menus():
        return False

    def get_is_muted(self):
        return self.isMuted

    def set_is_muted(self, value):
        self.isMuted = value

    def get_unique_id():
        return 12345678

    def get_gender():
        return 0 # skin id?

    def save_picked_up_items_for_next_spawn():
        print("Save picked up items for next spawn!")

    def get_value_of_original_items():
        return 2

    def item_slot_is_picked_up(itemSlotNo):
        return False

