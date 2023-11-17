# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("./data_objects/")

from dialog import Dialog

dialog_start = Dialog("anyone", "Hi there!", starting_state="start", ending_state="lord_pretalk")

dialog1 = Dialog("anyone", "Anything else?", starting_state="lord_pretalk", ending_state="lord_talk")

dialog1_answer1 = Dialog("anyone", "I want to give some troops to you.", is_player_text=True, starting_state="lord_talk", ending_state="lord_give_troops")
def code():
    if "$g_talk_troop_faction" == "fac_player_supporters_faction": #and not troop_slot_ge("$g_talk_troop", slot_troop_prisoner_of_party, 0):
        pass

dialog1_answer1.conditionBlock = code

dialog2 = Dialog("anyone", "Here, have these troops!", starting_state="lord_give_troops")

#[anyone|plyr,"lord_talk", [(eq, "$g_talk_troop_faction", "fac_player_supporters_faction"),
#                           #(troop_slot_eq, "$g_talk_troop", slot_troop_is_prisoner, 0),
#                           (neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0),
#                           ],
# "I want to give some troops to you.", "lord_give_troops",[]],


