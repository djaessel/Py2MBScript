from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_menus import *
from ID_map_icons import *

no_menu = 0
pmf_is_prisoner = 0x0001

party_templates = [

("none", "None", 0, menu_none, fac_no_faction, 0, []),
("hunters", "Hunters", 0, menu_none, fac_no_faction, 0, [(trp_npc1,1,1,0),(trp_looter,1,2,0),]),

] # PARTY TEMPLATES END
