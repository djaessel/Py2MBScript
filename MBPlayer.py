# This Python file uses the following encoding: utf-8


class MBPlayer:
    id = ""
    active = True
    teamNo = 0
    troopId = 0
    agentId = 1
    gold = 0

    def __init__(self, player_id):
        self.id = player_id

    def isActive(self):
        return self.active

    def getTeamNo(self):
        return self.teamNo

    def setTeamNo(self, teamNo):
        self.teamNo = teamNo

    def getTroopId(self):
        return self.troopId

    def setTroopId(self, troopId):
        self.troopId = troopId

    def getAgentId(self):
        return self.agentId

    def getGold(self):
        return self.gold

    def setGold(self, gold, maxValue):
        if gold > maxValue and maxValue > 0:
            gold = maxValue
        self.gold = gold

    def spawnNewAgent(entryPoint):
        print("Spawn at", entryPoint)

    def addSpawnItem(itemSlotNo, itemId):
        print("Add", itemId, "for slot", itemSlotNo)

        player_control_agent                 = 421 # (player_control_agent, <player_id>, <agent_id>),
        player_get_item_id                   = 422 # (player_get_item_id, <destination>, <player_id>, <item_slot_no>), #only for server
        player_get_banner_id                 = 423 # (player_get_banner_id, <destination>, <player_id>),
        player_set_is_admin                  = 429 # (player_set_is_admin, <player_id>, <value>), #value is 0 or 1
        player_is_admin                      = 430 # (player_is_admin, <player_id>),
        player_get_score                     = 431 # (player_get_score, <destination>, <player_id>),
        player_set_score                     = 432 # (player_set_score,<player_id>, <value>),
        player_get_kill_count                = 433 # (player_get_kill_count, <destination>, <player_id>),
        player_set_kill_count                = 434 # (player_set_kill_count,<player_id>, <value>),
        player_get_death_count               = 435 # (player_get_death_count, <destination>, <player_id>),
        player_set_death_count               = 436 # (player_set_death_count, <player_id>, <value>),
        player_get_ping                      = 437 # (player_get_ping, <destination>, <player_id>),
        player_is_busy_with_menus            = 438 # (player_is_busy_with_menus, <player_id>),
        player_get_is_muted                  = 439 # (player_get_is_muted, <destination>, <player_id>),
        player_set_is_muted                  = 440 # (player_set_is_muted, <player_id>, <value>, [mute_for_everyone]), #mute_for_everyone optional parameter should be set to 1 if player is muted for everyone (this works only on server).
        player_get_unique_id                 = 441 # (player_get_unique_id, <destination>, <player_id>), #can only bew used on server side
        player_get_gender                    = 442 # (player_get_gender, <destination>, <player_id>),
        player_save_picked_up_items_for_next_spawn  = 459 # (player_save_picked_up_items_for_next_spawn, <player_id>),
        player_get_value_of_original_items   = 460 # (player_get_value_of_original_items, <player_id>), #this operation returns values of the items, but default troop items will be counted as zero (except horse)
        player_item_slot_is_picked_up        = 461 # (player_item_slot_is_picked_up, <player_id>, <item_slot_no>), #item slots are overriden when player picks up an item and stays alive until the next round


