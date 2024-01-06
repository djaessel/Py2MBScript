from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_menus import *
from ID_party_templates import *
from ID_map_icons import *

no_menu = 0
pt_none = 0
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

parties = [

("main_party", "Main Party", icon_player|pf_limit_members, no_menu, pt_none, fac_player_faction, 0, ai_bhvr_hold, 0, (17,20), [(trp_player,1,0),]),
("temp_party", "{!}temp_party", pf_disabled, no_menu, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0.0,0.0), []),
("camp_bandits", "{!}camp_bandits", pf_disabled, no_menu, pt_none, fac_outlaws, 0, ai_bhvr_hold, 0, (1,1), []),
("test_town", "Test Town", icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (12,20), [(trp_looter,20,0),]),

] # PARTIES END
