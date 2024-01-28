# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")


from MBParty import MBParty


def game_start():
    print("Hello world!")



def game_event_party_encounter(_g_encountered_party, _g_encountered_party_2):
    _g_encountered_party_faction = store_faction_of_party(_g_encountered_party)
    _g_encountered_party_relation = store_relation(_g_encountered_party_faction, "fac_player_faction")

    _g_encountered_party = MBParty(_g_encountered_party)
    template_idx = _g_encountered_party.get_template_id()
    if template_idx == 0:
        jump_to_menu("mnu_town")
    else:
        jump_to_menu("mnu_simple_encounter")



# TODO: add more game events
