# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")

from MBPlayer import MBPlayer
from MBOptions import MBOptions
from MBParty import MBParty
from game_menu import GameMenu, MenuOption

from scripts import *


start_game_0 = GameMenu("start_game_0", 18374686479671624192,
"Welcome, adventurer, to Mount and Blade: Warband. Before beginning the game you must create your character. Remember that in the traditional medieval society depicted in the game, war and politics are usually dominated by male members of the nobility. That does not however mean that you should not choose to play a female character, or one who is not of noble birth. Male nobles may have a somewhat easier start, but women and commoners can attain all of the same goals -- and in fact may have a much more interesting if more challenging early game."
)

start_game_0_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.start_game_1)
start_game_0_continue.codeBlock = code

start_game_0_go_back = MenuOption("go_back", "Go back")
def code():
    change_screen_quit()
start_game_0_go_back.codeBlock = code



start_phase_2 = GameMenu("start_phase_2", 512,
"You hear about Calradia, a land torn between rival kingdoms battling each other for supremacy, a haven for knights and mercenaries,  cutthroats and adventurers, all willing to risk their lives in pursuit of fortune, power, or glory... In this land which holds great dangers and even greater opportunities, you believe you may leave your past behind and start a new life. You feel that finally, you hold the key of your destiny in your hands, free to choose as you will, and that whatever course you take, great adventures will await you. Drawn by the stories you hear about Calradia and its kingdoms, you..."
)

start_phase_2_town_1 = MenuOption("town_1", "join a caravan to Praven, in the Kingdom of Swadia.")
def code():
    _current_town = p.town_6
    _g_starting_town = _current_town
    _g_journey_string = gstr.journey_to_praven
    jump_to_menu(mnu.start_phase_2_5)
start_phase_2_town_1.codeBlock = code

start_phase_2_town_2 = MenuOption("town_2", "join a caravan to Reyvadin, in the Kingdom of the Vaegirs.")
def code():
    _current_town = p.town_8
    _g_starting_town = _current_town
    _g_journey_string = gstr.journey_to_reyvadin
    jump_to_menu(mnu.start_phase_2_5)
start_phase_2_town_2.codeBlock = code

start_phase_2_town_3 = MenuOption("town_3", "join a caravan to Tulga, in the Khergit Khanate.")
def code():
    _current_town = p.town_10
    _g_starting_town = _current_town
    _g_journey_string = gstr.journey_to_tulga
    jump_to_menu(mnu.start_phase_2_5)
start_phase_2_town_3.codeBlock = code

start_phase_2_town_4 = MenuOption("town_4", "take a ship to Sargoth, in the Kingdom of the Nords.")
def code():
    _current_town = p.town_1
    _g_starting_town = _current_town
    _g_journey_string = gstr.journey_to_sargoth
    jump_to_menu(mnu.start_phase_2_5)
start_phase_2_town_4.codeBlock = code

start_phase_2_town_5 = MenuOption("town_5", "take a ship to Jelkala, in the Kingdom of the Rhodoks.")
def code():
    _current_town = p.town_5
    _g_starting_town = _current_town
    _g_journey_string = gstr.journey_to_jelkala
    jump_to_menu(mnu.start_phase_2_5)
start_phase_2_town_5.codeBlock = code

start_phase_2_town_6 = MenuOption("town_6", "join a caravan to Shariz, in the Sarranid Sultanate.")
def code():
    _current_town = p.town_19
    _g_starting_town = _current_town
    _g_journey_string = gstr.journey_to_shariz
    jump_to_menu(mnu.start_phase_2_5)
start_phase_2_town_6.codeBlock = code

start_phase_2_tutorial_cheat = MenuOption("tutorial_cheat", "{!}CHEAT!")
def code():
    change_screen_return()
    _cheat_mode = 1
    set_show_messages(0)
    add_xp_to_troop(15000,trp.player)
    troop_raise_skill(trp.player,1,7)
    troop_raise_skill(trp.player,2,5)
    troop_raise_skill(trp.player,12,10)
    party_add_members(p.main_party,trp.swadian_knight,10)
    party_add_members(p.main_party,trp.vaegir_knight,10)
    party_add_members(p.main_party,trp.vaegir_archer,10)
    party_add_members(p.main_party,trp.swadian_sharpshooter,10)
    troop_add_item(trp.player,itm.scale_armor,0)
    troop_add_item(trp.player,itm.full_helm,0)
    troop_add_item(trp.player,itm.hafted_blade_b,0)
    troop_add_item(trp.player,itm.hafted_blade_a,0)
    troop_add_item(trp.player,itm.morningstar,0)
    troop_add_item(trp.player,itm.tutorial_spear,0)
    troop_add_item(trp.player,itm.tutorial_staff,0)
    troop_add_item(trp.player,itm.tutorial_staff_no_attack,0)
    troop_add_item(trp.player,itm.arena_lance,0)
    troop_add_item(trp.player,itm.practice_staff,0)
    troop_add_item(trp.player,itm.practice_lance,0)
    troop_add_item(trp.player,itm.practice_javelin,0)
    troop_add_item(trp.player,itm.scythe,0)
    troop_add_item(trp.player,itm.pitch_fork,0)
    troop_add_item(trp.player,itm.military_fork,0)
    troop_add_item(trp.player,itm.battle_fork,0)
    troop_add_item(trp.player,itm.boar_spear,0)
    troop_add_item(trp.player,itm.jousting_lance,0)
    troop_add_item(trp.player,itm.double_sided_lance,0)
    troop_add_item(trp.player,itm.glaive,0)
    troop_add_item(trp.player,itm.poleaxe,0)
    troop_add_item(trp.player,itm.polehammer,0)
    troop_add_item(trp.player,itm.staff,0)
    troop_add_item(trp.player,itm.quarter_staff,0)
    troop_add_item(trp.player,itm.iron_staff,0)
    troop_add_item(trp.player,itm.shortened_spear,0)
    troop_add_item(trp.player,itm.spear,0)
    troop_add_item(trp.player,itm.war_spear,0)
    troop_add_item(trp.player,itm.military_scythe,0)
    troop_add_item(trp.player,itm.light_lance,0)
    troop_add_item(trp.player,itm.lance,0)
    troop_add_item(trp.player,itm.heavy_lance,0)
    troop_add_item(trp.player,itm.great_lance,0)
    troop_add_item(trp.player,itm.pike,0)
    troop_add_item(trp.player,itm.ashwood_pike,0)
    troop_add_item(trp.player,itm.awlpike,0)
    troop_add_item(trp.player,itm.throwing_spears,0)
    troop_add_item(trp.player,itm.javelin,0)
    troop_add_item(trp.player,itm.jarid,0)
    troop_add_item(trp.player,itm.long_axe_b,0)
    set_show_messages(1)
    for scn_001 in range(scn.town_1_center, scn.castle_1_exterior):
        scene_set_slot(scn_001,0,1)
    #end
    get_player_party_morale_values()
    party_set_morale(p.main_party,reg0)
start_phase_2_tutorial_cheat.codeBlock = code



start_game_3 = GameMenu("start_game_3", 512,
"Choose your scenario:"
)
def condition():
    _g_custom_battle_scenario = 0
    _g_custom_battle_scenario = _g_custom_battle_scenario
start_game_3.conditionBlock = condition

start_game_3_go_back = MenuOption("go_back", "Go back")
def code():
    change_screen_quit()
start_game_3_go_back.codeBlock = code



tutorial = GameMenu("tutorial", 512,
"You approach a field where the locals are training with weapons. You can practice here to improve your combat skills."
)
def condition():
    if _g_tutorial_entered == 1:
        change_screen_quit()
    else:
        set_passage_menu(mnu.tutorial)
        _g_tutorial_entered = 1
    #end
tutorial.conditionBlock = condition

tutorial_continue = MenuOption("continue", "Continue...")
def code():
    modify_visitors_at_site(scn.tutorial_training_ground)
    reset_visitors(0)
    set_player_troop(trp.player)
    _g_player_troop = trp.player
    troop_raise_attribute(_g_player_troop,0,12)
    troop_raise_attribute(_g_player_troop,1,9)
    troop_raise_attribute(_g_player_troop,3,5)
    troop_raise_skill(_g_player_troop,26,3)
    troop_raise_skill(_g_player_troop,25,2)
    troop_raise_skill(_g_player_troop,24,3)
    troop_raise_skill(_g_player_troop,35,1)
    troop_raise_skill(_g_player_troop,33,5)
    troop_raise_skill(_g_player_troop,27,4)
    troop_raise_skill(_g_player_troop,36,1)
    troop_raise_skill(_g_player_troop,23,6)
    troop_raise_proficiency_linear(_g_player_troop,0,70)
    troop_raise_proficiency_linear(_g_player_troop,1,70)
    troop_raise_proficiency_linear(_g_player_troop,2,70)
    troop_raise_proficiency_linear(_g_player_troop,4,70)
    troop_raise_proficiency_linear(_g_player_troop,5,70)
    troop_clear_inventory(_g_player_troop)
    troop_add_item(_g_player_troop,itm.leather_jerkin,0)
    troop_add_item(_g_player_troop,itm.leather_boots,0)
    troop_add_item(_g_player_troop,itm.practice_sword,0)
    troop_add_item(_g_player_troop,itm.quarter_staff,0)
    troop_equip_items(_g_player_troop)
    set_visitor(0,trp.player)
    set_visitor(32,trp.tutorial_fighter_1)
    set_visitor(33,trp.tutorial_fighter_2)
    set_visitor(34,trp.tutorial_fighter_3)
    set_visitor(35,trp.tutorial_fighter_4)
    set_visitor(40,trp.tutorial_master_archer)
    set_visitor(41,trp.tutorial_archer_1)
    set_visitor(42,trp.tutorial_archer_1)
    set_visitor(60,trp.tutorial_master_horseman)
    set_visitor(61,trp.tutorial_rider_1)
    set_visitor(62,trp.tutorial_rider_1)
    set_visitor(63,trp.tutorial_rider_2)
    set_visitor(64,trp.tutorial_rider_2)
    set_jump_mission(mt.tutorial_training_ground)
    jump_to_scene(scn.tutorial_training_ground)
    change_screen_mission()
tutorial_continue.codeBlock = code

tutorial_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    change_screen_quit()
tutorial_go_back_dot.codeBlock = code



reports = GameMenu("reports", 0,
"Character Renown: {reg5}^Honor Rating: {reg6}^Party Morale: {reg8}^Party Size Limit: {reg7}^"
)
def condition():
    game_get_party_companion_limit()
    var001 = reg0
    troop_slot_002 = troop_get_slot(trp.player,7)
    reg5 = troop_slot_002
    reg6 = _player_honor
    reg7 = var001
    reg8 = party_get_morale(p.main_party)
reports.conditionBlock = condition

reports_cheat_faction_orders = MenuOption("cheat_faction_orders", "{!}Cheat: Faction orders.")
def code():
    jump_to_menu(mnu.faction_orders)
reports_cheat_faction_orders.codeBlock = code

reports_view_character_report = MenuOption("view_character_report", "View character report.")
def code():
    jump_to_menu(mnu.character_report)
reports_view_character_report.codeBlock = code

reports_view_party_size_report = MenuOption("view_party_size_report", "View party size report.")
def code():
    jump_to_menu(mnu.party_size_report)
reports_view_party_size_report.codeBlock = code

reports_view_npc_mission_report = MenuOption("view_npc_mission_report", "View companion mission report.")
def code():
    jump_to_menu(mnu.companion_report)
reports_view_npc_mission_report.codeBlock = code

reports_view_weekly_budget_report = MenuOption("view_weekly_budget_report", "View weekly budget report.")
def code():
    _g_apply_budget_report_to_gold = 0
    start_presentation(prsnt.budget_report)
reports_view_weekly_budget_report.codeBlock = code

reports_view_morale_report = MenuOption("view_morale_report", "View party morale report.")
def code():
    jump_to_menu(mnu.morale_report)
reports_view_morale_report.codeBlock = code

reports_lord_relations = MenuOption("lord_relations", "View list of known lords by relation.")
def code():
    jump_to_menu(mnu.lord_relations)
reports_lord_relations.codeBlock = code

reports_courtship_relations = MenuOption("courtship_relations", "View courtship relations.")
def code():
    jump_to_menu(mnu.courtship_relations)
reports_courtship_relations.codeBlock = code

reports_status_check = MenuOption("status_check", "{!}NPC status check.")
def code():
    for trp_001 in range(trp.npc1, trp.kingdom_1_lord):
        if main_party_has_troop(trp_001):
            s4 = str_store_troop_name(trp_001)
            reg3 = troop_get_slot(trp_001,61)
            reg4 = troop_get_slot(trp_001,65)
            reg5 = troop_get_slot(trp_001,72)
            reg6 = troop_get_slot(trp_001,74)
            reg7 = troop_get_slot(trp_001,76)
            print("@{!}{s4}: M{reg3}, 2M{reg4}, PC{reg5}, 2PC{reg6}, PM{reg7}")
        #end
    #end
reports_status_check.codeBlock = code

reports_view_faction_relations_report = MenuOption("view_faction_relations_report", "View faction relations report.")
def code():
    jump_to_menu(mnu.faction_relations_report)
reports_view_faction_relations_report.codeBlock = code

reports_resume_travelling = MenuOption("resume_travelling", "Resume travelling.")
def code():
    change_screen_return()
reports_resume_travelling.codeBlock = code



custom_battle_scene = GameMenu("custom_battle_scene", 18374686479671624192,
"(NO TRANS)"
)

custom_battle_scene_quick_battle_scene_1 = MenuOption("quick_battle_scene_1", "{!}quick battle scene 1")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.quick_battle_scene_1)
    change_screen_mission()
custom_battle_scene_quick_battle_scene_1.codeBlock = code

custom_battle_scene_quick_battle_scene_2 = MenuOption("quick_battle_scene_2", "{!}quick battle scene 2")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.quick_battle_scene_2)
    change_screen_mission()
custom_battle_scene_quick_battle_scene_2.codeBlock = code

custom_battle_scene_quick_battle_scene_3 = MenuOption("quick_battle_scene_3", "{!}quick battle scene 3")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.quick_battle_scene_3)
    change_screen_mission()
custom_battle_scene_quick_battle_scene_3.codeBlock = code

custom_battle_scene_quick_battle_scene_4 = MenuOption("quick_battle_scene_4", "{!}quick battle scene 4")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.quick_battle_scene_4)
    change_screen_mission()
custom_battle_scene_quick_battle_scene_4.codeBlock = code

custom_battle_scene_quick_battle_scene_5 = MenuOption("quick_battle_scene_5", "{!}quick battle scene 5")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.quick_battle_scene_5)
    change_screen_mission()
custom_battle_scene_quick_battle_scene_5.codeBlock = code

custom_battle_scene_go_back = MenuOption("go_back", "{!}Go back")
def code():
    change_screen_quit()
custom_battle_scene_go_back.codeBlock = code



custom_battle_end = GameMenu("custom_battle_end", 512,
"The battle is over. {s1} Your side killed {reg5} enemies and lost {reg6} troops over the battle. You personally slew {reg7} men in the fighting."
)
def condition():
    music_set_situation(0)
    reg5 = _g_custom_battle_team2_death_count
    reg6 = _g_custom_battle_team1_death_count
    agent_kill_count_001 = get_player_agent_kill_count()
    agent_kill_count_002 = get_player_agent_kill_count(1)
    reg7 = agent_kill_count_001 + agent_kill_count_002
    if _g_battle_result == 1:
        s1 = str_store_string(gstr.battle_won)
    else:
        s1 = str_store_string(gstr.battle_lost)
    #end
    if _g_custom_battle_team2_death_count >= 100:
        unlock_achievement(4)
    #end
custom_battle_end.conditionBlock = condition

custom_battle_end_continue = MenuOption("continue", "Continue.")
def code():
    change_screen_quit()
custom_battle_end_continue.codeBlock = code



start_game_1 = GameMenu("start_game_1", 18374686479671624192,
"Select your character's gender."
)

start_game_1_start_male = MenuOption("start_male", "Male")
def code():
    troop_set_type(trp.player,0)
    _character_gender = 0
    jump_to_menu(mnu.start_character_1)
start_game_1_start_male.codeBlock = code

start_game_1_start_female = MenuOption("start_female", "Female")
def code():
    troop_set_type(trp.player,1)
    _character_gender = 1
    jump_to_menu(mnu.start_character_1)
start_game_1_start_female.codeBlock = code

start_game_1_go_back = MenuOption("go_back", "Go back")
def code():
    jump_to_menu(mnu.start_game_0)
start_game_1_go_back.codeBlock = code



start_character_1 = GameMenu("start_character_1", 512,
"You were born years ago, in a land far away. Your father was..."
)
def condition():
    str_clear(10)
    str_clear(11)
    str_clear(12)
    str_clear(13)
    str_clear(14)
    str_clear(15)
start_character_1.conditionBlock = condition

start_character_1_start_noble = MenuOption("start_noble", "An impoverished noble.")
def code():
    _background_type = 1
    reg3 = _character_gender
    s10 = str_store_string("@You came into the world a {reg3?daughter:son} of declining nobility, owning only the house in which they lived. However, despite your family's hardships, they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court.")
    jump_to_menu(mnu.start_character_2)
start_character_1_start_noble.codeBlock = code

start_character_1_start_merchant = MenuOption("start_merchant", "A travelling merchant.")
def code():
    _background_type = 2
    reg3 = _character_gender
    s10 = str_store_string("@You were born the {reg3?daughter:son} of travelling merchants, always moving from place to place in search of a profit. Although your parents were wealthier than most and educated you as well as they could, you found little opportunity to make friends on the road, living mostly for the moments when you could sell something to somebody.")
    jump_to_menu(mnu.start_character_2)
start_character_1_start_merchant.codeBlock = code

start_character_1_start_guard = MenuOption("start_guard", "A veteran warrior.")
def code():
    _background_type = 3
    reg3 = _character_gender
    s10 = str_store_string("@As a child, your family scrabbled out a meagre living from your father's wages as a guardsman to the local lord. It was not an easy existence, and you were too poor to get much of an education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand.")
    jump_to_menu(mnu.start_character_2)
start_character_1_start_guard.codeBlock = code

start_character_1_start_forester = MenuOption("start_forester", "A hunter.")
def code():
    _background_type = 4
    reg3 = _character_gender
    s11 = str_store_string("@{reg3?daughter:son}")
    s10 = str_store_string("@You were the {reg3?daughter:son} of a family who lived off the woods, doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows, even a spot of poaching whenever things got tight. Winter was never a good time for your family as the cold took animals and people alike, but you always lived to see another dawn, though your brothers and sisters might not be so fortunate.")
    jump_to_menu(mnu.start_character_2)
start_character_1_start_forester.codeBlock = code

start_character_1_start_nomad = MenuOption("start_nomad", "A steppe nomad.")
def code():
    _background_type = 5
    reg3 = _character_gender
    s11 = str_store_string("@{reg3?daughter:son}")
    s10 = str_store_string("@You were a child of the steppe, born to a tribe of wandering nomads who lived in great camps throughout the arid grasslands. Like the other tribesmen, your family revered horses above almost everything else, and they taught you how to ride almost before you learned how to walk. ")
    jump_to_menu(mnu.start_character_2)
start_character_1_start_nomad.codeBlock = code

start_character_1_start_thief = MenuOption("start_thief", "A thief.")
def code():
    _background_type = 6
    reg3 = _character_gender
    s10 = str_store_string("@As the {reg3?daughter:son} of a thief, you had very little 'formal' education. Instead you were out on the street, begging until you learned how to cut purses, cutting purses until you learned how to pick locks, all the way through your childhood. Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways.")
    jump_to_menu(mnu.start_character_2)
start_character_1_start_thief.codeBlock = code

start_character_1_go_back = MenuOption("go_back", "Go back")
def code():
    jump_to_menu(mnu.start_game_1)
start_character_1_go_back.codeBlock = code



start_character_2 = GameMenu("start_character_2", 0,
"{s10}^^ You started to learn about the world almost as soon as you could walk and talk. You spent your early life as..."
)

start_character_2_page = MenuOption("page", "A page at a nobleman's court.")
def code():
    _background_answer_2 = 0
    reg3 = _character_gender
    s11 = str_store_string("@As a {reg3?girl:boy} growing out of childhood, you were sent to live in the court of one of the nobles of the land. There, your first lessons were in humility, as you waited upon the lords and ladies of the household. But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords.")
    jump_to_menu(mnu.start_character_3)
start_character_2_page.codeBlock = code

start_character_2_apprentice = MenuOption("apprentice", "A craftsman's apprentice.")
def code():
    _background_answer_2 = 1
    reg3 = _character_gender
    s11 = str_store_string("@As a {reg3?girl:boy} growing out of childhood, you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as you wished to stay.")
    jump_to_menu(mnu.start_character_3)
start_character_2_apprentice.codeBlock = code

start_character_2_stockboy = MenuOption("stockboy", "A shop assistant.")
def code():
    _background_answer_2 = 4
    reg3 = _character_gender
    s11 = str_store_string("@As a {reg3?girl:boy} growing out of childhood, you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans. You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd got the better deal.")
    jump_to_menu(mnu.start_character_3)
start_character_2_stockboy.codeBlock = code

start_character_2_urchin = MenuOption("urchin", "A street urchin.")
def code():
    _background_answer_2 = 2
    reg3 = _character_gender
    s11 = str_store_string("@As a {reg3?girl:boy} growing out of childhood, you took to the streets, doing whatever you must to survive. Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world, always one step ahead of the law and those who wished you ill.")
    jump_to_menu(mnu.start_character_3)
start_character_2_urchin.codeBlock = code

start_character_2_nomad = MenuOption("nomad", "A steppe child.")
def code():
    _background_answer_2 = 3
    reg3 = _character_gender
    s11 = str_store_string("@As a {reg3?girl:boy} growing out of childhood, you rode the great steppes on a horse of your own, learning the ways of the grass and the desert. Although you sometimes went hungry, you became a skillful hunter and pathfinder in this trackless country. Your body too started to harden with muscle as you grew into the life of a nomad {reg3?woman:man}.")
    jump_to_menu(mnu.start_character_3)
start_character_2_nomad.codeBlock = code

start_character_2_go_back = MenuOption("go_back", "Go back.")
def code():
    jump_to_menu(mnu.start_character_1)
start_character_2_go_back.codeBlock = code



start_character_3 = GameMenu("start_character_3", 512,
"{s11}^^ Then, as a young adult, life changed as it always does. You became..."
)
def condition():
    reg3 = _character_gender
start_character_3.conditionBlock = condition

start_character_3_squire = MenuOption("squire", "A squire.")
def code():
    _background_answer_3 = 8
    s14 = str_store_string("@{reg3?daughter:man}")
    s12 = str_store_string("@Though the distinction felt sudden to you, somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you. When you were named squire to a noble at court, you practiced long hours with weapons, learning how to deal out hard knocks and how to take them, too. You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals. But in addition to learning the chivalric ideal, you also learned about the less uplifting side -- old warriors' stories of ruthless power politics, of betrayals and usurpations, of men who used guile as well as valor to achieve their aims.")
    jump_to_menu(mnu.start_character_4)
start_character_3_squire.codeBlock = code

start_character_3_lady = MenuOption("lady", "A lady-in-waiting.")
def code():
    _background_answer_3 = 9
    s14 = str_store_string("@{reg3?daughter:man}")
    s13 = str_store_string("@{reg3?woman:man}")
    s12 = str_store_string("@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things, the wives and mistresses of noble men as well as maidens who had yet to find a husband. However, even here you found politics at work as the ladies schemed for prominence and fought each other bitterly to catch the eye of whatever unmarried man was in fashion at court. You soon learned ways of turning these situations and goings-on to your advantage. With it came the realisation that you yourself could wield great influence in the world, if only you applied yourself with a little bit of subtlety.")
    jump_to_menu(mnu.start_character_4)
start_character_3_lady.codeBlock = code

start_character_3_troubadour = MenuOption("troubadour", "A troubadour.")
def code():
    _background_answer_3 = 7
    s14 = str_store_string("@{reg3?daughter:man}")
    s13 = str_store_string("@{reg3?woman:man}")
    s12 = str_store_string("@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. You set out on your own with nothing except the instrument slung over your back and your own voice. It was a poor existence, with many a hungry night when people failed to appreciate your play, but you managed to survive on your music alone. As the years went by you became adept at playing the drunken crowds in your taverns, and even better at talking anyone out of anything you wanted.")
    jump_to_menu(mnu.start_character_4)
start_character_3_troubadour.codeBlock = code

start_character_3_student = MenuOption("student", "A university student.")
def code():
    _background_answer_3 = 10
    s12 = str_store_string("@Though the distinction felt sudden to you, somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you. You found yourself as a student in the university of one of the great cities, where you studied theology, philosophy, and medicine. But not all your lessons were learned in the lecture halls. You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight. However, you certainly were able to observe how a broken jaw is set, or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop.")
    jump_to_menu(mnu.start_character_4)
start_character_3_student.codeBlock = code

start_character_3_peddler = MenuOption("peddler", "A goods peddler.")
def code():
    _background_answer_3 = 5
    s14 = str_store_string("@{reg3?daughter:man}")
    s13 = str_store_string("@{reg3?woman:man}")
    s12 = str_store_string("@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. Heeding the call of the open road, you travelled from village to village buying and selling what you could. It was not a rich existence, but you became a master at haggling even the most miserly elders into giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire...")
    jump_to_menu(mnu.start_character_4)
start_character_3_peddler.codeBlock = code

start_character_3_craftsman = MenuOption("craftsman", "A smith.")
def code():
    _background_answer_3 = 4
    s14 = str_store_string("@{reg3?daughter:man}")
    s13 = str_store_string("@{reg3?woman:man}")
    s12 = str_store_string("@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. You pursued a career as a smith, crafting items of function and beauty out of simple metal. As time wore on you became a master of your trade, and fine work started to fetch fine prices. With food in your belly and logs on your fire, you could take pride in your work and your growing reputation.")
    jump_to_menu(mnu.start_character_4)
start_character_3_craftsman.codeBlock = code

start_character_3_poacher = MenuOption("poacher", "A game poacher.")
def code():
    _background_answer_3 = 3
    s14 = str_store_string("@{reg3?daughter:man}")
    s13 = str_store_string("@{reg3?woman:man}")
    s12 = str_store_string("@Though the distinction felt sudden to you, somewhere along the way you had become a {s13}, and the whole world seemed to change around you. Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into firewood that warmed many freezing homes during winter. All for a few silvers, of course.")
    jump_to_menu(mnu.start_character_4)
start_character_3_poacher.codeBlock = code

start_character_3_go_back = MenuOption("go_back", "Go back.")
def code():
    jump_to_menu(mnu.start_character_2)
start_character_3_go_back.codeBlock = code



start_character_4 = GameMenu("start_character_4", 512,
"{s12}^^But soon everything changed and you decided to strike out on your own as an adventurer. What made you take this decision was..."
)

start_character_4_revenge = MenuOption("revenge", "Personal revenge.")
def code():
    _background_answer_4 = 1
    s13 = str_store_string("@Only you know exactly what caused you to give up your old life and become an adventurer. Still, it was not a difficult choice to leave, with the rage burning brightly in your heart. You want vengeance. You want justice. What was done to you cannot be undone, and these debts can only be paid in blood...")
    jump_to_menu(mnu.choose_skill)
start_character_4_revenge.codeBlock = code

start_character_4_death = MenuOption("death", "The loss of a loved one.")
def code():
    _background_answer_4 = 2
    s13 = str_store_string("@Only you know exactly what caused you to give up your old life and become an adventurer. All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so painful. Perhaps your new life will let you forget, or honour the name that you can no longer bear to speak...")
    jump_to_menu(mnu.choose_skill)
start_character_4_death.codeBlock = code

start_character_4_wanderlust = MenuOption("wanderlust", "Wanderlust.")
def code():
    _background_answer_4 = 3
    s13 = str_store_string("@Only you know exactly what caused you to give up your old life and become an adventurer. You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back...")
    jump_to_menu(mnu.choose_skill)
start_character_4_wanderlust.codeBlock = code

start_character_4_disown = MenuOption("disown", "Being forced out of your home.")
def code():
    _background_answer_4 = 5
    s13 = str_store_string("@Only you know exactly what caused you to give up your old life and become an adventurer. However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone now, and you must face the fact that you're out in the wide wide world. Alone to sink or swim...")
    jump_to_menu(mnu.choose_skill)
start_character_4_disown.codeBlock = code

start_character_4_greed = MenuOption("greed", "Lust for money and power.")
def code():
    _background_answer_4 = 6
    s13 = str_store_string("@Only you know exactly what caused you to give up your old life and become an adventurer. To everyone else, it's clear that you're now motivated solely by personal gain. You want to be rich, powerful, respected, feared. You want to be the one whom others hurry to obey. You want people to know your name, and tremble whenever it is spoken. You want everything, and you won't let anyone stop you from having it...")
    jump_to_menu(mnu.choose_skill)
start_character_4_greed.codeBlock = code

start_character_4_go_back = MenuOption("go_back", "Go back.")
def code():
    jump_to_menu(mnu.start_character_3)
start_character_4_go_back.codeBlock = code



choose_skill = GameMenu("choose_skill", 512,
"{s13}"
)
def condition():
    _current_string_reg = 10
    var001 = 0
    if _character_gender == 1:
        s14 = str_store_string(gstr.woman)
        var001 += 1
    else:
        s14 = str_store_string(gstr.man)
    #end
    if _background_type == 1:
        s15 = str_store_string(gstr.noble)
        var001 -= 1
    else:
        s15 = str_store_string(gstr.common)
    #end
    if var001 == -1:
        s16 = str_store_string(gstr.may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly)
    elif var001 == 0:
        s16 = str_store_string(gstr.may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords)
    elif var001 == 1:
        s16 = str_store_string(gstr.may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords)
    #end
choose_skill.conditionBlock = condition

choose_skill_begin_adventuring = MenuOption("begin_adventuring", "Become an adventurer and ride to your destiny.")
def code():
    set_show_messages(0)
    if _character_gender == 0:
        troop_raise_attribute(trp.player,0,1)
        troop_raise_attribute(trp.player,3,1)
    else:
        troop_raise_attribute(trp.player,1,1)
        troop_raise_attribute(trp.player,2,1)
    #end
    troop_raise_attribute(trp.player,0,1)
    troop_raise_attribute(trp.player,1,1)
    troop_raise_attribute(trp.player,3,1)
    troop_raise_skill(trp.player,skl.leadership,1)
    troop_raise_skill(trp.player,skl.riding,1)
    if _background_type == 1 and _character_gender == 0:
        troop_raise_attribute(trp.player,2,1)
        troop_raise_attribute(trp.player,3,2)
        troop_raise_skill(trp.player,27,1)
        troop_raise_skill(trp.player,35,1)
        troop_raise_skill(trp.player,24,1)
        troop_raise_skill(trp.player,15,1)
        troop_raise_skill(trp.player,1,1)
        troop_raise_proficiency(trp.player,0,10)
        troop_raise_proficiency(trp.player,1,10)
        troop_raise_proficiency(trp.player,2,10)
        troop_add_item(trp.player,itm.tab_shield_round_a,5)
        troop_set_slot(trp.player,7,100)
        change_player_honor(3)
        troop_add_gold(trp.player,100)
    elif _background_type == 1 and _character_gender == 1:
        troop_raise_attribute(trp.player,2,2)
        troop_raise_attribute(trp.player,3,1)
        troop_raise_skill(trp.player,11,1)
        troop_raise_skill(trp.player,24,2)
        troop_raise_skill(trp.player,9,1)
        troop_raise_skill(trp.player,1,1)
        troop_raise_proficiency(trp.player,0,20)
        troop_set_slot(trp.player,7,50)
        troop_add_item(trp.player,itm.tab_shield_round_a,5)
        troop_add_gold(trp.player,100)
    elif _background_type == 2:
        troop_raise_attribute(trp.player,2,2)
        troop_raise_attribute(trp.player,3,1)
        troop_raise_skill(trp.player,24,1)
        troop_raise_skill(trp.player,1,1)
        troop_raise_skill(trp.player,0,2)
        troop_raise_skill(trp.player,12,1)
        troop_raise_proficiency(trp.player,1,10)
        troop_add_gold(trp.player,250)
        troop_set_slot(trp.player,7,20)
    elif _background_type == 3:
        troop_raise_attribute(trp.player,0,1)
        troop_raise_attribute(trp.player,1,1)
        troop_raise_attribute(trp.player,3,1)
        troop_raise_skill(trp.player,skl.ironflesh,1)
        troop_raise_skill(trp.player,skl.power_strike,1)
        troop_raise_skill(trp.player,skl.weapon_master,1)
        troop_raise_skill(trp.player,skl.leadership,1)
        troop_raise_skill(trp.player,skl.trainer,1)
        troop_raise_proficiency(trp.player,0,10)
        troop_raise_proficiency(trp.player,1,15)
        troop_raise_proficiency(trp.player,2,20)
        troop_raise_proficiency(trp.player,5,10)
        troop_add_item(trp.player,itm.tab_shield_kite_b,5)
        troop_add_gold(trp.player,50)
        troop_set_slot(trp.player,7,10)
    elif _background_type == 4:
        troop_raise_attribute(trp.player,0,1)
        troop_raise_attribute(trp.player,1,2)
        troop_raise_skill(trp.player,skl.power_draw,1)
        troop_raise_skill(trp.player,skl.tracking,1)
        troop_raise_skill(trp.player,skl.pathfinding,1)
        troop_raise_skill(trp.player,skl.spotting,1)
        troop_raise_skill(trp.player,skl.athletics,1)
        troop_raise_proficiency(trp.player,1,10)
        troop_raise_proficiency(trp.player,3,30)
        troop_add_gold(trp.player,30)
    elif _background_type == 5 and _character_gender == 0:
        troop_raise_attribute(trp.player,0,1)
        troop_raise_attribute(trp.player,1,1)
        troop_raise_attribute(trp.player,2,1)
        troop_raise_skill(trp.player,skl.power_draw,1)
        troop_raise_skill(trp.player,skl.horse_archery,1)
        troop_raise_skill(trp.player,skl.pathfinding,1)
        troop_raise_skill(trp.player,skl.riding,2)
        troop_raise_proficiency(trp.player,0,10)
        troop_raise_proficiency(trp.player,3,30)
        troop_raise_proficiency(trp.player,5,10)
        troop_add_item(trp.player,itm.tab_shield_small_round_a,5)
        troop_add_gold(trp.player,15)
        troop_set_slot(trp.player,7,10)
    elif _background_type == 5 and _character_gender == 1:
        troop_raise_attribute(trp.player,0,1)
        troop_raise_attribute(trp.player,1,1)
        troop_raise_attribute(trp.player,2,1)
        troop_raise_skill(trp.player,skl.wound_treatment,1)
        troop_raise_skill(trp.player,skl.first_aid,1)
        troop_raise_skill(trp.player,skl.pathfinding,1)
        troop_raise_skill(trp.player,skl.riding,2)
        troop_raise_proficiency(trp.player,0,5)
        troop_raise_proficiency(trp.player,3,20)
        troop_raise_proficiency(trp.player,5,5)
        troop_add_item(trp.player,itm.tab_shield_small_round_a,5)
        troop_add_gold(trp.player,20)
    elif _background_type == 6:
        troop_raise_attribute(trp.player,1,3)
        troop_raise_skill(trp.player,skl.athletics,2)
        troop_raise_skill(trp.player,skl.power_throw,1)
        troop_raise_skill(trp.player,skl.inventory_management,1)
        troop_raise_skill(trp.player,skl.looting,1)
        troop_raise_proficiency(trp.player,0,20)
        troop_raise_proficiency(trp.player,5,20)
        troop_add_item(trp.player,itm.throwing_knives,0)
        troop_add_gold(trp.player,25)
    #end
    if _background_answer_2 == 0:
        troop_raise_attribute(trp.player,3,1)
        troop_raise_attribute(trp.player,0,1)
        troop_raise_skill(trp.player,skl.power_strike,1)
        troop_raise_skill(trp.player,skl.persuasion,1)
        troop_raise_proficiency(trp.player,0,15)
        troop_raise_proficiency(trp.player,2,5)
    elif _background_answer_2 == 1:
        troop_raise_attribute(trp.player,2,1)
        troop_raise_attribute(trp.player,0,1)
        troop_raise_skill(trp.player,skl.engineer,1)
        troop_raise_skill(trp.player,skl.trade,1)
    elif _background_answer_2 == 2:
        troop_raise_attribute(trp.player,1,1)
        troop_raise_attribute(trp.player,2,1)
        troop_raise_skill(trp.player,skl.spotting,1)
        troop_raise_skill(trp.player,skl.looting,1)
        troop_raise_proficiency(trp.player,0,15)
        troop_raise_proficiency(trp.player,5,5)
    elif _background_answer_2 == 3:
        troop_raise_attribute(trp.player,0,1)
        troop_raise_attribute(trp.player,1,1)
        troop_raise_skill(trp.player,skl.horse_archery,1)
        troop_raise_skill(trp.player,skl.power_throw,1)
        troop_raise_proficiency(trp.player,3,15)
        change_troop_renown(trp.player,5)
    elif _background_answer_2 == 4:
        troop_raise_attribute(trp.player,2,1)
        troop_raise_attribute(trp.player,3,1)
        troop_raise_skill(trp.player,skl.inventory_management,1)
        troop_raise_skill(trp.player,skl.trade,1)
    #end
    if _background_answer_3 == 3:
        troop_raise_attribute(trp.player,0,1)
        troop_raise_attribute(trp.player,1,1)
        troop_raise_skill(trp.player,skl.power_draw,1)
        troop_raise_skill(trp.player,skl.tracking,1)
        troop_raise_skill(trp.player,skl.spotting,1)
        troop_raise_skill(trp.player,skl.athletics,1)
        troop_add_gold(trp.player,10)
        troop_raise_proficiency(trp.player,2,10)
        troop_raise_proficiency(trp.player,3,35)
        troop_add_item(trp.player,itm.axe,4)
        troop_add_item(trp.player,itm.rawhide_coat,0)
        troop_add_item(trp.player,itm.hide_boots,0)
        troop_add_item(trp.player,itm.hunting_bow,0)
        troop_add_item(trp.player,itm.barbed_arrows,0)
        troop_add_item(trp.player,itm.sumpter_horse,18)
        troop_add_item(trp.player,itm.dried_meat,0)
        troop_add_item(trp.player,itm.dried_meat,0)
        troop_add_item(trp.player,itm.furs,0)
        troop_add_item(trp.player,itm.furs,0)
    elif _background_answer_3 == 4:
        troop_raise_attribute(trp.player,0,1)
        troop_raise_attribute(trp.player,2,1)
        troop_raise_skill(trp.player,skl.weapon_master,1)
        troop_raise_skill(trp.player,skl.engineer,1)
        troop_raise_skill(trp.player,skl.tactics,1)
        troop_raise_skill(trp.player,skl.trade,1)
        troop_raise_proficiency(trp.player,0,15)
        troop_add_gold(trp.player,100)
        troop_add_item(trp.player,itm.leather_boots,22)
        troop_add_item(trp.player,itm.coarse_tunic,0)
        troop_add_item(trp.player,itm.sword_medieval_b,13)
        troop_add_item(trp.player,itm.hunting_crossbow,0)
        troop_add_item(trp.player,itm.bolts,0)
        troop_add_item(trp.player,itm.tools,0)
        troop_add_item(trp.player,itm.saddle_horse,0)
        troop_add_item(trp.player,itm.smoked_fish,0)
    elif _background_answer_3 == 5:
        troop_raise_attribute(trp.player,3,1)
        troop_raise_attribute(trp.player,2,1)
        troop_raise_skill(trp.player,skl.riding,1)
        troop_raise_skill(trp.player,skl.trade,1)
        troop_raise_skill(trp.player,skl.pathfinding,1)
        troop_raise_skill(trp.player,skl.inventory_management,1)
        troop_add_item(trp.player,itm.leather_gloves,0)
        troop_add_gold(trp.player,90)
        troop_raise_proficiency(trp.player,2,15)
        troop_add_item(trp.player,itm.leather_jacket,0)
        troop_add_item(trp.player,itm.leather_boots,22)
        troop_add_item(trp.player,itm.fur_hat,0)
        troop_add_item(trp.player,itm.staff,0)
        troop_add_item(trp.player,itm.hunting_crossbow,0)
        troop_add_item(trp.player,itm.bolts,0)
        troop_add_item(trp.player,itm.saddle_horse,0)
        troop_add_item(trp.player,itm.sumpter_horse,0)
        troop_add_item(trp.player,itm.linen,0)
        troop_add_item(trp.player,itm.pottery,0)
        troop_add_item(trp.player,itm.wool,0)
        troop_add_item(trp.player,itm.wool,0)
        troop_add_item(trp.player,itm.smoked_fish,0)
    elif _background_answer_3 == 7:
        troop_raise_attribute(trp.player,3,2)
        troop_raise_skill(trp.player,skl.weapon_master,1)
        troop_raise_skill(trp.player,skl.persuasion,1)
        troop_raise_skill(trp.player,skl.leadership,1)
        troop_raise_skill(trp.player,skl.pathfinding,1)
        troop_add_gold(trp.player,80)
        troop_raise_proficiency(trp.player,0,25)
        troop_raise_proficiency(trp.player,4,10)
        troop_add_item(trp.player,itm.tabard,24)
        troop_add_item(trp.player,itm.leather_boots,22)
        troop_add_item(trp.player,itm.sword_medieval_a,2)
        troop_add_item(trp.player,itm.hunting_crossbow,0)
        troop_add_item(trp.player,itm.bolts,0)
        troop_add_item(trp.player,itm.saddle_horse,31)
        troop_add_item(trp.player,itm.smoked_fish,0)
    elif _background_answer_3 == 8:
        troop_raise_attribute(trp.player,0,1)
        troop_raise_attribute(trp.player,1,1)
        troop_raise_skill(trp.player,skl.riding,1)
        troop_raise_skill(trp.player,skl.weapon_master,1)
        troop_raise_skill(trp.player,skl.power_strike,1)
        troop_raise_skill(trp.player,skl.leadership,1)
        troop_add_gold(trp.player,20)
        troop_raise_proficiency(trp.player,0,30)
        troop_raise_proficiency(trp.player,1,30)
        troop_raise_proficiency(trp.player,2,30)
        troop_raise_proficiency(trp.player,3,10)
        troop_raise_proficiency(trp.player,4,10)
        troop_raise_proficiency(trp.player,5,10)
        troop_add_item(trp.player,itm.leather_jerkin,22)
        troop_add_item(trp.player,itm.leather_boots,21)
        troop_add_item(trp.player,itm.sword_medieval_a,2)
        troop_add_item(trp.player,itm.hunting_crossbow,0)
        troop_add_item(trp.player,itm.bolts,0)
        troop_add_item(trp.player,itm.saddle_horse,31)
        troop_add_item(trp.player,itm.smoked_fish,0)
    elif _background_answer_3 == 9 and _character_gender == 1:
        troop_raise_attribute(trp.player,2,1)
        troop_raise_attribute(trp.player,3,1)
        troop_raise_skill(trp.player,skl.persuasion,2)
        troop_raise_skill(trp.player,skl.riding,1)
        troop_raise_skill(trp.player,skl.wound_treatment,1)
        troop_add_item(trp.player,itm.dagger,0)
        troop_add_item(trp.player,itm.hunting_crossbow,0)
        troop_add_item(trp.player,itm.bolts,0)
        troop_add_item(trp.player,itm.courser,35)
        troop_add_item(trp.player,itm.woolen_hood,24)
        troop_add_item(trp.player,itm.woolen_dress,24)
        troop_add_gold(trp.player,100)
        troop_raise_proficiency(trp.player,0,10)
        troop_raise_proficiency(trp.player,4,15)
        troop_add_item(trp.player,itm.smoked_fish,0)
    elif _background_answer_3 == 10:
        troop_raise_attribute(trp.player,2,2)
        troop_raise_skill(trp.player,skl.weapon_master,1)
        troop_raise_skill(trp.player,skl.surgery,1)
        troop_raise_skill(trp.player,skl.wound_treatment,1)
        troop_raise_skill(trp.player,skl.persuasion,1)
        troop_add_gold(trp.player,80)
        troop_raise_proficiency(trp.player,0,20)
        troop_raise_proficiency(trp.player,4,20)
        troop_add_item(trp.player,itm.linen_tunic,24)
        troop_add_item(trp.player,itm.woolen_hose,0)
        troop_add_item(trp.player,itm.sword_medieval_a,2)
        troop_add_item(trp.player,itm.hunting_crossbow,0)
        troop_add_item(trp.player,itm.bolts,0)
        troop_add_item(trp.player,itm.saddle_horse,31)
        troop_add_item(trp.player,itm.smoked_fish,0)
        random_x_001 = store_random_in_range(itm.book_tactics,itm.spice)
        troop_add_item(trp.player,random_x_001,0)
    #end
    if _background_answer_4 == 1:
        troop_raise_attribute(trp.player,0,2)
        troop_raise_skill(trp.player,skl.power_strike,1)
    elif _background_answer_4 == 2:
        troop_raise_attribute(trp.player,3,2)
        troop_raise_skill(trp.player,skl.ironflesh,1)
    elif _background_answer_4 == 3:
        troop_raise_attribute(trp.player,1,2)
        troop_raise_skill(trp.player,skl.pathfinding,1)
    elif _background_answer_4 == 5:
        troop_raise_attribute(trp.player,0,1)
        troop_raise_attribute(trp.player,2,1)
        troop_raise_skill(trp.player,skl.weapon_master,1)
    elif _background_answer_4 == 6:
        troop_raise_attribute(trp.player,1,1)
        troop_raise_attribute(trp.player,2,1)
        troop_raise_skill(trp.player,skl.looting,1)
    #end
    if _background_type == 1:
        jump_to_menu(mnu.auto_return)
        start_presentation(prsnt.banner_selection)
    else:
        change_screen_return(0)
    #end
    set_show_messages(1)
choose_skill_begin_adventuring.codeBlock = code

choose_skill_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    jump_to_menu(mnu.start_character_4)
choose_skill_go_back_dot.codeBlock = code



past_life_explanation = GameMenu("past_life_explanation", 512,
"{s3}"
)
def condition():
    if _current_string_reg > 14:
        _current_string_reg = 10
    #end
    s3 = str_store_string_reg(_current_string_reg)
    if _current_string_reg >= 14:
        s5 = str_store_string("@Back to the beginning...")
    else:
        s5 = str_store_string("@View next segment...")
    #end
past_life_explanation.conditionBlock = condition

past_life_explanation_view_next = MenuOption("view_next", "{s5}")
def code():
    _current_string_reg += 1
    jump_to_menu(mnu.past_life_explanation)
past_life_explanation_view_next.codeBlock = code

past_life_explanation_continue = MenuOption("continue", "Continue...")

past_life_explanation_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    jump_to_menu(mnu.choose_skill)
past_life_explanation_go_back_dot.codeBlock = code



auto_return = GameMenu("auto_return", 0,
"{!}This menu automatically returns to caller."
)
def condition():
    change_screen_return(0)
auto_return.conditionBlock = condition



morale_report = GameMenu("morale_report", 0,
"{s1}"
)
def condition():
    get_player_party_morale_values()
    var001 = reg0
    reg1 = _g_player_party_morale_modifier_party_size
    if reg1 > 0:
        s2 = str_store_string("@{!} -")
    else:
        s2 = str_store_string(gstr.space)
    #end
    reg2 = _g_player_party_morale_modifier_leadership
    if reg2 > 0:
        s3 = str_store_string("@{!} +")
    else:
        s3 = str_store_string(gstr.space)
    #end
    if _g_player_party_morale_modifier_no_food > 0:
        reg7 = _g_player_party_morale_modifier_no_food
        s5 = str_store_string("@^No food:  -{reg7}")
    else:
        s5 = str_store_string(gstr.space)
    #end
    reg3 = _g_player_party_morale_modifier_food
    if reg3 > 0:
        s4 = str_store_string("@{!} +")
    else:
        s4 = str_store_string(gstr.space)
    #end
    if _g_player_party_morale_modifier_debt > 0:
        reg6 = _g_player_party_morale_modifier_debt
        s6 = str_store_string("@^Wage debt:  -{reg6}")
    else:
        s6 = str_store_string(gstr.space)
    #end
    reg5 = party_get_morale(p.main_party)
    reg4 = reg5 - var001
    if reg4 > 0:
        s7 = str_store_string("@{!} +")
    else:
        s7 = str_store_string(gstr.space)
    #end
    reg6 = 50
    s1 = str_store_string(gstr.current_party_morale_is_reg5_current_party_morale_modifiers_are__base_morale__50_party_size_s2reg1_leadership_s3reg2_food_variety_s4reg3s5s6_recent_events_s7reg4_total__reg5___)
    for fac_002 in range(fac.kingdom_1, fac.kingdoms_end):
        faction_slot_003 = faction_get_slot(fac_002,99)
        faction_slot_003 /= 100
        if faction_slot_003 != 0:
            reg6 = faction_slot_003
            s9 = str_store_faction_name(fac_002)
            s1 = str_store_string(gstr.s1extra_morale_for_s9_troops__reg6_)
        #end
    #end
morale_report.conditionBlock = condition

morale_report_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.reports)
morale_report_continue.codeBlock = code



courtship_relations = GameMenu("courtship_relations", 0,
"{s1}"
)
def condition():
    s1 = str_store_string(gstr.courtships_in_progress_)
    for trp_001 in range(trp.knight_1_1_wife, trp.heroes_end):
        if troop_slot_eq(trp_001,5,2):
            troop_get_relation_with_troop(trp.player,trp_001)
            if reg0 > 0:
                reg3 = reg0
                s2 = str_store_troop_name(trp_001)
                cur_hours_002 = store_current_hours()
                troop_slot_003 = troop_get_slot(trp_001,4)
                cur_hours_002 -= troop_slot_003
                var004 = cur_hours_002 / 24
                reg4 = var004
                s1 = str_store_string(gstr.s1_s2_relation_reg3_last_visit_reg4_days_ago)
            #end
        #end
    #end
    s1 = str_store_string(gstr.s1__poems_known)
    if _allegoric_poem_recitations > 0:
        s1 = str_store_string(gstr.s1_storming_the_castle_of_love_allegoric)
    #end
    if _tragic_poem_recitations > 0:
        s1 = str_store_string(gstr.s1_kais_and_layali_tragic)
    #end
    if _comic_poem_recitations > 0:
        s1 = str_store_string(gstr.s1_a_conversation_in_the_garden_comic)
    #end
    if _heroic_poem_recitations > 0:
        s1 = str_store_string(gstr.s1_helgered_and_kara_epic)
    #end
    if _mystic_poem_recitations > 0:
        s1 = str_store_string(gstr.s1_a_hearts_desire_mystic)
    #end
courtship_relations.conditionBlock = condition

courtship_relations_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.reports)
courtship_relations_continue.codeBlock = code



lord_relations = GameMenu("lord_relations", 0,
"{s1}"
)
def condition():
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        troop_set_slot(trp_001,46,0)
    #end
    str_clear(1)
    for trp_002 in range(trp.npc1, trp.knight_1_1_wife):
        var003 = -100
        troop_id_004 = -1
        for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
            if troop_slot_eq(trp_001,46,0) and troop_slot_eq(trp_001,2,2) and troop_slot_ge(trp_001,5,1):
                troop_get_player_relation(trp_001)
                var005 = reg0
                if var005 >= var003:
                    var003 = var005
                    troop_id_004 = trp_001
                #end
            #end
        #end
        if troop_id_004 > -1:
            s4 = str_store_troop_name_link(troop_id_004)
            reg4 = var003
            s1 = str_store_string("@{!}{s1}^{s4}: {reg4}")
            troop_set_slot(troop_id_004,46,1)
        #end
    #end
lord_relations.conditionBlock = condition

lord_relations_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.reports)
lord_relations_continue.codeBlock = code



companion_report = GameMenu("companion_report", 0,
"{s7}{s1}"
)
def condition():
    str_clear(1)
    s7 = str_store_string(gstr.no_companions_in_service)
    if True:
        troop_slot_001 = troop_get_slot(trp.player,30)
        if True:
            troop_type_002 = troop_get_type(trp.player)
            if troop_type_002 == 1:
                s8 = str_store_string(gstr.husband)
            else:
                s8 = str_store_string(gstr.wife)
            #end
        #end
        if troop_slot_001 <= 0:
            troop_slot_001 = troop_get_slot(trp.player,34)
            s8 = str_store_string(gstr.betrothed)
        #end
        if troop_slot_001 > 0:
            s4 = str_store_troop_name(troop_slot_001)
            troop_slot_003 = troop_get_slot(troop_slot_001,12)
            if is_between(troop_slot_003,p.town_1,p.salt_mine):
                s5 = str_store_party_name(troop_slot_003)
            elif troop_slot_eq(troop_slot_001,2,2):
                s5 = str_store_string(gstr.leading_party)
            else:
                s5 = str_store_string(gstr.whereabouts_unknown)
            #end
        #end
        s3 = str_store_string(gstr.s4_s8_s5)
        s2 = str_store_string(1)
        s1 = str_store_string(gstr.s2_s3)
    #end
    if _cheat_mode >= 1 and _npc_to_rejoin_party >= 0:
        s5 = str_store_troop_name(_npc_to_rejoin_party)
        s1 = str_store_string("@{!}DEBUG -- {s1}^NPC in rejoin queue: {s5}^")
    #end
    for trp_004 in range(trp.npc1, trp.kingdom_1_lord):
        str_clear(2)
        str_clear(3)
        if True:
            troop_slot_005 = troop_get_slot(trp_004,150)
            if troop_slot_eq(trp_004,2,5):
                s4 = str_store_troop_name(trp_004)
                if troop_slot_eq(trp_004,151,1):
                    s8 = str_store_string(gstr.gathering_support)
                    if troop_slot_005 == 1:
                        s5 = str_store_string(gstr.expected_back_imminently)
                    else:
                        reg3 = troop_slot_005
                        s5 = str_store_string(gstr.expected_back_in_approximately_reg3_days)
                    #end
                #end
            elif troop_slot_eq(trp_004,151,2):
                troop_slot_006 = troop_get_slot(trp_004,67)
                s11 = str_store_party_name(troop_slot_006)
                s8 = str_store_string(gstr.gathering_intelligence)
                if troop_slot_005 == 1:
                    s5 = str_store_string(gstr.expected_back_imminently)
                else:
                    reg3 = troop_slot_005
                    s5 = str_store_string(gstr.expected_back_in_approximately_reg3_days)
                #end
            elif troop_slot_ge(trp_004,151,3) and not troop_slot_ge(trp_004,151,8):
                troop_slot_007 = troop_get_slot(trp_004,152)
                s9 = str_store_faction_name(troop_slot_007)
                s8 = str_store_string(gstr.diplomatic_embassy_to_s9)
                if troop_slot_005 == 1:
                    s5 = str_store_string(gstr.expected_back_imminently)
                else:
                    reg3 = troop_slot_005
                    s5 = str_store_string(gstr.expected_back_in_approximately_reg3_days)
                #end
            elif trp_004 == _g_player_minister:
                s8 = str_store_string(gstr.serving_as_minister)
                if is_between(_g_player_court,p.town_1,p.salt_mine):
                    s9 = str_store_party_name(_g_player_court)
                    s5 = str_store_string(gstr.in_your_court_at_s9)
                else:
                    s5 = str_store_string(gstr.whereabouts_unknown)
                #end
            elif main_party_has_troop(trp_004):
                s8 = str_store_string(gstr.under_arms)
                s5 = str_store_string(gstr.in_your_party)
            elif troop_slot_eq(trp_004,151,8):
                s8 = str_store_string(gstr.attempting_to_rejoin_party)
                s5 = str_store_string(gstr.whereabouts_unknown)
            elif troop_slot_ge(trp_004,12,1):
                s8 = str_store_string(gstr.separated_from_party)
                s5 = str_store_string(gstr.whereabouts_unknown)
            else:
                if check_quest_active(qst.lend_companion) and quest_slot_eq(qst.lend_companion,2,trp_004):
                    s8 = str_store_string("@On loan,")
                elif check_quest_active(qst.lend_surgeon) and quest_slot_eq(qst.lend_surgeon,2,trp_004):
                    s8 = str_store_string("@On loan,")
                else:
                    troop_set_slot(trp_004,151,8)
                    s8 = str_store_string(gstr.attempting_to_rejoin_party)
                #end
                s5 = str_store_string(gstr.whereabouts_unknown)
                if _cheat_mode >= 1:
                    reg2 = troop_get_slot(trp_004,151)
                    reg3 = troop_get_slot(trp_004,150)
                    reg4 = troop_get_slot(trp_004,8)
                    reg4 = troop_get_slot(trp_004,82)
                    print("@{!}DEBUG: {s4} current mission: {reg2};;; days on mission: {reg3};;; prisoner: {reg4};;; pphistory: {reg5}")
                #end
            #end
            s3 = str_store_string(gstr.s4_s8_s5)
            s2 = str_store_string(1)
            s1 = str_store_string(gstr.s2_s3)
            str_clear(7)
        elif not troop_slot_eq(trp_004,2,2) and troop_slot_ge(trp_004,8,p.town_1):
            s4 = str_store_troop_name(trp_004)
            s8 = str_store_string(gstr.missing_after_battle)
            s5 = str_store_string(gstr.whereabouts_unknown)
            s3 = str_store_string(gstr.s4_s8_s5)
            s2 = str_store_string(1)
            s1 = str_store_string(gstr.s2_s3)
            str_clear(7)
        #end
    #end
companion_report.conditionBlock = condition

companion_report_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.reports)
companion_report_continue.codeBlock = code



faction_orders = GameMenu("faction_orders", 0,
"{!}{s9}"
)
def condition():
    var006_list1 = [
    6,
    0,
    ]
    str_clear(9)
    cur_hours_001 = store_current_hours()
    for fac_002 in range(fac.player_supporters_faction, fac.kingdoms_end):
        if faction_slot_eq(fac_002,21,0) and fac_002 != fac.player_supporters_faction:
            faction_slot_003 = faction_get_slot(fac_002,4)
            if True:
                faction_slot_004 = faction_get_slot(fac_002,8)
                if faction_slot_004 > -1:
                    faction_slot_005 = faction_slot_004
                else:
                    faction_slot_005 = faction_get_slot(fac_002,11)
                #end
            #end
        #end
        npc_decision_checklist_faction_ai_alt(faction_slot_005)
        var006 = reg0
        s26 = str_store_string(14)
        faction_slot_007 = faction_get_slot(fac_002,4)
        faction_slot_008 = faction_get_slot(fac_002,5)
        faction_slot_009 = faction_get_slot(fac_002,8)
        faction_slot_010 = faction_get_slot(fac_002,9)
        s10 = str_store_faction_name(fac_002)
        if True:
            faction_slot_011 = faction_get_slot(fac_002,64)
            if faction_slot_011 == 1:
                s11 = str_store_string("@Appoint next marshal")
            elif is_between(faction_slot_011,p.town_1,p.salt_mine):
                s12 = str_store_party_name(faction_slot_011)
                s11 = str_store_string("@Award {s12} as fief")
            elif faction_slot_011 == 0:
                s11 = str_store_string("@None")
            else:
                reg3 = faction_slot_011
                s11 = str_store_string("@{!}Error [[[{reg3}]]]")
            #end
            reg4 = store_current_hours()
            faction_slot_012 = faction_get_slot(fac_002,65)
            reg4 -= faction_slot_012
            s10 = str_store_string("@{!}{s10}^Faction political issue: {s11}")
            if faction_slot_ge(fac_002,64,1):
                s10 = str_store_string("@{!}{s10} [[[on agenda {reg4} hours]]]")
            #end
        #end
        reg2 = faction_slot_010
        if faction_slot_007 == 0:
            s11 = str_store_string("@{!}Defending")
        elif faction_slot_007 == 1:
            s11 = str_store_string("@{!}Gathering army")
        elif faction_slot_007 == 2:
            s11 = str_store_party_name(faction_slot_008)
            s11 = str_store_string("@{!}Besieging {s11}")
        elif faction_slot_007 == 3:
            s11 = str_store_party_name(faction_slot_008)
            s11 = str_store_string("@{!}Raiding {s11}")
        elif faction_slot_007 == 4:
            s11 = str_store_party_name(faction_slot_008)
            s11 = str_store_string(gstr.attacking_enemy_army_near_s11)
        elif faction_slot_007 == 6:
            s11 = str_store_party_name(faction_slot_008)
            s11 = str_store_string(gstr.holding_feast_at_s11)
        elif faction_slot_007 == 5:
            s11 = str_store_party_name(faction_slot_008)
            s11 = str_store_string("@{!}Attacking enemies around {s11}")
        else:
            reg4 = faction_slot_007
            s11 = str_store_string(gstr.sfai_reg4)
        #end
        if faction_slot_009 < 0:
            s12 = str_store_string("@No one")
        else:
            s12 = str_store_troop_name(faction_slot_009)
            reg21 = troop_get_slot(faction_slot_009,150)
            s12 = str_store_string("@{!}{s12} [[[controversy: {reg21}]]]")
        #end
        for cur_party in __all_parties__:
            if party_slot_eq(cur_party,4,12):
                party_faction_014 = store_faction_of_party(cur_party)
                if party_faction_014 == fac_002:
                    s38 = str_store_party_name(cur_party)
                    s12 = str_store_string("@{!}{s12}^Screening party: {s38}")
                #end
            #end
        #end
        if var006 in var006_list1:
            cur_hours_015 = store_current_hours()
            faction_slot_016 = faction_get_slot(fac_002,97)
            cur_hours_015 -= faction_slot_016
            if cur_hours_015 >= 18:
                cur_hours_017 = store_current_hours()
                faction_set_slot(fac_002,96,cur_hours_017)
            #end
        #end
        if var006 != faction_slot_003:
            cur_hours_017 = store_current_hours()
            faction_set_slot(fac_002,97,cur_hours_017)
        #end
        evaluate_realm_stability(fac_002)
        var018 = reg0
        var019 = reg1
        faction_slot_020 = faction_get_slot(fac_002,94)
        var021 = cur_hours_001 - faction_slot_020
        var021 -= 72
        faction_slot_016 = faction_get_slot(fac_002,97)
        cur_hours_015 = cur_hours_001 - faction_slot_016
        faction_slot_022 = faction_get_slot(fac_002,95)
        var023 = cur_hours_001 - faction_slot_022
        faction_slot_024 = faction_get_slot(fac_002,96)
        var025 = cur_hours_001 - faction_slot_024
        faction_slot_026 = faction_get_slot(fac_002,98)
        var027 = cur_hours_001 - faction_slot_026
        reg3 = cur_hours_015
        reg4 = var023
        reg5 = var021
        reg7 = var018
        reg8 = var019
        reg9 = var025
        reg10 = var027
        s14 = str_store_string(26)
        s9 = str_store_string(gstr.s9s10_current_state_s11_hours_at_current_state_reg3_current_strategic_thinking_s14_marshall_s12_since_the_last_offensive_ended_reg4_hours_since_the_decisive_event_reg10_hours_since_the_last_rest_reg9_hours_since_the_last_feast_ended_reg5_hours_percent_disgruntled_lords_reg7_percent_restless_lords_reg8__)
    #end
    if not is_between(_g_cheat_selected_faction,fac.player_supporters_faction,fac.kingdoms_end):
        get_next_active_kingdom(fac.kingdoms_end)
        _g_cheat_selected_faction = reg0
    #end
    s10 = str_store_faction_name(_g_cheat_selected_faction)
    s9 = str_store_string("@Selected faction is: {s10}^^{s9}")
faction_orders.conditionBlock = condition

faction_orders_faction_orders_next_faction = MenuOption("faction_orders_next_faction", "{!}Select next faction.")
def code():
    get_next_active_kingdom(_g_cheat_selected_faction)
    _g_cheat_selected_faction = reg0
    jump_to_menu(mnu.faction_orders)
faction_orders_faction_orders_next_faction.codeBlock = code

faction_orders_faction_orders_political_collapse = MenuOption("faction_orders_political_collapse", "{!}CHEAT - Cause all lords in faction to fall out with their liege.")
def code():
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        if troop_slot_eq(trp_001,2,2):
            troop_faction_002 = store_faction_of_troop(trp_001)
            if troop_faction_002 == _g_cheat_selected_faction:
                faction_slot_003 = faction_get_slot(troop_faction_002,11)
                troop_change_relation_with_troop(trp_001,faction_slot_003,-200)
            #end
        #end
    #end
faction_orders_faction_orders_political_collapse.codeBlock = code

faction_orders_faction_orders_defend = MenuOption("faction_orders_defend", "{!}Force defend.")
def code():
    faction_set_slot(_g_cheat_selected_faction,4,0)
    faction_set_slot(_g_cheat_selected_faction,5,-1)
    jump_to_menu(mnu.faction_orders)
faction_orders_faction_orders_defend.codeBlock = code

faction_orders_faction_orders_feast = MenuOption("faction_orders_feast", "{!}Force feast.")
def code():
    var001 = 0
    for p_002 in range(p.town_1, p.village_1):
        if not party_slot_ge(p_002,54,1):
            party_faction_003 = store_faction_of_party(p_002)
            if party_faction_003 == _g_cheat_selected_faction:
                party_slot_004 = party_get_slot(p_002,7)
                troop_slot_005 = troop_get_slot(party_slot_004,7)
                random_x_006 = store_random_in_range(0,1000)
                troop_slot_005 += random_x_006
                if troop_slot_005 > var001:
                    var001 = troop_slot_005
                    var007 = p_002
                #end
            #end
        #end
    #end
    if var007 > p.town_1:
        faction_set_slot(_g_cheat_selected_faction,4,6)
        faction_set_slot(_g_cheat_selected_faction,5,var007)
        if _g_player_eligible_feast_center_no == var007:
            _g_player_eligible_feast_center_no = -1
        #end
        cur_hours_008 = store_current_hours()
        faction_set_slot(_g_cheat_selected_faction,94,cur_hours_008)
    #end
    jump_to_menu(mnu.faction_orders)
faction_orders_faction_orders_feast.codeBlock = code

faction_orders_faction_orders_gather = MenuOption("faction_orders_gather", "{!}Force gather army.")
def code():
    cur_hours_001 = store_current_hours()
    faction_set_slot(_g_cheat_selected_faction,4,1)
    faction_set_slot(_g_cheat_selected_faction,95,cur_hours_001)
    faction_set_slot(_g_cheat_selected_faction,9,1)
    faction_set_slot(_g_cheat_selected_faction,5,-1)
    jump_to_menu(mnu.faction_orders)
faction_orders_faction_orders_gather.codeBlock = code

faction_orders_faction_orders_increase_time = MenuOption("faction_orders_increase_time", "{!}Increase last offensive time by 24 hours.")
def code():
    faction_slot_001 = faction_get_slot(_g_cheat_selected_faction,95)
    faction_slot_001 -= 24
    faction_set_slot(_g_cheat_selected_faction,95,faction_slot_001)
    jump_to_menu(mnu.faction_orders)
faction_orders_faction_orders_increase_time.codeBlock = code

faction_orders_faction_orders_rethink = MenuOption("faction_orders_rethink", "{!}Force rethink.")
def code():
    init_ai_calculation()
    decide_faction_ai(_g_cheat_selected_faction)
    jump_to_menu(mnu.faction_orders)
faction_orders_faction_orders_rethink.codeBlock = code

faction_orders_faction_orders_rethink_all = MenuOption("faction_orders_rethink_all", "{!}Force rethink for all factions.")
def code():
    recalculate_ais()
    jump_to_menu(mnu.faction_orders)
faction_orders_faction_orders_rethink_all.codeBlock = code

faction_orders_enable_alt_ai = MenuOption("enable_alt_ai", "{!}CHEAT! - enable alternative ai")
def code():
    _g_use_alternative_ai = 1
    jump_to_menu(mnu.faction_orders)
faction_orders_enable_alt_ai.codeBlock = code

faction_orders_disable_alt_ai = MenuOption("disable_alt_ai", "{!}CHEAT! - disable alternative ai")
def code():
    _g_use_alternative_ai = 0
    jump_to_menu(mnu.faction_orders)
faction_orders_disable_alt_ai.codeBlock = code

faction_orders_faction_orders_init_econ = MenuOption("faction_orders_init_econ", "{!}Initialize economic stats.")
def code():
    initialize_economic_information()
    jump_to_menu(mnu.faction_orders)
faction_orders_faction_orders_init_econ.codeBlock = code

faction_orders_go_back_dot = MenuOption("go_back_dot", "{!}Go back.")
def code():
    jump_to_menu(mnu.reports)
faction_orders_go_back_dot.codeBlock = code



character_report = GameMenu("character_report", 0,
"{s9}"
)
def condition():
    if _g_player_reading_book > 0 and player_has_item(_g_player_reading_book):
        s8 = str_store_item_name(_g_player_reading_book)
        s9 = str_store_string("@You are currently reading {s8}.")
    else:
        _g_player_reading_book = 0
        s9 = str_store_string("@You are not reading any books.")
    #end
    var001 = 0
    var002 = 0
    s6 = str_store_string("@none")
    s8 = str_store_string("@none")
    for trp_003 in range(trp.npc1, trp.knight_1_1_wife):
        if troop_slot_eq(trp_003,2,2) or troop_slot_eq(trp_003,2,9):
            troop_get_player_relation(trp_003)
            var004 = reg0
            if var004 > 20:
                if var001 == 0:
                    s8 = str_store_troop_name(trp_003)
                elif var001 == 1:
                    s7 = str_store_troop_name(trp_003)
                    s8 = str_store_string("@{s7} and {s8}")
                else:
                    s7 = str_store_troop_name(trp_003)
                    s8 = str_store_string("@{!}{s7}, {s8}")
                #end
            #end
            var001 += 1
        elif var004 < -20:
            if var002 == 0:
                s6 = str_store_troop_name(trp_003)
            elif var002 == 1:
                s5 = str_store_troop_name(trp_003)
                s6 = str_store_string("@{s5} and {s6}")
            else:
                s5 = str_store_troop_name(trp_003)
                s6 = str_store_string("@{!}{s5}, {s6}")
            #end
            var002 += 1
        #end
    #end
    str_clear(12)
    if _player_right_to_rule > 0:
        reg12 = _player_right_to_rule
        s12 = str_store_string(gstr._right_to_rule_reg12)
    #end
    str_clear(15)
    if _claim_arguments_made > 0 or _ruler_arguments_made > 0 or _victory_arguments_made > 0 or _lords_arguments_made > 0 or 1 == 0:
        reg3 = _claim_arguments_made
        reg4 = _ruler_arguments_made
        reg5 = _victory_arguments_made
        reg6 = _lords_arguments_made
        reg7 = _benefit_arguments_made
        s15 = str_store_string(gstr.political_arguments_made_legality_reg3_rights_of_lords_reg4_unificationpeace_reg5_rights_of_commons_reg6_fief_pledges_reg7)
    #end
    reg3 = _player_honor
    reg2 = troop_get_slot(trp.player,7)
    s9 = str_store_string(gstr.renown_reg2_honour_rating_reg3s12_friends_s8_enemies_s6_s9)
    get_number_of_hero_centers(trp.player)
    var005 = reg0
    if var005 > 0:
        for var006 in range(0, var005):
            troop_get_leaded_center_with_index(trp.player,var006)
            var007 = reg0
            if var006 == 0:
                s8 = str_store_party_name(var007)
            elif var006 == 1:
                s7 = str_store_party_name(var007)
                s8 = str_store_string("@{s7} and {s8}")
            else:
                s7 = str_store_party_name(var007)
                s8 = str_store_string("@{!}{s7}, {s8}")
            #end
        #end
        s9 = str_store_string("@Your estates are: {s8}.^{s9}")
    #end
    if _players_kingdom > 0:
        s8 = str_store_faction_name(_players_kingdom)
        if is_between(_players_kingdom,fac.kingdom_1,fac.kingdoms_end) or not faction_slot_eq(fac.player_supporters_faction,11,trp.player):
            s9 = str_store_string(gstr.you_are_a_lord_lady_of_s8_s9)
        else:
            s9 = str_store_string(gstr.you_are_king_queen_of_s8_s9)
        #end
    #end
character_report.conditionBlock = condition

character_report_continue = MenuOption("continue", "{!}CHEAT! - increase Right to Rule")
def code():
    _player_right_to_rule += 10
    jump_to_menu(mnu.character_report)
character_report_continue.codeBlock = code

character_report_continue = MenuOption("continue", "{!}CHEAT! - increase your relation with {s14}")
def condition():
    if _cheat_mode == 1:
        s14 = str_store_troop_name(_g_talk_troop)
character_report_continue.conditionBlock = condition
def code():
    change_player_relation_with_troop(_g_talk_troop,10)
    jump_to_menu(mnu.character_report)
character_report_continue.codeBlock = code

character_report_continue = MenuOption("continue", "{!}CHEAT! - increase honor")
def code():
    _player_honor += 10
    jump_to_menu(mnu.character_report)
character_report_continue.codeBlock = code

character_report_continue = MenuOption("continue", "{!}CHEAT! - increase renown")
def code():
    troop_slot_001 = troop_get_slot(trp.player,7)
    troop_slot_001 += 50
    troop_set_slot(trp.player,7,troop_slot_001)
    jump_to_menu(mnu.character_report)
character_report_continue.codeBlock = code

character_report_continue = MenuOption("continue", "{!}CHEAT! - increase persuasion")
def code():
    troop_raise_skill(trp.player,skl.persuasion,1)
    jump_to_menu(mnu.character_report)
character_report_continue.codeBlock = code

character_report_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.reports)
character_report_continue.codeBlock = code



party_size_report = GameMenu("party_size_report", 0,
"{s1}"
)
def condition():
    game_get_party_companion_limit()
    var001 = reg0
    skill_lvl_002 = store_skill_level(skl.leadership,trp.player)
    skill_lvl_002 *= 5
    attribute_lvl_003 = store_attribute_level(trp.player,3)
    troop_slot_004 = troop_get_slot(trp.player,7)
    troop_slot_004 /= 25
    if skill_lvl_002 > 0:
        s2 = str_store_string("@{!} +")
    else:
        s2 = str_store_string(gstr.space)
    #end
    if attribute_lvl_003 > 0:
        s3 = str_store_string("@{!} +")
    else:
        s3 = str_store_string(gstr.space)
    #end
    if troop_slot_004 > 0:
        s4 = str_store_string("@{!} +")
    else:
        s4 = str_store_string(gstr.space)
    #end
    reg5 = var001
    reg1 = skill_lvl_002
    reg2 = attribute_lvl_003
    reg3 = troop_slot_004
    s1 = str_store_string("@Current party size limit is {reg5}.^Current party size modifiers are:^^Base size:  +30^Leadership: {s2}{reg1}^Charisma: {s3}{reg2}^Renown: {s4}{reg3}^TOTAL:  {reg5}")
party_size_report.conditionBlock = condition

party_size_report_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.reports)
party_size_report_continue.codeBlock = code



faction_relations_report = GameMenu("faction_relations_report", 0,
"{s1}"
)
def condition():
    str_clear(2)
    for fac_001 in range(fac.player_supporters_faction, fac.kingdoms_end):
        if faction_slot_eq(fac_001,21,0) and fac_001 != fac.player_supporters_faction:
            faction_relation_002 = store_relation(fac.player_supporters_faction,fac_001)
            if faction_relation_002 >= 90:
                s3 = str_store_string("@Loyal")
            elif faction_relation_002 >= 80:
                s3 = str_store_string("@Devoted")
            elif faction_relation_002 >= 70:
                s3 = str_store_string("@Fond")
            elif faction_relation_002 >= 60:
                s3 = str_store_string("@Gracious")
            elif faction_relation_002 >= 50:
                s3 = str_store_string("@Friendly")
            elif faction_relation_002 >= 40:
                s3 = str_store_string("@Supportive")
            elif faction_relation_002 >= 30:
                s3 = str_store_string("@Favorable")
            elif faction_relation_002 >= 20:
                s3 = str_store_string("@Cooperative")
            elif faction_relation_002 >= 10:
                s3 = str_store_string("@Accepting")
            elif faction_relation_002 >= 0:
                s3 = str_store_string("@Indifferent")
            elif faction_relation_002 >= -10:
                s3 = str_store_string("@Suspicious")
            elif faction_relation_002 >= -20:
                s3 = str_store_string("@Grumbling")
            elif faction_relation_002 >= -30:
                s3 = str_store_string("@Hostile")
            elif faction_relation_002 >= -40:
                s3 = str_store_string("@Resentful")
            elif faction_relation_002 >= -50:
                s3 = str_store_string("@Angry")
            elif faction_relation_002 >= -60:
                s3 = str_store_string("@Hateful")
            elif faction_relation_002 >= -70:
                s3 = str_store_string("@Revengeful")
            else:
                s3 = str_store_string("@Vengeful")
            #end
        #end
        s4 = str_store_faction_name(fac_001)
        reg1 = faction_relation_002
        s2 = str_store_string("@{!}{s2}^{s4}: {reg1} [[[{s3}]]]")
    #end
    s1 = str_store_string("@Your relation with the factions are:^{s2}")
faction_relations_report.conditionBlock = condition

faction_relations_report_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.reports)
faction_relations_report_continue.codeBlock = code



camp = GameMenu("camp", 4096,
"You set up camp. What do you want to do?"
)
def condition():
    _g_player_icon_state = 0
    set_background_mesh(mesh.pic_camp)
camp.conditionBlock = condition

camp_camp_action_1 = MenuOption("camp_action_1", "{!}Cheat: Walk around.")
def code():
    set_jump_mission(mt.ai_training)
    setup_random_scene()
    change_screen_mission()
camp_camp_action_1.codeBlock = code

camp_camp_action = MenuOption("camp_action", "Take an action.")
def code():
    jump_to_menu(mnu.camp_action)
camp_camp_action.codeBlock = code

camp_camp_wait_here = MenuOption("camp_wait_here", "Wait here for some time.")
def code():
    _g_camp_mode = 1
    _g_infinite_camping = 0
    _g_player_icon_state = 1
    if party_is_active(p.main_party):
        party_cur_terrain_001 = party_get_current_terrain(p.main_party)
        if party_cur_terrain_001 == 5:
            unlock_achievement(28)
        #end
    #end
    rest_for_hours_interactive(8760,5,1)
    change_screen_return()
camp_camp_wait_here.codeBlock = code

camp_camp_cheat = MenuOption("camp_cheat", "CHEAT MENU!")
def code():
    jump_to_menu(mnu.camp_cheat)
camp_camp_cheat.codeBlock = code

camp_resume_travelling = MenuOption("resume_travelling", "Resume travelling.")
def code():
    change_screen_return()
camp_resume_travelling.codeBlock = code



camp_cheat = GameMenu("camp_cheat", 0,
"Select a cheat:"
)

camp_cheat_camp_cheat_find_item = MenuOption("camp_cheat_find_item", "Find an item...")
def code():
    jump_to_menu(mnu.cheat_find_item)
camp_cheat_camp_cheat_find_item.codeBlock = code

camp_cheat_camp_cheat_find_item = MenuOption("camp_cheat_find_item", "Change weather..")
def code():
    jump_to_menu(mnu.cheat_change_weather)
camp_cheat_camp_cheat_find_item.codeBlock = code

camp_cheat_camp_cheat_1 = MenuOption("camp_cheat_1", "{!}Increase player renown.")
def code():
    s1 = str_store_string("@Player renown is increased by 100. ")
    change_troop_renown(trp.player,100)
    jump_to_menu(mnu.camp_cheat)
camp_cheat_camp_cheat_1.codeBlock = code

camp_cheat_camp_cheat_2 = MenuOption("camp_cheat_2", "{!}Increase player honor.")
def code():
    reg7 = _player_honor
    reg7 += 1
    print("@Player honor is increased by 1 and it is now {reg7}.")
    _player_honor += 1
    jump_to_menu(mnu.camp_cheat)
camp_cheat_camp_cheat_2.codeBlock = code

camp_cheat_camp_cheat_3 = MenuOption("camp_cheat_3", "{!}Update political notes.")
def code():
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        if troop_slot_eq(trp_001,2,2):
            update_troop_political_notes(trp_001)
        #end
    #end
    for fac_002 in range(fac.player_supporters_faction, fac.kingdoms_end):
        update_faction_political_notes(fac_002)
    #end
camp_cheat_camp_cheat_3.codeBlock = code

camp_cheat_camp_cheat_4 = MenuOption("camp_cheat_4", "{!}Update troop notes.")
def code():
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        if troop_slot_eq(trp_001,2,2):
            update_troop_notes(trp_001)
        #end
    #end
    for trp_002 in range(trp.knight_1_1_wife, trp.heroes_end):
        update_troop_notes(trp_002)
        update_troop_political_notes(trp_002)
        update_troop_location_notes(trp_002,0)
    #end
camp_cheat_camp_cheat_4.codeBlock = code

camp_cheat_camp_cheat_5 = MenuOption("camp_cheat_5", "{!}Scramble minstrels.")
def code():
    update_tavern_minstrels()
camp_cheat_camp_cheat_5.codeBlock = code

camp_cheat_camp_cheat_6 = MenuOption("camp_cheat_6", "{!}Infinite camp")
def code():
    _g_camp_mode = 1
    _g_infinite_camping = 1
    _g_player_icon_state = 1
    rest_for_hours_interactive(87600,20)
    change_screen_return()
camp_cheat_camp_cheat_6.codeBlock = code

camp_cheat_cheat_faction_orders = MenuOption("cheat_faction_orders", "{!}Cheat: Set Debug messages to All.")
def code():
    _cheat_mode = 1
    jump_to_menu(mnu.camp_cheat)
camp_cheat_cheat_faction_orders.codeBlock = code

camp_cheat_cheat_faction_orders = MenuOption("cheat_faction_orders", "{!}Cheat: Set Debug messages to Econ Only.")
def code():
    _cheat_mode = 3
    jump_to_menu(mnu.camp_cheat)
camp_cheat_cheat_faction_orders.codeBlock = code

camp_cheat_cheat_faction_orders = MenuOption("cheat_faction_orders", "{!}Cheat: Set Debug messages to Political Only.")
def code():
    _cheat_mode = 4
    jump_to_menu(mnu.camp_cheat)
camp_cheat_cheat_faction_orders.codeBlock = code

camp_cheat_back_to_camp_menu = MenuOption("back_to_camp_menu", "{!}Back to camp menu.")
def code():
    jump_to_menu(mnu.camp)
camp_cheat_back_to_camp_menu.codeBlock = code



cheat_find_item = GameMenu("cheat_find_item", 0,
"{!}Current item range: {reg5} to {reg6}"
)
def condition():
    reg5 = _cheat_find_item_range_begin
    reg6 = _cheat_find_item_range_begin + 96
    val_min(reg6,itm.items_end)
    reg6 -= 1
cheat_find_item.conditionBlock = condition

cheat_find_item_cheat_find_item_next_range = MenuOption("cheat_find_item_next_range", "{!}Move to next item range.")
def code():
    _cheat_find_item_range_begin += 96
    if _cheat_find_item_range_begin >= itm.items_end:
        _cheat_find_item_range_begin = 0
    #end
    jump_to_menu(mnu.cheat_find_item)
cheat_find_item_cheat_find_item_next_range.codeBlock = code

cheat_find_item_cheat_find_item_choose_this = MenuOption("cheat_find_item_choose_this", "{!}Choose from this range.")
def code():
    troop_clear_inventory(trp.find_item_cheat)
    var001 = _cheat_find_item_range_begin + 96
    val_min(var001,itm.items_end)
    var002 = var001 - _cheat_find_item_range_begin
    for var003 in range(0, var002):
        item_id_004 = _cheat_find_item_range_begin + var003
        troop_add_items(trp.find_item_cheat,item_id_004,1)
    #end
    change_screen_trade(trp.find_item_cheat)
cheat_find_item_cheat_find_item_choose_this.codeBlock = code

cheat_find_item_camp_action_4 = MenuOption("camp_action_4", "{!}Back to camp menu.")
def code():
    jump_to_menu(mnu.camp)
cheat_find_item_camp_action_4.codeBlock = code



cheat_change_weather = GameMenu("cheat_change_weather", 0,
"{!}Current cloud amount: {reg5}^Current Fog Strength: {reg6}"
)
def condition():
    reg5 = get_global_cloud_amount()
    reg6 = get_global_haze_amount()
cheat_change_weather.conditionBlock = condition

cheat_change_weather_cheat_increase_cloud = MenuOption("cheat_increase_cloud", "{!}Increase Cloud Amount.")
def code():
    var001 = get_global_cloud_amount()
    var001 += 5
    val_min(var001,100)
    set_global_cloud_amount(var001)
cheat_change_weather_cheat_increase_cloud.codeBlock = code

cheat_change_weather_cheat_decrease_cloud = MenuOption("cheat_decrease_cloud", "{!}Decrease Cloud Amount.")
def code():
    var001 = get_global_cloud_amount()
    var001 -= 5
    val_max(var001,0)
    set_global_cloud_amount(var001)
cheat_change_weather_cheat_decrease_cloud.codeBlock = code

cheat_change_weather_cheat_increase_fog = MenuOption("cheat_increase_fog", "{!}Increase Fog Amount.")
def code():
    var001 = get_global_haze_amount()
    var001 += 5
    val_min(var001,100)
    set_global_haze_amount(var001)
cheat_change_weather_cheat_increase_fog.codeBlock = code

cheat_change_weather_cheat_decrease_fog = MenuOption("cheat_decrease_fog", "{!}Decrease Fog Amount.")
def code():
    var001 = get_global_haze_amount()
    var001 -= 5
    val_max(var001,0)
    set_global_haze_amount(var001)
cheat_change_weather_cheat_decrease_fog.codeBlock = code

cheat_change_weather_camp_action_4 = MenuOption("camp_action_4", "{!}Back to camp menu.")
def code():
    jump_to_menu(mnu.camp)
cheat_change_weather_camp_action_4.codeBlock = code



camp_action = GameMenu("camp_action", 0,
"Choose an action:"
)

camp_action_camp_recruit_prisoners = MenuOption("camp_recruit_prisoners", "Recruit some of your prisoners to your party.")
def condition():
    if troops_can_join(1):
        cur_hours_001 = store_current_hours()
        cur_hours_001 -= 24
        if cur_hours_001 > _g_prisoner_recruit_last_time:
            if _g_prisoner_recruit_last_time > 0:
                _g_prisoner_recruit_troop_id = 0
                _g_prisoner_recruit_size = 0
                _g_prisoner_recruit_last_time = 0
            #end
        #end
    #end
camp_action_camp_recruit_prisoners.conditionBlock = condition
def code():
    jump_to_menu(mnu.camp_recruit_prisoners)
camp_action_camp_recruit_prisoners.codeBlock = code

camp_action_action_read_book = MenuOption("action_read_book", "Select a book to read.")
def code():
    jump_to_menu(mnu.camp_action_read_book)
camp_action_action_read_book.codeBlock = code

camp_action_action_rename_kingdom = MenuOption("action_rename_kingdom", "Rename your kingdom.")
def code():
    start_presentation(prsnt.name_kingdom)
camp_action_action_rename_kingdom.codeBlock = code

camp_action_action_modify_banner = MenuOption("action_modify_banner", "{!}Cheat: Modify your banner.")
def code():
    start_presentation(prsnt.banner_selection)
camp_action_action_modify_banner.codeBlock = code

camp_action_action_retire = MenuOption("action_retire", "Retire from adventuring.")
def code():
    jump_to_menu(mnu.retirement_verify)
camp_action_action_retire.codeBlock = code

camp_action_camp_action_4 = MenuOption("camp_action_4", "Back to camp menu.")
def code():
    jump_to_menu(mnu.camp)
camp_action_camp_action_4.codeBlock = code



camp_recruit_prisoners = GameMenu("camp_recruit_prisoners", 0,
"You offer your prisoners freedom if they agree to join you as soldiers. {s18}"
)
def condition():
    var001 = 0
    party_num_prisoners_stacks_002 = party_get_num_prisoner_stacks(p.main_party)
    for var003 in range(0, party_num_prisoners_stacks_002):
        party_prisoner_troop_id_004 = party_prisoner_stack_get_troop_id(p.main_party,var003)
        if not troop_is_hero(party_prisoner_troop_id_004):
            var001 += 1
        #end
    #end
    if var001 == 0:
        jump_to_menu(mnu.camp_no_prisoners)
    elif _g_prisoner_recruit_troop_id == 0:
        _g_prisoner_recruit_last_time = store_current_hours()
        random_x_005 = store_random_in_range(0,100)
        skill_lvl_006 = store_skill_level(skl.persuasion,trp.player)
        var007 = 15 - skill_lvl_006
        var007 *= 4
        if random_x_005 < var007:
            _g_prisoner_recruit_troop_id = -7
        else:
            var001 = 0
            party_num_prisoners_stacks_002 = party_get_num_prisoner_stacks(p.main_party)
            for var003 in range(0, party_num_prisoners_stacks_002):
                party_prisoner_troop_id_004 = party_prisoner_stack_get_troop_id(p.main_party,var003)
                if not troop_is_hero(party_prisoner_troop_id_004):
                    var001 += 1
                #end
            #end
            random_x_008 = store_random_in_range(0,var001)
            for var003 in range(0, party_num_prisoners_stacks_002):
                party_prisoner_troop_id_004 = party_prisoner_stack_get_troop_id(p.main_party,var003)
                if not troop_is_hero(party_prisoner_troop_id_004):
                    random_x_008 -= 1
                    if random_x_008 < 0:
                        party_num_prisoners_stacks_002 = 0
                        _g_prisoner_recruit_troop_id = party_prisoner_troop_id_004
                        _g_prisoner_recruit_size = party_prisoner_stack_get_size(p.main_party,var003)
                    #end
                #end
            #end
        #end
        if _g_prisoner_recruit_troop_id > 0:
            party_free_companions_capacity_009 = party_get_free_companions_capacity(p.main_party)
            val_min(_g_prisoner_recruit_size,party_free_companions_capacity_009)
            reg1 = _g_prisoner_recruit_size
            if _g_prisoner_recruit_size > 0:
                if _g_prisoner_recruit_size > 1:
                    reg2 = 1
                else:
                    reg2 = 0
                #end
            #end
            str_store_troop_name_by_count(s1,_g_prisoner_recruit_troop_id,_g_prisoner_recruit_size)
            s18 = str_store_string("@{reg1} {s1} {reg2?accept:accepts} the offer.")
        else:
            s18 = str_store_string("@No one accepts the offer.")
        #end
    #end
camp_recruit_prisoners.conditionBlock = condition

camp_recruit_prisoners_camp_recruit_prisoners_accept = MenuOption("camp_recruit_prisoners_accept", "Take them.")
def code():
    remove_troops_from_prisoners(_g_prisoner_recruit_troop_id,_g_prisoner_recruit_size)
    party_add_members(p.main_party,_g_prisoner_recruit_troop_id,_g_prisoner_recruit_size)
    var001 = -3 * _g_prisoner_recruit_size
    change_player_party_morale(var001)
    jump_to_menu(mnu.camp)
camp_recruit_prisoners_camp_recruit_prisoners_accept.codeBlock = code

camp_recruit_prisoners_camp_recruit_prisoners_reject = MenuOption("camp_recruit_prisoners_reject", "Reject them.")
def code():
    jump_to_menu(mnu.camp)
    _g_prisoner_recruit_troop_id = 0
    _g_prisoner_recruit_size = 0
camp_recruit_prisoners_camp_recruit_prisoners_reject.codeBlock = code

camp_recruit_prisoners_continue = MenuOption("continue", "Go back.")
def code():
    jump_to_menu(mnu.camp)
camp_recruit_prisoners_continue.codeBlock = code



camp_no_prisoners = GameMenu("camp_no_prisoners", 0,
"You have no prisoners to recruit from."
)

camp_no_prisoners_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.camp)
camp_no_prisoners_continue.codeBlock = code



camp_action_read_book = GameMenu("camp_action_read_book", 0,
"Choose a book to read:"
)

camp_action_read_book_action_read_book_1 = MenuOption("action_read_book_1", "{s1}.")
def condition():
    if player_has_item(itm.book_tactics) and item_slot_eq(itm.book_tactics,3,0):
        s1 = str_store_item_name(itm.book_tactics)
camp_action_read_book_action_read_book_1.conditionBlock = condition
def code():
    _temp = itm.book_tactics
    jump_to_menu(mnu.camp_action_read_book_start)
camp_action_read_book_action_read_book_1.codeBlock = code

camp_action_read_book_action_read_book_2 = MenuOption("action_read_book_2", "{s1}.")
def condition():
    if player_has_item(itm.book_persuasion) and item_slot_eq(itm.book_persuasion,3,0):
        s1 = str_store_item_name(itm.book_persuasion)
camp_action_read_book_action_read_book_2.conditionBlock = condition
def code():
    _temp = itm.book_persuasion
    jump_to_menu(mnu.camp_action_read_book_start)
camp_action_read_book_action_read_book_2.codeBlock = code

camp_action_read_book_action_read_book_3 = MenuOption("action_read_book_3", "{s1}.")
def condition():
    if player_has_item(itm.book_leadership) and item_slot_eq(itm.book_leadership,3,0):
        s1 = str_store_item_name(itm.book_leadership)
camp_action_read_book_action_read_book_3.conditionBlock = condition
def code():
    _temp = itm.book_leadership
    jump_to_menu(mnu.camp_action_read_book_start)
camp_action_read_book_action_read_book_3.codeBlock = code

camp_action_read_book_action_read_book_4 = MenuOption("action_read_book_4", "{s1}.")
def condition():
    if player_has_item(itm.book_intelligence) and item_slot_eq(itm.book_intelligence,3,0):
        s1 = str_store_item_name(itm.book_intelligence)
camp_action_read_book_action_read_book_4.conditionBlock = condition
def code():
    _temp = itm.book_intelligence
    jump_to_menu(mnu.camp_action_read_book_start)
camp_action_read_book_action_read_book_4.codeBlock = code

camp_action_read_book_action_read_book_5 = MenuOption("action_read_book_5", "{s1}.")
def condition():
    if player_has_item(itm.book_trade) and item_slot_eq(itm.book_trade,3,0):
        s1 = str_store_item_name(itm.book_trade)
camp_action_read_book_action_read_book_5.conditionBlock = condition
def code():
    _temp = itm.book_trade
    jump_to_menu(mnu.camp_action_read_book_start)
camp_action_read_book_action_read_book_5.codeBlock = code

camp_action_read_book_action_read_book_6 = MenuOption("action_read_book_6", "{s1}.")
def condition():
    if player_has_item(itm.book_weapon_mastery) and item_slot_eq(itm.book_weapon_mastery,3,0):
        s1 = str_store_item_name(itm.book_weapon_mastery)
camp_action_read_book_action_read_book_6.conditionBlock = condition
def code():
    _temp = itm.book_weapon_mastery
    jump_to_menu(mnu.camp_action_read_book_start)
camp_action_read_book_action_read_book_6.codeBlock = code

camp_action_read_book_action_read_book_7 = MenuOption("action_read_book_7", "{s1}.")
def condition():
    if player_has_item(itm.book_engineering) and item_slot_eq(itm.book_engineering,3,0):
        s1 = str_store_item_name(itm.book_engineering)
camp_action_read_book_action_read_book_7.conditionBlock = condition
def code():
    _temp = itm.book_engineering
    jump_to_menu(mnu.camp_action_read_book_start)
camp_action_read_book_action_read_book_7.codeBlock = code

camp_action_read_book_camp_action_4 = MenuOption("camp_action_4", "Back to camp menu.")
def code():
    jump_to_menu(mnu.camp)
camp_action_read_book_camp_action_4.codeBlock = code



camp_action_read_book_start = GameMenu("camp_action_read_book_start", 0,
"{s1}"
)
def condition():
    item_id_001 = _temp
    s2 = str_store_item_name(item_id_001)
    if True:
        attribute_lvl_002 = store_attribute_level(trp.player,2)
        item_slot_003 = item_get_slot(item_id_001,4)
        if item_slot_003 <= attribute_lvl_002:
            s1 = str_store_string("@You start reading {s2}. After a few pages;;; you feel you could learn a lot from this book. You decide to keep it close by and read whenever you have the time.")
            _g_player_reading_book = item_id_001
        else:
            s1 = str_store_string("@You flip through the pages of {s2};;; but you find the text confusing and difficult to follow. Try as you might;;; it soon gives you a headache;;; and you're forced to give up the attempt.")
        #end
    #end
camp_action_read_book_start.conditionBlock = condition

camp_action_read_book_start_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.camp)
camp_action_read_book_start_continue.codeBlock = code



retirement_verify = GameMenu("retirement_verify", 0,
"You are at day {reg0}. Your current luck is {reg1}. Are you sure you want to retire?"
)
def condition():
    reg0 = store_current_day()
    reg1 = _g_player_luck
retirement_verify.conditionBlock = condition

retirement_verify_retire_yes = MenuOption("retire_yes", "Yes.")
def code():
    start_presentation(prsnt.retirement)
retirement_verify_retire_yes.codeBlock = code

retirement_verify_retire_no = MenuOption("retire_no", "No.")
def code():
    jump_to_menu(mnu.camp)
retirement_verify_retire_no.codeBlock = code



end_game = GameMenu("end_game", 0,
"The decision is made, and you resolve to give up your adventurer's life and settle down. You sell off your weapons and armour, gather up all your money, and ride off into the sunset...."
)

end_game_end_game_bye = MenuOption("end_game_bye", "Farewell.")
def code():
    change_screen_quit()
end_game_end_game_bye.codeBlock = code



cattle_herd = GameMenu("cattle_herd", 4096,
"You encounter a herd of cattle."
)
def condition():
    play_sound(snd.cow_moo)
    set_background_mesh(mesh.pic_cattle)
cattle_herd.conditionBlock = condition

cattle_herd_cattle_drive_away = MenuOption("cattle_drive_away", "Drive the cattle onward.")
def code():
    party_set_slot(_g_encountered_party,7,1)
    party_set_ai_behavior(_g_encountered_party,11)
    party_set_ai_object(_g_encountered_party,p.main_party)
    change_screen_return()
cattle_herd_cattle_drive_away.codeBlock = code

cattle_herd_cattle_stop = MenuOption("cattle_stop", "Bring the herd to a stop.")
def code():
    party_set_slot(_g_encountered_party,7,0)
    party_set_ai_behavior(_g_encountered_party,0)
    change_screen_return()
cattle_herd_cattle_stop.codeBlock = code

cattle_herd_cattle_kill = MenuOption("cattle_kill", "Slaughter some of the animals.")
def condition():
    var001 = 1
    if check_quest_active(qst.move_cattle_herd) and quest_slot_eq(qst.move_cattle_herd,8,_g_encountered_party):
        var001 = 0
    #end
cattle_herd_cattle_kill.conditionBlock = condition
def code():
    jump_to_menu(mnu.cattle_herd_kill)
cattle_herd_cattle_kill.codeBlock = code

cattle_herd_leave = MenuOption("leave", "Leave.")
def code():
    change_screen_return()
cattle_herd_leave.codeBlock = code



cattle_herd_kill = GameMenu("cattle_herd_kill", 0,
"How many animals do you want to slaughter?"
)
def condition():
    reg5 = party_get_num_companions(_g_encountered_party)
cattle_herd_kill.conditionBlock = condition

cattle_herd_kill_cattle_kill_1 = MenuOption("cattle_kill_1", "One.")
def code():
    kill_cattle_from_herd(_g_encountered_party,1)
    jump_to_menu(mnu.cattle_herd_kill_end)
    change_screen_loot(trp.temp_troop)
    play_sound(snd.cow_slaughter)
cattle_herd_kill_cattle_kill_1.codeBlock = code

cattle_herd_kill_cattle_kill_2 = MenuOption("cattle_kill_2", "Two.")
def code():
    kill_cattle_from_herd(_g_encountered_party,2)
    jump_to_menu(mnu.cattle_herd_kill_end)
    change_screen_loot(trp.temp_troop)
    play_sound(snd.cow_slaughter)
cattle_herd_kill_cattle_kill_2.codeBlock = code

cattle_herd_kill_cattle_kill_3 = MenuOption("cattle_kill_3", "Three.")
def code():
    kill_cattle_from_herd(_g_encountered_party,3)
    jump_to_menu(mnu.cattle_herd_kill_end)
    change_screen_loot(trp.temp_troop)
    play_sound(snd.cow_slaughter)
cattle_herd_kill_cattle_kill_3.codeBlock = code

cattle_herd_kill_cattle_kill_4 = MenuOption("cattle_kill_4", "Four.")
def code():
    kill_cattle_from_herd(_g_encountered_party,4)
    jump_to_menu(mnu.cattle_herd_kill_end)
    change_screen_loot(trp.temp_troop)
    play_sound(snd.cow_slaughter)
cattle_herd_kill_cattle_kill_4.codeBlock = code

cattle_herd_kill_cattle_kill_5 = MenuOption("cattle_kill_5", "Five.")
def code():
    kill_cattle_from_herd(_g_encountered_party,5)
    jump_to_menu(mnu.cattle_herd_kill_end)
    change_screen_loot(trp.temp_troop)
    play_sound(snd.cow_slaughter)
cattle_herd_kill_cattle_kill_5.codeBlock = code

cattle_herd_kill_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    jump_to_menu(mnu.cattle_herd)
cattle_herd_kill_go_back_dot.codeBlock = code



cattle_herd_kill_end = GameMenu("cattle_herd_kill_end", 0,
"{!}You shouldn't be reading this."
)
def condition():
    change_screen_return()
cattle_herd_kill_end.conditionBlock = condition



arena_duel_fight = GameMenu("arena_duel_fight", 0,
"You and your opponent prepare to duel."
)

arena_duel_fight_continue = MenuOption("continue", "Continue...")
def code():
    _g_leave_encounter = 0
    if is_between(_g_encountered_party,p.town_1,p.castle_1):
        party_slot_001 = party_get_slot(_g_encountered_party,16)
    elif _g_start_arena_fight_at_nearest_town == 1:
        party_id_002 = -1
        var003 = 10000
        for p_004 in range(p.town_1, p.castle_1):
            distance_parties_005 = store_distance_to_party_from_party(p_004,_g_encountered_party)
            if distance_parties_005 < var003:
                var003 = distance_parties_005
                party_id_002 = p_004
            #end
        #end
        if party_id_002 >= 0:
            party_slot_001 = party_get_slot(party_id_002,16)
        #end
        _g_start_arena_fight_at_nearest_town = 0
    else:
        party_cur_terrain_006 = party_get_current_terrain(p.main_party)
        if party_cur_terrain_006 == 4:
            party_slot_001 = scn.training_ground_ranged_melee_3
        elif party_cur_terrain_006 == 5:
            party_slot_001 = scn.training_ground_ranged_melee_4
        else:
            party_slot_001 = scn.training_ground_ranged_melee_1
        #end
    #end
    modify_visitors_at_site(party_slot_001)
    reset_visitors()
    set_visitor(0,trp.player)
    set_visitor(1,_g_duel_troop)
    set_jump_mission(mt.duel_with_lord)
    jump_to_scene(party_slot_001)
    jump_to_menu(mnu.arena_duel_conclusion)
    change_screen_mission()
arena_duel_fight_continue.codeBlock = code



arena_duel_conclusion = GameMenu("arena_duel_conclusion", 0,
"{!}{s11}"
)
def condition():
    if _g_leave_encounter == 1:
        change_screen_return()
    #end
    s10 = str_store_troop_name(_g_duel_troop)
    if quest_slot_eq(qst.duel_for_lady,2,_g_duel_troop) and check_quest_failed(qst.duel_for_lady):
        s11 = str_store_string(gstr.you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel)
    elif quest_slot_eq(qst.duel_for_lady,2,_g_duel_troop) and check_quest_succeeded(qst.duel_for_lady):
        s11 = str_store_string(gstr.s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel)
    elif quest_slot_eq(qst.duel_courtship_rival,2,_g_duel_troop) and check_quest_failed(qst.duel_courtship_rival):
        s11 = str_store_string(gstr.you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel)
    elif quest_slot_eq(qst.duel_courtship_rival,2,_g_duel_troop) and check_quest_succeeded(qst.duel_courtship_rival):
        s11 = str_store_string(gstr.s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel)
    elif quest_slot_eq(qst.duel_avenge_insult,2,_g_duel_troop) and check_quest_succeeded(qst.duel_avenge_insult):
        s11 = str_store_string(gstr.s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel)
    elif quest_slot_eq(qst.duel_avenge_insult,2,_g_duel_troop) and check_quest_failed(qst.duel_avenge_insult):
        s11 = str_store_string(gstr.you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel)
    elif quest_slot_eq(qst.denounce_lord,2,_g_duel_troop) and check_quest_succeeded(qst.denounce_lord):
        s11 = str_store_string(gstr.s10_lies_in_the_arenas_dust_for_several_minutes_then_staggers_to_his_feet_you_have_won_the_duel)
    elif quest_slot_eq(qst.denounce_lord,2,_g_duel_troop) and check_quest_failed(qst.denounce_lord):
        s11 = str_store_string(gstr.you_lie_stunned_for_several_minutes_then_stagger_to_your_feet_to_find_your_s10_standing_over_you_you_have_lost_the_duel)
    else:
        s10 = str_store_troop_name(_g_duel_troop)
    #end
arena_duel_conclusion.conditionBlock = condition

arena_duel_conclusion_continue = MenuOption("continue", "Continue...")
def code():
    get_meeting_scene()
    scene_id_001 = reg0
    modify_visitors_at_site(scene_id_001)
    reset_visitors()
    set_visitor(0,trp.player)
    set_visitor(17,_g_duel_troop)
    set_jump_mission(mt.conversation_encounter)
    jump_to_scene(scene_id_001)
    _talk_context = 17
    change_screen_map_conversation(_g_duel_troop)
arena_duel_conclusion_continue.codeBlock = code



simple_encounter = GameMenu("simple_encounter", 4352,
"{s2} You have {reg10} troops fit for battle against their {reg11}."
)
def condition():
    _g_enemy_party = _g_encountered_party
    _g_ally_party = -1
    encounter_calculate_fit()
    if _new_encounter == 1:
        _new_encounter = 0
        _g_encounter_is_in_village = 0
        _g_encounter_type = 0
        if party_slot_eq(_g_enemy_party,4,5):
            party_slot_001 = party_get_slot(_g_enemy_party,5)
            distance_parties_002 = store_distance_to_party_from_party(party_slot_001,_g_enemy_party)
            if distance_parties_002 < 4:
                _g_encounter_is_in_village = party_slot_001
                _g_encounter_type = 1
            #end
        #end
        if _g_player_raiding_village > 0:
            _g_encounter_is_in_village = _g_player_raiding_village
            _g_encounter_type = 2
            party_quick_attach_to_current_battle(_g_encounter_is_in_village,1)
            s1 = str_store_string("@Villagers")
            print(gstr.s1_joined_battle_enemy)
        elif _g_encounter_type == 1:
            party_quick_attach_to_current_battle(_g_encounter_is_in_village,0)
            s1 = str_store_string("@Villagers")
            print(gstr.s1_joined_battle_friend)
        #end
        let_nearby_parties_join_current_battle(0,0)
        encounter_init_variables()
        _encountered_party_hostile = 0
        _encountered_party_friendly = 0
        if _g_encountered_party_relation > 0:
            _encountered_party_friendly = 1
        #end
        if _g_encountered_party_relation < 0:
            _encountered_party_hostile = 1
            if encountered_party_is_attacker():
                _cant_leave_encounter = 1
            #end
        #end
        _talk_context = 2
        setup_party_meeting(_g_encountered_party)
    else:
        if _cant_leave_encounter == 1:
            party_count_members_with_full_health(p.main_party_backup)
            var003 = reg0
            party_count_members_with_full_health(p.encountered_party_backup)
            var003 += reg0
            party_count_members_with_full_health(p.main_party)
            var004 = reg0
            party_count_members_with_full_health(p.collective_enemy)
            var004 += reg0
            var005 = var003 - 10
            if var004 < var005:
                _cant_leave_encounter = 0
            #end
        #end
        if _g_leave_encounter == 1:
            change_screen_return()
        #end
    #end
    if party_is_active(_g_encountered_party):
        s1 = str_store_party_name(_g_encountered_party)
        if _g_encounter_type == 0:
            s2 = str_store_string("@You have encountered {s1}.")
        elif _g_encounter_type == 1:
            s3 = str_store_party_name(_g_encounter_is_in_village)
            s2 = str_store_string("@You have engaged {s1} while they were raiding {s3}.")
        elif _g_encounter_type == 2:
            s3 = str_store_party_name(_g_encounter_is_in_village)
            s2 = str_store_string("@You were caught by {s1} while your forces were raiding {s3}.")
        #end
    #end
    if True:
        party_count_members_with_full_health(p.collective_enemy)
        var006 = reg0
        var007 = 0
        if _g_battle_result == 1 and var006 > 0 or var006 <= _num_routed_enemies:
            var007 = 1
        elif _g_engaged_enemy == 1 and var006 > 0 or _g_enemy_fit_for_battle <= _num_routed_enemies and _g_friend_fit_for_battle >= 1:
            var007 = 1
        #end
        if var007 == 1 or _g_enemy_surrenders == 1:
            _g_next_menu = -1
            jump_to_menu(mnu.total_victory)
        else:
            party_count_members_with_full_health(p.main_party)
            var008 = reg0
            var009 = 0
            if _g_battle_result == -1 and var008 <= _num_routed_us:
                var009 = 1
            elif _g_engaged_enemy == 1 and _g_enemy_fit_for_battle >= 1 and _g_friend_fit_for_battle <= 0:
                var009 = 1
            #end
        #end
        if var009 == 1 or _g_player_surrenders == 1:
            _g_next_menu = mnu.captivity_start_wilderness
            jump_to_menu(mnu.total_defeat)
        #end
    #end
    if _g_encountered_party_template == pt.looters:
        set_background_mesh(mesh.pic_bandits)
    elif _g_encountered_party_template == pt.mountain_bandits:
        set_background_mesh(mesh.pic_mountain_bandits)
    elif _g_encountered_party_template == pt.steppe_bandits:
        set_background_mesh(mesh.pic_steppe_bandits)
    elif _g_encountered_party_template == pt.taiga_bandits:
        set_background_mesh(mesh.pic_steppe_bandits)
    elif _g_encountered_party_template == pt.sea_raiders:
        set_background_mesh(mesh.pic_sea_raiders)
    elif _g_encountered_party_template == pt.forest_bandits:
        set_background_mesh(mesh.pic_forest_bandits)
    elif _g_encountered_party_template == pt.deserters:
        set_background_mesh(mesh.pic_deserters)
    elif _g_encountered_party_template == pt.kingdom_hero_party:
        troop_id_010 = party_stack_get_troop_id(_g_encountered_party,0)
        if troop_id_010 >= 1:
            troop_slot_011 = troop_get_slot(troop_id_010,14)
            if troop_slot_011 == 15:
                set_background_mesh(mesh.pic_swad)
            elif troop_slot_011 == 16:
                set_background_mesh(mesh.pic_vaegir)
            elif troop_slot_011 == 17:
                set_background_mesh(mesh.pic_khergit)
            elif troop_slot_011 == 18:
                set_background_mesh(mesh.pic_nord)
            elif troop_slot_011 == 19:
                set_background_mesh(mesh.pic_rhodock)
            elif troop_slot_011 == 20:
                set_background_mesh(mesh.pic_sarranid_encounter)
            #end
        #end
    #end
simple_encounter.conditionBlock = condition

simple_encounter_encounter_attack = MenuOption("encounter_attack", "Charge the enemy.")
def code():
    _g_battle_result = 0
    _g_engaged_enemy = 1
    party_template_id_001 = party_get_template_id(_g_encountered_party)
    if party_template_id_001 == pt.village_farmers:
        unlock_achievement(27)
    #end
    calculate_renown_value()
    calculate_battle_advantage()
    set_battle_advantage(reg0)
    set_party_battle_mode()
    if _g_encounter_type == 1:
        _g_village_raid_evil = 0
        set_jump_mission(mt.village_raid)
        party_slot_002 = party_get_slot(_g_encounter_is_in_village,10)
        jump_to_scene(party_slot_002)
    elif _g_encounter_type == 2:
        _g_village_raid_evil = 0
        set_jump_mission(mt.village_raid)
        party_slot_002 = party_get_slot(_g_encounter_is_in_village,10)
        jump_to_scene(party_slot_002)
    else:
        set_jump_mission(mt.lead_charge)
        setup_random_scene()
    #end
    _g_next_menu = mnu.simple_encounter
    jump_to_menu(mnu.battle_debrief)
    change_screen_mission()
simple_encounter_encounter_attack.codeBlock = code

simple_encounter_encounter_order_attack = MenuOption("encounter_order_attack", "Order your troops to attack without you.")
def condition():
    if _encountered_party_friendly == 0:
        party_count_members_with_full_health(p.main_party)
simple_encounter_encounter_order_attack.conditionBlock = condition
def code():
    jump_to_menu(mnu.order_attack_begin)
simple_encounter_encounter_order_attack.codeBlock = code

simple_encounter_encounter_leave = MenuOption("encounter_leave", "Leave.")
def code():
    if _encountered_party_friendly == 0 and encountered_party_is_attacker():
        objectionable_action(1,gstr.flee_battle)
    #end
    if _encountered_party_friendly == 0:
        party_num_companions_stacks_001 = party_get_num_companion_stacks(p.encountered_party_backup)
        for stack_no_002 in range(0, party_num_companions_stacks_001):
            troop_id_003 = party_stack_get_troop_id(p.encountered_party_backup,stack_no_002)
            if is_between(troop_id_003,trp.npc1,trp.knight_1_1_wife) and troop_slot_eq(troop_id_003,2,2):
                troop_faction_004 = store_faction_of_troop(troop_id_003)
                add_log_entry(15,trp.player,-1,troop_id_003,troop_faction_004)
            #end
        #end
    #end
    leave_encounter()
    change_screen_return()
simple_encounter_encounter_leave.codeBlock = code

simple_encounter_encounter_retreat = MenuOption("encounter_retreat", "Pull back, leaving some soldiers behind to cover your retreat.")
def condition():
    if _cant_leave_encounter == 1:
        get_max_skill_of_player_party(skl.tactics)
        var001 = reg0
        var001 += 4
        party_count_members_with_full_health(p.collective_enemy,0)
        var002 = reg0
        var002 /= 2
        var002 /= var001
        val_max(var002,1)
        party_count_fit_regulars(p.main_party)
        var003 = reg0
simple_encounter_encounter_retreat.conditionBlock = condition
def code():
    jump_to_menu(mnu.encounter_retreat_confirm)
simple_encounter_encounter_retreat.codeBlock = code

simple_encounter_encounter_surrender = MenuOption("encounter_surrender", "Surrender.")
def code():
    _g_player_surrenders = 1
simple_encounter_encounter_surrender.codeBlock = code



encounter_retreat_confirm = GameMenu("encounter_retreat_confirm", 0,
"As the party member with the highest tactics skill, ({reg2}), {reg3?you devise:{s3} devises} a plan that will allow you and your men to escape with your lives, but you'll have to leave {reg4} soldiers behind to stop the enemy from giving chase."
)
def condition():
    get_max_skill_of_player_party(skl.tactics)
    var001 = reg0
    var002 = reg1
    reg2 = var001
    var001 += 4
    party_count_members_with_full_health(p.collective_enemy,0)
    var003 = reg0
    var003 /= 2
    reg4 = var003 / var001
    val_max(reg4,1)
    if var002 == trp.player:
        reg3 = 1
    else:
        reg3 = 0
        s3 = str_store_troop_name(var002)
    #end
encounter_retreat_confirm.conditionBlock = condition

encounter_retreat_confirm_leave_behind = MenuOption("leave_behind", "Go on. The sacrifice of these men will save the rest.")
def code():
    var001 = reg4
    for var002 in range(0, var001):
        if cf_party_remove_random_regular_troop(p.main_party):
            var003 = reg0
            random_x_004 = store_random_in_range(0,100)
            if random_x_004 >= 30:
                party_add_prisoners(_g_encountered_party,var003,1)
            #end
        #end
    #end
    change_player_party_morale(-20)
    jump_to_menu(mnu.encounter_retreat)
encounter_retreat_confirm_leave_behind.codeBlock = code

encounter_retreat_confirm_dont_leave_behind = MenuOption("dont_leave_behind", "No. We leave no one behind.")
def code():
    jump_to_menu(mnu.simple_encounter)
encounter_retreat_confirm_dont_leave_behind.codeBlock = code



encounter_retreat = GameMenu("encounter_retreat", 0,
"You tell {reg4} of your troops to hold the enemy while you retreat with the rest of your party."
)

encounter_retreat_continue = MenuOption("continue", "Continue...")
def code():
    objectionable_action(1,gstr.flee_battle)
    party_num_companions_stacks_001 = party_get_num_companion_stacks(p.encountered_party_backup)
    for stack_no_002 in range(0, party_num_companions_stacks_001):
        troop_id_003 = party_stack_get_troop_id(p.encountered_party_backup,stack_no_002)
        if is_between(troop_id_003,trp.npc1,trp.knight_1_1_wife) and troop_slot_eq(troop_id_003,2,2):
            troop_faction_004 = store_faction_of_troop(troop_id_003)
            add_log_entry(16,trp.player,-1,troop_id_003,troop_faction_004)
        #end
    #end
    party_ignore_player(_g_encountered_party,1)
    leave_encounter()
    change_screen_return()
encounter_retreat_continue.codeBlock = code



order_attack_begin = GameMenu("order_attack_begin", 0,
"Your troops prepare to attack the enemy."
)

order_attack_begin_order_attack_begin = MenuOption("order_attack_begin", "Order the attack to begin.")
def code():
    party_template_id_001 = party_get_template_id(_g_encountered_party)
    if party_template_id_001 == pt.village_farmers:
        unlock_achievement(27)
    #end
    _g_engaged_enemy = 1
    jump_to_menu(mnu.order_attack_2)
order_attack_begin_order_attack_begin.codeBlock = code

order_attack_begin_call_back = MenuOption("call_back", "Call them back.")
def code():
    jump_to_menu(mnu.simple_encounter)
order_attack_begin_call_back.codeBlock = code



order_attack_2 = GameMenu("order_attack_2", 512,
"{s4}^^Your casualties: {s8}^^Enemy casualties: {s9}"
)
def condition():
    set_background_mesh(mesh.pic_charge)
    party_calculate_strength(p.main_party,1)
    var001 = reg0
    party_calculate_strength(p.collective_enemy,0)
    var002 = reg0
    party_collect_attachments_to_party(p.main_party,p.collective_ally)
    party_calculate_strength(p.collective_ally,1)
    var003 = reg0
    if var003 <= var002:
        var004 = var003
    else:
        var004 = var002
    #end
    if var004 <= 25:
        var005 = 1
    elif var004 <= 50:
        var005 = 2
    elif var004 <= 75:
        var005 = 3
    elif var004 <= 125:
        var005 = 4
    elif var004 <= 200:
        var005 = 5
    elif var004 <= 400:
        var005 = 6
    elif var004 <= 800:
        var005 = 7
    elif var004 <= 1600:
        var005 = 8
    elif var004 <= 3200:
        var005 = 9
    elif var004 <= 6400:
        var005 = 10
    elif var004 <= 12800:
        var005 = 11
    elif var004 <= 25600:
        var005 = 12
    elif var004 <= 51200:
        var005 = 13
    elif var004 <= 102400:
        var005 = 14
    else:
        var005 = 15
    #end
    var001 /= var005
    val_max(var001,1)
    var002 /= var005
    val_max(var002,1)
    var003 /= var005
    val_max(var003,1)
    _g_strength_contribution_of_player = var001 * 100
    _g_strength_contribution_of_player /= var003
    inflict_casualties_to_party_group(p.main_party,var002,p.temp_casualties)
    print_casualties_to_s0(p.temp_casualties,0)
    s8 = str_store_string_reg(0)
    if _g_ally_party >= 0:
        inflict_casualties_to_party_group(_g_ally_party,var002,p.temp_casualties)
        s8 = str_store_string_reg(0)
    #end
    inflict_casualties_to_party_group(_g_encountered_party,var003,p.temp_casualties)
    party_num_companions_stacks_006 = party_get_num_companion_stacks(p.temp_casualties)
    for stack_no_007 in range(0, party_num_companions_stacks_006):
        troop_id_008 = party_stack_get_troop_id(p.temp_casualties,stack_no_007)
        if True:
            party_stack_size_009 = party_stack_get_size(p.temp_casualties,stack_no_007)
            if party_stack_size_009 > 0:
                party_add_members(p.total_enemy_casualties,troop_id_008,party_stack_size_009)
                party_stack_num_wounded_010 = party_stack_get_num_wounded(p.temp_casualties,stack_no_007)
                if party_stack_num_wounded_010 > 0:
                    party_wound_members(p.total_enemy_casualties,troop_id_008,party_stack_num_wounded_010)
                #end
            #end
        #end
    #end
    print_casualties_to_s0(p.temp_casualties,0)
    s9 = str_store_string_reg(0)
    party_collect_attachments_to_party(_g_encountered_party,p.collective_enemy)
    _no_soldiers_left = 0
    if True:
        party_count_members_with_full_health(p.main_party)
        var011 = reg0
        var012 = _num_routed_us + 1
        if var011 <= var012:
            _no_soldiers_left = 1
            s4 = str_store_string(gstr.order_attack_failure)
        else:
            party_count_members_with_full_health(p.collective_enemy)
            var013 = reg0
            if var013 > 0 or var013 <= _num_routed_enemies:
                var014 = 0
                party_num_companions_stacks_015 = party_get_num_companion_stacks(p.collective_enemy)
                if party_num_companions_stacks_015 == 0:
                    var014 = 1
                else:
                    troop_id_016 = party_stack_get_troop_id(p.collective_enemy,0)
                    if not troop_is_hero(troop_id_016):
                        var014 = 1
                    elif troop_is_wounded(troop_id_016):
                        var014 = 1
                    #end
                #end
            #end
        #end
        if var014 == 1:
            _g_battle_result = 1
            _no_soldiers_left = 1
            s4 = str_store_string(gstr.order_attack_success)
        else:
            s4 = str_store_string(gstr.order_attack_continue)
        #end
    #end
order_attack_2.conditionBlock = condition

order_attack_2_order_attack_continue = MenuOption("order_attack_continue", "Order your soldiers to continue the attack.")
def code():
    jump_to_menu(mnu.order_attack_2)
order_attack_2_order_attack_continue.codeBlock = code

order_attack_2_order_retreat = MenuOption("order_retreat", "Call your soldiers back.")
def code():
    jump_to_menu(mnu.simple_encounter)
order_attack_2_order_retreat.codeBlock = code

order_attack_2_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.simple_encounter)
order_attack_2_continue.codeBlock = code



battle_debrief = GameMenu("battle_debrief", 4608,
"{s11}^^Your Casualties:{s8}{s10}^^Enemy Casualties:{s9}"
)
def condition():
    if _g_battle_result == 1:
        change_troop_renown(trp.player,_battle_renown_value)
        if _g_encountered_party >= 0 and party_is_active(_g_encountered_party):
            party_template_id_001 = party_get_template_id(_g_encountered_party)
            if party_template_id_001 == pt.kingdom_caravan_party:
                var002 = get_achievement_stat(30,0)
                var003 = get_achievement_stat(30,1)
                var003 += 1
                set_achievement_stat(30,1,var003)
                if var002 >= 3 and var003 >= 3:
                    unlock_achievement(30)
                #end
            #end
        #end
        if True:
            party_cur_terrain_004 = party_get_current_terrain(p.main_party)
            if party_cur_terrain_004 == 4:
                var005 = get_achievement_stat(8,0)
                var005 += 1
                set_achievement_stat(8,0,var005)
                if var005 == 10:
                    unlock_achievement(8)
                #end
            #end
        #end
        if _g_enemy_party >= 0 and party_is_active(_g_enemy_party):
            troop_id_006 = party_stack_get_troop_id(_g_enemy_party,0)
            if troop_id_006 == trp.mountain_bandit:
                var007 = get_achievement_stat(13,0)
                var007 += 1
                set_achievement_stat(13,0,var007)
                if var007 == 10:
                    unlock_achievement(13)
                #end
            #end
        #end
        if is_between(_g_ally_party,p.town_1,p.village_1):
            unlock_achievement(1)
        #end
        if _g_joined_battle_to_help == 1:
            unlock_achievement(34)
        #end
    #end
    _g_joined_battle_to_help = 0
    count_casualties_and_adjust_morale()
    encounter_calculate_fit()
    party_count_fit_regulars(p.main_party)
    _playerparty_postbattle_regulars = reg0
    if _g_battle_result == 1 and _g_enemy_fit_for_battle == 0:
        s11 = str_store_string("@You were victorious!")
        if _g_friend_fit_for_battle > 1:
            set_background_mesh(mesh.pic_victory)
        #end
    elif _g_battle_result == -1 and _g_enemy_fit_for_battle >= 1 and _g_friend_fit_for_battle > 0 or _playerparty_postbattle_regulars <= 0:
        s11 = str_store_string("@Battle was lost. Your forces were utterly crushed.")
        set_background_mesh(mesh.pic_defeat)
    elif _g_battle_result == -1:
        s11 = str_store_string("@Your companions carry you away from the fighting.")
        troop_type_008 = troop_get_type(trp.player)
        if troop_type_008 == 1:
            set_background_mesh(mesh.pic_wounded_fem)
        else:
            set_background_mesh(mesh.pic_wounded)
        #end
    elif _g_battle_result == 1:
        s11 = str_store_string("@You have defeated the enemy.")
        if _g_friend_fit_for_battle > 1:
            set_background_mesh(mesh.pic_victory)
        #end
    elif _g_battle_result == 0:
        s11 = str_store_string("@You have retreated from the fight.")
    #end
    if _playerparty_prebattle_regulars > 9:
        var009 = 3 + _g_battle_result
        var010 = _playerparty_prebattle_regulars / var009
        if _playerparty_postbattle_regulars < var010:
            objectionable_action(2,gstr.excessive_casualties)
        #end
    #end
    print_casualties_to_s0(p.player_casualties,0)
    s8 = str_store_string_reg(0)
    print_casualties_to_s0(p.enemy_casualties,0)
    s9 = str_store_string_reg(0)
    str_clear(10)
    if _any_allies_at_the_last_battle == 1:
        print_casualties_to_s0(p.ally_casualties,0)
        s10 = str_store_string("@^^Ally Casualties:{s0}")
    #end
battle_debrief.conditionBlock = condition

battle_debrief_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(_g_next_menu)
battle_debrief_continue.codeBlock = code



total_victory = GameMenu("total_victory", 0,
"You shouldn't be reading this... {s9}"
)
def condition():
    var001 = 0
    if _routed_party_added == 0:
        _routed_party_added = 1
        add_routed_party()
    #end
    if check_quest_active(qst.track_down_bandits) and not check_quest_succeeded(qst.track_down_bandits) and not check_quest_failed(qst.track_down_bandits):
        quest_slot_002 = quest_get_slot(qst.track_down_bandits,8)
        if party_is_active(quest_slot_002):
            party_attached_003 = party_get_attached_to()
            if quest_slot_002 == _g_enemy_party or party_attached_003 == _g_enemy_party:
                succeed_quest(qst.track_down_bandits)
            #end
        #end
    #end
    if _g_private_battle_with_troop > 0 and troop_slot_eq(_g_private_battle_with_troop,10,_g_encountered_party):
        _g_private_battle_with_troop = 0
        _g_disable_condescending_comments = 1
    #end
    party_num_companions_stacks_004 = party_get_num_companion_stacks(p.collective_enemy)
    for stack_no_005 in range(0, party_num_companions_stacks_004):
        troop_id_006 = party_stack_get_troop_id(p.collective_enemy,stack_no_005)
        if is_between(troop_id_006,trp.knight_1_1,trp.kingdom_1_pretender) and troop_is_wounded(troop_id_006):
            party_add_members(p.total_enemy_casualties,troop_id_006,1)
        #end
    #end
    if _thanked_by_ally_leader == 0:
        _thanked_by_ally_leader = 1
        if _g_ally_party > 0:
            var007 = _g_starting_strength_friends + _g_starting_strength_enemy_party
            var007 -= _g_starting_strength_main_party
            var008 = _g_starting_strength_friends - _g_starting_strength_main_party
            var009 = var008 * 100
            var007 += 1
            var009 /= var007
            var010 = 100 - var009
            var011 = var010 * _g_starting_strength_enemy_party
            var011 /= 3000
            val_min(var011,4)
            _g_relation_boost = var010 * var010
            _g_relation_boost /= 700
            val_clamp(_g_relation_boost,0,20)
            party_num_companions_stacks_012 = party_get_num_companion_stacks(_g_ally_party)
            if party_num_companions_stacks_012 > 0:
                party_faction_013 = store_faction_of_party(_g_ally_party)
                change_player_relation_with_faction(party_faction_013,var011)
                troop_id_014 = party_stack_get_troop_id(_g_ally_party,0) # Johandros added 0
                party_stack_troop_dna_015 = party_stack_get_troop_dna(_g_ally_party,0)
                if troop_is_hero(troop_id_014):
                    troop_slot_016 = troop_get_slot(troop_id_014,22)
                    var017 = _g_relation_boost
                    if troop_slot_016 < -5:
                        var017 /= 3
                    #end
                #end
            #end
            change_player_relation_with_troop(troop_id_014,var017)
        #end
        _talk_context = 13
        setup_troop_meeting(troop_id_014,party_stack_troop_dna_015)
    else:
        var001 = 0
        party_num_companions_stacks_004 = party_get_num_companion_stacks(p.total_enemy_casualties)
        for stack_no_018 in range(_last_defeated_hero, party_num_companions_stacks_004):
            if var001 == 0:
                troop_id_006 = party_stack_get_troop_id(p.total_enemy_casualties,stack_no_018)
                party_stack_troop_dna_019 = party_stack_get_troop_dna(p.total_enemy_casualties,stack_no_018)
                if troop_is_hero(troop_id_006):
                    troop_faction_020 = store_faction_of_troop(troop_id_006)
                    if True:
                        faction_relation_021 = store_relation(troop_faction_020,fac.player_faction)
                        if faction_relation_021 >= 0:
                            s4 = str_store_troop_name(troop_id_006)
                            if _cheat_mode == 1:
                                print("@{!}{s4} skipped in p total enemy casualties capture queue because is friendly")
                            #end
                        #end
                    #end
                #end
            else:
                if True:
                    troop_id_022 = party_stack_get_troop_id(_g_encountered_party,0)
                    if is_between(troop_id_022,trp.npc1,trp.knight_1_1_wife) and troop_slot_eq(troop_id_022,2,2):
                        var023 = troop_id_022 - trp.npc1
                        var024 = get_achievement_stat(7,var023)
                        if var024 == 1:
                            unlock_achievement(7)
                        #end
                    #end
                #end
                _last_defeated_hero = stack_no_018 + 1
                remove_troop_from_prison(troop_id_006)
                troop_set_slot(troop_id_006,10,-1)
                if cf_check_hero_can_escape_from_player(troop_id_006):
                    s1 = str_store_troop_name(troop_id_006)
                    s3 = str_store_faction_name(troop_faction_020)
                    s17 = str_store_string("@{s1} of {s3} managed to escape.")
                    display_log_message("@{!}{s17}")
                    jump_to_menu(mnu.enemy_slipped_away)
                    var001 = 1
                else:
                    _last_defeated_hero = stack_no_018 + 1
                    remove_troop_from_prison(troop_id_006)
                    troop_set_slot(troop_id_006,10,-1)
                    _talk_context = 9
                    setup_troop_meeting(troop_id_006,party_stack_troop_dna_019)
                    var001 = 1
                #end
            #end
        #end
        if var001 == 1:
            pass
        else:
            var001 = 0
            party_num_prisoners_stacks_025 = party_get_num_prisoner_stacks(p.collective_enemy)
            for stack_no_018 in range(_last_freed_hero, party_num_prisoners_stacks_025):
                if var001 == 0:
                    troop_id_006 = party_prisoner_stack_get_troop_id(p.collective_enemy,stack_no_018)
                    if troop_is_hero(troop_id_006):
                        party_stack_troop_dna_019 = party_prisoner_stack_get_troop_dna(p.collective_enemy,stack_no_018)
                        _last_freed_hero = stack_no_018 + 1
                        _talk_context = 8
                        setup_troop_meeting(troop_id_006,party_stack_troop_dna_019)
                        var001 = 1
                    #end
                #end
            #end
        #end
        if var001 == 1:
            pass
        elif _capture_screen_shown == 0:
            _capture_screen_shown = 1
            party_clear(p.temp_party)
            _g_move_heroes = 0
            party_add_wounded_members_as_prisoners(p.temp_party,p.total_enemy_casualties)
            party_add_party_prisoners(p.temp_party,p.collective_enemy)
            if True:
                party_calculate_strength(p.collective_friends_backup,0)
                var026 = reg0
                if var026 > 0:
                    party_calculate_strength(p.main_party_backup,0)
                    var027 = reg0
                    var028 = var026 - var027
                    var029 = var028 * 1000
                    var029 /= var026
                    _pin_number = var029
                    party_clear(p.temp_party_2)
                    move_members_with_ratio(p.temp_party,p.temp_party_2)
                    if _g_ally_party > 0:
                        distribute_party_among_party_group(p.temp_party_2,_g_ally_party)
                    #end
                #end
            #end
        #end
        party_num_companions_030 = party_get_num_companions(p.temp_party)
        party_num_prisioners_031 = party_get_num_prisoners(p.temp_party)
        var032 = party_num_companions_030 + party_num_prisioners_031
        if var032 > 0:
            change_screen_exchange_with_party(p.temp_party)
        elif _loot_screen_shown == 0:
            _loot_screen_shown = 1
            troop_clear_inventory(trp.temp_troop)
            party_calculate_loot(p.total_enemy_casualties)
            if reg0 > 0:
                troop_sort_inventory(trp.temp_troop)
                change_screen_loot(trp.temp_troop)
            else:
                if _g_ally_party <= 0:
                    end_current_battle()
                #end
            #end
        #end
        party_give_xp_and_gold(p.total_enemy_casualties)
        if _g_enemy_party == 0:
            print(gstr.error_string)
        #end
        if party_is_active(_g_ally_party):
            battle_political_consequences(_g_enemy_party,_g_ally_party)
        else:
            battle_political_consequences(_g_enemy_party,p.main_party)
        #end
        event_player_defeated_enemy_party(_g_enemy_party)
        clear_party_group(_g_enemy_party)
        if _g_next_menu == -1:
            post_battle_personality_clash_check()
            troop_id_033 = party_stack_get_troop_id(p.encountered_party_backup,0)
            if is_between(troop_id_033,trp.npc1,trp.knight_1_1_wife) and not is_between(_g_encountered_party,p.town_1,p.salt_mine):
                troop_faction_034 = store_faction_of_troop(troop_id_033)
                if _g_ally_party == 0:
                    add_log_entry(11,trp.player,-1,troop_id_033,troop_faction_034)
                    if _cheat_mode == 1:
                        print("@{!}Victory comment. Player was alone")
                    #end
                elif _g_strength_contribution_of_player >= 40:
                    add_log_entry(11,trp.player,-1,troop_id_033,troop_faction_034)
                    if _cheat_mode == 1:
                        print("@{!}Ordinary victory comment. The player provided at least 40 percent forces.")
                    #end
                elif _g_starting_strength_enemy_party > 1000:
                    get_closest_center(p.main_party)
                    var035 = reg0
                    add_log_entry(19,trp.player,var035,-1,troop_faction_034)
                    if _cheat_mode == 1:
                        print("@{!}Player participation comment. The enemy had at least 1k starting strength.")
                    #end
                elif _cheat_mode == 1:
                    print("@{!}No victory comment. The battle was small;;; and the player provided less than 40 percent of allied strength")
                #end
            #end
            _g_total_victories += 1
            leave_encounter()
            change_screen_return()
        else:
            if _g_next_menu == mnu.castle_taken:
                add_log_entry(10,trp.player,_g_encountered_party,-1,_g_encountered_x_party_faction)
                cur_hours_036 = store_current_hours()
                faction_set_slot(_players_kingdom,98,cur_hours_036)
                if is_between(_players_kingdom,fac.kingdom_1,fac.kingdoms_end):
                    jump_to_menu(_g_next_menu)
                elif _players_kingdom == fac.player_supporters_faction:
                    _g_center_taken_by_player_faction = _g_encountered_party
                    if not faction_slot_eq(fac.player_supporters_faction,11,trp.player):
                        faction_slot_037 = faction_get_slot(fac.player_supporters_faction,11)
                        change_screen_return()
                        start_map_conversation(faction_slot_037,-1)
                    elif not is_between(_players_kingdom,fac.kingdom_1,fac.kingdoms_end):
                        _g_center_taken_by_player_faction = _g_encountered_party
                        _talk_context = 20
                        change_screen_return()
                        var038 = trp.swadian_sharpshooter
                        var039 = 0
                        party_num_companions_stacks_004 = party_get_num_companion_stacks(p.main_party)
                        for stack_no_018 in range(0, party_num_companions_stacks_004):
                            troop_id_006 = party_stack_get_troop_id(p.main_party,stack_no_018)
                            if troop_id_006 != trp.player:
                                party_stack_size_040 = party_stack_get_size(p.main_party,stack_no_018)
                                party_stack_num_wounded_041 = party_stack_get_num_wounded(p.main_party,stack_no_018)
                                troop_slot_042 = troop_get_slot(p.main_party,146)
                                var043 = 0
                                if not troop_is_hero(troop_id_006):
                                    var044 = party_stack_num_wounded_041 + troop_slot_042
                                    if party_stack_size_040 > var044:
                                        var043 = 1
                                    elif troop_is_hero(troop_id_006) and not troop_is_wounded(troop_id_006):
                                        var043 = 1
                                    #end
                                #end
                            #end
                        #end
                        if var043 == 1:
                            if troop_is_hero(troop_id_006):
                                troop_slot_045 = troop_get_slot(troop_id_006,7)
                                var046 = troop_slot_045 * 100
                                var046 += 1000
                            else:
                                character_lvl_047 = store_character_level(troop_id_006)
                                var046 = character_lvl_047
                            #end
                        #end
                        if var046 > var039:
                            var039 = var046
                            var038 = troop_id_006
                            party_stack_troop_dna_048 = party_stack_get_troop_dna(p.main_party,stack_no_018)
                        #end
                    #end
                    start_map_conversation(var038,party_stack_troop_dna_048)
                #end
            #end
        #end
    #end
total_victory.conditionBlock = condition

total_victory_continue = MenuOption("continue", "Continue...")



enemy_slipped_away = GameMenu("enemy_slipped_away", 0,
"{s17}"
)

enemy_slipped_away_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.total_victory)
enemy_slipped_away_continue.codeBlock = code



total_defeat = GameMenu("total_defeat", 0,
"{!}You shouldn't be reading this..."
)
def condition():
    play_track(track.capture,1)
    party_num_prisoners_stacks_001 = party_get_num_prisoner_stacks(p.main_party)
    for stack_no_002 in range(0, party_num_prisoners_stacks_001):
        party_prisoner_troop_id_003 = party_prisoner_stack_get_troop_id(p.main_party,stack_no_002)
        if troop_is_hero(party_prisoner_troop_id_003):
            remove_troop_from_prison(party_prisoner_troop_id_003)
        #end
    #end
    if party_is_active(_g_ally_party):
        battle_political_consequences(_g_ally_party,_g_enemy_party)
    else:
        battle_political_consequences(p.main_party,_g_enemy_party)
    #end
    loot_player_items(_g_enemy_party)
    _g_move_heroes = 0
    party_clear(p.temp_party)
    party_add_party_prisoners(p.temp_party,p.main_party)
    party_prisoners_add_party_companions(p.temp_party,p.main_party)
    distribute_party_among_party_group(p.temp_party,_g_enemy_party)
    _g_prison_heroes = 1
    party_remove_all_companions(p.main_party)
    _g_prison_heroes = 0
    _g_move_heroes = 1
    party_remove_all_prisoners(p.main_party)
    _g_total_defeats += 1
    if _g_player_surrenders != 1:
        random_x_004 = store_random_in_range(0,100)
        if random_x_004 >= _g_player_luck:
            jump_to_menu(mnu.permanent_damage)
        else:
            if _g_next_menu == -1:
                leave_encounter()
                change_screen_return()
            else:
                jump_to_menu(_g_next_menu)
            #end
        #end
    #end
    if _g_ally_party > 0:
        party_wound_all_members(_g_ally_party)
    #end
    party_num_companions_stacks_005 = party_get_num_companion_stacks(p.encountered_party_backup)
    for stack_no_002 in range(0, party_num_companions_stacks_005):
        party_prisoner_troop_id_003 = party_stack_get_troop_id(p.encountered_party_backup,stack_no_002)
        if is_between(party_prisoner_troop_id_003,trp.npc1,trp.knight_1_1_wife) and troop_slot_eq(party_prisoner_troop_id_003,2,2):
            troop_faction_006 = store_faction_of_troop(party_prisoner_troop_id_003)
            add_log_entry(14,trp.player,-1,party_prisoner_troop_id_003,troop_faction_006)
        #end
    #end
total_defeat.conditionBlock = condition



permanent_damage = GameMenu("permanent_damage", 512,
"{s0}"
)
def condition():
    var001 = 1
    for var002 in range(0, var001):
        random_x_003 = store_random_in_range(0,4)
        attribute_lvl_004 = store_attribute_level(trp.player,random_x_003)
        if attribute_lvl_004 > 3 and random_x_003 != 3:
            if random_x_003 == 0:
                s0 = str_store_string("@Some of your tendons have been damaged in the battle. You lose 1 strength.")
            elif random_x_003 == 1:
                s0 = str_store_string("@You took a nasty wound which will cause you to limp slightly even after it heals. You lose 1 agility.")
            else:
                s0 = str_store_string("@You have trouble thinking straight after the battle;;; perhaps from a particularly hard hit to your head;;; and frequent headaches now plague your existence. Your intelligence is reduced by 1.")
            #end
        elif var001 < 200:
            var001 += 1
        #end
    #end
    if var001 == 200:
        if _g_next_menu == -1:
            leave_encounter()
            change_screen_return()
        else:
            jump_to_menu(_g_next_menu)
        #end
    else:
        troop_raise_attribute(trp.player,random_x_003,-1)
    #end
permanent_damage.conditionBlock = condition

permanent_damage_s0 = MenuOption("s0", "{s0}")
def condition():
    random_x_001 = store_random_in_range(0,4)
    if random_x_001 == 0:
        s0 = str_store_string("@Perhaps I'm getting unlucky...")
    elif random_x_001 == 1:
        s0 = str_store_string("@Retirement is starting to sound better and better.")
    elif random_x_001 == 2:
        s0 = str_store_string("@No matter! I will persevere!")
    elif random_x_001 == 3:
        troop_type_002 = troop_get_type(trp.player)
        if troop_type_002 == 1:
            s0 = str_store_string("@What did I do to deserve this?")
        else:
            s0 = str_store_string("@I suppose it'll make for a good story;;; at least...")
        #end
    #end
permanent_damage_s0.conditionBlock = condition
def code():
    if _g_next_menu == -1:
        leave_encounter()
        change_screen_return()
    else:
        jump_to_menu(_g_next_menu)
    #end
permanent_damage_s0.codeBlock = code



pre_join = GameMenu("pre_join", 0,
"You come across a battle between {s2} and {s1}. You decide to..."
)
def condition():
    s1 = str_store_party_name(_g_encountered_party)
    s2 = str_store_party_name(_g_encountered_party_2)
pre_join.conditionBlock = condition

pre_join_pre_join_help_attackers = MenuOption("pre_join_help_attackers", "Move in to help the {s2}.")
def condition():
    party_faction_001 = store_faction_of_party(_g_encountered_party_2)
    faction_relation_002 = store_relation(party_faction_001,fac.player_supporters_faction)
    party_faction_003 = store_faction_of_party(_g_encountered_party)
    faction_relation_004 = store_relation(party_faction_003,fac.player_supporters_faction)
pre_join_pre_join_help_attackers.conditionBlock = condition
def code():
    select_enemy(0)
    _g_enemy_party = _g_encountered_party
    _g_ally_party = _g_encountered_party_2
    jump_to_menu(mnu.join_battle)
pre_join_pre_join_help_attackers.codeBlock = code

pre_join_pre_join_help_defenders = MenuOption("pre_join_help_defenders", "Rush to the aid of the {s1}.")
def condition():
    party_faction_001 = store_faction_of_party(_g_encountered_party_2)
    faction_relation_002 = store_relation(party_faction_001,fac.player_supporters_faction)
    party_faction_003 = store_faction_of_party(_g_encountered_party)
    faction_relation_004 = store_relation(party_faction_003,fac.player_supporters_faction)
pre_join_pre_join_help_defenders.conditionBlock = condition
def code():
    select_enemy(1)
    _g_enemy_party = _g_encountered_party_2
    _g_ally_party = _g_encountered_party
    jump_to_menu(mnu.join_battle)
pre_join_pre_join_help_defenders.codeBlock = code

pre_join_pre_join_leave = MenuOption("pre_join_leave", "Don't get involved.")
def code():
    leave_encounter()
    change_screen_return()
pre_join_pre_join_leave.codeBlock = code



join_battle = GameMenu("join_battle", 0,
"You are helping the {s2} against the {s1}. You have {reg10} troops fit for battle against the enemy's {reg11}."
)
def condition():
    s1 = str_store_party_name(_g_enemy_party)
    s2 = str_store_party_name(_g_ally_party)
    encounter_calculate_fit()
    if _new_encounter == 1:
        _new_encounter = 0
        encounter_init_variables()
    elif _g_leave_encounter == 1:
        change_screen_return()
    #end
    if True:
        party_count_members_with_full_health(p.collective_enemy)
        var001 = reg0
        var002 = 0
        if _g_battle_result == 1 and var001 > 0 or var001 <= _num_routed_enemies:
            var002 = 1
        elif _g_engaged_enemy == 1 and _g_enemy_fit_for_battle <= 0 and _g_friend_fit_for_battle >= 1:
            var002 = 1
        #end
        if var002 == 1 or _g_enemy_surrenders == 1:
            _g_next_menu = -1
            jump_to_menu(mnu.total_victory)
        else:
            party_count_members_with_full_health(p.collective_friends)
            var003 = reg0
            var004 = 0
            if _g_battle_result == -1 and var003 <= _num_routed_allies:
                var004 = 1
            #end
        #end
        if var004 == 1 or _g_player_surrenders == 1:
            leave_encounter()
            change_screen_return()
        #end
    #end
join_battle.conditionBlock = condition

join_battle_join_attack = MenuOption("join_attack", "Charge the enemy.")
def code():
    _g_joined_battle_to_help = 1
    party_set_next_battle_simulation_time(_g_encountered_party,-1)
    _g_battle_result = 0
    calculate_renown_value()
    calculate_battle_advantage()
    set_battle_advantage(reg0)
    set_party_battle_mode()
    set_jump_mission(mt.lead_charge)
    setup_random_scene()
    _g_next_menu = mnu.join_battle
    jump_to_menu(mnu.battle_debrief)
    change_screen_mission()
join_battle_join_attack.codeBlock = code

join_battle_join_order_attack = MenuOption("join_order_attack", "Order your troops to attack with your allies while you stay back.")
def condition():
    party_count_members_with_full_health(p.main_party)
join_battle_join_order_attack.conditionBlock = condition
def code():
    _g_joined_battle_to_help = 1
    party_set_next_battle_simulation_time(_g_encountered_party,-1)
    jump_to_menu(mnu.join_order_attack)
join_battle_join_order_attack.codeBlock = code

join_battle_join_leave = MenuOption("join_leave", "Leave.")
def code():
    if not troop_is_wounded(trp.player):
        objectionable_action(1,gstr.flee_battle)
        troop_id_001 = party_stack_get_troop_id(_g_enemy_party,0)
        if is_between(troop_id_001,trp.npc1,trp.knight_1_1_wife):
            add_log_entry(15,trp.player,-1,troop_id_001,-1)
        #end
    #end
    leave_encounter()
    change_screen_return()
join_battle_join_leave.codeBlock = code



join_order_attack = GameMenu("join_order_attack", 512,
"{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}"
)
def condition():
    party_calculate_strength(p.main_party,1)
    var001 = reg0
    var001 /= 5
    party_calculate_strength(p.collective_friends,0)
    var002 = reg0
    var002 /= 5
    party_calculate_strength(p.collective_enemy,0)
    var003 = reg0
    var003 /= 5
    if var002 == 0:
        var004 = var003 / 2
    else:
        var004 = var003
        var004 *= var001
        var004 /= var002
    #end
    var003 -= var004
    inflict_casualties_to_party_group(p.main_party,var004,p.temp_casualties)
    print_casualties_to_s0(p.temp_casualties,0)
    s8 = str_store_string_reg(0)
    inflict_casualties_to_party_group(_g_enemy_party,var002,p.temp_casualties)
    party_num_companions_stacks_005 = party_get_num_companion_stacks(p.temp_casualties)
    for stack_no_006 in range(0, party_num_companions_stacks_005):
        troop_id_007 = party_stack_get_troop_id(p.temp_casualties,stack_no_006)
        if True:
            party_stack_size_008 = party_stack_get_size(p.temp_casualties,stack_no_006)
            if party_stack_size_008 > 0:
                party_add_members(p.total_enemy_casualties,troop_id_007,party_stack_size_008)
                party_stack_num_wounded_009 = party_stack_get_num_wounded(p.temp_casualties,stack_no_006)
                if party_stack_num_wounded_009 > 0:
                    party_wound_members(p.total_enemy_casualties,troop_id_007,party_stack_num_wounded_009)
                #end
            #end
        #end
    #end
    print_casualties_to_s0(p.temp_casualties,0)
    s10 = str_store_string_reg(0)
    collect_friendly_parties()
    inflict_casualties_to_party_group(_g_ally_party,var003,p.temp_casualties)
    print_casualties_to_s0(p.temp_casualties,0)
    s9 = str_store_string_reg(0)
    party_collect_attachments_to_party(_g_enemy_party,p.collective_enemy)
    _no_soldiers_left = 0
    if True:
        party_count_members_with_full_health(p.main_party)
        var010 = reg0
        if var010 <= _num_routed_us:
            _no_soldiers_left = 1
            s4 = str_store_string(gstr.join_order_attack_failure)
        else:
            party_count_members_with_full_health(p.collective_enemy)
            var011 = reg0
            if var011 > 0 or var011 <= _num_routed_enemies:
                _g_battle_result = 1
                _no_soldiers_left = 1
                s4 = str_store_string(gstr.join_order_attack_success)
            else:
                s4 = str_store_string(gstr.join_order_attack_continue)
            #end
        #end
    #end
join_order_attack.conditionBlock = condition

join_order_attack_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.join_battle)
join_order_attack_continue.codeBlock = code



zendar = GameMenu("zendar", 16,
"You enter the town of Zendar."
)
def condition():
    reset_price_rates(0)
    set_price_rate_for_item(itm.tools,70)
    set_price_rate_for_item(itm.salt,140)
zendar.conditionBlock = condition

zendar_zendar_enter = MenuOption("zendar_enter", " ") # Door to the town center.
def code():
    set_jump_mission(mt.town_default)
    jump_to_scene(scn.zendar_center)
    change_screen_mission()
zendar_zendar_enter.codeBlock = code

zendar_zendar_tavern = MenuOption("zendar_tavern", " ") # Door to the tavern.
def code():
    set_jump_mission(mt.town_default)
    jump_to_scene(scn.the_happy_boar)
    change_screen_mission()
zendar_zendar_tavern.codeBlock = code

zendar_zendar_merchant = MenuOption("zendar_merchant", " ") # Door to the merchant.
def code():
    set_jump_mission(mt.town_default)
    jump_to_scene(scn.zendar_merchant)
    change_screen_mission()
zendar_zendar_merchant.codeBlock = code

zendar_zendar_arena = MenuOption("zendar_arena", " ") # Door to the arena.
def code():
    set_jump_mission(mt.town_default)
    jump_to_scene(scn.zendar_arena)
    change_screen_mission()
zendar_zendar_arena.codeBlock = code

zendar_town_1_leave = MenuOption("town_1_leave", " ")
def code():
    leave_encounter()
    change_screen_return()
zendar_town_1_leave.codeBlock = code



salt_mine = GameMenu("salt_mine", 16,
"You enter the salt mine."
)
def condition():
    reset_price_rates(0)
    set_price_rate_for_item(itm.salt,55)
salt_mine.conditionBlock = condition

salt_mine_enter = MenuOption("enter", "Enter.")
def code():
    set_jump_mission(mt.town_center)
    jump_to_scene(scn.salt_mine)
    change_screen_mission()
salt_mine_enter.codeBlock = code

salt_mine_leave = MenuOption("leave", "Leave.")
def code():
    leave_encounter()
    change_screen_return()
salt_mine_leave.codeBlock = code



four_ways_inn = GameMenu("four_ways_inn", 16,
"You arrive at the Four Ways Inn."
)

four_ways_inn_enter = MenuOption("enter", "Enter.")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.four_ways_inn)
    change_screen_mission()
four_ways_inn_enter.codeBlock = code

four_ways_inn_leave = MenuOption("leave", "Leave.")
def code():
    leave_encounter()
    change_screen_return()
four_ways_inn_leave.codeBlock = code



test_scene = GameMenu("test_scene", 0,
"You enter the test scene."
)

test_scene_enter = MenuOption("enter", "Enter 1.")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.multi_scene_1)
    change_screen_mission()
test_scene_enter.codeBlock = code

test_scene_enter = MenuOption("enter", "Enter 2.")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.multi_scene_2)
    change_screen_mission()
test_scene_enter.codeBlock = code

test_scene_enter = MenuOption("enter", "Enter 3.")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.multi_scene_3)
    change_screen_mission()
test_scene_enter.codeBlock = code

test_scene_enter = MenuOption("enter", "Enter 4.")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.multi_scene_4)
    change_screen_mission()
test_scene_enter.codeBlock = code

test_scene_enter = MenuOption("enter", "Enter 5.")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.multi_scene_5)
    change_screen_mission()
test_scene_enter.codeBlock = code

test_scene_enter = MenuOption("enter", "Enter 6.")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.multi_scene_6)
    change_screen_mission()
test_scene_enter.codeBlock = code

test_scene_enter = MenuOption("enter", "Enter 7.")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.test2)
    change_screen_mission()
test_scene_enter.codeBlock = code

test_scene_enter = MenuOption("enter", "Enter 8.")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.test3)
    change_screen_mission()
test_scene_enter.codeBlock = code

test_scene_enter = MenuOption("enter", "Enter 9.")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.multi_scene_13)
    change_screen_mission()
test_scene_enter.codeBlock = code

test_scene_leave = MenuOption("leave", "Leave.")
def code():
    leave_encounter()
    change_screen_return()
test_scene_leave.codeBlock = code



battlefields = GameMenu("battlefields", 0,
"{!}Select a field..."
)

battlefields_enter_f1 = MenuOption("enter_f1", "{!}Field 1")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.field_1)
    change_screen_mission()
battlefields_enter_f1.codeBlock = code

battlefields_enter_f2 = MenuOption("enter_f2", "{!}Field 2")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.field_2)
    change_screen_mission()
battlefields_enter_f2.codeBlock = code

battlefields_enter_f3 = MenuOption("enter_f3", "{!}Field 3")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.field_3)
    change_screen_mission()
battlefields_enter_f3.codeBlock = code

battlefields_enter_f4 = MenuOption("enter_f4", "{!}Field 4")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.field_4)
    change_screen_mission()
battlefields_enter_f4.codeBlock = code

battlefields_enter_f5 = MenuOption("enter_f5", "{!}Field 5")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(scn.field_5)
    change_screen_mission()
battlefields_enter_f5.codeBlock = code

battlefields_leave = MenuOption("leave", "Leave.")
def code():
    leave_encounter()
    change_screen_return()
battlefields_leave.codeBlock = code



dhorak_keep = GameMenu("dhorak_keep", 0,
"You enter the Dhorak Keep"
)

dhorak_keep_enter = MenuOption("enter", "Enter.")
def code():
    set_jump_mission(mt.town_center)
    jump_to_scene(scn.dhorak_keep)
    change_screen_mission()
dhorak_keep_enter.codeBlock = code

dhorak_keep_leave = MenuOption("leave", "Leave.")
def code():
    leave_encounter()
    change_screen_return()
dhorak_keep_leave.codeBlock = code



join_siege_outside = GameMenu("join_siege_outside", 4096,
"{s1} has come under siege by {s2}."
)
def condition():
    s1 = str_store_party_name(_g_encountered_party)
    s2 = str_store_party_name(_g_encountered_party_2)
    troop_type_001 = troop_get_type(trp.player)
    if troop_type_001 == 1:
        set_background_mesh(mesh.pic_siege_sighted_fem)
    else:
        set_background_mesh(mesh.pic_siege_sighted)
    #end
join_siege_outside.conditionBlock = condition

join_siege_outside_approach_besiegers = MenuOption("approach_besiegers", "Approach the siege camp.")
def condition():
    party_faction_001 = store_faction_of_party(_g_encountered_party_2)
    faction_relation_002 = store_relation(party_faction_001,fac.player_supporters_faction)
    if faction_relation_002 >= 0:
        party_faction_001 = store_faction_of_party(_g_encountered_party)
        faction_relation_002 = store_relation(party_faction_001,fac.player_supporters_faction)
join_siege_outside_approach_besiegers.conditionBlock = condition
def code():
    jump_to_menu(mnu.besiegers_camp_with_allies)
join_siege_outside_approach_besiegers.codeBlock = code

join_siege_outside_pass_through_siege = MenuOption("pass_through_siege", "Pass through the siege lines and enter {s1}.")
def condition():
    party_faction_001 = store_faction_of_party(_g_encountered_party)
    faction_relation_002 = store_relation(party_faction_001,fac.player_supporters_faction)
join_siege_outside_pass_through_siege.conditionBlock = condition
def code():
    jump_to_menu(mnu.cut_siege_without_fight)
join_siege_outside_pass_through_siege.codeBlock = code

join_siege_outside_leave = MenuOption("leave", "Leave.")
def code():
    leave_encounter()
    change_screen_return()
join_siege_outside_leave.codeBlock = code



cut_siege_without_fight = GameMenu("cut_siege_without_fight", 0,
"The besiegers let you approach the gates without challenge."
)

cut_siege_without_fight_continue = MenuOption("continue", "Continue...")
def code():
    _g_encountered_x_party_faction_list1 = [
    _players_kingdom,
    fac.player_supporters_faction,
    ]
    if _g_encountered_x_party_faction in _g_encountered_x_party_faction_list1:
        jump_to_menu(mnu.town)
    else:
        jump_to_menu(mnu.castle_outside)
    #end
cut_siege_without_fight_continue.codeBlock = code



besiegers_camp_with_allies = GameMenu("besiegers_camp_with_allies", 0,
"{s1} remains under siege. The banners of {s2} fly above the camp of the besiegers, where you and your men are welcomed."
)
def condition():
    s1 = str_store_party_name(_g_encountered_party)
    s2 = str_store_party_name(_g_encountered_party_2)
    _g_enemy_party = _g_encountered_party
    _g_ally_party = _g_encountered_party_2
    select_enemy(0)
    encounter_calculate_fit()
    if _new_encounter == 1:
        _new_encounter = 0
        encounter_init_variables()
    #end
    if _g_leave_encounter == 1:
        change_screen_return()
    else:
        var001 = 0
        if _g_battle_result == 1:
            var001 = 1
        elif _g_enemy_fit_for_battle <= 0 and _g_friend_fit_for_battle >= 1:
            var001 = 1
        #end
        if var001 == 1 or _g_enemy_surrenders == 1:
            party_wound_all_members(_g_enemy_party)
            leave_encounter()
            change_screen_return()
        else:
            party_count_members_with_full_health(p.collective_friends)
            var002 = reg0
            if _g_battle_result == -1 and var002 == 0:
                leave_encounter()
                change_screen_return()
            #end
        #end
    #end
besiegers_camp_with_allies.conditionBlock = condition

besiegers_camp_with_allies_talk_to_siege_commander = MenuOption("talk_to_siege_commander", "Request a meeting with the commander.")
def code():
    get_meeting_scene()
    scene_id_001 = reg0
    modify_visitors_at_site(scene_id_001)
    reset_visitors()
    set_visitor(0,trp.player)
    troop_id_002 = party_stack_get_troop_id(_g_encountered_party_2,0)
    party_stack_troop_dna_003 = party_stack_get_troop_dna(_g_encountered_party_2,0)
    set_visitor(17,troop_id_002,party_stack_troop_dna_003)
    set_jump_mission(mt.conversation_encounter)
    jump_to_scene(scene_id_001)
    _talk_context = 4
    change_screen_map_conversation(troop_id_002)
besiegers_camp_with_allies_talk_to_siege_commander.codeBlock = code

besiegers_camp_with_allies_join_siege_with_allies = MenuOption("join_siege_with_allies", "Join the next assault.")
def code():
    _g_joined_battle_to_help = 1
    party_set_next_battle_simulation_time(_g_encountered_party,-1)
    if check_quest_active(qst.join_siege_with_army) and quest_slot_eq(qst.join_siege_with_army,1,_g_encountered_party):
        add_xp_as_reward(250)
        end_quest(qst.join_siege_with_army)
        faction_slot_001 = faction_get_slot(_players_kingdom,8)
        s9 = str_store_troop_name_link(faction_slot_001)
        setup_quest_text(qst.follow_army)
        s2 = str_store_string("@{s9} wants you to follow his army until further notice.")
        start_quest(qst.follow_army,faction_slot_001)
        _g_player_follow_army_warnings = 0
    #end
    if party_slot_eq(_g_encountered_party,0,3):
        party_slot_002 = party_get_slot(_g_encountered_party,18)
    else:
        party_slot_002 = party_get_slot(_g_encountered_party,10)
    #end
    calculate_battle_advantage()
    reg0 *= 2
    reg0 /= 3
    set_battle_advantage(reg0)
    set_party_battle_mode()
    if party_slot_eq(_g_encountered_party,27,1):
        set_jump_mission(mt.castle_attack_walls_belfry)
    else:
        set_jump_mission(mt.castle_attack_walls_ladder)
    #end
    jump_to_scene(party_slot_002)
    _g_siege_final_menu = mnu.besiegers_camp_with_allies
    _g_siege_battle_state = 1
    _g_next_menu = mnu.castle_besiege_inner_battle
    jump_to_menu(mnu.battle_debrief)
    change_screen_mission()
besiegers_camp_with_allies_join_siege_with_allies.codeBlock = code

besiegers_camp_with_allies_join_siege_stay_back = MenuOption("join_siege_stay_back", "Order your soldiers to join the next assault without you.")
def condition():
    party_count_members_with_full_health(p.main_party)
besiegers_camp_with_allies_join_siege_stay_back.conditionBlock = condition
def code():
    _g_joined_battle_to_help = 1
    party_set_next_battle_simulation_time(_g_encountered_party,-1)
    if check_quest_active(qst.join_siege_with_army) and quest_slot_eq(qst.join_siege_with_army,1,_g_encountered_party):
        add_xp_as_reward(100)
        end_quest(qst.join_siege_with_army)
        faction_slot_001 = faction_get_slot(_players_kingdom,8)
        s9 = str_store_troop_name_link(faction_slot_001)
        setup_quest_text(qst.follow_army)
        s2 = str_store_string("@{s9} wants you to follow his army until further notice.")
        start_quest(qst.follow_army,faction_slot_001)
        _g_player_follow_army_warnings = 0
    #end
    jump_to_menu(mnu.castle_attack_walls_with_allies_simulate)
besiegers_camp_with_allies_join_siege_stay_back.codeBlock = code

besiegers_camp_with_allies_leave = MenuOption("leave", "Leave.")
def code():
    leave_encounter()
    change_screen_return()
besiegers_camp_with_allies_leave.codeBlock = code



castle_outside = GameMenu("castle_outside", 4096,
"You are outside {s2}.{s11} {s3} {s4}"
)
def condition():
    _g_enemy_party = _g_encountered_party
    _g_ally_party = -1
    s2 = str_store_party_name(_g_encountered_party)
    encounter_calculate_fit()
    _all_doors_locked = 1
    _current_town = _g_encountered_party
    if _new_encounter == 1:
        _new_encounter = 0
        let_nearby_parties_join_current_battle(1,0)
        encounter_init_variables()
        _entry_to_town_forbidden = 0
        _sneaked_into_town = 0
        _town_entered = 0
        _encountered_party_hostile = 0
        _encountered_party_friendly = 0
        if _g_player_besiege_town > 0 and _g_player_besiege_town != _g_encountered_party and party_slot_eq(_g_player_besiege_town,54,p.main_party):
            lift_siege(_g_player_besiege_town,0)
            _g_player_besiege_town = -1
        #end
        if _g_encountered_party_relation < 0:
            _encountered_party_hostile = 1
            _entry_to_town_forbidden = 1
        #end
        _cant_sneak_into_town = 0
        if _current_town == _last_sneak_attempt_town:
            reg2 = store_current_hours()
            reg2 -= _last_sneak_attempt_time
            if reg2 < 12:
                _cant_sneak_into_town = 1
            #end
        #end
    elif _g_leave_encounter == 1:
        change_screen_return()
    #end
    str_clear(4)
    if _entry_to_town_forbidden == 1:
        if _cant_sneak_into_town == 1:
            s4 = str_store_string(gstr.sneaking_to_town_impossible)
        else:
            s4 = str_store_string(gstr.entrance_to_town_forbidden)
        #end
    #end
    party_slot_001 = party_get_slot(_current_town,7)
    party_faction_002 = store_faction_of_party(_current_town)
    s9 = str_store_faction_name(party_faction_002)
    if party_slot_001 >= 0:
        s8 = str_store_troop_name(party_slot_001)
        s7 = str_store_string("@{s8} of {s9}")
    #end
    if party_slot_eq(_current_town,0,2):
        if party_slot_001 == trp.player:
            s11 = str_store_string("@ Your own banner flies over the castle gate.")
        elif party_slot_001 >= 0:
            s11 = str_store_string("@ You see the banner of {s7} over the castle gate.")
        elif is_between(party_faction_002,fac.player_supporters_faction,fac.kingdoms_end):
            s11 = str_store_string(gstr._this_castle_is_temporarily_under_royal_control)
        else:
            s11 = str_store_string(gstr._this_castle_does_not_seem_to_be_under_anyones_control)
        #end
    else:
        if party_slot_001 == trp.player:
            s11 = str_store_string("@ Your own banner flies over the town gates.")
        elif party_slot_001 >= 0:
            s11 = str_store_string("@ You see the banner of {s7} over the town gates.")
        elif is_between(party_faction_002,fac.player_supporters_faction,fac.kingdoms_end):
            s11 = str_store_string(gstr._this_town_is_temporarily_under_royal_control)
        else:
            s11 = str_store_string(gstr._the_townspeople_seem_to_have_declared_their_independence)
        #end
    #end
    reg7 = party_get_num_companions(p.collective_enemy)
    _castle_undefended = 0
    str_clear(3)
    if reg7 == 0:
        _castle_undefended = 1
        s3 = str_store_string(gstr.castle_is_abondened)
    elif _g_encountered_x_party_faction == fac.player_supporters_faction:
        s3 = str_store_string(gstr.place_is_occupied_by_player)
    elif _g_encountered_party_relation < 0:
        s3 = str_store_string(gstr.place_is_occupied_by_enemy)
    else:
        pass
    #end
    if _g_leave_town_outside == 1:
        _g_leave_town_outside = 0
        _g_permitted_to_center = 0
        change_screen_return()
    elif check_quest_active(qst.escort_lady) and quest_slot_eq(qst.escort_lady,1,_g_encountered_party):
        quest_slot_003 = quest_get_slot(qst.escort_lady,4)
        get_meeting_scene()
        scene_id_004 = reg0
        modify_visitors_at_site(scene_id_004)
        reset_visitors()
        set_visitor(0,trp.player)
        set_visitor(17,quest_slot_003)
        set_jump_mission(mt.conversation_encounter)
        jump_to_scene(scene_id_004)
        _talk_context = 10
        change_screen_map_conversation(quest_slot_003)
    elif check_quest_active(qst.kidnapped_girl) and quest_slot_eq(qst.kidnapped_girl,12,_g_encountered_party) and quest_slot_eq(qst.kidnapped_girl,11,3):
        get_meeting_scene()
        scene_id_004 = reg0
        modify_visitors_at_site(scene_id_004)
        reset_visitors()
        set_visitor(0,trp.player)
        set_visitor(17,trp.kidnapped_girl)
        set_jump_mission(mt.conversation_encounter)
        jump_to_scene(scene_id_004)
        _talk_context = 10
        change_screen_map_conversation(trp.kidnapped_girl)
    elif _g_town_visit_after_rest == 1:
        _g_town_visit_after_rest = 0
        jump_to_menu(mnu.town)
    elif party_slot_eq(_g_encountered_party,0,2) and party_slot_eq(_g_encountered_party,7,trp.player) or faction_slot_eq(_g_encountered_x_party_faction,11,trp.player):
        jump_to_menu(mnu.enter_your_own_castle)
    elif party_slot_eq(_g_encountered_party,0,2) and _g_encountered_party_relation >= 0 and _castle_undefended == 1 or _g_permitted_to_center == 1 or _g_encountered_x_party_faction == _players_kingdom:
        jump_to_menu(mnu.town)
    elif party_slot_eq(_g_encountered_party,0,3) and _g_encountered_party_relation >= 0:
        jump_to_menu(mnu.town)
    elif _g_player_besiege_town == _g_encountered_party:
        jump_to_menu(mnu.castle_besiege)
    #end
    set_town_picture()
castle_outside.conditionBlock = condition

castle_outside_approach_gates = MenuOption("approach_gates", "Approach the gates and hail the guard.")
def code():
    jump_to_menu(mnu.castle_guard)
castle_outside_approach_gates.codeBlock = code

castle_outside_town_sneak = MenuOption("town_sneak", "Disguise yourself and try to sneak into the {s7}")
def condition():
    if party_slot_eq(_g_encountered_party,0,3):
        s7 = str_store_string(gstr.town)
    else:
        s7 = str_store_string(gstr.castle)
    #end
castle_outside_town_sneak.conditionBlock = condition
def code():
    faction_slot_001 = faction_get_slot(_g_encountered_x_party_faction,30)
    party_num_companions_002 = party_get_num_companions(p.main_party)
    party_num_prisioners_003 = party_get_num_prisoners(p.main_party)
    party_num_companions_002 += party_num_prisioners_003
    party_num_companions_002 *= 2
    party_num_companions_002 /= 3
    var004 = faction_slot_001 + party_num_companions_002
    random_x_005 = store_random_in_range(0,100)
    if random_x_005 >= var004 or _g_last_defeated_bandits_town == _g_encountered_party:
        _g_last_defeated_bandits_town = 0
        _sneaked_into_town = 1
        _town_entered = 1
        jump_to_menu(mnu.sneak_into_town_suceeded)
        _g_mt_mode = 1
    else:
        jump_to_menu(mnu.sneak_into_town_caught)
    #end
castle_outside_town_sneak.codeBlock = code

castle_outside_castle_start_siege = MenuOption("castle_start_siege", "Besiege the {reg6?town:castle}.")
def condition():
    if party_slot_eq(_g_encountered_party,54,-1) or party_slot_eq(_g_encountered_party,54,p.main_party):
        faction_relation_001 = store_relation(_g_encountered_x_party_faction,fac.player_supporters_faction)
        if faction_relation_001 < 0 and _g_encountered_party_2 < 1:
            party_count_fit_for_battle(p.main_party)
            if reg0 > 5:
                if party_slot_eq(_g_encountered_party,0,3):
                    reg6 = 1
                else:
                    reg6 = 0
                #end
            #end
        #end
    #end
castle_outside_castle_start_siege.conditionBlock = condition
def code():
    _g_player_besiege_town = _g_encountered_party
    faction_relation_001 = store_relation(fac.player_supporters_faction,_g_encountered_x_party_faction)
    val_min(faction_relation_001,-40)
    set_player_relation_with_faction(_g_encountered_x_party_faction,faction_relation_001)
    update_all_notes()
    jump_to_menu(mnu.castle_besiege)
castle_outside_castle_start_siege.codeBlock = code

castle_outside_cheat_castle_start_siege = MenuOption("cheat_castle_start_siege", "{!}CHEAT: Besiege the {reg6?town:castle}...")
def condition():
    if _cheat_mode == 1 and party_slot_eq(_g_encountered_party,54,-1) or party_slot_eq(_g_encountered_party,54,p.main_party):
        faction_relation_001 = store_relation(_g_encountered_x_party_faction,fac.player_supporters_faction)
        if faction_relation_001 >= 0 and _g_encountered_party_2 < 1:
            party_count_fit_for_battle(p.main_party)
            if reg0 > 1:
                if party_slot_eq(_g_encountered_party,0,3):
                    reg6 = 1
                else:
                    reg6 = 0
                #end
            #end
        #end
    #end
castle_outside_cheat_castle_start_siege.conditionBlock = condition
def code():
    _g_player_besiege_town = _g_encountered_party
    jump_to_menu(mnu.castle_besiege)
castle_outside_cheat_castle_start_siege.codeBlock = code

castle_outside_castle_leave = MenuOption("castle_leave", "Leave.")
def code():
    change_screen_return(0)
castle_outside_castle_leave.codeBlock = code

castle_outside_castle_cheat_interior = MenuOption("castle_cheat_interior", "{!}CHEAT! Interior.")
def code():
    set_jump_mission(mt.ai_training)
    party_slot_001 = party_get_slot(_current_town,11)
    jump_to_scene(party_slot_001)
    change_screen_mission()
castle_outside_castle_cheat_interior.codeBlock = code

castle_outside_castle_cheat_exterior = MenuOption("castle_cheat_exterior", "{!}CHEAT! Exterior.")
def code():
    set_jump_mission(mt.ai_training)
    party_slot_001 = party_get_slot(_current_town,10)
    jump_to_scene(party_slot_001)
    change_screen_mission()
castle_outside_castle_cheat_exterior.codeBlock = code

castle_outside_castle_cheat_town_walls = MenuOption("castle_cheat_town_walls", "{!}CHEAT! Town Walls.")
def code():
    party_slot_001 = party_get_slot(_current_town,18)
    set_jump_mission(mt.ai_training)
    jump_to_scene(party_slot_001)
    change_screen_mission()
castle_outside_castle_cheat_town_walls.codeBlock = code



castle_guard = GameMenu("castle_guard", 4096,
"You approach the gate. The men on the walls watch you closely."
)
def condition():
    set_town_picture()
castle_guard.conditionBlock = condition

castle_guard_request_shelter = MenuOption("request_shelter", "Request entry to the castle.")
def code():
    party_slot_001 = party_get_slot(_g_encountered_party,7)
    if party_slot_001 < 0:
        jump_to_menu(mnu.castle_entry_granted)
    else:
        troop_get_player_relation(party_slot_001)
        var002 = reg0
        if var002 > -15:
            jump_to_menu(mnu.castle_entry_granted)
        else:
            jump_to_menu(mnu.castle_entry_denied)
        #end
    #end
castle_guard_request_shelter.codeBlock = code

castle_guard_request_meeting_commander = MenuOption("request_meeting_commander", "Request a meeting with someone.")
def code():
    jump_to_menu(mnu.castle_meeting)
castle_guard_request_meeting_commander.codeBlock = code

castle_guard_guard_leave = MenuOption("guard_leave", "Leave.")
def code():
    change_screen_return(0)
castle_guard_guard_leave.codeBlock = code



castle_entry_granted = GameMenu("castle_entry_granted", 4096,
"After a brief wait, the guards open the gates for you and allow your party inside."
)
def condition():
    set_town_picture()
castle_entry_granted.conditionBlock = condition

castle_entry_granted_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.town)
castle_entry_granted_continue.codeBlock = code



castle_entry_denied = GameMenu("castle_entry_denied", 4096,
"The lord of this castle has forbidden you from coming inside these walls, and the guard sergeant informs you that his men will fire if you attempt to come any closer."
)
def condition():
    set_town_picture()
castle_entry_denied.conditionBlock = condition

castle_entry_denied_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.castle_guard)
castle_entry_denied_continue.codeBlock = code



castle_meeting = GameMenu("castle_meeting", 4096,
"With whom do you want to meet?"
)
def condition():
    _num_castle_meeting_troops = 0
    for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
        if troop_slot_eq(trp_001,2,2):
            get_troop_attached_party(trp_001)
            if _g_encountered_party == reg0:
                troop_set_slot(trp.temp_array_a,_num_castle_meeting_troops,trp_001)
                _num_castle_meeting_troops += 1
            #end
        #end
    #end
    set_town_picture()
castle_meeting.conditionBlock = condition

castle_meeting_guard_meet_s5 = MenuOption("guard_meet_s5", "{s5}.")
def condition():
    if _num_castle_meeting_troops > 0:
        troop_slot_001 = troop_get_slot(trp.temp_array_a,0)
        s5 = str_store_troop_name(troop_slot_001)
castle_meeting_guard_meet_s5.conditionBlock = condition
def code():
    _castle_meeting_selected_troop = troop_get_slot(trp.temp_array_a,0)
    jump_to_menu(mnu.castle_meeting_selected)
castle_meeting_guard_meet_s5.codeBlock = code

castle_meeting_guard_meet_s5 = MenuOption("guard_meet_s5", "{s5}.")
def condition():
    if _num_castle_meeting_troops > 1:
        troop_slot_001 = troop_get_slot(trp.temp_array_a,1)
        s5 = str_store_troop_name(troop_slot_001)
castle_meeting_guard_meet_s5.conditionBlock = condition
def code():
    _castle_meeting_selected_troop = troop_get_slot(trp.temp_array_a,1)
    jump_to_menu(mnu.castle_meeting_selected)
castle_meeting_guard_meet_s5.codeBlock = code

castle_meeting_guard_meet_s5 = MenuOption("guard_meet_s5", "{s5}.")
def condition():
    if _num_castle_meeting_troops > 2:
        troop_slot_001 = troop_get_slot(trp.temp_array_a,2)
        s5 = str_store_troop_name(troop_slot_001)
castle_meeting_guard_meet_s5.conditionBlock = condition
def code():
    _castle_meeting_selected_troop = troop_get_slot(trp.temp_array_a,2)
    jump_to_menu(mnu.castle_meeting_selected)
castle_meeting_guard_meet_s5.codeBlock = code

castle_meeting_guard_meet_s5 = MenuOption("guard_meet_s5", "{s5}.")
def condition():
    if _num_castle_meeting_troops > 3:
        troop_slot_001 = troop_get_slot(trp.temp_array_a,3)
        s5 = str_store_troop_name(troop_slot_001)
castle_meeting_guard_meet_s5.conditionBlock = condition
def code():
    _castle_meeting_selected_troop = troop_get_slot(trp.temp_array_a,3)
    jump_to_menu(mnu.castle_meeting_selected)
castle_meeting_guard_meet_s5.codeBlock = code

castle_meeting_guard_meet_s5 = MenuOption("guard_meet_s5", "{s5}.")
def condition():
    if _num_castle_meeting_troops > 4:
        troop_slot_001 = troop_get_slot(trp.temp_array_a,4)
        s5 = str_store_troop_name(troop_slot_001)
castle_meeting_guard_meet_s5.conditionBlock = condition
def code():
    _castle_meeting_selected_troop = troop_get_slot(trp.temp_array_a,4)
    jump_to_menu(mnu.castle_meeting_selected)
castle_meeting_guard_meet_s5.codeBlock = code

castle_meeting_guard_meet_s5 = MenuOption("guard_meet_s5", "{s5}.")
def condition():
    if _num_castle_meeting_troops > 5:
        troop_slot_001 = troop_get_slot(trp.temp_array_a,5)
        s5 = str_store_troop_name(troop_slot_001)
castle_meeting_guard_meet_s5.conditionBlock = condition
def code():
    _castle_meeting_selected_troop = troop_get_slot(trp.temp_array_a,5)
    jump_to_menu(mnu.castle_meeting_selected)
castle_meeting_guard_meet_s5.codeBlock = code

castle_meeting_guard_meet_s5 = MenuOption("guard_meet_s5", "{s5}.")
def condition():
    if _num_castle_meeting_troops > 6:
        troop_slot_001 = troop_get_slot(trp.temp_array_a,6)
        s5 = str_store_troop_name(troop_slot_001)
castle_meeting_guard_meet_s5.conditionBlock = condition
def code():
    _castle_meeting_selected_troop = troop_get_slot(trp.temp_array_a,6)
    jump_to_menu(mnu.castle_meeting_selected)
castle_meeting_guard_meet_s5.codeBlock = code

castle_meeting_guard_meet_s5 = MenuOption("guard_meet_s5", "{s5}.")
def condition():
    if _num_castle_meeting_troops > 7:
        troop_slot_001 = troop_get_slot(trp.temp_array_a,7)
        s5 = str_store_troop_name(troop_slot_001)
castle_meeting_guard_meet_s5.conditionBlock = condition
def code():
    _castle_meeting_selected_troop = troop_get_slot(trp.temp_array_a,7)
    jump_to_menu(mnu.castle_meeting_selected)
castle_meeting_guard_meet_s5.codeBlock = code

castle_meeting_guard_meet_s5 = MenuOption("guard_meet_s5", "{s5}.")
def condition():
    if _num_castle_meeting_troops > 8:
        troop_slot_001 = troop_get_slot(trp.temp_array_a,8)
        s5 = str_store_troop_name(troop_slot_001)
castle_meeting_guard_meet_s5.conditionBlock = condition
def code():
    _castle_meeting_selected_troop = troop_get_slot(trp.temp_array_a,8)
    jump_to_menu(mnu.castle_meeting_selected)
castle_meeting_guard_meet_s5.codeBlock = code

castle_meeting_guard_meet_s5 = MenuOption("guard_meet_s5", "{s5}.")
def condition():
    if _num_castle_meeting_troops > 9:
        troop_slot_001 = troop_get_slot(trp.temp_array_a,9)
        s5 = str_store_troop_name(troop_slot_001)
castle_meeting_guard_meet_s5.conditionBlock = condition
def code():
    _castle_meeting_selected_troop = troop_get_slot(trp.temp_array_a,9)
    jump_to_menu(mnu.castle_meeting_selected)
castle_meeting_guard_meet_s5.codeBlock = code

castle_meeting_forget_it = MenuOption("forget_it", "Forget it.")
def code():
    jump_to_menu(mnu.castle_guard)
castle_meeting_forget_it.codeBlock = code



castle_meeting_selected = GameMenu("castle_meeting_selected", 0,
"Your request for a meeting is relayed inside, and finally {s6} appears in the courtyard to speak with you."
)
def condition():
    s6 = str_store_troop_name(_castle_meeting_selected_troop)
castle_meeting_selected.conditionBlock = condition

castle_meeting_selected_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.castle_outside)
    modify_visitors_at_site(scn.conversation_scene)
    reset_visitors()
    set_visitor(0,trp.player)
    set_visitor(17,_castle_meeting_selected_troop)
    set_jump_mission(mt.conversation_encounter)
    jump_to_scene(scn.conversation_scene)
    _talk_context = 3
    change_screen_map_conversation(_castle_meeting_selected_troop)
castle_meeting_selected_continue.codeBlock = code



castle_besiege = GameMenu("castle_besiege", 4096,
"You are laying siege to {s1}. {s2} {s3}"
)
def condition():
    troop_type_001 = troop_get_type(trp.player)
    if troop_type_001 == 1:
        set_background_mesh(mesh.pic_siege_sighted_fem)
    else:
        set_background_mesh(mesh.pic_siege_sighted)
    #end
    _g_siege_force_wait = 0
    if party_slot_eq(_g_encountered_party,54,-1):
        party_set_slot(_g_encountered_party,54,p.main_party)
        cur_hours_002 = store_current_hours()
        party_set_slot(_g_encountered_party,64,cur_hours_002)
        _g_siege_method = 0
        _g_siege_sallied_out_once = 0
    #end
    party_slot_003 = party_get_slot(_g_encountered_party,53)
    center_get_food_consumption(_g_encountered_party)
    var004 = reg0
    reg7 = var004
    reg8 = party_slot_003
    reg3 = party_slot_003 / var004
    if party_slot_eq(_g_encountered_party,0,3):
        reg6 = 1
    else:
        reg6 = 0
    #end
    if reg3 > 0:
        s2 = str_store_string("@The {reg6?town's:castle's} food stores should last for {reg3} more days.")
    else:
        s2 = str_store_string("@The {reg6?town's:castle's} food stores have run out and the defenders are starving.")
    #end
    s3 = str_store_string(gstr.empty_string)
    if _g_siege_method >= 1:
        cur_hours_002 = store_current_hours()
        if cur_hours_002 < _g_siege_method_finish_hours:
            reg9 = _g_siege_method_finish_hours - cur_hours_002
            if _g_siege_method == 1:
                s3 = str_store_string("@You're preparing to attack the walls;;; the work should finish in {reg9} hours.")
            elif _g_siege_method == 2:
                s3 = str_store_string("@Your forces are building a siege tower. They estimate another {reg9} hours to complete the build.")
            #end
        else:
            if _g_siege_method == 1:
                s3 = str_store_string("@You are ready to attack the walls at any time.")
            elif _g_siege_method == 2:
                s3 = str_store_string("@The siege tower is built and ready to make an assault.")
            #end
        #end
    #end
    if _g_castle_left_to_player == 1:
        _g_castle_left_to_player = 0
        party_faction_005 = store_faction_of_party(_g_encountered_party)
        party_set_faction(_g_encountered_party,fac.neutral)
        party_num_attached_parties_006 = party_get_num_attached_parties(_g_encountered_party)
        for var007 in range(0, party_num_attached_parties_006):
            party_attached_party_with_rank_008 = party_get_attached_party_with_rank(_g_encountered_party,var007)
            party_detach(party_attached_party_with_rank_008)
            party_slot_009 = party_get_slot(party_attached_party_with_rank_008,0)
            if party_slot_009 == 13:
                party_faction_010 = store_faction_of_party(party_attached_party_with_rank_008)
                get_closest_walled_center_of_faction(party_attached_party_with_rank_008,party_faction_010)
                if reg0 > 0:
                    party_set_ai_state(party_attached_party_with_rank_008,7,reg0)
                else:
                    party_set_ai_state(party_attached_party_with_rank_008,4,_g_encountered_party)
                #end
            #end
        #end
        party_remove_all_companions(_g_encountered_party)
        change_screen_return()
        party_collect_attachments_to_party(_g_encountered_party,p.collective_enemy)
        party_copy(p.encountered_party_backup,p.collective_enemy)
        party_set_faction(_g_encountered_party,party_faction_005)
    #end
    _g_enemy_party = _g_encountered_party
    _g_ally_party = -1
    s1 = str_store_party_name(_g_encountered_party)
    encounter_calculate_fit()
    reg11 = _g_enemy_fit_for_battle
    reg10 = _g_friend_fit_for_battle
    if _g_leave_encounter == 1:
        change_screen_return()
    else:
        party_count_fit_regulars(p.collective_enemy)
        var011 = 0
        if _g_battle_result == 1:
            var011 = 1
        elif _g_enemy_fit_for_battle <= 0 and _g_friend_fit_for_battle >= 1:
            var011 = 1
        #end
        if var011 == 1 or _g_enemy_surrenders == 1:
            _g_next_menu = mnu.castle_taken
            jump_to_menu(mnu.total_victory)
        else:
            party_count_members_with_full_health(p.main_party)
            var012 = reg0
            if _g_battle_result == -1 and var012 == 0:
                _g_next_menu = mnu.captivity_start_castle_defeat
                jump_to_menu(mnu.total_defeat)
            #end
        #end
    #end
castle_besiege.conditionBlock = condition

castle_besiege_siege_request_meeting = MenuOption("siege_request_meeting", "Call for a meeting with the castle commander.")
def code():
    _cant_talk_to_enemy = 1
    _g_enemy_surrenders = 0
    _g_castle_left_to_player = 0
    _talk_context = 7
    party_num_attached_parties_001 = party_get_num_attached_parties(_g_encountered_party)
    if party_num_attached_parties_001 > 0:
        party_attached_party_with_rank_002 = party_get_attached_party_with_rank(_g_encountered_party,0)
        setup_party_meeting(party_attached_party_with_rank_002)
    else:
        setup_party_meeting(_g_encountered_party)
    #end
castle_besiege_siege_request_meeting.codeBlock = code

castle_besiege_wait_24_hours = MenuOption("wait_24_hours", "Wait until tomorrow.")
def code():
    _auto_besiege_town = _g_encountered_party
    _g_siege_force_wait = 1
    cur_time_of_day_001 = store_time_of_day()
    cur_time_of_day_001 += 1
    var002 = 31
    var002 -= cur_time_of_day_001
    var002 %= 24
    var002 += 1
    rest_for_hours_interactive(var002,5,1)
    _cant_talk_to_enemy = 0
    change_screen_return()
castle_besiege_wait_24_hours.codeBlock = code

castle_besiege_castle_lead_attack = MenuOption("castle_lead_attack", "Lead your soldiers in an assault.")
def condition():
    if not troop_is_wounded(trp.player) and _g_siege_method >= 1 and _g_friend_fit_for_battle > 3:
        cur_hours_001 = store_current_hours()
castle_besiege_castle_lead_attack.conditionBlock = condition
def code():
    if party_slot_eq(_g_encountered_party,0,3):
        party_slot_001 = party_get_slot(_g_encountered_party,18)
    else:
        party_slot_001 = party_get_slot(_g_encountered_party,10)
    #end
    calculate_renown_value()
    calculate_battle_advantage()
    var002 = reg0
    var002 *= 2
    var002 /= 3
    set_battle_advantage(var002)
    set_party_battle_mode()
    _g_siege_battle_state = 1
    var003 = 0
    if var002 <= -4 and _g_siege_sallied_out_once == 0:
        set_jump_mission(mt.castle_attack_walls_defenders_sally)
        _g_siege_battle_state = 0
        var003 = 1
    elif party_slot_eq(_current_town,27,1):
        set_jump_mission(mt.castle_attack_walls_belfry)
    else:
        set_jump_mission(mt.castle_attack_walls_ladder)
    #end
    _cant_talk_to_enemy = 0
    _g_siege_final_menu = mnu.castle_besiege
    _g_next_menu = mnu.castle_besiege_inner_battle
    _g_siege_method = 0
    jump_to_scene(party_slot_001)
    if var003 == 1:
        jump_to_menu(mnu.siege_attack_meets_sally)
    else:
        jump_to_menu(mnu.battle_debrief)
        change_screen_mission()
    #end
castle_besiege_castle_lead_attack.codeBlock = code

castle_besiege_attack_stay_back = MenuOption("attack_stay_back", "Order your soldiers to attack while you stay back...")
def condition():
    if _g_siege_method >= 1 and _g_friend_fit_for_battle > 3:
        cur_hours_001 = store_current_hours()
castle_besiege_attack_stay_back.conditionBlock = condition
def code():
    _cant_talk_to_enemy = 0
    jump_to_menu(mnu.castle_attack_walls_simulate)
castle_besiege_attack_stay_back.codeBlock = code

castle_besiege_build_ladders = MenuOption("build_ladders", "Prepare ladders to attack the walls.")
def code():
    jump_to_menu(mnu.construct_ladders)
castle_besiege_build_ladders.codeBlock = code

castle_besiege_build_siege_tower = MenuOption("build_siege_tower", "Build a siege tower.")
def code():
    jump_to_menu(mnu.construct_siege_tower)
castle_besiege_build_siege_tower.codeBlock = code

castle_besiege_cheat_castle_lead_attack = MenuOption("cheat_castle_lead_attack", "{!}CHEAT: Instant build equipments.")
def code():
    _g_siege_method = 1
    _g_siege_method_finish_hours = 0
    jump_to_menu(mnu.castle_besiege)
castle_besiege_cheat_castle_lead_attack.codeBlock = code

castle_besiege_cheat_conquer_castle = MenuOption("cheat_conquer_castle", "{!}CHEAT: Instant conquer castle.")
def code():
    _g_next_menu = mnu.castle_taken
    jump_to_menu(mnu.total_victory)
castle_besiege_cheat_conquer_castle.codeBlock = code

castle_besiege_lift_siege = MenuOption("lift_siege", "Abandon the siege.")
def code():
    lift_siege(_g_player_besiege_town,0)
    _g_player_besiege_town = -1
    change_screen_return()
castle_besiege_lift_siege.codeBlock = code



siege_attack_meets_sally = GameMenu("siege_attack_meets_sally", 4096,
"The defenders sally out to meet your assault."
)
def condition():
    set_background_mesh(mesh.pic_sally_out)
siege_attack_meets_sally.conditionBlock = condition

siege_attack_meets_sally_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.battle_debrief)
    change_screen_mission()
siege_attack_meets_sally_continue.codeBlock = code



castle_besiege_inner_battle = GameMenu("castle_besiege_inner_battle", 4096,
"{s1}"
)
def condition():
    troop_type_001 = troop_get_type(trp.player)
    if troop_type_001 == 1:
        set_background_mesh(mesh.pic_siege_sighted_fem)
    else:
        set_background_mesh(mesh.pic_siege_sighted)
    #end
    var002 = _g_battle_result
    encounter_calculate_fit()
    s1 = str_store_string("@As a last defensive effort;;; you retreat to the main hall of the keep. You and your remaining soldiers will put up a desperate fight here. If you are defeated;;; there's no other place to fall back to.")
    s1 = str_store_string("@You've been driven away from the walls. Now the attackers are pouring into the streets. IF you can defeat them;;; you can perhaps turn the tide and save the day.")
    if var002 == 1 or _g_friend_fit_for_battle > 0 or _g_enemy_fit_for_battle <= 0:
        jump_to_menu(_g_siege_final_menu)
    else:
        encounter_calculate_fit()
        if party_slot_eq(_g_encountered_party,0,3):
            if _g_siege_battle_state == 0 and var002 == 1:
                _g_battle_result = 0
                jump_to_menu(_g_siege_final_menu)
            elif _g_siege_battle_state == 1 and var002 == 1:
                s1 = str_store_string("@You've breached the town walls;;; but the stubborn defenders continue to resist you in the streets! You'll have to deal with them before you can attack the keep at the heart of the town.")
            elif _g_siege_battle_state == 2 and var002 == 1:
                s1 = str_store_string("@The town centre is yours;;; but the remaining defenders have retreated to the castle. It must fall before you can complete your victory.")
            else:
                jump_to_menu(_g_siege_final_menu)
            #end
        else:
            if _g_siege_battle_state == 0 and var002 == 1:
                _g_battle_result = 0
                jump_to_menu(_g_siege_final_menu)
            elif _g_siege_battle_state == 1 and var002 == 1:
                s1 = str_store_string("@The remaining defenders have retreated to the castle as a last defense. You must go in and crush any remaining resistance.")
            else:
                jump_to_menu(_g_siege_final_menu)
            #end
        #end
    #end
castle_besiege_inner_battle.conditionBlock = condition

castle_besiege_inner_battle_continue = MenuOption("continue", "Continue...")
def code():
    if party_slot_eq(_g_encountered_party,0,3):
        if _g_siege_battle_state == 1:
            party_slot_001 = party_get_slot(_g_encountered_party,10)
            set_jump_mission(mt.besiege_inner_battle_town_center)
        else:
            party_slot_001 = party_get_slot(_g_encountered_party,11)
            set_jump_mission(mt.besiege_inner_battle_castle)
        #end
    else:
        party_slot_001 = party_get_slot(_g_encountered_party,11)
        set_jump_mission(mt.besiege_inner_battle_castle)
    #end
    set_party_battle_mode()
    jump_to_scene(party_slot_001)
    _g_siege_battle_state += 1
    _g_next_menu = mnu.castle_besiege_inner_battle
    jump_to_menu(mnu.battle_debrief)
    change_screen_mission()
castle_besiege_inner_battle_continue.codeBlock = code



construct_ladders = GameMenu("construct_ladders", 0,
"As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that it will take {reg4} hours to build enough scaling ladders for the assault."
)
def condition():
    get_max_skill_of_player_party(skl.engineer)
    var001 = reg0
    var002 = reg1
    reg2 = var001
    reg4 = 14 - var001
    reg4 *= 2
    reg4 /= 3
    if var002 == trp.player:
        reg3 = 1
    else:
        reg3 = 0
        s3 = str_store_troop_name(var002)
    #end
construct_ladders.conditionBlock = condition

construct_ladders_build_ladders_cont = MenuOption("build_ladders_cont", "Do it.")
def code():
    _g_siege_method = 1
    cur_hours_001 = store_current_hours()
    get_max_skill_of_player_party(skl.engineer)
    var002 = 14 - reg0
    var002 *= 2
    var002 /= 3
    _g_siege_method_finish_hours = cur_hours_001 + var002
    _auto_besiege_town = _current_town
    rest_for_hours_interactive(96,5,1)
    change_screen_return()
construct_ladders_build_ladders_cont.codeBlock = code

construct_ladders_go_back = MenuOption("go_back", "Go back.")
def code():
    jump_to_menu(mnu.castle_besiege)
construct_ladders_go_back.codeBlock = code



construct_siege_tower = GameMenu("construct_siege_tower", 0,
"As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that building a siege tower will take {reg4} hours."
)
def condition():
    get_max_skill_of_player_party(skl.engineer)
    var001 = reg0
    var002 = reg1
    reg2 = var001
    reg4 = 15 - var001
    reg4 *= 6
    if var002 == trp.player:
        reg3 = 1
    else:
        reg3 = 0
        s3 = str_store_troop_name(var002)
    #end
construct_siege_tower.conditionBlock = condition

construct_siege_tower_build_siege_tower_cont = MenuOption("build_siege_tower_cont", "Start building.")
def code():
    _g_siege_method = 2
    cur_hours_001 = store_current_hours()
    get_max_skill_of_player_party(skl.engineer)
    var002 = 15 - reg0
    var002 *= 6
    _g_siege_method_finish_hours = cur_hours_001 + var002
    _auto_besiege_town = _current_town
    rest_for_hours_interactive(240,5,1)
    change_screen_return()
construct_siege_tower_build_siege_tower_cont.codeBlock = code

construct_siege_tower_go_back = MenuOption("go_back", "Go back.")
def code():
    jump_to_menu(mnu.castle_besiege)
construct_siege_tower_go_back.codeBlock = code



castle_attack_walls_simulate = GameMenu("castle_attack_walls_simulate", 4608,
"{s4}^^Your casualties:{s8}^^Enemy casualties were: {s9}"
)
def condition():
    if True:
        set_background_mesh(mesh.pic_siege_attack)
    #end
    party_calculate_strength(p.main_party,1)
    var001 = reg0
    var001 /= 10
    party_calculate_strength(_g_encountered_party,0)
    var002 = reg0
    var002 /= 4
    inflict_casualties_to_party_group(p.main_party,var002,p.temp_casualties)
    print_casualties_to_s0(p.temp_casualties,0)
    s8 = str_store_string_reg(0)
    inflict_casualties_to_party_group(_g_encountered_party,var001,p.temp_casualties)
    print_casualties_to_s0(p.temp_casualties,0)
    s9 = str_store_string_reg(0)
    _no_soldiers_left = 0
    if True:
        party_count_members_with_full_health(p.main_party)
        if reg0 <= 0:
            _no_soldiers_left = 1
            s4 = str_store_string(gstr.attack_walls_failure)
        else:
            party_count_members_with_full_health(_g_encountered_party)
            if reg0 <= 0:
                _no_soldiers_left = 1
                _g_battle_result = 1
                s4 = str_store_string(gstr.attack_walls_success)
            else:
                s4 = str_store_string(gstr.attack_walls_continue)
            #end
        #end
    #end
castle_attack_walls_simulate.conditionBlock = condition

castle_attack_walls_simulate_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.castle_besiege)
castle_attack_walls_simulate_continue.codeBlock = code



castle_attack_walls_with_allies_simulate = GameMenu("castle_attack_walls_with_allies_simulate", 4608,
"{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}"
)
def condition():
    if True:
        set_background_mesh(mesh.pic_siege_attack)
    #end
    party_calculate_strength(p.main_party,1)
    var001 = reg0
    var001 /= 10
    party_calculate_strength(p.collective_friends,0)
    var002 = reg0
    var002 /= 10
    val_max(var002,1)
    party_calculate_strength(p.collective_enemy,0)
    var003 = reg0
    var003 /= 4
    if var002 == 0:
        var004 = var003 / 2
    else:
        var004 = var003
        var004 *= var001
        var004 /= var002
    #end
    var003 -= var004
    inflict_casualties_to_party_group(p.main_party,var004,p.temp_casualties)
    print_casualties_to_s0(p.temp_casualties,0)
    s8 = str_store_string_reg(0)
    inflict_casualties_to_party_group(_g_enemy_party,var002,p.temp_casualties)
    print_casualties_to_s0(p.temp_casualties,0)
    s10 = str_store_string_reg(0)
    collect_friendly_parties()
    inflict_casualties_to_party_group(_g_ally_party,var003,p.temp_casualties)
    print_casualties_to_s0(p.temp_casualties,0)
    s9 = str_store_string_reg(0)
    party_collect_attachments_to_party(_g_enemy_party,p.collective_enemy)
    _no_soldiers_left = 0
    if True:
        party_count_members_with_full_health(p.main_party)
        if reg0 <= 0:
            _no_soldiers_left = 1
            s4 = str_store_string(gstr.attack_walls_failure)
        else:
            party_count_members_with_full_health(p.collective_enemy)
            if reg0 <= 0:
                _no_soldiers_left = 1
                _g_battle_result = 1
                s4 = str_store_string(gstr.attack_walls_success)
            else:
                s4 = str_store_string(gstr.attack_walls_continue)
            #end
        #end
    #end
castle_attack_walls_with_allies_simulate.conditionBlock = condition

castle_attack_walls_with_allies_simulate_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.besiegers_camp_with_allies)
castle_attack_walls_with_allies_simulate_continue.codeBlock = code



castle_taken_by_friends = GameMenu("castle_taken_by_friends", 0,
"Nothing to see here."
)
def condition():
    party_clear(_g_encountered_party)
    troop_id_001 = party_stack_get_troop_id(_g_encountered_party_2,0)
    party_set_slot(_g_encountered_party,28,troop_id_001)
    troop_faction_002 = store_faction_of_troop(troop_id_001)
    change_center_prosperity(_g_encountered_party,-5)
    if True:
        var003 = 20
        if is_between(_g_encountered_party,p.town_1,p.castle_1):
            var003 = 40
        #end
    #end
    if troop_faction_002 != _g_encountered_x_party_faction:
        faction_inflict_war_damage_on_faction(troop_faction_002,_g_encountered_x_party_faction,var003)
    #end
    give_center_to_faction(_g_encountered_party,troop_faction_002)
    add_log_entry(18,trp.player,_g_encountered_party,0,_g_encountered_x_party_faction)
    change_screen_return()
castle_taken_by_friends.conditionBlock = condition



castle_taken = GameMenu("castle_taken", 512,
"{s3} has fallen to your troops, and you now have full control of the {reg2?town:castle}.{reg1? You may station troops here to defend it against enemies who may try to recapture it. Also, you should select now whether you will hold the {reg2?town:castle} yourself or give it to a faithful vassal...:}"
)
def condition():
    party_clear(_g_encountered_party)
    if _players_kingdom == fac.player_supporters_faction:
        party_slot_001 = party_get_slot(_g_encountered_party,7)
        if party_slot_001 != trp.player:
            for var002 in range(0, 4):
                if call_script(script.cf_reinforce_party,_g_encountered_party):
                    pass
                #end
            #end
        #end
    #end
    lift_siege(_g_encountered_party,0)
    _g_player_besiege_town = -1
    party_set_slot(_g_encountered_party,28,trp.player)
    change_center_prosperity(_g_encountered_party,-5)
    change_troop_renown(trp.player,5)
    var003 = 20
    if is_between(_g_encountered_party,p.town_1,p.castle_1):
        var003 = 40
    #end
    faction_inflict_war_damage_on_faction(_players_kingdom,_g_encountered_x_party_faction,var003)
    if is_between(_players_kingdom,fac.player_supporters_faction,fac.kingdoms_end) and _players_kingdom != fac.player_supporters_faction:
        give_center_to_faction(_g_encountered_party,_players_kingdom)
        order_best_besieger_party_to_guard_center(_g_encountered_party,_players_kingdom)
        jump_to_menu(mnu.castle_taken_2)
    else:
        give_center_to_faction(_g_encountered_party,fac.player_supporters_faction)
        order_best_besieger_party_to_guard_center(_g_encountered_party,fac.player_supporters_faction)
        s3 = str_store_party_name(_g_encountered_party)
        reg1 = 0
        if faction_slot_eq(fac.player_supporters_faction,11,trp.player):
            reg1 = 1
        #end
    #end
    reg2 = 0
    if is_between(_g_encountered_party,p.town_1,p.castle_1):
        reg2 = 1
    #end
castle_taken.conditionBlock = condition

castle_taken_continue = MenuOption("continue", "Continue...")
def code():
    _auto_enter_town = _g_encountered_party
    change_screen_return()
castle_taken_continue.codeBlock = code



castle_taken_2 = GameMenu("castle_taken_2", 512,
"{s3} has fallen to your troops, and you now have full control of the castle. It is time to send word to {s9} about your victory. {s5}"
)
def condition():
    s3 = str_store_party_name(_g_encountered_party)
    str_clear(5)
    faction_slot_001 = faction_get_slot(_players_kingdom,11)
    s9 = str_store_troop_name(faction_slot_001)
    if _player_has_homage == 0:
        reg8 = 0
        if party_slot_eq(_g_encountered_party,3,0):
            reg8 = 1
        #end
        s5 = str_store_string("@However;;; since you are not a sworn {man/follower} of {s9};;; there is no chance he would recognize you as the {lord/lady} of this {reg8?town:castle}.")
    #end
castle_taken_2.conditionBlock = condition

castle_taken_2_castle_taken_claim = MenuOption("castle_taken_claim", "Request that {s3} be awarded to you.")
def code():
    party_set_slot(_g_encountered_party,28,trp.player)
    _g_castle_requested_by_player = _current_town
    _g_castle_requested_for_troop = trp.player
    _auto_enter_town = _g_encountered_party
    change_screen_return()
castle_taken_2_castle_taken_claim.codeBlock = code

castle_taken_2_castle_taken_claim_2 = MenuOption("castle_taken_claim_2", "Request that {s3} be awarded to your {wife/husband}.")
def condition():
    troop_slot_001 = troop_get_slot(trp.player,30)
    if is_between(troop_slot_001,trp.npc1,trp.knight_1_1_wife) and troop_slot_eq(troop_slot_001,2,2):
        troop_faction_002 = store_faction_of_troop(troop_slot_001)
castle_taken_2_castle_taken_claim_2.conditionBlock = condition
def code():
    party_set_slot(_g_encountered_party,28,trp.player)
    _g_castle_requested_by_player = _current_town
    troop_slot_001 = troop_get_slot(trp.player,30)
    _g_castle_requested_for_troop = troop_slot_001
    _auto_enter_town = _g_encountered_party
    change_screen_return()
castle_taken_2_castle_taken_claim_2.codeBlock = code

castle_taken_2_castle_taken_no_claim = MenuOption("castle_taken_no_claim", "Ask no rewards.")
def code():
    party_set_slot(_g_encountered_party,28,-1)
    _auto_enter_town = _g_encountered_party
    change_screen_return()
castle_taken_2_castle_taken_no_claim.codeBlock = code



requested_castle_granted_to_player = GameMenu("requested_castle_granted_to_player", 4096,
"You receive a message from your liege, {s3}.^^ {reg4?She:He} has decided to grant {s2}{reg3? and the nearby village of {s4}:} to you, with all due incomes and titles, to hold in {reg4?her:his} name for as long as you maintain your oath of homage.."
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    faction_slot_001 = faction_get_slot(_players_kingdom,11)
    s3 = str_store_troop_name(faction_slot_001)
    s2 = str_store_party_name(_g_center_to_give_to_player)
    if party_slot_eq(_g_center_to_give_to_player,0,2):
        reg3 = 1
        for p_002 in range(p.village_1, p.salt_mine):
            if party_slot_eq(p_002,120,_g_center_to_give_to_player):
                s4 = str_store_party_name(p_002)
            #end
        #end
    else:
        reg3 = 0
    #end
    reg4 = troop_get_type(faction_slot_001)
requested_castle_granted_to_player.conditionBlock = condition

requested_castle_granted_to_player_continue = MenuOption("continue", "Continue.")
def code():
    give_center_to_lord(_g_center_to_give_to_player,trp.player,0)
    jump_to_menu(mnu.give_center_to_player_2)
requested_castle_granted_to_player_continue.codeBlock = code



requested_castle_granted_to_player_husband = GameMenu("requested_castle_granted_to_player_husband", 4096,
"You receive a message from your liege, {s3}.^^ {reg4?She:He} has decided to grant {s2}{reg3? and the nearby village of {s4}:} to your husband, {s7}."
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    faction_slot_001 = faction_get_slot(_players_kingdom,11)
    s3 = str_store_troop_name(faction_slot_001)
    s2 = str_store_party_name(_g_center_to_give_to_player)
    if party_slot_eq(_g_center_to_give_to_player,0,2):
        reg3 = 1
        for p_002 in range(p.village_1, p.salt_mine):
            if party_slot_eq(p_002,120,_g_center_to_give_to_player):
                s4 = str_store_party_name(p_002)
            #end
        #end
    else:
        reg3 = 0
    #end
    reg4 = troop_get_type(faction_slot_001)
    troop_slot_003 = troop_get_slot(trp.player,30)
    s11 = str_store_troop_name(troop_slot_003)
    s7 = str_store_string(gstr.to_your_husband_s11)
requested_castle_granted_to_player_husband.conditionBlock = condition

requested_castle_granted_to_player_husband_continue = MenuOption("continue", "Continue.")
def code():
    troop_slot_001 = troop_get_slot(trp.player,30)
    give_center_to_lord(_g_center_to_give_to_player,troop_slot_001,0)
requested_castle_granted_to_player_husband_continue.codeBlock = code



requested_castle_granted_to_another = GameMenu("requested_castle_granted_to_another", 4096,
"You receive a message from your monarch, {s3}.^^ 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts. You also requested me to give you ownership of the castle, but that is a favour which I fear I cannot grant, as you already hold significant estates in my realm. Instead I have sent you {reg6} denars to cover the expenses of your campaign, but {s2} I give to {s5}.' "
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    faction_slot_001 = faction_get_slot(_players_kingdom,11)
    s3 = str_store_troop_name(faction_slot_001)
    s2 = str_store_party_name(_g_center_to_give_to_player)
    party_slot_002 = party_get_slot(_g_center_to_give_to_player,7)
    s5 = str_store_troop_name(party_slot_002)
    reg6 = 900
    _g_castle_requested_by_player = -1
    _g_castle_requested_for_troop = -1
requested_castle_granted_to_another.conditionBlock = condition

requested_castle_granted_to_another_accept_decision = MenuOption("accept_decision", "Accept the decision.")
def code():
    troop_add_gold(trp.player,reg6)
    change_screen_return()
requested_castle_granted_to_another_accept_decision.codeBlock = code

requested_castle_granted_to_another_leave_faction = MenuOption("leave_faction", "You have been wronged! Renounce your oath to your liege! ")
def code():
    jump_to_menu(mnu.leave_faction)
    troop_add_gold(trp.player,reg6)
requested_castle_granted_to_another_leave_faction.codeBlock = code



requested_castle_granted_to_another_female = GameMenu("requested_castle_granted_to_another_female", 4096,
"You receive a message from your monarch, {s3}.^^ 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts. You also requested me to give ownership of the castle to your husband, but that is a favour which I fear I cannot grant, as he already holds significant estates in my realm. Instead I have sent you {reg6} denars to cover the expenses of your campaign, but {s2} I give to {s5}.' "
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    faction_slot_001 = faction_get_slot(_players_kingdom,11)
    s3 = str_store_troop_name(faction_slot_001)
    s2 = str_store_party_name(_g_center_to_give_to_player)
    party_slot_002 = party_get_slot(_g_center_to_give_to_player,7)
    s5 = str_store_troop_name(party_slot_002)
    reg6 = 900
    _g_castle_requested_by_player = -1
    _g_castle_requested_for_troop = -1
requested_castle_granted_to_another_female.conditionBlock = condition

requested_castle_granted_to_another_female_accept_decision = MenuOption("accept_decision", "Accept the decision.")
def code():
    troop_add_gold(trp.player,reg6)
    change_screen_return()
requested_castle_granted_to_another_female_accept_decision.codeBlock = code



leave_faction = GameMenu("leave_faction", 0,
"Renouncing your oath is a grave act. Your lord may condemn you and confiscate your lands and holdings. However, if you return them of your own free will, he may let the betrayal go without a fight."
)

leave_faction_leave_faction_give_back = MenuOption("leave_faction_give_back", "Renounce your oath and give up your holdings.")
def code():
    player_leave_faction(1)
    change_screen_return()
leave_faction_leave_faction_give_back.codeBlock = code

leave_faction_leave_faction_hold = MenuOption("leave_faction_hold", "Renounce your oath and rule your lands, including {s2}, in your own name.")
def condition():
    s2 = str_store_party_name(_g_center_to_give_to_player)
leave_faction_leave_faction_hold.conditionBlock = condition
def code():
    give_center_to_lord(_g_center_to_give_to_player,trp.player,0)
    player_leave_faction(0)
    activate_player_faction(trp.player)
    change_screen_return()
leave_faction_leave_faction_hold.codeBlock = code

leave_faction_leave_faction_cancel = MenuOption("leave_faction_cancel", "Remain loyal and accept the decision.")
def code():
    change_screen_return()
leave_faction_leave_faction_cancel.codeBlock = code



give_center_to_player = GameMenu("give_center_to_player", 4096,
"Your lord offers to extend your fiefs! {s1} sends word that he is willing to grant {s2} to you in payment for your loyal service, adding it to your holdings. What is your answer?"
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    party_faction_001 = store_faction_of_party(_g_center_to_give_to_player)
    faction_slot_002 = faction_get_slot(party_faction_001,11)
    s1 = str_store_troop_name(faction_slot_002)
    s2 = str_store_party_name(_g_center_to_give_to_player)
give_center_to_player.conditionBlock = condition

give_center_to_player_give_center_to_player_accept = MenuOption("give_center_to_player_accept", "Accept the offer.")
def code():
    give_center_to_lord(_g_center_to_give_to_player,trp.player,0)
    jump_to_menu(mnu.give_center_to_player_2)
give_center_to_player_give_center_to_player_accept.codeBlock = code

give_center_to_player_give_center_to_player_reject = MenuOption("give_center_to_player_reject", "Reject. You have no interest in holding {s2}.")
def code():
    party_set_slot(_g_center_to_give_to_player,7,-3)
    change_screen_return()
give_center_to_player_give_center_to_player_reject.codeBlock = code



give_center_to_player_2 = GameMenu("give_center_to_player_2", 0,
"With a brief ceremony, you are officially confirmed as the new lord of {s2}{reg3? and its bound village {s4}:}. {reg3?They:It} will make a fine part of your fiefdom. You can now claim the rents and revenues from your personal estates there, draft soldiers from the populace, and manage the lands as you see fit. However, you are also expected to defend your fief and your people from harm, as well as maintaining the rule of law and order."
)
def condition():
    s2 = str_store_party_name(_g_center_to_give_to_player)
    reg3 = 0
    if party_slot_eq(_g_center_to_give_to_player,0,2):
        for p_001 in range(p.village_1, p.salt_mine):
            if party_slot_eq(p_001,120,_g_center_to_give_to_player):
                s4 = str_store_party_name(p_001)
                reg3 = 1
            #end
        #end
    #end
give_center_to_player_2.conditionBlock = condition

give_center_to_player_2_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
give_center_to_player_2_continue.codeBlock = code



oath_fulfilled = GameMenu("oath_fulfilled", 0,
"You had a contract with {s1} to serve him for a certain duration. Your contract has now expired. What will you do?"
)
def condition():
    faction_slot_001 = faction_get_slot(_players_kingdom,11)
    s1 = str_store_troop_name(faction_slot_001)
oath_fulfilled.conditionBlock = condition

oath_fulfilled_renew_oath = MenuOption("renew_oath", "Renew your contract with {s1} for another month.")
def condition():
    faction_slot_001 = faction_get_slot(_players_kingdom,11)
    s1 = str_store_troop_name(faction_slot_001)
oath_fulfilled_renew_oath.conditionBlock = condition
def code():
    cur_day_001 = store_current_day()
    _mercenary_service_next_renew_day = cur_day_001 + 30
    change_screen_return()
oath_fulfilled_renew_oath.codeBlock = code

oath_fulfilled_dont_renew_oath = MenuOption("dont_renew_oath", "Become free of your bond.")
def code():
    player_leave_faction(1)
    change_screen_return()
oath_fulfilled_dont_renew_oath.codeBlock = code



siege_started_defender = GameMenu("siege_started_defender", 0,
"{s1} is launching an assault against the walls of {s2}. You have {reg10} troops fit for battle against the enemy's {reg11}. You decide to..."
)
def condition():
    select_enemy(1)
    _g_enemy_party = _g_encountered_party_2
    _g_ally_party = _g_encountered_party
    s1 = str_store_party_name(_g_enemy_party)
    s2 = str_store_party_name(_g_ally_party)
    encounter_calculate_fit()
    if _g_siege_first_encounter == 1:
        let_nearby_parties_join_current_battle(0,1)
        encounter_init_variables()
    #end
    if _g_siege_first_encounter == 0:
        if True:
            party_count_members_with_full_health(p.collective_enemy)
            var001 = reg0
            party_count_members_with_full_health(p.collective_friends)
            var002 = reg0
            var003 = 0
            if _g_battle_result == 1 and var001 == 0:
                var003 = 1
            elif _g_engaged_enemy == 1 and _g_enemy_fit_for_battle <= 0 and _g_friend_fit_for_battle >= 1:
                var003 = 1
            #end
            if var003 == 1 or _g_enemy_surrenders == 1:
                _g_next_menu = -1
                jump_to_menu(mnu.total_victory)
            else:
                var004 = 0
                if _g_battle_result == -1 or troop_is_wounded(trp.player) and var002 == 0:
                    var004 = 1
                #end
            #end
            if var004 == 1 or _g_player_surrenders == 1:
                _g_next_menu = mnu.captivity_start_under_siege_defeat
                jump_to_menu(mnu.total_defeat)
            else:
                var005 = 0
                if _g_battle_result == 1:
                    var005 = 1
                elif _g_battle_result == 0:
                    var006 = _g_enemy_fit_for_battle / 3
                    if var006 < _g_friend_fit_for_battle:
                        var005 = 1
                    else:
                        random_x_007 = store_random_in_range(0,100)
                        var008 = var002 * 13
                        var008 /= 10
                        if var008 >= var001 and random_x_007 < 10 and _new_encounter != 1:
                            var005 = 1
                        #end
                    #end
                #end
            #end
            if var005 == 1:
                party_slot_009 = party_get_slot(_g_encountered_party,65)
                party_slot_009 += 100
                party_set_slot(_g_encountered_party,65,party_slot_009)
                party_set_slot(_g_enemy_party,2,1)
                for trp_010 in range(trp.npc1, trp.knight_1_1_wife):
                    if troop_slot_eq(trp_010,2,2) and not troop_slot_ge(trp_010,8,0):
                        troop_slot_011 = troop_get_slot(trp_010,10)
                        if troop_slot_011 > 0 and party_slot_eq(troop_slot_011,4,1) and party_slot_eq(troop_slot_011,5,_g_encountered_party) and party_slot_eq(troop_slot_011,8,1):
                            party_set_ai_state(troop_slot_011,-1,-1)
                            party_set_ai_state(troop_slot_011,1,_g_encountered_party)
                        #end
                    #end
                #end
                print("@The enemy has been forced to retreat. The assault is over, but the siege continues.")
                _g_battle_simulation_cancel_for_party = _g_encountered_party
                leave_encounter()
                change_screen_return()
                _g_battle_simulation_auto_enter_town_after_battle = _g_encountered_party
            #end
        #end
    #end
    _g_siege_first_encounter = 0
    _new_encounter = 0
siege_started_defender.conditionBlock = condition

siege_started_defender_siege_defender_join_battle = MenuOption("siege_defender_join_battle", "Join the battle.")
def code():
    party_set_next_battle_simulation_time(_g_encountered_party,-1)
    _g_battle_result = 0
    if party_slot_eq(_g_encountered_party,0,3):
        party_slot_001 = party_get_slot(_g_encountered_party,18)
    else:
        party_slot_001 = party_get_slot(_g_encountered_party,10)
    #end
    calculate_battle_advantage()
    reg0 *= 2
    reg0 /= 3
    set_battle_advantage(reg0)
    set_party_battle_mode()
    if party_slot_eq(_current_town,27,1):
        set_jump_mission(mt.castle_attack_walls_belfry)
    else:
        set_jump_mission(mt.castle_attack_walls_ladder)
    #end
    jump_to_scene(party_slot_001)
    _g_next_menu = mnu.siege_started_defender
    jump_to_menu(mnu.battle_debrief)
    change_screen_mission()
siege_started_defender_siege_defender_join_battle.codeBlock = code

siege_started_defender_siege_defender_troops_join_battle = MenuOption("siege_defender_troops_join_battle", "Order your men to join the battle without you.")
def condition():
    party_count_members_with_full_health(p.main_party)
siege_started_defender_siege_defender_troops_join_battle.conditionBlock = condition
def code():
    party_set_next_battle_simulation_time(_g_encountered_party,-1)
    select_enemy(1)
    _g_enemy_party = _g_encountered_party_2
    _g_ally_party = _g_encountered_party
    _g_siege_join = 1
    jump_to_menu(mnu.siege_join_defense)
siege_started_defender_siege_defender_troops_join_battle.codeBlock = code



siege_join_defense = GameMenu("siege_join_defense", 512,
"{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}"
)
def condition():
    if _g_siege_join == 1:
        party_calculate_strength(p.main_party,1)
        var001 = reg0
        var001 /= 5
    else:
        var001 = 0
    #end
    party_calculate_strength(p.collective_ally,0)
    var002 = reg0
    var002 /= 5
    party_calculate_strength(p.collective_enemy,0)
    var003 = reg0
    var003 /= 10
    var004 = var001 + var002
    if var004 == 0:
        var005 = var003 / 2
    else:
        var005 = var003
        var005 *= var001
        var005 /= var004
    #end
    var003 -= var005
    inflict_casualties_to_party_group(p.main_party,var005,p.temp_casualties)
    print_casualties_to_s0(p.temp_casualties,0)
    s8 = str_store_string_reg(0)
    inflict_casualties_to_party_group(_g_ally_party,var003,p.temp_casualties)
    print_casualties_to_s0(p.temp_casualties,0)
    s9 = str_store_string_reg(0)
    party_collect_attachments_to_party(_g_ally_party,p.collective_ally)
    inflict_casualties_to_party_group(_g_enemy_party,var004,p.temp_casualties)
    print_casualties_to_s0(p.temp_casualties,0)
    s10 = str_store_string_reg(0)
    party_collect_attachments_to_party(_g_enemy_party,p.collective_enemy)
    if True:
        party_count_members_with_full_health(p.main_party)
        if reg0 <= 0:
            s4 = str_store_string(gstr.siege_defender_order_attack_failure)
        else:
            party_count_members_with_full_health(p.collective_enemy)
            if reg0 <= 0:
                _g_battle_result = 1
                s4 = str_store_string(gstr.siege_defender_order_attack_success)
            else:
                s4 = str_store_string(gstr.siege_defender_order_attack_continue)
            #end
        #end
    #end
siege_join_defense.conditionBlock = condition

siege_join_defense_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.siege_started_defender)
siege_join_defense_continue.codeBlock = code



enter_your_own_castle = GameMenu("enter_your_own_castle", 0,
"{s10}"
)
def condition():
    if not is_between(_players_kingdom,fac.kingdom_1,fac.kingdoms_end):
        faction_slot_001 = faction_get_slot(fac.player_supporters_faction,11)
        if faction_slot_001 == trp.player:
            s10 = str_store_string("@As you approach;;; you are spotted by the castle guards;;; who welcome you and open the gates for their {king/queen}.")
        else:
            s10 = str_store_string("@As you approach;;; you are spotted by the castle guards;;; who welcome you and open the gates for their {lord/lady}.")
        #end
    #end
    s2 = str_store_party_name(_current_town)
enter_your_own_castle.conditionBlock = condition

enter_your_own_castle_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.town)
enter_your_own_castle_continue.codeBlock = code



village = GameMenu("village", 256,
"{s10} {s12}^{s11}^{s6}{s7}"
)
def condition():
    party_cur_terrain_008_list2 = [
    12,
    4,
    ]
    party_cur_terrain_008_list1 = [
    13,
    5,
    10,
    2,
    ]
    _current_town = _g_encountered_party
    update_center_recon_notes(_current_town)
    _g_defending_against_siege = 0
    _g_battle_result = 0
    _qst_collect_taxes_currently_collecting = 0
    _qst_train_peasants_against_bandits_currently_training = 0
    if _auto_enter_in_center > 0:
        jump_to_menu(_auto_enter_in_center)
        _auto_enter_in_center = 0
    #end
    if _g_player_raiding_village != _current_town:
        _g_player_raiding_village = 0
    else:
        jump_to_menu(mnu.village_loot_continue)
    #end
    if _g_town_visit_after_rest == 1:
        _g_town_visit_after_rest = 0
    #end
    s2 = str_store_party_name(_current_town)
    party_slot_001 = party_get_slot(_current_town,7)
    party_faction_002 = store_faction_of_party(_current_town)
    s9 = str_store_faction_name(party_faction_002)
    if party_slot_001 >= 0:
        s8 = str_store_troop_name(party_slot_001)
        s7 = str_store_string("@{s8} of {s9}")
    #end
    str_clear(10)
    str_clear(12)
    if not party_slot_eq(_current_town,35,2):
        s60 = str_store_string(2)
        party_slot_003 = party_get_slot(_current_town,50)
        if _cheat_mode == 1:
            reg4 = party_slot_003
            print("@{!}Prosperity: {reg4}")
        #end
        var004 = party_slot_003 / 10
        val_min(var004,9)
        var004 += gstr.village_prosperity_0
        s10 = str_store_string(var004)
        var004 = party_slot_003 / 20
        val_min(var004,4)
        if is_between(_current_town,p.village_91,p.salt_mine):
            var004 += gstr.oasis_village_alt_prosperity_0
        else:
            var004 += gstr.village_alt_prosperity_0
        #end
        s12 = str_store_string(var004)
    #end
    str_clear(11)
    if party_slot_eq(_current_town,35,2):
        pass
    elif party_slot_001 == trp.player:
        s11 = str_store_string("@ This village and the surrounding lands belong to you.")
    elif party_slot_001 >= 0:
        s11 = str_store_string("@ You remember that this village and the surrounding lands belong to {s7}.")
    else:
        s11 = str_store_string("@ These lands belong to no one.")
    #end
    str_clear(7)
    if not party_slot_eq(_current_town,35,2):
        party_slot_005 = party_get_slot(_current_town,26)
        describe_center_relation_to_s3(party_slot_005)
        reg9 = party_slot_005
        s7 = str_store_string("@{!} {s3} [[[{reg9}]]].")
    #end
    str_clear(6)
    if party_slot_ge(_current_town,39,1):
        party_slot_006 = party_get_slot(_current_town,39)
        character_lvl_007 = store_character_level(trp.player)
        _qst_eliminate_bandits_infesting_village_num_bandits = character_lvl_007 + 10
        _qst_eliminate_bandits_infesting_village_num_bandits *= 12
        _qst_eliminate_bandits_infesting_village_num_bandits /= 10
        _qst_eliminate_bandits_infesting_village_num_villagers = store_random_in_range(25,30)
        reg8 = _qst_eliminate_bandits_infesting_village_num_bandits
        str_store_troop_name_by_count(s35,party_slot_006,_qst_eliminate_bandits_infesting_village_num_bandits)
        s6 = str_store_string("@ The village is infested by {reg8} {s35}.")
        _g_enemy_party = -1
        _g_ally_party = -1
        if party_slot_006 == trp.forest_bandit:
            set_background_mesh(mesh.pic_forest_bandits)
        elif party_slot_006 == trp.steppe_bandit:
            set_background_mesh(mesh.pic_steppe_bandits)
        elif party_slot_006 == trp.taiga_bandit:
            set_background_mesh(mesh.pic_steppe_bandits)
        elif party_slot_006 == trp.mountain_bandit:
            set_background_mesh(mesh.pic_mountain_bandits)
        elif party_slot_006 == trp.sea_raider:
            set_background_mesh(mesh.pic_sea_raiders)
        else:
            set_background_mesh(mesh.pic_bandits)
        #end
    elif party_slot_eq(_current_town,35,2):
        s6 = str_store_string("@ The village has been looted. A handful of souls scatter as you pass through the burnt out houses.")
        if _g_player_raid_complete != 1:
            play_track(track.empty_village,1)
        #end
        set_background_mesh(mesh.pic_looted_village)
    elif party_slot_eq(_current_town,35,1):
        s6 = str_store_string("@ The village is being raided.")
    else:
        party_cur_terrain_008 = party_get_current_terrain(_current_town)
        if party_cur_terrain_008 in party_cur_terrain_008_list1:
            set_background_mesh(mesh.pic_village_s)
        elif party_cur_terrain_008 in party_cur_terrain_008_list2:
            set_background_mesh(mesh.pic_village_w)
        else:
            set_background_mesh(mesh.pic_village_p)
        #end
    #end
    if _g_player_raid_complete == 1:
        _g_player_raid_complete = 0
        jump_to_menu(mnu.village_loot_complete)
    else:
        party_slot_009 = party_get_slot(_current_town,34)
        if party_slot_009 > 0:
            pass
        #end
    #end
    if _g_leave_town == 1:
        _g_leave_town = 0
        change_screen_return()
    #end
    if True:
        cur_time_of_day_010 = store_time_of_day()
        if cur_time_of_day_010 >= 5 and cur_time_of_day_010 < 21:
            _town_nighttime = 0
        else:
            _town_nighttime = 1
        #end
    #end
village.conditionBlock = condition

village_village_manage = MenuOption("village_manage", "Manage this village.")
def code():
    _g_next_menu = mnu.village
    jump_to_menu(mnu.center_manage)
village_village_manage.codeBlock = code

village_recruit_volunteers = MenuOption("recruit_volunteers", "Recruit Volunteers.")
def code():
    if call_script(script.cf_enter_center_location_bandit_check):
        pass
    else:
        jump_to_menu(mnu.recruit_volunteers)
    #end
village_recruit_volunteers.codeBlock = code

village_village_center = MenuOption("village_center", "Go to the village center.") # Door to the village center.
def code():
    if call_script(script.cf_enter_center_location_bandit_check):
        pass
    else:
        party_slot_001 = party_get_slot(_current_town,10)
        modify_visitors_at_site(party_slot_001)
        reset_visitors()
        party_slot_002 = party_get_slot(_current_town,25)
        set_visitor(11,party_slot_002)
        init_town_walkers()
        if check_quest_active(qst.hunt_down_fugitive) and not is_currently_night() and quest_slot_eq(qst.hunt_down_fugitive,1,_current_town) and not check_quest_succeeded(qst.hunt_down_fugitive) and not check_quest_failed(qst.hunt_down_fugitive):
            set_visitor(45,trp.fugitive)
        #end
        set_jump_mission(mt.village_center)
        jump_to_scene(party_slot_001)
        change_screen_mission()
    #end
village_village_center.codeBlock = code

village_village_buy_food = MenuOption("village_buy_food", "Buy supplies from the peasants.")
def code():
    if call_script(script.cf_enter_center_location_bandit_check):
        pass
    else:
        party_slot_001 = party_get_slot(_current_town,25)
        change_screen_trade(party_slot_001)
    #end
village_village_buy_food.codeBlock = code

village_village_attack_bandits = MenuOption("village_attack_bandits", "Attack the bandits.")
def code():
    party_slot_001 = party_get_slot(_current_town,39)
    party_slot_002 = party_get_slot(_current_town,10)
    modify_visitors_at_site(party_slot_002)
    reset_visitors()
    set_visitors(0,party_slot_001,_qst_eliminate_bandits_infesting_village_num_bandits)
    set_visitors(2,trp.farmer,_qst_eliminate_bandits_infesting_village_num_villagers)
    set_party_battle_mode()
    set_battle_advantage(0)
    _g_battle_result = 0
    set_jump_mission(mt.village_attack_bandits)
    jump_to_scene(party_slot_002)
    _g_next_menu = mnu.village_infest_bandits_result
    jump_to_menu(mnu.battle_debrief)
    _g_mt_mode = 1
    change_screen_mission()
village_village_attack_bandits.codeBlock = code

village_village_wait = MenuOption("village_wait", "Wait here for some time.")
def code():
    _auto_enter_town = _current_town
    _g_last_rest_center = _current_town
    if party_is_active(p.main_party):
        party_cur_terrain_001 = party_get_current_terrain(p.main_party)
        if party_cur_terrain_001 == 5:
            unlock_achievement(28)
        #end
    #end
    rest_for_hours_interactive(168,5,1)
    change_screen_return()
village_village_wait.codeBlock = code

village_collect_taxes_qst = MenuOption("collect_taxes_qst", "{reg5?Continue collecting taxes:Collect taxes} due to {s1}.")
def condition():
    if party_slot_eq(_current_town,35,0) and not party_slot_ge(_current_town,39,1) and check_quest_active(qst.collect_taxes):
        quest_slot_001 = quest_get_slot(qst.collect_taxes,6)
        if quest_slot_eq(qst.collect_taxes,1,_current_town) and not quest_slot_eq(qst.collect_taxes,11,4):
            s1 = str_store_troop_name(quest_slot_001)
            reg5 = quest_get_slot(qst.collect_taxes,11)
village_collect_taxes_qst.conditionBlock = condition
def code():
    jump_to_menu(mnu.collect_taxes)
village_collect_taxes_qst.codeBlock = code

village_train_peasants_against_bandits_qst = MenuOption("train_peasants_against_bandits_qst", "Train the peasants.")
def code():
    jump_to_menu(mnu.train_peasants_against_bandits)
village_train_peasants_against_bandits_qst.codeBlock = code

village_village_hostile_action = MenuOption("village_hostile_action", "Take a hostile action.")
def code():
    jump_to_menu(mnu.village_hostile_action)
village_village_hostile_action.codeBlock = code

village_village_reports = MenuOption("village_reports", "{!}CHEAT! Show reports.")
def code():
    jump_to_menu(mnu.center_reports)
village_village_reports.codeBlock = code

village_village_leave = MenuOption("village_leave", "Leave...")
def code():
    change_screen_return(0)
village_village_leave.codeBlock = code



village_hostile_action = GameMenu("village_hostile_action", 0,
"What action do you have in mind?"
)

village_hostile_action_village_take_food = MenuOption("village_take_food", "Force the peasants to give you supplies.")
def condition():
    if party_slot_eq(_current_town,35,0) and not party_slot_ge(_current_town,39,1):
        party_slot_001 = party_get_slot(_current_town,25)
        var002 = 0
        for inventory_slot_no_003 in range(10, 106):
            troop_inv_slot_004 = troop_get_inventory_slot(party_slot_001,inventory_slot_no_003)
            if troop_inv_slot_004 >= 0:
                var002 = 1
            #end
        #end
    #end
village_hostile_action_village_take_food.conditionBlock = condition
def code():
    jump_to_menu(mnu.village_take_food_confirm)
village_hostile_action_village_take_food.codeBlock = code

village_hostile_action_village_steal_cattle = MenuOption("village_steal_cattle", "Steal cattle.")
def condition():
    if party_slot_eq(_current_town,35,0) and party_slot_eq(_current_town,46,0) and not party_slot_ge(_current_town,39,1):
        party_slot_001 = party_get_slot(_current_town,205)
village_hostile_action_village_steal_cattle.conditionBlock = condition
def code():
    jump_to_menu(mnu.village_steal_cattle_confirm)
village_hostile_action_village_steal_cattle.codeBlock = code

village_hostile_action_village_loot = MenuOption("village_loot", "Loot and burn this village.")
def condition():
    if party_slot_eq(_current_town,35,0) and not party_slot_ge(_current_town,39,1):
        party_faction_001 = store_faction_of_party(_current_town)
        faction_relation_002 = store_relation(fac.player_supporters_faction,party_faction_001)
village_hostile_action_village_loot.conditionBlock = condition
def code():
    jump_to_menu(mnu.village_start_attack)
village_hostile_action_village_loot.codeBlock = code

village_hostile_action_forget_it = MenuOption("forget_it", "Forget it.")
def code():
    jump_to_menu(mnu.village)
village_hostile_action_forget_it.codeBlock = code



recruit_volunteers = GameMenu("recruit_volunteers", 0,
"{s18}"
)
def condition():
    party_slot_001 = party_get_slot(_current_town,92)
    party_slot_002 = party_get_slot(_current_town,93)
    party_free_companions_capacity_003 = party_get_free_companions_capacity(p.main_party)
    troop_gold_004 = store_troop_gold(trp.player)
    var005 = troop_gold_004 / 10
    var006 = party_free_companions_capacity_003
    val_min(var006,var005)
    if var006 > 0:
        val_min(party_slot_002,var006)
    #end
    reg5 = party_slot_002
    reg7 = 0
    if party_slot_002 > var005:
        reg7 = 1
    #end
    if party_slot_002 == 0:
        s18 = str_store_string("@No one here seems to be willing to join your party.")
    else:
        reg6 = party_slot_002 * 10
        str_store_troop_name_by_count(s3,party_slot_001,party_slot_002)
        if reg5 == 1:
            s18 = str_store_string("@One {s3} volunteers to follow you.")
        else:
            s18 = str_store_string("@{reg5} {s3} volunteer to follow you.")
        #end
        set_background_mesh(mesh.pic_recruits)
    #end
recruit_volunteers.conditionBlock = condition

recruit_volunteers_continue_not_enough_gold = MenuOption("continue_not_enough_gold", "I don't have enough money...")
def code():
    jump_to_menu(mnu.village)
recruit_volunteers_continue_not_enough_gold.codeBlock = code

recruit_volunteers_continue = MenuOption("continue", "Continue...")
def code():
    party_set_slot(_current_town,93,-1)
    jump_to_menu(mnu.village)
recruit_volunteers_continue.codeBlock = code

recruit_volunteers_recruit_them = MenuOption("recruit_them", "Recruit them ({reg6} denars).")
def code():
    village_recruit_volunteers_recruit()
    jump_to_menu(mnu.village)
recruit_volunteers_recruit_them.codeBlock = code

recruit_volunteers_forget_it = MenuOption("forget_it", "Forget it.")
def code():
    jump_to_menu(mnu.village)
recruit_volunteers_forget_it.codeBlock = code



village_hunt_down_fugitive_defeated = GameMenu("village_hunt_down_fugitive_defeated", 0,
"A heavy blow from the fugitive sends you to the ground, and your vision spins and goes dark. Time passes. When you open your eyes again you find yourself battered and bloody, but luckily none of the wounds appear to be lethal."
)

village_hunt_down_fugitive_defeated_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.village)
village_hunt_down_fugitive_defeated_continue.codeBlock = code



village_infest_bandits_result = GameMenu("village_infest_bandits_result", 4096,
"{s9}"
)
def condition():
    if _g_battle_result == 1:
        jump_to_menu(mnu.village_infestation_removed)
    else:
        s9 = str_store_string("@Try as you might;;; you could not defeat the bandits. Infuriated;;; they raze the village to the ground to punish the peasants;;; and then leave the burning wasteland behind to find greener pastures to plunder.")
        set_background_mesh(mesh.pic_looted_village)
    #end
village_infest_bandits_result.conditionBlock = condition

village_infest_bandits_result_continue = MenuOption("continue", "Continue...")
def code():
    party_set_slot(_g_encountered_party,39,0)
    village_set_state(_current_town,2)
    party_set_slot(_current_town,36,0)
    party_set_slot(_current_town,37,0)
    if check_quest_active(qst.eliminate_bandits_infesting_village) and quest_slot_eq(qst.eliminate_bandits_infesting_village,1,_g_encountered_party):
        change_player_relation_with_center(_g_encountered_party,-5)
        fail_quest(qst.eliminate_bandits_infesting_village)
        end_quest(qst.eliminate_bandits_infesting_village)
    elif check_quest_active(qst.deal_with_bandits_at_lords_village) and quest_slot_eq(qst.deal_with_bandits_at_lords_village,1,_g_encountered_party):
        change_player_relation_with_center(_g_encountered_party,-4)
        fail_quest(qst.deal_with_bandits_at_lords_village)
        end_quest(qst.deal_with_bandits_at_lords_village)
    else:
        change_player_relation_with_center(_g_encountered_party,-3)
    #end
    jump_to_menu(mnu.village)
village_infest_bandits_result_continue.codeBlock = code



village_infestation_removed = GameMenu("village_infestation_removed", 512,
"In a battle worthy of song, you and your men drive the bandits out of the village, making it safe once more. The villagers have little left in the way of wealth after their ordeal, but they offer you all they can find."
)
def condition():
    party_slot_001 = party_get_slot(_g_encountered_party,39)
    party_set_slot(_g_encountered_party,39,0)
    party_clear(p.temp_party)
    party_add_members(p.temp_party,party_slot_001,_qst_eliminate_bandits_infesting_village_num_bandits)
    _g_strength_contribution_of_player = 50
    party_give_xp_and_gold(p.temp_party)
    if check_quest_active(qst.eliminate_bandits_infesting_village) and quest_slot_eq(qst.eliminate_bandits_infesting_village,1,_g_encountered_party):
        end_quest(qst.eliminate_bandits_infesting_village)
        change_player_relation_with_center(_g_encountered_party,5)
    elif check_quest_active(qst.deal_with_bandits_at_lords_village) and quest_slot_eq(qst.deal_with_bandits_at_lords_village,1,_g_encountered_party):
        succeed_quest(qst.deal_with_bandits_at_lords_village)
        change_player_relation_with_center(_g_encountered_party,3)
    else:
        change_player_relation_with_center(_g_encountered_party,4)
    #end
    party_slot_002 = party_get_slot(_current_town,25)
    for inventory_slot_no_003 in range(10, 106):
        random_x_004 = store_random_in_range(0,100)
        if random_x_004 < 70:
            troop_set_inventory_slot(party_slot_002,inventory_slot_no_003,-1)
        #end
    #end
village_infestation_removed.conditionBlock = condition

village_infestation_removed_village_bandits_defeated_accept = MenuOption("village_bandits_defeated_accept", "Take it as your just due.")
def code():
    jump_to_menu(mnu.village)
    party_slot_001 = party_get_slot(_current_town,25)
    troop_sort_inventory(party_slot_001)
    change_screen_loot(party_slot_001)
village_infestation_removed_village_bandits_defeated_accept.codeBlock = code

village_infestation_removed_village_bandits_defeated_cont = MenuOption("village_bandits_defeated_cont", "Refuse, stating that they need these items more than you do.")
def code():
    change_player_relation_with_center(_g_encountered_party,3)
    change_player_honor(1)
    jump_to_menu(mnu.village)
village_infestation_removed_village_bandits_defeated_cont.codeBlock = code



center_manage = GameMenu("center_manage", 0,
"{s19}^{reg6?^^You are currently building {s7}. The building will be completed after {reg8} day{reg9?s:}.:}"
)
def condition():
    var001 = 0
    str_clear(18)
    if party_slot_eq(_g_encountered_party,0,4):
        var002 = 130
        var003 = 135
        s17 = str_store_string("@village")
    else:
        var002 = 134
        var003 = 136
        if party_slot_eq(_g_encountered_party,0,3):
            s17 = str_store_string("@town")
        else:
            s17 = str_store_string("@castle")
        #end
    #end
    for var004 in range(var002, var003):
        if party_slot_ge(_g_encountered_party,var004,1):
            var001 += 1
            get_improvement_details(var004)
            if var001 == 1:
                s18 = str_store_string("@{!}{s0}")
            else:
                s18 = str_store_string("@{!}{s18}, {s0}")
            #end
        #end
    #end
    if var001 == 0:
        s19 = str_store_string("@The {s17} has no improvements.")
    else:
        s19 = str_store_string("@The {s17} has the following improvements:{s18}.")
    #end
    reg6 = 0
    if True:
        party_slot_005 = party_get_slot(_g_encountered_party,124)
        if party_slot_005 > 0:
            get_improvement_details(party_slot_005)
            s7 = str_store_string(0)
            reg6 = 1
            cur_hours_006 = store_current_hours()
            party_slot_007 = party_get_slot(_g_encountered_party,125)
            party_slot_007 -= cur_hours_006
            reg8 = party_slot_007 / 24
            val_max(reg8,1)
            reg9 = reg8 - 1
        #end
    #end
center_manage.conditionBlock = condition

center_manage_center_build_manor = MenuOption("center_build_manor", "Build a manor.")
def code():
    _g_improvement_type = 130
    jump_to_menu(mnu.center_improve)
center_manage_center_build_manor.codeBlock = code

center_manage_center_build_fish_pond = MenuOption("center_build_fish_pond", "Build a mill.")
def code():
    _g_improvement_type = 131
    jump_to_menu(mnu.center_improve)
center_manage_center_build_fish_pond.codeBlock = code

center_manage_center_build_watch_tower = MenuOption("center_build_watch_tower", "Build a watch tower.")
def code():
    _g_improvement_type = 132
    jump_to_menu(mnu.center_improve)
center_manage_center_build_watch_tower.codeBlock = code

center_manage_center_build_school = MenuOption("center_build_school", "Build a school.")
def code():
    _g_improvement_type = 133
    jump_to_menu(mnu.center_improve)
center_manage_center_build_school.codeBlock = code

center_manage_center_build_messenger_post = MenuOption("center_build_messenger_post", "Build a messenger post.")
def code():
    _g_improvement_type = 134
    jump_to_menu(mnu.center_improve)
center_manage_center_build_messenger_post.codeBlock = code

center_manage_center_build_prisoner_tower = MenuOption("center_build_prisoner_tower", "Build a prisoner tower.")
def code():
    _g_improvement_type = 135
    jump_to_menu(mnu.center_improve)
center_manage_center_build_prisoner_tower.codeBlock = code

center_manage_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    jump_to_menu(_g_next_menu)
center_manage_go_back_dot.codeBlock = code



center_improve = GameMenu("center_improve", 0,
"{s19} As the party member with the highest engineer skill ({reg2}), {reg3?you reckon:{s3} reckons} that building the {s4} will cost you {reg5} denars and will take {reg6} days."
)
def condition():
    get_improvement_details(_g_improvement_type)
    var001 = reg0
    s4 = str_store_string(0)
    s19 = str_store_string(1)
    get_max_skill_of_player_party(skl.engineer)
    var002 = reg0
    var003 = reg1
    reg2 = var002
    var004 = 20 - var002
    var001 *= var004
    var001 /= 20
    var005 = var001 / 100
    var005 += 3
    reg5 = var001
    reg6 = var005
    if var003 == trp.player:
        reg3 = 1
    else:
        reg3 = 0
        s3 = str_store_troop_name(var003)
    #end
center_improve.conditionBlock = condition

center_improve_improve_cont = MenuOption("improve_cont", "Go on.")
def condition():
    troop_gold_001 = store_troop_gold(trp.player)
center_improve_improve_cont.conditionBlock = condition
def code():
    troop_remove_gold(trp.player,reg5)
    party_set_slot(_g_encountered_party,124,_g_improvement_type)
    cur_hours_001 = store_current_hours()
    var002 = reg6 * 24
    var002 += cur_hours_001
    party_set_slot(_g_encountered_party,125,var002)
    jump_to_menu(mnu.center_manage)
center_improve_improve_cont.codeBlock = code

center_improve_forget_it = MenuOption("forget_it", "Forget it.")
def condition():
    troop_gold_001 = store_troop_gold(trp.player)
center_improve_forget_it.conditionBlock = condition
def code():
    jump_to_menu(mnu.center_manage)
center_improve_forget_it.codeBlock = code

center_improve_improve_not_enough_gold = MenuOption("improve_not_enough_gold", "I don't have enough money for that.")
def condition():
    troop_gold_001 = store_troop_gold(trp.player)
center_improve_improve_not_enough_gold.conditionBlock = condition
def code():
    jump_to_menu(mnu.center_manage)
center_improve_improve_not_enough_gold.codeBlock = code



town_bandits_failed = GameMenu("town_bandits_failed", 512,
"{s4} {s5}"
)
def condition():
    troop_gold_001 = store_troop_gold(trp.player)
    gold_002 = troop_gold_001 / 30
    random_x_003 = store_random_in_range(40,100)
    gold_002 += random_x_003
    val_min(gold_002,troop_gold_001)
    troop_remove_gold(trp.player,gold_002)
    party_set_slot(_current_town,155,0)
    party_num_companions_004 = party_get_num_companions(p.main_party)
    s4 = str_store_string("@The assasins beat you down and leave you for dead. .")
    s4 = str_store_string("@You have fallen. The bandits quickly search your body for every coin they can find;;; then vanish into the night. They have left you alive;;; if only barely.")
    if party_num_companions_004 > 2:
        s5 = str_store_string("@Luckily some of your companions come to search for you when you do not return;;; and find you lying by the side of the road. They hurry you to safety and dress your wounds.")
    else:
        s5 = str_store_string("@Luckily some passing townspeople find you lying by the side of the road;;; and recognise you as something other than a simple beggar. They carry you to the nearest inn and dress your wounds.")
    #end
town_bandits_failed.conditionBlock = condition

town_bandits_failed_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
town_bandits_failed_continue.codeBlock = code



town_bandits_succeeded = GameMenu("town_bandits_succeeded", 512,
"The bandits fall before you as wheat to a scythe! Soon you stand alone in the streets while most of your attackers lie unconscious, dead or dying. Searching the bodies, you find a purse which must have belonged to a previous victim of these brutes. Or perhaps, it was given to them by someone who wanted to arrange a suitable ending to your life."
)
def condition():
    party_set_slot(_current_town,155,0)
    _g_last_defeated_bandits_town = _g_encountered_party
    if check_quest_active(qst.deal_with_night_bandits) and not check_quest_succeeded(qst.deal_with_night_bandits) and quest_slot_eq(qst.deal_with_night_bandits,1,_g_encountered_party):
        succeed_quest(qst.deal_with_night_bandits)
    #end
    var001 = _num_center_bandits * 117
    add_xp_to_troop(var001,trp.player)
    var002 = _num_center_bandits * 50
    troop_add_gold(trp.player,var002)
town_bandits_succeeded.conditionBlock = condition

town_bandits_succeeded_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
town_bandits_succeeded_continue.codeBlock = code



village_steal_cattle_confirm = GameMenu("village_steal_cattle_confirm", 0,
"As the party member with the highest looting skill ({reg2}), {reg3?you reckon:{s1} reckons} that you can steal as many as {reg4} heads of village's cattle."
)
def condition():
    get_max_skill_of_player_party(skl.looting)
    reg2 = reg0
    var001 = reg1
    if var001 == trp.player:
        reg3 = 1
    else:
        reg3 = 0
        s1 = str_store_troop_name(var001)
    #end
    calculate_amount_of_cattle_can_be_stolen(_current_town)
    reg4 = reg0
village_steal_cattle_confirm.conditionBlock = condition

village_steal_cattle_confirm_village_steal_cattle_confirm = MenuOption("village_steal_cattle_confirm", "Go on.")
def code():
    rest_for_hours_interactive(3,5,1)
    _auto_menu = mnu.village_steal_cattle
    change_screen_return()
village_steal_cattle_confirm_village_steal_cattle_confirm.codeBlock = code

village_steal_cattle_confirm_forget_it = MenuOption("forget_it", "Forget it.")
def code():
    change_screen_return()
village_steal_cattle_confirm_forget_it.codeBlock = code



village_steal_cattle = GameMenu("village_steal_cattle", 512,
"{s1}"
)
def condition():
    calculate_amount_of_cattle_can_be_stolen(_current_town)
    var001 = reg0
    var001 += 1
    random_x_002 = store_random_in_range(0,var001)
    party_set_slot(_current_town,46,1)
    party_slot_003 = party_get_slot(_current_town,7)
    if random_x_002 <= 0:
        change_player_relation_with_center(_current_town,-3)
        s1 = str_store_string("@You fail to steal any cattle.")
    else:
        reg17 = random_x_002
        reg12 = random_x_002 - 1
        if party_slot_003 > 0:
            change_player_relation_with_troop(party_slot_003,-3)
            add_log_entry(66,trp.player,_current_town,party_slot_003,_g_encountered_x_party_faction)
        #end
        change_player_relation_with_center(_current_town,-5)
        s1 = str_store_string("@You drive away {reg17} {reg12?heads:head} of cattle from the village's herd.")
        if random_x_002 == 3:
            unlock_achievement(31)
        #end
        create_cattle_herd(_current_town,random_x_002)
        party_slot_004 = party_get_slot(_current_town,205)
        party_slot_004 -= random_x_002
        party_set_slot(_current_town,205,party_slot_004)
    #end
village_steal_cattle.conditionBlock = condition

village_steal_cattle_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
village_steal_cattle_continue.codeBlock = code



village_take_food_confirm = GameMenu("village_take_food_confirm", 0,
"It will be difficult to force and threaten the peasants into giving their precious supplies. You think you will need at least one hour."
)

village_take_food_confirm_village_take_food_confirm = MenuOption("village_take_food_confirm", "Go ahead.")
def code():
    rest_for_hours_interactive(1,5,0)
    _auto_enter_town = _current_town
    _g_town_visit_after_rest = 1
    _auto_enter_in_center = mnu.village_take_food
    change_screen_return()
village_take_food_confirm_village_take_food_confirm.codeBlock = code

village_take_food_confirm_forget_it = MenuOption("forget_it", "Forget it.")
def code():
    jump_to_menu(mnu.village_hostile_action)
village_take_food_confirm_forget_it.codeBlock = code



village_take_food = GameMenu("village_take_food", 0,
"The villagers grudgingly bring out what they have for you."
)
def condition():
    party_count_members_with_full_health(p.main_party)
    var001 = reg0
    party_count_members_with_full_health(_current_town)
    var002 = reg0
    if var001 < 6 and var002 >= 40 and not party_slot_eq(_current_town,7,trp.player):
        jump_to_menu(mnu.village_start_attack)
    #end
village_take_food.conditionBlock = condition

village_take_food_take_supplies = MenuOption("take_supplies", "Take the supplies.")
def code():
    if party_slot_ge(_current_town,26,-55):
        if party_slot_eq(_current_town,7,trp.player):
            change_player_relation_with_center(_current_town,-1)
        else:
            change_player_relation_with_center(_current_town,-3)
        #end
    #end
    party_slot_001 = party_get_slot(_current_town,7)
    if party_slot_001 > 1:
        change_player_relation_with_troop(party_slot_001,-1)
    #end
    party_slot_002 = party_get_slot(_current_town,25)
    party_skill_lvl_003 = party_get_skill_level(p.main_party,skl.looting)
    party_skill_lvl_003 *= 3
    var004 = 70 - party_skill_lvl_003
    for inventory_slot_no_005 in range(10, 106):
        random_x_006 = store_random_in_range(0,100)
        if random_x_006 < var004:
            troop_set_inventory_slot(party_slot_002,inventory_slot_no_005,-1)
        #end
    #end
    objectionable_action(3,gstr.steal_from_villagers)
    add_log_entry(2,trp.player,_current_town,-1,-1)
    party_faction_007 = store_faction_of_party(_current_town)
    faction_inflict_war_damage_on_faction(_players_kingdom,party_faction_007,5)
    jump_to_menu(mnu.village)
    troop_sort_inventory(party_slot_002)
    change_screen_loot(party_slot_002)
village_take_food_take_supplies.codeBlock = code

village_take_food_let_them_keep_it = MenuOption("let_them_keep_it", "Let them keep it.")
def code():
    jump_to_menu(mnu.village)
village_take_food_let_them_keep_it.codeBlock = code



village_start_attack = GameMenu("village_start_attack", 4608,
"Some of the angry villagers grab their tools and prepare to resist you. It looks like you'll have a fight on your hands if you continue."
)
def condition():
    set_background_mesh(mesh.pic_villageriot)
    party_count_members_with_full_health(p.main_party)
    var001 = reg0
    party_count_members_with_full_health(_current_town)
    var002 = reg0
    if var001 > 25:
        jump_to_menu(mnu.village_loot_no_resist)
    elif var002 == 0 or _g_battle_result == 1:
        if _g_battle_result == 1:
            random_x_003 = store_random_in_range(-30,-15)
            change_player_relation_with_center(_current_town,random_x_003)
            party_slot_004 = party_get_slot(_current_town,7)
            if party_slot_004 > 0:
                change_player_relation_with_troop(party_slot_004,-3)
            #end
        #end
        jump_to_menu(mnu.village_loot_no_resist)
    elif _g_battle_result == -1:
        jump_to_menu(mnu.village_loot_defeat)
    #end
village_start_attack.conditionBlock = condition

village_start_attack_village_raid_attack = MenuOption("village_raid_attack", "Charge them.")
def code():
    random_x_001 = store_random_in_range(-10,-5)
    change_player_relation_with_center(_current_town,random_x_001)
    if True:
        party_slot_002 = party_get_slot(_current_town,7)
        if party_slot_002 > 0:
            change_player_relation_with_troop(party_slot_002,-3)
        #end
    #end
    calculate_battle_advantage()
    set_battle_advantage(reg0)
    set_party_battle_mode()
    _g_battle_result = 0
    _g_village_raid_evil = 1
    set_jump_mission(mt.village_raid)
    party_slot_003 = party_get_slot(_current_town,10)
    jump_to_scene(party_slot_003)
    _g_next_menu = mnu.village_start_attack
    diplomacy_party_attacks_neutral(p.main_party,_g_encountered_party)
    objectionable_action(3,gstr.loot_village)
    jump_to_menu(mnu.battle_debrief)
    change_screen_mission()
village_start_attack_village_raid_attack.codeBlock = code

village_start_attack_village_raid_leave = MenuOption("village_raid_leave", "Leave this village alone.")
def code():
    change_screen_return()
village_start_attack_village_raid_leave.codeBlock = code



village_loot_no_resist = GameMenu("village_loot_no_resist", 0,
"The villagers here are few and frightened, and they quickly scatter and run before you. The village is at your mercy."
)

village_loot_no_resist_village_loot = MenuOption("village_loot", "Plunder the village, then raze it.")
def code():
    village_set_state(_current_town,1)
    party_set_slot(_current_town,34,p.main_party)
    _g_player_raiding_village = _current_town
    if True:
        party_faction_001 = store_faction_of_party(_current_town)
        faction_relation_002 = store_relation(_players_kingdom,party_faction_001)
        if faction_relation_002 >= 0:
            diplomacy_party_attacks_neutral(p.main_party,_current_town)
        #end
    #end
    rest_for_hours(3,5,1)
    change_screen_return()
village_loot_no_resist_village_loot.codeBlock = code

village_loot_no_resist_village_raid_leave = MenuOption("village_raid_leave", "Leave this village alone.")
def code():
    change_screen_return()
village_loot_no_resist_village_raid_leave.codeBlock = code



village_loot_complete = GameMenu("village_loot_complete", 512,
"On your orders your troops sack the village, pillaging everything of any value, and then put the buildings to the torch. From the coins and valuables that are found, you get your share of {reg1} denars."
)
def condition():
    var001 = get_achievement_stat(30,0)
    var002 = get_achievement_stat(30,1)
    var001 += 1
    set_achievement_stat(30,0,var001)
    if var001 >= 3 and var002 >= 3:
        unlock_achievement(30)
    #end
    party_slot_003 = party_get_slot(_current_town,7)
    if party_slot_003 > 0:
        change_player_relation_with_troop(party_slot_003,-5)
    #end
    random_x_004 = store_random_in_range(-35,-25)
    change_player_relation_with_center(_current_town,random_x_004)
    party_faction_005 = store_faction_of_party(_current_town)
    faction_relation_006 = store_relation(party_faction_005,fac.player_supporters_faction)
    if faction_relation_006 < 0:
        change_player_relation_with_faction(party_faction_005,-3)
    #end
    var007 = 50
    party_slot_008 = party_get_slot(_current_town,50)
    var009 = party_slot_008 * 5
    var007 += var009
    troop_add_gold(trp.player,var007)
    var010 = 3
    var011 = var007 / 100
    var010 += var011
    change_player_party_morale(var010)
    faction_slot_012 = faction_get_slot(party_faction_005,99)
    var013 = var010 * 200
    faction_slot_012 -= var013
    faction_set_slot(party_faction_005,99,faction_slot_012)
    objectionable_action(3,gstr.loot_village)
    reg1 = var007
village_loot_complete.conditionBlock = condition

village_loot_complete_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.close)
    calculate_amount_of_cattle_can_be_stolen(_current_town)
    var001 = reg0
    var001 *= 3
    var001 /= 2
    party_slot_002 = party_get_slot(_current_town,205)
    val_min(var001,party_slot_002)
    var001 += 1
    random_x_003 = store_random_in_range(0,var001)
    if random_x_003 > 0:
        create_cattle_herd(_current_town,random_x_003)
        party_slot_002 -= random_x_003
        party_set_slot(_current_town,205,party_slot_002)
    #end
    troop_clear_inventory(trp.temp_troop)
    party_slot_004 = party_get_slot(120,_current_town)
    var005 = 250 - itm.spice
    reset_item_probabilities(100)
    var006 = 0
    for itm_007 in range(itm.spice, itm.siege_supply):
        slot_no_008 = itm_007 + var005
        party_slot_009 = party_get_slot(party_slot_004,slot_no_008)
        center_get_production(party_slot_004,itm_007)
        item_probability_010 = reg0
        center_get_consumption(party_slot_004,itm_007)
        reg0 /= 3
        item_probability_010 += reg0
        item_probability_010 *= 4
        item_probability_010 *= 1000
        item_probability_010 /= party_slot_009
        var006 += item_probability_010
    #end
    for itm_007 in range(itm.spice, itm.siege_supply):
        slot_no_008 = itm_007 + var005
        party_slot_009 = party_get_slot(party_slot_004,slot_no_008)
        center_get_production(party_slot_004,itm_007)
        item_probability_010 = reg0
        center_get_consumption(party_slot_004,itm_007)
        reg0 /= 3
        item_probability_010 += reg0
        item_probability_010 *= 4
        item_probability_010 *= 1000
        item_probability_010 /= party_slot_009
        item_probability_010 *= 40
        item_probability_010 *= 100
        item_probability_010 /= var006
        set_item_probability_in_merchandise(itm_007,item_probability_010)
    #end
    troop_add_merchandise(trp.temp_troop,11,30)
    troop_sort_inventory(trp.temp_troop)
    change_screen_loot(trp.temp_troop)
village_loot_complete_continue.codeBlock = code



village_loot_defeat = GameMenu("village_loot_defeat", 4096,
"Fighting with courage and determination, the villagers manage to hold together and drive off your forces."
)
def condition():
    set_background_mesh(mesh.pic_villageriot)
village_loot_defeat.conditionBlock = condition

village_loot_defeat_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
village_loot_defeat_continue.codeBlock = code



village_loot_continue = GameMenu("village_loot_continue", 0,
"Do you wish to continue looting this village?"
)

village_loot_continue_disembark_yes = MenuOption("disembark_yes", "Yes.")
def code():
    rest_for_hours(3,5,1)
    change_screen_return()
village_loot_continue_disembark_yes.codeBlock = code

village_loot_continue_disembark_no = MenuOption("disembark_no", "No.")
def code():
    village_set_state(_current_town,0)
    party_set_slot(_current_town,34,-1)
    _g_player_raiding_village = 0
    change_screen_return()
village_loot_continue_disembark_no.codeBlock = code



close = GameMenu("close", 0,
"Nothing."
)
def condition():
    change_screen_return()
close.conditionBlock = condition



town = GameMenu("town", 4352,
"{s10} {s14}^{s11}{s12}{s13}"
)
def condition():
    if _sneaked_into_town == 1:
        music_set_situation_with_culture(16384)
    else:
        music_set_situation_with_culture(65536)
    #end
    _current_town = store_encountered_party()
    update_center_recon_notes(_current_town)
    _g_defending_against_siege = 0
    str_clear(3)
    party_battle_opponent_001 = party_get_battle_opponent(_current_town)
    party_faction_002 = store_faction_of_party(_g_encountered_party)
    faction_relation_003 = store_relation(party_faction_002,fac.player_supporters_faction)
    if party_battle_opponent_001 > 0 and faction_relation_003 >= 0:
        party_faction_004 = store_faction_of_party(party_battle_opponent_001)
        faction_relation_005 = store_relation(party_faction_004,fac.player_supporters_faction)
        if faction_relation_005 < 0:
            _g_defending_against_siege = 1
            _g_siege_first_encounter = 1
            jump_to_menu(mnu.siege_started_defender)
        #end
    #end
    if is_between(_g_encountered_party,p.town_1,p.castle_1):
        var006 = _g_encountered_party - p.town_1
        set_achievement_stat(26,var006,1)
        var007 = 0
        for p_008 in range(p.town_1, p.castle_1):
            var006 = p_008 - p.town_1
            var009 = get_achievement_stat(26,var006)
            if var009 == 0:
                var007 = 1
            #end
        #end
        if var007 == 0:
            unlock_achievement(26)
        #end
    #end
    _qst_collect_taxes_currently_collecting = 0
    if _quest_auto_menu > 0:
        jump_to_menu(_quest_auto_menu)
        _quest_auto_menu = 0
    #end
    if _g_town_assess_trade_goods_after_rest == 1:
        _g_town_assess_trade_goods_after_rest = 0
        jump_to_menu(mnu.town_trade_assessment)
    #end
    _talk_context = 0
    _all_doors_locked = 0
    if _g_town_visit_after_rest == 1:
        _g_town_visit_after_rest = 0
        _town_entered = 1
    #end
    if _g_leave_town == 1:
        _g_leave_town = 0
        _g_permitted_to_center = 0
        leave_encounter()
        change_screen_return()
    #end
    s2 = str_store_party_name(_current_town)
    party_slot_010 = party_get_slot(_current_town,7)
    party_faction_011 = store_faction_of_party(_current_town)
    s9 = str_store_faction_name(party_faction_011)
    if party_slot_010 >= 0:
        s8 = str_store_troop_name(party_slot_010)
        s7 = str_store_string("@{s8} of {s9}")
    #end
    if party_slot_eq(_current_town,0,3):
        s60 = str_store_string(2)
        party_slot_012 = party_get_slot(_current_town,50)
        if _cheat_mode >= 1:
            reg4 = party_slot_012
            print("@{!}DEBUG -- Prosperity: {reg4}")
        #end
        var013 = party_slot_012 / 10
        val_min(var013,9)
        var013 += gstr.town_prosperity_0
        s10 = str_store_string(var013)
        var013 = party_slot_012 / 20
        val_min(var013,4)
        var013 += gstr.town_alt_prosperity_0
        s14 = str_store_string(var013)
    else:
        str_clear(14)
        s10 = str_store_string("@You are at {s2}.")
    #end
    if party_slot_eq(_current_town,0,2):
        if party_slot_010 == trp.player:
            s11 = str_store_string("@ Your own banner flies over the castle gate.")
        elif party_slot_010 > -1 and troop_slot_eq(party_slot_010,30,trp.player):
            s11 = str_store_string(gstr._you_see_the_banner_of_your_wifehusband_s7_over_the_castle_gate)
        elif party_slot_010 >= 0:
            s11 = str_store_string("@ You see the banner of {s7} over the castle gate.")
        else:
            s11 = str_store_string("@ This castle has no garrison.")
        #end
    else:
        if party_slot_010 == trp.player:
            s11 = str_store_string("@ Your own banner flies over the town gates.")
        elif party_slot_010 > -1 and troop_slot_eq(party_slot_010,30,trp.player):
            s11 = str_store_string(gstr._the_banner_of_your_wifehusband_s7_flies_over_the_town_gates)
        elif party_slot_010 >= 0:
            s11 = str_store_string("@ You see the banner of {s7} over the town gates.")
        else:
            s11 = str_store_string("@ This town has no garrison.")
        #end
    #end
    str_clear(12)
    if party_slot_eq(_current_town,0,3):
        party_slot_014 = party_get_slot(_current_town,26)
        describe_center_relation_to_s3(party_slot_014)
        reg9 = party_slot_014
        s12 = str_store_string("@{!} {s3} [[[{reg9}]]].")
    #end
    str_clear(13)
    if _entry_to_town_forbidden > 0:
        s13 = str_store_string("@ You have successfully sneaked in.")
    elif faction_slot_eq(party_faction_011,4,6) and faction_slot_eq(party_faction_011,5,_current_town):
        s13 = str_store_string(gstr._the_lord_is_currently_holding_a_feast_in_his_hall)
    #end
    if True:
        reg12 = store_time_of_day()
        if reg12 >= 5 and reg12 < 21:
            _town_nighttime = 0
        else:
            _town_nighttime = 1
            if party_slot_eq(_current_town,0,3):
                s13 = str_store_string(gstr.town_nighttime)
            #end
        #end
    #end
    if party_slot_ge(_current_town,156,1) and not is_currently_night():
        party_set_slot(_current_town,156,1)
        s13 = str_store_string("@{s13} A tournament will be held here soon.")
    #end
    _castle_undefended = 0
    party_num_companions_015 = party_get_num_companions(p.collective_enemy)
    if party_num_companions_015 == 0:
        _castle_undefended = 1
    #end
    set_town_picture()
town.conditionBlock = condition

town_castle_castle = MenuOption("castle_castle", "Go to the Lord's hall{s1}.") # Door to the castle.
def condition():
    if party_slot_eq(_current_town,0,2) and _sneaked_into_town == 0:
        str_clear(1)
        if True:
            party_faction_001 = store_faction_of_party(_current_town)
            if faction_slot_eq(party_faction_001,4,6) and faction_slot_eq(party_faction_001,5,_current_town):
                s1 = str_store_string(gstr._join_the_feast)
            #end
        #end
    #end
town_castle_castle.conditionBlock = condition
def code():
    if _all_doors_locked == 1 or _sneaked_into_town == 1:
        print(gstr.door_locked,4294945450)
    elif _players_kingdom == _g_encountered_x_party_faction or not troop_slot_ge(trp.player,7,50) and not troop_slot_ge(trp.player,7,125) and _g_player_eligible_feast_center_no != _current_town and faction_slot_eq(_g_encountered_x_party_faction,4,6) and faction_slot_eq(_g_encountered_x_party_faction,5,_g_encountered_party) and not check_quest_active(qst.wed_betrothed) and not check_quest_active(qst.wed_betrothed_female) and not troop_slot_ge(trp.player,30,trp.npc1):
        jump_to_menu(mnu.cannot_enter_court)
    else:
        _town_entered = 1
        enter_court(_current_town)
    #end
town_castle_castle.codeBlock = code

town_join_tournament = MenuOption("join_tournament", "Join the tournament.")
def code():
    fill_tournament_participants_troop(_current_town,1)
    _g_tournament_cur_tier = 0
    _g_tournament_player_team_won = -1
    _g_tournament_bet_placed = 0
    _g_tournament_bet_win_amount = 0
    _g_tournament_last_bet_tier = -1
    _g_tournament_next_num_teams = 0
    _g_tournament_next_team_size = 0
    jump_to_menu(mnu.town_tournament)
town_join_tournament.codeBlock = code

town_town_castle = MenuOption("town_castle", "Go to the castle{s1}.") # Door to the castle.
def condition():
    if party_slot_eq(_current_town,0,3) and _entry_to_town_forbidden == 0:
        str_clear(1)
        if True:
            party_faction_001 = store_faction_of_party(_current_town)
            if faction_slot_eq(party_faction_001,4,6) and faction_slot_eq(party_faction_001,5,_current_town):
                s1 = str_store_string(gstr._join_the_feast)
            #end
        #end
    #end
town_town_castle.conditionBlock = condition
def code():
    if _all_doors_locked == 1 or _sneaked_into_town == 1:
        print(gstr.door_locked,4294945450)
    elif _players_kingdom == _g_encountered_x_party_faction or not troop_slot_ge(trp.player,7,50) and not troop_slot_ge(trp.player,7,125) and _g_player_eligible_feast_center_no != _current_town and faction_slot_eq(_g_encountered_x_party_faction,4,6) and faction_slot_eq(_g_encountered_x_party_faction,5,_g_encountered_party) and not check_quest_active(qst.wed_betrothed) and not check_quest_active(qst.wed_betrothed_female) and not troop_slot_ge(trp.player,30,trp.npc1):
        jump_to_menu(mnu.cannot_enter_court)
    else:
        _town_entered = 1
        enter_court(_current_town)
    #end
town_town_castle.codeBlock = code

town_town_center = MenuOption("town_center", "Take a walk around the streets.") # Door to the town center.
def code():
    if _talk_context == 18:
        _talk_context = 19
        _g_mt_mode = 3
        party_faction_001 = store_faction_of_party(_current_town)
        faction_slot_002 = faction_get_slot(party_faction_001,43)
        faction_slot_003 = faction_get_slot(party_faction_001,43)
        faction_slot_004 = faction_get_slot(party_faction_001,44)
        party_slot_005 = party_get_slot(_current_town,10)
        modify_visitors_at_site(party_slot_005)
        reset_visitors()
        if True:
            party_slot_006 = party_get_slot(_current_town,240)
            cur_hours_007 = store_current_hours()
            var008 = party_slot_006 + 4
            if not is_between(cur_hours_007,party_slot_006,var008):
                cur_time_of_day_009 = store_time_of_day()
                if cur_time_of_day_009 >= 6 and cur_time_of_day_009 < 22:
                    set_visitors(25,faction_slot_002,2)
                    set_visitors(26,faction_slot_002,1)
                    set_visitors(27,faction_slot_003,2)
                    set_visitors(28,faction_slot_004,1)
                else:
                    set_visitors(25,faction_slot_002,1)
                    set_visitors(26,faction_slot_002,1)
                    set_visitors(27,faction_slot_003,1)
                    set_visitors(28,faction_slot_004,1)
                #end
            #end
        else:
            cur_time_of_day_009 = store_time_of_day()
            if cur_time_of_day_009 >= 6 and cur_time_of_day_009 < 22:
                set_visitors(25,faction_slot_002,1)
                set_visitors(26,faction_slot_002,0)
                set_visitors(27,faction_slot_003,1)
                set_visitors(28,faction_slot_004,0)
            else:
                set_visitors(25,faction_slot_002,1)
                set_visitors(26,faction_slot_002,0)
                set_visitors(27,faction_slot_003,0)
                set_visitors(28,faction_slot_004,0)
            #end
        #end
        set_jump_mission(mt.town_center)
        jump_to_scene(party_slot_005)
        change_screen_mission()
    else:
        _talk_context = 0
        if call_script(script.cf_enter_center_location_bandit_check):
            pass
        else:
            party_slot_005 = party_get_slot(_current_town,10)
            modify_visitors_at_site(party_slot_005)
            reset_visitors()
            _g_mt_mode = 0
            party_faction_001 = store_faction_of_party(_current_town)
            if party_faction_001 != fac.player_supporters_faction:
                faction_slot_010 = faction_get_slot(_g_encountered_x_party_faction,51)
                faction_slot_011 = faction_get_slot(_g_encountered_x_party_faction,52)
                faction_slot_002 = faction_get_slot(party_faction_001,42)
                faction_slot_003 = faction_get_slot(party_faction_001,43)
            else:
                party_slot_012 = party_get_slot(_current_town,61)
                faction_slot_010 = faction_get_slot(party_slot_012,51)
                faction_slot_011 = faction_get_slot(party_slot_012,52)
                faction_slot_002 = faction_get_slot(party_slot_012,42)
                faction_slot_003 = faction_get_slot(party_slot_012,43)
            #end
        #end
        if True:
            party_slot_006 = party_get_slot(_current_town,240)
            cur_hours_007 = store_current_hours()
            var008 = party_slot_006 + 4
            if not is_between(cur_hours_007,party_slot_006,var008):
                set_visitor(23,faction_slot_011)
            #end
        #end
        set_visitor(24,faction_slot_010)
        if faction_slot_002 > 0:
            reg0 = faction_slot_003
            reg1 = faction_slot_003
            reg2 = faction_slot_002
            reg3 = faction_slot_002
        else:
            reg0 = trp.vaegir_infantry
            reg1 = trp.vaegir_infantry
            reg2 = trp.vaegir_archer
            reg3 = trp.vaegir_footman
        #end
        shuffle_range(0,4)
        if True:
            party_slot_006 = party_get_slot(_current_town,240)
            cur_hours_007 = store_current_hours()
            var008 = party_slot_006 + 4
            if not is_between(cur_hours_007,party_slot_006,var008):
                set_visitor(25,reg0)
                set_visitor(26,reg1)
                set_visitor(27,reg2)
                set_visitor(28,reg3)
            #end
        #end
        party_slot_013 = party_get_slot(_current_town,22)
        set_visitor(9,party_slot_013)
        party_slot_013 = party_get_slot(_current_town,21)
        set_visitor(10,party_slot_013)
        party_slot_013 = party_get_slot(_current_town,25)
        set_visitor(11,party_slot_013)
        party_slot_013 = party_get_slot(_current_town,24)
        set_visitor(12,party_slot_013)
        init_town_walkers()
        set_jump_mission(mt.town_center)
        var014 = 256
        if _sneaked_into_town == 1:
            var014 = 447
        #end
        mission_tpl_entry_set_override_flags(mt.town_center,0,var014)
        mission_tpl_entry_set_override_flags(mt.town_center,2,var014)
        mission_tpl_entry_set_override_flags(mt.town_center,3,var014)
        mission_tpl_entry_set_override_flags(mt.town_center,4,var014)
        mission_tpl_entry_set_override_flags(mt.town_center,5,var014)
        mission_tpl_entry_set_override_flags(mt.town_center,6,var014)
        mission_tpl_entry_set_override_flags(mt.town_center,7,var014)
        if _town_entered == 0:
            _town_entered = 1
            if _town_nighttime == 0:
                set_jump_entry(1)
            #end
        #end
        jump_to_scene(party_slot_005)
        change_screen_mission()
    #end
town_town_center.codeBlock = code

town_town_tavern = MenuOption("town_tavern", "Visit the tavern.") # Door to the tavern.
def code():
    if _all_doors_locked == 1:
        print(gstr.door_locked,4294945450)
    elif cf_enter_center_location_bandit_check():
        pass
    else:
        _town_entered = 1
        set_jump_mission(mt.town_default)
        mission_tpl_entry_set_override_flags(mt.town_default,0,256)
        if _sneaked_into_town == 1:
            mission_tpl_entry_set_override_flags(mt.town_default,0,447)
        #end
        party_slot_001 = party_get_slot(_current_town,13)
        jump_to_scene(party_slot_001)
        scene_set_slot(party_slot_001,0,1)
        _talk_context = 14
        initialize_tavern_variables()
        random_x_002 = store_random_in_range(0,4)
        modify_visitors_at_site(party_slot_001)
        reset_visitors()
        entry_no_003 = 17
        if _cheat_mode == 1:
            troop_slot_004 = troop_get_slot(trp.belligerent_drunk,12)
            if _cheat_mode == 0:
                pass
            elif is_between(troop_slot_004,p.town_1,p.salt_mine):
                s4 = str_store_party_name(troop_slot_004)
                print(gstr.belligerent_drunk_in_s4)
            else:
                print(gstr.belligerent_drunk_not_found)
            #end
            troop_slot_005 = troop_get_slot(trp.fight_promoter,12)
            if _cheat_mode == 0:
                pass
            elif is_between(troop_slot_005,p.town_1,p.salt_mine):
                s4 = str_store_party_name(troop_slot_005)
                print(gstr.roughlooking_character_in_s4)
            else:
                print(gstr.roughlooking_character_not_found)
            #end
        #end
        if True:
            cur_hours_006 = store_current_hours()
            var007 = cur_hours_006 - _g_last_assassination_attempt_time
            if var007 > 168:
                for trp_008 in range(trp.npc1, trp.knight_1_1_wife):
                    if troop_slot_eq(trp_008,52,5):
                        troop_slot_009 = troop_get_slot(trp_008,10)
                        if party_is_active(troop_slot_009):
                            party_attached_010 = party_get_attached_to(troop_slot_009)
                            if party_attached_010 == _g_encountered_party:
                                troop_get_relation_with_troop(trp.player,trp_008)
                                if reg0 < -20:
                                    _g_last_assassination_attempt_time = cur_hours_006
                                    troop_set_slot(trp.hired_assassin,12,_g_encountered_party)
                                #end
                            #end
                        #end
                    #end
                #end
            #end
        #end
        if random_x_002 == 0:
            setup_tavern_attacker(entry_no_003)
            entry_no_003 += 1
        #end
        if 1 == 0 and troop_slot_eq(trp.fight_promoter,12,_current_town):
            set_visitor(entry_no_003,trp.fight_promoter)
            entry_no_003 += 1
        #end
        party_slot_011 = party_get_slot(_current_town,90)
        party_slot_012 = party_get_slot(_current_town,91)
        if party_slot_011 > 0 and party_slot_012 > 0:
            set_visitor(entry_no_003,party_slot_011)
            entry_no_003 += 1
        #end
        if random_x_002 == 1:
            setup_tavern_attacker(entry_no_003)
            entry_no_003 += 1
        #end
        for trp_013 in range(trp.npc1, trp.kingdom_1_lord):
            if troop_slot_eq(trp_013,2,0) and troop_slot_eq(trp_013,12,_current_town) and not troop_slot_ge(trp_013,8,p.town_1):
                set_visitor(entry_no_003,trp_013)
                entry_no_003 += 1
            #end
        #end
        if random_x_002 == 2:
            setup_tavern_attacker(entry_no_003)
            entry_no_003 += 1
        #end
        if True:
            party_slot_014 = party_get_slot(_current_town,95)
            if party_slot_014 > 0:
                reg0 = party_slot_014
                reg1 = _current_town
                set_visitor(entry_no_003,party_slot_014)
                entry_no_003 += 1
            elif is_between(_g_talk_troop,trp.ransom_broker_1,trp.tavern_traveler_1):
                party_id_015 = _current_town + 9
                if party_id_015 >= p.castle_1:
                    party_id_015 -= 22
                #end
            #end
            if _cheat_mode == 1:
                s3 = str_store_party_name(_current_town)
                s4 = str_store_party_name(party_id_015)
                print("@{!}DEBUG - Current town is {s3}, but also checking {s4}")
            #end
            party_slot_014 = party_get_slot(party_id_015,95)
            if party_slot_014 > 0:
                set_visitor(entry_no_003,party_slot_014)
                entry_no_003 += 1
            #end
        #end
        if True:
            party_slot_016 = party_get_slot(_current_town,96)
            if party_slot_016 > 0:
                set_visitor(entry_no_003,party_slot_016)
                entry_no_003 += 1
            #end
        #end
        if True:
            party_slot_017 = party_get_slot(_current_town,99)
            if party_slot_017 > 0:
                set_visitor(entry_no_003,party_slot_017)
                entry_no_003 += 1
            else:
                party_id_015 = _current_town + 9
                if party_id_015 >= p.castle_1:
                    party_id_015 -= 22
                #end
            #end
            party_slot_017 = party_get_slot(party_id_015,99)
            if party_slot_017 > 0:
                set_visitor(entry_no_003,party_slot_017)
                entry_no_003 += 1
            #end
        #end
        if True:
            party_slot_018 = party_get_slot(_current_town,98)
            if party_slot_018 > 0:
                set_visitor(entry_no_003,party_slot_018)
                entry_no_003 += 1
            #end
        #end
        if random_x_002 == 3:
            setup_tavern_attacker(entry_no_003)
            entry_no_003 += 1
        #end
        if not check_quest_active(qst.eliminate_bandits_infesting_village) and not check_quest_active(qst.deal_with_bandits_at_lords_village):
            var019 = p.salt_mine
            for var020 in range(p.village_1, var019):
                if party_slot_eq(var020,120,_current_town) and party_slot_ge(var020,39,1) and not party_slot_eq(var020,7,trp.player):
                    set_visitor(entry_no_003,trp.farmer_from_bandit_village)
                    entry_no_003 += 1
                    var019 = 0
                #end
            #end
        #end
        if _g_starting_town == _current_town and check_quest_finished(qst.collect_men) or check_quest_finished(qst.learn_where_merchant_brother_is) or check_quest_finished(qst.save_relative_of_merchant) or check_quest_finished(qst.save_town_from_bandits) or _g_do_one_more_meeting_with_merchant == 1:
            troop_id_021 = 0
            if _g_encountered_x_party_faction == fac.kingdom_1:
                troop_id_021 = trp.swadian_merchant
            elif _g_encountered_x_party_faction == fac.kingdom_2:
                troop_id_021 = trp.vaegir_merchant
            elif _g_encountered_x_party_faction == fac.kingdom_3:
                troop_id_021 = trp.khergit_merchant
            elif _g_encountered_x_party_faction == fac.kingdom_4:
                troop_id_021 = trp.nord_merchant
            elif _g_encountered_x_party_faction == fac.kingdom_5:
                troop_id_021 = trp.rhodok_merchant
            elif _g_encountered_x_party_faction == fac.kingdom_6:
                troop_id_021 = trp.sarranid_merchant
            #end
            if troop_id_021 > 0:
                set_visitor(entry_no_003,troop_id_021)
                entry_no_003 += 1
            #end
        #end
        change_screen_mission()
    #end
town_town_tavern.codeBlock = code

town_town_merchant = MenuOption("town_merchant", "Speak with the merchant.") # Door to the shop.
def code():
    if _all_doors_locked == 1 or _town_nighttime == 1:
        print(gstr.door_locked,4294945450)
    else:
        _town_entered = 1
        set_jump_mission(mt.town_default)
        mission_tpl_entry_set_override_flags(mt.town_default,0,256)
        if _sneaked_into_town == 1:
            mission_tpl_entry_set_override_flags(mt.town_default,0,447)
        #end
        party_slot_001 = party_get_slot(_current_town,14)
        jump_to_scene(party_slot_001)
        scene_set_slot(party_slot_001,0,1)
        change_screen_mission()
    #end
town_town_merchant.codeBlock = code

town_town_arena = MenuOption("town_arena", "Enter the arena.") # Door to the arena.
def code():
    if _all_doors_locked == 1 or _town_nighttime == 1:
        print(gstr.door_locked,4294945450)
    else:
        _g_mt_mode = 2
        _town_entered = 1
        set_jump_mission(mt.arena_melee_fight)
        party_slot_001 = party_get_slot(_current_town,16)
        modify_visitors_at_site(party_slot_001)
        reset_visitors()
        set_visitor(43,trp.veteran_fighter)
        set_visitor(44,trp.hired_blade)
        set_jump_entry(50)
        jump_to_scene(party_slot_001)
        scene_set_slot(party_slot_001,0,1)
        change_screen_mission()
    #end
town_town_arena.codeBlock = code

town_town_dungeon = MenuOption("town_dungeon", "Never: Enter the prison.") # Door to the dungeon.
def code():
    if _talk_context == 18 and _g_main_attacker_agent > 0 and not agent_is_alive(_g_main_attacker_agent):
        troop_id_001 = agent_get_troop_id(_g_main_attacker_agent)
        if _g_encountered_x_party_faction == fac.player_supporters_faction:
            party_slot_002 = party_get_slot(_current_town,61)
        else:
            party_slot_002 = _g_encountered_x_party_faction
        #end
        if faction_slot_eq(party_slot_002,51,troop_id_001):
            deduct_casualties_from_garrison()
            enter_dungeon(_current_town,mt.visit_town_castle)
        elif _all_doors_locked == 1:
            print(gstr.door_locked,4294945450)
        elif party_slot_eq(_current_town,7,trp.player) or _g_encountered_x_party_faction == _players_kingdom:
            _town_entered = 1
            enter_dungeon(_current_town,mt.visit_town_castle)
        else:
            print(gstr.door_locked,4294945450)
        #end
    #end
town_town_dungeon.codeBlock = code

town_castle_inspect = MenuOption("castle_inspect", "Take a walk around the courtyard.") # To the castle courtyard.
def code():
    if _talk_context == 18:
        _talk_context = 19
        party_slot_001 = party_get_slot(_current_town,10)
        modify_visitors_at_site(party_slot_001)
        reset_visitors()
        entry_no_002 = 40
        party_num_companions_stacks_003 = party_get_num_companion_stacks(_g_encountered_party)
        for stack_no_004 in range(0, party_num_companions_stacks_003):
            party_slot_005 = party_get_slot(_current_town,240)
            cur_hours_006 = store_current_hours()
            var007 = party_slot_005 + 4
            if entry_no_002 == 40 or not is_between(cur_hours_006,party_slot_005,var007) and entry_no_002 < 47:
                troop_id_008 = party_stack_get_troop_id(_g_encountered_party,stack_no_004)
                if not troop_is_hero(troop_id_008):
                    party_stack_size_009 = party_stack_get_size(_g_encountered_party,stack_no_004)
                    party_stack_num_wounded_010 = party_stack_get_num_wounded(_g_encountered_party,stack_no_004)
                    party_stack_size_009 -= party_stack_num_wounded_010
                    if party_stack_size_009 > 0:
                        party_stack_troop_dna_011 = party_stack_get_troop_dna(_g_encountered_party,stack_no_004)
                        set_visitor(entry_no_002,troop_id_008,party_stack_troop_dna_011)
                        entry_no_002 += 1
                    #end
                #end
            #end
        #end
        set_visitor(7,_g_player_troop)
        set_jump_mission(mt.castle_visit)
        jump_to_scene(party_slot_001)
        change_screen_mission()
    else:
        _talk_context = 0
        _g_mt_mode = 0
        party_slot_001 = party_get_slot(_current_town,10)
        modify_visitors_at_site(party_slot_001)
        reset_visitors()
        if _g_encountered_x_party_faction != fac.player_supporters_faction:
            faction_slot_012 = faction_get_slot(_g_encountered_x_party_faction,51)
        else:
            party_slot_013 = party_get_slot(_current_town,61)
            faction_slot_012 = faction_get_slot(party_slot_013,51)
        #end
        set_visitor(24,faction_slot_012)
        entry_no_002 = 40
        party_num_companions_stacks_003 = party_get_num_companion_stacks(_g_encountered_party)
        for stack_no_004 in range(0, party_num_companions_stacks_003):
            party_slot_005 = party_get_slot(_current_town,240)
            cur_hours_006 = store_current_hours()
            var007 = party_slot_005 + 4
            if not is_between(cur_hours_006,var007,party_slot_005) and entry_no_002 < 47:
                troop_id_008 = party_stack_get_troop_id(_g_encountered_party,stack_no_004)
                if not troop_is_hero(troop_id_008):
                    party_stack_size_009 = party_stack_get_size(_g_encountered_party,stack_no_004)
                    party_stack_num_wounded_010 = party_stack_get_num_wounded(_g_encountered_party,stack_no_004)
                    party_stack_size_009 -= party_stack_num_wounded_010
                    if party_stack_size_009 > 0:
                        party_stack_troop_dna_011 = party_stack_get_troop_dna(_g_encountered_party,stack_no_004)
                        set_visitor(entry_no_002,troop_id_008,party_stack_troop_dna_011)
                        entry_no_002 += 1
                    #end
                #end
            #end
        #end
        if _town_entered == 0:
            _town_entered = 1
        #end
        set_jump_entry(1)
        var014 = 256
        if _sneaked_into_town == 1:
            var014 = 447
        #end
        set_jump_mission(mt.castle_visit)
        mission_tpl_entry_set_override_flags(mt.castle_visit,0,var014)
        mission_tpl_entry_set_override_flags(mt.castle_visit,1,var014)
        mission_tpl_entry_set_override_flags(mt.castle_visit,2,var014)
        mission_tpl_entry_set_override_flags(mt.castle_visit,3,var014)
        mission_tpl_entry_set_override_flags(mt.castle_visit,4,var014)
        mission_tpl_entry_set_override_flags(mt.castle_visit,5,var014)
        mission_tpl_entry_set_override_flags(mt.castle_visit,6,var014)
        mission_tpl_entry_set_override_flags(mt.castle_visit,7,var014)
        jump_to_scene(party_slot_001)
        change_screen_mission()
    #end
town_castle_inspect.codeBlock = code

town_town_enterprise = MenuOption("town_enterprise", "Visit your {s3}.") # Door to your enterprise.
def condition():
    if party_slot_eq(_current_town,0,3):
        party_slot_001 = party_get_slot(_current_town,137)
        if party_slot_001 > 1 and _entry_to_town_forbidden == 0:
            get_enterprise_name(party_slot_001)
            s3 = str_store_string(reg0)
town_town_enterprise.conditionBlock = condition
def code():
    var001 = _current_town - p.town_1
    troop_id_002 = trp.town_1_master_craftsman + var001
    party_slot_003 = party_get_slot(_current_town,137)
    scene_id_004 = scn.enterprise_mill
    if party_slot_003 == itm.bread:
        scene_id_004 = scn.enterprise_mill
    elif party_slot_003 == itm.ale:
        scene_id_004 = scn.enterprise_brewery
    elif party_slot_003 == itm.oil:
        scene_id_004 = scn.enterprise_oil_press
    elif party_slot_003 == itm.wine:
        scene_id_004 = scn.enterprise_winery
    elif party_slot_003 == itm.leatherwork:
        scene_id_004 = scn.enterprise_tannery
    elif party_slot_003 == itm.wool_cloth:
        scene_id_004 = scn.enterprise_wool_weavery
    elif party_slot_003 == itm.linen:
        scene_id_004 = scn.enterprise_linen_weavery
    elif party_slot_003 == itm.velvet:
        scene_id_004 = scn.enterprise_dyeworks
    elif party_slot_003 == itm.tools:
        scene_id_004 = scn.enterprise_smithy
    #end
    modify_visitors_at_site(scene_id_004)
    reset_visitors()
    set_visitor(0,trp.player)
    set_visitor(17,troop_id_002)
    set_jump_mission(mt.town_default)
    jump_to_scene(scene_id_004)
    change_screen_mission()
town_town_enterprise.codeBlock = code

town_visit_lady = MenuOption("visit_lady", "Attempt to visit a lady") # Door to the garden.
def condition():
    if not troop_slot_ge(trp.player,30,trp.knight_1_1_wife):
        _love_interest_in_town = 0
        _love_interest_in_town_2 = 0
        _love_interest_in_town_3 = 0
        _love_interest_in_town_4 = 0
        _love_interest_in_town_5 = 0
        _love_interest_in_town_6 = 0
        _love_interest_in_town_7 = 0
        _love_interest_in_town_8 = 0
        for trp_001 in range(trp.knight_1_1_wife, trp.heroes_end):
            if troop_slot_eq(trp_001,12,_current_town):
                get_kingdom_lady_social_determinants(trp_001)
                var002 = reg0
                if troop_slot_eq(trp_001,30,-1) and var002 >= 0 and troop_slot_ge(trp_001,5,2) or troop_slot_eq(var002,38,1) and not troop_slot_eq(trp_001,5,4):
                    if _love_interest_in_town == 0:
                        _love_interest_in_town = trp_001
                    elif _love_interest_in_town_2 == 0:
                        _love_interest_in_town_2 = trp_001
                    elif _love_interest_in_town_3 == 0:
                        _love_interest_in_town_3 = trp_001
                    elif _love_interest_in_town_4 == 0:
                        _love_interest_in_town_4 = trp_001
                    elif _love_interest_in_town_5 == 0:
                        _love_interest_in_town_5 = trp_001
                    elif _love_interest_in_town_6 == 0:
                        _love_interest_in_town_6 = trp_001
                    elif _love_interest_in_town_7 == 0:
                        _love_interest_in_town_7 = trp_001
                    elif _love_interest_in_town_8 == 0:
                        _love_interest_in_town_8 = trp_001
                    #end
                #end
            #end
        #end
    #end
town_visit_lady.conditionBlock = condition
def code():
    jump_to_menu(mnu.lady_visit)
town_visit_lady.codeBlock = code

town_trade_with_merchants = MenuOption("trade_with_merchants", "Go to the marketplace.")
def code():
    if call_script(script.cf_enter_center_location_bandit_check):
        pass
    else:
        jump_to_menu(mnu.town_trade)
    #end
town_trade_with_merchants.codeBlock = code

town_walled_center_manage = MenuOption("walled_center_manage", "Manage this {reg0?town:castle}.")
def condition():
    if not party_slot_eq(_current_town,35,5) and party_slot_eq(_current_town,7,trp.player):
        reg0 = 1
        if party_slot_eq(_current_town,0,2):
            reg0 = 0
        #end
    #end
town_walled_center_manage.conditionBlock = condition
def code():
    _g_next_menu = mnu.town
    jump_to_menu(mnu.center_manage)
town_walled_center_manage.codeBlock = code

town_walled_center_move_court = MenuOption("walled_center_move_court", "Move your court here.")
def code():
    jump_to_menu(mnu.establish_court)
town_walled_center_move_court.codeBlock = code

town_castle_station_troops = MenuOption("castle_station_troops", "Manage the garrison {s10}")
def condition():
    party_slot_001 = party_get_slot(_current_town,7)
    str_clear(10)
    var002 = 0
    if party_slot_001 == trp.player:
        var002 = 1
    else:
        party_faction_003 = store_faction_of_party(_g_encountered_party)
        if party_faction_003 == fac.player_supporters_faction and not party_slot_ge(_g_encountered_party,7,trp.npc1):
            var002 = 1
        elif party_slot_001 < 0:
            party_faction_004 = store_faction_of_party(_g_encountered_party)
            if _players_kingdom == party_faction_004 and _g_encountered_party == _g_castle_requested_by_player:
                s10 = str_store_string(gstr.retrieve_garrison_warning)
                var002 = 1
            elif party_slot_001 < 0:
                party_faction_004 = store_faction_of_party(_g_encountered_party)
                if _players_kingdom == party_faction_004:
                    party_size_wo_prisoners_005 = store_party_size_wo_prisoners(_g_encountered_party)
                    if party_size_wo_prisoners_005 == 0:
                        s10 = str_store_string(gstr.retrieve_garrison_warning)
                        var002 = 1
                    elif party_slot_ge(_g_encountered_party,7,trp.npc1):
                        party_faction_004 = store_faction_of_party(_g_encountered_party)
                        if _players_kingdom == party_faction_004 and troop_slot_eq(trp.player,30,party_slot_001):
                            var002 = 1
                        #end
                    #end
                #end
            #end
        #end
    #end
town_castle_station_troops.conditionBlock = condition
def code():
    change_screen_exchange_members(1)
town_castle_station_troops.codeBlock = code

town_castle_wait = MenuOption("castle_wait", "Wait here for some time{s1}.")
def condition():
    if _g_encountered_party_relation >= 0 or _castle_undefended == 1:
        var001 = 1
        str_clear(1)
        if not party_slot_eq(_current_town,7,trp.player):
            troop_slot_002 = troop_get_slot(trp.player,30)
            if not party_slot_eq(_current_town,7,troop_slot_002) and party_slot_ge(_current_town,7,trp.player):
                party_faction_003 = store_faction_of_party(_current_town)
                if party_faction_003 != fac.player_supporters_faction:
                    party_num_companions_004 = party_get_num_companions(p.main_party)
                    reg1 = party_num_companions_004 / 4
                    reg1 += 1
                    s1 = str_store_string("@ ({reg1} denars per night)")
                    troop_gold_005 = store_troop_gold(trp.player)
                    if troop_gold_005 < reg1:
                        var001 = 0
                    #end
                #end
            #end
        #end
    #end
town_castle_wait.conditionBlock = condition
def code():
    _auto_enter_town = _current_town
    _g_town_visit_after_rest = 1
    _g_last_rest_center = _current_town
    _g_last_rest_payment_until = -1
    if party_is_active(p.main_party):
        party_cur_terrain_001 = party_get_current_terrain(p.main_party)
        if party_cur_terrain_001 == 5:
            unlock_achievement(28)
        #end
    #end
    rest_for_hours_interactive(168,5,0)
    change_screen_return()
town_castle_wait.codeBlock = code

town_town_alley = MenuOption("town_alley", "{!}CHEAT: Go to the alley.")
def code():
    reg11 = party_get_slot(_current_town,17)
    set_jump_mission(mt.ai_training)
    jump_to_scene(reg11)
    change_screen_mission()
town_town_alley.codeBlock = code

town_collect_taxes_qst = MenuOption("collect_taxes_qst", "{reg5?Continue collecting taxes:Collect taxes} due to {s1}.")
def condition():
    if check_quest_active(qst.collect_taxes) and quest_slot_eq(qst.collect_taxes,1,_current_town) and not quest_slot_eq(qst.collect_taxes,11,4):
        quest_slot_001 = quest_get_slot(qst.collect_taxes,6)
        s1 = str_store_troop_name(quest_slot_001)
        reg5 = quest_get_slot(qst.collect_taxes,11)
town_collect_taxes_qst.conditionBlock = condition
def code():
    jump_to_menu(mnu.collect_taxes)
town_collect_taxes_qst.codeBlock = code

town_town_leave = MenuOption("town_leave", "Leave...") # Leave Area.
def code():
    _g_permitted_to_center = 0
    change_screen_return(0)
town_town_leave.codeBlock = code

town_castle_cheat_interior = MenuOption("castle_cheat_interior", "{!}CHEAT! Interior.")
def code():
    set_jump_mission(mt.ai_training)
    party_slot_001 = party_get_slot(_current_town,11)
    jump_to_scene(party_slot_001)
    change_screen_mission()
town_castle_cheat_interior.codeBlock = code

town_castle_cheat_town_exterior = MenuOption("castle_cheat_town_exterior", "{!}CHEAT! Exterior.")
def code():
    if party_slot_eq(_current_town,0,2):
        party_slot_001 = party_get_slot(_current_town,10)
    else:
        party_slot_001 = party_get_slot(_current_town,10)
    #end
    set_jump_mission(mt.ai_training)
    jump_to_scene(party_slot_001)
    change_screen_mission()
town_castle_cheat_town_exterior.codeBlock = code

town_castle_cheat_dungeon = MenuOption("castle_cheat_dungeon", "{!}CHEAT! Prison.")
def code():
    set_jump_mission(mt.ai_training)
    party_slot_001 = party_get_slot(_current_town,12)
    jump_to_scene(party_slot_001)
    change_screen_mission()
town_castle_cheat_dungeon.codeBlock = code

town_castle_cheat_town_walls = MenuOption("castle_cheat_town_walls", "{!}CHEAT! Town Walls.")
def code():
    party_slot_001 = party_get_slot(_current_town,18)
    set_jump_mission(mt.ai_training)
    jump_to_scene(party_slot_001)
    change_screen_mission()
town_castle_cheat_town_walls.codeBlock = code

town_cheat_town_start_siege = MenuOption("cheat_town_start_siege", "{!}CHEAT: Besiege the {reg6?town:castle}...")
def condition():
    if _cheat_mode == 1 and party_slot_eq(_g_encountered_party,54,-1) and _g_encountered_party_2 < 1:
        party_count_fit_for_battle(p.main_party)
        if reg0 > 1:
            if party_slot_eq(_g_encountered_party,0,3):
                reg6 = 1
            else:
                reg6 = 0
            #end
        #end
    #end
town_cheat_town_start_siege.conditionBlock = condition
def code():
    _g_player_besiege_town = _g_encountered_party
    jump_to_menu(mnu.castle_besiege)
town_cheat_town_start_siege.codeBlock = code

town_center_reports = MenuOption("center_reports", "{!}CHEAT! Show reports.")
def code():
    jump_to_menu(mnu.center_reports)
town_center_reports.codeBlock = code

town_sail_from_port = MenuOption("sail_from_port", "{!}CHEAT: Sail from port.")
def code():
    _g_player_icon_state = 2
    party_set_flags(p.main_party,512,1)
    pos1 = party_get_position(p.main_party)
    if map_get_water_position_around_position(2,1,6):
        party_set_position(p.main_party,2)
        _g_main_ship_party = -1
        change_screen_return()
town_sail_from_port.codeBlock = code



cannot_enter_court = GameMenu("cannot_enter_court", 0,
"There is a feast in progress in the lord's hall, but you are not of sufficient status to be invited inside. Perhaps increasing your renown would win you admittance -- or you might also try distinguishing yourself at a tournament while the feast is in progress..."
)

cannot_enter_court_continue = MenuOption("continue", "Continue")
def code():
    jump_to_menu(mnu.town)
cannot_enter_court_continue.codeBlock = code



lady_visit = GameMenu("lady_visit", 0,
"Whom do you wish to visit?"
)

lady_visit_visit_lady_1 = MenuOption("visit_lady_1", "Visit {s12}")
def condition():
    if _love_interest_in_town > 0:
        s12 = str_store_troop_name(_love_interest_in_town)
lady_visit_visit_lady_1.conditionBlock = condition
def code():
    _love_interest_in_town = _love_interest_in_town
    jump_to_menu(mnu.garden)
lady_visit_visit_lady_1.codeBlock = code

lady_visit_visit_lady_2 = MenuOption("visit_lady_2", "Visit {s12}")
def condition():
    if _love_interest_in_town_2 > 0:
        s12 = str_store_troop_name(_love_interest_in_town_2)
lady_visit_visit_lady_2.conditionBlock = condition
def code():
    _love_interest_in_town = _love_interest_in_town_2
    jump_to_menu(mnu.garden)
lady_visit_visit_lady_2.codeBlock = code

lady_visit_visit_lady_3 = MenuOption("visit_lady_3", "Visit {s12}") # Door to the garden.
def condition():
    if _love_interest_in_town_3 > 0:
        s12 = str_store_troop_name(_love_interest_in_town_3)
lady_visit_visit_lady_3.conditionBlock = condition
def code():
    _love_interest_in_town = _love_interest_in_town_3
    jump_to_menu(mnu.garden)
lady_visit_visit_lady_3.codeBlock = code

lady_visit_visit_lady_4 = MenuOption("visit_lady_4", "Visit {s12}")
def condition():
    if _love_interest_in_town_4 > 0:
        s12 = str_store_troop_name(_love_interest_in_town_4)
lady_visit_visit_lady_4.conditionBlock = condition
def code():
    _love_interest_in_town = _love_interest_in_town_4
    jump_to_menu(mnu.garden)
lady_visit_visit_lady_4.codeBlock = code

lady_visit_visit_lady_5 = MenuOption("visit_lady_5", "Visit {s12}")
def condition():
    if _love_interest_in_town_5 > 0:
        s12 = str_store_troop_name(_love_interest_in_town_5)
lady_visit_visit_lady_5.conditionBlock = condition
def code():
    _love_interest_in_town = _love_interest_in_town_5
    jump_to_menu(mnu.garden)
lady_visit_visit_lady_5.codeBlock = code

lady_visit_visit_lady_6 = MenuOption("visit_lady_6", "Visit {s12}")
def condition():
    if _love_interest_in_town_6 > 0:
        s12 = str_store_troop_name(_love_interest_in_town_6)
lady_visit_visit_lady_6.conditionBlock = condition
def code():
    _love_interest_in_town = _love_interest_in_town_6
    jump_to_menu(mnu.garden)
lady_visit_visit_lady_6.codeBlock = code

lady_visit_visit_lady_7 = MenuOption("visit_lady_7", "Visit {s12}")
def condition():
    if _love_interest_in_town_7 > 0:
        s12 = str_store_troop_name(_love_interest_in_town_7)
lady_visit_visit_lady_7.conditionBlock = condition
def code():
    _love_interest_in_town = _love_interest_in_town_7
    jump_to_menu(mnu.garden)
lady_visit_visit_lady_7.codeBlock = code

lady_visit_visit_lady_8 = MenuOption("visit_lady_8", "Visit {s12}")
def condition():
    if _love_interest_in_town_8 > 0:
        s12 = str_store_troop_name(_love_interest_in_town_8)
lady_visit_visit_lady_8.conditionBlock = condition
def code():
    _love_interest_in_town = _love_interest_in_town_8
    jump_to_menu(mnu.garden)
lady_visit_visit_lady_8.codeBlock = code

lady_visit_leave = MenuOption("leave", "Leave")
def code():
    jump_to_menu(mnu.town)
lady_visit_leave.codeBlock = code



town_tournament_lost = GameMenu("town_tournament_lost", 0,
"You have been eliminated from the tournament.{s8}"
)
def condition():
    str_clear(8)
    if _players_kingdom == _g_encountered_x_party_faction or not troop_slot_ge(trp.player,7,50) and not troop_slot_ge(trp.player,7,125) and _g_player_tournament_placement > 4 and faction_slot_eq(_g_encountered_x_party_faction,4,6) and faction_slot_eq(_g_encountered_x_party_faction,5,_g_encountered_party):
        s8 = str_store_string(gstr._however_you_have_sufficiently_distinguished_yourself_to_be_invited_to_attend_the_ongoing_feast_in_the_lords_castle)
    #end
town_tournament_lost.conditionBlock = condition

town_tournament_lost_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.town_tournament_won_by_another)
town_tournament_lost_continue.codeBlock = code



town_tournament_won = GameMenu("town_tournament_won", 512,
"You have won the tournament of {s3}! You are filled with pride as the crowd cheers your name. In addition to honour, fame and glory, you earn a prize of {reg9} denars. {s8}"
)
def condition():
    s3 = str_store_party_name(_current_town)
    change_troop_renown(trp.player,20)
    change_player_relation_with_center(_current_town,1)
    reg9 = 200
    add_xp_to_troop(250,trp.player)
    troop_add_gold(trp.player,reg9)
    str_clear(8)
    gold_001 = _g_tournament_bet_placed + _g_tournament_bet_win_amount
    if _g_tournament_bet_win_amount > 0:
        reg8 = gold_001
        s8 = str_store_string("@Moreover;;; you earn {reg8} denars from the clever bets you placed on yourself...")
    #end
    if _players_kingdom == _g_encountered_x_party_faction or not troop_slot_ge(trp.player,7,70) and not troop_slot_ge(trp.player,7,145) and faction_slot_eq(_g_encountered_x_party_faction,4,6) and faction_slot_eq(_g_encountered_x_party_faction,5,_g_encountered_party):
        s8 = str_store_string(gstr.s8_you_are_also_invited_to_attend_the_ongoing_feast_in_the_castle)
    #end
    troop_add_gold(trp.player,gold_001)
    var002 = 0
    var002 = _g_tournament_bet_win_amount / 5
    party_slot_003 = party_get_slot(_current_town,51)
    party_slot_003 -= var002
    val_max(party_slot_003,250)
    party_set_slot(_current_town,51,party_slot_003)
    play_victorious_sound()
    unlock_achievement(33)
town_tournament_won.conditionBlock = condition

town_tournament_won_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.town)
town_tournament_won_continue.codeBlock = code



town_tournament_won_by_another = GameMenu("town_tournament_won_by_another", 512,
"As the only {reg3?fighter:man} to remain undefeated this day, {s1} wins the lists and the glory of this tournament."
)
def condition():
    get_num_tournament_participants()
    var001 = reg0 - 1
    if troop_slot_eq(trp.tournament_participants,0,0):
        troop_set_slot(trp.tournament_participants,0,-1)
        var001 -= 1
    #end
    remove_tournament_participants_randomly(var001)
    sort_tournament_participant_troops()
    troop_slot_002 = troop_get_slot(trp.tournament_participants,0)
    s1 = str_store_troop_name(troop_slot_002)
    if troop_is_hero(troop_slot_002):
        change_troop_renown(troop_slot_002,20)
    #end
    reg3 = troop_get_type(troop_slot_002)
town_tournament_won_by_another.conditionBlock = condition

town_tournament_won_by_another_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.town)
town_tournament_won_by_another_continue.codeBlock = code



town_tournament = GameMenu("town_tournament", 512,
"{s1}You are at tier {reg0} of the tournament, with {reg1} participants remaining. In the next round, there will be {reg2} teams with {reg3} {reg4?fighters:fighter} each."
)
def condition():
    party_set_slot(_current_town,156,0)
    sort_tournament_participant_troops()
    get_num_tournament_participants()
    var001 = reg0
    if not troop_slot_eq(trp.tournament_participants,0,0):
        var002 = 0
        var002 = _g_tournament_bet_placed / 5
        party_slot_003 = party_get_slot(_current_town,51)
        party_slot_003 += var002
        val_min(party_slot_003,4000)
        party_set_slot(_current_town,51,party_slot_003)
        jump_to_menu(mnu.town_tournament_lost)
    elif var001 == 1:
        jump_to_menu(mnu.town_tournament_won)
    else:
        if _g_tournament_next_num_teams <= 0:
            get_random_tournament_team_amount_and_size()
            _g_tournament_next_num_teams = reg0
            _g_tournament_next_team_size = reg1
        #end
        reg2 = _g_tournament_next_num_teams
        reg3 = _g_tournament_next_team_size
        reg4 = reg3 - 1
        str_clear(1)
        if _g_tournament_player_team_won == 1:
            s1 = str_store_string("@Victory is yours! You have won this melee;;; but now you must prepare yourself for the next round. ")
        elif _g_tournament_player_team_won == 0:
            s1 = str_store_string("@You have been bested in this melee;;; but the master of ceremonies declares a recognition of your skill and bravery;;; allowing you to take part in the next round. ")
        #end
        reg1 = var001
        reg0 = _g_tournament_cur_tier + 1
    #end
town_tournament.conditionBlock = condition

town_tournament_tournament_view_participants = MenuOption("tournament_view_participants", "View participants.")
def code():
    jump_to_menu(mnu.tournament_participants)
town_tournament_tournament_view_participants.codeBlock = code

town_tournament_tournament_bet = MenuOption("tournament_bet", "Place a bet on yourself.")
def code():
    jump_to_menu(mnu.tournament_bet)
town_tournament_tournament_bet.codeBlock = code

town_tournament_tournament_join_next_fight = MenuOption("tournament_join_next_fight", "Fight in the next round.")
def code():
    party_slot_001 = party_get_slot(_current_town,16)
    modify_visitors_at_site(party_slot_001)
    reset_visitors()
    _g_player_tournament_placement = _g_tournament_cur_tier
    if _g_player_tournament_placement > 4:
        _g_player_eligible_feast_center_no = _current_town
    #end
    _g_tournament_cur_tier += 1
    _g_tournament_num_participants_for_fight = _g_tournament_next_num_teams * _g_tournament_next_team_size
    troop_set_slot(trp.tournament_participants,0,-1)
    troop_set_slot(trp.temp_array_a,0,trp.player)
    for slot_no_002 in range(1, _g_tournament_num_participants_for_fight):
        get_random_tournament_participant()
        troop_set_slot(trp.temp_array_a,slot_no_002,reg0)
    #end
    shuffle_troop_slots(trp.temp_array_a,0,_g_tournament_num_participants_for_fight)
    for slot_no_002 in range(0, 4):
        troop_set_slot(trp.temp_array_b,slot_no_002,slot_no_002)
    #end
    shuffle_troop_slots(trp.temp_array_b,0,4)
    slot_no_003 = 0
    for slot_no_004 in range(0, _g_tournament_next_num_teams):
        troop_slot_005 = troop_get_slot(trp.temp_array_b,slot_no_004)
        for slot_no_002 in range(0, 8):
            troop_set_slot(trp.temp_array_c,slot_no_002,slot_no_002)
        #end
        shuffle_troop_slots(trp.temp_array_c,0,8)
        for slot_no_006 in range(0, _g_tournament_next_team_size):
            entry_no_007 = troop_slot_005 * 8
            troop_slot_008 = troop_get_slot(trp.temp_array_c,slot_no_006)
            entry_no_007 += troop_slot_008
            troop_slot_009 = troop_get_slot(trp.temp_array_a,slot_no_003)
            set_visitor(entry_no_007,troop_slot_009)
            slot_no_003 += 1
        #end
    #end
    _g_tournament_next_num_teams = 0
    _g_tournament_next_team_size = 0
    _g_mt_mode = 3
    party_slot_010 = party_get_slot(_current_town,61)
    var011 = 0
    var012 = p.castle_1
    for var013 in range(p.town_1, var012):
        if var013 == _current_town:
            var012 = 0
        elif party_slot_eq(var013,61,party_slot_010):
            var011 += 1
        #end
    #end
    set_jump_mission(mt.arena_melee_fight)
    if party_slot_010 == fac.kingdom_1:
        var014 = store_mod(var011,4)
        if var014 == 0:
            set_items_for_tournament(40,80,50,20,0,0,0,0,itm.arena_armor_red,itm.tourney_helm_red)
        elif var014 == 1:
            set_items_for_tournament(100,100,0,0,0,0,0,0,itm.arena_armor_red,itm.tourney_helm_red)
        elif var014 == 2:
            set_items_for_tournament(100,0,100,0,0,0,0,0,itm.arena_armor_red,itm.tourney_helm_red)
        elif var014 == 3:
            set_items_for_tournament(40,80,50,20,40,0,0,0,itm.arena_armor_red,itm.tourney_helm_red)
        #end
    elif party_slot_010 == fac.kingdom_2:
        var014 = store_mod(var011,4)
        if var014 == 0:
            set_items_for_tournament(40,80,50,20,0,0,0,0,itm.arena_armor_red,itm.steppe_helmet_red)
        elif var014 == 1:
            set_items_for_tournament(100,50,0,0,0,20,30,0,itm.arena_armor_red,itm.steppe_helmet_red)
        elif var014 == 2:
            set_items_for_tournament(100,0,50,0,0,20,30,0,itm.arena_armor_red,itm.steppe_helmet_red)
        elif var014 == 3:
            set_items_for_tournament(40,80,50,20,30,0,60,0,itm.arena_armor_red,itm.steppe_helmet_red)
        #end
    elif party_slot_010 == fac.kingdom_3:
        var014 = store_mod(var011,2)
        if var014 == 0:
            set_items_for_tournament(100,0,0,0,0,40,60,0,itm.arena_tunic_red,itm.steppe_helmet_red)
        elif var014 == 1:
            set_items_for_tournament(100,50,25,0,0,30,50,0,itm.arena_tunic_red,itm.steppe_helmet_red)
        #end
    elif party_slot_010 == fac.kingdom_4:
        var014 = store_mod(var011,3)
        if var014 == 0:
            set_items_for_tournament(0,0,50,80,0,0,0,0,itm.arena_armor_red,-1)
        elif var014 == 1:
            set_items_for_tournament(0,0,50,80,50,0,0,0,itm.arena_armor_red,-1)
        elif var014 == 2:
            set_items_for_tournament(40,0,0,100,0,0,0,0,itm.arena_armor_red,-1)
        #end
    elif party_slot_010 == fac.kingdom_5:
        set_items_for_tournament(25,100,60,0,30,0,30,50,itm.arena_tunic_red,itm.arena_helmet_red)
    else:
        var014 = store_mod(var011,2)
        if var014 == 0:
            set_items_for_tournament(100,40,60,0,30,30,0,0,itm.arena_tunic_red,itm.arena_turban_red)
        else:
            set_items_for_tournament(50,0,60,0,30,30,0,0,itm.arena_tunic_red,itm.arena_turban_red)
        #end
    #end
    jump_to_scene(party_slot_001)
    change_screen_mission()
town_tournament_tournament_join_next_fight.codeBlock = code

town_tournament_leave_tournament = MenuOption("leave_tournament", "Withdraw from the tournament.")
def code():
    jump_to_menu(mnu.tournament_withdraw_verify)
town_tournament_leave_tournament.codeBlock = code



tournament_withdraw_verify = GameMenu("tournament_withdraw_verify", 0,
"Are you sure you want to withdraw from the tournament?"
)

tournament_withdraw_verify_tournament_withdraw_yes = MenuOption("tournament_withdraw_yes", "Yes. This is a pointless affectation.")
def code():
    jump_to_menu(mnu.town_tournament_won_by_another)
tournament_withdraw_verify_tournament_withdraw_yes.codeBlock = code

tournament_withdraw_verify_tournament_withdraw_no = MenuOption("tournament_withdraw_no", "No, not as long as there is a chance of victory!")
def code():
    jump_to_menu(mnu.town_tournament)
tournament_withdraw_verify_tournament_withdraw_no.codeBlock = code



tournament_bet = GameMenu("tournament_bet", 0,
"The odds against you are {reg5} to {reg6}.{reg1? You have already bet {reg1} denars on yourself, and if you win, you will earn {reg2} denars.:} How much do you want to bet?"
)
def condition():
    reg1 = _g_tournament_bet_placed
    reg2 = _g_tournament_bet_win_amount + _g_tournament_bet_placed
    get_win_amount_for_tournament_bet()
    var001 = reg0
    var002 = 100000
    var003 = 1
    var004 = 1
    for var005 in range(1, 50):
        for var006 in range(1, 50):
            var007 = 100 * var005
            var007 /= var006
            var008 = var001 - var007
            val_abs(var008)
            if var008 < var002:
                var002 = var008
                var003 = var006
                var004 = var005
            #end
        #end
    #end
    reg5 = var004
    reg6 = var003
tournament_bet.conditionBlock = condition

tournament_bet_bet_100_denars = MenuOption("bet_100_denars", "100 denars.")
def condition():
    troop_gold_001 = store_troop_gold(trp.player)
tournament_bet_bet_100_denars.conditionBlock = condition
def code():
    _temp = 100
    jump_to_menu(mnu.tournament_bet_confirm)
tournament_bet_bet_100_denars.codeBlock = code

tournament_bet_bet_50_denars = MenuOption("bet_50_denars", "50 denars.")
def condition():
    troop_gold_001 = store_troop_gold(trp.player)
tournament_bet_bet_50_denars.conditionBlock = condition
def code():
    _temp = 50
    jump_to_menu(mnu.tournament_bet_confirm)
tournament_bet_bet_50_denars.codeBlock = code

tournament_bet_bet_20_denars = MenuOption("bet_20_denars", "20 denars.")
def condition():
    troop_gold_001 = store_troop_gold(trp.player)
tournament_bet_bet_20_denars.conditionBlock = condition
def code():
    _temp = 20
    jump_to_menu(mnu.tournament_bet_confirm)
tournament_bet_bet_20_denars.codeBlock = code

tournament_bet_bet_10_denars = MenuOption("bet_10_denars", "10 denars.")
def condition():
    troop_gold_001 = store_troop_gold(trp.player)
tournament_bet_bet_10_denars.conditionBlock = condition
def code():
    _temp = 10
    jump_to_menu(mnu.tournament_bet_confirm)
tournament_bet_bet_10_denars.codeBlock = code

tournament_bet_bet_5_denars = MenuOption("bet_5_denars", "5 denars.")
def condition():
    troop_gold_001 = store_troop_gold(trp.player)
tournament_bet_bet_5_denars.conditionBlock = condition
def code():
    _temp = 5
    jump_to_menu(mnu.tournament_bet_confirm)
tournament_bet_bet_5_denars.codeBlock = code

tournament_bet_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    jump_to_menu(mnu.town_tournament)
tournament_bet_go_back_dot.codeBlock = code



tournament_bet_confirm = GameMenu("tournament_bet_confirm", 0,
"If you bet {reg1} denars, you will earn {reg2} denars if you win the tournament. Is that all right?"
)
def condition():
    get_win_amount_for_tournament_bet()
    var001 = reg0
    var001 *= _temp
    var001 /= 100
    reg1 = _temp
    reg2 = var001
tournament_bet_confirm.conditionBlock = condition

tournament_bet_confirm_tournament_bet_accept = MenuOption("tournament_bet_accept", "Go ahead.")
def code():
    tournament_place_bet(_temp)
    jump_to_menu(mnu.town_tournament)
tournament_bet_confirm_tournament_bet_accept.codeBlock = code

tournament_bet_confirm_tournament_bet_cancel = MenuOption("tournament_bet_cancel", "Forget it.")
def code():
    jump_to_menu(mnu.tournament_bet)
tournament_bet_confirm_tournament_bet_cancel.codeBlock = code



tournament_participants = GameMenu("tournament_participants", 0,
"You ask one of the criers for the names of the tournament participants. They are:^{s11}"
)
def condition():
    str_clear(11)
    sort_tournament_participant_troops()
    get_num_tournament_participants()
    var001 = reg0
    for slot_no_002 in range(0, var001):
        troop_slot_003 = troop_get_slot(trp.tournament_participants,slot_no_002)
        s12 = str_store_troop_name(troop_slot_003)
        s11 = str_store_string("@{!}{s11}^{s12}")
    #end
tournament_participants.conditionBlock = condition

tournament_participants_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    jump_to_menu(mnu.town_tournament)
tournament_participants_go_back_dot.codeBlock = code



collect_taxes = GameMenu("collect_taxes", 512,
"As the party member with the highest trade skill ({reg2}), {reg3?you expect:{s1} expects} that collecting taxes from here will take {reg4} days..."
)
def condition():
    get_max_skill_of_player_party(skl.trade)
    var001 = reg0
    reg2 = reg0
    var002 = reg1
    if var002 == trp.player:
        reg3 = 1
    else:
        reg3 = 0
        s1 = str_store_troop_name(var002)
    #end
    var003 = 3000
    if party_slot_eq(_current_town,0,3):
        var003 = 6000
    #end
    if quest_slot_eq(qst.collect_taxes,11,0):
        var004 = var001 + 30
        if party_slot_eq(_current_town,0,3):
            _qst_collect_taxes_total_hours = 5040 / var004
        else:
            _qst_collect_taxes_total_hours = 2160 / var004
        #end
        party_count_fit_for_battle(p.main_party)
        reg0 += 20
        _qst_collect_taxes_total_hours *= 20
        _qst_collect_taxes_total_hours /= reg0
        quest_set_slot(qst.collect_taxes,10,_qst_collect_taxes_total_hours)
        var005 = _qst_collect_taxes_total_hours / 20
        var006 = _qst_collect_taxes_total_hours / 4
        var007 = var006
        var008 = _qst_collect_taxes_total_hours * 3
        var008 /= 4
        var003 *= 2
        _qst_collect_taxes_hourly_income = var003 / _qst_collect_taxes_total_hours
        _qst_collect_taxes_counter = store_random_in_range(var005,var006)
        _qst_collect_taxes_unrest_counter = store_random_in_range(var007,var008)
        _qst_collect_taxes_halve_taxes = 0
    #end
    quest_slot_009 = quest_get_slot(qst.collect_taxes,10)
    var010 = quest_slot_009 / 24
    var010 *= 24
    if var010 < quest_slot_009:
        var010 += 24
    #end
    var010 /= 24
    reg4 = var010
collect_taxes.conditionBlock = condition

collect_taxes_start_collecting = MenuOption("start_collecting", "Start collecting.")
def code():
    _qst_collect_taxes_currently_collecting = 1
    if quest_slot_eq(qst.collect_taxes,11,0):
        quest_set_slot(qst.collect_taxes,11,1)
    #end
    rest_for_hours_interactive(1000,5,0)
    _auto_enter_town = _current_town
    _g_town_visit_after_rest = 1
    change_screen_return()
collect_taxes_start_collecting.codeBlock = code

collect_taxes_collect_later = MenuOption("collect_later", "Put it off until later.")
def code():
    if party_slot_eq(_current_town,0,3):
        jump_to_menu(mnu.town)
    else:
        jump_to_menu(mnu.village)
    #end
collect_taxes_collect_later.codeBlock = code



collect_taxes_complete = GameMenu("collect_taxes_complete", 512,
"You've collected {reg3} denars in taxes from {s3}. {s19} will be expecting you to take the money to him."
)
def condition():
    s3 = str_store_party_name(_current_town)
    quest_slot_001 = quest_get_slot(qst.collect_taxes,6)
    s19 = str_store_troop_name(quest_slot_001)
    reg3 = quest_get_slot(qst.collect_taxes,22)
    if _qst_collect_taxes_halve_taxes == 0:
        change_player_relation_with_center(_current_town,-2)
    #end
    succeed_quest(qst.collect_taxes)
collect_taxes_complete.conditionBlock = condition

collect_taxes_complete_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
collect_taxes_complete_continue.codeBlock = code



collect_taxes_rebels_killed = GameMenu("collect_taxes_rebels_killed", 0,
"Your quick action and strong arm have successfully put down the revolt. Surely, anyone with a mind to rebel against you will think better of it after this."
)

collect_taxes_rebels_killed_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_map()
collect_taxes_rebels_killed_continue.codeBlock = code



collect_taxes_failed = GameMenu("collect_taxes_failed", 512,
"You could collect only {reg3} denars as tax from {s3} before the revolt broke out. {s1} won't be happy, but some silver will placate him better than nothing at all..."
)
def condition():
    s3 = str_store_party_name(_current_town)
    quest_slot_001 = quest_get_slot(qst.collect_taxes,6)
    s1 = str_store_troop_name(quest_slot_001)
    reg3 = quest_get_slot(qst.collect_taxes,22)
    fail_quest(qst.collect_taxes)
    quest_set_slot(qst.collect_taxes,11,4)
    rest_for_hours(0,0,0)
collect_taxes_failed.conditionBlock = condition

collect_taxes_failed_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_map()
collect_taxes_failed_continue.codeBlock = code



collect_taxes_revolt_warning = GameMenu("collect_taxes_revolt_warning", 0,
"The people of {s3} are outraged at your demands and decry it as nothing more than extortion. They're getting very restless, and they may react badly if you keep pressing them."
)
def condition():
    s3 = str_store_party_name(_current_town)
collect_taxes_revolt_warning.conditionBlock = condition

collect_taxes_revolt_warning_continue_collecting_taxes = MenuOption("continue_collecting_taxes", "Ignore them and continue.")
def code():
    change_screen_return()
collect_taxes_revolt_warning_continue_collecting_taxes.codeBlock = code

collect_taxes_revolt_warning_halve_taxes = MenuOption("halve_taxes", "Agree to reduce your collection by half. ({s1} may be upset)")
def condition():
    quest_slot_001 = quest_get_slot(qst.collect_taxes,6)
    s1 = str_store_troop_name(quest_slot_001)
collect_taxes_revolt_warning_halve_taxes.conditionBlock = condition
def code():
    _qst_collect_taxes_halve_taxes = 1
    change_screen_return()
collect_taxes_revolt_warning_halve_taxes.codeBlock = code



collect_taxes_revolt = GameMenu("collect_taxes_revolt", 0,
"You are interrupted while collecting the taxes at {s3}. A large band of angry {reg9?peasants:townsmen} is marching nearer, shouting about the exorbitant taxes and waving torches and weapons. It looks like they aim to fight you!"
)
def condition():
    s3 = str_store_party_name(_current_town)
    reg9 = 0
    if party_slot_eq(_current_town,0,4):
        reg9 = 1
    #end
collect_taxes_revolt.conditionBlock = condition

collect_taxes_revolt_continue = MenuOption("continue", "Continue...")
def code():
    set_jump_mission(mt.back_alley_revolt)
    quest_slot_001 = quest_get_slot(qst.collect_taxes,1)
    if party_slot_eq(quest_slot_001,0,3):
        party_slot_002 = party_get_slot(quest_slot_001,17)
    else:
        party_slot_002 = party_get_slot(quest_slot_001,10)
    #end
    modify_visitors_at_site(party_slot_002)
    reset_visitors()
    number_of_troops_003 = 6
    character_lvl_004 = store_character_level(trp.player)
    character_lvl_004 /= 5
    number_of_troops_003 += character_lvl_004
    set_visitors(1,trp.tax_rebel,number_of_troops_003)
    jump_to_scene(party_slot_002)
    change_screen_mission()
collect_taxes_revolt_continue.codeBlock = code



train_peasants_against_bandits = GameMenu("train_peasants_against_bandits", 0,
"As the party member with the highest training skill ({reg2}), {reg3?you expect:{s1} expects} that getting some peasants ready for practice will take {reg4} hours."
)
def condition():
    get_max_skill_of_player_party(skl.trainer)
    var001 = reg0
    reg2 = reg0
    var002 = reg1
    if var002 == trp.player:
        reg3 = 1
    else:
        reg3 = 0
        s1 = str_store_troop_name(var002)
    #end
    var003 = 20 - var001
    var003 *= 3
    var003 /= 5
    reg4 = var003 - _qst_train_peasants_against_bandits_num_hours_trained
train_peasants_against_bandits.conditionBlock = condition

train_peasants_against_bandits_make_preparation = MenuOption("make_preparation", "Train them.")
def code():
    _qst_train_peasants_against_bandits_currently_training = 1
    rest_for_hours_interactive(1000,5,0)
    _auto_enter_town = _current_town
    _g_town_visit_after_rest = 1
    change_screen_return()
train_peasants_against_bandits_make_preparation.codeBlock = code

train_peasants_against_bandits_train_later = MenuOption("train_later", "Put it off until later.")
def code():
    jump_to_menu(mnu.village)
train_peasants_against_bandits_train_later.codeBlock = code



train_peasants_against_bandits_ready = GameMenu("train_peasants_against_bandits_ready", 0,
"You put the peasants through the basics of soldiering, discipline and obedience. You think {reg0} of them {reg1?have:has} fully grasped the training and {reg1?are:is} ready for some practice."
)
def condition():
    character_lvl_001 = store_character_level(trp.player)
    character_lvl_001 /= 10
    character_lvl_001 += 1
    quest_slot_002 = quest_get_slot(qst.train_peasants_against_bandits,10)
    quest_slot_003 = quest_get_slot(qst.train_peasants_against_bandits,11)
    quest_slot_002 -= quest_slot_003
    var004 = character_lvl_001
    val_min(var004,quest_slot_002)
    var004 += 1
    random_x_005 = store_random_in_range(1,var004)
    _g_train_peasants_against_bandits_num_peasants = random_x_005
    reg0 = random_x_005
    reg1 = random_x_005 - 1
    str_store_troop_name_by_count(s0,trp.trainee_peasant,random_x_005)
train_peasants_against_bandits_ready.conditionBlock = condition

train_peasants_against_bandits_ready_peasant_start_practice = MenuOption("peasant_start_practice", "Start the practice fight.")
def code():
    set_jump_mission(mt.village_training)
    quest_slot_001 = quest_get_slot(qst.train_peasants_against_bandits,1)
    party_slot_002 = party_get_slot(quest_slot_001,10)
    modify_visitors_at_site(party_slot_002)
    reset_visitors()
    set_visitor(0,trp.player)
    set_visitors(1,trp.trainee_peasant,_g_train_peasants_against_bandits_num_peasants)
    set_jump_entry(11)
    jump_to_scene(party_slot_002)
    jump_to_menu(mnu.train_peasants_against_bandits_training_result)
    music_set_situation(0)
    change_screen_mission()
train_peasants_against_bandits_ready_peasant_start_practice.codeBlock = code



train_peasants_against_bandits_training_result = GameMenu("train_peasants_against_bandits_training_result", 512,
"{s0}"
)
def condition():
    reg5 = _g_train_peasants_against_bandits_num_peasants
    str_store_troop_name_by_count(s0,trp.trainee_peasant,_g_train_peasants_against_bandits_num_peasants)
    if _g_train_peasants_against_bandits_training_succeeded == 0:
        s0 = str_store_string("@You were beaten. The peasants are heartened by their success;;; but the lesson you wanted to teach them probably didn't get through...")
    else:
        s0 = str_store_string("@After beating your last opponent;;; you explain to the peasants how to better defend themselves against such an attack. Hopefully they'll take the experience on board and will be prepared next time.")
        quest_slot_001 = quest_get_slot(qst.train_peasants_against_bandits,11)
        quest_slot_001 += _g_train_peasants_against_bandits_num_peasants
        quest_set_slot(qst.train_peasants_against_bandits,11,quest_slot_001)
    #end
train_peasants_against_bandits_training_result.conditionBlock = condition

train_peasants_against_bandits_training_result_continue = MenuOption("continue", "Continue...")
def code():
    if True:
        quest_slot_001 = quest_get_slot(qst.train_peasants_against_bandits,11)
        if quest_slot_eq(qst.train_peasants_against_bandits,10,quest_slot_001):
            jump_to_menu(mnu.train_peasants_against_bandits_attack)
        else:
            change_screen_map()
        #end
    #end
train_peasants_against_bandits_training_result_continue.codeBlock = code



train_peasants_against_bandits_attack = GameMenu("train_peasants_against_bandits_attack", 0,
"As you get ready to continue the training, a sentry from the village runs up to you, shouting alarums. The bandits have been spotted on the horizon, riding hard for {s3}. The elder begs that you organize your newly-trained militia and face them."
)
def condition():
    s3 = str_store_party_name(_current_town)
train_peasants_against_bandits_attack.conditionBlock = condition

train_peasants_against_bandits_attack_peasants_against_bandits_attack_resist = MenuOption("peasants_against_bandits_attack_resist", "Prepare for a fight!")
def code():
    random_x_001 = store_random_in_range(0,3)
    if random_x_001 == 0:
        troop_id_002 = trp.bandit
    elif random_x_001 == 1:
        troop_id_002 = trp.mountain_bandit
    else:
        troop_id_002 = trp.forest_bandit
    #end
    party_slot_003 = party_get_slot(_g_encountered_party,10)
    modify_visitors_at_site(party_slot_003)
    reset_visitors()
    character_lvl_004 = store_character_level(trp.player)
    character_lvl_004 /= 2
    var005 = character_lvl_004 + 16
    var006 = var005 + 6
    random_x_001 = store_random_in_range(var005,var006)
    set_visitors(0,troop_id_002,random_x_001)
    number_of_troops_007 = var006
    set_visitors(2,trp.trainee_peasant,number_of_troops_007)
    set_party_battle_mode()
    set_battle_advantage(0)
    _g_battle_result = 0
    set_jump_mission(mt.village_attack_bandits)
    jump_to_scene(party_slot_003)
    _g_next_menu = mnu.train_peasants_against_bandits_attack_result
    jump_to_menu(mnu.battle_debrief)
    _g_mt_mode = 2
    change_screen_mission()
train_peasants_against_bandits_attack_peasants_against_bandits_attack_resist.codeBlock = code



train_peasants_against_bandits_attack_result = GameMenu("train_peasants_against_bandits_attack_result", 4608,
"{s9}"
)
def condition():
    if _g_battle_result == 1:
        s9 = str_store_string("@The bandits are broken! Those few who remain alive and conscious run off with their tails between their legs;;; terrified of the peasants and their new champion.")
        succeed_quest(qst.train_peasants_against_bandits)
        jump_to_menu(mnu.train_peasants_against_bandits_success)
    else:
        fail_quest(qst.train_peasants_against_bandits)
        s9 = str_store_string("@Try as you might;;; you could not defeat the bandits. Infuriated;;; they raze the village to the ground to punish the peasants;;; and then leave the burning wasteland behind to find greener pastures to plunder.")
        set_background_mesh(mesh.pic_looted_village)
    #end
train_peasants_against_bandits_attack_result.conditionBlock = condition

train_peasants_against_bandits_attack_result_continue = MenuOption("continue", "Continue...")
def code():
    if True:
        village_set_state(_current_town,2)
        party_set_slot(_current_town,36,0)
        party_set_slot(_current_town,37,0)
        change_player_relation_with_center(_g_encountered_party,-3)
        end_quest(qst.train_peasants_against_bandits)
    #end
    change_screen_map()
train_peasants_against_bandits_attack_result_continue.codeBlock = code



train_peasants_against_bandits_success = GameMenu("train_peasants_against_bandits_success", 512,
"The bandits are broken! Those few who remain run off with their tails between their legs, terrified of the peasants and their new champion. The villagers have little left in the way of wealth after their ordeal, but they offer you all they can find to show their gratitude."
)
def condition():
    party_clear(p.temp_party)
    end_quest(qst.train_peasants_against_bandits)
    change_player_relation_with_center(_g_encountered_party,4)
    party_slot_001 = party_get_slot(_current_town,25)
    for inventory_slot_no_002 in range(10, 106):
        random_x_003 = store_random_in_range(0,100)
        if random_x_003 < 50:
            troop_set_inventory_slot(party_slot_001,inventory_slot_no_002,-1)
        #end
    #end
    add_log_entry(4,trp.player,_current_town,-1,-1)
train_peasants_against_bandits_success.conditionBlock = condition

train_peasants_against_bandits_success_village_bandits_defeated_accept = MenuOption("village_bandits_defeated_accept", "Take it as your just due.")
def code():
    jump_to_menu(mnu.auto_return_to_map)
    party_slot_001 = party_get_slot(_current_town,25)
    troop_sort_inventory(party_slot_001)
    change_screen_loot(party_slot_001)
train_peasants_against_bandits_success_village_bandits_defeated_accept.codeBlock = code

train_peasants_against_bandits_success_village_bandits_defeated_cont = MenuOption("village_bandits_defeated_cont", "Refuse, stating that they need these items more than you do.")
def code():
    change_player_relation_with_center(_g_encountered_party,3)
    change_player_honor(1)
    change_screen_map()
train_peasants_against_bandits_success_village_bandits_defeated_cont.codeBlock = code



disembark = GameMenu("disembark", 0,
"Do you wish to disembark?"
)

disembark_disembark_yes = MenuOption("disembark_yes", "Yes.")
def code():
    _g_player_icon_state = 0
    party_set_flags(p.main_party,512,0)
    pos1 = party_get_position(p.main_party)
    party_set_position(p.main_party,0)
    if _g_main_ship_party <= 0:
        set_spawn_radius(0)
        spawn_around_party(p.main_party,pt.none)
        _g_main_ship_party = reg0
        party_set_flags(_g_main_ship_party,2115072,1)
        s1 = str_store_troop_name(trp.player)
        party_set_name(_g_main_ship_party,"@{s1}'s Ship")
        party_set_icon(_g_main_ship_party,1297036692682702876)
        party_set_slot(_g_main_ship_party,0,16)
    #end
    enable_party(_g_main_ship_party)
    party_set_position(_g_main_ship_party,0)
    party_set_icon(_g_main_ship_party,1297036692682702877)
    _g_main_ship_party = -1
    change_screen_return()
disembark_disembark_yes.codeBlock = code

disembark_disembark_no = MenuOption("disembark_no", "No.")
def code():
    change_screen_return()
disembark_disembark_no.codeBlock = code



ship_reembark = GameMenu("ship_reembark", 0,
"Do you wish to embark?"
)

ship_reembark_reembark_yes = MenuOption("reembark_yes", "Yes.")
def code():
    _g_player_icon_state = 2
    party_set_flags(p.main_party,512,1)
    pos1 = party_get_position(p.main_party)
    if map_get_water_position_around_position(2,1,6):
        party_set_position(p.main_party,2)
        _g_main_ship_party = _g_encountered_party
        disable_party(_g_encountered_party)
        change_screen_return()
ship_reembark_reembark_yes.codeBlock = code

ship_reembark_reembark_no = MenuOption("reembark_no", "No.")
def code():
    change_screen_return()
ship_reembark_reembark_no.codeBlock = code



center_reports = GameMenu("center_reports", 0,
"Town Name: {s1}^Rent Income: {reg1} denars^Tariff Income: {reg2} denars^Food Stock: for {reg3} days"
)
def condition():
    party_slot_001 = party_get_slot(_g_encountered_party,53)
    center_get_food_consumption(_g_encountered_party)
    var002 = reg0
    if var002 > 0:
        reg3 = party_slot_001 / var002
    else:
        reg3 = 9999
    #end
    s1 = str_store_party_name(_g_encountered_party)
    reg1 = party_get_slot(_g_encountered_party,47)
    reg2 = party_get_slot(_g_encountered_party,48)
center_reports.conditionBlock = condition

center_reports_to_price_and_productions = MenuOption("to_price_and_productions", "Show prices and productions.")
def code():
    jump_to_menu(mnu.price_and_production)
center_reports_to_price_and_productions.codeBlock = code

center_reports_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    if party_slot_eq(_g_encountered_party,0,4):
        jump_to_menu(mnu.village)
    else:
        jump_to_menu(mnu.town)
    #end
center_reports_go_back_dot.codeBlock = code



price_and_production = GameMenu("price_and_production", 0,
"Productions are:^(Note: base/modified by raw materials/modified by materials plus prosperity)^{s1}^^Price factors are:^{s2}"
)
def condition():
    var001 = 0
    var002 = 0
    for p_003 in range(p.town_1, p.castle_1):
        center_get_goods_availability(p_003)
        var001 += reg0
    #end
    for p_003 in range(p.village_1, p.salt_mine):
        center_get_goods_availability(p_003)
        var002 += reg0
    #end
    var002 /= 110
    var001 /= 22
    center_get_goods_availability(_g_encountered_party)
    reg1 = var001
    reg2 = var002
    if _cheat_mode >= 1:
        s1 = str_store_string(gstr.__hardship_index_reg0_avg_towns_reg1_avg_villages_reg2__)
        print("@{!}DEBUG - {s1}")
    #end
    for itm_004 in range(itm.spice, itm.siege_supply):
        if itm_004 != itm.pork and itm_004 != itm.chicken and itm_004 != itm.butter and itm_004 != itm.cattle_meat and itm_004 != itm.cabbages:
            center_get_production(_g_encountered_party,itm_004)
            var005 = reg0
            var006 = reg2
            var007 = reg1
            center_get_consumption(_g_encountered_party,itm_004)
            var008 = reg2
            var009 = reg1
            var010 = reg0
            slot_no_011 = itm_004 - itm.spice
            slot_no_011 += 250
            party_slot_012 = party_get_slot(_g_encountered_party,slot_no_011)
            var013 = 0
            var014 = 0
            var015 = 0
            var016 = 0
            for p_003 in range(p.town_1, p.salt_mine):
                if not is_between(p_003,p.castle_1,p.village_1):
                    var013 += 1
                    center_get_production(p_003,itm_004)
                    var017 = reg2
                    center_get_consumption(p_003,itm_004)
                    var018 = reg1 + reg2
                    party_slot_019 = party_get_slot(p_003,slot_no_011)
                    var014 += party_slot_019
                    var015 += var017
                    var016 += var018
                #end
            #end
        #end
        var020 = var015
        var021 = var016
        var014 /= var013
        var015 /= var013
        var016 /= var013
        s3 = str_store_item_name(itm_004)
        reg1 = var006
        reg2 = var007
        reg3 = var005
        reg4 = party_slot_012
        reg5 = var015
        reg6 = var014
        reg7 = var008
        reg8 = var009
        reg9 = var010
        reg10 = var016
        item_slot_022 = item_get_slot(itm_004,14)
        party_slot_023 = party_get_slot(_g_encountered_party,item_slot_022)
        reg11 = party_slot_023
        reg12 = var020
        reg13 = var021
        item_slot_024 = item_get_slot(itm_004,15)
        s4 = str_store_string(item_slot_024)
        s1 = str_store_string(gstr.__s3_price_equal_reg4_calradian_average_reg6_capital_reg11_s4_base_reg1modified_by_raw_material_reg2modified_by_prosperity_reg3_calradian_average_production_base_reg5_total_reg12_consumed_reg7used_as_raw_material_reg8modified_total_reg9_calradian_consumption_base_reg10_total_reg13s1_)
    #end
price_and_production.conditionBlock = condition

price_and_production_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    if party_slot_eq(_g_encountered_party,0,4):
        jump_to_menu(mnu.village)
    else:
        jump_to_menu(mnu.town)
    #end
price_and_production_go_back_dot.codeBlock = code



town_trade = GameMenu("town_trade", 0,
"You head towards the marketplace."
)

town_trade_assess_prices = MenuOption("assess_prices", "Assess the local prices.")
def condition():
    party_faction_001 = store_faction_of_party(_current_town)
    faction_relation_002 = store_relation(party_faction_001,fac.player_supporters_faction)
town_trade_assess_prices.conditionBlock = condition
def code():
    jump_to_menu(mnu.town_trade_assessment_begin)
town_trade_assess_prices.codeBlock = code

town_trade_trade_with_arms_merchant = MenuOption("trade_with_arms_merchant", "Trade with the arms merchant.")
def code():
    party_slot_001 = party_get_slot(_current_town,21)
    change_screen_trade(party_slot_001)
town_trade_trade_with_arms_merchant.codeBlock = code

town_trade_trade_with_armor_merchant = MenuOption("trade_with_armor_merchant", "Trade with the armor merchant.")
def code():
    party_slot_001 = party_get_slot(_current_town,22)
    change_screen_trade(party_slot_001)
town_trade_trade_with_armor_merchant.codeBlock = code

town_trade_trade_with_horse_merchant = MenuOption("trade_with_horse_merchant", "Trade with the horse merchant.")
def code():
    party_slot_001 = party_get_slot(_current_town,24)
    change_screen_trade(party_slot_001)
town_trade_trade_with_horse_merchant.codeBlock = code

town_trade_trade_with_goods_merchant = MenuOption("trade_with_goods_merchant", "Trade with the goods merchant.")
def code():
    party_slot_001 = party_get_slot(_current_town,23)
    change_screen_trade(party_slot_001)
town_trade_trade_with_goods_merchant.codeBlock = code

town_trade_back_to_town_menu = MenuOption("back_to_town_menu", "Head back.")
def code():
    jump_to_menu(mnu.town)
town_trade_back_to_town_menu.codeBlock = code



town_trade_assessment_begin = GameMenu("town_trade_assessment_begin", 0,
"You overhear several discussions about the price of trade goods across the local area.^You listen closely, trying to work out the best deals around."
)
def condition():
    str_clear(42)
town_trade_assessment_begin.conditionBlock = condition

town_trade_assessment_begin_continue = MenuOption("continue", "Continue...")
def code():
    _auto_enter_town = _current_town
    _g_town_assess_trade_goods_after_rest = 1
    get_max_skill_of_player_party(skl.trade)
    reg0 /= 2
    var001 = 6 - reg0
    _g_last_rest_center = _current_town
    _g_last_rest_payment_until = -1
    rest_for_hours(var001,5,0)
    change_screen_return()
town_trade_assessment_begin_continue.codeBlock = code

town_trade_assessment_begin_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    jump_to_menu(mnu.town_trade)
town_trade_assessment_begin_go_back_dot.codeBlock = code



town_trade_assessment = GameMenu("town_trade_assessment", 512,
"As the party member with the highest trade skill ({reg2}), {reg3?you try to figure out:{s1} tries to figure out} the best goods to trade in. {s2}"
)
def condition():
    get_max_skill_of_player_party(skl.trade)
    var001 = reg0
    var002 = reg1
    var003 = 0
    var004 = -1
    var005 = -1
    var006 = 0
    var007 = -1
    var008 = -1
    var009 = 0
    var010 = -1
    var011 = -1
    var012 = 0
    var013 = -1
    var014 = -1
    var015 = 0
    var016 = -1
    var017 = -1
    var018 = 0
    var019 = p.village_1
    var019 -= p.town_1
    var020 = itm.siege_supply
    var20 -= itm.spice
    var021 = var019 * var020
    var021 *= var001
    var021 /= 20
    party_id_022 = _g_encountered_party
    for var023 in range(0, var021):
        random_x_024 = store_random_in_range(itm.spice,itm.siege_supply)
        random_x_025 = store_random_in_range(p.town_1,p.castle_1)
        party_slot_026 = party_get_slot(party_id_022,23)
        var027 = 0
        for inventory_slot_no_028 in range(10, 106):
            troop_inv_slot_029 = troop_get_inventory_slot(party_slot_026,inventory_slot_no_028)
            if troop_inv_slot_029 == random_x_024:
                var027 += 1
            #end
        #end
        if var027 >= 1:
            var030 = 0
            if random_x_024 == var004 and random_x_025 == var005:
                var030 += 1
            #end
        #end
        if random_x_024 == var007 and random_x_025 == var008:
            var030 += 1
        #end
        if random_x_024 == var010 and random_x_025 == var011:
            var030 += 1
        #end
        if random_x_024 == var013 and random_x_025 == var014:
            var030 += 1
        #end
        if random_x_024 == var016 and random_x_025 == var017:
            var030 += 1
        #end
        if var030 <= 1:
            item_value_031 = store_item_value(random_x_024)
            _g_encountered_party = party_id_022
            game_get_item_buy_price_factor(random_x_024)
            var032 = item_value_031 * reg0
            var032 /= 100
            val_max(var032,1)
            _g_encountered_party = random_x_025
            game_get_item_sell_price_factor(random_x_024)
            var033 = item_value_031 * reg0
            var033 /= 100
            val_max(var033,1)
            var034 = var033 - var032
            if var004 == random_x_024 or var007 == random_x_024 or var010 == random_x_024 or var013 == random_x_024 or var016 == random_x_024:
                if var004 == random_x_024 and var034 > var006:
                    var004 = random_x_024
                    var005 = random_x_025
                    var006 = var034
                elif var007 == random_x_024 and var034 > var009:
                    var007 = random_x_024
                    var008 = random_x_025
                    var009 = var034
                elif var010 == random_x_024 and var034 > var012:
                    var010 = random_x_024
                    var011 = random_x_025
                    var012 = var034
                elif var013 == random_x_024 and var034 > var015:
                    var013 = random_x_024
                    var014 = random_x_025
                    var015 = var034
                elif var016 == random_x_024 and var034 > var018:
                    var016 = random_x_024
                    var017 = random_x_025
                    var018 = var034
                #end
            #end
        else:
            if var034 > var006:
                var003 += 1
                val_min(var003,5)
                var016 = var013
                var017 = var014
                var018 = var015
                var013 = var010
                var014 = var011
                var015 = var012
                var010 = var007
                var011 = var008
                var012 = var009
                var007 = var004
                var008 = var005
                var009 = var006
                var004 = random_x_024
                var005 = random_x_025
                var006 = var034
            elif var034 > var009:
                var003 += 1
                val_min(var003,5)
                var016 = var013
                var017 = var014
                var018 = var015
                var013 = var010
                var014 = var011
                var015 = var012
                var010 = var007
                var011 = var008
                var012 = var009
                var007 = random_x_024
                var008 = random_x_025
                var009 = var034
            elif var034 > var012:
                var003 += 1
                val_min(var003,5)
                var016 = var013
                var017 = var014
                var018 = var015
                var013 = var010
                var014 = var011
                var015 = var012
                var010 = random_x_024
                var011 = random_x_025
                var012 = var034
            elif var034 > var015:
                var003 += 1
                val_min(var003,5)
                var016 = var013
                var017 = var014
                var018 = var015
                var013 = random_x_024
                var014 = random_x_025
                var015 = var034
            elif var034 > var018:
                var003 += 1
                val_min(var003,5)
                var016 = var013
                var017 = var014
                var018 = var015
            #end
        #end
    #end
    _g_encountered_party = party_id_022
    str_clear(3)
    reg2 = var001
    if var002 == trp.player:
        reg3 = 1
    else:
        reg3 = 0
        s1 = str_store_troop_name(var002)
    #end
    if var003 <= 0:
        s2 = str_store_string("@However;;; {reg3?You are:{s1} is} unable to find any trade goods that would bring a profit.")
    else:
        if var016 >= 0:
            reg6 = var018
            s4 = str_store_item_name(var016)
            s5 = str_store_party_name(var017)
            s3 = str_store_string("@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}")
        #end
        if var013 >= 0:
            reg6 = var015
            s4 = str_store_item_name(var013)
            s5 = str_store_party_name(var014)
            s3 = str_store_string("@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}")
        #end
        if var010 >= 0:
            reg6 = var012
            s4 = str_store_item_name(var010)
            s5 = str_store_party_name(var011)
            s3 = str_store_string("@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}")
        #end
        if var007 >= 0:
            reg6 = var009
            s4 = str_store_item_name(var007)
            s5 = str_store_party_name(var008)
            s3 = str_store_string("@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}")
        #end
        if var004 >= 0:
            reg6 = var006
            s4 = str_store_item_name(var004)
            s5 = str_store_party_name(var005)
            s3 = str_store_string("@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}")
        #end
        s2 = str_store_string("@{reg3?You find:{s1} finds} out the following:^{s3}")
    #end
town_trade_assessment.conditionBlock = condition

town_trade_assessment_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.town_trade)
town_trade_assessment_continue.codeBlock = code



sneak_into_town_suceeded = GameMenu("sneak_into_town_suceeded", 0,
"Disguised in the garments of a poor pilgrim, you fool the guards and make your way into the town."
)

sneak_into_town_suceeded_continue = MenuOption("continue", "Continue...")
def code():
    _sneaked_into_town = 1
    jump_to_menu(mnu.town)
sneak_into_town_suceeded_continue.codeBlock = code



sneak_into_town_caught = GameMenu("sneak_into_town_caught", 0,
"As you try to sneak in, one of the guards recognizes you and raises the alarm! You must flee back through the gates before all the guards in the town come down on you!"
)
def condition():
    _auto_menu = mnu.captivity_start_castle_surrender
sneak_into_town_caught.conditionBlock = condition

sneak_into_town_caught_sneak_caught_fight = MenuOption("sneak_caught_fight", "Try to fight your way out!")
def code():
    _talk_context_list1 = [
    18,
    19,
    ]
    _all_doors_locked = 1
    party_slot_001 = party_get_slot(_current_town,10)
    modify_visitors_at_site(party_slot_001)
    reset_visitors()
    if _talk_context in _talk_context_list1:
        set_jump_entry(7)
    elif party_slot_eq(_current_town,0,3):
        set_jump_entry(0)
    else:
        set_jump_entry(1)
    #end
    set_jump_mission(mt.sneak_caught_fight)
    set_passage_menu(mnu.town)
    jump_to_scene(party_slot_001)
    change_screen_mission()
sneak_into_town_caught_sneak_caught_fight.codeBlock = code

sneak_into_town_caught_sneak_caught_surrender = MenuOption("sneak_caught_surrender", "Surrender.")
def code():
    jump_to_menu(mnu.captivity_start_castle_surrender)
sneak_into_town_caught_sneak_caught_surrender.codeBlock = code



sneak_into_town_caught_dispersed_guards = GameMenu("sneak_into_town_caught_dispersed_guards", 0,
"You drive off the guards and cover your trail before running off, easily losing your pursuers in the maze of streets."
)

sneak_into_town_caught_dispersed_guards_continue = MenuOption("continue", "Continue...")
def code():
    _sneaked_into_town = 1
    _town_entered = 1
    jump_to_menu(mnu.town)
sneak_into_town_caught_dispersed_guards_continue.codeBlock = code



sneak_into_town_caught_ran_away = GameMenu("sneak_into_town_caught_ran_away", 0,
"You make your way back through the gates and quickly retreat to the safety of the countryside.{s11}"
)
def condition():
    str_clear(11)
    var001 = 0
    var002 = trp.heroes_end
    for troop_id_003 in range(trp.npc1, var002):
        if troop_slot_eq(troop_id_003,149,4):
            _talk_context = 8
            reg14 = troop_id_003
            setup_troop_meeting(troop_id_003,-1)
            troop_set_slot(troop_id_003,149,-1)
            troop_slot_004 = troop_get_slot(troop_id_003,8)
            party_remove_prisoners(troop_slot_004,troop_id_003,1)
            troop_set_slot(troop_id_003,8,-1)
            var002 = -1
        elif troop_slot_eq(troop_id_003,149,5):
            s12 = str_store_troop_name(troop_id_003)
            if var001 == 0:
                s11 = str_store_string(gstr.s11_unfortunately_s12_was_wounded_and_had_to_be_left_behind)
            else:
                s11 = str_store_string(gstr.s11_also_s12_was_wounded_and_had_to_be_left_behind)
            #end
            var001 = 1
        #end
        troop_set_slot(troop_id_003,149,0)
    #end
sneak_into_town_caught_ran_away.conditionBlock = condition

sneak_into_town_caught_ran_away_continue = MenuOption("continue", "Continue...")
def code():
    _auto_menu = -1
    _last_sneak_attempt_town = store_encountered_party()
    _last_sneak_attempt_time = store_current_hours()
    change_screen_return()
sneak_into_town_caught_ran_away_continue.codeBlock = code



enemy_offer_ransom_for_prisoner = GameMenu("enemy_offer_ransom_for_prisoner", 0,
"{s2} offers you a sum of {reg12} denars in silver if you are willing to sell him {s1}."
)
def condition():
    calculate_ransom_amount_for_troop(_g_ransom_offer_troop)
    reg12 = reg0
    s1 = str_store_troop_name(_g_ransom_offer_troop)
    troop_faction_001 = store_faction_of_troop(_g_ransom_offer_troop)
    s2 = str_store_faction_name(troop_faction_001)
enemy_offer_ransom_for_prisoner.conditionBlock = condition

enemy_offer_ransom_for_prisoner_ransom_accept = MenuOption("ransom_accept", "Accept the offer.")
def code():
    troop_add_gold(trp.player,reg12)
    party_remove_prisoners(_g_ransom_offer_party,_g_ransom_offer_troop,1)
    remove_troop_from_prison(_g_ransom_offer_troop)
    if True:
        troop_type_001 = troop_get_type(trp.player)
        if troop_type_001 == 1:
            var002 = get_achievement_stat(75,0)
            var002 += 1
            set_achievement_stat(75,0,var002)
            if var002 == 3:
                unlock_achievement(75)
            #end
        #end
    #end
    change_screen_return()
enemy_offer_ransom_for_prisoner_ransom_accept.codeBlock = code

enemy_offer_ransom_for_prisoner_ransom_reject = MenuOption("ransom_reject", "Reject the offer.")
def code():
    change_player_relation_with_troop(_g_ransom_offer_troop,-4)
    change_player_honor(-1)
    _g_ransom_offer_rejected = 1
    change_screen_return()
enemy_offer_ransom_for_prisoner_ransom_reject.codeBlock = code



training_ground = GameMenu("training_ground", 0,
"You approach a training field where you can practice your martial skills. What kind of training do you want to do?"
)
def condition():
    _g_training_ground_melee_training_scene = scn.training_ground_ranged_melee_1
    _g_training_ground_melee_training_scene += _g_encountered_party
    _g_training_ground_melee_training_scene -= p.training_ground_1
    if _g_training_ground_training_count >= 3:
        _g_training_ground_training_count = 0
        rest_for_hours(1,5,1)
        _auto_enter_town = _g_encountered_party
        change_screen_return()
    #end
training_ground.conditionBlock = condition

training_ground_camp_trainer = MenuOption("camp_trainer", "Speak with the trainer.")
def code():
    set_jump_mission(mt.training_ground_trainer_talk)
    modify_visitors_at_site(_g_training_ground_melee_training_scene)
    reset_visitors()
    set_jump_entry(5)
    jump_to_scene(_g_training_ground_melee_training_scene)
    change_screen_mission()
    music_set_situation(0)
training_ground_camp_trainer.codeBlock = code

training_ground_camp_train_melee = MenuOption("camp_train_melee", "Sparring practice.")
def condition():
    if not troop_is_wounded(trp.player):
        party_count_fit_for_battle(p.main_party)
training_ground_camp_train_melee.conditionBlock = condition
def code():
    _g_mt_mode = 1
    jump_to_menu(mnu.training_ground_selection_details_melee_1)
    music_set_situation(0)
training_ground_camp_train_melee.codeBlock = code

training_ground_camp_train_archery = MenuOption("camp_train_archery", "Ranged weapon practice.")
def code():
    jump_to_menu(mnu.training_ground_selection_details_ranged_1)
    music_set_situation(0)
training_ground_camp_train_archery.codeBlock = code

training_ground_camp_train_mounted = MenuOption("camp_train_mounted", "Horseback practice.")
def code():
    _g_mt_mode = 3
    jump_to_menu(mnu.training_ground_selection_details_mounted)
    music_set_situation(0)
training_ground_camp_train_mounted.codeBlock = code

training_ground_go_to_track = MenuOption("go_to_track", "{!}Cheat: Go to track.")
def code():
    set_jump_mission(mt.ai_training)
    var001 = scn.training_ground_horse_track_1 + _g_encountered_party
    var001 -= p.training_ground_1
    jump_to_scene(var001)
    change_screen_mission()
training_ground_go_to_track.codeBlock = code

training_ground_go_to_range = MenuOption("go_to_range", "{!}Cheat: Go to range.")
def code():
    set_jump_mission(mt.ai_training)
    jump_to_scene(_g_training_ground_melee_training_scene)
    change_screen_mission()
training_ground_go_to_range.codeBlock = code

training_ground_leave = MenuOption("leave", "Leave.")
def code():
    change_screen_return()
training_ground_leave.codeBlock = code



training_ground_selection_details_melee_1 = GameMenu("training_ground_selection_details_melee_1", 0,
"How many opponents will you go against?"
)
def condition():
    write_fit_party_members_to_stack_selection(p.main_party,1)
    _temp = troop_get_slot(trp.stack_selection_amounts,1)
    _temp_2 = 1
training_ground_selection_details_melee_1.conditionBlock = condition

training_ground_selection_details_melee_1_camp_train_melee_num_men_1 = MenuOption("camp_train_melee_num_men_1", "One.")
def code():
    _temp = 1
    jump_to_menu(mnu.training_ground_selection_details_melee_2)
training_ground_selection_details_melee_1_camp_train_melee_num_men_1.codeBlock = code

training_ground_selection_details_melee_1_camp_train_melee_num_men_2 = MenuOption("camp_train_melee_num_men_2", "Two.")
def code():
    _temp = 2
    jump_to_menu(mnu.training_ground_selection_details_melee_2)
training_ground_selection_details_melee_1_camp_train_melee_num_men_2.codeBlock = code

training_ground_selection_details_melee_1_camp_train_melee_num_men_3 = MenuOption("camp_train_melee_num_men_3", "Three.")
def code():
    _temp = 3
    jump_to_menu(mnu.training_ground_selection_details_melee_2)
training_ground_selection_details_melee_1_camp_train_melee_num_men_3.codeBlock = code

training_ground_selection_details_melee_1_camp_train_melee_num_men_4 = MenuOption("camp_train_melee_num_men_4", "Four.")
def code():
    _temp = 4
    jump_to_menu(mnu.training_ground_selection_details_melee_2)
training_ground_selection_details_melee_1_camp_train_melee_num_men_4.codeBlock = code

training_ground_selection_details_melee_1_go_back_dot = MenuOption("go_back_dot", "Cancel.")
def code():
    jump_to_menu(mnu.training_ground)
training_ground_selection_details_melee_1_go_back_dot.codeBlock = code



training_ground_selection_details_melee_2 = GameMenu("training_ground_selection_details_melee_2", 0,
"Choose your opponent #{reg1}:"
)
def condition():
    reg1 = _temp_2
    _temp_3 = troop_get_slot(trp.stack_selection_amounts,0)
training_ground_selection_details_melee_2.conditionBlock = condition

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(1)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(2)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(3)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(4)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(5)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(6)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(7)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(8)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(9)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(10)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(11)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(12)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(13)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(14)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(15)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(16)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(17)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(18)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(19)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_s0 = MenuOption("s0", "{s0}")
def code():
    training_ground_sub_routine_2_for_melee_details(20)
training_ground_selection_details_melee_2_s0.codeBlock = code

training_ground_selection_details_melee_2_training_ground_selection_details_melee_random = MenuOption("training_ground_selection_details_melee_random", "Choose randomly.")
def code():
    training_ground_sub_routine_2_for_melee_details(-1)
training_ground_selection_details_melee_2_training_ground_selection_details_melee_random.codeBlock = code

training_ground_selection_details_melee_2_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    jump_to_menu(mnu.training_ground)
training_ground_selection_details_melee_2_go_back_dot.codeBlock = code



training_ground_selection_details_mounted = GameMenu("training_ground_selection_details_mounted", 0,
"What kind of weapon do you want to train with?"
)

training_ground_selection_details_mounted_camp_train_mounted_details_1 = MenuOption("camp_train_mounted_details_1", "One handed weapon.")
def code():
    start_training_at_training_ground(2,0)
training_ground_selection_details_mounted_camp_train_mounted_details_1.codeBlock = code

training_ground_selection_details_mounted_camp_train_mounted_details_2 = MenuOption("camp_train_mounted_details_2", "Polearm.")
def code():
    start_training_at_training_ground(4,0)
training_ground_selection_details_mounted_camp_train_mounted_details_2.codeBlock = code

training_ground_selection_details_mounted_camp_train_mounted_details_3 = MenuOption("camp_train_mounted_details_3", "Bow.")
def code():
    start_training_at_training_ground(8,0)
training_ground_selection_details_mounted_camp_train_mounted_details_3.codeBlock = code

training_ground_selection_details_mounted_camp_train_mounted_details_4 = MenuOption("camp_train_mounted_details_4", "Thrown weapon.")
def code():
    start_training_at_training_ground(10,0)
training_ground_selection_details_mounted_camp_train_mounted_details_4.codeBlock = code

training_ground_selection_details_mounted_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    jump_to_menu(mnu.training_ground)
training_ground_selection_details_mounted_go_back_dot.codeBlock = code



training_ground_selection_details_ranged_1 = GameMenu("training_ground_selection_details_ranged_1", 0,
"What kind of ranged weapon do you want to train with?"
)

training_ground_selection_details_ranged_1_camp_train_ranged_weapon_bow = MenuOption("camp_train_ranged_weapon_bow", "Bow and arrows.")
def code():
    _g_mt_mode = 2
    _temp = 8
    jump_to_menu(mnu.training_ground_selection_details_ranged_2)
training_ground_selection_details_ranged_1_camp_train_ranged_weapon_bow.codeBlock = code

training_ground_selection_details_ranged_1_camp_train_ranged_weapon_crossbow = MenuOption("camp_train_ranged_weapon_crossbow", "Crossbow.")
def code():
    _g_mt_mode = 2
    _temp = 9
    jump_to_menu(mnu.training_ground_selection_details_ranged_2)
training_ground_selection_details_ranged_1_camp_train_ranged_weapon_crossbow.codeBlock = code

training_ground_selection_details_ranged_1_camp_train_ranged_weapon_thrown = MenuOption("camp_train_ranged_weapon_thrown", "Throwing Knives.")
def code():
    _g_mt_mode = 2
    _temp = 10
    jump_to_menu(mnu.training_ground_selection_details_ranged_2)
training_ground_selection_details_ranged_1_camp_train_ranged_weapon_thrown.codeBlock = code

training_ground_selection_details_ranged_1_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    jump_to_menu(mnu.training_ground)
training_ground_selection_details_ranged_1_go_back_dot.codeBlock = code



training_ground_selection_details_ranged_2 = GameMenu("training_ground_selection_details_ranged_2", 0,
"What range do you want to practice at?"
)

training_ground_selection_details_ranged_2_camp_train_ranged_details_1 = MenuOption("camp_train_ranged_details_1", "10 yards.")
def code():
    start_training_at_training_ground(_temp,10)
training_ground_selection_details_ranged_2_camp_train_ranged_details_1.codeBlock = code

training_ground_selection_details_ranged_2_camp_train_ranged_details_2 = MenuOption("camp_train_ranged_details_2", "20 yards.")
def code():
    start_training_at_training_ground(_temp,20)
training_ground_selection_details_ranged_2_camp_train_ranged_details_2.codeBlock = code

training_ground_selection_details_ranged_2_camp_train_ranged_details_3 = MenuOption("camp_train_ranged_details_3", "30 yards.")
def code():
    start_training_at_training_ground(_temp,30)
training_ground_selection_details_ranged_2_camp_train_ranged_details_3.codeBlock = code

training_ground_selection_details_ranged_2_camp_train_ranged_details_4 = MenuOption("camp_train_ranged_details_4", "40 yards.")
def code():
    start_training_at_training_ground(_temp,40)
training_ground_selection_details_ranged_2_camp_train_ranged_details_4.codeBlock = code

training_ground_selection_details_ranged_2_camp_train_ranged_details_5 = MenuOption("camp_train_ranged_details_5", "50 yards.")
def code():
    start_training_at_training_ground(_temp,50)
training_ground_selection_details_ranged_2_camp_train_ranged_details_5.codeBlock = code

training_ground_selection_details_ranged_2_camp_train_ranged_details_6 = MenuOption("camp_train_ranged_details_6", "60 yards.")
def code():
    start_training_at_training_ground(_temp,60)
training_ground_selection_details_ranged_2_camp_train_ranged_details_6.codeBlock = code

training_ground_selection_details_ranged_2_camp_train_ranged_details_7 = MenuOption("camp_train_ranged_details_7", "70 yards.")
def code():
    start_training_at_training_ground(_temp,70)
training_ground_selection_details_ranged_2_camp_train_ranged_details_7.codeBlock = code

training_ground_selection_details_ranged_2_go_back_dot = MenuOption("go_back_dot", "Go back.")
def code():
    jump_to_menu(mnu.training_ground)
training_ground_selection_details_ranged_2_go_back_dot.codeBlock = code



training_ground_description = GameMenu("training_ground_description", 0,
"{s0}"
)

training_ground_description_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_scene(_g_training_ground_training_scene)
    change_screen_mission()
training_ground_description_continue.codeBlock = code



training_ground_training_result = GameMenu("training_ground_training_result", 512,
"{s7}{s2}"
)
def condition():
    skill_lvl_001 = store_skill_level(skl.trainer,trp.player)
    var002 = 5 + skill_lvl_001
    write_fit_party_members_to_stack_selection(p.main_party,1)
    str_clear(2)
    troop_slot_003 = troop_get_slot(trp.stack_selection_amounts,1)
    troop_slot_004 = troop_get_slot(trp.stack_selection_amounts,0)
    if _g_training_ground_training_success_ratio > 0:
        var005 = _g_training_ground_training_success_ratio * _g_training_ground_training_success_ratio
        if _g_training_ground_training_success_ratio == 100:
            var005 *= 2
        #end
        if _g_mt_mode == 1:
            var005 /= 2
        #end
        var005 /= 10
        if troop_slot_003 > 8:
            var005 *= 3
            var006 = troop_slot_003
            convert_to_fixed_point(var006)
            var006 = store_sqrt(var006)
            convert_to_fixed_point(var005)
            var005 /= var006
        #end
        var007 = var005 * var002
        var007 /= 10
        party_num_companions_stacks_008 = party_get_num_companion_stacks(p.main_party)
        var009 = troop_slot_004 + 2
        for slot_no_010 in range(2, var009):
            troop_slot_011 = troop_get_slot(trp.stack_selection_amounts,slot_no_010)
            troop_slot_012 = troop_get_slot(trp.stack_selection_ids,slot_no_010)
            var013 = party_num_companions_stacks_008
            for stack_no_014 in range(0, var013):
                troop_id_015 = party_stack_get_troop_id(p.main_party,stack_no_014)
                if troop_id_015 == troop_slot_012:
                    var013 = 0
                    if cf_training_ground_sub_routine_for_training_result(troop_slot_012,stack_no_014,troop_slot_011,var007):
                        str_store_troop_name_by_count(s1,troop_slot_012,troop_slot_011)
                        reg1 = troop_slot_011
                        s2 = str_store_string("@{s2}^{reg1} {s1} earned {reg0} experience.")
                    #end
                #end
            #end
        #end
        if _g_mt_mode == 1:
            var016 = var005 * 3
            var016 /= 2
            for slot_no_017 in range(0, _g_training_ground_training_num_enemies):
                troop_slot_012 = troop_get_slot(trp.temp_array_a,slot_no_017)
                var013 = party_num_companions_stacks_008
                for stack_no_014 in range(0, var013):
                    troop_id_015 = party_stack_get_troop_id(p.main_party,stack_no_014)
                    if troop_id_015 == troop_slot_012:
                        var013 = 0
                        if cf_training_ground_sub_routine_for_training_result(troop_slot_012,stack_no_014,1,var016):
                            s1 = str_store_troop_name(troop_slot_012)
                            s2 = str_store_string("@{s2}^{s1} earned an additional {reg0} experience.")
                        #end
                    #end
                #end
            #end
        #end
        if cf_training_ground_sub_routine_for_training_result(trp.player,-1,1,var005):
            s2 = str_store_string("@^You earned {reg0} experience.{s2}")
        #end
    #end
    if _g_training_ground_training_success_ratio == 0:
        s7 = str_store_string("@The training didn't go well at all.")
    elif _g_training_ground_training_success_ratio < 25:
        s7 = str_store_string("@The training didn't go well at all.")
    elif _g_training_ground_training_success_ratio < 50:
        s7 = str_store_string("@The training didn't go very well.")
    elif _g_training_ground_training_success_ratio < 75:
        s7 = str_store_string("@The training went quite well.")
    elif _g_training_ground_training_success_ratio < 99:
        s7 = str_store_string("@The training went very well.")
    else:
        s7 = str_store_string("@The training went perfectly.")
    #end
training_ground_training_result.conditionBlock = condition

training_ground_training_result_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.training_ground)
training_ground_training_result_continue.codeBlock = code



marshall_selection_candidate_ask = GameMenu("marshall_selection_candidate_ask", 0,
"{s15} will soon select a new marshall for {s23}. Some of the lords have suggested your name as a likely candidate."
)
def condition():
    if _g_presentation_marshall_selection_ended == 1:
        change_screen_return()
    #end
    faction_slot_001 = faction_get_slot(_players_kingdom,11)
    s15 = str_store_troop_name(faction_slot_001)
    s23 = str_store_faction_name(_players_kingdom)
marshall_selection_candidate_ask.conditionBlock = condition

marshall_selection_candidate_ask_marshall_candidate_accept = MenuOption("marshall_candidate_accept", "Let {s15} learn that you are willing to serve as marshall.")
def code():
    start_presentation(prsnt.marshall_selection)
marshall_selection_candidate_ask_marshall_candidate_accept.codeBlock = code

marshall_selection_candidate_ask_marshall_candidate_reject = MenuOption("marshall_candidate_reject", "Tell everyone that you are too busy these days.")
def code():
    if _g_presentation_marshall_selection_max_renown_2_troop == trp.player:
        _g_presentation_marshall_selection_max_renown_2 = _g_presentation_marshall_selection_max_renown_3
        _g_presentation_marshall_selection_max_renown_2_troop = _g_presentation_marshall_selection_max_renown_3_troop
    else:
        _g_presentation_marshall_selection_max_renown_1 = _g_presentation_marshall_selection_max_renown_2
        _g_presentation_marshall_selection_max_renown_1_troop = _g_presentation_marshall_selection_max_renown_2_troop
        _g_presentation_marshall_selection_max_renown_2 = _g_presentation_marshall_selection_max_renown_3
        _g_presentation_marshall_selection_max_renown_2_troop = _g_presentation_marshall_selection_max_renown_3_troop
    #end
    start_presentation(prsnt.marshall_selection)
marshall_selection_candidate_ask_marshall_candidate_reject.codeBlock = code



captivity_avoid_wilderness = GameMenu("captivity_avoid_wilderness", 0,
"Suddenly all the world goes black around you. Many hours later you regain your conciousness and find yourself at the spot you fell. Your enemies must have taken you up for dead and left you there. However, it seems that none of your wound were lethal, and altough you feel awful, you find out that can still walk. You get up and try to look for any other survivors from your party."
)



captivity_start_wilderness = GameMenu("captivity_start_wilderness", 0,
"Stub"
)
def condition():
    _g_player_is_captive = 1
    if _g_player_surrenders == 1:
        jump_to_menu(mnu.captivity_start_wilderness_surrender)
    else:
        jump_to_menu(mnu.captivity_start_wilderness_defeat)
    #end
captivity_start_wilderness.conditionBlock = condition



captivity_start_wilderness_surrender = GameMenu("captivity_start_wilderness_surrender", 0,
"Stub"
)
def condition():
    _g_player_is_captive = 1
    _auto_menu = -1
    _capturer_party = _g_encountered_party
    jump_to_menu(mnu.captivity_wilderness_taken_prisoner)
captivity_start_wilderness_surrender.conditionBlock = condition



captivity_start_wilderness_defeat = GameMenu("captivity_start_wilderness_defeat", 0,
"Your enemies take you prisoner."
)
def condition():
    _g_player_is_captive = 1
    _auto_menu = -1
    _capturer_party = _g_encountered_party
    if True:
        troop_id_001 = party_stack_get_troop_id(_g_encountered_party,0)
        if is_between(troop_id_001,trp.npc1,trp.knight_1_1_wife) and troop_slot_eq(troop_id_001,2,2):
            var002 = troop_id_001 - trp.npc1
            set_achievement_stat(7,var002,1)
        #end
    #end
    jump_to_menu(mnu.captivity_wilderness_taken_prisoner)
captivity_start_wilderness_defeat.conditionBlock = condition



captivity_start_castle_surrender = GameMenu("captivity_start_castle_surrender", 0,
"Stub"
)
def condition():
    _g_player_is_captive = 1
    _auto_menu = -1
    _capturer_party = _g_encountered_party
    jump_to_menu(mnu.captivity_castle_taken_prisoner)
captivity_start_castle_surrender.conditionBlock = condition



captivity_start_castle_defeat = GameMenu("captivity_start_castle_defeat", 0,
"Stub"
)
def condition():
    _g_player_is_captive = 1
    _auto_menu = -1
    _capturer_party = _g_encountered_party
    jump_to_menu(mnu.captivity_castle_taken_prisoner)
captivity_start_castle_defeat.conditionBlock = condition



captivity_start_under_siege_defeat = GameMenu("captivity_start_under_siege_defeat", 0,
"Your enemies take you prisoner."
)
def condition():
    _g_player_is_captive = 1
    _auto_menu = -1
    _capturer_party = _g_encountered_party
    jump_to_menu(mnu.captivity_castle_taken_prisoner)
captivity_start_under_siege_defeat.conditionBlock = condition



captivity_wilderness_taken_prisoner = GameMenu("captivity_wilderness_taken_prisoner", 4096,
"Your enemies take you prisoner."
)
def condition():
    set_background_mesh(mesh.pic_prisoner_wilderness)
captivity_wilderness_taken_prisoner.conditionBlock = condition

captivity_wilderness_taken_prisoner_continue = MenuOption("continue", "Continue...")
def code():
    set_camera_follow_party(_capturer_party)
    _g_player_is_captive = 1
    random_x_001 = store_random_in_range(18,30)
    event_player_captured_as_prisoner()
    stay_captive_for_hours(random_x_001)
    _auto_menu = mnu.captivity_wilderness_check
    change_screen_return()
captivity_wilderness_taken_prisoner_continue.codeBlock = code



captivity_wilderness_check = GameMenu("captivity_wilderness_check", 0,
"stub"
)
def condition():
    jump_to_menu(mnu.captivity_end_wilderness_escape)
captivity_wilderness_check.conditionBlock = condition



captivity_end_wilderness_escape = GameMenu("captivity_end_wilderness_escape", 4096,
"After painful days of being dragged about as a prisoner, you find a chance and escape from your captors!"
)
def condition():
    play_cue_track(track.escape)
    troop_type_001 = troop_get_type(trp.player)
    if troop_type_001 == 1:
        set_background_mesh(mesh.pic_escape_1_fem)
    else:
        set_background_mesh(mesh.pic_escape_1)
    #end
captivity_end_wilderness_escape.conditionBlock = condition

captivity_end_wilderness_escape_continue = MenuOption("continue", "Continue...")
def code():
    _g_player_is_captive = 0
    if party_is_active(_capturer_party):
        party_relocate_near_party(p.main_party,_capturer_party,2)
    #end
    set_parties_around_player_ignore_player(8,12)
    _g_player_icon_state = 0
    set_camera_follow_party(p.main_party)
    rest_for_hours(0,0,0)
    change_screen_return()
captivity_end_wilderness_escape_continue.codeBlock = code



captivity_castle_taken_prisoner = GameMenu("captivity_castle_taken_prisoner", 0,
"You are quickly surrounded by guards who take away your weapons. With curses and insults, they throw you into the dungeon where you must while away the miserable days of your captivity."
)
def condition():
    troop_type_001 = troop_get_type(trp.player)
    if troop_type_001 == 1:
        set_background_mesh(mesh.pic_prisoner_fem)
    else:
        set_background_mesh(mesh.pic_prisoner_man)
    #end
captivity_castle_taken_prisoner.conditionBlock = condition

captivity_castle_taken_prisoner_continue = MenuOption("continue", "Continue...")
def code():
    _g_player_is_captive = 1
    random_x_001 = store_random_in_range(16,22)
    event_player_captured_as_prisoner()
    stay_captive_for_hours(random_x_001)
    _auto_menu = mnu.captivity_castle_check
    change_screen_return()
captivity_castle_taken_prisoner_continue.codeBlock = code



captivity_rescue_lord_taken_prisoner = GameMenu("captivity_rescue_lord_taken_prisoner", 0,
"You remain in disguise for as long as possible before revealing yourself. The guards are outraged and beat you savagely before throwing you back into the cell for God knows how long..."
)
def condition():
    troop_type_001 = troop_get_type(trp.player)
    if troop_type_001 == 1:
        set_background_mesh(mesh.pic_prisoner_fem)
    else:
        set_background_mesh(mesh.pic_prisoner_man)
    #end
captivity_rescue_lord_taken_prisoner.conditionBlock = condition

captivity_rescue_lord_taken_prisoner_continue = MenuOption("continue", "Continue...")
def code():
    _g_player_is_captive = 1
    random_x_001 = store_random_in_range(16,22)
    event_player_captured_as_prisoner()
    stay_captive_for_hours(random_x_001)
    _auto_menu = mnu.captivity_castle_check
    change_screen_return()
captivity_rescue_lord_taken_prisoner_continue.codeBlock = code



captivity_castle_check = GameMenu("captivity_castle_check", 0,
"stub"
)
def condition():
    reg7 = store_random_in_range(0,10)
    if party_is_active(_capturer_party):
        party_faction_001 = store_faction_of_party(_capturer_party)
        if is_between(party_faction_001,fac.player_supporters_faction,fac.kingdoms_end):
            faction_relation_002 = store_relation(party_faction_001,fac.player_faction)
            if faction_relation_002 >= 0:
                jump_to_menu(mnu.captivity_end_exchanged_with_prisoner)
            elif reg7 < 4:
                character_lvl_003 = store_character_level(trp.player)
                _player_ransom_amount = character_lvl_003 * 50
                _player_ransom_amount += 100
                reg3 = store_troop_gold(trp.player)
                var004 = reg3 / 20
                _player_ransom_amount += var004
                if reg3 > _player_ransom_amount:
                    jump_to_menu(mnu.captivity_end_propose_ransom)
                elif reg7 < 7:
                    jump_to_menu(mnu.captivity_end_exchanged_with_prisoner)
                else:
                    jump_to_menu(mnu.captivity_castle_remain)
                #end
            #end
        #end
    #end
captivity_castle_check.conditionBlock = condition



captivity_end_exchanged_with_prisoner = GameMenu("captivity_end_exchanged_with_prisoner", 0,
"After days of imprisonment, you are finally set free when your captors exchange you with another prisoner."
)
def condition():
    play_cue_track(track.escape)
captivity_end_exchanged_with_prisoner.conditionBlock = condition

captivity_end_exchanged_with_prisoner_continue = MenuOption("continue", "Continue...")
def code():
    _g_player_is_captive = 0
    if party_is_active(_capturer_party):
        party_relocate_near_party(p.main_party,_capturer_party,2)
    #end
    set_parties_around_player_ignore_player(8,12)
    _g_player_icon_state = 0
    set_camera_follow_party(p.main_party)
    rest_for_hours(0,0,0)
    change_screen_return()
captivity_end_exchanged_with_prisoner_continue.codeBlock = code



captivity_end_propose_ransom = GameMenu("captivity_end_propose_ransom", 0,
"You spend long hours in the sunless dank of the dungeon, more than you can count. Suddenly one of your captors enters your cell with an offer; he proposes to free you in return for {reg5} denars of your hidden wealth. You decide to..."
)
def condition():
    reg5 = _player_ransom_amount
captivity_end_propose_ransom.conditionBlock = condition

captivity_end_propose_ransom_captivity_end_ransom_accept = MenuOption("captivity_end_ransom_accept", "Accept the offer.")
def condition():
    troop_gold_001 = store_troop_gold(trp.player)
captivity_end_propose_ransom_captivity_end_ransom_accept.conditionBlock = condition
def code():
    play_cue_track(track.escape)
    _g_player_is_captive = 0
    troop_remove_gold(trp.player,_player_ransom_amount)
    if party_is_active(_capturer_party):
        party_relocate_near_party(p.main_party,_capturer_party,1)
    #end
    set_parties_around_player_ignore_player(8,12)
    _g_player_icon_state = 0
    set_camera_follow_party(p.main_party)
    rest_for_hours(0,0,0)
    change_screen_return()
captivity_end_propose_ransom_captivity_end_ransom_accept.codeBlock = code

captivity_end_propose_ransom_captivity_end_ransom_deny = MenuOption("captivity_end_ransom_deny", "Refuse him, wait for something better.")
def code():
    _g_player_is_captive = 1
    reg8 = store_random_in_range(16,22)
    stay_captive_for_hours(reg8)
    _auto_menu = mnu.captivity_castle_check
    change_screen_return()
captivity_end_propose_ransom_captivity_end_ransom_deny.codeBlock = code



captivity_castle_remain = GameMenu("captivity_castle_remain", 4608,
"More days pass in the darkness of your cell. You get through them as best you can, enduring the kicks and curses of the guards, watching your underfed body waste away more and more..."
)
def condition():
    troop_type_001 = troop_get_type(trp.player)
    if troop_type_001 == 1:
        set_background_mesh(mesh.pic_prisoner_fem)
    else:
        set_background_mesh(mesh.pic_prisoner_man)
    #end
    random_x_002 = store_random_in_range(16,22)
    stay_captive_for_hours(random_x_002)
    _auto_menu = mnu.captivity_castle_check
captivity_castle_remain.conditionBlock = condition

captivity_castle_remain_continue = MenuOption("continue", "Continue...")
def code():
    _g_player_is_captive = 1
    change_screen_return()
captivity_castle_remain_continue.codeBlock = code



kingdom_army_quest_report_to_army = GameMenu("kingdom_army_quest_report_to_army", 4096,
"{s8} sends word that he wishes you to join {reg4?her:his} new military campaign. You need to bring at least {reg13} troops to the army, and are instructed to raise more men with all due haste if you do not have enough."
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    quest_slot_001 = quest_get_slot(qst.report_to_army,2)
    quest_slot_002 = quest_get_slot(qst.report_to_army,10)
    get_information_about_troops_position(quest_slot_001,0)
    str_clear(9)
    if reg0 == 1:
        s9 = str_store_string(1)
    #end
    s8 = str_store_troop_name(quest_slot_001)
    reg13 = quest_slot_002
    reg4 = troop_get_type(quest_slot_001)
kingdom_army_quest_report_to_army.conditionBlock = condition

kingdom_army_quest_report_to_army_continue = MenuOption("continue", "Continue...")
def code():
    quest_slot_001 = quest_get_slot(qst.report_to_army,2)
    quest_slot_002 = quest_get_slot(qst.report_to_army,10)
    s13 = str_store_troop_name_link(quest_slot_001)
    reg13 = quest_slot_002
    setup_quest_text(qst.report_to_army)
    s2 = str_store_string("@{s13} asked you to report to him with at least {reg13} troops.")
    start_quest(qst.report_to_army,quest_slot_001)
    report_quest_troop_positions(qst.report_to_army,quest_slot_001,3)
    change_screen_return()
kingdom_army_quest_report_to_army_continue.codeBlock = code



kingdom_army_quest_messenger = GameMenu("kingdom_army_quest_messenger", 4096,
"{s8} sends word that he wishes to speak with you about a task he needs performed. He requests you to come and see him as soon as possible."
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    faction_slot_001 = faction_get_slot(_players_kingdom,8)
    s8 = str_store_troop_name(faction_slot_001)
kingdom_army_quest_messenger.conditionBlock = condition

kingdom_army_quest_messenger_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
kingdom_army_quest_messenger_continue.codeBlock = code



kingdom_army_quest_join_siege_order = GameMenu("kingdom_army_quest_join_siege_order", 4096,
"{s8} sends word that you are to join the siege of {s9} in preparation for a full assault. Your troops are to take {s9} at all costs."
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    faction_slot_001 = faction_get_slot(_players_kingdom,8)
    quest_slot_002 = quest_get_slot(qst.join_siege_with_army,1)
    s8 = str_store_troop_name(faction_slot_001)
    s9 = str_store_party_name(quest_slot_002)
kingdom_army_quest_join_siege_order.conditionBlock = condition

kingdom_army_quest_join_siege_order_continue = MenuOption("continue", "Continue...")
def code():
    end_quest(qst.follow_army)
    quest_slot_001 = quest_get_slot(qst.join_siege_with_army,1)
    faction_slot_002 = faction_get_slot(_players_kingdom,8)
    s13 = str_store_troop_name_link(faction_slot_002)
    s14 = str_store_party_name_link(quest_slot_001)
    setup_quest_text(qst.join_siege_with_army)
    s2 = str_store_string("@{s13} ordered you to join the assault against {s14}.")
    start_quest(qst.join_siege_with_army,faction_slot_002)
    change_screen_return()
kingdom_army_quest_join_siege_order_continue.codeBlock = code



kingdom_army_follow_failed = GameMenu("kingdom_army_follow_failed", 4096,
"You have failed to follow {s8}. The marshal assumes that you were otherwise engaged, but would have appreciated your support."
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    faction_slot_001 = faction_get_slot(_players_kingdom,8)
    s8 = str_store_troop_name(faction_slot_001)
    abort_quest(qst.follow_army,1)
kingdom_army_follow_failed.conditionBlock = condition

kingdom_army_follow_failed_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
kingdom_army_follow_failed_continue.codeBlock = code



invite_player_to_faction_without_center = GameMenu("invite_player_to_faction_without_center", 4096,
"You receive an offer of vassalage!^^ {s8} of {s9} has sent a royal herald to bring you an invititation in his own hand. You would be granted the honour of becoming a vassal {lord/lady} of {s9}, and in return {s8} asks you to swear an oath of homage to him and fight in his military campaigns, although he offers you no lands or titles. He will surely be offended if you do not take the offer..."
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    _g_invite_faction_lord = faction_get_slot(_g_invite_faction,11)
    s8 = str_store_troop_name(_g_invite_faction_lord)
    s9 = str_store_faction_name(_g_invite_faction)
invite_player_to_faction_without_center.conditionBlock = condition

invite_player_to_faction_without_center_faction_accept = MenuOption("faction_accept", "Accept!")
def code():
    s1 = str_store_troop_name(_g_invite_faction_lord)
    setup_quest_text(qst.join_faction)
    s3 = str_store_troop_name_link(_g_invite_faction_lord)
    s4 = str_store_faction_name_link(_g_invite_faction)
    quest_set_slot(qst.join_faction,6,_g_invite_faction_lord)
    quest_set_slot(qst.join_faction,23,30)
    quest_set_slot(qst.join_faction,26,0)
    s2 = str_store_string("@Find and speak with {s3} of {s4} to give him your oath of homage.")
    start_quest(qst.join_faction,_g_invite_faction_lord)
    report_quest_troop_positions(qst.join_faction,_g_invite_faction_lord,3)
    jump_to_menu(mnu.invite_player_to_faction_accepted)
invite_player_to_faction_without_center_faction_accept.codeBlock = code

invite_player_to_faction_without_center_faction_reject = MenuOption("faction_reject", "Decline the invitation.")
def code():
    change_player_relation_with_troop(_g_invite_faction_lord,-3)
    change_player_relation_with_faction(_g_invite_faction,-10)
    _g_invite_faction = 0
    _g_invite_faction_lord = 0
    _g_invite_offered_center = 0
    change_screen_return()
invite_player_to_faction_without_center_faction_reject.codeBlock = code



invite_player_to_faction = GameMenu("invite_player_to_faction", 4096,
"You receive an offer of vassalage!^^ {s8} of {s9} has sent a royal herald to bring you an invititation in his own hand. You would be granted the honour of becoming a vassal {lord/lady} of {s9}, and in return {s8} asks you to swear an oath of homage to him and fight in his military campaigns, offering you the fief of {s2} for your loyal service. He will surely be offended if you do not take the offer..."
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    _g_invite_faction_lord = faction_get_slot(_g_invite_faction,11)
    s8 = str_store_troop_name(_g_invite_faction_lord)
    s9 = str_store_faction_name(_g_invite_faction)
    s2 = str_store_party_name(_g_invite_offered_center)
invite_player_to_faction.conditionBlock = condition

invite_player_to_faction_faction_accept = MenuOption("faction_accept", "Accept!")
def code():
    s1 = str_store_troop_name(_g_invite_faction_lord)
    setup_quest_text(qst.join_faction)
    s3 = str_store_troop_name_link(_g_invite_faction_lord)
    s4 = str_store_faction_name_link(_g_invite_faction)
    quest_set_slot(qst.join_faction,6,_g_invite_faction_lord)
    quest_set_slot(qst.join_faction,23,30)
    s2 = str_store_string("@Find and speak with {s3} of {s4} to give him your oath of homage.")
    start_quest(qst.join_faction,_g_invite_faction_lord)
    report_quest_troop_positions(qst.join_faction,_g_invite_faction_lord,3)
    jump_to_menu(mnu.invite_player_to_faction_accepted)
invite_player_to_faction_faction_accept.codeBlock = code

invite_player_to_faction_faction_reject = MenuOption("faction_reject", "Decline the invitation.")
def code():
    change_player_relation_with_troop(_g_invite_faction_lord,-3)
    _g_invite_faction = 0
    _g_invite_faction_lord = 0
    _g_invite_offered_center = 0
    change_screen_return()
invite_player_to_faction_faction_reject.codeBlock = code



invite_player_to_faction_accepted = GameMenu("invite_player_to_faction_accepted", 0,
"In order to become a vassal, you must swear an oath of homage to {s3}. You shall have to find him and give him your oath in person. {s5}"
)
def condition():
    get_information_about_troops_position(_g_invite_faction_lord,0)
    s3 = str_store_troop_name(_g_invite_faction_lord)
    s5 = str_store_string("@{!}{s1}")
invite_player_to_faction_accepted.conditionBlock = condition

invite_player_to_faction_accepted_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
invite_player_to_faction_accepted_continue.codeBlock = code



question_peace_offer = GameMenu("question_peace_offer", 0,
"You Receive a Peace Offer^^The {s1} offers you a peace agreement. What is your answer?"
)
def condition():
    s1 = str_store_faction_name(_g_notification_var1)
    set_fixed_point_multiplier(100)
    position_set_x(0,65)
    position_set_y(0,30)
    position_set_z(0,170)
    # set_game_menu_tableau_mesh(tab.faction_note_mesh_banner,_g_notification_var1,0)
question_peace_offer.conditionBlock = condition

question_peace_offer_peace_offer_accept = MenuOption("peace_offer_accept", "Accept")
def code():
    diplomacy_start_peace_between_kingdoms(fac.player_supporters_faction,_g_notification_var1,1)
    change_screen_return()
question_peace_offer_peace_offer_accept.codeBlock = code

question_peace_offer_peace_offer_reject = MenuOption("peace_offer_reject", "Reject")
def code():
    change_player_relation_with_faction(_g_notification_var1,-5)
    change_screen_return()
question_peace_offer_peace_offer_reject.codeBlock = code



notification_truce_expired = GameMenu("notification_truce_expired", 0,
"Truce Has Expired^^The truce between {s1} and {s2} has expired."
)
def condition():
    s1 = str_store_faction_name(_g_notification_var1)
    s2 = str_store_faction_name(_g_notification_var2)
    set_fixed_point_multiplier(100)
    position_set_x(0,65)
    position_set_y(0,30)
    position_set_z(0,170)
    # set_game_menu_tableau_mesh(tab.faction_note_mesh_banner,_g_notification_var1,0)
notification_truce_expired.conditionBlock = condition

notification_truce_expired_continue = MenuOption("continue", "Continue")
def code():
    change_screen_return()
notification_truce_expired_continue.codeBlock = code



notification_feast_quest_expired = GameMenu("notification_feast_quest_expired", 0,
"{s10}"
)
def condition():
    s10 = str_store_string(gstr.feast_quest_expired)
notification_feast_quest_expired.conditionBlock = condition

notification_feast_quest_expired_continue = MenuOption("continue", "Continue")
def code():
    change_screen_return()
notification_feast_quest_expired_continue.codeBlock = code



notification_sortie_possible = GameMenu("notification_sortie_possible", 0,
"Enemy Sighted: Enemies have been sighted outside the walls of {s4}, and {s5} and others are preparing for a sortie. You may join them if you wish."
)
def condition():
    s4 = str_store_party_name(_g_notification_var1)
    troop_id_001 = party_stack_get_troop_id(_g_notification_var2,0)
    s5 = str_store_troop_name(troop_id_001)
notification_sortie_possible.conditionBlock = condition

notification_sortie_possible_continue = MenuOption("continue", "Continue")
def code():
    change_screen_return()
notification_sortie_possible_continue.codeBlock = code



notification_casus_belli_expired = GameMenu("notification_casus_belli_expired", 0,
"Kingdom Fails to Respond^^The {s1} has not responded to the {s2}'s provocations, and {s3} suffers a loss of face among {reg4?her:his} more bellicose subjects...^"
)
def condition():
    s1 = str_store_faction_name(_g_notification_var1)
    s2 = str_store_faction_name(_g_notification_var2)
    faction_slot_001 = faction_get_slot(_g_notification_var1,11)
    s3 = str_store_troop_name(faction_slot_001)
    reg4 = troop_get_type(faction_slot_001)
    set_fixed_point_multiplier(100)
    position_set_x(0,65)
    position_set_y(0,30)
    position_set_z(0,170)
    # set_game_menu_tableau_mesh(tab.faction_note_mesh_banner,_g_notification_var1,0)
notification_casus_belli_expired.conditionBlock = condition

notification_casus_belli_expired_continue = MenuOption("continue", "Continue")
def code():
    faction_follows_controversial_policy(_g_notification_var1,81)
    change_screen_return()
notification_casus_belli_expired_continue.codeBlock = code



notification_lord_defects = GameMenu("notification_lord_defects", 0,
"Defection: {s4} has abandoned the {s5} and joined the {s7}, taking {reg4?her:his} his fiefs with him"
)
def condition():
    troop_id_001 = _g_notification_var1
    var002 = _g_notification_var2
    s4 = str_store_troop_name(troop_id_001)
    s5 = str_store_faction_name(var002)
    troop_faction_003 = store_faction_of_troop(troop_id_001)
    s7 = str_store_faction_name(troop_faction_003)
    reg4 = troop_get_type(troop_id_001)
notification_lord_defects.conditionBlock = condition

notification_lord_defects_continue = MenuOption("continue", "Continue")
def code():
    change_screen_return()
notification_lord_defects_continue.codeBlock = code



notification_treason_indictment = GameMenu("notification_treason_indictment", 0,
"Treason Indictment^^{s9}"
)
def condition():
    troop_id_001 = _g_notification_var1
    faction_id_002 = _g_notification_var2
    faction_slot_003 = faction_get_slot(faction_id_002,11)
    if troop_id_001 == trp.player:
        s7 = str_store_troop_name(faction_slot_003)
        s9 = str_store_string(gstr.you_have_been_indicted_for_treason_to_s7_your_properties_have_been_confiscated_and_you_would_be_well_advised_to_flee_for_your_life)
    else:
        s4 = str_store_troop_name(troop_id_001)
        s5 = str_store_faction_name(faction_id_002)
        s6 = str_store_troop_name(faction_slot_003)
        reg4 = troop_get_type(troop_id_001)
        troop_faction_004 = store_faction_of_troop(troop_id_001)
        if is_between(troop_faction_004,fac.player_supporters_faction,fac.kingdoms_end):
            s10 = str_store_faction_name(troop_faction_004)
            s11 = str_store_string(gstr.with_the_s10)
        else:
            s11 = str_store_string(gstr.outside_calradia)
        #end
        s9 = str_store_string(gstr.by_order_of_s6_s4_of_the_s5_has_been_indicted_for_treason_the_lord_has_been_stripped_of_all_reg4herhis_properties_and_has_fled_for_reg4herhis_life_he_is_rumored_to_have_gone_into_exile_s11)
    #end
notification_treason_indictment.conditionBlock = condition

notification_treason_indictment_continue = MenuOption("continue", "Continue")
def code():
    change_screen_return()
notification_treason_indictment_continue.codeBlock = code



notification_border_incident = GameMenu("notification_border_incident", 0,
"Border incident^^Word reaches you that {s9}. Though you don't know whether or not the rumors are true, you do know one thing -- this seemingly minor incident has raised passions among the {s4}, making it easier for them to go to war against the {s3}, if they want it..."
)
def condition():
    party_id_001 = _g_notification_var1
    var002 = _g_notification_var2
    party_faction_003 = store_faction_of_party(party_id_001)
    if var002 == -1:
        party_slot_004 = party_get_slot(party_id_001,61)
        if party_slot_004 == party_faction_003 or not faction_slot_eq(party_slot_004,21,0):
            party_slot_004 = party_get_slot(party_id_001,62)
        #end
        s1 = str_store_party_name(party_id_001)
        s3 = str_store_faction_name(party_faction_003)
        s4 = str_store_faction_name(party_slot_004)
        faction_slot_005 = faction_get_slot(party_slot_004,11)
        s5 = str_store_troop_name(faction_slot_005)
        s9 = str_store_string(gstr.local_notables_from_s1_a_village_claimed_by_the_s4_have_been_mistreated_by_their_overlords_from_the_s3_and_petition_s5_for_protection)
        display_log_message("@There has been an alleged border incident: {s9}")
        add_log_entry(75,party_id_001,-1,-1,party_faction_003)
    else:
        party_slot_004 = store_faction_of_party(var002)
        s1 = str_store_party_name(party_id_001)
        s2 = str_store_party_name(var002)
        random_x_006 = store_random_in_range(0,3)
        if random_x_006 == 0:
            s9 = str_store_string(gstr.villagers_from_s1_stole_some_cattle_from_s2)
            display_log_message("@There has been an alleged border incident: {s9}")
            add_log_entry(72,party_id_001,var002,-1,party_faction_003)
        elif random_x_006 == 1:
            s9 = str_store_string(gstr.villagers_from_s1_abducted_a_woman_from_a_prominent_family_in_s2_to_marry_one_of_their_boys)
            display_log_message("@There has been an alleged border incident: {s9}")
            add_log_entry(73,party_id_001,var002,-1,party_faction_003)
        elif random_x_006 == 2:
            s9 = str_store_string(gstr.villagers_from_s1_killed_some_farmers_from_s2_in_a_fight_over_the_diversion_of_a_stream)
            display_log_message("@There has been an alleged border incident: {s9}")
            add_log_entry(74,party_id_001,var002,-1,party_faction_003)
        #end
    #end
    s3 = str_store_faction_name(party_faction_003)
    s4 = str_store_faction_name(party_slot_004)
    slot_no_007 = party_faction_003 + 130
    slot_no_007 -= fac.player_supporters_faction
    faction_set_slot(party_slot_004,slot_no_007,30)
notification_border_incident.conditionBlock = condition

notification_border_incident_continue = MenuOption("continue", "Continue")
def code():
    change_screen_return()
notification_border_incident_continue.codeBlock = code



notification_player_faction_active = GameMenu("notification_player_faction_active", 0,
"You now possess land in your name, without being tied to any kingdom. This makes you a monarch in your own right, with your court temporarily located at {s12}. However, the other kings in Calradia will at first consider you a threat, for if any upstart warlord can grab a throne, then their own legitimacy is called into question.^^You may find it desirable at this time to pledge yourself to an existing kingdom. If you want to continue as a sovereign monarch, then your first priority should be to establish an independent right to rule. You can establish your right to rule through several means -- marrying into a high-born family, recruiting new lords, governing your lands, treating with other kings, or dispatching your companions on missions.^^At any rate, your first step should be to appoint a chief minister from among your companions, to handle affairs of state. Different companions have different capabilities.^You may appoint new ministers from time to time. You may also change the location of your court, by speaking to the minister."
)
def condition():
    set_fixed_point_multiplier(100)
    position_set_x(0,65)
    position_set_y(0,30)
    position_set_z(0,170)
    # set_game_menu_tableau_mesh(tab.faction_note_mesh_banner,fac.player_supporters_faction,0)
    unlock_achievement(52)
    play_track(track.coronation)
    for p_001 in range(p.town_1, p.village_1):
        if _g_player_court < p.town_1:
            party_faction_002 = store_faction_of_party(p_001)
            if party_faction_002 == fac.player_supporters_faction:
                _g_player_court = p_001
                if True:
                    troop_slot_003 = troop_get_slot(trp.player,30)
                    if is_between(troop_slot_003,trp.knight_1_1_wife,trp.heroes_end):
                        troop_set_slot(troop_slot_003,12,_g_player_court)
                    #end
                #end
            #end
        #end
        s12 = str_store_party_name(_g_player_court)
    #end
notification_player_faction_active.conditionBlock = condition

notification_player_faction_active_appoint_spouse = MenuOption("appoint_spouse", "Appoint your wife, {s10}...")
def condition():
    if troop_slot_ge(trp.player,30,1):
        troop_slot_001 = troop_get_slot(trp.player,30)
        if not troop_slot_eq(troop_slot_001,2,2):
            s10 = str_store_troop_name(troop_slot_001)
notification_player_faction_active_appoint_spouse.conditionBlock = condition
def code():
    troop_slot_001 = troop_get_slot(trp.player,30)
    _g_player_minister = troop_slot_001
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_spouse.codeBlock = code

notification_player_faction_active_appoint_npc1 = MenuOption("appoint_npc1", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc1):
        s10 = str_store_troop_name(trp.npc1)
notification_player_faction_active_appoint_npc1.conditionBlock = condition
def code():
    _g_player_minister = trp.npc1
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc1.codeBlock = code

notification_player_faction_active_appoint_npc2 = MenuOption("appoint_npc2", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc2):
        s10 = str_store_troop_name(trp.npc2)
notification_player_faction_active_appoint_npc2.conditionBlock = condition
def code():
    _g_player_minister = trp.npc2
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc2.codeBlock = code

notification_player_faction_active_appoint_npc3 = MenuOption("appoint_npc3", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc3):
        s10 = str_store_troop_name(trp.npc3)
notification_player_faction_active_appoint_npc3.conditionBlock = condition
def code():
    _g_player_minister = trp.npc3
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc3.codeBlock = code

notification_player_faction_active_appoint_npc4 = MenuOption("appoint_npc4", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc4):
        s10 = str_store_troop_name(trp.npc4)
notification_player_faction_active_appoint_npc4.conditionBlock = condition
def code():
    _g_player_minister = trp.npc4
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc4.codeBlock = code

notification_player_faction_active_appoint_npc5 = MenuOption("appoint_npc5", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc5):
        s10 = str_store_troop_name(trp.npc5)
notification_player_faction_active_appoint_npc5.conditionBlock = condition
def code():
    _g_player_minister = trp.npc5
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc5.codeBlock = code

notification_player_faction_active_appoint_npc6 = MenuOption("appoint_npc6", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc6):
        s10 = str_store_troop_name(trp.npc6)
notification_player_faction_active_appoint_npc6.conditionBlock = condition
def code():
    _g_player_minister = trp.npc6
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc6.codeBlock = code

notification_player_faction_active_appoint_npc7 = MenuOption("appoint_npc7", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc7):
        s10 = str_store_troop_name(trp.npc7)
notification_player_faction_active_appoint_npc7.conditionBlock = condition
def code():
    _g_player_minister = trp.npc7
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc7.codeBlock = code

notification_player_faction_active_appoint_npc8 = MenuOption("appoint_npc8", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc8):
        s10 = str_store_troop_name(trp.npc8)
notification_player_faction_active_appoint_npc8.conditionBlock = condition
def code():
    _g_player_minister = trp.npc8
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc8.codeBlock = code

notification_player_faction_active_appoint_npc9 = MenuOption("appoint_npc9", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc9):
        s10 = str_store_troop_name(trp.npc9)
notification_player_faction_active_appoint_npc9.conditionBlock = condition
def code():
    _g_player_minister = trp.npc9
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc9.codeBlock = code

notification_player_faction_active_appoint_npc10 = MenuOption("appoint_npc10", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc10):
        s10 = str_store_troop_name(trp.npc10)
notification_player_faction_active_appoint_npc10.conditionBlock = condition
def code():
    _g_player_minister = trp.npc10
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc10.codeBlock = code

notification_player_faction_active_appoint_npc11 = MenuOption("appoint_npc11", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc11):
        s10 = str_store_troop_name(trp.npc11)
notification_player_faction_active_appoint_npc11.conditionBlock = condition
def code():
    _g_player_minister = trp.npc11
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc11.codeBlock = code

notification_player_faction_active_appoint_npc12 = MenuOption("appoint_npc12", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc12):
        s10 = str_store_troop_name(trp.npc12)
notification_player_faction_active_appoint_npc12.conditionBlock = condition
def code():
    _g_player_minister = trp.npc12
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc12.codeBlock = code

notification_player_faction_active_appoint_npc13 = MenuOption("appoint_npc13", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc13):
        s10 = str_store_troop_name(trp.npc13)
notification_player_faction_active_appoint_npc13.conditionBlock = condition
def code():
    _g_player_minister = trp.npc13
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc13.codeBlock = code

notification_player_faction_active_appoint_npc14 = MenuOption("appoint_npc14", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc14):
        s10 = str_store_troop_name(trp.npc14)
notification_player_faction_active_appoint_npc14.conditionBlock = condition
def code():
    _g_player_minister = trp.npc14
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc14.codeBlock = code

notification_player_faction_active_appoint_npc15 = MenuOption("appoint_npc15", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc15):
        s10 = str_store_troop_name(trp.npc15)
notification_player_faction_active_appoint_npc15.conditionBlock = condition
def code():
    _g_player_minister = trp.npc15
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc15.codeBlock = code

notification_player_faction_active_appoint_npc16 = MenuOption("appoint_npc16", "Appoint {s10}")
def condition():
    if main_party_has_troop(trp.npc16):
        s10 = str_store_troop_name(trp.npc16)
notification_player_faction_active_appoint_npc16.conditionBlock = condition
def code():
    _g_player_minister = trp.npc16
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_npc16.codeBlock = code

notification_player_faction_active_appoint_default = MenuOption("appoint_default", "Appoint a prominent citizen from the area...")
def code():
    _g_player_minister = trp.temporary_minister
    troop_set_faction(trp.temporary_minister,fac.player_supporters_faction)
    jump_to_menu(mnu.minister_confirm)
notification_player_faction_active_appoint_default.codeBlock = code



minister_confirm = GameMenu("minister_confirm", 0,
"{s9}can be found at your court in {s12}. You should consult periodically, to avoid the accumulation of unresolved issues that may sap your authority..."
)
def condition():
    if _players_kingdom_name_set == 1:
        change_screen_return()
    #end
    if _g_player_minister == trp.temporary_minister:
        s9 = str_store_string(gstr.your_new_minister_)
    else:
        s10 = str_store_troop_name(_g_player_minister)
        s9 = str_store_string(gstr.s10_is_your_new_minister_and_)
    #end
    if main_party_has_troop(_g_player_minister):
        remove_member_from_party(_g_player_minister,p.main_party)
    #end
minister_confirm.conditionBlock = condition

minister_confirm_continue = MenuOption("continue", "Continue...")
def code():
    start_presentation(prsnt.name_kingdom)
minister_confirm_continue.codeBlock = code



notification_court_lost = GameMenu("notification_court_lost", 0,
"{s12}"
)
def condition():
    if is_between(_g_player_court,p.town_1,p.salt_mine):
        s10 = str_store_party_name(_g_player_court)
        s11 = str_store_party_name(_g_player_court)
    else:
        s10 = str_store_string(gstr.your_previous_court_some_time_ago)
        s11 = str_store_string(gstr.your_previous_court_some_time_ago)
    #end
    _g_player_court = -1
    s14 = str_store_string(gstr.after_to_the_fall_of_s11_your_court_has_nowhere_to_go)
    if faction_slot_eq(fac.player_supporters_faction,21,2):
        s14 = str_store_string(gstr.as_you_no_longer_maintain_an_independent_kingdom_you_no_longer_maintain_a_court)
    #end
    for p_001 in range(p.town_1, p.village_1):
        if _g_player_court == -1:
            party_faction_002 = store_faction_of_party(p_001)
            if party_faction_002 == fac.player_supporters_faction and not party_slot_ge(p_001,7,trp.npc1):
                _g_player_court = p_001
                if True:
                    troop_slot_003 = troop_get_slot(trp.player,30)
                    if is_between(troop_slot_003,trp.knight_1_1_wife,trp.heroes_end):
                        troop_set_slot(troop_slot_003,12,_g_player_court)
                        s11 = str_store_party_name(_g_player_court)
                    #end
                #end
            #end
        #end
        s14 = str_store_string(gstr.due_to_the_fall_of_s10_your_court_has_been_relocated_to_s12)
    #end
    for p_001 in range(p.town_1, p.village_1):
        if _g_player_court == -1:
            party_faction_002 = store_faction_of_party(p_001)
            if party_faction_002 == fac.player_supporters_faction:
                _g_player_court = p_001
                if True:
                    troop_slot_003 = troop_get_slot(trp.player,30)
                    if is_between(troop_slot_003,trp.knight_1_1_wife,trp.heroes_end):
                        troop_set_slot(troop_slot_003,12,_g_player_court)
                    #end
                #end
            #end
        #end
        party_slot_004 = party_get_slot(p_001,7)
        s11 = str_store_party_name(_g_player_court)
        s9 = str_store_troop_name(party_slot_004)
        s14 = str_store_string(gstr.after_to_the_fall_of_s10_your_faithful_vassal_s9_has_invited_your_court_to_s11_)
    #end
    if faction_slot_eq(fac.player_supporters_faction,21,2):
        s14 = str_store_string(gstr.as_you_no_longer_maintain_an_independent_kingdom_you_no_longer_maintain_a_court)
    #end
    s12 = str_store_string(14)
notification_court_lost.conditionBlock = condition

notification_court_lost_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_court_lost_continue.codeBlock = code



notification_player_faction_deactive = GameMenu("notification_player_faction_deactive", 0,
"Your kingdom no longer holds any land."
)
def condition():
    set_fixed_point_multiplier(100)
    position_set_x(0,65)
    position_set_y(0,30)
    position_set_z(0,170)
    # set_game_menu_tableau_mesh(tab.faction_note_mesh_banner,fac.player_supporters_faction,0)
notification_player_faction_deactive.conditionBlock = condition

notification_player_faction_deactive_continue = MenuOption("continue", "Continue...")
def code():
    if True:
        pass
    #end
    _g_player_minister = -1
    change_screen_return()
notification_player_faction_deactive_continue.codeBlock = code



notification_player_wedding_day = GameMenu("notification_player_wedding_day", 4096,
"{s8} wishes to inform you that preparations for your wedding at {s10} have been complete, and that your presence is expected imminently ."
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    s8 = str_store_troop_name(_g_notification_var1)
    s10 = str_store_party_name(_g_notification_var2)
notification_player_wedding_day.conditionBlock = condition

notification_player_wedding_day_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_player_wedding_day_continue.codeBlock = code



notification_player_kingdom_holds_feast = GameMenu("notification_player_kingdom_holds_feast", 4096,
"{s11}"
)
def condition():
    set_background_mesh(mesh.pic_messenger)
    s8 = str_store_troop_name(_g_notification_var1)
    troop_faction_001 = store_faction_of_troop(_g_notification_var1)
    s9 = str_store_faction_name(troop_faction_001)
    s10 = str_store_party_name(_g_notification_var2)
    str_clear(12)
    if check_quest_active(qst.wed_betrothed):
        quest_slot_002 = quest_get_slot(qst.wed_betrothed,6)
        troop_faction_003 = store_faction_of_troop(quest_slot_002)
        if troop_faction_003 == _players_kingdom:
            s12 = str_store_string(gstr.feast_wedding_opportunity)
        #end
    #end
    s11 = str_store_string(gstr.s8_wishes_to_inform_you_that_the_lords_of_s9_will_be_gathering_for_a_feast_at_his_great_hall_in_s10_and_invites_you_to_be_part_of_this_august_assembly)
    if _g_notification_var1 == 0:
        s11 = str_store_string(gstr.the_great_lords_of_your_kingdom_plan_to_gather_at_your_hall_in_s10_for_a_feast)
    #end
    s11 = str_store_string("@{!}{s11}{s12}")
    if _cheat_mode >= 1:
        cur_hours_004 = store_current_hours()
        faction_slot_005 = faction_get_slot(_players_kingdom,94)
        cur_hours_004 -= faction_slot_005
        reg4 = cur_hours_004
        print("@{!}DEBUG -- Hours since last feast started: {reg4}")
    #end
notification_player_kingdom_holds_feast.conditionBlock = condition

notification_player_kingdom_holds_feast_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_player_kingdom_holds_feast_continue.codeBlock = code



notification_center_under_siege = GameMenu("notification_center_under_siege", 0,
"{s1} has been besieged by {s2} of {s3}!"
)
def condition():
    s1 = str_store_party_name(_g_notification_var1)
    s2 = str_store_troop_name(_g_notification_var2)
    troop_faction_001 = store_faction_of_troop(_g_notification_var2)
    s3 = str_store_faction_name(troop_faction_001)
    set_fixed_point_multiplier(100)
    position_set_x(0,62)
    position_set_y(0,30)
    position_set_z(0,170)
    # set_game_menu_tableau_mesh(tab.center_note_mesh,_g_notification_var1,0)
notification_center_under_siege.conditionBlock = condition

notification_center_under_siege_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_center_under_siege_continue.codeBlock = code



notification_village_raided = GameMenu("notification_village_raided", 0,
"Enemies have Laid Waste to a Fief^^{s1} has been raided by {s2} of {s3}!"
)
def condition():
    s1 = str_store_party_name(_g_notification_var1)
    s2 = str_store_troop_name(_g_notification_var2)
    troop_faction_001 = store_faction_of_troop(_g_notification_var2)
    s3 = str_store_faction_name(troop_faction_001)
    set_fixed_point_multiplier(100)
    position_set_x(0,62)
    position_set_y(0,30)
    position_set_z(0,170)
    # set_game_menu_tableau_mesh(tab.center_note_mesh,_g_notification_var1,0)
notification_village_raided.conditionBlock = condition

notification_village_raided_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_village_raided_continue.codeBlock = code



notification_village_raid_started = GameMenu("notification_village_raid_started", 0,
"Your Village is under Attack!^^{s2} of {s3} is laying waste to {s1}."
)
def condition():
    s1 = str_store_party_name(_g_notification_var1)
    s2 = str_store_troop_name(_g_notification_var2)
    troop_faction_001 = store_faction_of_troop(_g_notification_var2)
    s3 = str_store_faction_name(troop_faction_001)
    set_fixed_point_multiplier(100)
    position_set_x(0,62)
    position_set_y(0,30)
    position_set_z(0,170)
    # set_game_menu_tableau_mesh(tab.center_note_mesh,_g_notification_var1,0)
notification_village_raid_started.conditionBlock = condition

notification_village_raid_started_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_village_raid_started_continue.codeBlock = code



notification_one_faction_left = GameMenu("notification_one_faction_left", 0,
"Calradia Conquered by One Kingdom^^{s1} has defeated all rivals and stands as the sole kingdom."
)
def condition():
    s1 = str_store_faction_name(_g_notification_var1)
    set_fixed_point_multiplier(100)
    position_set_x(0,65)
    position_set_y(0,30)
    position_set_z(0,170)
    #if is_between(_g_notification_var1,fac.kingdom_1,fac.kingdoms_end):
    #    set_game_menu_tableau_mesh(tab.faction_note_mesh_for_menu,_g_notification_var1,0)
    #else:
    #    set_game_menu_tableau_mesh(tab.faction_note_mesh_banner,_g_notification_var1,0)
    #end
    if faction_slot_eq(_g_notification_var1,11,trp.player):
        unlock_achievement(44)
    else:
        unlock_achievement(53)
    #end
    if True:
        troop_type_001 = troop_get_type(trp.player)
        if troop_type_001 == 1:
            unlock_achievement(78)
        #end
    #end
notification_one_faction_left.conditionBlock = condition

notification_one_faction_left_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_one_faction_left_continue.codeBlock = code



notification_oath_renounced_faction_defeated = GameMenu("notification_oath_renounced_faction_defeated", 0,
"Your Old Faction was Defeated^^You won the battle against {s1}! This ends your struggle which started after you renounced your oath to them."
)
def condition():
    s1 = str_store_faction_name(_g_notification_var1)
    set_fixed_point_multiplier(100)
    position_set_x(0,65)
    position_set_y(0,30)
    position_set_z(0,170)
    #if is_between(_g_notification_var1,fac.kingdom_1,fac.kingdoms_end):
    #    set_game_menu_tableau_mesh(tab.faction_note_mesh_for_menu,_g_notification_var1,0)
    #else:
    #    set_game_menu_tableau_mesh(tab.faction_note_mesh_banner,_g_notification_var1,0)
    #end
notification_oath_renounced_faction_defeated.conditionBlock = condition

notification_oath_renounced_faction_defeated_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_oath_renounced_faction_defeated_continue.codeBlock = code



notification_center_lost = GameMenu("notification_center_lost", 0,
"An Estate was Lost^^You have lost {s1} to {s2}."
)
def condition():
    s1 = str_store_party_name(_g_notification_var1)
    s2 = str_store_faction_name(_g_notification_var2)
    set_fixed_point_multiplier(100)
    position_set_x(0,62)
    position_set_y(0,30)
    position_set_z(0,170)
    # set_game_menu_tableau_mesh(tab.center_note_mesh,_g_notification_var1,0)
notification_center_lost.conditionBlock = condition

notification_center_lost_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_center_lost_continue.codeBlock = code



notification_troop_left_players_faction = GameMenu("notification_troop_left_players_faction", 0,
"Betrayal!^^{s1} has left {s2} and joined {s3}."
)
def condition():
    s1 = str_store_troop_name(_g_notification_var1)
    s2 = str_store_faction_name(_players_kingdom)
    s3 = str_store_faction_name(_g_notification_var2)
    set_fixed_point_multiplier(100)
    position_set_x(0,55)
    position_set_y(0,20)
    position_set_z(0,100)
    # set_game_menu_tableau_mesh(tab.troop_note_mesh,_g_notification_var1,0)
notification_troop_left_players_faction.conditionBlock = condition

notification_troop_left_players_faction_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_troop_left_players_faction_continue.codeBlock = code



notification_troop_joined_players_faction = GameMenu("notification_troop_joined_players_faction", 0,
"Good news!^^ {s1} has left {s2} and joined {s3}."
)
def condition():
    s1 = str_store_troop_name(_g_notification_var1)
    s2 = str_store_faction_name(_g_notification_var2)
    s3 = str_store_faction_name(_players_kingdom)
    set_fixed_point_multiplier(100)
    position_set_x(0,55)
    position_set_y(0,20)
    position_set_z(0,100)
    # set_game_menu_tableau_mesh(tab.troop_note_mesh,_g_notification_var1,0)
notification_troop_joined_players_faction.conditionBlock = condition

notification_troop_joined_players_faction_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_troop_joined_players_faction_continue.codeBlock = code



notification_war_declared = GameMenu("notification_war_declared", 0,
"Declaration of War^^{s1} has declared war against {s2}!"
)
def condition():
    if True:
        s1 = str_store_faction_name(_g_notification_var1)
        s2 = str_store_faction_name(_g_notification_var2)
    #end
    set_fixed_point_multiplier(100)
    position_set_x(0,65)
    position_set_y(0,30)
    position_set_z(0,170)
    var001 = _g_notification_var1 - fac.player_supporters_faction
    var002 = _g_notification_var2 - fac.player_supporters_faction
    var001 *= 128
    var001 += var002
    # set_game_menu_tableau_mesh(tab.two_factions_mesh,var001,0)
notification_war_declared.conditionBlock = condition

notification_war_declared_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_war_declared_continue.codeBlock = code



notification_peace_declared = GameMenu("notification_peace_declared", 0,
"Peace Agreement^^{s1} and {s2} have made peace!^{s57}"
)
def condition():
    if 1 == 0 and _g_include_diplo_explanation == _g_notification_var1:
        _g_include_diplo_explanation = 0
    else:
        str_clear(57)
    #end
    s1 = str_store_faction_name(_g_notification_var1)
    s2 = str_store_faction_name(_g_notification_var2)
    set_fixed_point_multiplier(100)
    position_set_x(0,65)
    position_set_y(0,30)
    position_set_z(0,170)
    var001 = _g_notification_var1 - fac.player_supporters_faction
    var002 = _g_notification_var2 - fac.player_supporters_faction
    var001 *= 128
    var001 += var002
    # set_game_menu_tableau_mesh(tab.two_factions_mesh,var001,0)
notification_peace_declared.conditionBlock = condition

notification_peace_declared_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_peace_declared_continue.codeBlock = code



notification_faction_defeated = GameMenu("notification_faction_defeated", 0,
"Faction Eliminated^^{s1} is no more!"
)
def condition():
    s1 = str_store_faction_name(_g_notification_var1)
    set_fixed_point_multiplier(100)
    position_set_x(0,65)
    position_set_y(0,30)
    position_set_z(0,170)
    #if is_between(_g_notification_var1,fac.kingdom_1,fac.kingdoms_end):
    #    set_game_menu_tableau_mesh(tab.faction_note_mesh_for_menu,_g_notification_var1,0)
    #else:
    #    set_game_menu_tableau_mesh(tab.faction_note_mesh_banner,_g_notification_var1,0)
    #end
notification_faction_defeated.conditionBlock = condition

notification_faction_defeated_continue = MenuOption("continue", "Continue...")
def code():
    _g_notification_var1_list1 = [
    fac.player_supporters_faction,
    _players_kingdom,
    ]
    if is_between(_supported_pretender,trp.kingdom_1_pretender,trp.knight_1_1_wife) and troop_slot_eq(_supported_pretender,14,_g_notification_var1):
        for trp_001 in range(trp.npc1, trp.knight_1_1_wife):
            if troop_slot_eq(trp_001,2,2):
                troop_faction_002 = store_faction_of_troop(trp_001)
                if troop_faction_002 == fac.player_supporters_faction:
                    troop_set_faction(trp_001,_g_notification_var1)
                    troop_set_title_according_to_faction(trp_001,_g_notification_var1)
                    if _g_notification_var1 in _g_notification_var1_list1:
                        check_concilio_calradi_achievement()
                    #end
                #end
            elif troop_slot_eq(trp_001,2,2): # Johandros ???
                troop_faction_002 = store_faction_of_troop(trp_001)
                if troop_faction_002 == _g_notification_var1:
                    troop_change_relation_with_troop(trp_001,trp.player,5)
                #end
            #end
        #end
        for cur_party in __all_parties__:
            troop_faction_002 = store_faction_of_party(cur_party)
            if troop_faction_002 == fac.player_supporters_faction:
                party_set_faction(cur_party,_g_notification_var1)
            #end
        #end
        _players_kingdom = _g_notification_var1
        if True:
            troop_slot_004 = troop_get_slot(trp.player,30)
            if is_between(troop_slot_004,trp.knight_1_1_wife,trp.heroes_end):
                troop_set_faction(troop_slot_004,_g_notification_var1)
            #end
        #end
        add_notification_menu(mnu.notification_rebels_switched_to_faction,_g_notification_var1,_supported_pretender)
        faction_set_slot(_g_notification_var1,21,0)
        faction_set_slot(fac.player_supporters_faction,21,2)
        faction_slot_005 = faction_get_slot(_g_notification_var1,11)
        troop_set_slot(faction_slot_005,55,fac.commoners)
        faction_set_slot(_g_notification_var1,11,_supported_pretender)
        troop_set_faction(_supported_pretender,_g_notification_var1)
        faction_slot_006 = faction_get_slot(_g_notification_var1,8)
        if faction_slot_006 >= 0:
            troop_slot_007 = troop_get_slot(faction_slot_006,10)
            if party_is_active(troop_slot_007):
                party_set_marshall(troop_slot_007,0)
            #end
        #end
        faction_set_slot(_g_notification_var1,8,trp.player)
        faction_set_slot(_g_notification_var1,4,0)
        faction_set_slot(_g_notification_var1,5,-1)
        troop_set_slot(_supported_pretender,2,2)
        troop_set_slot(_supported_pretender,7,1000)
        party_remove_members(p.main_party,_supported_pretender,1)
        set_player_relation_with_faction(_g_notification_var1,0)
        for fac_008 in range(fac.player_supporters_faction, fac.kingdoms_end):
            if faction_slot_eq(fac_008,21,0) and fac_008 != _g_notification_var1:
                faction_relation_009 = store_relation(fac_008,fac.player_supporters_faction)
                set_relation(fac_008,_g_notification_var1,faction_relation_009)
            #end
        #end
        _supported_pretender = 0
        _supported_pretender_old_faction = 0
        _g_recalculate_ais = 1
        update_all_notes()
    #end
    change_screen_return()
notification_faction_defeated_continue.codeBlock = code



notification_rebels_switched_to_faction = GameMenu("notification_rebels_switched_to_faction", 0,
"Rebellion Success^^ Your rebellion is victorious! Your faction now has the sole claim to the title of {s11}, with {s12} as the single ruler."
)
def condition():
    s11 = str_store_faction_name(_g_notification_var1)
    s12 = str_store_troop_name(_g_notification_var2)
    set_fixed_point_multiplier(100)
    position_set_x(0,65)
    position_set_y(0,30)
    position_set_z(0,170)
    #if is_between(_g_notification_var1,fac.kingdom_1,fac.kingdoms_end):
    #    set_game_menu_tableau_mesh(tab.faction_note_mesh_for_menu,_g_notification_var1,0)
    #else:
    #    set_game_menu_tableau_mesh(tab.faction_note_mesh_banner,_g_notification_var1,0)
    ##end
notification_rebels_switched_to_faction.conditionBlock = condition

notification_rebels_switched_to_faction_continue = MenuOption("continue", "Continue...")
def code():
    _talk_context = 15
    start_map_conversation(_g_notification_var2,-1)
    change_screen_return()
notification_rebels_switched_to_faction_continue.codeBlock = code



notification_player_should_consult = GameMenu("notification_player_should_consult", 0,
"Your minister send words that there are problems brewing in the realm which, if left untreated, could sap your authority. You should consult with him at your earliest convenience"
)

notification_player_should_consult_continue = MenuOption("continue", "Continue...")
def code():
    setup_quest_text(qst.consult_with_minister)
    s11 = str_store_troop_name(_g_player_minister)
    s12 = str_store_party_name(_g_player_court)
    s2 = str_store_string(gstr.consult_with_s11_at_your_court_in_s12)
    start_quest(qst.consult_with_minister,-1)
    quest_set_slot(qst.consult_with_minister,23,30)
    quest_set_slot(qst.consult_with_minister,6,_g_player_minister)
    change_screen_return()
notification_player_should_consult_continue.codeBlock = code



notification_player_feast_in_progress = GameMenu("notification_player_feast_in_progress", 0,
"Feast in Preparation^^Your wife has started preparations for a feast in your hall in {s11}"
)
def condition():
    s11 = str_store_party_name(_g_notification_var1)
notification_player_feast_in_progress.conditionBlock = condition

notification_player_feast_in_progress_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_player_feast_in_progress_continue.codeBlock = code



notification_lady_requests_visit = GameMenu("notification_lady_requests_visit", 0,
"An elderly woman approaches your party and passes one of your men a letter, sealed in plain wax. It is addressed to you. When you break the seal, you see it is from {s15}. It reads, 'I so enjoyed your last visit. {s14} I am currently in {s10}.{s12}'"
)
def condition():
    troop_id_001 = _g_notification_var1
    var002 = _g_notification_var2
    s15 = str_store_troop_name(troop_id_001)
    s10 = str_store_party_name(var002)
    cur_hours_003 = store_current_hours()
    troop_slot_004 = troop_get_slot(troop_id_001,4)
    cur_hours_003 -= troop_slot_004
    get_kingdom_lady_social_determinants(troop_id_001)
    var005 = reg0
    s16 = str_store_troop_name(var005)
    troop_get_family_relation_to_troop(var005,troop_id_001)
    str_clear(14)
    if cur_hours_003 < 336:
        if troop_slot_eq(troop_id_001,52,23):
            s14 = str_store_string(gstr.as_brief_as_our_separation_has_been_the_longing_in_my_heart_to_see_you_has_made_it_seem_as_many_years)
        else:
            s14 = str_store_string(gstr.although_it_has_only_been_a_short_time_since_your_departure_but_i_would_be_most_pleased_to_see_you_again)
        #end
    elif cur_hours_003 >= 336:
        if troop_slot_eq(troop_id_001,52,24):
            s14 = str_store_string(gstr.although_i_have_received_no_word_from_you_for_quite_some_time_i_am_sure_that_you_must_have_been_very_busy_and_that_your_failure_to_come_see_me_in_no_way_indicates_that_your_attentions_to_me_were_insincere_)
        elif troop_slot_eq(troop_id_001,52,25):
            s14 = str_store_string(gstr.i_trust_that_you_have_comported_yourself_in_a_manner_becoming_a_gentleman_during_our_long_separation_)
        else:
            s14 = str_store_string(gstr.it_has_been_many_days_since_you_came_and_i_would_very_much_like_to_see_you_again)
        #end
    #end
    str_clear(12)
    str_clear(18)
    if troop_slot_eq(var005,38,0):
        s12 = str_store_string(gstr._you_should_ask_my_s11_s16s_permission_but_i_have_no_reason_to_believe_that_he_will_prevent_you_from_coming_to_see_me)
        s18 = str_store_string(gstr._you_should_first_ask_her_s11_s16s_permission)
    elif troop_slot_eq(var005,38,-1):
        s12 = str_store_string(gstr._alas_as_we_know_my_s11_s16_will_not_permit_me_to_see_you_however_i_believe_that_i_can_arrange_away_for_you_to_enter_undetected)
    elif troop_slot_eq(var005,38,1):
        s12 = str_store_string(gstr._as_my_s11_s16_has_already_granted_permission_for_you_to_see_me_i_shall_expect_your_imminent_arrival)
    #end
notification_lady_requests_visit.conditionBlock = condition

notification_lady_requests_visit_continue = MenuOption("continue", "Tell the woman to inform her mistress that you will come shortly")
def code():
    var001 = _g_notification_var1
    s3 = str_store_troop_name_link(var001)
    s4 = str_store_party_name_link(_g_notification_var2)
    s2 = str_store_string(gstr.visit_s3_who_was_last_at_s4s18)
    start_quest(qst.visit_lady,var001)
    quest_set_slot(qst.visit_lady,6,var001)
    if _cheat_mode == 1:
        quest_slot_002 = quest_get_slot(qst.visit_lady,6)
        s2 = str_store_troop_name(quest_slot_002)
        print(gstr.giver_troop_equal_s2)
    #end
    quest_set_slot(qst.visit_lady,23,30)
    change_screen_return()
notification_lady_requests_visit_continue.codeBlock = code

notification_lady_requests_visit_continue = MenuOption("continue", "Tell the woman to inform her mistress that you are indisposed")
def code():
    troop_set_slot(_g_notification_var1,37,1)
    change_screen_return()
notification_lady_requests_visit_continue.codeBlock = code



garden = GameMenu("garden", 0,
"{s12}"
)
def condition():
    get_kingdom_lady_social_determinants(_love_interest_in_town)
    troop_id_001 = reg0
    s11 = str_store_troop_name(_love_interest_in_town)
    if True:
        npc_decision_checklist_male_guardian_assess_suitor(troop_id_001,trp.player)
        if reg0 < 0:
            troop_set_slot(troop_id_001,38,-1)
        #end
    #end
    _nurse_assists_entry = 0
    if troop_slot_eq(troop_id_001,38,1):
        s12 = str_store_string(gstr.the_guards_at_the_gate_have_been_ordered_to_allow_you_through_you_might_be_imagining_things_but_you_think_one_of_them_may_have_given_you_a_wink)
    else:
        troop_get_relation_with_troop(trp.player,_love_interest_in_town)
        if reg0 > 0:
            var002 = 0
            if check_quest_active(qst.visit_lady) and quest_slot_eq(qst.visit_lady,6,_love_interest_in_town):
                var002 = 1
            elif check_quest_active(qst.formal_marriage_proposal) and quest_slot_eq(qst.formal_marriage_proposal,6,_love_interest_in_town) and check_quest_succeeded(qst.formal_marriage_proposal) or check_quest_failed(qst.formal_marriage_proposal):
                var002 = 1
            elif check_quest_active(qst.duel_courtship_rival) and quest_slot_eq(qst.duel_courtship_rival,6,_love_interest_in_town) and check_quest_succeeded(qst.duel_courtship_rival) or check_quest_failed(qst.duel_courtship_rival):
                var002 = 1
            #end
        #end
        if True:
            cur_hours_003 = store_current_hours()
            troop_slot_004 = troop_get_slot(_love_interest_in_town,4)
            cur_hours_003 -= troop_slot_004
            if cur_hours_003 >= 96 or var002 == 1:
                if is_between(_g_encountered_party,p.town_1,p.castle_1):
                    s12 = str_store_string(gstr.the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_don_this_dress_and_throw_the_hood_over_your_face_i_will_smuggle_you_inside_the_castle_to_meet_her_in_the_guise_of_a_skullery_maid__the_guards_will_not_look_too_carefully_but_i_beg_you_for_all_of_our_sakes_be_discrete)
                    _nurse_assists_entry = 1
                else:
                    s12 = str_store_string(gstr.the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_wait_for_a_while_by_the_spring_outside_the_walls_i_will_smuggle_her_ladyship_out_to_meet_you_dressed_in_the_guise_of_a_shepherdess_but_i_beg_you_for_all_of_our_sakes_be_discrete)
                    _nurse_assists_entry = 2
                #end
            #end
        else:
            s12 = str_store_string(gstr.the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter_however_as_you_walk_back_towards_your_lodgings_an_elderly_lady_dressed_in_black_approaches_you_i_am_s11s_nurse_she_whispers_urgently_her_ladyship_asks_me_to_say_that_yearns_to_see_you_but_that_you_should_bide_your_time_a_bit_her_ladyship_says_that_to_arrange_a_clandestine_meeting_so_soon_after_your_last_encounter_would_be_too_dangerous)
        #end
    #else:
    #    s12 = str_store_string(gstr.the_guards_glare_at_you_and_you_know_better_than_to_ask_permission_to_enter)
    #end
garden.conditionBlock = condition

garden_enter = MenuOption("enter", "Enter")
def condition():
    get_kingdom_lady_social_determinants(_love_interest_in_town)
garden_enter.conditionBlock = condition
def code():
    jump_to_menu(mnu.town)
    setup_meet_lady(_love_interest_in_town,_g_encountered_party)
garden_enter.codeBlock = code

garden_nurse = MenuOption("nurse", "Go with the nurse")
def code():
    jump_to_menu(mnu.town)
    setup_meet_lady(_love_interest_in_town,_g_encountered_party)
garden_nurse.codeBlock = code

garden_nurse = MenuOption("nurse", "Wait by the spring")
def code():
    jump_to_menu(mnu.town)
    setup_meet_lady(_love_interest_in_town,_g_encountered_party)
garden_nurse.codeBlock = code

garden_leave = MenuOption("leave", "Leave")
def code():
    jump_to_menu(mnu.town)
garden_leave.codeBlock = code



kill_local_merchant_begin = GameMenu("kill_local_merchant_begin", 0,
"You spot your victim and follow him, observing as he turns a corner into a dark alley. This will surely be your best opportunity to attack him."
)

kill_local_merchant_begin_continue = MenuOption("continue", "Continue...")
def code():
    set_jump_mission(mt.back_alley_kill_local_merchant)
    party_slot_001 = party_get_slot(_qst_kill_local_merchant_center,17)
    modify_visitors_at_site(party_slot_001)
    reset_visitors()
    set_visitor(0,trp.player)
    set_visitor(1,trp.local_merchant)
    jump_to_menu(mnu.town)
    jump_to_scene(party_slot_001)
    change_screen_mission()
kill_local_merchant_begin_continue.codeBlock = code



debug_alert_from_s65 = GameMenu("debug_alert_from_s65", 0,
"DEBUG ALERT: {s65}"
)

debug_alert_from_s65_continue = MenuOption("continue", "Continue...")
def code():
    _debug_message_in_queue = 0
    change_screen_return()
debug_alert_from_s65_continue.codeBlock = code



auto_return_to_map = GameMenu("auto_return_to_map", 0,
"stub"
)
def condition():
    change_screen_map()
auto_return_to_map.conditionBlock = condition



bandit_lair = GameMenu("bandit_lair", 0,
"{s3}"
)
def condition():
    if _loot_screen_shown == 1:
        for pt_001 in range(pt.steppe_bandits, pt.deserters):
            if party_template_slot_eq(pt_001,4,_g_encountered_party):
                party_template_set_slot(pt_001,4,0)
            #end
        #end
        if _g_encountered_party >= 0 and party_is_active(_g_encountered_party):
            party_template_id_002 = party_get_template_id(_g_encountered_party)
            if party_template_id_002 != pt.looter_lair:
                remove_party(_g_encountered_party)
            #end
        #end
        _g_leave_encounter = 0
        change_screen_return()
    else:
        troop_id_003 = party_stack_get_troop_id(_g_encountered_party,0)
        s4 = str_store_troop_name_plural(troop_id_003)
        s5 = str_store_string(gstr.bandit_approach_defile)
        if troop_id_003 == trp.desert_bandit:
            s5 = str_store_string(gstr.bandit_approach_defile)
        elif troop_id_003 == trp.mountain_bandit:
            s5 = str_store_string(gstr.bandit_approach_cliffs)
        elif troop_id_003 == trp.forest_bandit:
            s5 = str_store_string(gstr.bandit_approach_swamp)
        elif troop_id_003 == trp.taiga_bandit:
            s5 = str_store_string(gstr.bandit_approach_swamp)
        elif troop_id_003 == trp.steppe_bandit:
            s5 = str_store_string(gstr.bandit_approach_thickets)
        elif troop_id_003 == trp.sea_raider:
            s5 = str_store_string(gstr.bandit_approach_cove)
        #end
        if party_slot_eq(_g_encountered_party,8,0):
            s3 = str_store_string(gstr.bandit_hideout_preattack)
        else:
            party_template_id_002 = party_get_template_id(_g_encountered_party)
            if party_template_id_002 == pt.looter_lair and party_slot_eq(_g_encountered_party,8,1):
                s3 = str_store_string(gstr.lost_startup_hideout_attack)
            elif party_slot_eq(_g_encountered_party,8,1):
                s3 = str_store_string(gstr.bandit_hideout_failure)
            elif party_slot_eq(_g_encountered_party,8,2):
                s3 = str_store_string(gstr.bandit_hideout_success)
            #end
        #end
    #end
bandit_lair.conditionBlock = condition

bandit_lair_continue_1 = MenuOption("continue_1", "Attack the hideout...")
def code():
    party_set_slot(_g_encountered_party,8,1)
    party_template_id_001 = party_get_template_id(_g_encountered_party)
    _g_enemy_party = _g_encountered_party
    if party_template_id_001 == pt.sea_raider_lair:
        troop_id_002 = trp.sea_raider
        scene_id_003 = scn.lair_sea_raiders
    elif party_template_id_001 == pt.forest_bandit_lair:
        troop_id_002 = trp.forest_bandit
        scene_id_003 = scn.lair_forest_bandits
    elif party_template_id_001 == pt.desert_bandit_lair:
        troop_id_002 = trp.desert_bandit
        scene_id_003 = scn.lair_desert_bandits
    elif party_template_id_001 == pt.mountain_bandit_lair:
        troop_id_002 = trp.mountain_bandit
        scene_id_003 = scn.lair_mountain_bandits
    elif party_template_id_001 == pt.taiga_bandit_lair:
        troop_id_002 = trp.taiga_bandit
        scene_id_003 = scn.lair_taiga_bandits
    elif party_template_id_001 == pt.steppe_bandit_lair:
        troop_id_002 = trp.steppe_bandit
        scene_id_003 = scn.lair_steppe_bandits
    elif party_template_id_001 == pt.looter_lair:
        troop_id_002 = trp.looter
        party_faction_004 = store_faction_of_party(_g_starting_town)
        if party_faction_004 == fac.kingdom_1:
            scene_id_003 = scn.lair_forest_bandits
        elif party_faction_004 == fac.kingdom_2:
            scene_id_003 = scn.lair_taiga_bandits
        elif party_faction_004 == fac.kingdom_3:
            scene_id_003 = scn.lair_steppe_bandits
        elif party_faction_004 == fac.kingdom_4:
            scene_id_003 = scn.lair_sea_raiders
        elif party_faction_004 == fac.kingdom_5:
            scene_id_003 = scn.lair_mountain_bandits
        elif party_faction_004 == fac.kingdom_6:
            scene_id_003 = scn.lair_desert_bandits
        #end
    #end
    modify_visitors_at_site(scene_id_003)
    reset_visitors()
    character_lvl_005 = store_character_level(trp.player)
    var006 = 5 + character_lvl_005
    var006 /= 3
    for var007 in range(0, var006):
        random_x_008 = store_random_in_range(2,11)
        set_visitor(random_x_008,troop_id_002,1)
    #end
    party_clear(p.temp_casualties)
    set_party_battle_mode()
    set_battle_advantage(0)
    _g_battle_result = 0
    set_jump_mission(mt.bandit_lair)
    jump_to_scene(scene_id_003)
    change_screen_mission()
bandit_lair_continue_1.codeBlock = code

bandit_lair_leave_no_attack = MenuOption("leave_no_attack", "Leave...")
def code():
    change_screen_return()
bandit_lair_leave_no_attack.codeBlock = code

bandit_lair_leave_victory = MenuOption("leave_victory", "Continue...")
def code():
    for pt_001 in range(pt.steppe_bandits, pt.deserters):
        if party_template_slot_eq(pt_001,4,_g_encountered_party):
            party_template_set_slot(pt_001,4,0)
        #end
    #end
    party_template_id_002 = party_get_template_id(_g_encountered_party)
    if party_template_id_002 != pt.looter_lair and check_quest_active(qst.destroy_bandit_lair) and quest_slot_eq(qst.destroy_bandit_lair,8,_g_encountered_party):
        succeed_quest(qst.destroy_bandit_lair)
    #end
    _g_leave_encounter = 0
    change_screen_return()
    if _loot_screen_shown == 0:
        _loot_screen_shown = 1
        troop_clear_inventory(trp.temp_troop)
        party_num_companions_stacks_003 = party_get_num_companion_stacks(p.temp_casualties)
        for stack_no_004 in range(0, party_num_companions_stacks_003):
            troop_id_005 = party_stack_get_troop_id(p.temp_casualties,stack_no_004)
            if True:
                party_stack_size_006 = party_stack_get_size(p.temp_casualties,stack_no_004)
                troop_id_005 = party_stack_get_troop_id(p.temp_casualties,stack_no_004)
                if party_stack_size_006 > 0:
                    party_add_members(p.total_enemy_casualties,troop_id_005,party_stack_size_006)
                    party_stack_num_wounded_007 = party_stack_get_num_wounded(p.temp_casualties,stack_no_004)
                    if party_stack_num_wounded_007 > 0:
                        party_wound_members(p.total_enemy_casualties,troop_id_005,party_stack_num_wounded_007)
                    #end
                #end
            #end
        #end
        party_calculate_loot(p.total_enemy_casualties)
        if reg0 > 0:
            troop_sort_inventory(trp.temp_troop)
            change_screen_loot(trp.temp_troop)
        #end
    #end
    if _g_encountered_party >= 0 and party_is_active(_g_encountered_party):
        party_template_id_002 = party_get_template_id(_g_encountered_party)
        if party_template_id_002 == pt.looter_lair:
            remove_party(_g_encountered_party)
        #end
    #end
bandit_lair_leave_victory.codeBlock = code

bandit_lair_leave_defeat = MenuOption("leave_defeat", "Continue...")
def code():
    for pt_001 in range(pt.steppe_bandits, pt.deserters):
        if party_template_slot_eq(pt_001,4,_g_encountered_party):
            party_template_set_slot(pt_001,4,0)
        #end
    #end
    if True:
        party_template_id_002 = party_get_template_id(_g_encountered_party)
        if party_template_id_002 != pt.looter_lair and check_quest_active(qst.destroy_bandit_lair) and quest_slot_eq(qst.destroy_bandit_lair,8,_g_encountered_party):
            fail_quest(qst.destroy_bandit_lair)
        #end
    #end
    if _g_encountered_party >= 0 and party_is_active(_g_encountered_party):
        party_template_id_002 = party_get_template_id(_g_encountered_party)
        if party_template_id_002 != pt.looter_lair:
            remove_party(_g_encountered_party)
        #end
    #end
    _g_leave_encounter = 0
    if party_is_active(_g_encountered_party):
        party_set_slot(_g_encountered_party,8,0)
    #end
    change_screen_return()
bandit_lair_leave_defeat.codeBlock = code



notification_player_faction_political_issue_resolved = GameMenu("notification_player_faction_political_issue_resolved", 0,
"After consulting with the peers of the realm, {s10} has decided to confer {s11} on {s12}."
)
def condition():
    var001 = _g_notification_var1
    var002 = _g_notification_var2
    faction_slot_003 = faction_get_slot(_players_kingdom,11)
    s10 = str_store_troop_name(faction_slot_003)
    if var001 == 1:
        s11 = str_store_string(gstr.the_marshalship)
    else:
        s11 = str_store_party_name(var001)
    #end
    s12 = str_store_troop_name(var002)
notification_player_faction_political_issue_resolved.conditionBlock = condition

notification_player_faction_political_issue_resolved_continue = MenuOption("continue", "Continue...")
def code():
    change_screen_return()
notification_player_faction_political_issue_resolved_continue.codeBlock = code



notification_player_faction_political_issue_resolved_for_player = GameMenu("notification_player_faction_political_issue_resolved_for_player", 0,
"After consulting with the peers of the realm, {s10} has decided to confer {s11} on you. You may decline the honor, but it will probably mean that you will not receive other awards for a little while.{s12}"
)
def condition():
    faction_slot_001 = faction_get_slot(_players_kingdom,11)
    s10 = str_store_troop_name(faction_slot_001)
    faction_slot_002 = faction_get_slot(_players_kingdom,64)
    if faction_slot_002 == 1:
        s11 = str_store_string(gstr.the_marshalship)
        s12 = str_store_string("@^^Note that so long as you remain marshal;;; the lords of the realm will be expecting you to lead them on campaign. So;;; if you are awaiting a feast;;; either for a wedding or for other purposes;;; you may wish to resign the marshalship by speaking to your liege.")
    else:
        str_clear(12)
        s11 = str_store_party_name(faction_slot_002)
    #end
notification_player_faction_political_issue_resolved_for_player.conditionBlock = condition

notification_player_faction_political_issue_resolved_for_player_accept = MenuOption("accept", "Accept the honor")
def code():
    faction_slot_001 = faction_get_slot(_players_kingdom,64)
    if faction_slot_001 == 1:
        check_and_finish_active_army_quests_for_faction(_players_kingdom)
        appoint_faction_marshall(_players_kingdom,trp.player)
        unlock_achievement(41)
    else:
        give_center_to_lord(faction_slot_001,trp.player,0)
    #end
    faction_set_slot(_players_kingdom,64,0)
    for trp_002 in range(trp.npc1, trp.knight_1_1_wife):
        troop_faction_003 = store_faction_of_troop(trp_002)
        if troop_faction_003 == _players_kingdom:
            troop_set_slot(trp_002,154,-1)
        #end
    #end
    change_screen_return()
notification_player_faction_political_issue_resolved_for_player_accept.codeBlock = code

notification_player_faction_political_issue_resolved_for_player_decline = MenuOption("decline", "Decline the honor")
def code():
    faction_slot_001 = faction_get_slot(_players_kingdom,64)
    if is_between(faction_slot_001,p.town_1,p.salt_mine):
        _g_dont_give_fief_to_player_days = 30
    else:
        _g_dont_give_marshalship_to_player_days = 30
    #end
    for trp_002 in range(trp.npc1, trp.knight_1_1_wife):
        troop_faction_003 = store_faction_of_troop(trp_002)
        if troop_faction_003 == _players_kingdom:
            troop_set_slot(trp_002,154,-1)
        #end
    #end
    change_screen_return()
notification_player_faction_political_issue_resolved_for_player_decline.codeBlock = code



start_phase_2_5 = GameMenu("start_phase_2_5", 512,
"{!}{s16}"
)
def condition():
    s1 = str_store_party_name(_g_starting_town)
    s16 = str_store_string(_g_journey_string)
start_phase_2_5.conditionBlock = condition

start_phase_2_5_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.start_phase_3)
start_phase_2_5_continue.codeBlock = code



start_phase_3 = GameMenu("start_phase_3", 512,
"{s16}^^You are exhausted by the time you find the inn in {s1}, and fall asleep quickly. However, you awake before dawn and are eager to explore your surroundings. You venture out onto the streets, which are still deserted. All of a sudden, you hear a sound that stands the hairs of your neck on end -- the rasp of a blade sliding from its scabbard..."
)
def condition():
    var001 = 1
    if _current_startup_quest_phase == 1:
        if _g_killed_first_bandit == 1:
            s11 = str_store_string(gstr.killed_bandit_at_alley_fight)
        else:
            s11 = str_store_string(gstr.wounded_by_bandit_at_alley_fight)
        #end
        jump_to_menu(mnu.start_phase_4)
        var001 = 0
    elif _current_startup_quest_phase == 3:
        if _g_killed_first_bandit == 1:
            s11 = str_store_string(gstr.killed_bandit_at_alley_fight)
        else:
            s11 = str_store_string(gstr.wounded_by_bandit_at_alley_fight)
        #end
        jump_to_menu(mnu.start_phase_4)
        var001 = 0
    #end
    s1 = str_store_party_name(_g_starting_town)
    str_clear(16)
start_phase_3.conditionBlock = condition

start_phase_3_continue = MenuOption("continue", "Continue...")
def code():
    _g_starting_town = _current_town
    player_arrived()
    party_set_morale(p.main_party,100)
    set_encountered_party(_current_town)
    prepare_alley_to_fight()
start_phase_3_continue.codeBlock = code



start_phase_4 = GameMenu("start_phase_4", 512,
"{s11}"
)
def condition():
    var001 = 1
    if _current_startup_quest_phase == 2:
        change_screen_return()
        var001 = 0
    elif _current_startup_quest_phase == 3:
        s11 = str_store_string(gstr.merchant_and_you_call_some_townsmen_and_guards_to_get_ready_and_you_get_out_from_tavern)
    elif _current_startup_quest_phase == 4:
        if _g_killed_first_bandit == 1:
            s11 = str_store_string(gstr.town_fight_ended_you_and_citizens_cleaned_town_from_bandits)
        else:
            s11 = str_store_string(gstr.town_fight_ended_you_and_citizens_cleaned_town_from_bandits_you_wounded)
        #end
    #end
start_phase_4.conditionBlock = condition

start_phase_4_continue = MenuOption("continue", "Continue...")
def code():
    _town_entered = 1
    if _current_town == p.town_1:
        troop_id_001 = trp.nord_merchant
        scene_id_002 = scn.town_1_room
    elif _current_town == p.town_5:
        troop_id_001 = trp.rhodok_merchant
        scene_id_002 = scn.town_5_room
    elif _current_town == p.town_6:
        troop_id_001 = trp.swadian_merchant
        scene_id_002 = scn.town_6_room
    elif _current_town == p.town_8:
        troop_id_001 = trp.vaegir_merchant
        scene_id_002 = scn.town_8_room
    elif _current_town == p.town_10:
        troop_id_001 = trp.khergit_merchant
        scene_id_002 = scn.town_10_room
    elif _current_town == p.town_19:
        troop_id_001 = trp.sarranid_merchant
        scene_id_002 = scn.town_19_room
    #end
    modify_visitors_at_site(scene_id_002)
    reset_visitors()
    set_visitor(0,trp.player)
    set_visitor(9,troop_id_001)
    _talk_context = 21
    _dialog_with_merchant_ended = 0
    set_jump_mission(mt.meeting_merchant)
    jump_to_scene(scene_id_002)
    change_screen_mission()
start_phase_4_continue.codeBlock = code

start_phase_4_continue = MenuOption("continue", "Continue...")
def code():
    prepare_town_to_fight()
start_phase_4_continue.codeBlock = code



lost_tavern_duel = GameMenu("lost_tavern_duel", 512,
"{s11}"
)
def condition():
    if True:
        troop_id_001 = agent_get_troop_id(_g_main_attacker_agent)
        if troop_id_001 == trp.belligerent_drunk:
            s11 = str_store_string(gstr.lost_tavern_duel_ordinary)
        else:
            troop_id_001 = agent_get_troop_id(_g_main_attacker_agent)
            if troop_id_001 == trp.hired_assassin:
                s11 = str_store_string(gstr.lost_tavern_duel_assassin)
            #end
        #end
    #end
    troop_set_slot(trp.hired_assassin,12,-1)
lost_tavern_duel.conditionBlock = condition

lost_tavern_duel_continue = MenuOption("continue", "Continue...")
def code():
    jump_to_menu(mnu.town)
lost_tavern_duel_continue.codeBlock = code



establish_court = GameMenu("establish_court", 512,
"To establish {s4} as your court will require a small refurbishment. In particular, you will need a set of tools and a bolt of velvet. it may also take a short while for some of your followers to relocate here. Do you wish to proceed?"
)
def condition():
    s4 = str_store_party_name(_g_encountered_party)
establish_court.conditionBlock = condition

establish_court_establish = MenuOption("establish", "Establish {s4} as your court")
def code():
    _g_player_court = _current_town
    troop_remove_item(trp.player,itm.tools)
    troop_remove_item(trp.player,itm.velvet)
    jump_to_menu(mnu.town)
establish_court_establish.codeBlock = code

establish_court_continue = MenuOption("continue", "Hold off...")
def code():
    jump_to_menu(mnu.town)
establish_court_continue.codeBlock = code



notification_relieved_as_marshal = GameMenu("notification_relieved_as_marshal", 512,
"{s4} wishes to inform you that your services as marshal are no longer required. In honor of valiant efforts on behalf of the realm over the last {reg4} days, however, {reg8?she:he} offers you a purse of {reg5} denars."
)
def condition():
    reg4 = _g_player_days_as_marshal
    var001 = _g_player_days_as_marshal / 4
    val_min(var001,20)
    gold_002 = _g_player_days_as_marshal * 50
    val_max(gold_002,200)
    val_min(gold_002,4000)
    troop_add_gold(trp.player,gold_002)
    change_troop_renown(trp.player,var001)
    _g_player_days_as_marshal = 0
    _g_dont_give_marshalship_to_player_days = 15
    reg5 = gold_002
    faction_slot_003 = faction_get_slot(_players_kingdom,11)
    s4 = str_store_troop_name(faction_slot_003)
    reg8 = troop_get_type(faction_slot_003)
notification_relieved_as_marshal.conditionBlock = condition

notification_relieved_as_marshal_continue = MenuOption("continue", "Continue")
def code():
    change_screen_return()
notification_relieved_as_marshal_continue.codeBlock = code


