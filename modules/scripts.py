# This Python file uses the following encoding: utf-8

def game_start():
    print("Hello world!")


def game_event_party_encounter(_g_encountered_party, _g_encountered_party_2):
    _g_encountered_party_faction = store_faction_of_party(_g_encountered_party)
    _g_encountered_party_relation = store_relation(_g_encountered_party_faction, "fac_player_faction")

    jump_to_menu("mnu_town")
