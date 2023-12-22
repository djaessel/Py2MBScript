from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

game_menus = [
  ("start_game_0",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Welcome adventurer, hopefully you will enjoy this new adventure through another world.",
    "none",
    [],
    [
     ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_start_game_1"),
        ]
       ),
      ("go_back",[],"Go back",
       [
         (change_screen_quit),
       ]),
    ]
  ),

#      ("tutorial_cheat",[(eq,1,0)],"{!}CHEAT!",
#       [
#         (change_screen_return),
#         (assign, "$cheat_mode", 1),
#         (set_show_messages, 0),
#		 (add_xp_to_troop, 15000, "trp_player"),
#         (troop_raise_skill, "trp_player", skl_leadership, 7),
#         (troop_raise_skill, "trp_player", skl_prisoner_management, 5),
#         (troop_raise_skill, "trp_player", skl_inventory_management, 10),
#         (party_add_members, "p_main_party", "trp_swadian_knight", 10),
#         (party_add_members, "p_main_party", "trp_vaegir_knight", 10),
#         (party_add_members, "p_main_party", "trp_vaegir_archer", 10),
#         (party_add_members, "p_main_party", "trp_swadian_sharpshooter", 10),
#         (troop_add_item, "trp_player","itm_scale_armor",0),
#         (troop_add_item, "trp_player","itm_full_helm",0),
#         
#         (troop_add_item, "trp_player","itm_hafted_blade_b",0),
#         (troop_add_item, "trp_player","itm_hafted_blade_a",0),
#         (troop_add_item, "trp_player","itm_morningstar",0),
#         (troop_add_item, "trp_player","itm_tutorial_spear",0),
#         (troop_add_item, "trp_player","itm_tutorial_staff",0),
#         (troop_add_item, "trp_player","itm_tutorial_staff_no_attack",0),
#         (troop_add_item, "trp_player","itm_arena_lance",0),
#         (troop_add_item, "trp_player","itm_practice_staff",0),
#         (troop_add_item, "trp_player","itm_practice_lance",0),
#         (troop_add_item, "trp_player","itm_practice_javelin",0),
#         (troop_add_item, "trp_player","itm_scythe",0),
#         (troop_add_item, "trp_player","itm_pitch_fork",0),
#         (troop_add_item, "trp_player","itm_military_fork",0),
#         (troop_add_item, "trp_player","itm_battle_fork",0),
#         (troop_add_item, "trp_player","itm_boar_spear",0),
#         (troop_add_item, "trp_player","itm_jousting_lance",0),
#         (troop_add_item, "trp_player","itm_double_sided_lance",0),
#         (troop_add_item, "trp_player","itm_glaive",0),
#         (troop_add_item, "trp_player","itm_poleaxe",0),
#         (troop_add_item, "trp_player","itm_polehammer",0),
#         (troop_add_item, "trp_player","itm_staff",0),
#         (troop_add_item, "trp_player","itm_quarter_staff",0),
#         (troop_add_item, "trp_player","itm_iron_staff",0),
#         (troop_add_item, "trp_player","itm_shortened_spear",0),
#         (troop_add_item, "trp_player","itm_spear",0),
#         (troop_add_item, "trp_player","itm_war_spear",0),
#         (troop_add_item, "trp_player","itm_military_scythe",0),
#         (troop_add_item, "trp_player","itm_light_lance",0),
#         (troop_add_item, "trp_player","itm_lance",0),
#         (troop_add_item, "trp_player","itm_heavy_lance",0),
#         (troop_add_item, "trp_player","itm_great_lance",0),
#         (troop_add_item, "trp_player","itm_pike",0),
#         (troop_add_item, "trp_player","itm_ashwood_pike",0),
#         (troop_add_item, "trp_player","itm_awlpike",0),
#         (troop_add_item, "trp_player","itm_throwing_spears",0),
#         (troop_add_item, "trp_player","itm_javelin",0),
#         (troop_add_item, "trp_player","itm_jarid",0),
#         
#         (troop_add_item, "trp_player","itm_long_axe_b",0),		 
#         
#         (set_show_messages, 1),
#
#         (try_for_range, ":cur_place", scenes_begin, scenes_end),
#           (scene_set_slot, ":cur_place", slot_scene_visited, 1),
#         (try_end),
#         
#         (call_script, "script_get_player_party_morale_values"),
#         (party_set_morale, "p_main_party", reg0),
#       ]
#	   ),
#    ]
#  ),
 


 
#  (
#    "start_game_3",mnf_disable_all_keys,
#    "Choose your scenario:",
#    "none",
#    [
#      (assign, "$g_custom_battle_scenario", 0),
#      (assign, "$g_custom_battle_scenario", "$g_custom_battle_scenario"),
##      #Default banners
##      (troop_set_slot, "trp_banner_background_color_array", 126, 0xFF212221),
##      (troop_set_slot, "trp_banner_background_color_array", 127, 0xFF212221),
##      (troop_set_slot, "trp_banner_background_color_array", 128, 0xFF2E3B10),
##      (troop_set_slot, "trp_banner_background_color_array", 129, 0xFF425D7B),
##      (troop_set_slot, "trp_banner_background_color_array", 130, 0xFF394608),
#      ],
#    [
##      ("custom_battle_scenario_1",[], "Skirmish 1",
##       [
##           (assign, "$g_custom_battle_scenario", 0),
##           (jump_to_menu, "mnu_custom_battle_2"),
##
##        ]
##       ),
####      ("custom_battle_scenario_2",[],"Siege Attack 1",
####       [
####           (assign, "$g_custom_battle_scenario", 1),
####           (jump_to_menu, "mnu_custom_battle_2"),
####
####        ]
####       ),
##      ("custom_battle_scenario_3",[],"Skirmish 2",
##       [
##           (assign, "$g_custom_battle_scenario", 1),
##           (jump_to_menu, "mnu_custom_battle_2"),
##
##        ]
##       ),
##       ("custom_battle_scenario_4",[],"Siege Defense",
##       [
##           (assign, "$g_custom_battle_scenario", 2),
##           (jump_to_menu, "mnu_custom_battle_2"),
##        ]
##       ),
##       ("custom_battle_scenario_5",[],"Skirmish 3",
##       [
##           (assign, "$g_custom_battle_scenario", 3),
##           (jump_to_menu, "mnu_custom_battle_2"),
##        ]
##       ),
##      ("custom_battle_scenario_6",[],"Siege Attack",
##       [
##           (assign, "$g_custom_battle_scenario", 4),
##           (jump_to_menu, "mnu_custom_battle_2"),
##
##        ]
##       ),
#      ("go_back",[],"Go back",
#       [(change_screen_quit), 
#        ]
#		),
#    ]
#  ),


#  (
#    "tutorial",mnf_disable_all_keys,
#    "The tutorial is not available yet.",
#    "none",
#    [
#      (try_begin),
#        (eq, "$g_tutorial_entered", 1),
#        (change_screen_quit),
#      (else_try),
#        (set_passage_menu, "mnu_tutorial"),
#        (assign, "$g_tutorial_entered", 1),
#      (try_end),
#    ],
#    [
##      ("continue",[],"Continue...",
##      [
##        (change_screen_mission),
##        ]),
#
#      ("go_back_dot",
#      [],
#      "Go back.",
#       [
#         (change_screen_quit),
#       ]),
#    ]
#  ),

  ("reports",0,
   "TODO: Reports^",
   "none",
   [
    (call_script, "script_game_get_party_companion_limit"),
    (assign, ":party_size_limit", reg0),
    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (assign, reg5, ":renown"),
    (assign, reg6, "$player_honor"),
    (assign, reg7, ":party_size_limit"),
    #(call_script, "script_get_player_party_morale_values"),
    #(party_set_morale, "p_main_party", reg0),
    (party_get_morale, reg8, "p_main_party"),
   ],
    [
#      ("cheat_faction_orders",[(ge,"$cheat_mode",1)],"{!}Cheat: Faction orders.",
#       [(jump_to_menu, "mnu_faction_orders"),
#        ]
#       ),
#	   
#      ("view_character_report",[],"View character report.",
#       [(jump_to_menu, "mnu_character_report"),
#        ]
#       ),
#      ("view_party_size_report",[],"View party size report.",
#       [(jump_to_menu, "mnu_party_size_report"),
#        ]
#       ),
#	   
#      ("view_npc_mission_report",[],"View companion mission report.",
#       [(jump_to_menu, "mnu_companion_report"),
#        ]
#       ),
#
#      ("view_weekly_budget_report",[],"View weekly budget report.",
#       [
#         (assign, "$g_apply_budget_report_to_gold", 0),
#         (start_presentation, "prsnt_budget_report"),
#        ]
#       ),
#
#      ("view_morale_report",[],"View party morale report.",
#       [(jump_to_menu, "mnu_morale_report"),
#        ]
#       ),
#
#NPC companion changes begin
#      ("lord_relations",[],"View list of known lords by relation.",
#       [
#		(jump_to_menu, "mnu_lord_relations"),
#        ]
#       ),
#	   
#      ("courtship_relations",[],"View courtship relations.",
#       [
#		(jump_to_menu, "mnu_courtship_relations"),
#        ]
#       ),

      ("status_check",[(eq,"$cheat_mode",1)],"{!}NPC status check.",
       [
        (try_for_range, ":npc", companions_begin, companions_end),
            (main_party_has_troop, ":npc"),
            (str_store_troop_name, 4, ":npc"),
            (troop_get_slot, reg3, ":npc", slot_troop_morality_state),
            (troop_get_slot, reg4, ":npc", slot_troop_2ary_morality_state),
            (troop_get_slot, reg5, ":npc", slot_troop_personalityclash_state),    
            (troop_get_slot, reg6, ":npc", slot_troop_personalityclash2_state),    
            (troop_get_slot, reg7, ":npc", slot_troop_personalitymatch_state),    
            (display_message, "@{!}{s4}: M{reg3}, 2M{reg4}, PC{reg5}, 2PC{reg6}, PM{reg7}"),
        (try_end),
        ]
       ),

#NPC companion changes end

#      ("view_faction_relations_report",[],"View faction relations report.",
#       [(jump_to_menu, "mnu_faction_relations_report"),
#        ]
#       ),
      ("resume_travelling",[],"Resume travelling.",
       [(change_screen_return),
        ]
       ),
      ]
  ),

  (
    "custom_battle_scene",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "(NO_TRANS)",
	
    "none",
    [],
    [

      ("go_back",[],"{!}Go back",
       [(change_screen_quit),
        ]
       ),
      ]
  ),
  

  (
    "custom_battle_end",mnf_disable_all_keys,
    "The battle is over. TODO: Add info.",
    "none",
    [
     (music_set_situation, 0),
#     (assign, reg5, "$g_custom_battle_team2_death_count"),
#     (assign, reg6, "$g_custom_battle_team1_death_count"),
#     (get_player_agent_kill_count, ":kill_count"),
#     (get_player_agent_kill_count, ":wound_count", 1),
#     (store_add, reg7, ":kill_count", ":wound_count"),
#     (try_begin),
#       (eq, "$g_battle_result", 1),
#       (str_store_string, s1, "str_battle_won"),
#     (else_try),
#       (str_store_string, s1, "str_battle_lost"),
#     (try_end),
#     
#     (try_begin),
#       (ge, "$g_custom_battle_team2_death_count", 100),
#       (unlock_achievement, ACHIEVEMENT_LOOK_AT_THE_BONES),
#     (try_end),
     ],
    [
      ("continue",[],"Continue.",
       [(change_screen_quit),
        ]
       ),
    ]
  ),
  
  ("start_game_1",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Select your character's gender.",
    "none",
    [],
    [
      ("start_male",[],"Male",
       [
         (troop_set_type,"trp_player", 0),
         (assign,"$character_gender",tf_male),
#         (jump_to_menu,"mnu_start_character_1"),
         (jump_to_menu, "mnu_choose_skill"),
        ]
       ),
      ("start_female",[],"Female",
       [
         (troop_set_type, "trp_player", 1),
         (assign, "$character_gender", tf_female),
#         (jump_to_menu, "mnu_start_character_1"),
         (jump_to_menu, "mnu_choose_skill"),
       ]
       ),
	  ("go_back",[],"Go back",
       [
	     (jump_to_menu,"mnu_start_game_0"),
       ]),
    ]
  ),


  (
    "choose_skill",mnf_disable_all_keys,
    "{s13}", 
    "none",
    [
         (assign,"$current_string_reg",10),
#	 (assign, ":difficulty", 0),
#	 
#	 (try_begin),
#		(eq, "$character_gender", tf_female),
#		(str_store_string, s14, "str_woman"),
#		(val_add, ":difficulty", 1),
#	 (else_try),	
#		(str_store_string, s14, "str_man"),
#	 (try_end),
#	
#	 (try_begin),
#         (eq,"$background_type",cb_noble),
#		(str_store_string, s15, "str_noble"),
#		(val_sub, ":difficulty", 1),
#	 (else_try),
#		(str_store_string, s15, "str_common"),
#	 (try_end),
#	 
#	 (try_begin),
#		(eq, ":difficulty", -1),
#		(str_store_string, s16, "str_may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly"),
#	 (else_try),
#		(eq, ":difficulty", 0),
#		(str_store_string, s16, "str_may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
#	 (else_try),
#		(eq, ":difficulty", 1),
#		(str_store_string, s16, "str_may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
#	 (try_end),
	],
    [
      ("begin_adventuring",[],"Become an adventurer and ride to your destiny.",[
#           (try_begin),
#             (eq, "$background_type", cb_noble),
#             (jump_to_menu, "mnu_auto_return"),
##normal_banner_begin
#             (start_presentation, "prsnt_banner_selection"),
##custom_banner_begin
##             (start_presentation, "prsnt_custom_banner"),
#           (else_try),
             (change_screen_return, 0),
#           (try_end),
           (set_show_messages, 1),
        ]),
      ("go_back_dot",[],"Go back.",[
        (jump_to_menu,"mnu_start_game_1"),
        ]),
    ]
  ),

  (
    "past_life_explanation",mnf_disable_all_keys,
    "{s3}",
    "none",
    [
     (try_begin),
       (gt,"$current_string_reg",14),
       (assign,"$current_string_reg",10),
     (try_end),
     (str_store_string_reg,s3,"$current_string_reg"),
     (try_begin),
       (ge,"$current_string_reg",14),
       (str_store_string,s5,"@Back to the beginning..."),
     (else_try),
       (str_store_string,s5,"@View next segment..."),
     (try_end),
     ],
    [
      ("view_next",[],"{s5}",[
        (val_add,"$current_string_reg",1),
        (jump_to_menu, "mnu_past_life_explanation"),
        ]),
      ("continue",[],"Continue...",
       [
        ]),
      ("go_back_dot",[],"Go back.",[
        (jump_to_menu, "mnu_choose_skill"),
        ]),
    ]
  ),

  (
    "auto_return",0,
    "{!}This menu automatically returns to caller.",
    "none",
    [(change_screen_return, 0)],
    [
    ]
  ),
  
  
  
  ("camp",mnf_scale_picture,
   "You set up camp. What do you want to do?",
   "none",
   [
     (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
    ],
    [
      ("camp_action_1",[(eq,"$cheat_mode",1)],"{!}Cheat: Walk around.",
       [(set_jump_mission,"mt_ai_training"),
        (call_script, "script_setup_random_scene"),
        (change_screen_mission),
        ]
       ),
      ("camp_action",[],"Take an action.",
       [(jump_to_menu, "mnu_camp_action"),
        ]
       ),
      ("set_town_1_faction",[],"Change Town 1 faction",
        [
            (store_faction_of_party, ":cur_faction", "p_town_1"),
            (try_begin),
               (eq, ":cur_faction", "fac_neutral"),
               (party_set_faction, "p_town_1", "fac_outlaws"),
               (assign, "$g_coop_coords_1_y", 1877),
            (else_try),
               (party_set_faction, "p_town_1", "fac_neutral"),
               (assign, "$g_coop_coords_1_y", 1337),
            (try_end),
        ],
       ),
      ("camp_wait_here",[],"Wait here for some time.",
       [
           (assign,"$g_camp_mode", 1),
           (assign, "$g_infinite_camping", 0),
           (assign, "$g_player_icon_state", pis_camping),
           
           (try_begin),
             (party_is_active, "p_main_party"),
             (party_get_current_terrain, ":cur_terrain", "p_main_party"),
             (try_begin),
               (eq, ":cur_terrain", rt_desert),
               (unlock_achievement, ACHIEVEMENT_SARRANIDIAN_NIGHTS),
             (try_end),  
           (try_end),  

           (rest_for_hours_interactive, 24 * 365, 5, 1), #rest while attackable
                      
           (change_screen_return),
        ]
       ),
      ("camp_cheat",
       [(ge, "$cheat_mode", 1)
        ], "CHEAT MENU!",
       [(jump_to_menu, "mnu_camp_cheat"),
        ],
       ),
      ("resume_travelling",[],"Resume travelling.",
       [
           (change_screen_return),
        ]
       ),
      ]
  ),
  ("camp_cheat",0,
   "Select a cheat:",
   "none",
   [
     ],
    [
      ("camp_cheat_find_item",[], "Find an item...",
       [
         (jump_to_menu, "mnu_cheat_find_item"),
	   ]
       ),	   

      ("camp_cheat_find_item",[], "Change weather..",
       [
         (jump_to_menu, "mnu_cheat_change_weather"),
	   ]
       ),	   
	   
      ("camp_cheat_1",[],"{!}Increase player renown.",
       [
         (str_store_string, s1, "@Player renown is increased by 100. "),
         (call_script, "script_change_troop_renown", "trp_player", 100),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
	   
      ("camp_cheat_2",[],"{!}Increase player honor.",      
       [
         (assign, reg7, "$player_honor"),
         (val_add, reg7, 1),
         (display_message, "@Player honor is increased by 1 and it is now {reg7}."),
         (val_add, "$player_honor", 1),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),

#      ("camp_cheat_3",[],"{!}Update political notes.",
#       [
#         (try_for_range, ":hero", active_npcs_begin, active_npcs_end),
#           (troop_slot_eq, ":hero", slot_troop_occupation, slto_kingdom_hero),
#           (call_script, "script_update_troop_political_notes", ":hero"),
#         (try_end),
#         
#         (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
#           (call_script, "script_update_faction_political_notes", ":kingdom"),
#         (try_end),		
#        ]
#       ),	   
#	   
#      ("camp_cheat_4",[],"{!}Update troop notes.",
#       [
#         (try_for_range, ":hero", active_npcs_begin, active_npcs_end),
#           (troop_slot_eq, ":hero", slot_troop_occupation, slto_kingdom_hero),
#           (call_script, "script_update_troop_notes", ":hero"),
#         (try_end),
#         
#         (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
#           (call_script, "script_update_troop_notes", ":lady"),
#           (call_script, "script_update_troop_political_notes", ":lady"),
#           (call_script, "script_update_troop_location_notes", ":lady", 0),
#         (try_end),		
#        ]
#       ),	   
#	   
#      ("camp_cheat_5",[],"{!}Scramble minstrels.",
#       [
#         (call_script, "script_update_tavern_minstrels"),
#        ]
#       ),	   
	   
      ("camp_cheat_6",[],"{!}Infinite camp",
       [
         (assign,"$g_camp_mode", 1),
         (assign, "$g_infinite_camping", 1),
         (assign, "$g_player_icon_state", pis_camping),
         (rest_for_hours_interactive, 10 * 24 * 365, 20), #10 year rest while not attackable with 20x speed
         (change_screen_return),
        ]
       ),	   

      ("cheat_faction_orders",[(ge,"$cheat_mode",1)],
	  "{!}Cheat: Set Debug messages to All.",
       [(assign,"$cheat_mode",1),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
      ("cheat_faction_orders",[
	  (ge, "$cheat_mode", 1),
	  (neq,"$cheat_mode",3)],"{!}Cheat: Set Debug messages to Econ Only.",
       [(assign,"$cheat_mode",3),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
      ("cheat_faction_orders",[
	  (ge, "$cheat_mode", 1),
	  (neq,"$cheat_mode",4)],"{!}Cheat: Set Debug messages to Political Only.",
       [(assign,"$cheat_mode",4),
         (jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
	   
	   
      ("back_to_camp_menu",[],"{!}Back to camp menu.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),
  
  ("cheat_find_item",0,
   "{!}Current item range: {reg5} to {reg6}",
   "none",
   [
     (assign, reg5, "$cheat_find_item_range_begin"),
     (store_add, reg6, "$cheat_find_item_range_begin", max_inventory_items),
	 (val_min, reg6, "itm_items_end"),
	 (val_sub, reg6, 1),
     ],
    [
      ("cheat_find_item_next_range",[], "{!}Move to next item range.",
       [
	    (val_add, "$cheat_find_item_range_begin", max_inventory_items),
	    (try_begin),
	      (ge, "$cheat_find_item_range_begin", "itm_items_end"),
		  (assign, "$cheat_find_item_range_begin", 0),
	    (try_end),
	    (jump_to_menu, "mnu_cheat_find_item"),
	   ]
       ),	   

	   ("cheat_find_item_choose_this",[], "{!}Choose from this range.",
       [
        (troop_clear_inventory, "trp_find_item_cheat"),
        (store_add, ":max_item", "$cheat_find_item_range_begin", max_inventory_items),
	    (val_min, ":max_item", "itm_items_end"),
		(store_sub, ":num_items_to_add", ":max_item", "$cheat_find_item_range_begin"),
		(try_for_range, ":i_slot", 0, ":num_items_to_add"),
		  (store_add, ":item_id", "$cheat_find_item_range_begin", ":i_slot"),
          (troop_add_items, "trp_find_item_cheat", ":item_id", 1),
        (try_end),
        (change_screen_trade, "trp_find_item_cheat"),
	   ]
       ),	   
	   
      ("camp_action_4",[],"{!}Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

   ("cheat_change_weather",0,
   "{!}Current cloud amount: {reg5}^Current Fog Strength: {reg6}",
   "none",
   [
     (get_global_cloud_amount, reg5),
     (get_global_haze_amount, reg6),
     ],
    [
      ("cheat_increase_cloud",[], "{!}Increase Cloud Amount.",
       [
	    (get_global_cloud_amount, ":cur_cloud_amount"),
		(val_add, ":cur_cloud_amount", 5),
		(val_min, ":cur_cloud_amount", 100),
	    (set_global_cloud_amount, ":cur_cloud_amount"),
	   ]
       ),
      ("cheat_decrease_cloud",[], "{!}Decrease Cloud Amount.",
       [
	    (get_global_cloud_amount, ":cur_cloud_amount"),
		(val_sub, ":cur_cloud_amount", 5),
		(val_max, ":cur_cloud_amount", 0),
	    (set_global_cloud_amount, ":cur_cloud_amount"),
	   ]
       ),
      ("cheat_increase_fog",[], "{!}Increase Fog Amount.",
       [
	    (get_global_haze_amount, ":cur_fog_amount"),
		(val_add, ":cur_fog_amount", 5),
		(val_min, ":cur_fog_amount", 100),
	    (set_global_haze_amount, ":cur_fog_amount"),
	   ]
       ),
      ("cheat_decrease_fog",[], "{!}Decrease Fog Amount.",
       [
	    (get_global_haze_amount, ":cur_fog_amount"),
		(val_sub, ":cur_fog_amount", 5),
		(val_max, ":cur_fog_amount", 0),
	    (set_global_haze_amount, ":cur_fog_amount"),
	   ]
       ),

      ("camp_action_4",[],"{!}Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action",0,
   "Choose an action:",
   "none",
   [
     ],
    [
      ("action_read_book",[],"Select a book to read.",
       [(jump_to_menu, "mnu_camp_action_read_book"),
        ]
       ),

      ("action_rename_kingdom",
       [
         (eq, "$players_kingdom_name_set", 1),
         (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
         (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
         ],"Rename your kingdom.",
       [(start_presentation, "prsnt_name_kingdom"),
        ]
       ),

      ("action_modify_banner",[(eq, "$cheat_mode", 1)],"{!}Cheat: Modify your banner.",
       [
           (start_presentation, "prsnt_banner_selection"),
           #(start_presentation, "prsnt_custom_banner"),
        ]
       ),

      ("action_retire",[],"Retire from adventuring.",
       [(jump_to_menu, "mnu_retirement_verify"),
        ]
       ),

      ("camp_action_4",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action_read_book",0,
   "Choose a book to read:",
   "none",
   [],
    [
      ("action_read_book_1",[(player_has_item, "itm_book_tactics"),
                             (item_slot_eq, "itm_book_tactics", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_tactics"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_tactics"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_2",[(player_has_item, "itm_book_persuasion"),
                             (item_slot_eq, "itm_book_persuasion", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_persuasion"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_persuasion"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_3",[(player_has_item, "itm_book_leadership"),
                             (item_slot_eq, "itm_book_leadership", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_leadership"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_leadership"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_4",[(player_has_item, "itm_book_intelligence"),
                             (item_slot_eq, "itm_book_intelligence", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_intelligence"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_intelligence"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_5",[(player_has_item, "itm_book_trade"),
                             (item_slot_eq, "itm_book_trade", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_trade"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_trade"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_6",[(player_has_item, "itm_book_weapon_mastery"),
                             (item_slot_eq, "itm_book_weapon_mastery", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_weapon_mastery"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_weapon_mastery"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_7",[(player_has_item, "itm_book_engineering"),
                             (item_slot_eq, "itm_book_engineering", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_engineering"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_engineering"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("camp_action_4",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action_read_book_start",0,
   "{s1}",
   "none",
   [(assign, ":new_book", "$temp"),
    (str_store_item_name, s2, ":new_book"),
    (try_begin),
      (store_attribute_level, ":int", "trp_player", ca_intelligence),
      (item_get_slot, ":int_req", ":new_book", slot_item_intelligence_requirement),
      (le, ":int_req", ":int"),
      (str_store_string, s1, "@You start reading {s2}. After a few pages,\
 you feel you could learn a lot from this book. You decide to keep it close by and read whenever you have the time."),
      (assign, "$g_player_reading_book", ":new_book"),
    (else_try),
      (str_store_string, s1, "@You flip through the pages of {s2}, but you find the text confusing and difficult to follow.\
 Try as you might, it soon gives you a headache, and you're forced to give up the attempt."),
    (try_end),],
    [
      ("continue",[],"Continue...",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),


  ("retirement_verify",0,
   "You are at day {reg0}. Your current luck is {reg1}. Are you sure you want to retire?",
   "none",
   [
     (store_current_day, reg0),
     (assign, reg1, "$g_player_luck"),
     ],
    [
      ("retire_yes",[],"Yes.",
       [
         (start_presentation, "prsnt_retirement"),
        ]
       ),
      ("retire_no",[],"No.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("end_game",0,
   "The decision is made, and you resolve to give up your adventurer's\
 life and settle down. You sell off your weapons and armour, gather up\
 all your money, and ride off into the sunset....",
   "none",
   [],
    [
      ("end_game_bye",[],"Farewell.",
       [
         (change_screen_quit),
        ]
       ),
      ]
  ),

  ("cattle_herd",mnf_scale_picture,
   "You encounter a herd of cattle.",
   "none",
   [(play_sound, "snd_cow_moo"),
    (set_background_mesh, "mesh_pic_cattle"),
   ],
    [
      ("cattle_drive_away",[],"Drive the cattle onward.",
       [
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 1),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_driven_by_party),
        (party_set_ai_object,"$g_encountered_party", "p_main_party"),
        (change_screen_return),
        ]
       ),
      ("cattle_stop",[],"Bring the herd to a stop.",
       [
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 0),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_hold),
        (change_screen_return),
        ]
       ),
      ("cattle_kill",[(assign, ":continue", 1),
                      (try_begin),
                        (check_quest_active, "qst_move_cattle_herd"),
                        (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, "$g_encountered_party"),
                        (assign, ":continue", 0),
                      (try_end),
                      (eq, ":continue", 1)],"Slaughter some of the animals.",
       [(jump_to_menu, "mnu_cattle_herd_kill"),
        ]
       ),
      ("leave",[],"Leave.",
       [(change_screen_return),
        ]
       ),
      ]
  ),

  ("cattle_herd_kill",0,
   "How many animals do you want to slaughter?",
   "none",
   [(party_get_num_companions, reg5, "$g_encountered_party")],
    [
      ("cattle_kill_1",[(ge, reg5, 1),],"One.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 1),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_2",[(ge, reg5, 2),],"Two.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 2),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_3",[(ge, reg5, 3),],"Three.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 3),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_4",[(ge, reg5, 4),],"Four.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 4),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("cattle_kill_5",[(ge, reg5, 5),],"Five.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 5),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_cattle_herd"),
        ]
       ),
      ]
  ),

  ("cattle_herd_kill_end",0,
   "{!}You shouldn't be reading this.",
   "none",
   [(change_screen_return)],
    [
      ]
  ),


  (
    "simple_encounter",mnf_enable_hot_keys|mnf_scale_picture,
    "{s2} You have {reg10} troops fit for battle against their {reg11}.",
    "none",
    [      
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (assign, "$g_encounter_is_in_village", 0),
          (assign, "$g_encounter_type", 0),
          (try_begin),
            (party_slot_eq, "$g_enemy_party", slot_party_ai_state, spai_raiding_around_center),        
            (party_get_slot, ":village_no", "$g_enemy_party", slot_party_ai_object),
        
            (store_distance_to_party_from_party, ":dist", ":village_no", "$g_enemy_party"),

            (try_begin),
              (lt, ":dist", raid_distance),
              (assign, "$g_encounter_is_in_village", ":village_no"),
              (assign, "$g_encounter_type", enctype_fighting_against_village_raid),
            (try_end),
          (try_end),
          (try_begin),
            (gt, "$g_player_raiding_village", 0),
            (assign, "$g_encounter_is_in_village", "$g_player_raiding_village"),
            (assign, "$g_encounter_type", enctype_catched_during_village_raid),
            (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 1), #attach as enemy
            (str_store_string, s1, "@Villagers"),
            (display_message, "str_s1_joined_battle_enemy"),
          (else_try),
            (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
            (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 0), #attach as friend
            (str_store_string, s1, "@Villagers"),
            (display_message, "str_s1_joined_battle_friend"),
            # Let village party join battle at your side
          (try_end),
                    
          (call_script, "script_let_nearby_parties_join_current_battle", 0, 0),
          (call_script, "script_encounter_init_variables"),
          (assign, "$encountered_party_hostile", 0),
          (assign, "$encountered_party_friendly", 0),
          (try_begin),
            (gt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_friendly", 1),
          (try_end),
          (try_begin),
            (lt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_hostile", 1),
            (try_begin),
              (encountered_party_is_attacker),
              (assign, "$cant_leave_encounter", 1),
            (try_end),
          (try_end),
          (assign, "$talk_context", tc_party_encounter),
          (call_script, "script_setup_party_meeting", "$g_encountered_party"),
        (else_try), #second or more turn
#          (try_begin),
#            (call_script, "script_encounter_calculate_morale_change"),
#          (try_end),
          (try_begin),
            # We can leave battle only after some troops have been killed. 
            (eq, "$cant_leave_encounter", 1),
            (call_script, "script_party_count_members_with_full_health", "p_main_party_backup"),
            (assign, ":org_total_party_counts", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_encountered_party_backup"),
            (val_add, ":org_total_party_counts", reg0),

            (call_script, "script_party_count_members_with_full_health", "p_main_party"),
            (assign, ":cur_total_party_counts", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
            (val_add, ":cur_total_party_counts", reg0),

            (store_sub, ":leave_encounter_limit", ":org_total_party_counts", 10),
            (lt, ":cur_total_party_counts", ":leave_encounter_limit"),
            (assign, "$cant_leave_encounter", 0),
          (try_end),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        #setup s2
        (try_begin),
          (party_is_active, "$g_encountered_party"),
          (str_store_party_name, s1,"$g_encountered_party"),
          (try_begin),
            (eq, "$g_encounter_type", 0),
            (str_store_string, s2,"@You have encountered {s1}."),
          (else_try),
            (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
            (str_store_party_name, s3, "$g_encounter_is_in_village"),
            (str_store_string, s2,"@You have engaged {s1} while they were raiding {s3}."),
          (else_try),
            (eq, "$g_encounter_type", enctype_catched_during_village_raid),
            (str_store_party_name, s3, "$g_encounter_is_in_village"),
            (str_store_string, s2,"@You were caught by {s1} while your forces were raiding {s3}."),
          (try_end),
        (try_end),
        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (assign, ":num_enemy_regulars_remaining", reg0),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1), #battle won
                        
            (this_or_next|le, ":num_enemy_regulars_remaining", 0), #battle won
            (le, ":num_enemy_regulars_remaining",  "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

            (assign, ":enemy_finished",1),
          (else_try),
            (eq, "$g_engaged_enemy", 1), 
            
            (this_or_next|le, ":num_enemy_regulars_remaining", 0), 
            (le, "$g_enemy_fit_for_battle", "$num_routed_enemies"),  #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
            
            (ge, "$g_friend_fit_for_battle",1),
            (assign, ":enemy_finished",1),
          (try_end),
                
          (this_or_next|eq, ":enemy_finished",1),
          (eq,"$g_enemy_surrenders",1),
          (assign, "$g_next_menu", -1),
#          (jump_to_menu, "mnu_total_victory"),
        (else_try),       
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),        
          (assign, ":num_our_regulars_remaining", reg0),
          (assign, ":friends_finished",0),
          (try_begin),
            (eq, "$g_battle_result", -1),

            #(eq, ":num_our_regulars_remaining", 0), #battle lost
            (le, ":num_our_regulars_remaining",  "$num_routed_us"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.

            (assign,  ":friends_finished", 1),
          (else_try),
            (eq, "$g_engaged_enemy", 1),
            (ge, "$g_enemy_fit_for_battle",1),
            (le, "$g_friend_fit_for_battle",0),
            (assign,  ":friends_finished",1),
          (try_end),
          
          (this_or_next|eq,  ":friends_finished",1),
          (eq,"$g_player_surrenders",1),

#          (assign, "$g_next_menu", "mnu_captivity_start_wilderness"),
#          (jump_to_menu, "mnu_total_defeat"),
        (try_end),

       
        (try_begin),
          (eq, "$g_encountered_party_template", "pt_looters"),
          (set_background_mesh, "mesh_pic_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_mountain_bandits"),
          (set_background_mesh, "mesh_pic_mountain_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_steppe_bandits"),
          (set_background_mesh, "mesh_pic_steppe_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_taiga_bandits"),
          (set_background_mesh, "mesh_pic_steppe_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_sea_raiders"),
          (set_background_mesh, "mesh_pic_sea_raiders"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_forest_bandits"),
          (set_background_mesh, "mesh_pic_forest_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_deserters"),
          (set_background_mesh, "mesh_pic_deserters"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_kingdom_hero_party"),
#	  (party_stack_get_troop_id, ":leader_troop", "$g_encountered_party", 0),
#	  (ge, ":leader_troop", 1),
#	  (troop_get_slot, ":leader_troop_faction", ":leader_troop", slot_troop_original_faction),
#	  (try_begin),
#		(eq, ":leader_troop_faction", fac_kingdom_1),
#                (set_background_mesh, "mesh_pic_swad"),
#	  (else_try),
#		(eq, ":leader_troop_faction", fac_kingdom_2),
#                (set_background_mesh, "mesh_pic_vaegir"),
#	  (else_try),
#		(eq, ":leader_troop_faction", fac_kingdom_3),
#                (set_background_mesh, "mesh_pic_khergit"),
#	  (else_try),
#		(eq, ":leader_troop_faction", fac_kingdom_4),
#                (set_background_mesh, "mesh_pic_nord"),
#	  (else_try),
#		(eq, ":leader_troop_faction", fac_kingdom_5),
#                (set_background_mesh, "mesh_pic_rhodock"),
#	  (else_try),
#		(eq, ":leader_troop_faction", fac_kingdom_6),
#                (set_background_mesh, "mesh_pic_sarranid_encounter"),
#	  (try_end),
        (try_end),
    ],
    [
      ("encounter_attack",
      [
        (eq, "$encountered_party_friendly", 0),
        (neg|troop_is_wounded, "trp_player"),
      ],
      "Charge the enemy.",
      [
        (assign, "$g_battle_result", 0),
        (assign, "$g_engaged_enemy", 1),
        
        (party_get_template_id, ":encountered_party_template", "$g_encountered_party"),		
        (try_begin),
		  (eq, ":encountered_party_template", "pt_village_farmers"),
		  (unlock_achievement, ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED),
		(try_end),          
        
        (call_script, "script_calculate_renown_value"),
        (call_script, "script_calculate_battle_advantage"),
        (set_battle_advantage, reg0),
        (set_party_battle_mode),
        (try_begin),
#          (eq, "$g_encounter_type", enctype_fighting_against_village_raid),
#          (assign, "$g_village_raid_evil", 0),
#          (set_jump_mission,"mt_village_raid"),
#          (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_castle_exterior),
#          (jump_to_scene, ":scene_to_use"),
#        (else_try),
#          (eq, "$g_encounter_type", enctype_catched_during_village_raid),
#          (assign, "$g_village_raid_evil", 0),
#          (set_jump_mission,"mt_village_raid"),
#          (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_castle_exterior),
#          (jump_to_scene, ":scene_to_use"),
#        (else_try),
          (set_jump_mission,"mt_lead_charge"),
          (call_script, "script_setup_random_scene"),
        (try_end),
        (assign, "$g_next_menu", "mnu_simple_encounter"),
#        (jump_to_menu, "mnu_battle_debrief"),
        (change_screen_mission),
      ]),
      
#      ("encounter_order_attack",
#      [
#        (eq, "$encountered_party_friendly", 0),
#        (call_script, "script_party_count_members_with_full_health", "p_main_party"),(ge, reg0, 4),
#      ],
#      "Order your troops to attack without you.",
#      [
#        (jump_to_menu, "mnu_order_attack_begin"),
#        #(simulate_battle,3),
#      ]),
      
      ("encounter_leave",[
          (eq,"$cant_leave_encounter", 0),
          ],"Leave.",[

###NPC companion changes begin
              (try_begin),
                  (eq, "$encountered_party_friendly", 0),
                  (encountered_party_is_attacker),
                  (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
              (try_end),
###NPC companion changes end
#Troop commentary changes begin
              (try_begin),
                  (eq, "$encountered_party_friendly", 0),
#                  (encountered_party_is_attacker),
                  (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
                  (try_for_range, ":stack_no", 0, ":num_stacks"),
                    (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
                    (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
                    (store_troop_faction, ":victorious_faction", ":stack_troop"),
#					(store_relation, ":relation_with_stack_troop", ":victorious_faction", "fac_player_faction"),
#					(lt, ":relation_with_stack_troop", 0),
                    (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
                  (try_end),
              (try_end),
#Troop commentary changes end
          	(leave_encounter),(change_screen_return)]),
      ("encounter_retreat",[
         (eq,"$cant_leave_encounter", 1),
         (call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
         (assign, ":max_skill", reg0),
         (val_add, ":max_skill", 4),

         (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
         (assign, ":enemy_party_strength", reg0),
         (val_div, ":enemy_party_strength", 2),

         (val_div, ":enemy_party_strength", ":max_skill"),
         (val_max, ":enemy_party_strength", 1),

         (call_script, "script_party_count_fit_regulars", "p_main_party"),
         (assign, ":player_count", reg0),
         (ge, ":player_count", ":enemy_party_strength"),
         ],"Pull back, leaving some soldiers behind to cover your retreat.",[
#             (jump_to_menu, "mnu_encounter_retreat_confirm"),
             ]),
         
      ("encounter_surrender",[
         (eq,"$cant_leave_encounter", 1),
          ],"Surrender.",[(assign,"$g_player_surrenders",1)]),
    ]
  ),
#  (
#    "encounter_retreat_confirm",0,
#    "As the party member with the highest tactics skill,\
# ({reg2}), {reg3?you devise:{s3} devises} a plan that will allow you and your men to escape with your lives,\
# but you'll have to leave {reg4} soldiers behind to stop the enemy from giving chase.",
#    "none",
#    [(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
#     (assign, ":max_skill", reg0),
#     (assign, ":max_skill_owner", reg1),
#     (assign, reg2, ":max_skill"),
#     (val_add, ":max_skill", 4),
#
#     (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
#     (assign, ":enemy_party_strength", reg0),
#     (val_div, ":enemy_party_strength", 2),
#
#     (store_div, reg4, ":enemy_party_strength", ":max_skill"),
#     (val_max, reg4, 1),
#     
#     (try_begin),
#       (eq, ":max_skill_owner", "trp_player"),
#       (assign, reg3, 1),
#     (else_try),
#       (assign, reg3, 0),
#       (str_store_troop_name, s3, ":max_skill_owner"),
#     (try_end),
#     ],
#    [
#      ("leave_behind",[],"Go on. The sacrifice of these men will save the rest.",
#	  [
#	    (assign, ":num_casualties", reg4),
#		(try_for_range, ":unused", 0, ":num_casualties"),
#		  (call_script, "script_cf_party_remove_random_regular_troop", "p_main_party"),
#		  (assign, ":lost_troop", reg0),
#		  (store_random_in_range, ":random_no", 0, 100),
#		  (ge, ":random_no", 30),
#		  (party_add_prisoners, "$g_encountered_party", ":lost_troop", 1),
#		(try_end),
#		(call_script, "script_change_player_party_morale", -20),
#		(jump_to_menu, "mnu_encounter_retreat"),
#      ]),
#      ("dont_leave_behind",[],"No. We leave no one behind.",[(jump_to_menu, "mnu_simple_encounter"),]),
#    ]
#  ),
#  (
#    "encounter_retreat",0,
#    "You tell {reg4} of your troops to hold the enemy while you retreat with the rest of your party.",
#    "none",
#    [
#     ],
#    [
#      ("continue",[],"Continue...",
#	  [
#        ###Troop commentary changes begin
#        (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
#        (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
#        (try_for_range, ":stack_no", 0, ":num_stacks"),
#          (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
#          (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
#          (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
#          (store_troop_faction, ":victorious_faction", ":stack_troop"),
#          (call_script, "script_add_log_entry", logent_player_retreated_from_lord_cowardly, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
#        (try_end),
#        ###Troop commentary changes end
#        (party_ignore_player, "$g_encountered_party", 1),
#        (leave_encounter),
#		(change_screen_return)
#      ]),
#    ]
#  ),
#
#  
#  (
#    "enemy_slipped_away",0,
#    "{s17}",
#    "none",
#    [],
#    [
#      ("continue",[],"Continue...",[(jump_to_menu,"mnu_total_victory")]),
#    ]
#  ),
#
#  (
#    "total_defeat",0,
#    "{!}You shouldn't be reading this...",
#    "none",
#    [
#        (play_track, "track_captured", 1),
#           # Free prisoners
#          (party_get_num_prisoner_stacks, ":num_prisoner_stacks","p_main_party"),
#          (try_for_range, ":stack_no", 0, ":num_prisoner_stacks"),
#            (party_prisoner_stack_get_troop_id, ":stack_troop","p_main_party",":stack_no"),
#            (troop_is_hero, ":stack_troop"),
#            (call_script, "script_remove_troop_from_prison", ":stack_troop"),
#          (try_end),
#
#		  (try_begin),
#		    (party_is_active, "$g_ally_party"),
#			(call_script, "script_battle_political_consequences", "$g_ally_party", "$g_enemy_party"),
#		  (else_try),
#			(call_script, "script_battle_political_consequences", "p_main_party", "$g_enemy_party"),
#		  (try_end),
#		  
#          (call_script, "script_loot_player_items", "$g_enemy_party"),
#
#          (assign, "$g_move_heroes", 0),
#          (party_clear, "p_temp_party"),
#          (call_script, "script_party_add_party_prisoners", "p_temp_party", "p_main_party"),
#          (call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_main_party"),
#          (distribute_party_among_party_group, "p_temp_party", "$g_enemy_party"),
#        
#          (assign, "$g_prison_heroes", 1),
#          (call_script, "script_party_remove_all_companions", "p_main_party"),
#          (assign, "$g_prison_heroes", 0),
#          (assign, "$g_move_heroes", 1),
#          (call_script, "script_party_remove_all_prisoners", "p_main_party"),
#
#          (val_add, "$g_total_defeats", 1),
#
#          (try_begin),
#            (neq, "$g_player_surrenders", 1),
#            (store_random_in_range, ":random_no", 0, 100),
#            (ge, ":random_no", "$g_player_luck"),
#            (jump_to_menu, "mnu_permanent_damage"),
#          (else_try),
#            (try_begin),
#              (eq, "$g_next_menu", -1),
#              (leave_encounter),
#              (change_screen_return),
#            (else_try),
#              (jump_to_menu, "$g_next_menu"),
#            (try_end),
#          (try_end),
#          (try_begin),
#            (gt, "$g_ally_party", 0),
#            (call_script, "script_party_wound_all_members", "$g_ally_party"),
#          (try_end),
#
##Troop commentary changes begin
#          (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
#          (try_for_range, ":stack_no", 0, ":num_stacks"),
#            (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
#            (is_between, ":stack_troop", active_npcs_begin, active_npcs_end),
#			(troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
#            (store_troop_faction, ":victorious_faction", ":stack_troop"),
#            (call_script, "script_add_log_entry", logent_player_defeated_by_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
#          (try_end),
##Troop commentary changes end
#
#      ],
#    []
#  ),
#
#  (
#    "permanent_damage",mnf_disable_all_keys,
#    "{s0}",
#    "none",
#    [
#      (assign, ":end_cond", 1),
#      (try_for_range, ":unused", 0, ":end_cond"),
#        (store_random_in_range, ":random_attribute", 0, 4),
#        (store_attribute_level, ":attr_level", "trp_player", ":random_attribute"),
#        (try_begin),
#          (gt, ":attr_level", 3),
#          (neq, ":random_attribute", ca_charisma),
#          (try_begin),
#            (eq, ":random_attribute", ca_strength),
#            (str_store_string, s0, "@Some of your tendons have been damaged in the battle. You lose 1 strength."),
#          (else_try),
#            (eq, ":random_attribute", ca_agility),
#            (str_store_string, s0, "@You took a nasty wound which will cause you to limp slightly even after it heals. You lose 1 agility."),
###          (else_try),
###            (eq, ":random_attribute", ca_charisma),
###            (str_store_string, s0, "@After the battle you are aghast to find that one of the terrible blows you suffered has left a deep, disfiguring scar on your face, horrifying those around you. Your charisma is reduced by 1."),
#          (else_try),
###            (eq, ":random_attribute", ca_intelligence),
#            (str_store_string, s0, "@You have trouble thinking straight after the battle, perhaps from a particularly hard hit to your head, and frequent headaches now plague your existence. Your intelligence is reduced by 1."),
#          (try_end),
#        (else_try),
#          (lt, ":end_cond", 200),
#          (val_add, ":end_cond", 1),
#        (try_end),
#      (try_end),
#      (try_begin),
#        (eq, ":end_cond", 200),
#        (try_begin),
#          (eq, "$g_next_menu", -1),
#          (leave_encounter),
#          (change_screen_return),
#        (else_try),
#          (jump_to_menu, "$g_next_menu"),
#        (try_end),
#      (else_try),
#        (troop_raise_attribute, "trp_player", ":random_attribute", -1),
#      (try_end),
#      ],
#    [
#      ("s0",
#       [
#         (store_random_in_range, ":random_no", 0, 4),
#         (try_begin),
#           (eq, ":random_no", 0),
#           (str_store_string, s0, "@Perhaps I'm getting unlucky..."),
#         (else_try),
#           (eq, ":random_no", 1),
#           (str_store_string, s0, "@Retirement is starting to sound better and better."),
#         (else_try),
#           (eq, ":random_no", 2),
#           (str_store_string, s0, "@No matter! I will persevere!"),
#         (else_try),
#           (eq, ":random_no", 3),
#           (troop_get_type, ":is_female", "trp_player"),
#           (try_begin),
#             (eq, ":is_female", 1),
#             (str_store_string, s0, "@What did I do to deserve this?"),
#           (else_try),
#             (str_store_string, s0, "@I suppose it'll make for a good story, at least..."),
#           (try_end),
#         (try_end),
#         ],
#       "{s0}",
#       [
#         (try_begin),
#           (eq, "$g_next_menu", -1),
#           (leave_encounter),
#           (change_screen_return),
#         (else_try),
#           (jump_to_menu, "$g_next_menu"),
#         (try_end),
#         ]),
#      ]
#  ),
  
  (
    "pre_join",0,
    "You come across a battle between {s2} and {s1}. You decide to...",
    "none",
    [
        (str_store_party_name, 1,"$g_encountered_party"),
        (str_store_party_name, 2,"$g_encountered_party_2"),
      ],
    [
#      ("pre_join_help_attackers",[
#          (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
#          (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
#          (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
#          (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
#          (ge, ":attacker_relation", 0),
#          (lt, ":defender_relation", 0),
#          ],
#          "Move in to help the {s2}.",[
#              (select_enemy,0),
#              (assign,"$g_enemy_party","$g_encountered_party"),
#              (assign,"$g_ally_party","$g_encountered_party_2"),
#              (jump_to_menu,"mnu_join_battle")]),
#      ("pre_join_help_defenders",[
#          (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
#          (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
#          (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
#          (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
#          (ge, ":defender_relation", 0),
#          (lt, ":attacker_relation", 0),
#          ],
#          "Rush to the aid of the {s1}.",[
#              (select_enemy,1),
#              (assign,"$g_enemy_party","$g_encountered_party_2"),
#              (assign,"$g_ally_party","$g_encountered_party"),
#              (jump_to_menu,"mnu_join_battle")]),
      ("pre_join_leave",[],"Don't get involved.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  
#  (
#    "join_battle",0,
#    "You are helping the {s2} against the {s1}. You have {reg10} troops fit for battle against the enemy's {reg11}.",
#    "none",
#    [                
#        (str_store_party_name, 1,"$g_enemy_party"),
#        (str_store_party_name, 2,"$g_ally_party"),
#
#        (call_script, "script_encounter_calculate_fit"),                
#
#        (try_begin),
#          (eq, "$new_encounter", 1),
#          (assign, "$new_encounter", 0),
#          (call_script, "script_encounter_init_variables"),
#        (else_try), #second or more turn
#          (eq, "$g_leave_encounter",1),
#          (change_screen_return),
#        (try_end),
#
#        (try_begin),
#          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
#          (assign, ":num_enemy_regulars_remaining", reg0),
#          (assign, ":enemy_finished",0),
#          (try_begin),
#            (eq, "$g_battle_result", 1), 
#            
#            (this_or_next|le, ":num_enemy_regulars_remaining", 0), #battle won
#            (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#            
#            (assign, ":enemy_finished",1),
#          (else_try),
#            (eq, "$g_engaged_enemy", 1),
#            (le, "$g_enemy_fit_for_battle",0),
#            (ge, "$g_friend_fit_for_battle",1),
#            (assign, ":enemy_finished",1),
#          (try_end),
#          
#          (this_or_next|eq, ":enemy_finished",1),
#          (eq,"$g_enemy_surrenders",1),
#          (assign, "$g_next_menu", -1),
#          (jump_to_menu, "mnu_total_victory"),
#        (else_try),
#          (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
#          (assign, ":num_ally_regulars_remaining", reg0),
#          (assign, ":battle_lost", 0),
#          (try_begin),
#            (eq, "$g_battle_result", -1),
#            
#            #(eq, ":num_ally_regulars_remaining", 0), #battle lost
#            (le, ":num_ally_regulars_remaining",  "$num_routed_allies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#            
#            (assign, ":battle_lost",1),
#          (try_end),
#          
#          (this_or_next|eq, ":battle_lost",1),
#          (eq,"$g_player_surrenders",1),
#          (leave_encounter),
#          (change_screen_return),
#        (try_end),
#      ],
#    [
#      ("join_attack",
#      [
#        (neg|troop_is_wounded, "trp_player"),
#      ],
#      "Charge the enemy.",
#      [
#        (assign, "$g_joined_battle_to_help", 1),
#        (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
#        (assign, "$g_battle_result", 0),
#        (call_script, "script_calculate_renown_value"),
#        (call_script, "script_calculate_battle_advantage"),
#        (set_battle_advantage, reg0),
#        (set_party_battle_mode),
#        (set_jump_mission,"mt_lead_charge"),
#        (call_script, "script_setup_random_scene"),
#        (assign, "$g_next_menu", "mnu_join_battle"),
#        (jump_to_menu, "mnu_battle_debrief"),
#        (change_screen_mission),
#      ]),
#
#      ("join_order_attack",
#      [
#        (call_script, "script_party_count_members_with_full_health", "p_main_party"),
#        (ge, reg0, 3),
#      ],
#      "Order your troops to attack with your allies while you stay back.",
#      [
#        (assign, "$g_joined_battle_to_help", 1),
#        (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
#        (jump_to_menu,"mnu_join_order_attack"),
#      ]),
#      
#      ("join_leave",[],"Leave.",
#      [
#        (try_begin),
#           (neg|troop_is_wounded, "trp_player"),
#           (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
#           (party_stack_get_troop_id, ":enemy_leader","$g_enemy_party",0),
#		   (is_between, ":enemy_leader", active_npcs_begin, active_npcs_end),
#           (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":enemy_leader", -1),
#        (try_end),
#        
#        (leave_encounter),(change_screen_return)]),
#      ]),
#
#  (
#    "join_order_attack",mnf_disable_all_keys,
#    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
#    "none",
#    [
#      (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
#      (assign, ":player_party_strength", reg0),
#      (val_div, ":player_party_strength", 5),
#      (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
#      (assign, ":friend_party_strength", reg0),
#      (val_div, ":friend_party_strength", 5),
#                                    
#      (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
#      (assign, ":enemy_party_strength", reg0),
#      (val_div, ":enemy_party_strength", 5),
#
#      (try_begin),
#        (eq, ":friend_party_strength", 0),
#        (store_div, ":enemy_party_strength_for_p", ":enemy_party_strength", 2),
#      (else_try),
#        (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
#        (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
#        (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
#      (try_end),
#
#      (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
#      (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
#      (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#      (str_store_string_reg, s8, s0),
#                                    
#      (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
#                                    
#      #ozan begin
#      (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"), 
#      (try_for_range, ":stack_no", 0, ":num_stacks"),
#        (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"), 
#        (try_begin),
#          (party_stack_get_size, ":stack_size", "p_temp_casualties", ":stack_no"),
#          (gt, ":stack_size", 0),
#          (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
#          (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties", ":stack_no"),                                    
#          (gt, ":stack_wounded_size", 0),
#          (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
#        (try_end),
#      (try_end),
#      #ozan end
#
#      (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#      (str_store_string_reg, s10, s0),
#                                    
#      (call_script, "script_collect_friendly_parties"),
#      #(party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),
#
#      (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
#      (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#      (str_store_string_reg, s9, s0),
#      (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),
#
#       #(assign, "$cant_leave_encounter", 0),
#       (assign, "$no_soldiers_left", 0),
#       (try_begin),
#         (call_script, "script_party_count_members_with_full_health","p_main_party"),
#         (assign, ":num_our_regulars_remaining", reg0),
#                                      
#         #(le, ":num_our_regulars_remaining", 0),
#         (le, ":num_our_regulars_remaining", "$num_routed_us"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#                                      
#         (assign, "$no_soldiers_left", 1),
#         (str_store_string, s4, "str_join_order_attack_failure"),
#       (else_try),
#         (call_script, "script_party_count_members_with_full_health","p_collective_enemy"),
#         (assign, ":num_enemy_regulars_remaining", reg0),
#
#         (this_or_next|le, ":num_enemy_regulars_remaining", 0),
#         (le, ":num_enemy_regulars_remaining", "$num_routed_enemies"), #replaced for above line because we do not want routed agents to spawn again in next turn of battle.
#
#         (assign, "$g_battle_result", 1),
#         (assign, "$no_soldiers_left", 1),
#         (str_store_string, s4, "str_join_order_attack_success"),
#       (else_try),
#         (str_store_string, s4, "str_join_order_attack_continue"),
#       (try_end),
#    ],
#    [
#      ("continue",[],"Continue...",
#      [
#        (jump_to_menu,"mnu_join_battle"),
#      ]),
#    ]
#  ),

  
# Towns
#  (
#    "test_scene",0,
#    "You enter the test scene.",
#    "none",
#    [],
#    [
#
#      ("enter",[],"Enter 1.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_1"],[change_screen_mission]]),
#      ("enter",[],"Enter 2.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_2"],[change_screen_mission]]),
#      ("enter",[],"Enter 3.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_3"],[change_screen_mission]]),
#      ("enter",[],"Enter 4.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_4"],[change_screen_mission]]),
#      ("enter",[],"Enter 5.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_5"],[change_screen_mission]]),
#      ("enter",[],"Enter 6.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_6"],[change_screen_mission]]),
#      ("enter",[],"Enter 7.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_test2"],[change_screen_mission]]),
#      ("enter",[],"Enter 8.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_test3"],[change_screen_mission]]),
#      ("enter",[],"Enter 9.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_multi_scene_13"],[change_screen_mission]]),
#      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
#    ]
#  ),
#  (
#    "battlefields",0,
#    "{!}Select a field...",
#    "none",
#    [],
#    [
#
#      ("enter_f1",[],"{!}Field 1",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_1"],[change_screen_mission]]),
#      ("enter_f2",[],"{!}Field 2",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_2"],[change_screen_mission]]),
#      ("enter_f3",[],"{!}Field 3",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_3"],[change_screen_mission]]),
#      ("enter_f4",[],"{!}Field 4",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_4"],[change_screen_mission]]),
#      ("enter_f5",[],"{!}Field 5",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_5"],[change_screen_mission]]),
#      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
#    ]
#  ),
 
#  (
#    "join_siege_outside",mnf_scale_picture,
#    "{s1} has come under siege by {s2}.",
#    "none",
#    [
#        (str_store_party_name, s1, "$g_encountered_party"),
#        (str_store_party_name, s2, "$g_encountered_party_2"),
#        (troop_get_type, ":is_female", "trp_player"),
#        (try_begin),
#          (eq, ":is_female", 1),
#          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
#        (else_try),
#          (set_background_mesh, "mesh_pic_siege_sighted"),
#        (try_end),
#    ],
#    [
#      ("approach_besiegers",[(store_faction_of_party, ":faction_no", "$g_encountered_party_2"),
#                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
#                             (ge, ":relation", 0),
#                             (store_faction_of_party, ":faction_no", "$g_encountered_party"),
#                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
#                             (lt, ":relation", 0),
#                             ],"Approach the siege camp.",[
#          (jump_to_menu, "mnu_besiegers_camp_with_allies"),
#                                ]),
#      ("pass_through_siege",[(store_faction_of_party, ":faction_no", "$g_encountered_party"),
#                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
#                             (ge, ":relation", 0),
#                             ],"Pass through the siege lines and enter {s1}.",
#       [
#            (jump_to_menu,"mnu_cut_siege_without_fight"),
#          ]),
#      ("leave",[],"Leave.",[(leave_encounter),
#                            (change_screen_return)]),
#    ]
#  ),
#  (
#    "cut_siege_without_fight",0,
#    "The besiegers let you approach the gates without challenge.",
#    "none",
#    [],
#    [
#      ("continue",[],"Continue...",[(try_begin),
#                                   (this_or_next|eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
#                                   (eq, "$g_encountered_party_faction", "$players_kingdom"),
#                                   (jump_to_menu, "mnu_town"),
#                                 (else_try),
#                                   (jump_to_menu, "mnu_castle_outside"),
#                                 (try_end)]),
#      ]
#  ),
#  (
#    "besiegers_camp_with_allies",0,
#    "{s1} remains under siege. The banners of {s2} fly above the camp of the besiegers,\
# where you and your men are welcomed.",
#    "none",
#    [        
#        (str_store_party_name, s1, "$g_encountered_party"),
#        (str_store_party_name, s2, "$g_encountered_party_2"),
#        (assign, "$g_enemy_party", "$g_encountered_party"),
#        (assign, "$g_ally_party", "$g_encountered_party_2"),
#        (select_enemy, 0),
#        (call_script, "script_encounter_calculate_fit"),
#        (try_begin),
#          (eq, "$new_encounter", 1),
#          (assign, "$new_encounter", 0),
#          (call_script, "script_encounter_init_variables"),
#        (try_end),
#
#        (try_begin),
#          (eq, "$g_leave_encounter",1),
#          (change_screen_return),
#        (else_try),
#          (assign, ":enemy_finished", 0),
#          (try_begin),
#            (eq, "$g_battle_result", 1),
#            (assign, ":enemy_finished", 1),
#          (else_try),
#            (le, "$g_enemy_fit_for_battle", 0),
#            (ge, "$g_friend_fit_for_battle", 1),
#            (assign, ":enemy_finished", 1),
#          (try_end),
#          (this_or_next|eq, ":enemy_finished", 1),
#          (eq, "$g_enemy_surrenders", 1),
###          (assign, "$g_next_menu", -1),#"mnu_castle_taken_by_friends"),
###          (jump_to_menu, "mnu_total_victory"),
#          (call_script, "script_party_wound_all_members", "$g_enemy_party"),
#          (leave_encounter),
#          (change_screen_return),
#        (else_try),
#          (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),          
#          (assign, ":ally_num_soldiers", reg0),
#          (eq, "$g_battle_result", -1),
#          (eq, ":ally_num_soldiers", 0), #battle lost (TODO : also compare this with routed allies too like in other parts)
#          (leave_encounter),
#          (change_screen_return),
#        (try_end),
#        ],
#    [
#      ("talk_to_siege_commander",[],"Request a meeting with the commander.",[
#                                (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
#                                (modify_visitors_at_site,":meeting_scene"),(reset_visitors),
#                                (set_visitor,0,"trp_player"),
#                                (party_stack_get_troop_id, ":siege_leader_id","$g_encountered_party_2",0),
#                                (party_stack_get_troop_dna,":siege_leader_dna","$g_encountered_party_2",0),
#                                (set_visitor,17,":siege_leader_id",":siege_leader_dna"),
#                                (set_jump_mission,"mt_conversation_encounter"),
#                                (jump_to_scene,":meeting_scene"),
#                                (assign, "$talk_context", tc_siege_commander),
#                                (change_screen_map_conversation, ":siege_leader_id")]),
#      ("join_siege_with_allies",[(neg|troop_is_wounded, "trp_player")], "Join the next assault.",
#       [
#           (assign, "$g_joined_battle_to_help", 1), 
#           (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
#           (try_begin),
#             (check_quest_active, "qst_join_siege_with_army"),
#             (quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
#             (add_xp_as_reward, 250),
#             (call_script, "script_end_quest", "qst_join_siege_with_army"),
#             #Reactivating follow army quest
#             (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
#             (str_store_troop_name_link, s9, ":faction_marshall"),
#             (setup_quest_text, "qst_follow_army"),
#             (str_store_string, s2, "@{s9} wants you to follow his army until further notice."),
#             (call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
#             (assign, "$g_player_follow_army_warnings", 0),
#           (try_end),
#           (try_begin),
#             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
#             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
#           (else_try),
#             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
#           (try_end),
#           (call_script, "script_calculate_battle_advantage"),
#           (val_mul, reg0, 2),
#           (val_div, reg0, 3), #scale down the advantage a bit in sieges.
#           (set_battle_advantage, reg0),
#           (set_party_battle_mode),
#           (try_begin),
#             (party_slot_eq, "$g_encountered_party", slot_center_siege_with_belfry, 1),
#             (set_jump_mission,"mt_castle_attack_walls_belfry"),
#           (else_try),
#             (set_jump_mission,"mt_castle_attack_walls_ladder"),
#           (try_end),
#           (jump_to_scene,":battle_scene"),
#           (assign, "$g_siege_final_menu", "mnu_besiegers_camp_with_allies"),
#           (assign, "$g_siege_battle_state", 1),
#           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
#           (jump_to_menu, "mnu_battle_debrief"),
#           (change_screen_mission),
#          ]),
#      ("join_siege_stay_back", [(call_script, "script_party_count_members_with_full_health", "p_main_party"),
#                                (ge, reg0, 3),
#                                ],
#       "Order your soldiers to join the next assault without you.",
#       [
#         (assign, "$g_joined_battle_to_help", 1), 
#         (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
#         (try_begin),
#           (check_quest_active, "qst_join_siege_with_army"),
#           (quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
#           (add_xp_as_reward, 100),
#           (call_script, "script_end_quest", "qst_join_siege_with_army"),
#           #Reactivating follow army quest
#           (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
#           (str_store_troop_name_link, s9, ":faction_marshall"),
#           (setup_quest_text, "qst_follow_army"),
#           (str_store_string, s2, "@{s9} wants you to follow his army until further notice."),
#           (call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
#           (assign, "$g_player_follow_army_warnings", 0),
#         (try_end),
#         (jump_to_menu,"mnu_castle_attack_walls_with_allies_simulate")]),
#      ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
#    ]
#  ),

  (
    "castle_outside",mnf_scale_picture,
    "You are outside {s2}.{s11} {s3} {s4}",
    "none",
    [
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (str_store_party_name, s2,"$g_encountered_party"),
        (call_script, "script_encounter_calculate_fit"),
        (assign,"$all_doors_locked",1),
        (assign, "$current_town","$g_encountered_party"),
                
        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_let_nearby_parties_join_current_battle", 1, 0),
          (call_script, "script_encounter_init_variables"),
          (assign, "$entry_to_town_forbidden",0),
          (assign, "$sneaked_into_town",0),
          (assign, "$town_entered", 0),
#          (assign, "$waiting_for_arena_fight_result", 0),
          (assign, "$encountered_party_hostile", 0),
          (assign, "$encountered_party_friendly", 0),
          (try_begin),
            (gt, "$g_player_besiege_town", 0),
            (neq,"$g_player_besiege_town","$g_encountered_party"),
            (party_slot_eq, "$g_player_besiege_town", slot_center_is_besieged_by, "p_main_party"),
            (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
            (assign,"$g_player_besiege_town",-1),
          (try_end),
          (try_begin),
            (lt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_hostile", 1),
            (assign,"$entry_to_town_forbidden",1),
          (try_end),

          (assign,"$cant_sneak_into_town",0),
          (try_begin),
            (eq,"$current_town","$last_sneak_attempt_town"),
            (store_current_hours,reg(2)),
            (val_sub,reg(2),"$last_sneak_attempt_time"),
            (lt,reg(2),12),
            (assign,"$cant_sneak_into_town",1),
          (try_end),
        (else_try), #second or more turn
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        (str_clear,s4),
        (try_begin), 
          (eq,"$entry_to_town_forbidden",1),
          (try_begin),
            (eq,"$cant_sneak_into_town",1),
            (str_store_string,s4,"str_sneaking_to_town_impossible"),
          (else_try),
            (str_store_string,s4,"str_entrance_to_town_forbidden"),
          (try_end),
        (try_end),

        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9,":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),

        (try_begin), # same mnu_town
          (party_slot_eq,"$current_town",slot_party_type, spt_castle),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the castle gate."),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the castle gate."),
          (else_try),
		    (is_between, ":center_faction", kingdoms_begin, kingdoms_end),
            (str_store_string,s11,"str__this_castle_is_temporarily_under_royal_control"),
		  (else_try),
            (str_store_string,s11,"str__this_castle_does_not_seem_to_be_under_anyones_control"),
          (try_end),
        (else_try),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the town gates."),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the town gates."),
          (else_try),
		    (is_between, ":center_faction", kingdoms_begin, kingdoms_end),
            (str_store_string,s11,"str__this_town_is_temporarily_under_royal_control"),
		  (else_try),	
            (str_store_string,s11,"str__the_townspeople_seem_to_have_declared_their_independence"),
          (try_end),
        (try_end),

        (party_get_num_companions, reg(7),"p_collective_enemy"),
        (assign,"$castle_undefended",0),
        (str_clear, s3),
        (try_begin),
          (eq,reg(7),0),
          (assign,"$castle_undefended",1),
#          (party_set_faction,"$g_encountered_party","fac_neutral"),
#          (party_set_slot, "$g_encountered_party", slot_town_lord, stl_unassigned),
          (str_store_string, s3, "str_castle_is_abondened"),
        (else_try),
          (eq,"$g_encountered_party_faction","fac_player_supporters_faction"),
          (str_store_string, s3, "str_place_is_occupied_by_player"),
        (else_try),
          (lt, "$g_encountered_party_relation", 0),
          (str_store_string, s3, "str_place_is_occupied_by_enemy"),
        (else_try),
#          (str_store_string, s3, "str_place_is_occupied_by_friendly"),
        (try_end),

        (try_begin),
          (eq, "$g_leave_town_outside",1),
          (assign, "$g_leave_town_outside",0),
          (assign, "$g_permitted_to_center", 0),
          (change_screen_return),
        (else_try),
          (check_quest_active, "qst_kidnapped_girl"),
          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_giver_center, "$g_encountered_party"),
          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 3),
          (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
          (modify_visitors_at_site,":meeting_scene"),
          (reset_visitors),
          (set_visitor,0, "trp_player"),
          (set_visitor,17, "trp_kidnapped_girl"),
          (set_jump_mission, "mt_conversation_encounter"),
          (jump_to_scene, ":meeting_scene"),
          (assign, "$talk_context", tc_entering_center_quest_talk),
          (change_screen_map_conversation, "trp_kidnapped_girl"),
##        (else_try),
##          (gt, "$lord_requested_to_talk_to", 0),
##          (store_current_hours, ":cur_hours"),
##          (neq, ":cur_hours", "$quest_given_time"),
##          (modify_visitors_at_site,"scn_conversation_scene"),
##          (reset_visitors),
##          (assign, ":cur_lord", "$lord_requested_to_talk_to"),
##          (assign, "$lord_requested_to_talk_to", 0),
##          (set_visitor,0,"trp_player"),
##          (set_visitor,17,":cur_lord"),
##          (set_jump_mission,"mt_conversation_encounter"),
##          (jump_to_scene,"scn_conversation_scene"),
##          (assign, "$talk_context", tc_castle_gate_lord),
##          (change_screen_map_conversation, ":cur_lord"),
        (else_try),
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
          (jump_to_menu,"mnu_town"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),                    
          (this_or_next|party_slot_eq, "$g_encountered_party", slot_town_lord, "trp_player"),
          (faction_slot_eq, "$g_encountered_party_faction", slot_faction_leader, "trp_player"),          
          (jump_to_menu, "mnu_enter_your_own_castle"),
        (else_try),
          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_castle),
          (ge, "$g_encountered_party_relation", 0),
          (this_or_next|eq,"$castle_undefended", 1),
          (this_or_next|eq, "$g_permitted_to_center", 1),
          (eq, "$g_encountered_party_faction", "$players_kingdom"),          
          (jump_to_menu, "mnu_town"),
        (else_try),
          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_town),
          (ge, "$g_encountered_party_relation", 0),
          (jump_to_menu, "mnu_town"),
#        (else_try),
#          (eq, "$g_player_besiege_town", "$g_encountered_party"),
#          (jump_to_menu, "mnu_castle_besiege"),
        (try_end),
		
		(call_script, "script_set_town_picture"),
        ],
    [
#        ("talk_to_castle_commander",[
#            (party_get_num_companions, ":no_companions", "$g_encountered_party"),
#            (ge, ":no_companions", 1),
#            (eq,"$ruler_meeting_denied",0), #this variable is removed
#            ],
#         "Request a meeting with the lord of the castle.",[
#             (modify_visitors_at_site,"scn_conversation_scene"),(reset_visitors),
#             (set_visitor,0,"trp_player"),
#             (party_stack_get_troop_id, reg(6),"$g_encountered_party",0),
#             (party_stack_get_troop_dna,reg(7),"$g_encountered_party",0),
#             (set_visitor,17,reg(6),reg(7)),
#             (set_jump_mission,"mt_conversation_encounter"),
#             (jump_to_scene,"scn_conversation_scene"),
#             (assign, "$talk_context", tc_castle_commander),
#             (change_screen_map_conversation, reg(6))
#             ]),
      ("approach_gates",[(this_or_next|eq,"$entry_to_town_forbidden",1),
                          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_castle)],
       "Approach the gates and hail the guard.",[
                                                  (jump_to_menu, "mnu_castle_guard"),
##                                                   (modify_visitors_at_site,"scn_conversation_scene"),(reset_visitors),
##                                                   (set_visitor,0,"trp_player"),
##                                                   (store_faction_of_party, ":cur_faction", "$g_encountered_party"),
##                                                   (faction_get_slot, ":cur_guard", ":cur_faction", slot_faction_guard_troop),
##                                                   (set_visitor,17,":cur_guard"),
##                                                   (set_jump_mission,"mt_conversation_encounter"),
##                                                   (jump_to_scene,"scn_conversation_scene"),
##                                                   (assign, "$talk_context", tc_castle_gate),
##                                                   (change_screen_map_conversation, ":cur_guard")
                                                   ]),
      
      ("town_sneak",
        [
          (try_begin),
            (party_slot_eq, "$g_encountered_party", slot_party_type,spt_town),
            (str_store_string, s7, "str_town"),
          (else_try),  
            (str_store_string, s7, "str_castle"),
          (try_end),  
          
          (eq, "$entry_to_town_forbidden", 1),
          (eq, "$cant_sneak_into_town", 0)
        ],
       "Disguise yourself and try to sneak into the {s7}",
       [
         (faction_get_slot, ":player_alarm", "$g_encountered_party_faction", slot_faction_player_alarm),
         (party_get_num_companions, ":num_men", "p_main_party"),
         (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
         (val_add, ":num_men", ":num_prisoners"),
         (val_mul, ":num_men", 2),
         (val_div, ":num_men", 3),
         (store_add, ":get_caught_chance", ":player_alarm", ":num_men"),
         (store_random_in_range, ":random_chance", 0, 100),
         (try_begin),
           (this_or_next|ge, ":random_chance", ":get_caught_chance"),
           (eq, "$g_last_defeated_bandits_town", "$g_encountered_party"),
           (assign, "$g_last_defeated_bandits_town", 0),
           (assign, "$sneaked_into_town",1),
           (assign, "$town_entered", 1),
           (jump_to_menu,"mnu_sneak_into_town_suceeded"),
           (assign, "$g_mt_mode", tcm_disguised),
         (else_try),
           (jump_to_menu,"mnu_sneak_into_town_caught"),
         (try_end)
         ]),
         
#      ("castle_start_siege",
#       [
#           (this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
#           (             party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
#           (store_relation, ":reln", "$g_encountered_party_faction", "fac_player_supporters_faction"),
#           (lt, ":reln", 0),
#           (lt, "$g_encountered_party_2", 1),
#           (call_script, "script_party_count_fit_for_battle","p_main_party"),
#           (gt, reg(0), 5),
#           (try_begin),
#             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
#             (assign, reg6, 1),
#           (else_try),
#             (assign, reg6, 0),
#           (try_end),
#           ],
#       "Besiege the {reg6?town:castle}.",
#       [
#         (assign,"$g_player_besiege_town","$g_encountered_party"),
#         (store_relation, ":relation", "fac_player_supporters_faction", "$g_encountered_party_faction"),
#         (val_min, ":relation", -40),
#         (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":relation"),
#         (call_script, "script_update_all_notes"),
#         (jump_to_menu, "mnu_castle_besiege"),
#         ]),
#
#      ("cheat_castle_start_siege",
#       [
#         (eq, "$cheat_mode", 1),
#         (this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
#         (             party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
#         (store_relation, ":reln", "$g_encountered_party_faction", "fac_player_supporters_faction"),
#         (ge, ":reln", 0),
#         (lt, "$g_encountered_party_2", 1),
#         (call_script, "script_party_count_fit_for_battle","p_main_party"),
#         (gt, reg(0), 1),
#         (try_begin),
#           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
#           (assign, reg6, 1),
#         (else_try),
#           (assign, reg6, 0),
#         (try_end),
#           ],
#       "{!}CHEAT: Besiege the {reg6?town:castle}...",
#       [
#           (assign,"$g_player_besiege_town","$g_encountered_party"),
#           (jump_to_menu, "mnu_castle_besiege"),
#           ]),

      ("castle_leave",[],"Leave.",[(change_screen_return,0)]),
      ("castle_cheat_interior",[(eq, "$cheat_mode", 1)], "{!}CHEAT! Interior.",[(set_jump_mission,"mt_ai_training"),
                                                       (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
                                                       (jump_to_scene,":castle_scene"),
                                                       (change_screen_mission)]),
      ("castle_cheat_exterior",[(eq, "$cheat_mode", 1)], "{!}CHEAT! Exterior.",[
#                                                       (set_jump_mission,"mt_town_default"),
                                                       (set_jump_mission,"mt_ai_training"),
                                                       (party_get_slot, ":castle_scene", "$current_town", slot_castle_exterior),
                                                       (jump_to_scene,":castle_scene"),
                                                       (change_screen_mission)]),
      ("castle_cheat_town_walls",[(eq, "$cheat_mode", 1),(party_slot_eq,"$current_town",slot_party_type, spt_town),], "{!}CHEAT! Town Walls.",
       [
         (party_get_slot, ":scene", "$current_town", slot_town_walls),
         (set_jump_mission,"mt_ai_training"),
         (jump_to_scene,":scene"),
         (change_screen_mission)]),

    ]
  ),
   (
    "castle_guard",mnf_scale_picture,
    "You approach the gate. The men on the walls watch you closely.",
    "none",
    [
		(call_script, "script_set_town_picture"),
    ],
    [
      ("request_shelter",[(party_slot_eq, "$g_encountered_party",slot_party_type, spt_castle),
                          (ge, "$g_encountered_party_relation", 0)],
       "Request entry to the castle.",
       [(party_get_slot, ":castle_lord", "$g_encountered_party", slot_town_lord),
        (try_begin),
          (lt, ":castle_lord", 0),
          (jump_to_menu, "mnu_castle_entry_granted"),
        (else_try),
          (call_script, "script_troop_get_player_relation", ":castle_lord"),
          (assign, ":castle_lord_relation", reg0),
          #(troop_get_slot, ":castle_lord_relation", ":castle_lord", slot_troop_player_relation),
          (try_begin),
            (gt, ":castle_lord_relation", -15),
            (jump_to_menu, "mnu_castle_entry_granted"),
          (else_try),
            (jump_to_menu, "mnu_castle_entry_denied"),
          (try_end),
        (try_end),
       ]),
      ("request_meeting_commander",[],
       "Request a meeting with someone.",
       [
          (jump_to_menu, "mnu_castle_meeting"),
       ]),
      ("guard_leave",[],
       "Leave.",
       [(change_screen_return,0)]),
    ]
  ),
  (
    "castle_entry_granted",mnf_scale_picture,
    "After a brief wait, the guards open the gates for you and allow your party inside.",
    "none",
    [
		(call_script, "script_set_town_picture"),
    ],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu,"mnu_town")]),
    ]
  ),
  (
    "castle_entry_denied",mnf_scale_picture,
    "The lord of this castle has forbidden you from coming inside these walls,\
 and the guard sergeant informs you that his men will fire if you attempt to come any closer.",
    "none",
    [
		(call_script, "script_set_town_picture"),
    ],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu,"mnu_castle_guard")]),
    ]
  ),
  (
    "castle_meeting",mnf_scale_picture,
    "With whom do you want to meet?",
    "none",
    [
        (assign, "$num_castle_meeting_troops", 0),
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (call_script, "script_get_troop_attached_party", ":troop_no"),
          (eq, "$g_encountered_party", reg0),
          (troop_set_slot, "trp_temp_array_a", "$num_castle_meeting_troops", ":troop_no"),
          (val_add, "$num_castle_meeting_troops", 1),
        (try_end),
		(call_script, "script_set_town_picture"),
    ],
    [
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 0),(troop_get_slot, ":troop_no", "trp_temp_array_a", 0),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 0),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 1),(troop_get_slot, ":troop_no", "trp_temp_array_a", 1),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 1),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 2),(troop_get_slot, ":troop_no", "trp_temp_array_a", 2),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 2),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 3),(troop_get_slot, ":troop_no", "trp_temp_array_a", 3),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 3),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 4),(troop_get_slot, ":troop_no", "trp_temp_array_a", 4),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 4),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 5),(troop_get_slot, ":troop_no", "trp_temp_array_a", 5),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 5),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 6),(troop_get_slot, ":troop_no", "trp_temp_array_a", 6),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 6),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 7),(troop_get_slot, ":troop_no", "trp_temp_array_a", 7),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 7),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 8),(troop_get_slot, ":troop_no", "trp_temp_array_a", 8),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 8),(jump_to_menu,"mnu_castle_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_castle_meeting_troops", 9),(troop_get_slot, ":troop_no", "trp_temp_array_a", 9),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$castle_meeting_selected_troop", "trp_temp_array_a", 9),(jump_to_menu,"mnu_castle_meeting_selected")]),
      
      ("forget_it",[],
       "Forget it.",
       [(jump_to_menu,"mnu_castle_guard")]),
    ]
  ),
  (
    "castle_meeting_selected",0,
    "Your request for a meeting is relayed inside, and finally {s6} appears in the courtyard to speak with you.",
    "none",
    [(str_store_troop_name, s6, "$castle_meeting_selected_troop")],
    [
      ("continue",[],
       "Continue...",
       [(jump_to_menu, "mnu_castle_outside"),
        (modify_visitors_at_site,"scn_conversation_scene"),(reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,17,"$castle_meeting_selected_troop"),
        (set_jump_mission,"mt_conversation_encounter"),
        (jump_to_scene,"scn_conversation_scene"),
        (assign, "$talk_context", tc_castle_gate),
        (change_screen_map_conversation, "$castle_meeting_selected_troop"),
        ]),
    ]
  ),


#   (
#    "castle_besiege",mnf_scale_picture,
#    "You are laying siege to {s1}. {s2} {s3}",
#    "none",
#    [
#        (troop_get_type, ":is_female", "trp_player"),
#        (try_begin),
#          (eq, ":is_female", 1),
#          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
#        (else_try),
#          (set_background_mesh, "mesh_pic_siege_sighted"),
#        (try_end),
#        (assign, "$g_siege_force_wait", 0),
#        (try_begin),
#          (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
#          (party_set_slot, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
#          (store_current_hours, ":cur_hours"),
#          (party_set_slot, "$g_encountered_party", slot_center_siege_begin_hours, ":cur_hours"),
#          (assign, "$g_siege_method", 0),
#          (assign, "$g_siege_sallied_out_once", 0),
#        (try_end),
#
#        (party_get_slot, ":town_food_store", "$g_encountered_party", slot_party_food_store),
#        (call_script, "script_center_get_food_consumption", "$g_encountered_party"),
#        (assign, ":food_consumption", reg0),
#        (assign, reg7, ":food_consumption"),
#        (assign, reg8, ":town_food_store"),
#        (store_div, reg3, ":town_food_store", ":food_consumption"),
#
#        (try_begin),
#          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
#          (assign, reg6, 1),
#        (else_try),
#          (assign, reg6, 0),
#        (try_end),
#        
#        (try_begin),
#          (gt, reg3, 0),
#          (str_store_string, s2, "@The {reg6?town's:castle's} food stores should last for {reg3} more days."),
#        (else_try),
#          (str_store_string, s2, "@The {reg6?town's:castle's} food stores have run out and the defenders are starving."),
#        (try_end),
#
#        (str_store_string, s3, "str_empty_string"),
#        (try_begin),
#          (ge, "$g_siege_method", 1),
#          (store_current_hours, ":cur_hours"),
#          (try_begin),
#            (lt, ":cur_hours",  "$g_siege_method_finish_hours"),
#            (store_sub, reg9, "$g_siege_method_finish_hours", ":cur_hours"),
#            (try_begin),
#              (eq, "$g_siege_method", 1),
#              (str_store_string, s3, "@You're preparing to attack the walls, the work should finish in {reg9} hours."),
#            (else_try),
#              (eq, "$g_siege_method", 2),
#              (str_store_string, s3, "@Your forces are building a siege tower. They estimate another {reg9} hours to complete the build."),
#            (try_end),
#          (else_try),
#            (try_begin),
#              (eq, "$g_siege_method", 1),
#              (str_store_string, s3, "@You are ready to attack the walls at any time."),
#            (else_try),
#              (eq, "$g_siege_method", 2),
#              (str_store_string, s3, "@The siege tower is built and ready to make an assault."),
#            (try_end),
#          (try_end),
#        (try_end),
#        
#        #Check if enemy leaves the castle to us...
#        (try_begin),
#          (eq, "$g_castle_left_to_player",1), #we come here after dialog. Empty the castle and send parties away.
#          (assign, "$g_castle_left_to_player",0),
#          (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
#          (party_set_faction,"$g_encountered_party","fac_neutral"), #temporarily erase faction so that it is not the closest town
#          (party_get_num_attached_parties, ":num_attached_parties_to_castle","$g_encountered_party"),
#          (try_for_range_backwards, ":iap", 0, ":num_attached_parties_to_castle"),
#            (party_get_attached_party_with_rank, ":attached_party", "$g_encountered_party", ":iap"),
#            (party_detach, ":attached_party"),
#            (party_get_slot, ":attached_party_type", ":attached_party", slot_party_type),
#            (eq, ":attached_party_type", spt_kingdom_hero_party),
#            (store_faction_of_party, ":attached_party_faction", ":attached_party"),
#            (call_script, "script_get_closest_walled_center_of_faction", ":attached_party", ":attached_party_faction"),
#            (try_begin),
#              (gt, reg0, 0),
#              (call_script, "script_party_set_ai_state", ":attached_party", spai_holding_center, reg0),
#            (else_try),
#              (call_script, "script_party_set_ai_state", ":attached_party", spai_patrolling_around_center, "$g_encountered_party"),
#            (try_end),
#          (try_end),
#          (call_script, "script_party_remove_all_companions", "$g_encountered_party"),
#          (change_screen_return),
#          (party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"), #recalculate so that
#          (call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"), #leaving troops will not be considered as captured
#          (party_set_faction,"$g_encountered_party",":castle_faction"), 
#        (try_end),
#
#        #Check for victory or defeat....
#        (assign, "$g_enemy_party", "$g_encountered_party"),
#        (assign, "$g_ally_party", -1),
#        (str_store_party_name, 1,"$g_encountered_party"),
#        (call_script, "script_encounter_calculate_fit"),
#        
#        (assign, reg11, "$g_enemy_fit_for_battle"),
#        (assign, reg10, "$g_friend_fit_for_battle"),
#
#
#        (try_begin),
#          (eq, "$g_leave_encounter",1),
#          (change_screen_return),
#        (else_try),
#          (call_script, "script_party_count_fit_regulars","p_collective_enemy"),
#          (assign, ":enemy_finished", 0),
#          (try_begin),
#            (eq, "$g_battle_result", 1),
#            (assign, ":enemy_finished", 1),
#          (else_try),
#            (le, "$g_enemy_fit_for_battle", 0),
#            (ge, "$g_friend_fit_for_battle", 1),
#            (assign, ":enemy_finished", 1),
#          (try_end),
#          (this_or_next|eq, ":enemy_finished", 1),
#          (eq, "$g_enemy_surrenders", 1),
#
#          (assign, "$g_next_menu", "mnu_castle_taken"), 
#          (jump_to_menu, "mnu_total_victory"),
#        (else_try),
#          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
#          (assign, ":main_party_fit_regulars", reg0),
#          (eq, "$g_battle_result", -1),
#          (eq, ":main_party_fit_regulars", 0), #all lost (TODO : )
#          (assign, "$g_next_menu", "mnu_captivity_start_castle_defeat"),
#          (jump_to_menu, "mnu_total_defeat"),
#        (try_end),
#    ],
#    [
#      ("siege_request_meeting",[(eq, "$cant_talk_to_enemy", 0)],"Call for a meeting with the castle commander.", [
#          (assign, "$cant_talk_to_enemy", 1),
#          (assign, "$g_enemy_surrenders",0),
#          (assign, "$g_castle_left_to_player",0),
#          (assign, "$talk_context", tc_castle_commander),
#          (party_get_num_attached_parties, ":num_attached_parties_to_castle","$g_encountered_party"),
#          (try_begin),
#            (gt, ":num_attached_parties_to_castle", 0),
#            (party_get_attached_party_with_rank, ":leader_attached_party", "$g_encountered_party", 0),
#            (call_script, "script_setup_party_meeting", ":leader_attached_party"),
#          (else_try),
#            (call_script, "script_setup_party_meeting", "$g_encountered_party"),
#          (try_end),
#           ]),
#        
#      ("wait_24_hours",[],"Wait until tomorrow.", [
#          (assign,"$auto_besiege_town","$g_encountered_party"),
#          (assign, "$g_siege_force_wait", 1),
#          (store_time_of_day,":cur_time_of_day"),
#          (val_add, ":cur_time_of_day", 1),
#          (assign, ":time_to_wait", 31),
#          (val_sub,":time_to_wait",":cur_time_of_day"),
#          (val_mod,":time_to_wait",24),
#          (val_add, ":time_to_wait", 1),
#          (rest_for_hours_interactive, ":time_to_wait", 5, 1), #rest while attackable
#          (assign, "$cant_talk_to_enemy", 0),
#          (change_screen_return),
#          ]),
#
#      
#      ("castle_lead_attack",
#       [
#         (neg|troop_is_wounded, "trp_player"),
#         (ge, "$g_siege_method", 1),
#         (gt, "$g_friend_fit_for_battle", 3),
#         (store_current_hours, ":cur_hours"),
#         (ge, ":cur_hours", "$g_siege_method_finish_hours"),
#       ],
#       "Lead your soldiers in an assault.", 
#       [
#           (try_begin),
#             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
#             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
#           (else_try),
#             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
#           (try_end),
#
#           (call_script, "script_calculate_renown_value"),            
#           (call_script, "script_calculate_battle_advantage"),
#           (assign, ":battle_advantage", reg0),
#           (val_mul, ":battle_advantage", 2),
#           (val_div, ":battle_advantage", 3), #scale down the advantage a bit in sieges.
#           (set_battle_advantage, ":battle_advantage"),
#           (set_party_battle_mode),
#           (assign, "$g_siege_battle_state", 1),
#           (assign, ":siege_sally", 0),
#           (try_begin),
#             (le, ":battle_advantage", -4), #we are outnumbered, defenders sally out
#             (eq, "$g_siege_sallied_out_once", 0),
#             (set_jump_mission,"mt_castle_attack_walls_defenders_sally"),
#             (assign, "$g_siege_battle_state", 0),
#             (assign, ":siege_sally", 1),
#           (else_try),
#             (party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
#             (set_jump_mission,"mt_castle_attack_walls_belfry"),
#           (else_try),
#             (set_jump_mission,"mt_castle_attack_walls_ladder"),
#           (try_end),
#           (assign, "$cant_talk_to_enemy", 0),           
#           (assign, "$g_siege_final_menu", "mnu_castle_besiege"),
#           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
#           (assign, "$g_siege_method", 0), #reset siege timer
#           (jump_to_scene,":battle_scene"),
#           (try_begin),
#             (eq, ":siege_sally", 1),
#             (jump_to_menu, "mnu_siege_attack_meets_sally"),
#           (else_try),
#             (jump_to_menu, "mnu_battle_debrief"),
#             (change_screen_mission),
#           (try_end),
#       ]),
#      ("attack_stay_back",
#       [
#         (ge, "$g_siege_method", 1),
#         (gt, "$g_friend_fit_for_battle", 3),
#         (store_current_hours, ":cur_hours"),
#         (ge, ":cur_hours",  "$g_siege_method_finish_hours"),
#         ],
#       "Order your soldiers to attack while you stay back...", [(assign, "$cant_talk_to_enemy", 0),(jump_to_menu,"mnu_castle_attack_walls_simulate")]),
#
#      ("build_ladders",[(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 0),(eq, "$g_siege_method", 0)],
#       "Prepare ladders to attack the walls.", [(jump_to_menu,"mnu_construct_ladders")]),
#
#     ("build_siege_tower",[(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),(eq, "$g_siege_method", 0)],
#      "Build a siege tower.", [(jump_to_menu,"mnu_construct_siege_tower")]),
#
#      ("cheat_castle_lead_attack",[(eq, "$cheat_mode", 1),
#                                   (eq, "$g_siege_method", 0)],
#       "{!}CHEAT: Instant build equipments.",
#       [
#         (assign, "$g_siege_method", 1),
#         (assign, "$g_siege_method_finish_hours", 0),
#         (jump_to_menu, "mnu_castle_besiege"),
#       ]),
#
#      ("cheat_conquer_castle",[(eq, "$cheat_mode", 1),
#                                   ],
#       "{!}CHEAT: Instant conquer castle.",
#       [
#        (assign, "$g_next_menu", "mnu_castle_taken"),
#        (jump_to_menu, "mnu_total_victory"),
#       ]),
#	   
#      ("lift_siege",[],"Abandon the siege.",
#       [
#         (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
#         (assign,"$g_player_besiege_town", -1),
#         (change_screen_return)]),
#    ]
#  ),
#  
#  (
#    "siege_attack_meets_sally",mnf_scale_picture,
#    "The defenders sally out to meet your assault.",
#    "none",
#    [
#        (set_background_mesh, "mesh_pic_sally_out"),
#    ],
#    [
#      ("continue",[],
#       "Continue...",
#       [
#             (jump_to_menu, "mnu_battle_debrief"),
#             (change_screen_mission),
#       ]),
#    ]
#  ),
#
#   (
#    "castle_besiege_inner_battle",mnf_scale_picture,
#    "{s1}",
#    "none",
#    [
#        (troop_get_type, ":is_female", "trp_player"),
#        (try_begin),
#          (eq, ":is_female", 1),
#          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
#        (else_try),
#          (set_background_mesh, "mesh_pic_siege_sighted"),
#        (try_end),
#        (assign, ":result", "$g_battle_result"),#will be reset at script_encounter_calculate_fit
#        (call_script, "script_encounter_calculate_fit"),
#        
## TODO: To use for the future:
#            (str_store_string, s1, "@As a last defensive effort, you retreat to the main hall of the keep.\
# You and your remaining soldiers will put up a desperate fight here. If you are defeated, there's no other place to fall back to."),
#            (str_store_string, s1, "@You've been driven away from the walls.\
# Now the attackers are pouring into the streets. IF you can defeat them, you can perhaps turn the tide and save the day."),
#        (try_begin),
#          (this_or_next|neq, ":result", 1),
#          (this_or_next|le, "$g_friend_fit_for_battle", 0),
#          (le, "$g_enemy_fit_for_battle", 0),
#          (jump_to_menu, "$g_siege_final_menu"),
#        (else_try),
#          (call_script, "script_encounter_calculate_fit"),
#          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
#          (try_begin),
#            (eq, "$g_siege_battle_state", 0),
#            (eq, ":result", 1),
#            (assign, "$g_battle_result", 0),
#            (jump_to_menu, "$g_siege_final_menu"),
#          (else_try),
#            (eq, "$g_siege_battle_state", 1),
#            (eq, ":result", 1),
#            (str_store_string, s1, "@You've breached the town walls,\
# but the stubborn defenders continue to resist you in the streets!\
# You'll have to deal with them before you can attack the keep at the heart of the town."),
#          (else_try),
#            (eq, "$g_siege_battle_state", 2),
#            (eq, ":result", 1),
#            (str_store_string, s1, "@The town centre is yours,\
# but the remaining defenders have retreated to the castle.\
# It must fall before you can complete your victory."),
#          (else_try),
#            (jump_to_menu, "$g_siege_final_menu"),
#          (try_end),
#        (else_try),
#          (try_begin),
#            (eq, "$g_siege_battle_state", 0),
#            (eq, ":result", 1),
#            (assign, "$g_battle_result", 0),
#            (jump_to_menu, "$g_siege_final_menu"),
#          (else_try),
#            (eq, "$g_siege_battle_state", 1),
#            (eq, ":result", 1),
#            (str_store_string, s1, "@The remaining defenders have retreated to the castle as a last defense. You must go in and crush any remaining resistance."),
#          (else_try),
#            (jump_to_menu, "$g_siege_final_menu"),
#          (try_end),
#        (try_end),
#    ],
#    [
#      ("continue",[],
#       "Continue...",
#       [
#           (try_begin),
#             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
#             (try_begin),
#               (eq, "$g_siege_battle_state", 1),
#               (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_center),
#               (set_jump_mission, "mt_besiege_inner_battle_town_center"),
#             (else_try),
#               (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_castle),
#               (set_jump_mission, "mt_besiege_inner_battle_castle"),
#             (try_end),
#           (else_try),
#             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_castle),
#             (set_jump_mission, "mt_besiege_inner_battle_castle"),
#           (try_end),
###           (call_script, "script_calculate_battle_advantage"),
###           (set_battle_advantage, reg0),
#           (set_party_battle_mode),
#           (jump_to_scene, ":battle_scene"),
#           (val_add, "$g_siege_battle_state", 1),
#           (assign, "$g_next_menu", "mnu_castle_besiege_inner_battle"),
#           (jump_to_menu, "mnu_battle_debrief"),
#           (change_screen_mission),
#       ]),
#    ]
#  ),
#
#  
#  (
#    "construct_ladders",0,
#    "As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that it will take\
# {reg4} hours to build enough scaling ladders for the assault.",
#    "none",
#    [(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
#     (assign, ":max_skill", reg0),
#     (assign, ":max_skill_owner", reg1),
#     (assign, reg2, ":max_skill"),
#
#     (store_sub, reg4, 14, ":max_skill"),
#     (val_mul, reg4, 2),
#     (val_div, reg4, 3),
#     
#     (try_begin),
#       (eq, ":max_skill_owner", "trp_player"),
#       (assign, reg3, 1),
#     (else_try),
#       (assign, reg3, 0),
#       (str_store_troop_name, s3, ":max_skill_owner"),
#     (try_end),
#    ],
#    [
#      ("build_ladders_cont",[],
#       "Do it.", [
#           (assign, "$g_siege_method", 1),
#           (store_current_hours, ":cur_hours"),
#           (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
#           (store_sub, ":hours_takes", 14, reg0),
#           (val_mul, ":hours_takes", 2),
#           (val_div, ":hours_takes", 3),
#           (store_add, "$g_siege_method_finish_hours",":cur_hours", ":hours_takes"),
#           (assign,"$auto_besiege_town","$current_town"),
#           (rest_for_hours_interactive, 96, 5, 1), #rest while attackable. A trigger will divert control when attack is ready.
#           (change_screen_return),
#           ]),
#      ("go_back",[],
#       "Go back.", [(jump_to_menu,"mnu_castle_besiege")]),
#        ],
#  ),
#
#  
#  (
#    "construct_siege_tower",0,
#    "As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that building a siege tower will take\
# {reg4} hours.",
#    "none",
#    [(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
#     (assign, ":max_skill", reg0),
#     (assign, ":max_skill_owner", reg1),
#     (assign, reg2, ":max_skill"),
#
#     (store_sub, reg4, 15, ":max_skill"),
#     (val_mul, reg4, 6),
#     
#     (try_begin),
#       (eq, ":max_skill_owner", "trp_player"),
#       (assign, reg3, 1),
#     (else_try),
#       (assign, reg3, 0),
#       (str_store_troop_name, s3, ":max_skill_owner"),
#     (try_end),
#    ],
#    [
#      ("build_siege_tower_cont",[],
#       "Start building.", [
#           (assign, "$g_siege_method", 2),
#           (store_current_hours, ":cur_hours"),
#           (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
#           (store_sub, ":hours_takes", 15, reg0),
#           (val_mul, ":hours_takes", 6),
#           (store_add, "$g_siege_method_finish_hours",":cur_hours", ":hours_takes"),
#           (assign,"$auto_besiege_town","$current_town"),
#           (rest_for_hours_interactive, 240, 5, 1), #rest while attackable. A trigger will divert control when attack is ready.
#           (change_screen_return),
#           ]),
#      ("go_back",[],
#       "Go back.", [(jump_to_menu,"mnu_castle_besiege")]),
#        ],
#  ),
#
#   (
#    "castle_attack_walls_simulate",mnf_scale_picture|mnf_disable_all_keys,
#    "{s4}^^Your casualties:{s8}^^Enemy casualties were: {s9}",
#    "none",
#    [
#        (try_begin),
#          (set_background_mesh, "mesh_pic_siege_attack"),
#        (try_end),
#        
#        (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
#        (assign, ":player_party_strength", reg0),
#        (val_div, ":player_party_strength", 10),
#
#        (call_script, "script_party_calculate_strength", "$g_encountered_party", 0),
#        (assign, ":enemy_party_strength", reg0),
#        (val_div, ":enemy_party_strength", 4),
#
#        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength", "p_temp_casualties"),
#        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#        (str_store_string_reg, s8, s0),
#
#        (inflict_casualties_to_party_group, "$g_encountered_party", ":player_party_strength", "p_temp_casualties"),
#        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#        (str_store_string_reg, s9, s0),
#
#        (assign, "$no_soldiers_left", 0),
#        (try_begin),
#          (call_script, "script_party_count_members_with_full_health","p_main_party"),
#          (le, reg0, 0), #(TODO : compare with num_routed_us)
#          (assign, "$no_soldiers_left", 1),
#          (str_store_string, s4, "str_attack_walls_failure"),
#        (else_try),
#          (call_script, "script_party_count_members_with_full_health","$g_encountered_party"),
#          (le, reg0, 0), #(TODO : compare with num_routed_enemies)
#          (assign, "$no_soldiers_left", 1),
#          (assign, "$g_battle_result", 1),
#          (str_store_string, s4, "str_attack_walls_success"),
#        (else_try),
#          (str_store_string, s4, "str_attack_walls_continue"),
#        (try_end),
#     ],
#    [
###      ("lead_next_wave",[(eq, "$no_soldiers_left", 0)],"Lead the next wave of attack personally.", [
###           (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
###           (set_party_battle_mode),
###           (set_jump_mission,"mt_castle_attack_walls"),
###           (jump_to_scene,":battle_scene"),
###           (jump_to_menu,"mnu_castle_outside"),
###           (change_screen_mission),
###       ]),
###      ("continue_attacking",[(eq, "$no_soldiers_left", 0)],"Order your soldiers to keep attacking...", [
###                                    (jump_to_menu,"mnu_castle_attack_walls_3"),
###                                    ]),
###      ("call_soldiers_back",[(eq, "$no_soldiers_left", 0)],"Call your soldiers back.",[(jump_to_menu,"mnu_castle_outside")]),
#      ("continue",[],"Continue...",[(jump_to_menu,"mnu_castle_besiege")]),
#    ]
#  ),
#  
#   (
#    "castle_attack_walls_with_allies_simulate",mnf_scale_picture|mnf_disable_all_keys,
#    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
#    "none",
#    [
#        (try_begin),
#          (set_background_mesh, "mesh_pic_siege_attack"),
#        (try_end),
#
#        (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
#        (assign, ":player_party_strength", reg0),
#        (val_div, ":player_party_strength", 10),
#        (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
#        (assign, ":friend_party_strength", reg0),
#        (val_div, ":friend_party_strength", 10),
#
#        (val_max, ":friend_party_strength", 1),
#
#        (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
#        (assign, ":enemy_party_strength", reg0),
#        (val_div, ":enemy_party_strength", 4),
#
###        (assign, reg0, ":player_party_strength"),
###        (assign, reg1, ":friend_party_strength"),
###        (assign, reg2, ":enemy_party_strength"),
###        (assign, reg3, "$g_enemy_party"),
###        (assign, reg4, "$g_ally_party"),
###        (display_message, "@{!}player_str={reg0} friend_str={reg1} enemy_str={reg2}"),
###        (display_message, "@{!}enemy_party={reg3} ally_party={reg4}"),
#
#        (try_begin),
#          (eq, ":friend_party_strength", 0),
#          (store_div, ":enemy_party_strength_for_p", ":enemy_party_strength", 2),
#        (else_try),
#          (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
#          (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
#          (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
#        (try_end),
#
#        (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
#        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
#        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#        (str_store_string_reg, s8, s0),
#                                    
#        (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
#        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#        (str_store_string_reg, s10, s0),
#
#        (call_script, "script_collect_friendly_parties"),
#
#        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
#        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#        (str_store_string_reg, s9, s0),
#
#        (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),
#
#        (assign, "$no_soldiers_left", 0),
#        (try_begin),
#          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
#          (le, reg0, 0), #(TODO : compare with num_routed_us)
#          (assign, "$no_soldiers_left", 1),
#          (str_store_string, s4, "str_attack_walls_failure"),
#        (else_try),
#          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
#          (le, reg0, 0), #(TODO : compare with num_routed_enemies)
#          (assign, "$no_soldiers_left", 1),
#          (assign, "$g_battle_result", 1),
#          (str_store_string, s4, "str_attack_walls_success"),
#        (else_try),
#          (str_store_string, s4, "str_attack_walls_continue"),
#        (try_end),
#     ],
#    [
#      ("continue",[],"Continue...",[(jump_to_menu,"mnu_besiegers_camp_with_allies")]),
#    ]
#  ),
#
#  (
#    "castle_taken_by_friends",0,
#    "Nothing to see here.",
#    "none",
#    [
#        (party_clear, "$g_encountered_party"),
#        (party_stack_get_troop_id, ":leader", "$g_encountered_party_2", 0),
#        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, ":leader"),
#        (store_troop_faction, ":faction_no", ":leader"),
#        #Reduce prosperity of the center by 5
#        (call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
#		(try_begin),
#			(assign, ":damage", 20),
#			(is_between, "$g_encountered_party", towns_begin, towns_end),
#			(assign, ":damage", 40),
#		(try_end),
#		(try_begin),
#			(neq, ":faction_no", "$g_encountered_party_faction"),
#			(call_script, "script_faction_inflict_war_damage_on_faction", ":faction_no", "$g_encountered_party_faction", ":damage"),
#		(try_end),
#		
#        (call_script, "script_give_center_to_faction", "$g_encountered_party", ":faction_no"),
#        (call_script, "script_add_log_entry", logent_player_participated_in_siege, "trp_player",  "$g_encountered_party", 0, "$g_encountered_party_faction"),
###        (call_script, "script_change_troop_renown", "trp_player", 1),
#        (change_screen_return),
#    ],
#    [
#    ],
#  ),
#
#
#  (
#    "castle_taken",mnf_disable_all_keys,
#    "{s3} has fallen to your troops, and you now have full control of the {reg2?town:castle}.\
#{reg1? You may station troops here to defend it against enemies who may try to recapture it. Also, you should select now whether you will hold the {reg2?town:castle} yourself or give it to a faithful vassal...:}",# Only visible when castle is taken without being a vassal of a kingdom.
#    "none",
#    [
#        (party_clear, "$g_encountered_party"),
#
#        (try_begin),        
#          (eq, "$players_kingdom", "fac_player_supporters_faction"),
#          (party_get_slot, ":new_owner", "$g_encountered_party", slot_town_lord),
#          (neq, ":new_owner", "trp_player"),
#          
#          (try_for_range, ":unused", 0, 4),
#            (call_script, "script_cf_reinforce_party", "$g_encountered_party"),
#          (try_end),  
#        (try_end),
#        
#        (call_script, "script_lift_siege", "$g_encountered_party", 0),
#        (assign, "$g_player_besiege_town", -1),
#                        
#        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
#        #Reduce prosperity of the center by 5
#        (call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
#
#        (call_script, "script_change_troop_renown", "trp_player", 5),		
#
#		(assign, ":damage", 20),
#		(try_begin),
#			(is_between, "$g_encountered_party", towns_begin, towns_end),
#			(assign, ":damage", 40),
#		(try_end),
#		(call_script, "script_faction_inflict_war_damage_on_faction", "$players_kingdom", "$g_encountered_party_faction", ":damage"),
#		
#		#removed, is it duplicate (useless)? See 20 lines above.
#        #(call_script, "script_add_log_entry", logent_castle_captured_by_player, "trp_player", "$g_encountered_party", -1, "$g_encountered_party_faction"),
#        
#        (try_begin),
#          (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
#          (neq, "$players_kingdom", "fac_player_supporters_faction"),
#          (call_script, "script_give_center_to_faction", "$g_encountered_party", "$players_kingdom"),
#          (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "$players_kingdom"),
#          (jump_to_menu, "mnu_castle_taken_2"),
#        (else_try),
#          (call_script, "script_give_center_to_faction", "$g_encountered_party", "fac_player_supporters_faction"),          
#          (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "fac_player_supporters_faction"),
#          (str_store_party_name, s3, "$g_encountered_party"),
#          (assign, reg1, 0),
#          (try_begin),
#            (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
#            (assign, reg1, 1),
#          (try_end),          
#		  #(party_set_slot, "$g_encountered_party", slot_town_lord, stl_unassigned),		  
#        (try_end),
#        (assign, reg2, 0),
#        (try_begin),
#          (is_between, "$g_encountered_party", towns_begin, towns_end),
#          (assign, reg2, 1),
#        (try_end),
#    ],
#    [
#      ("continue",[],"Continue...",
#       [         
#         (assign, "$auto_enter_town", "$g_encountered_party"),                  
#         (change_screen_return),
#        ]),
#    ],        
#  ),
#  (
#    "castle_taken_2",mnf_disable_all_keys,
#    "{s3} has fallen to your troops, and you now have full control of the castle.\
# It is time to send word to {s9} about your victory. {s5}",
#    "none",
#    [
#        (str_store_party_name, s3, "$g_encountered_party"),
#        (str_clear, s5),
#        (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
#        (str_store_troop_name, s9, ":faction_leader"),
#        (try_begin),
#          (eq, "$player_has_homage", 0),
#          (assign, reg8, 0),
#          (try_begin),
#            (party_slot_eq, "$g_encountered_party", spt_town),
#            (assign, reg8, 1),
#          (try_end),
#          (str_store_string, s5, "@However, since you are not a sworn {man/follower} of {s9}, there is no chance he would recognize you as the {lord/lady} of this {reg8?town:castle}."),
#        (try_end),
#    ],
#    [
#        ("castle_taken_claim",[(eq, "$player_has_homage", 1)],
#		"Request that {s3} be awarded to you.",
#        [
#       (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
#        (assign, "$g_castle_requested_by_player", "$current_town"),
#		(assign, "$g_castle_requested_for_troop", "trp_player"),
#        (assign, "$auto_enter_town", "$g_encountered_party"),
#        (change_screen_return),
#        ]),
#
#		("castle_taken_claim_2",[
#		(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
#		(is_between, ":spouse", active_npcs_begin, active_npcs_end),
#		(troop_slot_eq, ":spouse", slot_troop_occupation, slto_kingdom_hero),
#		(store_faction_of_troop, ":spouse_faction", ":spouse"),
#		(eq, ":spouse_faction", "$players_kingdom"),
#		],
#		"Request that {s3} be awarded to your {wife/husband}.",
#        [
#        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
#        (assign, "$g_castle_requested_by_player", "$current_town"),
#		(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
#		(assign, "$g_castle_requested_for_troop", ":spouse"),
#        (assign, "$auto_enter_town", "$g_encountered_party"),
#        (change_screen_return),
#        ]),
#		
#		
#		
#      ("castle_taken_no_claim",[],"Ask no rewards.",
#       [
#        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, -1),
#        (assign, "$auto_enter_town", "$g_encountered_party"),
#        (change_screen_return),
##        (jump_to_menu, "mnu_town"),
#        ]),
#    ],
#  ),
#
#(
#    "requested_castle_granted_to_player",mnf_scale_picture,
#    "You receive a message from your liege, {s3}.^^\
# {reg4?She:He} has decided to grant {s2}{reg3? and the nearby village of {s4}:} to you, with all due incomes and titles, to hold in {reg4?her:his} name for as long as you maintain your oath of homage..",
#    "none",
#    [
#		(set_background_mesh, "mesh_pic_messenger"),
#		(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
#		(str_store_troop_name, s3, ":faction_leader"),
#		(str_store_party_name, s2, "$g_center_to_give_to_player"),
#		(try_begin),
#			(party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
#			(assign, reg3, 1),
#			(try_for_range, ":cur_village", villages_begin, villages_end),
#				(party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
#				(str_store_party_name, s4, ":cur_village"),
#			(try_end),
#		(else_try),
#			(assign, reg3, 0),
#		(try_end),
#		(troop_get_type, reg4, ":faction_leader"),
#	 
#   ],
#    [
#		("continue",[],"Continue.",
#			[
#			(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
#			(jump_to_menu, "mnu_give_center_to_player_2"),
#			],
#		),
#	]
#),
#  
#
#
#(
#    "requested_castle_granted_to_player_husband", mnf_scale_picture,
#    "You receive a message from your liege, {s3}.^^\
# {reg4?She:He} has decided to grant {s2}{reg3? and the nearby village of {s4}:} to your husband, {s7}.",	 
#    "none",
#    [
#		(set_background_mesh, "mesh_pic_messenger"),
#		(faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
#		(str_store_troop_name, s3, ":faction_leader"),
#		(str_store_party_name, s2, "$g_center_to_give_to_player"),
#		(try_begin),
#			(party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
#			(assign, reg3, 1),
#			(try_for_range, ":cur_village", villages_begin, villages_end),
#				(party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
#				(str_store_party_name, s4, ":cur_village"),
#			(try_end),
#		(else_try),
#			(assign, reg3, 0),
#		(try_end),
#		(troop_get_type, reg4, ":faction_leader"),
#	 
#		(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
#		(str_store_troop_name, s11, ":spouse"), 
#		(str_store_string, s7, "str_to_your_husband_s11"),	 
#    ],
#    [
#		("continue",[],"Continue.",
#			[
#			(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
#			(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", ":spouse", 0),
#			],
#		),
#	]
#),
#
#  
#(
#    "requested_castle_granted_to_another",mnf_scale_picture,
#    "You receive a message from your monarch, {s3}.^^\
# 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts.\
# You also requested me to give you ownership of the castle, but that is a favour which I fear I cannot grant,\
# as you already hold significant estates in my realm.\
# Instead I have sent you {reg6} denars to cover the expenses of your campaign, but {s2} I give to {s5}.'\
# ",
#    "none",
#    [(set_background_mesh, "mesh_pic_messenger"),
#     (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
#     (str_store_troop_name, s3, ":faction_leader"),
#     (str_store_party_name, s2, "$g_center_to_give_to_player"),
#     (party_get_slot, ":new_owner", "$g_center_to_give_to_player", slot_town_lord),
#     (str_store_troop_name, s5, ":new_owner"),
#     (assign, reg6, 900),
#	 
#	 (assign, "$g_castle_requested_by_player", -1),
#	 (assign, "$g_castle_requested_for_troop", -1),
#	 
#    ],
#    [
#      ("accept_decision",[],"Accept the decision.",
#       [
#       (call_script, "script_troop_add_gold", "trp_player", reg6),
#       (change_screen_return),
#       ]),
#	   
#       ("leave_faction",[],"You have been wronged! Renounce your oath to your liege! ",
#       [
#         (jump_to_menu, "mnu_leave_faction"),
#         (call_script, "script_troop_add_gold", "trp_player", reg6),
#        ]),
#     ],
#  ),
#
#  
#(
#    "requested_castle_granted_to_another_female",mnf_scale_picture,
#    "You receive a message from your monarch, {s3}.^^\
# 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts.\
# You also requested me to give ownership of the castle to your husband, but that is a favour which I fear I cannot grant,\
# as he already holds significant estates in my realm.\
# Instead I have sent you {reg6} denars to cover the expenses of your campaign, but {s2} I give to {s5}.'\
# ",
#    "none",
#    [(set_background_mesh, "mesh_pic_messenger"),
#     (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
#     (str_store_troop_name, s3, ":faction_leader"),
#     (str_store_party_name, s2, "$g_center_to_give_to_player"),
#     (party_get_slot, ":new_owner", "$g_center_to_give_to_player", slot_town_lord),
#     (str_store_troop_name, s5, ":new_owner"),
#     (assign, reg6, 900),
#
#	 (assign, "$g_castle_requested_by_player", -1),
#	 (assign, "$g_castle_requested_for_troop", -1),
#    ],
#	
#    [
#		("accept_decision",[],"Accept the decision.",
#        [
#        (call_script, "script_troop_add_gold", "trp_player", reg6),
#        (change_screen_return),
#        ]),
#    ],
#),
#  
#  
#  
#  (
#    "leave_faction",0,
#    "Renouncing your oath is a grave act. Your lord may condemn you and confiscate your lands and holdings.\
# However, if you return them of your own free will, he may let the betrayal go without a fight.",
#    "none",
#    [
#    ],
#    [
#      ("leave_faction_give_back", [], "Renounce your oath and give up your holdings.",
#       [
##Troop commentary changes begin
##        (call_script, "script_add_log_entry", logent_renounced_allegiance,   "trp_player",  -1, "$g_talk_troop", "$g_talk_troop_faction"),
##Troop commentary changes end
#        (call_script, "script_player_leave_faction", 1), #1 means give back fiefs
#        (change_screen_return),
#        ]),
#      ("leave_faction_hold", [
#          (str_store_party_name, s2, "$g_center_to_give_to_player"),
#          ], "Renounce your oath and rule your lands, including {s2}, in your own name.",
#       [
#        (call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0), #this should activate the player faction (it does not)
#        (call_script, "script_player_leave_faction", 0), #"1" would mean give back fiefs
#		(call_script, "script_activate_player_faction", "trp_player"), #Activating player faction should now work
#        (change_screen_return),
#        ]),
#      ("leave_faction_cancel", [], "Remain loyal and accept the decision.",
#       [
#        (change_screen_return),
#        ]),
#    ],
#  ),
#
#  (
#    "give_center_to_player",mnf_scale_picture,
#    "Your lord offers to extend your fiefs!\
# {s1} sends word that he is willing to grant {s2} to you in payment for your loyal service,\
# adding it to your holdings. What is your answer?",
#    "none",
#    [(set_background_mesh, "mesh_pic_messenger"),
#     (store_faction_of_party, ":center_faction", "$g_center_to_give_to_player"),
#     (faction_get_slot, ":faction_leader", ":center_faction", slot_faction_leader),
#     (str_store_troop_name, s1, ":faction_leader"),
#     (str_store_party_name, s2, "$g_center_to_give_to_player"),
#    ],
#    [
#      ("give_center_to_player_accept",[],"Accept the offer.",
#       [(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
#        (jump_to_menu, "mnu_give_center_to_player_2"),
#        ]),
#      ("give_center_to_player_reject",[],"Reject. You have no interest in holding {s2}.",
#       [(party_set_slot, "$g_center_to_give_to_player", slot_town_lord, stl_rejected_by_player),
#        (change_screen_return),
#        ]),
#    ],
#  ),
#  
#  (
#    "give_center_to_player_2",0,
#    "With a brief ceremony, you are officially confirmed as the new lord of {s2}{reg3? and its bound village {s4}:}.\
# {reg3?They:It} will make a fine part of your fiefdom.\
# You can now claim the rents and revenues from your personal estates there, draft soldiers from the populace,\
# and manage the lands as you see fit.\
# However, you are also expected to defend your fief and your people from harm,\
# as well as maintaining the rule of law and order.",
#    "none",
#    [
#      (str_store_party_name, s2, "$g_center_to_give_to_player"),
#      (assign, reg3, 0),
#      (try_begin),
#        (party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
#        (try_for_range, ":cur_village", villages_begin, villages_end),
#          (party_slot_eq, ":cur_village", slot_village_bound_center, "$g_center_to_give_to_player"),
#          (str_store_party_name, s4, ":cur_village"),
#          (assign, reg3, 1),
#        (try_end),
#      (try_end),
#    ],
#    [
#      ("continue",[],"Continue...",
#       [(change_screen_return),
#        ]),
#    ],
#  ),
#
#
#  (
#    "siege_started_defender",0,
#    "{s1} is launching an assault against the walls of {s2}. You have {reg10} troops fit for battle against the enemy's {reg11}. You decide to...",
#    "none",
#    [
#        (select_enemy,1),
#        (assign, "$g_enemy_party", "$g_encountered_party_2"),
#        (assign, "$g_ally_party", "$g_encountered_party"),
#        (str_store_party_name, 1,"$g_enemy_party"),
#        (str_store_party_name, 2,"$g_ally_party"),
#        (call_script, "script_encounter_calculate_fit"),
#        (try_begin),
#          (eq, "$g_siege_first_encounter", 1),
#          (call_script, "script_let_nearby_parties_join_current_battle", 0, 1),
#          (call_script, "script_encounter_init_variables"),
#        (try_end),
#
#        (try_begin),
#          (eq, "$g_siege_first_encounter", 0),
#          (try_begin),
#            (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
#            (assign, ":num_enemy_regulars_remaining", reg0),
#            (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
#            (assign, ":num_ally_regulars_remaining", reg0),
#            (assign, ":enemy_finished", 0),
#            (try_begin),
#              (eq, "$g_battle_result", 1),
#              (eq, ":num_enemy_regulars_remaining", 0), #battle won (TODO : compare with num_routed_us)
#              (assign, ":enemy_finished",1),
#            (else_try),
#              (eq, "$g_engaged_enemy", 1),
#              (le, "$g_enemy_fit_for_battle",0),
#              (ge, "$g_friend_fit_for_battle",1),
#              (assign, ":enemy_finished",1),
#            (try_end),
#            (this_or_next|eq, ":enemy_finished",1),
#            (eq,"$g_enemy_surrenders",1),
#            (assign, "$g_next_menu", -1),
#            (jump_to_menu, "mnu_total_victory"),
#          (else_try),
#            (assign, ":battle_lost", 0),
#            (try_begin),
#              (this_or_next|eq, "$g_battle_result", -1),
#              (troop_is_wounded,  "trp_player"),
#              (eq, ":num_ally_regulars_remaining", 0), #(TODO : compare with num_routed_allies)
#              (assign, ":battle_lost",1),
#            (try_end),
#            (this_or_next|eq, ":battle_lost",1),
#            (eq,"$g_player_surrenders",1),
#            (assign, "$g_next_menu", "mnu_captivity_start_under_siege_defeat"),
#            (jump_to_menu, "mnu_total_defeat"),
#          (else_try),
#            # Ordinary victory/defeat.
#            (assign, ":attackers_retreat", 0),
#            (try_begin),
#            #check whether enemy retreats
#              (eq, "$g_battle_result", 1),
#  ##            (store_mul, ":min_enemy_str", "$g_enemy_fit_for_battle", 2),
#  ##            (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
#              (assign, ":attackers_retreat", 1),
#            (else_try),
#              (eq, "$g_battle_result", 0),
#              (store_div, ":min_enemy_str", "$g_enemy_fit_for_battle", 3),
#              (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
#              (assign, ":attackers_retreat", 1),
#            (else_try),
#              (store_random_in_range, ":random_no", 0, 100),
#              (store_mul, ":num_ally_regulars_remaining_multiplied", ":num_ally_regulars_remaining", 13),
#              (val_div, ":num_ally_regulars_remaining_multiplied", 10),
#              (ge, ":num_ally_regulars_remaining_multiplied", ":num_enemy_regulars_remaining"),
#              (lt, ":random_no", 10),
#              (neq, "$new_encounter", 1),
#              (assign, ":attackers_retreat", 1),
#            (try_end),
#            (try_begin),
#              (eq, ":attackers_retreat", 1),
#              (party_get_slot, ":siege_hardness", "$g_encountered_party", slot_center_siege_hardness),
#              (val_add, ":siege_hardness", 100),
#              (party_set_slot, "$g_encountered_party", slot_center_siege_hardness, ":siege_hardness"),
#              (party_set_slot, "$g_enemy_party", slot_party_retreat_flag, 1),
#
#              (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
#                (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
#                #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
#                (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
#                (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
#                (gt, ":party_no", 0),
#                (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
#                (party_slot_eq, ":party_no", slot_party_ai_object, "$g_encountered_party"),
#                (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
#                (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
#                (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, "$g_encountered_party"),
#              (try_end),
#              (display_message, "@The enemy has been forced to retreat. The assault is over, but the siege continues."),
#              (assign, "$g_battle_simulation_cancel_for_party", "$g_encountered_party"),
#              (leave_encounter),
#              (change_screen_return),
#              (assign, "$g_battle_simulation_auto_enter_town_after_battle", "$g_encountered_party"),
#            (try_end),
#          (try_end),
#        (try_end),
#        (assign, "$g_siege_first_encounter", 0),
#        (assign, "$new_encounter", 0),
#        ],
#    [
#      ("siege_defender_join_battle",
#       [
#         (neg|troop_is_wounded, "trp_player"),
#         ],
#          "Join the battle.",[              
#              (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
#              (assign, "$g_battle_result", 0),
#              (try_begin),
#                (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
#                (party_get_slot, ":battle_scene", "$g_encountered_party", slot_town_walls),
#              (else_try),
#                (party_get_slot, ":battle_scene", "$g_encountered_party", slot_castle_exterior),
#              (try_end),
#              (call_script, "script_calculate_battle_advantage"),
#              (val_mul, reg0, 2),
#              (val_div, reg0, 3), #scale down the advantage a bit.
#              (set_battle_advantage, reg0),
#              (set_party_battle_mode),
#              (try_begin),
#                (party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
#                (set_jump_mission,"mt_castle_attack_walls_belfry"),
#              (else_try),
#                (set_jump_mission,"mt_castle_attack_walls_ladder"),
#              (try_end),
#              (jump_to_scene,":battle_scene"),
#              (assign, "$g_next_menu", "mnu_siege_started_defender"),
#              (jump_to_menu, "mnu_battle_debrief"),
#              (change_screen_mission)]),
#      ("siege_defender_troops_join_battle",[(call_script, "script_party_count_members_with_full_health", "p_main_party"),
#                                            (this_or_next|troop_is_wounded,  "trp_player"),
#                                            (ge, reg0, 3)],
#          "Order your men to join the battle without you.",[
#              (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
#              (select_enemy,1),
#              (assign,"$g_enemy_party","$g_encountered_party_2"),
#              (assign,"$g_ally_party","$g_encountered_party"),
#              (assign,"$g_siege_join", 1),
#              (jump_to_menu,"mnu_siege_join_defense")]),
#    ]
#  ),
#
#  (
#    "siege_join_defense",mnf_disable_all_keys,
#    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
#    "none",
#    [
#        (try_begin),
#          (eq, "$g_siege_join", 1),
#          (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
#          (assign, ":player_party_strength", reg0),
#          (val_div, ":player_party_strength", 5),
#        (else_try),
#          (assign, ":player_party_strength", 0),
#        (try_end),
#        
#        (call_script, "script_party_calculate_strength", "p_collective_ally", 0),
#        (assign, ":ally_party_strength", reg0),
#        (val_div, ":ally_party_strength", 5),
#        (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
#        (assign, ":enemy_party_strength", reg0),
#        (val_div, ":enemy_party_strength", 10),
#
#        (store_add, ":friend_party_strength", ":player_party_strength", ":ally_party_strength"),
#        (try_begin),
#          (eq, ":friend_party_strength", 0),
#          (store_div, ":enemy_party_strength_for_p", ":enemy_party_strength", 2),
#        (else_try),
#          (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
#          (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
#          (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
#        (try_end),
#
#        (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
#        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
#        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#        (str_store_string_reg, s8, s0),
#
#        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
#        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#        (str_store_string_reg, s9, s0),
#        (party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),
#
#        (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
#        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
#        (str_store_string_reg, s10, s0),
#        (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),
#
#        (try_begin),
#          (call_script, "script_party_count_members_with_full_health","p_main_party"),
#          (le, reg0, 0),
#          (str_store_string, s4, "str_siege_defender_order_attack_failure"),
#        (else_try),
#          (call_script, "script_party_count_members_with_full_health","p_collective_enemy"),
#          (le, reg0, 0),
#          (assign, "$g_battle_result", 1),
#          (str_store_string, s4, "str_siege_defender_order_attack_success"),
#        (else_try),
#          (str_store_string, s4, "str_siege_defender_order_attack_continue"),
#        (try_end),
#    ],
#    [
#      ("continue",[],"Continue...",[
#          (jump_to_menu,"mnu_siege_started_defender"),
#          ]),
#    ]
#  ),

  (
    "enter_your_own_castle",0,
    "{s10}",
    "none",
    [
      (try_begin),
        (neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_get_slot, ":faction_leader", "fac_player_supporters_faction", slot_faction_leader),
        (eq, ":faction_leader", "trp_player"),
        (str_store_string, s10, "@As you approach, you are spotted by the castle guards, who welcome you and open the gates for their {king/queen}."),
      (else_try),  
        (str_store_string, s10, "@As you approach, you are spotted by the castle guards, who welcome you and open the gates for their {lord/lady}."),
      (try_end),  
      
      (str_store_party_name, s2, "$current_town"),
    ],
    [
      ("continue",[],"Continue...",
       [ (jump_to_menu,"mnu_town"),
        ]),
    ],
  ),

  (
    "village",mnf_enable_hot_keys,
    "{s10} {s12}^{s11}^{s6}{s7}",
    "none",
    [
        (assign, "$current_town", "$g_encountered_party"),
        (call_script, "script_update_center_recon_notes", "$current_town"),

        (assign, "$g_defending_against_siege", 0), #required for bandit check
        (assign, "$g_battle_result", 0),
        (assign, "$qst_collect_taxes_currently_collecting", 0),
        (assign, "$qst_train_peasants_against_bandits_currently_training", 0),

        (try_begin),
          (gt, "$auto_enter_menu_in_center", 0),
          (jump_to_menu, "$auto_enter_menu_in_center"),
          (assign, "$auto_enter_menu_in_center", 0),
        (try_end),

        (try_begin),
          (neq, "$g_player_raiding_village",  "$current_town"),
          (assign, "$g_player_raiding_village", 0),
#        (else_try),
#          (jump_to_menu, "mnu_village_loot_continue"),
        (try_end),

        (try_begin),#Fix for collecting taxes
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
        (try_end),

        (str_store_party_name,s2, "$current_town"),
        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9,":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),

        (str_clear, s10),
        (str_clear, s12),
		
        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (str_store_string, s60, s2),
		  		  
          (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		  (try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg4, ":prosperity",),
			(display_message, "@{!}Prosperity: {reg4}"),
		  (try_end),
		  
		  #(val_add, ":prosperity", 5),
          (store_div, ":str_id", ":prosperity", 10),
		  (val_min, ":str_id", 9),
		  (val_add, ":str_id", "str_village_prosperity_0"),
          (str_store_string, s10, ":str_id"),


          (store_div, ":str_id", ":prosperity", 20),
		  (val_min, ":str_id", 4),
#		  (try_begin),
#			(is_between, "$current_town", "p_village_91", villages_end),
#			(val_add, ":str_id", "str_oasis_village_alt_prosperity_0"),
#		  (else_try),
			(val_add, ":str_id", "str_village_alt_prosperity_0"),
#		  (try_end),
		  
          (str_store_string, s12, ":str_id"),		  		 		  
        (try_end),

        (str_clear, s11),
        (try_begin),
          (party_slot_eq, "$current_town", slot_village_state, svs_looted),
        (else_try),
          (eq, ":center_lord", "trp_player"),
          (str_store_string,s11,"@ This village and the surrounding lands belong to you."),
        (else_try),
          (ge, ":center_lord", 0),
          (str_store_string,s11,"@ You remember that this village and the surrounding lands belong to {s7}."),
        (else_try),
          (str_store_string,s11,"@ These lands belong to no one."),
        (try_end),

        (str_clear, s7),
        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
          (call_script, "script_describe_center_relation_to_s3", ":center_relation"),
          (assign, reg9, ":center_relation"),
          (str_store_string, s7, "@{!} {s3} ({reg9})."),
        (try_end),
        (str_clear, s6),
        (try_begin),
          (party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
          (party_get_slot, ":bandit_troop", "$current_town", slot_village_infested_by_bandits),
          (store_character_level, ":player_level", "trp_player"),
          (store_add, "$qst_eliminate_bandits_infesting_village_num_bandits", ":player_level", 10),
          (val_mul, "$qst_eliminate_bandits_infesting_village_num_bandits", 12),
          (val_div, "$qst_eliminate_bandits_infesting_village_num_bandits", 10),
          (store_random_in_range, "$qst_eliminate_bandits_infesting_village_num_villagers", 25, 30),
          (assign, reg8, "$qst_eliminate_bandits_infesting_village_num_bandits"),
          (str_store_troop_name_by_count, s35, ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
          (str_store_string, s6, "@ The village is infested by {reg8} {s35}."),
          
          (assign, "$g_enemy_party", -1), #new, no known enemy party while saving village from bandits dfdf
          (assign, "$g_ally_party", -1), #new, no known enemy party while saving village from bandits dfdf
          
          (try_begin),
            (eq, ":bandit_troop", "trp_forest_bandit"),
            (set_background_mesh, "mesh_pic_forest_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_steppe_bandit"),
            (set_background_mesh, "mesh_pic_steppe_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_taiga_bandit"),
            (set_background_mesh, "mesh_pic_steppe_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_mountain_bandit"),
            (set_background_mesh, "mesh_pic_mountain_bandits"),
          (else_try),
            (eq, ":bandit_troop", "trp_sea_raider"),
            (set_background_mesh, "mesh_pic_sea_raiders"),
          (else_try),
            (set_background_mesh, "mesh_pic_bandits"),
          (try_end),
        (else_try),
          (party_slot_eq, "$current_town", slot_village_state, svs_looted),
          (str_store_string, s6, "@ The village has been looted. A handful of souls scatter as you pass through the burnt out houses."),
          (try_begin),
            (neq, "$g_player_raid_complete", 1),
            (play_track, "track_empty_village", 1),
          (try_end),
          (set_background_mesh, "mesh_pic_looted_village"),
        (else_try),
          (party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
          (str_store_string, s6, "@ The village is being raided."),
        (else_try),
          (party_get_current_terrain, ":cur_terrain", "$current_town"),
          (try_begin),
            (this_or_next|eq, ":cur_terrain", rt_steppe),
            (this_or_next|eq, ":cur_terrain", rt_steppe_forest),
            (this_or_next|eq, ":cur_terrain", rt_desert),
            (             eq, ":cur_terrain", rt_desert_forest),
            (set_background_mesh, "mesh_pic_village_s"),
          (else_try),
            (this_or_next|eq, ":cur_terrain", rt_snow),
            (             eq, ":cur_terrain", rt_snow_forest),
            (set_background_mesh, "mesh_pic_village_w"),
          (else_try),
            (set_background_mesh, "mesh_pic_village_p"),
          (try_end),
        (try_end),

        (try_begin),
#          (eq, "$g_player_raid_complete", 1),
#          (assign, "$g_player_raid_complete", 0),
#          (jump_to_menu, "mnu_village_loot_complete"),
#        (else_try),
          (party_get_slot, ":raider_party", "$current_town", slot_village_raided_by),
          (gt, ":raider_party", 0),
        # Process here...
        (try_end),

        (try_begin),
          (eq,"$g_leave_town",1),
          (assign,"$g_leave_town",0),
          (change_screen_return),
        (try_end),

        (try_begin), 
          (store_time_of_day, ":cur_hour"),
          (ge, ":cur_hour", 5),
          (lt, ":cur_hour", 21),
          (assign, "$town_nighttime", 0),
        (else_try),
          (assign, "$town_nighttime", 1),
        (try_end),
    ],
    [
      ("village_manage",
      [
        (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
        (neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
        (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player")
        ]
       ,"Manage this village.",
       [
           (assign, "$g_next_menu", "mnu_village"),
           (jump_to_menu, "mnu_center_manage"),
        ]),

#      ("recruit_volunteers",
#      [
#        (call_script, "script_cf_village_recruit_volunteers_cond"),
#       ]
#       ,"Recruit Volunteers.",
#       [
#         (try_begin),
#           (call_script, "script_cf_enter_center_location_bandit_check"),
#         (else_try),
#           (jump_to_menu, "mnu_recruit_volunteers"),
#         (try_end),
#        ]),

      ("village_center",[(neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
                         (neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
                         (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),]
       ,"Go to the village center.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":village_scene", "$current_town", slot_castle_exterior),
           (modify_visitors_at_site,":village_scene"),
           (reset_visitors),
           (party_get_slot, ":village_elder_troop", "$current_town",slot_town_elder),
           (set_visitor, 11, ":village_elder_troop"),

           (call_script, "script_init_town_walkers"),

           (set_jump_mission,"mt_village_center"),
           (jump_to_scene,":village_scene"),
           (change_screen_mission),
         (try_end),
        ],"Door to the village center."),
      ("village_buy_food",[(party_slot_eq, "$current_town", slot_village_state, 0),
                           (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
                           ],"Buy supplies from the peasants.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),

      #(try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
        #(store_sub, ":cur_good_price_slot", ":cur_goods", trade_goods_begin),
        #(val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
		#(party_get_slot, ":cur_price", "$current_town", ":cur_good_price_slot"),
	    #(call_script, "script_center_get_production", "$current_town", ":cur_goods"),
        #(assign, reg13, reg0),
	    #(call_script, "script_center_get_consumption", "$current_town", ":cur_goods"),
        #(str_store_party_name, s1, "$current_town"),
        #(str_store_item_name, s2, ":cur_goods"),
		#(assign, reg16, ":cur_price"),
        #(display_log_message, "@DEBUG:{s1}-{s2}, prd: {reg13}, con: {reg0}, raw: {reg1}, cns: {reg2}, fee: {reg16}"),
	  #(try_end),

           (change_screen_trade, ":merchant_troop"),
         (try_end),
         ]),

      ("village_attack_bandits",[(party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),],
       "Attack the bandits.",
       [(party_get_slot, ":bandit_troop", "$current_town", slot_village_infested_by_bandits),
        (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
        (modify_visitors_at_site,":scene_to_use"),
        (reset_visitors),
        (set_visitors, 0, ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
        (set_visitors, 2, "trp_farmer", "$qst_eliminate_bandits_infesting_village_num_villagers"),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission,"mt_village_attack_bandits"),
        (jump_to_scene, ":scene_to_use"),
#        (assign, "$g_next_menu", "mnu_village_infest_bandits_result"),
#        (jump_to_menu, "mnu_battle_debrief"),
        (assign, "$g_mt_mode", vba_normal),
        (change_screen_mission),
        ]),

      ("village_wait",
       [(party_slot_eq, "$current_town", slot_center_has_manor, 1),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
        ],
         "Wait here for some time.",
         [
           (assign,"$auto_enter_town","$current_town"),
           (assign, "$g_last_rest_center", "$current_town"),

           (try_begin),
             (party_is_active, "p_main_party"),
             (party_get_current_terrain, ":cur_terrain", "p_main_party"),
             (try_begin),
               (eq, ":cur_terrain", rt_desert),
               (unlock_achievement, ACHIEVEMENT_SARRANIDIAN_NIGHTS),
             (try_end),  
           (try_end),  

           (rest_for_hours_interactive, 24 * 7, 5, 1), #rest while attackable

           (change_screen_return),
          ]),
      
      
      ("train_peasants_against_bandits_qst",
       [
         (party_slot_eq, "$current_town", slot_village_state, 0),
         (check_quest_active, "qst_train_peasants_against_bandits"),
         (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
         (quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_center, "$current_town"),
         ], "Train the peasants.",
       [(jump_to_menu, "mnu_train_peasants_against_bandits"),]),

#      ("village_hostile_action",[(party_slot_eq, "$current_town", slot_village_state, 0),
#                                 (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
#								 (neq, "$players_kingdom", "$g_encountered_party_faction"),
#								 ], "Take a hostile action.",
#       [(jump_to_menu,"mnu_village_hostile_action"),
#           ]),
      
      ("village_reports",[(eq, "$cheat_mode", 1),], "{!}CHEAT! Show reports.",
       [(jump_to_menu,"mnu_center_reports"),
           ]),
      ("village_leave",[],"Leave...",[(change_screen_return,0)]),
      
    ],
  ),

  (
    "village_hostile_action",0,
    "What action do you have in mind?",
    "none",
    [],
    [
#      ("village_take_food",[
#          (party_slot_eq, "$current_town", slot_village_state, 0),
#          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
#          (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
#          (assign, ":town_stores_not_empty", 0),
#          (try_for_range, ":slot_no", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
#            (troop_get_inventory_slot, ":slot_item", ":merchant_troop", ":slot_no"),
#            (ge, ":slot_item", 0),
#            (assign, ":town_stores_not_empty", 1),
#          (try_end),
#          (eq, ":town_stores_not_empty", 1),
#          ],"Force the peasants to give you supplies.",
#       [
#           (jump_to_menu, "mnu_village_take_food_confirm")
#        ]),
#      ("village_steal_cattle",
#       [
#          (party_slot_eq, "$current_town", slot_village_state, 0),
#          (party_slot_eq, "$current_town", slot_village_player_can_not_steal_cattle, 0),
#          (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
#          (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
#          (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
#          (gt, ":num_cattle", 0),
#          ],"Steal cattle.",
#       [
#           (jump_to_menu, "mnu_village_steal_cattle_confirm")
#        ]),
#      ("village_loot",[(party_slot_eq, "$current_town", slot_village_state, 0),
#                       (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
#                       (store_faction_of_party, ":center_faction", "$current_town"),
#                       (store_relation, ":reln", "fac_player_supporters_faction", ":center_faction"),
#                       (lt, ":reln", 0),
#                       ],
#       "Loot and burn this village.",
#       [
##           (party_clear, "$current_town"),
##           (party_add_template, "$current_town", "pt_villagers_in_raid"),
#           (jump_to_menu, "mnu_village_start_attack"),
#           ]),
      ("forget_it",[],
      "Forget it.",[(jump_to_menu,"mnu_village")]),
    ],
  ),
  
  (
    "recruit_volunteers",0,
    "{s18}",
    "none",
    [(party_get_slot, ":volunteer_troop", "$current_town", slot_center_volunteer_troop_type),
     (party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
     (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
     (store_troop_gold, ":gold", "trp_player"),
     (store_div, ":gold_capacity", ":gold", 10),#10 denars per man
     (assign, ":party_capacity", ":free_capacity"),
     (val_min, ":party_capacity", ":gold_capacity"),
     (try_begin),
       (gt, ":party_capacity", 0),
       (val_min, ":volunteer_amount", ":party_capacity"),
     (try_end),
     (assign, reg5, ":volunteer_amount"),
     (assign, reg7, 0),
     (try_begin),
       (gt, ":volunteer_amount", ":gold_capacity"),
       (assign, reg7, 1), #not enough money
     (try_end),
     (try_begin),
       (eq, ":volunteer_amount", 0),
       (str_store_string, s18, "@No one here seems to be willing to join your party."),
     (else_try),
       (store_mul, reg6, ":volunteer_amount", 10),#10 denars per man
       (str_store_troop_name_by_count, s3, ":volunteer_troop", ":volunteer_amount"),
       (try_begin),
         (eq, reg5, 1),
         (str_store_string, s18, "@One {s3} volunteers to follow you."),
       (else_try),
         (str_store_string, s18, "@{reg5} {s3} volunteer to follow you."),
       (try_end),
       (set_background_mesh, "mesh_pic_recruits"),
     (try_end),
    ],
    [
      ("continue_not_enough_gold",
      [
        (eq, reg7, 1),
      ],
      "I don't have enough money...",
      [
        (jump_to_menu,"mnu_village"),
      ]),
       
      ("continue",
      [
        (eq, reg7, 0),
        (eq, reg5, 0),
      ], #noone willing to join                   
      "Continue...",
      [
        (party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
        (jump_to_menu,"mnu_village"),
      ]),
       
#      ("recruit_them",
#      [
#        (eq, reg7, 0),
#        (gt, reg5, 0),
#      ],
#      "Recruit them ({reg6} denars).",
#      [
#        (call_script, "script_village_recruit_volunteers_recruit"),
#                        
#        (jump_to_menu,"mnu_village"),
#      ]),
      
      ("forget_it",
      [
        (eq, reg7, 0),
        (gt, reg5, 0),
      ],
      "Forget it.",
      [
        (jump_to_menu,"mnu_village"),
      ]),
    ],
  ),

  (
    "village_infestation_removed",mnf_disable_all_keys,
    "In a battle worthy of song, you and your men drive the bandits out of the village, making it safe once more.\
 The villagers have little left in the way of wealth after their ordeal,\
 but they offer you all they can find.",
    "none",
    [(party_get_slot, ":bandit_troop", "$g_encountered_party", slot_village_infested_by_bandits),
     (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
     (party_clear, "p_temp_party"),
     (party_add_members, "p_temp_party", ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
     (assign, "$g_strength_contribution_of_player", 50),
     (call_script, "script_party_give_xp_and_gold", "p_temp_party"),
     (try_begin),
       (check_quest_active, "qst_eliminate_bandits_infesting_village"),
       (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
       (call_script, "script_end_quest", "qst_eliminate_bandits_infesting_village"),
       #Add quest reward
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 5),
     (else_try),
     #Add normal reward
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 4),
     (try_end),
   
     (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
     (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 70),
        (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
     (try_end),
    ],
    [
      ("village_bandits_defeated_accept",[],"Take it as your just due.",[(jump_to_menu, "mnu_village"),
                                                                         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
                                                                         (troop_sort_inventory, ":merchant_troop"),
                                                                         (change_screen_loot, ":merchant_troop"),
                                                                       ]),
																	   
      ("village_bandits_defeated_cont",[],  "Refuse, stating that they need these items more than you do.",
	  [	(call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
		(call_script, "script_change_player_honor", 1),	  
		(jump_to_menu, "mnu_village")]),
    ],
  ),

  (
    "center_manage",0,
    "{s19}^{reg6?^^You are\
 currently building {s7}. The building will be completed after {reg8} day{reg9?s:}.:}",
    "none",
    [(assign, ":num_improvements", 0),
     (str_clear, s18),
     (try_begin),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
       (assign, ":begin", village_improvements_begin),
       (assign, ":end", village_improvements_end),
       (str_store_string, s17, "@village"),
     (else_try),
       (assign, ":begin", walled_center_improvements_begin),
       (assign, ":end", walled_center_improvements_end),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
       (str_store_string, s17, "@town"),
     (else_try),
       (str_store_string, s17, "@castle"),
     (try_end),
     
     (try_for_range, ":improvement_no", ":begin", ":end"),
       (party_slot_ge, "$g_encountered_party", ":improvement_no", 1),
       (val_add,  ":num_improvements", 1),
       (call_script, "script_get_improvement_details", ":improvement_no"),
       (try_begin),
         (eq,  ":num_improvements", 1),
         (str_store_string, s18, "@{!}{s0}"),
       (else_try),
         (str_store_string, s18, "@{!}{s18}, {s0}"),
       (try_end),
     (try_end),
     
     (try_begin),
       (eq,  ":num_improvements", 0),
       (str_store_string, s19, "@The {s17} has no improvements."),
     (else_try),
       (str_store_string, s19, "@The {s17} has the following improvements:{s18}."),
     (try_end),
     
     (assign, reg6, 0),
     (try_begin),
       (party_get_slot, ":cur_improvement", "$g_encountered_party", slot_center_current_improvement),
       (gt, ":cur_improvement", 0),
       (call_script, "script_get_improvement_details", ":cur_improvement"),
       (str_store_string, s7, s0),
       (assign, reg6, 1),
       (store_current_hours, ":cur_hours"),
       (party_get_slot, ":finish_time", "$g_encountered_party", slot_center_improvement_end_hour),
       (val_sub, ":finish_time", ":cur_hours"),
       (store_div, reg8, ":finish_time", 24),
       (val_max, reg8, 1),
       (store_sub, reg9, reg8, 1),
     (try_end),
    ],
    [
      ("center_build_manor",[(eq, reg6, 0),
                             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                             (party_slot_eq, "$g_encountered_party", slot_center_has_manor, 0),
                                  ],
       "Build a manor.",[(assign, "$g_improvement_type", slot_center_has_manor),
                         (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_fish_pond",[(eq, reg6, 0),
                                 (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                 (party_slot_eq, "$g_encountered_party", slot_center_has_fish_pond, 0),
                                  ],
       "Build a mill.",[(assign, "$g_improvement_type", slot_center_has_fish_pond),
                             (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_watch_tower",[(eq, reg6, 0),
                                   (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                                   (party_slot_eq, "$g_encountered_party", slot_center_has_watch_tower, 0),
                                  ],
       "Build a watch tower.",[(assign, "$g_improvement_type", slot_center_has_watch_tower),
                               (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_school",[(eq, reg6, 0),
                              (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
                              (party_slot_eq, "$g_encountered_party", slot_center_has_school, 0),
                                  ],
       "Build a school.",[(assign, "$g_improvement_type", slot_center_has_school),
                          (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_messenger_post",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_messenger_post, 0),
                                       ],
       "Build a messenger post.",[(assign, "$g_improvement_type", slot_center_has_messenger_post),
                                  (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_prisoner_tower",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_prisoner_tower, 0),
                                       ],
       "Build a prisoner tower.",[(assign, "$g_improvement_type", slot_center_has_prisoner_tower),
                                  (jump_to_menu, "mnu_center_improve"),]),
                           
      ("go_back_dot",[],"Go back.",[(jump_to_menu, "$g_next_menu")]),
    ],
  ),

  (
    "center_improve",0,
    "{s19} As the party member with the highest engineer skill ({reg2}), {reg3?you reckon:{s3} reckons} that building the {s4} will cost you\
 {reg5} denars and will take {reg6} days.",
    "none",
    [(call_script, "script_get_improvement_details", "$g_improvement_type"),
     (assign, ":improvement_cost", reg0),
     (str_store_string, s4, s0),
     (str_store_string, s19, s1),
     (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),

     (store_sub, ":multiplier", 20, ":max_skill"),
     (val_mul, ":improvement_cost", ":multiplier"),
     (val_div, ":improvement_cost", 20),
     
     (store_div, ":improvement_time", ":improvement_cost", 100),
     (val_add, ":improvement_time", 3),

     (assign, reg5, ":improvement_cost"),
     (assign, reg6, ":improvement_time"),

     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
    ],
    [
      ("improve_cont",[(store_troop_gold, ":cur_gold", "trp_player"),
                       (ge, ":cur_gold", reg5)],
       "Go on.", [(troop_remove_gold, "trp_player", reg5),
                  (party_set_slot, "$g_encountered_party", slot_center_current_improvement, "$g_improvement_type"),
                  (store_current_hours, ":cur_hours"),
                  (store_mul, ":hours_takes", reg6, 24),
                  (val_add, ":hours_takes", ":cur_hours"),
                  (party_set_slot, "$g_encountered_party", slot_center_improvement_end_hour, ":hours_takes"),
                  (jump_to_menu,"mnu_center_manage"),
                  ]),
      ("forget_it",[(store_troop_gold, ":cur_gold", "trp_player"),
                    (ge, ":cur_gold", reg5)],
       "Forget it.", [(jump_to_menu,"mnu_center_manage")]),
      ("improve_not_enough_gold",[(store_troop_gold, ":cur_gold", "trp_player"),
                                  (lt, ":cur_gold", reg5)],
       "I don't have enough money for that.", [(jump_to_menu, "mnu_center_manage"),]),
    ],
  ),

  (
    "town_bandits_failed",mnf_disable_all_keys,
    "{s4} {s5}",
    "none",
    [
#      (call_script, "script_loot_player_items", 0),
      (store_troop_gold, ":total_gold", "trp_player"),
      (store_div, ":gold_loss", ":total_gold", 30),
      (store_random_in_range, ":random_loss", 40, 100),
      (val_add, ":gold_loss", ":random_loss"),
      (val_min, ":gold_loss", ":total_gold"),
      (troop_remove_gold, "trp_player",":gold_loss"),
      (party_set_slot, "$current_town", slot_center_has_bandits, 0),
      (party_get_num_companions, ":num_companions", "p_main_party"),
      (str_store_string, s4, "@The assasins beat you down and leave you for dead. ."),
      (str_store_string, s4, "@You have fallen. The bandits quickly search your body for every coin they can find,\
 then vanish into the night. They have left you alive, if only barely."),
      (try_begin),
        (gt, ":num_companions", 2),
        (str_store_string, s5, "@Luckily some of your companions come to search for you when you do not return, and find you lying by the side of the road. They hurry you to safety and dress your wounds."),
      (else_try),
        (str_store_string, s5, "@Luckily some passing townspeople find you lying by the side of the road, and recognise you as something other than a simple beggar. They carry you to the nearest inn and dress your wounds."),
      (try_end),
    ],
    [
      ("continue",[],"Continue...",[(change_screen_return)]),
    ],
  ),

  (
    "town_bandits_succeeded",mnf_disable_all_keys,
    "The bandits fall before you as wheat to a scythe! Soon you stand alone in the streets\
 while most of your attackers lie unconscious, dead or dying.\
 Searching the bodies, you find a purse which must have belonged to a previous victim of these brutes.\
 Or perhaps, it was given to them by someone who wanted to arrange a suitable ending to your life.",
    "none",
    [
      (party_set_slot, "$current_town", slot_center_has_bandits, 0),
      (assign, "$g_last_defeated_bandits_town", "$g_encountered_party"),
      (store_mul, ":xp_reward", "$num_center_bandits", 117),
      (add_xp_to_troop, ":xp_reward", "trp_player"),
      (store_mul, ":gold_reward", "$num_center_bandits", 50),
      (call_script, "script_troop_add_gold","trp_player",":gold_reward"),
    ],
    [
      ("continue",[],"Continue...",[(change_screen_return)]),
    ],
  ),

  
#   (
#    "village_steal_cattle_confirm",0,
#    "As the party member with the highest looting skill ({reg2}), {reg3?you reckon:{s1} reckons} that you can steal as many as {reg4} heads of village's cattle.",
#    "none",
#    [
#      (call_script, "script_get_max_skill_of_player_party", "skl_looting"),
#      (assign, reg2, reg0),
#      (assign, ":max_skill_owner", reg1),
#      (try_begin),
#        (eq, ":max_skill_owner", "trp_player"),
#        (assign, reg3, 1),
#      (else_try),
#        (assign, reg3, 0),
#        (str_store_troop_name, s1, ":max_skill_owner"),
#      (try_end),
#      (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
#      (assign, reg4, reg0),
#      ],
#    [
#      ("village_steal_cattle_confirm",[],"Go on.",
#       [
#         (rest_for_hours_interactive, 3, 5, 1), #rest while attackable
#         (assign, "$auto_menu", "mnu_village_steal_cattle"),
#         (change_screen_return),
#       ]),
#      ("forget_it",[],"Forget it.",[(change_screen_return)]),
#    ],
#  ),
#
#  (
#    "village_steal_cattle",mnf_disable_all_keys,
#    "{s1}",
#    "none",
#    [
#      (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
#      (assign, ":max_value", reg0),
#      (val_add, ":max_value", 1),
#      (store_random_in_range, ":random_value", 0, ":max_value"),
#      (party_set_slot, "$current_town", slot_village_player_can_not_steal_cattle, 1),
#      (party_get_slot, ":lord", "$current_town", slot_town_lord),
#      (try_begin),
#        (le, ":random_value", 0),
#        (call_script, "script_change_player_relation_with_center", "$current_town", -3),
#        (str_store_string, s1, "@You fail to steal any cattle."),
#      (else_try),
#        (assign, reg17, ":random_value"),
#        (store_sub, reg12, ":random_value", 1),
#        (try_begin),
#          (gt, ":lord", 0),
#          (call_script, "script_change_player_relation_with_troop", ":lord", -3),
#          (call_script, "script_add_log_entry", logent_player_stole_cattles_from_village, "trp_player",  "$current_town", ":lord", "$g_encountered_party_faction"),
#        (try_end),
#        (call_script, "script_change_player_relation_with_center", "$current_town", -5),
#        (str_store_string, s1, "@You drive away {reg17} {reg12?heads:head} of cattle from the village's herd."),
#        
#        (try_begin),
#          (eq, ":random_value", 3),
#          (unlock_achievement, ACHIEVEMENT_GOT_MILK),
#        (try_end),
#        
#        (call_script, "script_create_cattle_herd", "$current_town", ":random_value"),
#        (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
#        (val_sub, ":num_cattle", ":random_value"),
#        (party_set_slot, "$current_town", slot_village_number_of_cattle, ":num_cattle"),
#      (try_end),
#    ],
#    [
#      ("continue",[],"Continue...",
#       [
#         (change_screen_return),
#         ]),
#    ],
#  ),
#  
#
#   (
#    "village_take_food_confirm",0,
#    "It will be difficult to force and threaten the peasants into giving their precious supplies. You think you will need at least one hour.",
#    #TODO: mention looting skill?
#    "none",
#    [],
#    [
#      ("village_take_food_confirm",[],"Go ahead.",
#       [
#         (rest_for_hours_interactive, 1, 5, 0), #rest while not attackable
#         (assign, "$auto_enter_town", "$current_town"),
#         (assign, "$g_town_visit_after_rest", 1),
#         (assign, "$auto_enter_menu_in_center", "mnu_village_take_food"),
#         (change_screen_return),
#         ]),
#      ("forget_it",[],"Forget it.",[(jump_to_menu, "mnu_village_hostile_action")]),
#    ],
#  ),
#
#  (
#    "village_take_food",0,
#    "The villagers grudgingly bring out what they have for you.",
#    "none",
#    [
#       (call_script, "script_party_count_members_with_full_health","p_main_party"),
#       (assign, ":player_party_size", reg0),
#       (call_script, "script_party_count_members_with_full_health","$current_town"),
#       (assign, ":villagers_party_size", reg0),
#       (try_begin),
#         (lt, ":player_party_size", 6),
#         (ge, ":villagers_party_size", 40),
#         (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
#         (jump_to_menu, "mnu_village_start_attack"),
#       (try_end),
#    ],
#    [
#      ("take_supplies",[],"Take the supplies.",
#       [
#         (try_begin),
#           (party_slot_ge, "$current_town", slot_center_player_relation, -55),
#           (try_begin),
#             (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
#             (call_script, "script_change_player_relation_with_center", "$current_town", -1),
#           (else_try),
#             (call_script, "script_change_player_relation_with_center", "$current_town", -3),
#           (try_end),
#         (try_end),
#         (party_get_slot, ":village_lord", "$current_town", slot_town_lord),
#         (try_begin),
#           (gt,  ":village_lord", 1),
#          (call_script, "script_change_player_relation_with_troop", ":village_lord", -1),
#          (try_end),
#         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
#         (party_get_skill_level, ":player_party_looting", "p_main_party", "skl_looting"),
#         (val_mul, ":player_party_looting", 3),
#         (store_sub, ":random_chance", 70, ":player_party_looting"), #Increases the chance of looting by 3% per skill level
#         (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
#           (store_random_in_range, ":rand", 0, 100), 
#           (lt, ":rand", ":random_chance"),
#           (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
#         (try_end),
#
####NPC companion changes begin
#         (call_script, "script_objectionable_action", tmt_humanitarian, "str_steal_from_villagers"),
##NPC companion changes end
##Troop commentary changes begin
#          (call_script, "script_add_log_entry", logent_village_extorted, "trp_player",  "$current_town", -1, -1),
#          (store_faction_of_party,":village_faction",  "$current_town"),
#		  (call_script, "script_faction_inflict_war_damage_on_faction", "$players_kingdom", ":village_faction", 5),
##Troop commentary changes end          
#
#         (jump_to_menu, "mnu_village"),
#         (troop_sort_inventory, ":merchant_troop"),
#         (change_screen_loot, ":merchant_troop"),       
#         ]),
#      ("let_them_keep_it",[],"Let them keep it.",[(jump_to_menu, "mnu_village")]),
#    ],
#  ),
#
#
#  (
#    "village_start_attack",mnf_disable_all_keys|mnf_scale_picture,
#    "Some of the angry villagers grab their tools and prepare to resist you.\
# It looks like you'll have a fight on your hands if you continue.",
#    "none",
#    [
#       (set_background_mesh, "mesh_pic_villageriot"),
#       (call_script, "script_party_count_members_with_full_health","p_main_party"),
#       (assign, ":player_party_size", reg0),
#       (call_script, "script_party_count_members_with_full_health","$current_town"),
#       (assign, ":villagers_party_size", reg0),
#       
#       (try_begin),
#         (gt, ":player_party_size", 25),
#         (jump_to_menu, "mnu_village_loot_no_resist"),
#       (else_try),
#         (this_or_next|eq, ":villagers_party_size", 0),
#         (eq, "$g_battle_result", 1),
#         (try_begin),
#           (eq, "$g_battle_result", 1),
#           (store_random_in_range, ":enmity", -30, -15),
#           (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
#           (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
#           (gt, ":town_lord", 0),
#           (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
#         (try_end),
#         (jump_to_menu, "mnu_village_loot_no_resist"),
#       (else_try),
#         (eq, "$g_battle_result", -1),
#         (jump_to_menu, "mnu_village_loot_defeat"),
#       (try_end),
#    ],
#    [
#      ("village_raid_attack",[],"Charge them.",[
#          (store_random_in_range, ":enmity", -10, -5),
#          (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
#          (try_begin),
#            (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
#            (gt, ":town_lord", 0),
#            (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
#          (try_end),
#          (call_script, "script_calculate_battle_advantage"),
#          (set_battle_advantage, reg0),
#          (set_party_battle_mode),
#          (assign, "$g_battle_result", 0),
#          (assign, "$g_village_raid_evil", 1),
#          (set_jump_mission,"mt_village_raid"),
#          (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
#          (jump_to_scene, ":scene_to_use"),
#          (assign, "$g_next_menu", "mnu_village_start_attack"),
#
#		  (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
####NPC companion changes begin
#          (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
##NPC companion changes end
#
#          (jump_to_menu, "mnu_battle_debrief"),
#          (change_screen_mission),
#          ]),
#      ("village_raid_leave",[],"Leave this village alone.",[(change_screen_return)]),
#    ],
#  ),
#  
#  (
#    "village_loot_no_resist",0,
#    "The villagers here are few and frightened, and they quickly scatter and run before you.\
# The village is at your mercy.",
#    "none",
#    [],
#    [
#      ("village_loot",[], "Plunder the village, then raze it.",
#       [
#          (call_script, "script_village_set_state", "$current_town", svs_being_raided),
#          (party_set_slot, "$current_town", slot_village_raided_by, "p_main_party"),
#          (assign,"$g_player_raiding_village","$current_town"),
#		  
#		  (try_begin),
#		    (store_faction_of_party, ":village_faction", "$current_town"),
#			(store_relation, ":relation", "$players_kingdom", ":village_faction"),
#			(ge, ":relation", 0),
#			(call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$current_town"),
#		  (try_end),	
#		  
#          (rest_for_hours, 3, 5, 1), #rest while attackable (3 hours will be extended by the trigger)
#          (change_screen_return),
#           ]),
#      ("village_raid_leave",[],"Leave this village alone.",[(change_screen_return)]),
#    ],
#  ),
#  (
#    "village_loot_complete",mnf_disable_all_keys,
#    "On your orders your troops sack the village, pillaging everything of any value,\
# and then put the buildings to the torch. From the coins and valuables that are found, you get your share of {reg1} denars.",
#    "none",
#    [
#        (get_achievement_stat, ":number_of_village_raids", ACHIEVEMENT_THE_BANDIT, 0),
#        (get_achievement_stat, ":number_of_caravan_raids", ACHIEVEMENT_THE_BANDIT, 1),
#        (val_add, ":number_of_village_raids", 1),
#        (set_achievement_stat, ACHIEVEMENT_THE_BANDIT, 0, ":number_of_village_raids"),
#                
#        (try_begin),
#          (ge, ":number_of_village_raids", 3),
#          (ge, ":number_of_caravan_raids", 3),
#          (unlock_achievement, ACHIEVEMENT_THE_BANDIT),
#        (try_end),
#    
#        (party_get_slot, ":village_lord", "$current_town", slot_town_lord),
#        (try_begin),
#          (gt,  ":village_lord", 0),
#          (call_script, "script_change_player_relation_with_troop", ":village_lord", -5),
#        (try_end),
#        (store_random_in_range, ":enmity", -35, -25),
#        (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
#
#        (store_faction_of_party, ":village_faction", "$current_town"),
#        (store_relation, ":relation", ":village_faction", "fac_player_supporters_faction"),
#        (try_begin),
#          (lt, ":relation", 0),
#          (call_script, "script_change_player_relation_with_faction", ":village_faction", -3),
#        (try_end),
#                
#        (assign, ":money_gained", 50),
#        (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
#        (store_mul, ":prosperity_of_village_mul_5", ":prosperity", 5),
#        (val_add, ":money_gained", ":prosperity_of_village_mul_5"),
#        (call_script, "script_troop_add_gold", "trp_player", ":money_gained"),
#		
#        (assign, ":morale_increase", 3),
#        (store_div, ":money_gained_div_100", ":money_gained", 100),
#        (val_add, ":morale_increase", ":money_gained_div_100"),
#        (call_script, "script_change_player_party_morale", ":morale_increase"),
#        
#                
#        (faction_get_slot, ":faction_morale", ":village_faction",  slot_faction_morale_of_player_troops),
#        (store_mul, ":morale_increase_mul_2", ":morale_increase", 200),
#        (val_sub, ":faction_morale", ":morale_increase_mul_2"),           
#        (faction_set_slot, ":village_faction",  slot_faction_morale_of_player_troops, ":faction_morale"),
#        
#
#		
##NPC companion changes begin
#        (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
##NPC companion changes end
#        (assign, reg1, ":money_gained"),
#      ],
#    [
#      ("continue",[], "Continue...",
#       [
#          (jump_to_menu, "mnu_close"),
#          (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
#          (assign, ":max_cattle", reg0),
#          (val_mul, ":max_cattle", 3),
#          (val_div, ":max_cattle", 2),
#          (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
#          (val_min, ":max_cattle", ":num_cattle"),
#          (val_add, ":max_cattle", 1),
#          (store_random_in_range, ":random_value", 0, ":max_cattle"),
#          (try_begin),
#            (gt, ":random_value", 0),
#            (call_script, "script_create_cattle_herd", "$current_town", ":random_value"),
#            (val_sub, ":num_cattle", ":random_value"),
#            (party_set_slot, "$current_town", slot_village_number_of_cattle, ":num_cattle"),
#          (try_end),
#          (troop_clear_inventory, "trp_temp_troop"),
#
#		  #below line changed with below lines to make plunder result more realistic. Now only items produced in bound town can be stolen after raid.
#          #(reset_item_probabilities,100),
#
#		  #begin of changes
#		  (party_get_slot, ":bound_town", slot_village_bound_center, "$current_town"),
#          (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
#          (reset_item_probabilities,100),
#          (assign, ":total_probability", 0),
#          (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
#            (store_add, ":cur_price_slot", ":cur_goods", ":item_to_price_slot"),
#            (party_get_slot, ":cur_price", ":bound_town", ":cur_price_slot"),
#            (call_script, "script_center_get_production", ":bound_town", ":cur_goods"),
#            (assign, ":cur_probability", reg0),
#            (call_script, "script_center_get_consumption", ":bound_town", ":cur_goods"),
#            (val_div, reg0, 3),
#            (val_add, ":cur_probability", reg0),
#            (val_mul, ":cur_probability", 4),
#            (val_mul, ":cur_probability", average_price_factor),
#            (val_div, ":cur_probability", ":cur_price"),
#			#first only simulation
#            #(set_item_probability_in_merchandise,":cur_goods",":cur_probability"),						  
#			(val_add, ":total_probability", ":cur_probability"),
#          (try_end),
#
#          (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
#            (store_add, ":cur_price_slot", ":cur_goods", ":item_to_price_slot"),
#            (party_get_slot, ":cur_price", ":bound_town", ":cur_price_slot"),
#            (call_script, "script_center_get_production", ":bound_town", ":cur_goods"),
#            (assign, ":cur_probability", reg0),
#            (call_script, "script_center_get_consumption", ":bound_town", ":cur_goods"),
#            (val_div, reg0, 3),
#            (val_add, ":cur_probability", reg0),
#            (val_mul, ":cur_probability", 4),
#            (val_mul, ":cur_probability", average_price_factor),
#            (val_div, ":cur_probability", ":cur_price"),
#
#			(val_mul, ":cur_probability", num_merchandise_goods),
#			(val_mul, ":cur_probability", 100),
#			(val_div, ":cur_probability", ":total_probability"),
#
#            (set_item_probability_in_merchandise,":cur_goods",":cur_probability"),						  
#          (try_end),
#		  #end of changes
#
#          (troop_add_merchandise,"trp_temp_troop",itp_type_goods,30),
#          (troop_sort_inventory, "trp_temp_troop"),
#          (change_screen_loot, "trp_temp_troop"),
#        ]),
#    ],
#  ),
#  (
#    "village_loot_defeat",mnf_scale_picture,
#    "Fighting with courage and determination, the villagers manage to hold together and drive off your forces.",
#    "none",
#    [
#        (set_background_mesh, "mesh_pic_villageriot"),
#	],
#    [
#      ("continue",[],"Continue...",[(change_screen_return)]),
#    ],
#  ),
#  
#  (
#    "village_loot_continue",0,
#    "Do you wish to continue looting this village?",
#    "none",
#    [],
#    [
#      ("disembark_yes",[],"Yes.",[ (rest_for_hours, 3, 5, 1), #rest while attackable (3 hours will be extended by the trigger)
#                              (change_screen_return),
#                              ]),
#      ("disembark_no",[],"No.",[(call_script, "script_village_set_state", "$current_town", 0),
#                            (party_set_slot, "$current_town", slot_village_raided_by, -1),
#                            (assign, "$g_player_raiding_village", 0),
#                            (change_screen_return)]),
#    ],
#  ),
  
  (
    "close",0,
    "Nothing.",
    "none",
    [
        (change_screen_return),
      ],
    [],
  ),
 
  (
    "town",mnf_enable_hot_keys|mnf_scale_picture,
    "{s10} {s14}^{s11}{s12}{s13}",
    "none",
    [    
        (try_begin),
          (eq, "$sneaked_into_town", 1),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
        (try_end),
        (store_encountered_party, "$current_town"),
        (call_script, "script_update_center_recon_notes", "$current_town"),
        (assign, "$g_defending_against_siege", 0),
        (str_clear, s3),
        (party_get_battle_opponent, ":besieger_party", "$current_town"),
        (store_faction_of_party, ":encountered_faction", "$g_encountered_party"),
        (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
        (try_begin),
          (gt, ":besieger_party", 0),
          (ge, ":faction_relation", 0),
          (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
          (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
          (lt, ":besieger_party_relation", 0),
          (assign, "$g_defending_against_siege", 1),
          (assign, "$g_siege_first_encounter", 1),
#          (jump_to_menu, "mnu_siege_started_defender"),
        (try_end),
        
        (try_begin),
          (is_between, "$g_encountered_party", towns_begin, towns_end),
          (store_sub, ":encountered_town_no", "$g_encountered_party", towns_begin),
          (set_achievement_stat, ACHIEVEMENT_MIGRATING_COCONUTS, ":encountered_town_no", 1),

          (assign, ":there_are_villages_not_visited", 0),
          (try_for_range, ":cur_town", towns_begin, towns_end),
            (store_sub, ":encountered_town_no", ":cur_town", towns_begin),
            (get_achievement_stat, ":town_is_visited", ACHIEVEMENT_MIGRATING_COCONUTS, ":encountered_town_no"),
            (eq, ":town_is_visited", 0),
            (assign, ":there_are_villages_not_visited", 1),
          (try_end),
          
          (try_begin),
            (eq, ":there_are_villages_not_visited", 0),
            (unlock_achievement, ACHIEVEMENT_MIGRATING_COCONUTS),
          (try_end),
        (try_end),  

        #Quest menus
        
        (assign, "$qst_collect_taxes_currently_collecting", 0),
        
        (try_begin),
          (gt, "$quest_auto_menu", 0),
          (jump_to_menu, "$quest_auto_menu"),
          (assign, "$quest_auto_menu", 0),
        (try_end),

        (try_begin),
##          (eq, "$g_center_under_siege_battle", 1),
##          (jump_to_menu,"mnu_siege_started_defender"),
##        (else_try),
          (eq, "$g_town_assess_trade_goods_after_rest", 1),
          (assign, "$g_town_assess_trade_goods_after_rest", 0),
          (jump_to_menu,"mnu_town_trade_assessment"),
        (try_end),

        (assign, "$talk_context", 0),
        (assign,"$all_doors_locked",0),

        (try_begin),
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
          (assign, "$town_entered", 1),
        (try_end),

        (try_begin),
          (eq,"$g_leave_town",1),
          (assign,"$g_leave_town",0),
          (assign,"$g_permitted_to_center",0),
          (leave_encounter),
          (change_screen_return),
        (try_end),
        
        (str_store_party_name, s2, "$current_town"),
        (party_get_slot, ":center_lord", "$current_town", slot_town_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name, s9, ":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),
        
        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_town),

          (str_store_string, s60, s2),
		  
		  (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
		  (try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg4, ":prosperity",),
			(display_message, "@{!}DEBUG -- Prosperity: {reg4}"),
		  (try_end),

	 #          (val_add, ":prosperity", 5),
          (store_div, ":str_id", ":prosperity", 10),
		  (val_min, ":str_id", 9),
		  (val_add, ":str_id", "str_town_prosperity_0"),
          (str_store_string, s10, ":str_id"),

          (store_div, ":str_id", ":prosperity", 20),
		  (val_min, ":str_id", 4),
		  (val_add, ":str_id", "str_town_alt_prosperity_0"),
		  
          (str_store_string, s14, ":str_id"),

		  
        (else_try),
		  (str_clear, s14),
          (str_store_string,s10,"@You are at {s2}."),
        (try_end),
        
        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_castle),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the castle gate."),
		  (else_try),
			(gt, ":center_lord", -1),
			(troop_slot_eq, ":center_lord", slot_troop_spouse, "trp_player"),
            (str_store_string,s11,"str__you_see_the_banner_of_your_wifehusband_s7_over_the_castle_gate"),
		  (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the castle gate."),
          (else_try),
##            (str_store_string,s11,"@ This castle seems to belong to no one."),
            (str_store_string,s11,"@ This castle has no garrison."),
          (try_end),
        (else_try),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the town gates."),
		  (else_try),	
			(gt, ":center_lord", -1),
			(troop_slot_eq, ":center_lord", slot_troop_spouse, "trp_player"),
            (str_store_string,s11,"str__the_banner_of_your_wifehusband_s7_flies_over_the_town_gates"),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the town gates."),
          (else_try),
##            (str_store_string,s11,"@ The townsfolk here have declared their independence."),
            (str_store_string,s11,"@ This town has no garrison."),
          (try_end),
        (try_end),

        (str_clear, s12),
        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
          (call_script, "script_describe_center_relation_to_s3", ":center_relation"),
          (assign, reg9, ":center_relation"),
          (str_store_string, s12, "@{!} {s3} ({reg9})."),
        (try_end),

        (str_clear, s13),
        (try_begin), 
          (gt,"$entry_to_town_forbidden",0),
          (str_store_string, s13, "@ You have successfully sneaked in."),
		(else_try),  
		  (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
		  (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),
		  
          (str_store_string, s13, "str__the_lord_is_currently_holding_a_feast_in_his_hall"),
        (try_end),

        #forbidden to enter?
        (try_begin), 
          (store_time_of_day,reg(12)),
          (ge,reg(12),5),
          (lt,reg(12),21),
          (assign,"$town_nighttime",0),
        (else_try),
          (assign,"$town_nighttime",1),
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (str_store_string, s13, "str_town_nighttime"),
        (try_end),

        (try_begin),
          (party_slot_ge, "$current_town", slot_town_has_tournament, 1),
          (neg|is_currently_night),
          (party_set_slot, "$current_town", slot_town_has_tournament, 1),
          (str_store_string, s13, "@{s13} A tournament will be held here soon."),
        (try_end),

        (assign,"$castle_undefended",0),
        (party_get_num_companions, ":castle_garrison_size", "p_collective_enemy"),
        (try_begin),
          (eq,":castle_garrison_size",0),
          (assign,"$castle_undefended",1),
        (try_end),

		(call_script, "script_set_town_picture"),
		
#		(str_clear, s5), #alert player that there are new rumors
#		(try_begin),
#			(eq, 1, 0),
#			(neg|is_currently_night),
#			(str_store_string, s5, "@^The buzz of excited voices as you come near the gate suggests to you that news of some import is circulating among the townsfolk."),
#			(lt, "$last_town_log_entry_checked", "$num_log_entries"),
#			(assign, "$g_town_rumor_log_entry", 0),
#			(try_for_range, ":log_entry", "$last_town_log_entry_checked", "$num_log_entries"),
#				(eq, ":log_entry", 4123), #placeholder to avoid having unused variable error message
#			(try_end),
#			(assign, "$last_town_log_entry_checked", "$num_log_entries"),
#		(try_end),
        ],
    [
      ("castle_castle",
      [        
        (party_slot_eq,"$current_town",slot_party_type, spt_castle),        
        
        (eq, "$sneaked_into_town", 0),         
        
        (str_clear, s1),
        (try_begin),
          (store_faction_of_party, ":center_faction", "$current_town"),
          (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
          (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),
          (str_store_string, s1, "str__join_the_feast"),
        (try_end),
        ],"Go to the Lord's hall{s1}.",
       [          
           (try_begin),
             (this_or_next|eq, "$all_doors_locked", 1),
             (eq, "$sneaked_into_town", 1),           
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
		     (this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
		     (neg|troop_slot_ge, "trp_player", slot_troop_renown, 50),
			 (neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
			 (neq, "$g_player_eligible_feast_center_no", "$current_town"),

			 (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
			 (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
			 
			 (neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin), #Married players always make the cut
			 
			 (jump_to_menu, "mnu_cannot_enter_court"),
		   (else_try),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_court", "$current_town"),
           (try_end),
        ], "Door to the castle."),
		
#      ("join_tournament", [(neg|is_currently_night),(party_slot_ge, "$current_town", slot_town_has_tournament, 1),]
#       ,"Join the tournament.",
#       [
#           (call_script, "script_fill_tournament_participants_troop", "$current_town", 1),
#           (assign, "$g_tournament_cur_tier", 0),
#           (assign, "$g_tournament_player_team_won", -1),
#           (assign, "$g_tournament_bet_placed", 0),
#           (assign, "$g_tournament_bet_win_amount", 0),
#           (assign, "$g_tournament_last_bet_tier", -1),
#           (assign, "$g_tournament_next_num_teams", 0),
#           (assign, "$g_tournament_next_team_size", 0),
#           (jump_to_menu, "mnu_town_tournament"),
#        ]),
      
      ("town_castle",[        
          (party_slot_eq,"$current_town",slot_party_type, spt_town),        
          (eq,"$entry_to_town_forbidden",0),        
          (str_clear, s1),
          (try_begin),
            (store_faction_of_party, ":center_faction", "$current_town"),
            (faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
            (faction_slot_eq, ":center_faction", slot_faction_ai_object, "$current_town"),
            (str_store_string, s1, "str__join_the_feast"),
          (try_end),

          ],"Go to the castle{s1}.",
       [           
           (try_begin),
             (this_or_next|eq, "$all_doors_locked", 1),
             (eq, "$sneaked_into_town", 1),           
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
		     (this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
		     (neg|troop_slot_ge, "trp_player", slot_troop_renown, 50),
		     (neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
			 (neq, "$g_player_eligible_feast_center_no", "$current_town"),			 
			 
			 (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
			 (faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),

			 (neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin), #Married players always make the cut
			 
             (jump_to_menu, "mnu_cannot_enter_court"),
			(else_try),
			  (assign, "$town_entered", 1),              
              (call_script, "script_enter_court", "$current_town"),
           (try_end),
        ], "Door to the castle."),
      
      ("town_center",
      [                        
        (party_slot_eq, "$current_town", slot_party_type, spt_town),
        (this_or_next|eq,"$entry_to_town_forbidden",0),
        (eq, "$sneaked_into_town",1)
      ],
      "Take a walk around the streets.",
       [
         #If the player is fighting his or her way out
         (try_begin),
           (eq, "$talk_context", tc_prison_break),
           (assign, "$talk_context", tc_escape),
           (assign, "$g_mt_mode", tcm_escape),
           (store_faction_of_party, ":town_faction", "$current_town"),
           (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_3_troop),
           (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           (faction_get_slot, ":tier_4_troop", ":town_faction", slot_faction_tier_4_troop),
           (party_get_slot, ":town_scene", "$current_town", slot_town_center),
           (modify_visitors_at_site, ":town_scene"),
           (reset_visitors),
           #ideally we could alarm troops at locations
           (try_begin), 
	         #if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),                          
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),
                                                    
             (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             (store_time_of_day, ":cur_day_hour"),
             (try_begin), #there are 6 guards at day time (no fire ext)
               (ge, ":cur_day_hour", 6),
               (lt, ":cur_day_hour", 22),
               (set_visitors, 25, ":tier_2_troop", 2),
               (set_visitors, 26, ":tier_2_troop", 1),
               (set_visitors, 27, ":tier_3_troop", 2),
               (set_visitors, 28, ":tier_4_troop", 1),
             (else_try),  #only 4 guards because of night
               (set_visitors, 25, ":tier_2_troop", 1),
               (set_visitors, 26, ":tier_2_troop", 1),
               (set_visitors, 27, ":tier_3_troop", 1),
               (set_visitors, 28, ":tier_4_troop", 1),
             (try_end),
           (else_try),
	         #if guards have gone to some other important happening at nearby villages, then spawn only 1 guard. (example : fire)
             (store_time_of_day, ":cur_day_hour"),
             (try_begin), #only 2 guard because there is a fire at one owned village
               (ge, ":cur_day_hour", 6),
               (lt, ":cur_day_hour", 22),
               (set_visitors, 25, ":tier_2_troop", 1),
               (set_visitors, 26, ":tier_2_troop", 0),
               (set_visitors, 27, ":tier_3_troop", 1),
               (set_visitors, 28, ":tier_4_troop", 0),
             (else_try), #only 1 guard because both night and there is a fire at one owned village
               (set_visitors, 25, ":tier_2_troop", 1),
               (set_visitors, 26, ":tier_2_troop", 0),
               (set_visitors, 27, ":tier_3_troop", 0),
               (set_visitors, 28, ":tier_4_troop", 0),
             (try_end),                   
           (try_end),
           (set_jump_mission,"mt_town_center"),
           (jump_to_scene, ":town_scene"),
           (change_screen_mission),
            #If you're already at escape, then talk context will reset
         (else_try),
           (assign, "$talk_context", 0),
           (call_script, "script_cf_enter_center_location_bandit_check"),
           #All other circumstances...
         (else_try),
           (party_get_slot, ":town_scene", "$current_town", slot_town_center),
           (modify_visitors_at_site, ":town_scene"),
           (reset_visitors),
           (assign, "$g_mt_mode", tcm_default),
           (store_faction_of_party, ":town_faction","$current_town"),
                      
           (try_begin),
             (neq, ":town_faction", "fac_player_supporters_faction"),
             (faction_get_slot, ":troop_prison_guard", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
             (faction_get_slot, ":troop_castle_guard", "$g_encountered_party_faction", slot_faction_castle_guard_troop),
             (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
             (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           (else_try),
             (party_get_slot, ":town_original_faction", "$current_town", slot_center_original_faction),
             (faction_get_slot, ":troop_prison_guard", ":town_original_faction", slot_faction_prison_guard_troop),
             (faction_get_slot, ":troop_castle_guard", ":town_original_faction", slot_faction_castle_guard_troop),
             (faction_get_slot, ":tier_2_troop", ":town_original_faction", slot_faction_tier_2_troop),
             (faction_get_slot, ":tier_3_troop", ":town_original_faction", slot_faction_tier_3_troop),
           (try_end),
           (try_begin), #think about this, should castle guard have to go nearby fire too? If he do not go, killing 2 armored guard is too hard for player. For now he goes too.
             #if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),

             (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             (set_visitor, 23, ":troop_castle_guard"),
           (try_end),
           (set_visitor, 24, ":troop_prison_guard"),
           
           (try_begin),
             (gt,":tier_2_troop", 0),
             (assign,reg0,":tier_3_troop"),
             (assign,reg1,":tier_3_troop"),
             (assign,reg2,":tier_2_troop"),
             (assign,reg3,":tier_2_troop"),
           (else_try),
#             (assign,reg0,"trp_vaegir_infantry"),
#             (assign,reg1,"trp_vaegir_infantry"),
#             (assign,reg2,"trp_vaegir_archer"),
#             (assign,reg3,"trp_vaegir_footman"),
              (assign,reg0,"trp_farmer"),
              (assign,reg1,"trp_farmer"),
              (assign,reg2,"trp_farmer"),
              (assign,reg3,"trp_farmer"),
           (try_end),
           (shuffle_range,0,4),
         
           (try_begin),
             #if guards have not gone to some other important happening at nearby villages, then spawn 4 guards. (example : fire)
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),

             (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             (set_visitor,25,reg0),
             (set_visitor,26,reg1),
             (set_visitor,27,reg2),
             (set_visitor,28,reg3),
           (try_end),
         
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_armorer),
           (set_visitor, 9, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_weaponsmith),
           (set_visitor, 10, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_elder),
           (set_visitor, 11, ":spawned_troop"),
           (party_get_slot, ":spawned_troop", "$current_town", slot_town_horse_merchant),
           (set_visitor, 12, ":spawned_troop"),
           (call_script, "script_init_town_walkers"),
           (set_jump_mission,"mt_town_center"),
           (assign, ":override_state", af_override_horse),
           (try_begin),
             (eq, "$sneaked_into_town", 1), #setup disguise
             (assign, ":override_state", af_override_all),
           (try_end),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 0, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 2, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 3, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 4, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 5, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 6, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_town_center", 7, ":override_state"),
           (try_begin),
             (eq, "$town_entered", 0),
             (assign, "$town_entered", 1),
             (eq, "$town_nighttime", 0),
             (set_jump_entry, 1),
           (try_end),
           (jump_to_scene, ":town_scene"),
           (change_screen_mission),
         (try_end),	   
      ],"Door to the town center."),
      
      ("town_tavern",[
          (party_slot_eq,"$current_town",slot_party_type, spt_town),
          (this_or_next|eq,"$entry_to_town_forbidden",0),
          (eq, "$sneaked_into_town",1),
#          (party_get_slot, ":scene", "$current_town", slot_town_tavern),
#          (scene_slot_eq, ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
          ]
       ,"Visit the tavern.",
       [
           (try_begin),
             (eq,"$all_doors_locked",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (assign, "$town_entered", 1),
             (set_jump_mission, "mt_town_default"),
             (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_horse),
             (try_begin),
               (eq, "$sneaked_into_town",1),
               (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_all),
             (try_end),
             (party_get_slot, ":cur_scene", "$current_town", slot_town_tavern),
             (jump_to_scene, ":cur_scene"),
             (scene_set_slot, ":cur_scene", slot_scene_visited, 1),

             (assign, "$talk_context", tc_tavern_talk),
             (call_script, "script_initialize_tavern_variables"),

#			 (store_random_in_range, ":randomize_attacker_placement", 0, 4),

             (modify_visitors_at_site, ":cur_scene"),
             (reset_visitors),
             
             (assign, ":cur_entry", 17),

			 #this is just a cheat right now
			 
			 #this determines whether or not a lord who dislikes you will commission an assassin


             (party_get_slot, ":mercenary_troop", "$current_town", slot_center_mercenary_troop_type),
             (party_get_slot, ":mercenary_amount", "$current_town", slot_center_mercenary_troop_amount),
             (try_begin),
			   (gt, ":mercenary_troop", 0),
               (gt, ":mercenary_amount", 0),
               (set_visitor, ":cur_entry", ":mercenary_troop"),
               (val_add, ":cur_entry", 1),
             (try_end),

             (try_for_range, ":companion_candidate", companions_begin, companions_end),
               (troop_slot_eq, ":companion_candidate", slot_troop_occupation, 0),
               (troop_slot_eq, ":companion_candidate", slot_troop_cur_center, "$current_town"),
			   (neg|troop_slot_ge, ":companion_candidate", slot_troop_prisoner_of_party, centers_begin),
			   
               (set_visitor, ":cur_entry", ":companion_candidate"),

               (val_add, ":cur_entry", 1),
             (try_end),
			 
             (try_begin), #this doubles the incidence of ransom brokers and (below) minstrels
               (party_get_slot, ":ransom_broker", "$current_town", slot_center_ransom_broker),
               (gt, ":ransom_broker", 0),
               
               (assign, reg0, ":ransom_broker"),
               (assign, reg1, "$current_town"),
			   
               (set_visitor, ":cur_entry", ":ransom_broker"),
               (val_add, ":cur_entry", 1),
             (try_end),
			 
             (try_begin),
               (party_get_slot, ":tavern_traveler", "$current_town", slot_center_tavern_traveler),
               (gt, ":tavern_traveler", 0),
               (set_visitor, ":cur_entry", ":tavern_traveler"),
               (val_add, ":cur_entry", 1),
             (try_end),
			 
             (try_begin),
               (party_get_slot, ":tavern_minstrel", "$current_town", slot_center_tavern_minstrel),
               (gt, ":tavern_minstrel", 0),
			   
               (set_visitor, ":cur_entry", ":tavern_minstrel"),
               (val_add, ":cur_entry", 1),
			 (else_try),  
			   (store_add, ":alternative_town", "$current_town", 9),
			   (try_begin),
				(ge, ":alternative_town", towns_end),
				(val_sub, ":alternative_town", 22),
			   (try_end),
               (party_get_slot, ":tavern_minstrel", ":alternative_town", slot_center_tavern_minstrel),			   
               (gt, ":tavern_minstrel", 0),
			   
               (set_visitor, ":cur_entry", ":tavern_minstrel"),
               (val_add, ":cur_entry", 1),
             (try_end),
			 
             (try_begin),
               (party_get_slot, ":tavern_bookseller", "$current_town", slot_center_tavern_bookseller),
               (gt, ":tavern_bookseller", 0),
               (set_visitor, ":cur_entry", ":tavern_bookseller"),
               (val_add, ":cur_entry", 1),
             (try_end),
			 
             (try_begin),
               (neg|check_quest_active, "qst_eliminate_bandits_infesting_village"),
#               (neg|check_quest_active, "qst_deal_with_bandits_at_lords_village"),
               (assign, ":end_cond", villages_end),
               (try_for_range, ":cur_village", villages_begin, ":end_cond"),
                 (party_slot_eq, ":cur_village", slot_village_bound_center, "$current_town"),
                 (party_slot_ge, ":cur_village", slot_village_infested_by_bandits, 1),
                 (neg|party_slot_eq, ":cur_village", slot_town_lord, "trp_player"),
                 (set_visitor, ":cur_entry", "trp_farmer_from_bandit_village"),
                 (val_add, ":cur_entry", 1),
                 (assign, ":end_cond", 0),
               (try_end),
             (try_end),
             
#             (try_begin),
#               (eq, "$g_starting_town", "$current_town"),
#                              
#               (this_or_next|neg|check_quest_finished, "qst_collect_men"),
#               (this_or_next|neg|check_quest_finished, "qst_learn_where_merchant_brother_is"),
#               (this_or_next|neg|check_quest_finished, "qst_save_relative_of_merchant"),
#               (this_or_next|neg|check_quest_finished, "qst_save_town_from_bandits"),
#               (eq,  "$g_do_one_more_meeting_with_merchant", 1),
#               
#			   (assign, ":troop_of_merchant", 0),	
#               (try_begin),
#                 (eq, "$g_encountered_party_faction", "fac_kingdom_1"),
#                 (assign, ":troop_of_merchant", "trp_swadian_merchant"),
#               (else_try),  
#                 (eq, "$g_encountered_party_faction", "fac_kingdom_2"),
#                 (assign, ":troop_of_merchant", "trp_vaegir_merchant"),
#               (else_try),                   
#                 (eq, "$g_encountered_party_faction", "fac_kingdom_3"),
#                 (assign, ":troop_of_merchant", "trp_khergit_merchant"),
#               (else_try),  
#                 (eq, "$g_encountered_party_faction", "fac_kingdom_4"),
#                 (assign, ":troop_of_merchant", "trp_nord_merchant"),
#               (else_try),  
#                 (eq, "$g_encountered_party_faction", "fac_kingdom_5"),
#                 (assign, ":troop_of_merchant", "trp_rhodok_merchant"),
#               (else_try),  
#                 (eq, "$g_encountered_party_faction", "fac_kingdom_6"),
#                 (assign, ":troop_of_merchant", "trp_sarranid_merchant"),
#               (try_end),
#			   (gt, ":troop_of_merchant", 0),	
#               
#               (set_visitor, ":cur_entry", ":troop_of_merchant"),
#               (val_add, ":cur_entry", 1),
#             (try_end),                         
             
             (change_screen_mission),
           (try_end),
        ],"Door to the tavern."),
                               
#      ("town_smithy",[
#          (eq,"$entry_to_town_forbidden",0),
#          (eq,"$town_nighttime",0),
#          ],
#       "Visit the smithy.",
#       [
#           (set_jump_mission,"mt_town_default"),
#           (jump_to_scene,"$pout_scn_smithy"),
#           (change_screen_mission,0),
#        ]),

      
      ("town_merchant",
       [(party_slot_eq,"$current_town",slot_party_type, spt_town),
           (eq, 1, 0),
           (eq,"$town_nighttime",0),
           (this_or_next|eq,"$entry_to_town_forbidden",0),
           (eq, "$sneaked_into_town",1),
#           (party_get_slot, ":scene", "$current_town", slot_town_store),
#           (scene_slot_eq, ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
           ],
       "Speak with the merchant.",
       [           
           (try_begin),
             (this_or_next|eq,"$all_doors_locked",1),
             (eq,"$town_nighttime",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (assign, "$town_entered", 1),
             (set_jump_mission, "mt_town_default"),
             (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_horse),
             (try_begin),
               (eq, "$sneaked_into_town",1),
               (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_all),
             (try_end),
             (party_get_slot, ":cur_scene", "$current_town", slot_town_store),
             (jump_to_scene, ":cur_scene"),
             (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
             (change_screen_mission),
           (try_end),
        ],"Door to the shop."),       
                
#      ("town_arena",
#       [(party_slot_eq,"$current_town",slot_party_type, spt_town),
#        (eq, "$sneaked_into_town", 0),
##           (party_get_slot, ":scene", "$current_town", slot_town_arena),
##           (scene_slot_eq,  ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
#           ],
#       "Enter the arena.",
#       [
#           (try_begin),
#             (this_or_next|eq,"$all_doors_locked",1),
#             (eq,"$town_nighttime",1),
#             (display_message,"str_door_locked",0xFFFFAAAA),
#           (else_try),
#             (assign, "$g_mt_mode", abm_visit),
#             (assign, "$town_entered", 1),
#             (set_jump_mission, "mt_arena_melee_fight"),
#             (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
#             (modify_visitors_at_site, ":arena_scene"),
#             (reset_visitors),
#             (set_visitor, 43, "trp_veteran_fighter"),
#             (set_visitor, 44, "trp_hired_blade"),
#             (set_jump_entry, 50),
#             (jump_to_scene, ":arena_scene"),
#             (scene_set_slot, ":arena_scene", slot_scene_visited, 1),
#             (change_screen_mission),
#           (try_end),
#        ],"Door to the arena."),
#      ("town_dungeon",
#       [(eq, 1, 0)],
#       "Never: Enter the prison.",
#       [	   
#           (try_begin),
#		    (eq, "$talk_context", tc_prison_break),
#			(gt, "$g_main_attacker_agent", 0),
#			
#		   	(neg|agent_is_alive, "$g_main_attacker_agent"),
#
#			(agent_get_troop_id, ":agent_type", "$g_main_attacker_agent"),
#			(try_begin),
#			  (eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
#			  (party_get_slot, ":prison_guard_faction", "$current_town", slot_center_original_faction),
#			(else_try),
#			  (assign, ":prison_guard_faction", "$g_encountered_party_faction"),
#			(try_end),
#			(faction_slot_eq, ":prison_guard_faction", slot_faction_prison_guard_troop, ":agent_type"),
#
#			(call_script, "script_deduct_casualties_from_garrison"),
#            (call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle"),
#
#		   (else_try),
#             (eq,"$all_doors_locked",1),
#             (display_message,"str_door_locked",0xFFFFAAAA),
#           (else_try),
#             (this_or_next|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
#             (eq, "$g_encountered_party_faction", "$players_kingdom"),
#             (assign, "$town_entered", 1),
#             (call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle"),
#           (else_try),
#             (display_message,"str_door_locked",0xFFFFAAAA),
#           (try_end),
#        ],"Door to the dungeon."),
		
      ("castle_inspect", 
      [
         (party_slot_eq,"$current_town",slot_party_type, spt_castle),
      ],
       "Take a walk around the courtyard.",
       [
         (try_begin),
           (eq, "$talk_context", tc_prison_break),
           (assign, "$talk_context", tc_escape),
           
           (party_get_slot, ":cur_castle_exterior", "$current_town", slot_castle_exterior),
           (modify_visitors_at_site, ":cur_castle_exterior"),
           (reset_visitors),
           
           (assign, ":guard_no", 40),
           
           (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
           (try_for_range, ":troop_iterator", 0, ":num_stacks"),
             #nearby fire condition start
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),  
             (this_or_next|eq, ":guard_no", 40),
             (neg|is_between, ":cur_time", ":last_nearby_fire_time", ":fire_finish_time"),
             #nearby fire condition end

             (lt, ":guard_no", 47),
             (party_stack_get_troop_id, ":cur_troop_id", "$g_encountered_party", ":troop_iterator"),
             (neg|troop_is_hero, ":cur_troop_id"),
             (party_stack_get_size, ":stack_size","$g_encountered_party",":troop_iterator"),
             (party_stack_get_num_wounded, ":num_wounded","$g_encountered_party",":troop_iterator"),
             (val_sub, ":stack_size", ":num_wounded"),
             (gt, ":stack_size", 0),
             (party_stack_get_troop_dna,":troop_dna", "$g_encountered_party", ":troop_iterator"),
             (set_visitor, ":guard_no", ":cur_troop_id", ":troop_dna"),
             (val_add, ":guard_no", 1),
           (try_end),                      
           #(set_jump_entry, 1),           
           (set_visitor, 7, "$g_player_troop"),

           (set_jump_mission,"mt_castle_visit"),
           (jump_to_scene, ":cur_castle_exterior"),
           (change_screen_mission),
            #If you're already at escape, then talk context will reset            
         (else_try),                   
           (assign, "$talk_context", tc_town_talk),
           
           (assign, "$g_mt_mode", tcm_default),
           
           (party_get_slot, ":cur_castle_exterior", "$current_town", slot_castle_exterior),
           (modify_visitors_at_site,":cur_castle_exterior"),
           (reset_visitors),

           (try_begin),
             (neq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
             (faction_get_slot, ":troop_prison_guard", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
           (else_try),
             (party_get_slot, ":town_original_faction", "$current_town", slot_center_original_faction),
             (faction_get_slot, ":troop_prison_guard", ":town_original_faction", slot_faction_prison_guard_troop),
           (try_end),
           (set_visitor, 24, ":troop_prison_guard"),
           
           (assign, ":guard_no", 40),
           
           (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
           (try_for_range, ":troop_iterator", 0, ":num_stacks"),
             #nearby fire condition start
             (party_get_slot, ":last_nearby_fire_time", "$current_town", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_time"),
             (store_add, ":fire_finish_time", ":last_nearby_fire_time", fire_duration),  
             (neg|is_between, ":cur_time", ":fire_finish_time", ":last_nearby_fire_time"),

             (lt, ":guard_no", 47),
             (party_stack_get_troop_id, ":cur_troop_id", "$g_encountered_party", ":troop_iterator"),
             (neg|troop_is_hero, ":cur_troop_id"),
             (party_stack_get_size, ":stack_size","$g_encountered_party",":troop_iterator"),
             (party_stack_get_num_wounded, ":num_wounded","$g_encountered_party",":troop_iterator"),
             (val_sub, ":stack_size", ":num_wounded"),
             (gt, ":stack_size", 0),
             (party_stack_get_troop_dna,":troop_dna","$g_encountered_party",":troop_iterator"),
             (set_visitor, ":guard_no", ":cur_troop_id", ":troop_dna"),
                          
             (val_add, ":guard_no", 1),
           (try_end),
           
           (try_begin),
             (eq, "$town_entered", 0),
             (assign, "$town_entered", 1),
           (try_end),
           (set_jump_entry, 1),

           (assign, ":override_state", af_override_horse),             
           (try_begin),
             (eq, "$sneaked_into_town", 1), #setup disguise
             (assign, ":override_state", af_override_all),
           (try_end),
           (set_jump_mission, "mt_castle_visit"),

           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 0, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 1, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 2, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 3, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 4, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 5, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 6, ":override_state"),
           (mission_tpl_entry_set_override_flags, "mt_castle_visit", 7, ":override_state"),           
           
           (jump_to_scene, ":cur_castle_exterior"),
           (change_screen_mission),
         (try_end),
        ], "To the castle courtyard."),
        
     ("town_enterprise",
      [
        (party_slot_eq,"$current_town",slot_party_type, spt_town),
        (party_get_slot, ":item_produced", "$current_town", slot_center_player_enterprise),
		(gt, ":item_produced", 1),
        (eq,"$entry_to_town_forbidden",0),
		(call_script, "script_get_enterprise_name", ":item_produced"),
		(str_store_string, s3, reg0),
      ],	
      "Visit your {s3}.",
      [
        (store_sub, ":town_order", "$current_town", towns_begin),
		(store_add, ":master_craftsman", "trp_town_1_master_craftsman", ":town_order"),
        (party_get_slot, ":item_produced", "$current_town", slot_center_player_enterprise),
		(assign, ":enterprise_scene", "scn_enterprise_mill"),
		(try_begin),
			(eq, ":item_produced", "itm_bread"),
			(assign, ":enterprise_scene", "scn_enterprise_mill"),
		(else_try),
			(eq, ":item_produced", "itm_ale"),
			(assign, ":enterprise_scene", "scn_enterprise_brewery"),
		(else_try),
			(eq, ":item_produced", "itm_oil"),
			(assign, ":enterprise_scene", "scn_enterprise_oil_press"),
		(else_try),
			(eq, ":item_produced", "itm_wine"),
			(assign, ":enterprise_scene", "scn_enterprise_winery"),
		(else_try),
			(eq, ":item_produced", "itm_leatherwork"),
			(assign, ":enterprise_scene", "scn_enterprise_tannery"),
		(else_try),
			(eq, ":item_produced", "itm_wool_cloth"),
			(assign, ":enterprise_scene", "scn_enterprise_wool_weavery"),
		(else_try),
			(eq, ":item_produced", "itm_linen"),
			(assign, ":enterprise_scene", "scn_enterprise_linen_weavery"),
		(else_try),
			(eq, ":item_produced", "itm_velvet"),
			(assign, ":enterprise_scene", "scn_enterprise_dyeworks"),
		(else_try),
			(eq, ":item_produced", "itm_tools"),
			(assign, ":enterprise_scene", "scn_enterprise_smithy"),
		(try_end),
        (modify_visitors_at_site,":enterprise_scene"),
		(reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,17,":master_craftsman"),
        (set_jump_mission,"mt_town_default"),
        (jump_to_scene,":enterprise_scene"),
        (change_screen_mission),
      ],"Door to your enterprise."), 

#    ("visit_lady",
#	[
#	
#	(neg|troop_slot_ge, "trp_player", slot_troop_spouse, kingdom_ladies_begin),
#	
#	(assign, "$love_interest_in_town", 0),
#	(assign, "$love_interest_in_town_2", 0),
#	(assign, "$love_interest_in_town_3", 0),
#	(assign, "$love_interest_in_town_4", 0),
#	(assign, "$love_interest_in_town_5", 0),
#	(assign, "$love_interest_in_town_6", 0),
#	(assign, "$love_interest_in_town_7", 0),
#	(assign, "$love_interest_in_town_8", 0),
#	
#	(try_for_range, ":lady_no", kingdom_ladies_begin, kingdom_ladies_end),
#		(troop_slot_eq, ":lady_no", slot_troop_cur_center, "$current_town"),
#		(call_script, "script_get_kingdom_lady_social_determinants", ":lady_no"),
#		(assign, ":lady_guardian", reg0),
#		
#		(troop_slot_eq, ":lady_no", slot_troop_spouse, -1),
#		(ge, ":lady_guardian", 0), #not sure when this would not be the case
#
#		
#		#must have spoken to either father or lady
#		(this_or_next|troop_slot_ge, ":lady_no", slot_troop_met, 2),
#			(troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, 1),
#		
#		(neg|troop_slot_eq, ":lady_no", slot_troop_met, 4),
#		
#		#must have approached father
##		(this_or_next|troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, 1),
##			(troop_slot_eq, ":lady_guardian", slot_lord_granted_courtship_permission, -1),
#			
#		
#		(try_begin),
#			(eq, "$love_interest_in_town", 0),
#			(assign, "$love_interest_in_town", ":lady_no"),	
#		(else_try),
#			(eq, "$love_interest_in_town_2", 0),
#			(assign, "$love_interest_in_town_2", ":lady_no"),	
#		(else_try),
#			(eq, "$love_interest_in_town_3", 0),
#			(assign, "$love_interest_in_town_3", ":lady_no"),	
#		(else_try),
#			(eq, "$love_interest_in_town_4", 0),
#			(assign, "$love_interest_in_town_4", ":lady_no"),	
#		(else_try),
#			(eq, "$love_interest_in_town_5", 0),
#			(assign, "$love_interest_in_town_5", ":lady_no"),	
#		(else_try),
#			(eq, "$love_interest_in_town_6", 0),
#			(assign, "$love_interest_in_town_6", ":lady_no"),
#		(else_try),
#			(eq, "$love_interest_in_town_7", 0),
#			(assign, "$love_interest_in_town_7", ":lady_no"),		
#		(else_try),
#			(eq, "$love_interest_in_town_8", 0),
#			(assign, "$love_interest_in_town_8", ":lady_no"),		
#		(try_end),	
#	(try_end),
#	
#	(gt, "$love_interest_in_town", 0),
#	],
#	  "Attempt to visit a lady",
#       [
#        (jump_to_menu, "mnu_lady_visit"),
#        ], "Door to the garden."),										
		
      ("trade_with_merchants",
       [
           (party_slot_eq,"$current_town",slot_party_type, spt_town)
        ],
         "Go to the marketplace.",
         [
           (try_begin),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (jump_to_menu,"mnu_town_trade"),
           (try_end),
          ]),

      ("walled_center_manage",
      [
        (neg|party_slot_eq, "$current_town", slot_village_state, svs_under_siege),
        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
        (assign, reg0, 1),
        (try_begin),
          (party_slot_eq, "$current_town", slot_party_type, spt_castle),
          (assign, reg0, 0),
        (try_end),
       ],
       "Manage this {reg0?town:castle}.",
       [
           (assign, "$g_next_menu", "mnu_town"),
           (jump_to_menu, "mnu_center_manage"),
       ]),
		
#      ("walled_center_move_court",
#      [
#        (neg|party_slot_eq, "$current_town", slot_village_state, svs_under_siege),
#        (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
#        (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
#        (eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
#        (neq, "$g_player_court", "$current_town"),
#      ],
#      "Move your court here.",
#      [
#        (jump_to_menu, "mnu_establish_court"),
#      ]),
								
      ("castle_station_troops",
      [	  
		(party_get_slot, ":town_lord", "$current_town", slot_town_lord),
	    (str_clear, s10),
		  
	    (assign, ":player_can_draw_from_garrison", 0), 
		(try_begin), #option 1 - player is town lord
		  (eq, ":town_lord", "trp_player"),
		  (assign, ":player_can_draw_from_garrison", 1),
		(else_try), #option 2 - town is unassigned and part of the player faction
		  (store_faction_of_party, ":faction", "$g_encountered_party"),
		  (eq, ":faction", "fac_player_supporters_faction"),			
		  (neg|party_slot_ge, "$g_encountered_party", slot_town_lord, active_npcs_begin), #ie, zero or -1

		  (assign, ":player_can_draw_from_garrison", 1),
		(else_try), #option 3 - town was captured by player
		  (lt, ":town_lord", 0), #ie, unassigned
		  (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
		  (eq, "$players_kingdom", ":castle_faction"),
		  
		  (eq, "$g_encountered_party", "$g_castle_requested_by_player"),

		  (str_store_string, s10, "str_retrieve_garrison_warning"),
		  (assign, ":player_can_draw_from_garrison", 1),
		(else_try),
		  (lt, ":town_lord", 0), #ie, unassigned
		  (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
		  (eq, "$players_kingdom", ":castle_faction"),
		  
		  (store_party_size_wo_prisoners, ":party_size", "$g_encountered_party"),
		  (eq, ":party_size", 0),
			
		  (str_store_string, s10, "str_retrieve_garrison_warning"),
		  (assign, ":player_can_draw_from_garrison", 1),
		(else_try),
		  (party_slot_ge, "$g_encountered_party", slot_town_lord, active_npcs_begin),
		  (store_faction_of_party, ":castle_faction", "$g_encountered_party"),
		  (eq, "$players_kingdom", ":castle_faction"),
		  
		  (troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),		    

		  (assign, ":player_can_draw_from_garrison", 1),
		(try_end),

        (eq, ":player_can_draw_from_garrison", 1),
      ],
      "Manage the garrison {s10}",
      [
        (change_screen_exchange_members,1),
      ]),

      ("castle_wait",
      [
        #(party_slot_eq,"$current_town",slot_party_type, spt_castle),
        (this_or_next|ge, "$g_encountered_party_relation", 0),
        (eq,"$castle_undefended",1),
        (assign, ":can_rest", 1),
        (str_clear, s1),
        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
		  (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
          (neg|party_slot_eq, "$current_town", slot_town_lord, ":player_spouse"),

          (party_slot_ge, "$current_town", slot_town_lord, "trp_player"), #can rest for free in castles and towns with unassigned lords
          (store_faction_of_party, ":current_town_faction", "$current_town"),
          (neq, ":current_town_faction", "fac_player_supporters_faction"),
          (party_get_num_companions, ":num_men", "p_main_party"),
          (store_div, reg1, ":num_men", 4),
          (val_add, reg1, 1),
          (str_store_string, s1, "@ ({reg1} denars per night)"),
          (store_troop_gold, ":gold", "trp_player"),
          (lt, ":gold", reg1),
          (assign, ":can_rest", 0),
        (try_end),
        (eq, ":can_rest", 1),
      ],
      "Wait here for some time{s1}.",
      [
        (assign, "$auto_enter_town", "$current_town"),
        (assign, "$g_town_visit_after_rest", 1),
        (assign, "$g_last_rest_center", "$current_town"),
        (assign, "$g_last_rest_payment_until", -1),

        (try_begin),
          (party_is_active, "p_main_party"),
          (party_get_current_terrain, ":cur_terrain", "p_main_party"),
          (try_begin),
            (eq, ":cur_terrain", rt_desert),
            (unlock_achievement, ACHIEVEMENT_SARRANIDIAN_NIGHTS),
          (try_end),  
        (try_end),  

        (rest_for_hours_interactive, 24 * 7, 5, 0), #rest while not attackable
        (change_screen_return),
      ]),

##      ("rest_until_morning",
##       [
##           (this_or_next|ge, "$g_encountered_party_relation", 0),
##           (eq,"$castle_undefended",1),
##           (store_time_of_day,reg(1)),(neg|is_between,reg(1), 5, 18),
##           (eq, "$g_defending_against_siege", 0),
##        ],
##         "Rest until morning.",
##         [
##           (store_time_of_day,reg(1)),
##           (assign, reg(2), 30),
##           (val_sub,reg(2),reg(1)),
##           (val_mod,reg(2),24),
##           (assign,"$auto_enter_town","$current_town"),
##           (assign, "$g_town_visit_after_rest", 1),
##           (rest_for_hours_interactive, reg(2)),
##           (change_screen_return),
##          ]),
##      
##      ("rest_until_evening",
##       [
##           (this_or_next|ge, "$g_encountered_party_relation", 0),
##           (eq,"$castle_undefended",1),
##           (store_time_of_day,reg(1)), (is_between,reg(1), 5, 18),
##           (eq, "$g_defending_against_siege", 0),
##        ],
##         "Rest until evening.",
##         [
##           (store_time_of_day,reg(1)),
##           (assign, reg(2), 20),
##           (val_sub,reg(2),reg(1)),
##           (assign,"$auto_enter_town","$current_town"),
##           (assign, "$g_town_visit_after_rest", 1),
##           (rest_for_hours_interactive, reg(2)),
##           (change_screen_return),
##          ]),
      ("town_alley",
      [
        (party_slot_eq,"$current_town",slot_party_type, spt_town),
        (eq, "$cheat_mode", 1),
      ],
      "{!}CHEAT: Go to the alley.",
      [
        (party_get_slot, reg11, "$current_town", slot_town_alley),
        (set_jump_mission, "mt_ai_training"),
        (jump_to_scene, reg11),
        (change_screen_mission),
      ]),
      
#      ("collect_taxes_qst",
#      [
#        (check_quest_active, "qst_collect_taxes"),
#        (quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, "$current_town"),
#        (neg|quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 4),
#        (quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
#        (str_store_troop_name, s1, ":quest_giver_troop"),
#        (quest_get_slot, reg5, "qst_collect_taxes", slot_quest_current_state),
#      ],
#      "{reg5?Continue collecting taxes:Collect taxes} due to {s1}.",
#      [
#        (jump_to_menu, "mnu_collect_taxes"),
#      ]),

       


      
      ("town_leave",[],"Leave...",
      [
        (assign, "$g_permitted_to_center",0),
        (change_screen_return,0),
      ],"Leave Area."),

      ("castle_cheat_interior",
      [
        (eq, "$cheat_mode", 1),
      ], 
      "{!}CHEAT! Interior.",
      [
        (set_jump_mission,"mt_ai_training"),
        (party_get_slot, ":castle_scene", "$current_town", slot_town_castle),
        (jump_to_scene,":castle_scene"),
        (change_screen_mission),
      ]),
                                                       
      ("castle_cheat_town_exterior",
      [
        (eq, "$cheat_mode", 1),
      ], 
      "{!}CHEAT! Exterior.",
      [
        (try_begin),
          (party_slot_eq, "$current_town",slot_party_type, spt_castle),
          (party_get_slot, ":scene", "$current_town", slot_castle_exterior),
        (else_try),
          (party_get_slot, ":scene", "$current_town", slot_town_center),
        (try_end),
        (set_jump_mission,"mt_ai_training"),
        (jump_to_scene,":scene"),
        (change_screen_mission),
      ]),
                                                       
      ("castle_cheat_dungeon",
      [
        (eq, "$cheat_mode", 1),
      ], 
      "{!}CHEAT! Prison.",
      [
        (set_jump_mission,"mt_ai_training"),
        (party_get_slot, ":castle_scene", "$current_town", slot_town_prison),
        (jump_to_scene,":castle_scene"),
        (change_screen_mission),
      ]),
      
      ("castle_cheat_town_walls",
      [
        (eq, "$cheat_mode", 1),
        (party_slot_eq,"$current_town",slot_party_type, spt_town),
      ], 
      "{!}CHEAT! Town Walls.",
      [
        (party_get_slot, ":scene", "$current_town", slot_town_walls),
        (set_jump_mission,"mt_ai_training"),
        (jump_to_scene,":scene"),
        (change_screen_mission),
      ]),

#      ("cheat_town_start_siege",
#      [
#        (eq, "$cheat_mode", 1),
#        (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
#        (lt, "$g_encountered_party_2", 1),
#        (call_script, "script_party_count_fit_for_battle","p_main_party"),
#        (gt, reg(0), 1),
#        (try_begin),
#          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
#          (assign, reg6, 1),
#        (else_try),
#          (assign, reg6, 0),
#        (try_end),
#      ],
#      "{!}CHEAT: Besiege the {reg6?town:castle}...",
#      [
#        (assign,"$g_player_besiege_town","$g_encountered_party"),
#        (jump_to_menu, "mnu_castle_besiege"),
#      ]),

      ("center_reports",
      [
        (eq, "$cheat_mode", 1),
      ], 
      "{!}CHEAT! Show reports.",
      [
        (jump_to_menu,"mnu_center_reports"),
      ]),

      ("sail_from_port",
      [
        (party_slot_eq,"$current_town",slot_party_type, spt_town),
        (eq, "$cheat_mode", 1),
        #(party_slot_eq,"$current_town",slot_town_near_shore, 1),
      ],
      "{!}CHEAT: Sail from port.",
      [
        (assign, "$g_player_icon_state", pis_ship),
        (party_set_flags, "p_main_party", pf_is_ship, 1),
        (party_get_position, pos1, "p_main_party"),
        (map_get_water_position_around_position, pos2, pos1, 6),
        (party_set_position, "p_main_party", pos2),
        (assign, "$g_main_ship_party", -1),
        (change_screen_return),
      ]),

    ]
   ),

      

  (
    "cannot_enter_court",0,
    "There is a feast in progress in the lord's hall, but you are not of sufficient status to be invited inside. Perhaps increasing your renown would win you admittance -- or you might also try distinguishing yourself at a tournament while the feast is in progress...",
    "none",
    [],
    [
	("continue", [],"Continue",
       [
        (jump_to_menu, "mnu_town"),
        ]),
	]),
  
  
#  (
#    "lady_visit",0,
#    "Whom do you wish to visit?",
#    "none",
#    [],
#    [		
#		
#	("visit_lady_1", [
#	(gt, "$love_interest_in_town", 0),
#	(str_store_troop_name, s12, "$love_interest_in_town"),
#	],
#	  "Visit {s12}",
#       [
#	    (assign, "$love_interest_in_town", "$love_interest_in_town"),
#        (jump_to_menu, "mnu_garden"),
#        ]),
#
#
#		
#	("visit_lady_2", [
#	(gt, "$love_interest_in_town_2", 0),
#	(str_store_troop_name, s12, "$love_interest_in_town_2"),
#	],
#	  "Visit {s12}",
#       [
#	    (assign, "$love_interest_in_town", "$love_interest_in_town_2"),
#        (jump_to_menu, "mnu_garden"),
#        ]),
#
#	("visit_lady_3", [
#	(gt, "$love_interest_in_town_3", 0),
#	(str_store_troop_name, s12, "$love_interest_in_town_3"),
#	],
#	  "Visit {s12}",
#       [
#	    (assign, "$love_interest_in_town", "$love_interest_in_town_3"),
#        (jump_to_menu, "mnu_garden")], "Door to the garden."),
#
#		
#	("visit_lady_4", [(gt, "$love_interest_in_town_4", 0),(str_store_troop_name, s12, "$love_interest_in_town_4"),],
#	"Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_4"),(jump_to_menu, "mnu_garden"),]),
#		
#	("visit_lady_5", [(gt, "$love_interest_in_town_5", 0),(str_store_troop_name, s12, "$love_interest_in_town_5"),],
#	"Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_5"),(jump_to_menu, "mnu_garden"),]),
#
#	("visit_lady_6",[(gt, "$love_interest_in_town_6", 0),(str_store_troop_name, s12, "$love_interest_in_town_6"),],
#	"Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_6"),(jump_to_menu, "mnu_garden"),]),
#	
#	("visit_lady_7",[(gt, "$love_interest_in_town_7", 0),(str_store_troop_name, s12, "$love_interest_in_town_7"),],
#	"Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_7"),(jump_to_menu, "mnu_garden"),]),
#
#	("visit_lady_8",[(gt, "$love_interest_in_town_8", 0),(str_store_troop_name, s12, "$love_interest_in_town_8"),],
#	"Visit {s12}",[(assign, "$love_interest_in_town", "$love_interest_in_town_8"),(jump_to_menu, "mnu_garden"),]),
#
#	
#	("leave",[], "Leave",[(jump_to_menu, "mnu_town")]),
#
#    ]
#	),
#
#	
#  (
#    "town_tournament_lost",0,
#    "You have been eliminated from the tournament.{s8}",
#    "none",
#    [
#	(str_clear, s8),
#	(try_begin),
#		(this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
#			(neg|troop_slot_ge, "trp_player", slot_troop_renown, 50),
#		(neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
#		(gt, "$g_player_tournament_placement", 4),
#		(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
#		(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
#		(str_store_string, s8, "str__however_you_have_sufficiently_distinguished_yourself_to_be_invited_to_attend_the_ongoing_feast_in_the_lords_castle"),
#	(try_end),
#	
#        ],
#    [
#      ("continue", [], "Continue...",
#       [(jump_to_menu, "mnu_town_tournament_won_by_another"),
#        ]),
#    ]
#  ),
#
#  (
#    "town_tournament_won",mnf_disable_all_keys,
#    "You have won the tournament of {s3}! You are filled with pride as the crowd cheers your name.\
# In addition to honour, fame and glory, you earn a prize of {reg9} denars. {s8}",
#    "none",
#    [
#        (str_store_party_name, s3, "$current_town"),
#        (call_script, "script_change_troop_renown", "trp_player", 20),
#        (call_script, "script_change_player_relation_with_center", "$current_town", 1),   
#        (assign, reg9, 200),
#        (add_xp_to_troop, 250, "trp_player"),
#        (troop_add_gold, "trp_player", reg9),
#        (str_clear, s8),
#        (store_add, ":total_win", "$g_tournament_bet_placed", "$g_tournament_bet_win_amount"),
#        (try_begin),
#          (gt, "$g_tournament_bet_win_amount", 0),
#          (assign, reg8, ":total_win"),
#          (str_store_string, s8, "@Moreover, you earn {reg8} denars from the clever bets you placed on yourself..."),
#        (try_end),
#		(try_begin),
#			(this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
#				(neg|troop_slot_ge, "trp_player", slot_troop_renown, 70),
#			(neg|troop_slot_ge, "trp_player", slot_troop_renown, 145),
#
#			(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_state, sfai_feast),
#			(faction_slot_eq, "$g_encountered_party_faction", slot_faction_ai_object, "$g_encountered_party"),
#			(str_store_string, s8, "str_s8_you_are_also_invited_to_attend_the_ongoing_feast_in_the_castle"),
#		(try_end),
#        (troop_add_gold, "trp_player", ":total_win"),
#        (assign, ":player_odds_sub", 0),
#        (store_div, ":player_odds_sub", "$g_tournament_bet_win_amount", 5),
#        (party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
#        (val_sub, ":player_odds", ":player_odds_sub"),
#        (val_max, ":player_odds", 250),
#        (party_set_slot, "$current_town", slot_town_player_odds, ":player_odds"),
#        (call_script, "script_play_victorious_sound"),
#        
#        (unlock_achievement, ACHIEVEMENT_MEDIEVAL_TIMES),
#        ],
#    [
#      ("continue", [], "Continue...",
#       [(jump_to_menu, "mnu_town"),
#        ]),
#    ]
#  ),
#  
#  (
#    "town_tournament_won_by_another",mnf_disable_all_keys,
#    "As the only {reg3?fighter:man} to remain undefeated this day, {s1} wins the lists and the glory of this tournament.",
#    "none",
#    [
#      (call_script, "script_get_num_tournament_participants"),
#      (store_sub, ":needed_to_remove_randomly", reg0, 1),
#      (try_begin),
#        (troop_slot_eq, "trp_tournament_participants", 0, 0), #delete player from the participants
#        (troop_set_slot, "trp_tournament_participants", 0, -1),
#        (val_sub, ":needed_to_remove_randomly", 1),
#      (try_end),
#        (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
#        (call_script, "script_sort_tournament_participant_troops"),
#        (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
#        (str_store_troop_name, s1, ":winner_troop"),
#        (try_begin),
#          (troop_is_hero, ":winner_troop"),
#          (call_script, "script_change_troop_renown", ":winner_troop", 20),
#        (try_end),
#        (troop_get_type, reg3, ":winner_troop"),
#        ],
#    [
#      ("continue", [], "Continue...",
#       [(jump_to_menu, "mnu_town"),
#        ]),
#    ]
#  ),
#
#  (
#    "town_tournament",mnf_disable_all_keys,
#    "{s1}You are at tier {reg0} of the tournament, with {reg1} participants remaining. In the next round, there will be {reg2} teams with {reg3} {reg4?fighters:fighter} each.",
#    "none",
#    [
#        (party_set_slot, "$current_town", slot_town_has_tournament, 0), #No way to return back if this menu is left
#        (call_script, "script_sort_tournament_participant_troops"),#Moving trp_player to the top of the list
#        (call_script, "script_get_num_tournament_participants"),
#        (assign, ":num_participants", reg0),
#        (try_begin),
#          (neg|troop_slot_eq, "trp_tournament_participants", 0, 0),#Player is defeated
#
#          (assign, ":player_odds_add", 0),
#          (store_div, ":player_odds_add", "$g_tournament_bet_placed", 5),
#          (party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
#          (val_add, ":player_odds", ":player_odds_add"),
#          (val_min, ":player_odds", 4000),
#          (party_set_slot, "$current_town", slot_town_player_odds, ":player_odds"),
#
#          (jump_to_menu, "mnu_town_tournament_lost"),
#        (else_try),
#          (eq, ":num_participants", 1),#Tournament won
#          (jump_to_menu, "mnu_town_tournament_won"),
#        (else_try),
#          (try_begin),
#            (le, "$g_tournament_next_num_teams", 0),
#            (call_script, "script_get_random_tournament_team_amount_and_size"),
#            (assign, "$g_tournament_next_num_teams", reg0),
#            (assign, "$g_tournament_next_team_size", reg1),
#          (try_end),
#          (assign, reg2, "$g_tournament_next_num_teams"),
#          (assign, reg3, "$g_tournament_next_team_size"),
#          (store_sub, reg4, reg3, 1),
#          (str_clear, s1),
#          (try_begin),
#            (eq, "$g_tournament_player_team_won", 1),
#            (str_store_string, s1, "@Victory is yours! You have won this melee, but now you must prepare yourself for the next round. "),
#          (else_try),
#            (eq, "$g_tournament_player_team_won", 0),
#            (str_store_string, s1, "@You have been bested in this melee, but the master of ceremonies declares a recognition of your skill and bravery, allowing you to take part in the next round. "),
#          (try_end),
#          (assign, reg1, ":num_participants"),
#          (store_add, reg0, "$g_tournament_cur_tier", 1),
#        (try_end),
#        ],
#    [
#      ("tournament_view_participants", [], "View participants.",
#       [(jump_to_menu, "mnu_tournament_participants"),
#        ]),
#      ("tournament_bet", [(neq, "$g_tournament_cur_tier", "$g_tournament_last_bet_tier")], "Place a bet on yourself.",
#       [(jump_to_menu, "mnu_tournament_bet"),
#        ]),
#      ("tournament_join_next_fight", [], "Fight in the next round.",
#       [
#           (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
#           (modify_visitors_at_site, ":arena_scene"),
#           (reset_visitors),
#           #Assuming that there are enough participants for the teams
#		   (assign, "$g_player_tournament_placement", "$g_tournament_cur_tier"),
#		   (try_begin),
#		     (gt, "$g_player_tournament_placement", 4),
#		     (assign, "$g_player_eligible_feast_center_no", "$current_town"),
#		   (try_end),
#           (val_add, "$g_tournament_cur_tier", 1),
#		   
#           (store_mul, "$g_tournament_num_participants_for_fight", "$g_tournament_next_num_teams", "$g_tournament_next_team_size"),
#           (troop_set_slot, "trp_tournament_participants", 0, -1),#Removing trp_player from the list
#           (troop_set_slot, "trp_temp_array_a", 0, "trp_player"),
#           (try_for_range, ":slot_no", 1, "$g_tournament_num_participants_for_fight"),
#             (call_script, "script_get_random_tournament_participant"),
#             (troop_set_slot, "trp_temp_array_a", ":slot_no", reg0),
#           (try_end),
#           (call_script, "script_shuffle_troop_slots", "trp_temp_array_a", 0, "$g_tournament_num_participants_for_fight"),
#
#
#           (try_for_range, ":slot_no", 0, 4),#shuffle teams
#             (troop_set_slot, "trp_temp_array_b", ":slot_no", ":slot_no"),
#           (try_end),
#           (call_script, "script_shuffle_troop_slots", "trp_temp_array_b", 0, 4),
#
#           (assign, ":cur_slot", 0),
#           (try_for_range, ":cur_team_offset", 0, "$g_tournament_next_num_teams"),
#             (troop_get_slot, ":cur_team", "trp_temp_array_b", ":cur_team_offset"),
#           
#             (try_for_range, ":slot_no", 0, 8),#shuffle entry_points
#               (troop_set_slot, "trp_temp_array_c", ":slot_no", ":slot_no"),
#             (try_end),
#             (call_script, "script_shuffle_troop_slots", "trp_temp_array_c", 0, 8),
#           
#             (try_for_range, ":cur_index", 0, "$g_tournament_next_team_size"),
#               (store_mul, ":cur_entry_point", ":cur_team", 8),
#               (troop_get_slot, ":entry_offset", "trp_temp_array_c", ":cur_index"),
#               (val_add, ":cur_entry_point", ":entry_offset"),
#               (troop_get_slot, ":troop_no", "trp_temp_array_a", ":cur_slot"),
#               (set_visitor, ":cur_entry_point", ":troop_no"),
#               (val_add, ":cur_slot", 1),
#             (try_end),
#           (try_end),
#
#           (assign, "$g_tournament_next_num_teams", 0),
#           (assign, "$g_tournament_next_team_size", 0),
#           
#           (assign, "$g_mt_mode", abm_tournament),
#
#           (party_get_slot, ":town_original_faction", "$current_town", slot_center_original_faction),
#           (assign, ":town_index_within_faction", 0),
#           (assign, ":end_cond", towns_end),
#           (try_for_range, ":cur_town", towns_begin, ":end_cond"),
#             (try_begin),
#               (eq, ":cur_town", "$current_town"),
#               (assign, ":end_cond", 0), #break
#             (else_try),
#               (party_slot_eq, ":cur_town", slot_center_original_faction, ":town_original_faction"),
#               (val_add, ":town_index_within_faction", 1),
#             (try_end),
#           (try_end),
#           
#           (set_jump_mission, "mt_arena_melee_fight"),
#           
#           (try_begin),
#             (eq, ":town_original_faction", "fac_kingdom_1"),
#             #Swadia
#             (store_mod, ":mod", ":town_index_within_faction", 4),
#             (try_begin),
#               (eq, ":mod", 0),
#               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
#            (else_try),
#               (eq, ":mod", 1),
#               (call_script, "script_set_items_for_tournament", 100, 100, 0, 0, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
#             (else_try),
#               (eq, ":mod", 2),
#               (call_script, "script_set_items_for_tournament", 100, 0, 100, 0, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
#             (else_try),
#               (eq, ":mod", 3),
#               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 40, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
#             (try_end),
#           (else_try),
#             (eq, ":town_original_faction", "fac_kingdom_2"),
#             #Vaegirs
#             (store_mod, ":mod", ":town_index_within_faction", 4),
#             (try_begin),
#               (eq, ":mod", 0),
#               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 0, 0, 0, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
#             (else_try),
#               (eq, ":mod", 1),
#               (call_script, "script_set_items_for_tournament", 100, 50, 0, 0, 0, 20, 30, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
#             (else_try),
#               (eq, ":mod", 2),
#               (call_script, "script_set_items_for_tournament", 100, 0, 50, 0, 0, 20, 30, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
#             (else_try),
#               (eq, ":mod", 3),
#               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 30, 0, 60, 0, "itm_arena_armor_red", "itm_steppe_helmet_red"),
#             (try_end),
#           (else_try),
#             (eq, ":town_original_faction", "fac_kingdom_3"),
#             #Khergit
#             (store_mod, ":mod", ":town_index_within_faction", 2),
#             (try_begin),
#               (eq, ":mod", 0),
#               (call_script, "script_set_items_for_tournament", 100, 0, 0, 0, 0, 40, 60, 0, "itm_arena_tunic_red", "itm_steppe_helmet_red"),
#             (else_try),
#               (eq, ":mod", 1),
#               (call_script, "script_set_items_for_tournament", 100, 50, 25, 0, 0, 30, 50, 0, "itm_arena_tunic_red", "itm_steppe_helmet_red"),
#             (try_end),
#           (else_try),
#             (eq, ":town_original_faction", "fac_kingdom_4"),
#             #Nords
#             (store_mod, ":mod", ":town_index_within_faction", 3),
#             (try_begin),
#               (eq, ":mod", 0),
#               (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 0, 0, 0, 0, "itm_arena_armor_red", -1),
#             (else_try),
#               (eq, ":mod", 1),
#               (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 50, 0, 0, 0, "itm_arena_armor_red", -1),
#             (else_try),
#               (eq, ":mod", 2),
#               (call_script, "script_set_items_for_tournament", 40, 0, 0, 100, 0, 0, 0, 0, "itm_arena_armor_red", -1),
#             (try_end),
#           (else_try),
#             #Rhodoks
#             (eq, ":town_original_faction", "fac_kingdom_5"),
#             (call_script, "script_set_items_for_tournament", 25, 100, 60, 0, 30, 0, 30, 50, "itm_arena_tunic_red", "itm_arena_helmet_red"),
#           (else_try),
#             #Sarranids
#             (store_mod, ":mod", ":town_index_within_faction", 2),
#             (try_begin),
#               (eq, ":mod", 0),
#               (call_script, "script_set_items_for_tournament", 100, 40, 60, 0, 30, 30, 0, 0, "itm_arena_tunic_red", "itm_arena_turban_red"),
#            (else_try),
#              (call_script, "script_set_items_for_tournament", 50, 0, 60, 0, 30, 30, 0, 0, "itm_arena_tunic_red", "itm_arena_turban_red"),
#            (try_end),
#          (try_end),
#          (jump_to_scene, ":arena_scene"),
#          (change_screen_mission),
#       ]),
#     ("leave_tournament",[],"Withdraw from the tournament.",
#       [
#           (jump_to_menu, "mnu_tournament_withdraw_verify"),
#        ]),
#    ]
#  ),
#
#  (
#    "tournament_withdraw_verify",0,
#    "Are you sure you want to withdraw from the tournament?",
#    "none",
#    [],
#    [
#      ("tournament_withdraw_yes", [], "Yes. This is a pointless affectation.",
#       [(jump_to_menu, "mnu_town_tournament_won_by_another"),
#        ]),
#      ("tournament_withdraw_no", [], "No, not as long as there is a chance of victory!",
#       [(jump_to_menu, "mnu_town_tournament"),
#        ]),
#    ]
#  ),
#
#  (
#    "tournament_bet",0,
#    "The odds against you are {reg5} to {reg6}.{reg1? You have already bet {reg1} denars on yourself, and if you win, you will earn {reg2} denars.:} How much do you want to bet?",
#    "none",
#    [
#      (assign, reg1, "$g_tournament_bet_placed"),
#      (store_add, reg2, "$g_tournament_bet_win_amount", "$g_tournament_bet_placed"),
#      (call_script, "script_get_win_amount_for_tournament_bet"),
#      (assign, ":player_odds", reg0),
#      (assign, ":min_dif", 100000),
#      (assign, ":min_dif_divisor", 1),
#      (assign, ":min_dif_multiplier", 1),
#      (try_for_range, ":cur_multiplier", 1, 50),
#        (try_for_range, ":cur_divisor", 1, 50),
#          (store_mul, ":result", 100, ":cur_multiplier"),
#          (val_div, ":result", ":cur_divisor"),
#          (store_sub, ":difference", ":player_odds", ":result"),
#          (val_abs, ":difference"),
#          (lt, ":difference", ":min_dif"),
#          (assign, ":min_dif", ":difference"),
#          (assign, ":min_dif_divisor", ":cur_divisor"),
#          (assign, ":min_dif_multiplier", ":cur_multiplier"),
#        (try_end),
#      (try_end),
#      (assign, reg5, ":min_dif_multiplier"),
#      (assign, reg6, ":min_dif_divisor"),
#      ],
#    [
#      ("bet_100_denars", [(store_troop_gold, ":gold", "trp_player"),
#                          (ge, ":gold", 100)
#                          ],
#       "100 denars.",
#       [
#         (assign, "$temp", 100),
#         (jump_to_menu, "mnu_tournament_bet_confirm"),
#        ]),
#      ("bet_50_denars", [(store_troop_gold, ":gold", "trp_player"),
#                         (ge, ":gold", 50)
#                         ],
#       "50 denars.",
#       [
#         (assign, "$temp", 50),
#         (jump_to_menu, "mnu_tournament_bet_confirm"),
#        ]),
#      ("bet_20_denars", [(store_troop_gold, ":gold", "trp_player"),
#                         (ge, ":gold", 20)
#                         ],
#       "20 denars.",
#       [
#         (assign, "$temp", 20),
#         (jump_to_menu, "mnu_tournament_bet_confirm"),
#        ]),
#      ("bet_10_denars", [(store_troop_gold, ":gold", "trp_player"),
#                         (ge, ":gold", 10)
#                         ],
#       "10 denars.",
#       [
#         (assign, "$temp", 10),
#         (jump_to_menu, "mnu_tournament_bet_confirm"),
#        ]),
#      ("bet_5_denars", [(store_troop_gold, ":gold", "trp_player"),
#                        (ge, ":gold", 5)
#                        ],
#       "5 denars.",
#       [
#         (assign, "$temp", 5),
#         (jump_to_menu, "mnu_tournament_bet_confirm"),
#        ]),
#      ("go_back_dot", [], "Go back.",
#       [
#         (jump_to_menu, "mnu_town_tournament"),
#        ]),
#    ]
#  ),
#
#  (
#    "tournament_bet_confirm",0,
#    "If you bet {reg1} denars, you will earn {reg2} denars if you win the tournament. Is that all right?",
#    "none",
#    [
#      (call_script, "script_get_win_amount_for_tournament_bet"),
#      (assign, ":win_amount", reg0),
#      (val_mul, ":win_amount", "$temp"),
#      (val_div, ":win_amount", 100),
#      (assign, reg1, "$temp"),
#      (assign, reg2, ":win_amount"),
#      ],
#    [
#      ("tournament_bet_accept", [],
#       "Go ahead.",
#       [
#         (call_script, "script_tournament_place_bet", "$temp"),
#         (jump_to_menu, "mnu_town_tournament"),
#         ]),
#      ("tournament_bet_cancel", [],
#       "Forget it.",
#       [
#         (jump_to_menu, "mnu_tournament_bet"),
#         ]),
#    ]
#  ),
#  
#  (
#    "tournament_participants",0,
#    "You ask one of the criers for the names of the tournament participants. They are:^{s11}",
#    "none",
#    [
#        (str_clear, s11),
#        (call_script, "script_sort_tournament_participant_troops"),
#        (call_script, "script_get_num_tournament_participants"),
#        (assign, ":num_participants", reg0),
#        (try_for_range, ":cur_slot", 0, ":num_participants"),
#          (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
#          (str_store_troop_name, s12, ":troop_no"),
#          (str_store_string, s11, "@{!}{s11}^{s12}"),
#        (try_end),
#        ],
#    [
#      ("go_back_dot", [], "Go back.",
#       [(jump_to_menu, "mnu_town_tournament"),
#        ]),
#    ]
#  ),


# They must learn field discipline and the steadiness to follow orders in combat before they can be thought to use arms.",
  (
    "train_peasants_against_bandits",0,
    "As the party member with the highest training skill ({reg2}), {reg3?you expect:{s1} expects} that getting some peasants ready for practice will take {reg4} hours.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
     (assign, ":max_skill", reg0),
     (assign, reg2, reg0),
     (assign, ":max_skill_owner", reg1),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (store_sub, ":needed_hours", 20, ":max_skill"),
     (val_mul, ":needed_hours", 3),
     (val_div, ":needed_hours", 5),
     (store_sub, reg4, ":needed_hours", "$qst_train_peasants_against_bandits_num_hours_trained"),
     ],
    [
      ("make_preparation", [], "Train them.",
       [
         (assign, "$qst_train_peasants_against_bandits_currently_training", 1),
         (rest_for_hours_interactive, 1000, 5, 0), #rest while not attackable
         (assign, "$auto_enter_town", "$current_town"),
         (assign, "$g_town_visit_after_rest", 1),
         (change_screen_return),
         ]),
      ("train_later", [], "Put it off until later.",
       [
         (jump_to_menu, "mnu_village"),
        ]),
    ]
  ), 

  (
    "train_peasants_against_bandits_ready",0,
    "You put the peasants through the basics of soldiering, discipline and obedience.\
 You think {reg0} of them {reg1?have:has} fully grasped the training and {reg1?are:is} ready for some practice.",
    "none",
    [
      (store_character_level, ":level", "trp_player"),
      (val_div, ":level", 10),
      (val_add, ":level", 1),
      (quest_get_slot, ":quest_target_amount", "qst_train_peasants_against_bandits", slot_quest_target_amount),
      (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
      (val_sub, ":quest_target_amount", ":quest_current_state"),
      (assign, ":max_random", ":level"),
      (val_min, ":max_random", ":quest_target_amount"),
      (val_add, ":max_random", 1),
      (store_random_in_range, ":random_number", 1, ":max_random"),
      (assign, "$g_train_peasants_against_bandits_num_peasants", ":random_number"),
      (assign, reg0, ":random_number"),
      (store_sub, reg1, ":random_number", 1),
      (str_store_troop_name_by_count, s0, "trp_trainee_peasant", ":random_number"),
     ],
    [
      ("peasant_start_practice", [], "Start the practice fight.",
       [
         (set_jump_mission,"mt_village_training"),
         (quest_get_slot, ":target_center", "qst_train_peasants_against_bandits", slot_quest_target_center),
         (party_get_slot, ":village_scene", ":target_center", slot_castle_exterior),
         (modify_visitors_at_site, ":village_scene"),
         (reset_visitors),
         (set_visitor, 0, "trp_player"),
         (set_visitors, 1, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
         (set_jump_entry, 11),
         (jump_to_scene, ":village_scene"),
         (jump_to_menu, "mnu_train_peasants_against_bandits_training_result"),
         (music_set_situation, 0),
         (change_screen_mission),
         ]),
      ]
    ),

  (
    "train_peasants_against_bandits_training_result",mnf_disable_all_keys,
    "{s0}",
    "none",
    [
      (assign, reg5, "$g_train_peasants_against_bandits_num_peasants"),
      (str_store_troop_name_by_count, s0, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
      (try_begin),
        (eq, "$g_train_peasants_against_bandits_training_succeeded", 0),
        (str_store_string, s0, "@You were beaten. The peasants are heartened by their success, but the lesson you wanted to teach them probably didn't get through..."),
      (else_try),
        (str_store_string, s0, "@After beating your last opponent, you explain to the peasants how to better defend themselves against such an attack. Hopefully they'll take the experience on board and will be prepared next time."),
        (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
        (val_add, ":quest_current_state", "$g_train_peasants_against_bandits_num_peasants"),
        (quest_set_slot, "qst_train_peasants_against_bandits", slot_quest_current_state, ":quest_current_state"),
      (try_end),
     ],
    [
      ("continue", [], "Continue...",
       [
         (try_begin),
           (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
           (quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_amount, ":quest_current_state"),
           (jump_to_menu, "mnu_train_peasants_against_bandits_attack"),
         (else_try),
           (change_screen_map),
         (try_end),
         ]),
      ]
    ),

  (
    "train_peasants_against_bandits_attack",0,
    "As you get ready to continue the training, a sentry from the village runs up to you, shouting alarums.\
 The bandits have been spotted on the horizon, riding hard for {s3}.\
 The elder begs that you organize your newly-trained militia and face them.",
    "none",
    [
	(str_store_party_name, s3, "$current_town"),
     ],
    [
      ("peasants_against_bandits_attack_resist", [], "Prepare for a fight!",
       [
        (store_random_in_range, ":random_no", 0, 3),
        (try_begin),
          (eq, ":random_no", 0),
          (assign, ":bandit_troop", "trp_bandit"),
        (else_try),
          (eq, ":random_no", 1),
          (assign, ":bandit_troop", "trp_mountain_bandit"),
        (else_try),
          (assign, ":bandit_troop", "trp_forest_bandit"),
        (try_end),
        (party_get_slot, ":scene_to_use", "$g_encountered_party", slot_castle_exterior),
        (modify_visitors_at_site, ":scene_to_use"),
        (reset_visitors),
        (store_character_level, ":level", "trp_player"),
        (val_div, ":level", 2),
        (store_add, ":min_bandits", ":level", 16),
        (store_add, ":max_bandits", ":min_bandits", 6),
        (store_random_in_range, ":random_no", ":min_bandits", ":max_bandits"),
        (set_visitors, 0, ":bandit_troop", ":random_no"),
        (assign, ":num_villagers", ":max_bandits"),
        (set_visitors, 2, "trp_trainee_peasant", ":num_villagers"),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission,"mt_village_attack_bandits"),
        (jump_to_scene, ":scene_to_use"),
        (assign, "$g_next_menu", "mnu_train_peasants_against_bandits_attack_result"),
#        (jump_to_menu, "mnu_battle_debrief"),
        (assign, "$g_mt_mode", vba_after_training),
        (change_screen_mission),
        ]),
      ]
    ),

  (
    "train_peasants_against_bandits_attack_result",mnf_scale_picture|mnf_disable_all_keys,
    "{s9}",
    "none",
    [
      (try_begin),
        (eq, "$g_battle_result", 1),
        (str_store_string, s9, "@The bandits are broken!\
 Those few who remain alive and conscious run off with their tails between their legs,\
 terrified of the peasants and their new champion."),
	(call_script, "script_succeed_quest", "qst_train_peasants_against_bandits"),
        (jump_to_menu, "mnu_train_peasants_against_bandits_success"),
      (else_try),
        (call_script, "script_fail_quest", "qst_train_peasants_against_bandits"),
        (str_store_string, s9, "@Try as you might, you could not defeat the bandits.\
 Infuriated, they raze the village to the ground to punish the peasants,\
 and then leave the burning wasteland behind to find greener pastures to plunder."),
        (set_background_mesh, "mesh_pic_looted_village"),
      (try_end),
     ],
    [
      ("continue", [], "Continue...",
       [(try_begin),
          (call_script, "script_village_set_state",  "$current_town", svs_looted),
          (party_set_slot, "$current_town", slot_village_raid_progress, 0),
          (party_set_slot, "$current_town", slot_village_recover_progress, 0),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
          (call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
        (try_end),
        (change_screen_map),
	 ]),
      ]
    ),

   (
    "train_peasants_against_bandits_success",mnf_disable_all_keys,
    "The bandits are broken!\
 Those few who remain run off with their tails between their legs,\
 terrified of the peasants and their new champion.\
 The villagers have little left in the way of wealth after their ordeal,\
 but they offer you all they can find to show their gratitude.",
    "none",
    [(party_clear, "p_temp_party"),
     (call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
     (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 4),

     (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
     (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 50),
        (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
     (try_end),
     (call_script, "script_add_log_entry", logent_helped_peasants, "trp_player",  "$current_town", -1, -1),
    ],
    [
      ("village_bandits_defeated_accept",[],"Take it as your just due.",[(jump_to_menu, "mnu_auto_return_to_map"),
                                                                         (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
                                                                         (troop_sort_inventory, ":merchant_troop"),
                                                                         (change_screen_loot, ":merchant_troop"),
                                                                       ]),
      ("village_bandits_defeated_cont",[],  "Refuse, stating that they need these items more than you do.",[
	  (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
      (call_script, "script_change_player_honor", 1),
      (change_screen_map)]),
    ],
  ),


  (
    "disembark",0,
    "Do you wish to disembark?",
    "none",
    [],
    [
      ("disembark_yes", [], "Yes.",
       [(assign, "$g_player_icon_state", pis_normal),
        (party_set_flags, "p_main_party", pf_is_ship, 0),
        (party_get_position, pos1, "p_main_party"),
        (party_set_position, "p_main_party", pos0),
        (try_begin),
          (le, "$g_main_ship_party", 0),
          (set_spawn_radius, 0),
          (spawn_around_party, "p_main_party", "pt_none"),
          (assign, "$g_main_ship_party", reg0),          
          (party_set_flags, "$g_main_ship_party", pf_is_static|pf_always_visible|pf_hide_defenders|pf_is_ship, 1),
          (str_store_troop_name, s1, "trp_player"),
          (party_set_name, "$g_main_ship_party", "@{s1}'s Ship"),
          (party_set_icon, "$g_main_ship_party", "icon_ship"),
          (party_set_slot, "$g_main_ship_party", slot_party_type, spt_ship),
        (try_end),
        (enable_party, "$g_main_ship_party"),
        (party_set_position, "$g_main_ship_party", pos0),
        (party_set_icon, "$g_main_ship_party", "icon_ship_on_land"),
        (assign, "$g_main_ship_party", -1),
        (change_screen_return),
        ]),
      ("disembark_no", [], "No.",
       [(change_screen_return),
        ]),
    ]
  ),

  (
    "ship_reembark",0,
    "Do you wish to embark?",
    "none",
    [],
    [
      ("reembark_yes", [], "Yes.",
       [(assign, "$g_player_icon_state", pis_ship),
        (party_set_flags, "p_main_party", pf_is_ship, 1),
        (party_get_position, pos1, "p_main_party"),
        (map_get_water_position_around_position, pos2, pos1, 6),
        (party_set_position, "p_main_party", pos2),
        (assign, "$g_main_ship_party", "$g_encountered_party"),
        (disable_party, "$g_encountered_party"),
        (change_screen_return),
        ]),
      ("reembark_no", [], "No.",
       [(change_screen_return),
        ]),
    ]
  ),

  (
    "center_reports",0,
    "Town Name: {s1}^Rent Income: {reg1} denars^Tariff Income: {reg2} denars^Food Stock: for {reg3} days",
    "none",
    [(party_get_slot, ":town_food_store", "$g_encountered_party", slot_party_food_store),
     (call_script, "script_center_get_food_consumption", "$g_encountered_party"),
     (assign, ":food_consumption", reg0),
     (try_begin),
       (gt, ":food_consumption", 0),
       (store_div, reg3, ":town_food_store", ":food_consumption"),
     (else_try),
       (assign, reg3, 9999),
     (try_end),
     (str_store_party_name, s1, "$g_encountered_party"),
     (party_get_slot, reg1, "$g_encountered_party", slot_center_accumulated_rents),
     (party_get_slot, reg2, "$g_encountered_party", slot_center_accumulated_tariffs),
     ],
    [
      ("to_price_and_productions", [], "Show prices and productions.",
       [(jump_to_menu, "mnu_price_and_production"),
        ]),
      
      ("go_back_dot",[],"Go back.",
       [(try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_town"),
        (try_end),
        ]),
    ]
  ),
    
  (
    "price_and_production",0,
    "Productions are:^(Note: base/modified by raw materials/modified by materials plus prosperity)^{s1}^^Price factors are:^{s2}",
    "none",
    [
	
	 (assign, ":calradian_average_urban_hardship", 0),
	 (assign, ":calradian_average_rural_hardship", 0),

	 (try_for_range, ":center", towns_begin, towns_end),
		(call_script, "script_center_get_goods_availability", ":center"),
		(val_add, ":calradian_average_urban_hardship", reg0),
	 (try_end),

	 (try_for_range, ":center", villages_begin, villages_end),
		(call_script, "script_center_get_goods_availability", ":center"),
		(val_add, ":calradian_average_rural_hardship", reg0),
	 (try_end),	
	   
	 (val_div, ":calradian_average_rural_hardship", 110),
	 (val_div, ":calradian_average_urban_hardship", 22),


	   
	 (call_script, "script_center_get_goods_availability", "$g_encountered_party"),

	 (assign, reg1, ":calradian_average_urban_hardship"),
	 (assign, reg2, ":calradian_average_rural_hardship"),	      

	 (try_begin),
		(ge, "$cheat_mode", 1),
		(str_store_string, s1, "str___hardship_index_reg0_avg_towns_reg1_avg_villages_reg2__"),
		(display_message, "@{!}DEBUG - {s1}"),
	 (try_end),
	 
	 
     (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
	   (neq, ":cur_good", "itm_pork"), #tied to price of grain
	   (neq, ":cur_good", "itm_chicken"), #tied to price of grain
	   (neq, ":cur_good", "itm_butter"), #tied to price of cheese
	   (neq, ":cur_good", "itm_cattle_meat"),
	   (neq, ":cur_good", "itm_cabbages"), #possibly include later
	 
	   (call_script, "script_center_get_production", "$g_encountered_party", ":cur_good"),
	   (assign, ":production", reg0),
	   (assign, ":base_production", reg2),
	   (assign, ":base_production_modded_by_raw_materials", reg1),

	   (call_script, "script_center_get_consumption", "$g_encountered_party", ":cur_good"),
	   (assign, ":consumer_consumption", reg2),
	   (assign, ":raw_material_consumption", reg1),
	   (assign, ":consumption", reg0),

       (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
       (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
       (party_get_slot, ":price", "$g_encountered_party", ":cur_good_price_slot"),
	   	   
	   (assign, ":total_centers", 0),
	   (assign, ":calradian_average_price", 0),
	   (assign, ":calradian_average_production", 0),
	   (assign, ":calradian_average_consumption", 0),
	   
	   (try_for_range, ":center", centers_begin, centers_end),
		(neg|is_between, ":center", castles_begin, castles_end),
	    (val_add, ":total_centers", 1),
        (call_script, "script_center_get_production", ":center", ":cur_good"),
		(assign, ":center_production", reg2),
        (call_script, "script_center_get_consumption", ":center", ":cur_good"),
		(store_add, ":center_consumption", reg1, reg2),
		
        (party_get_slot, ":center_price", ":center", ":cur_good_price_slot"),
	    (val_add, ":calradian_average_price", ":center_price"),
	    (val_add, ":calradian_average_production", ":center_production"),
	    (val_add, ":calradian_average_consumption", ":center_consumption"),
	   (try_end),

	   (assign, ":calradian_total_production", ":calradian_average_production"),
	   (assign, ":calradian_total_consumption", ":calradian_average_consumption"),
	   
	   (val_div, ":calradian_average_price", ":total_centers"),
	   (val_div, ":calradian_average_production", ":total_centers"),
	   (val_div, ":calradian_average_consumption", ":total_centers"),


       (str_store_item_name, s3, ":cur_good"),
	   
       (assign, reg1, ":base_production"),
       (assign, reg2, ":base_production_modded_by_raw_materials"),
       (assign, reg3, ":production"),
       (assign, reg4, ":price"),
	   
	   (assign, reg5, ":calradian_average_production"),
	   (assign, reg6, ":calradian_average_price"),

	   (assign, reg7, ":consumer_consumption"),
	   (assign, reg8, ":raw_material_consumption"),
	   (assign, reg9, ":consumption"),

	   (assign, reg10, ":calradian_average_consumption"),

	   (item_get_slot, ":production_slot", ":cur_good", slot_item_production_slot),
	   (party_get_slot, ":production_number", "$g_encountered_party", ":production_slot"),
	   (assign, reg11, ":production_number"),
	   (assign, reg12, ":calradian_total_production"),
	   (assign, reg13, ":calradian_total_consumption"),
	   
	   (item_get_slot, ":production_string", ":cur_good", slot_item_production_string),
	   (str_store_string, s4, ":production_string"),
	   
       (str_store_string, s1, "str___s3_price_=_reg4_calradian_average_reg6_capital_reg11_s4_base_reg1modified_by_raw_material_reg2modified_by_prosperity_reg3_calradian_average_production_base_reg5_total_reg12_consumed_reg7used_as_raw_material_reg8modified_total_reg9_calradian_consumption_base_reg10_total_reg13s1_"),	   	   
     (try_end),
	 
	 
     ],
    [
      ("go_back_dot",[],"Go back.",
       [(try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_town"),
        (try_end),
        ]),
    ]
  ),
  
  (
    "town_trade",0,
    "You head towards the marketplace.",
    "none",
    [],
    [
      ("assess_prices",
       [
         (store_faction_of_party, ":current_town_faction", "$current_town"),
         (store_relation, ":reln", ":current_town_faction", "fac_player_supporters_faction"),
         (ge, ":reln", 0),
         ],
       "Assess the local prices.",
       [
           (jump_to_menu,"mnu_town_trade_assessment_begin"),
        ]),
      ("trade_with_arms_merchant",[(party_slot_ge, "$current_town", slot_town_weaponsmith, 1)],
       "Trade with the arms merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_weaponsmith),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_armor_merchant",[(party_slot_ge, "$current_town", slot_town_armorer, 1)],
       "Trade with the armor merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_armorer),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_horse_merchant",[(party_slot_ge, "$current_town", slot_town_horse_merchant, 1)],
       "Trade with the horse merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_horse_merchant),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_goods_merchant",[(party_slot_ge, "$current_town", slot_town_merchant, 1)],
       "Trade with the goods merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_town_merchant),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("back_to_town_menu",[],"Head back.",
       [
           (jump_to_menu,"mnu_town"),
        ]),
    ]
  ),

  (
   "town_trade_assessment_begin",0, 
   #"You overhear the following details about the roads out of town :^(experimental feature -- this may go into dialogs)^{s42}^You also overhear several discussions about the price of trade goods across the local area.^You listen closely, trying to work out the best deals around.",
   "You overhear several discussions about the price of trade goods across the local area.^You listen closely, trying to work out the best deals around.",
    "none",
    [
	(str_clear, s42),
##	(call_script, "script_merchant_road_info_to_s42", "$g_encountered_party"),
	
    ],

    [
      ("continue",[],"Continue...",
       [
           (assign,"$auto_enter_town", "$current_town"),
           (assign, "$g_town_assess_trade_goods_after_rest", 1),
           (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
           (val_div, reg0, 2),
           (store_sub, ":num_hours", 6, reg0),
           (assign, "$g_last_rest_center", "$current_town"),
           (assign, "$g_last_rest_payment_until", -1),
           (rest_for_hours, ":num_hours", 5, 0), #rest while not attackable
           (change_screen_return),
        ]),
      ("go_back_dot",[],"Go back.",
       [
           (jump_to_menu,"mnu_town_trade"),
        ]),
    ]
  ),

  (
    "town_trade_assessment",mnf_disable_all_keys,
    "As the party member with the highest trade skill ({reg2}), {reg3?you try to figure out:{s1} tries to figure out} the best goods to trade in. {s2}",
    "none",
    [

(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),

     (assign, ":num_best_results", 0),
     (assign, ":best_result_1_item", -1),
     (assign, ":best_result_1_town", -1),
     (assign, ":best_result_1_profit", 0),
     (assign, ":best_result_2_item", -1),
     (assign, ":best_result_2_town", -1),
     (assign, ":best_result_2_profit", 0),
     (assign, ":best_result_3_item", -1),
     (assign, ":best_result_3_town", -1),
     (assign, ":best_result_3_profit", 0),
     (assign, ":best_result_4_item", -1),
     (assign, ":best_result_4_town", -1),
     (assign, ":best_result_4_profit", 0),
     (assign, ":best_result_5_item", -1),
     (assign, ":best_result_5_town", -1),
     (assign, ":best_result_5_profit", 0),

     (store_sub, ":num_towns", walled_centers_end, walled_centers_begin),
     (store_sub, ":num_goods", trade_goods_end, trade_goods_begin),
     (store_mul, ":max_iteration", ":num_towns", ":num_goods"),
     (val_mul, ":max_iteration", ":max_skill"),
     (val_div, ":max_iteration", 20),

     (assign, ":org_encountered_party", "$g_encountered_party"),

     (try_for_range, ":unused", 0, ":max_iteration"),
       (store_random_in_range, ":random_trade_good", trade_goods_begin, trade_goods_end),

       (store_random_in_range, ":random_town", towns_begin, towns_end),

       (party_get_slot, ":cur_merchant", ":org_encountered_party", slot_town_merchant),       
	   (assign, ":num_items_in_town_inventory", 0),
       (try_for_range, ":i_slot", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
         (troop_get_inventory_slot, ":slot_item", ":cur_merchant", ":i_slot"),
         (try_begin),
           (eq, ":slot_item", ":random_trade_good"),           
		   (val_add, ":num_items_in_town_inventory", 1),
         (try_end),
       (try_end),

       (ge, ":num_items_in_town_inventory", 1),

       (assign, ":already_best", 0),
       
	   (try_begin),
         (eq, ":random_trade_good", ":best_result_1_item"),
         (eq, ":random_town", ":best_result_1_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_2_item"),
         (eq, ":random_town", ":best_result_2_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_3_item"),
         (eq, ":random_town", ":best_result_3_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_4_item"),
         (eq, ":random_town", ":best_result_4_town"),
         (val_add, ":already_best", 1),
       (try_end),

	   (try_begin),
         (eq, ":random_trade_good", ":best_result_5_item"),
         (eq, ":random_town", ":best_result_5_town"),
         (val_add, ":already_best", 1),
       (try_end),

       (le, ":already_best", 1),

       (store_item_value, ":random_trade_good_price", ":random_trade_good"),
       (assign, "$g_encountered_party", ":org_encountered_party"),
       (call_script, "script_game_get_item_buy_price_factor", ":random_trade_good"),
       (store_mul, ":random_trade_good_buy_price", ":random_trade_good_price", reg0),
       (val_div, ":random_trade_good_buy_price", 100),
       (val_max, ":random_trade_good_buy_price", 1),
       (assign, "$g_encountered_party", ":random_town"),
       (call_script, "script_game_get_item_sell_price_factor", ":random_trade_good"),
       (store_mul, ":random_trade_good_sell_price", ":random_trade_good_price", reg0),
       (val_div, ":random_trade_good_sell_price", 100),
       (val_max, ":random_trade_good_sell_price", 1),
       (store_sub, ":difference", ":random_trade_good_sell_price", ":random_trade_good_buy_price"),

       (try_begin),
	     (this_or_next|eq, ":best_result_1_item", ":random_trade_good"),
		 (this_or_next|eq, ":best_result_2_item", ":random_trade_good"),
		 (this_or_next|eq, ":best_result_3_item", ":random_trade_good"),
		 (this_or_next|eq, ":best_result_4_item", ":random_trade_good"),
		 (eq, ":best_result_5_item", ":random_trade_good"),

         (try_begin),
		   (eq, ":best_result_1_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_1_profit"),
           (assign, ":best_result_1_item", ":random_trade_good"),
           (assign, ":best_result_1_town", ":random_town"),
           (assign, ":best_result_1_profit", ":difference"),
         (else_try),
		   (eq, ":best_result_2_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_2_profit"),
           (assign, ":best_result_2_item", ":random_trade_good"),
           (assign, ":best_result_2_town", ":random_town"),
           (assign, ":best_result_2_profit", ":difference"),
		 (else_try),
		   (eq, ":best_result_3_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_3_profit"),
           (assign, ":best_result_3_item", ":random_trade_good"),
           (assign, ":best_result_3_town", ":random_town"),
           (assign, ":best_result_3_profit", ":difference"),
		 (else_try),
		   (eq, ":best_result_4_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":random_trade_good"),
           (assign, ":best_result_4_town", ":random_town"),
           (assign, ":best_result_4_profit", ":difference"),
		 (else_try),
		   (eq, ":best_result_5_item", ":random_trade_good"),
		   (gt, ":difference", ":best_result_5_profit"),
           (assign, ":best_result_5_item", ":random_trade_good"),
           (assign, ":best_result_5_town", ":random_town"),
           (assign, ":best_result_5_profit", ":difference"),
		 (try_end),
	   (else_try),
         (try_begin),
           (gt, ":difference", ":best_result_1_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":best_result_3_item"),
           (assign, ":best_result_4_town", ":best_result_3_town"),
           (assign, ":best_result_4_profit", ":best_result_3_profit"),
           (assign, ":best_result_3_item", ":best_result_2_item"),
           (assign, ":best_result_3_town", ":best_result_2_town"),
           (assign, ":best_result_3_profit", ":best_result_2_profit"),
           (assign, ":best_result_2_item", ":best_result_1_item"),
           (assign, ":best_result_2_town", ":best_result_1_town"),
           (assign, ":best_result_2_profit", ":best_result_1_profit"),
           (assign, ":best_result_1_item", ":random_trade_good"),
           (assign, ":best_result_1_town", ":random_town"),
           (assign, ":best_result_1_profit", ":difference"),
         (else_try),
           (gt, ":difference", ":best_result_2_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":best_result_3_item"),
           (assign, ":best_result_4_town", ":best_result_3_town"),
           (assign, ":best_result_4_profit", ":best_result_3_profit"),
           (assign, ":best_result_3_item", ":best_result_2_item"),
           (assign, ":best_result_3_town", ":best_result_2_town"),
           (assign, ":best_result_3_profit", ":best_result_2_profit"),
           (assign, ":best_result_2_item", ":random_trade_good"),
           (assign, ":best_result_2_town", ":random_town"),
           (assign, ":best_result_2_profit", ":difference"),
         (else_try),
           (gt, ":difference", ":best_result_3_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":best_result_3_item"),
           (assign, ":best_result_4_town", ":best_result_3_town"),
           (assign, ":best_result_4_profit", ":best_result_3_profit"),
           (assign, ":best_result_3_item", ":random_trade_good"),
           (assign, ":best_result_3_town", ":random_town"),
           (assign, ":best_result_3_profit", ":difference"),
         (else_try),
           (gt, ":difference", ":best_result_4_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
           (assign, ":best_result_4_item", ":random_trade_good"),
           (assign, ":best_result_4_town", ":random_town"),
           (assign, ":best_result_4_profit", ":difference"),
         (else_try),
           (gt, ":difference", ":best_result_5_profit"),
           (val_add, ":num_best_results", 1),
           (val_min, ":num_best_results", 5),
           (assign, ":best_result_5_item", ":best_result_4_item"),
           (assign, ":best_result_5_town", ":best_result_4_town"),
           (assign, ":best_result_5_profit", ":best_result_4_profit"),
         (try_end),
	   (try_end),
     (try_end),

     (assign, "$g_encountered_party", ":org_encountered_party"),

     (str_clear, s3),
     
     (assign, reg2, ":max_skill"),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (try_begin),
       (le, ":num_best_results", 0),
       (str_store_string, s2, "@However, {reg3?You are:{s1} is} unable to find any trade goods that would bring a profit."),
     (else_try),
       (try_begin),
         (ge, ":best_result_5_item", 0),
         (assign, reg6, ":best_result_5_profit"),
         (str_store_item_name, s4, ":best_result_5_item"),
         (str_store_party_name, s5, ":best_result_5_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_4_item", 0),
         (assign, reg6, ":best_result_4_profit"),
         (str_store_item_name, s4, ":best_result_4_item"),
         (str_store_party_name, s5, ":best_result_4_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_3_item", 0),
         (assign, reg6, ":best_result_3_profit"),
         (str_store_item_name, s4, ":best_result_3_item"),
         (str_store_party_name, s5, ":best_result_3_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_2_item", 0),
         (assign, reg6, ":best_result_2_profit"),
         (str_store_item_name, s4, ":best_result_2_item"),
         (str_store_party_name, s5, ":best_result_2_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_1_item", 0),
         (assign, reg6, ":best_result_1_profit"),
         (str_store_item_name, s4, ":best_result_1_item"),
         (str_store_party_name, s5, ":best_result_1_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} denars per item.{s3}"),
       (try_end), 
       (str_store_string, s2, "@{reg3?You find:{s1} finds} out the following:^{s3}"),
     (try_end),
     ],
    [
      ("continue",[],"Continue...",
       [
           (jump_to_menu,"mnu_town_trade"),
        ]),
    ]
  ),

  
  
  
  (
    "sneak_into_town_suceeded",0,
    "Disguised in the garments of a poor pilgrim, you fool the guards and make your way into the town.",
    "none",
    [],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$sneaked_into_town",1),
           (jump_to_menu,"mnu_town"),
        ]),
    ]
  ),
  (
    "sneak_into_town_caught",0,
    "As you try to sneak in, one of the guards recognizes you and raises the alarm!\
 You must flee back through the gates before all the guards in the town come down on you!",
    "none",
    [
#       (assign,"$auto_menu","mnu_captivity_start_castle_surrender"),
    ],
    [
      ("sneak_caught_fight",[],"Try to fight your way out!",
       [
           (assign,"$all_doors_locked",1),
           (party_get_slot, ":sneak_scene", "$current_town", slot_town_center), # slot_town_gate),
           (modify_visitors_at_site,":sneak_scene"),
           (reset_visitors),
           
           (try_begin),
             (this_or_next|eq, "$talk_context", tc_escape),
             (eq, "$talk_context", tc_prison_break),           
             (set_jump_entry, 7),                      
           (else_try),  
             (party_slot_eq, "$current_town", slot_party_type, spt_town),             
             #(set_visitor,0,"trp_player"),
             (set_jump_entry, 0),           
           (else_try),               
             #(set_visitor,1,"trp_player"),
             (set_jump_entry, 1),           
           (try_end),
                      
           #(store_faction_of_party, ":town_faction","$current_town"),
           #(faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
           #(faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           #(try_begin),
           #  (gt, ":tier_2_troop", 0),
           #  (gt, ":tier_3_troop", 0),
           #  (assign,reg0,":tier_3_troop"),
           #  (assign,reg1,":tier_3_troop"),
           #  (assign,reg2,":tier_2_troop"),
           #  (assign,reg3,":tier_2_troop"),
           #(else_try),
           #  (assign,reg0,"trp_swadian_skirmisher"),
           #  (assign,reg1,"trp_swadian_crossbowman"),
           #  (assign,reg2,"trp_swadian_infantry"),
           #  (assign,reg3,"trp_swadian_crossbowman"),
           #(try_end),
           #(assign,reg4,-1),
           #(shuffle_range,0,5),
           #(set_visitor,2,reg0),
           #(set_visitor,3,reg1),
           #(set_visitor,4,reg2),
           #(set_visitor,5,reg3),
           
           (set_jump_mission,"mt_sneak_caught_fight"),
           (set_passage_menu,"mnu_town"),
           (jump_to_scene,":sneak_scene"),
           (change_screen_mission),
        ]),
      ("sneak_caught_surrender",[],"Surrender.",
       [
#           (jump_to_menu,"mnu_captivity_start_castle_surrender"),
        ]),
    ]
  ),
  (
    "sneak_into_town_caught_dispersed_guards",0,
    "You drive off the guards and cover your trail before running off, easily losing your pursuers in the maze of streets.",
    "none",
    [],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$sneaked_into_town",1),
           (assign, "$town_entered", 1),
           (jump_to_menu,"mnu_town"),
        ]),
    ]
  ),
  
  (
    "sneak_into_town_caught_ran_away",0,
    "You make your way back through the gates and quickly retreat to the safety of the countryside.{s11}",
    "none",
    [
    
	(str_clear, s11),
	(assign, ":at_least_one_escaper_caught", 0),
	
	(assign, ":end_cond", kingdom_ladies_end),
	(try_for_range, ":prisoner", active_npcs_begin, ":end_cond"),
	  (try_begin),
		(troop_slot_eq, ":prisoner", slot_troop_mission_participation, mp_prison_break_escaped),
        (assign, "$talk_context", tc_hero_freed),
        (assign, reg14, ":prisoner"),
        (call_script, "script_setup_troop_meeting", ":prisoner", -1),
        (troop_set_slot, ":prisoner", slot_troop_mission_participation, -1),

        (troop_get_slot, ":prison_center", ":prisoner", slot_troop_prisoner_of_party),
        (party_remove_prisoners, ":prison_center", ":prisoner", 1),          
        (troop_set_slot, ":prisoner", slot_troop_prisoner_of_party, -1),

        (assign, ":end_cond", -1),
	  (else_try),	
		(troop_slot_eq, ":prisoner", slot_troop_mission_participation, mp_prison_break_caught),
		(str_store_troop_name, s12, ":prisoner"),
		(try_begin),
			(eq, ":at_least_one_escaper_caught", 0),
			(str_store_string, s11, "str_s11_unfortunately_s12_was_wounded_and_had_to_be_left_behind"),
		(else_try),
			(str_store_string, s11, "str_s11_also_s12_was_wounded_and_had_to_be_left_behind"),
		(try_end),	
		(assign, ":at_least_one_escaper_caught", 1),
	  (try_end),
	  
	  (troop_set_slot, ":prisoner", slot_troop_mission_participation, 0), #new
	(try_end),
	],
    [      
      ("continue",[],"Continue...",
       [
           (assign,"$auto_menu",-1),
           (store_encountered_party,"$last_sneak_attempt_town"),
           (store_current_hours,"$last_sneak_attempt_time"),
           (change_screen_return),
        ]),
    ]
  ),


#  (
#    "enemy_offer_ransom_for_prisoner",0,
#    "{s2} offers you a sum of {reg12} denars in silver if you are willing to sell him {s1}.",
#    "none",
#    [(call_script, "script_calculate_ransom_amount_for_troop", "$g_ransom_offer_troop"),
#     (assign, reg12, reg0),
#     (str_store_troop_name, s1, "$g_ransom_offer_troop"),
#     (store_troop_faction, ":faction_no", "$g_ransom_offer_troop"),
#     (str_store_faction_name, s2, ":faction_no"),
#     ],
#    [
#      ("ransom_accept",[],"Accept the offer.",
#       [(troop_add_gold, "trp_player", reg12),
#        (party_remove_prisoners, "$g_ransom_offer_party", "$g_ransom_offer_troop", 1),        
#        (call_script, "script_remove_troop_from_prison", "$g_ransom_offer_troop"),		
#        (try_begin),
#            (troop_get_type, ":is_female", "trp_player"),
#            (eq, ":is_female", 1),						
#
#            (get_achievement_stat, ":number_of_lords_sold", ACHIEVEMENT_MAN_HANDLER, 0),
#            (val_add, ":number_of_lords_sold", 1),
#            (set_achievement_stat, ACHIEVEMENT_MAN_HANDLER, 0, ":number_of_lords_sold"),			
#
#            (eq, ":number_of_lords_sold", 3),
#            (unlock_achievement, ACHIEVEMENT_MAN_HANDLER),
#        (try_end),
#
#        (change_screen_return),
#        ]),
#      ("ransom_reject",[],"Reject the offer.",
#       [
#        (call_script, "script_change_player_relation_with_troop", "$g_ransom_offer_troop", -4),
#        (call_script, "script_change_player_honor", -1),
#        (assign, "$g_ransom_offer_rejected", 1),
#        (change_screen_return),
#        ]),
#    ]
#  ),


  (
    "training_ground",0,
    "You approach a training field where you can practice your martial skills. What kind of training do you want to do?",
    "none",
    [
#      (store_add, "$g_training_ground_melee_training_scene", "scn_training_ground_ranged_melee_1", "$g_encountered_party"),
#      (val_sub, "$g_training_ground_melee_training_scene", training_grounds_begin),
#      (try_begin),
#        (ge, "$g_training_ground_training_count", 3),
#        (assign, "$g_training_ground_training_count", 0),
#        (rest_for_hours, 1, 5, 1), #rest while attackable
#        (assign, "$auto_enter_town", "$g_encountered_party"),
#        (change_screen_return),
#      (try_end),
      ],
    [
#      ("camp_trainer",
#       [], "Speak with the trainer.",
#       [
#         (set_jump_mission, "mt_training_ground_trainer_talk"),
#         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
#         (reset_visitors),
#         (set_jump_entry, 5),
#         (jump_to_scene, "$g_training_ground_melee_training_scene"),
#         (change_screen_mission),
#         (music_set_situation, 0),
#         ]),
#      ("camp_train_melee",
#       [
#         (neg|troop_is_wounded, "trp_player"),
#         (call_script, "script_party_count_fit_for_battle", "p_main_party"),
#         (gt, reg0, 1),
#         ], "Sparring practice.",
#       [
#         (assign, "$g_mt_mode", ctm_melee),
#         (jump_to_menu, "mnu_training_ground_selection_details_melee_1"),
#         (music_set_situation, 0),
#         ]),
#      ("camp_train_archery",[], "Ranged weapon practice.",
#       [
#         (jump_to_menu, "mnu_training_ground_selection_details_ranged_1"),
#         (music_set_situation, 0),
#         ]),
#      ("camp_train_mounted",[], "Horseback practice.",
#       [
#         (assign, "$g_mt_mode", ctm_mounted),
#         (jump_to_menu, "mnu_training_ground_selection_details_mounted"),
#         (music_set_situation, 0),
#         ]),
#
#      ("go_to_track",[(eq, "$cheat_mode", 1)],"{!}Cheat: Go to track.",
#       [
#         (set_jump_mission, "mt_ai_training"),
#         (store_add, ":scene_no", "scn_training_ground_horse_track_1", "$g_encountered_party"),
#         (val_sub, ":scene_no", training_grounds_begin),
#         (jump_to_scene, ":scene_no"),
#         (change_screen_mission),
#        ]
#       ),
#      ("go_to_range",[(eq, "$cheat_mode", 1)],"{!}Cheat: Go to range.",
#       [
#         (set_jump_mission, "mt_ai_training"),
#         (jump_to_scene, "$g_training_ground_melee_training_scene"),
#         (change_screen_mission),
#        ]
#       ),
      ("leave",[],"Leave.",
       [(change_screen_return),
        ]),
    ]
  ),


  ("training_ground_description",0,
   "{s0}",
   "none",
   [],
    [
      ("continue", [], "Continue...",
       [
         (jump_to_scene, "$g_training_ground_training_scene"),
         (change_screen_mission),
        ]
       ),
      ]
  ),

#  ("training_ground_training_result",mnf_disable_all_keys,
#   "{s7}{s2}",
#   "none",
#   [
#     (store_skill_level, ":trainer_skill", "skl_trainer", "trp_player"),
#     (store_add, ":trainer_skill_multiplier", 5, ":trainer_skill"),
#     (call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
#     (str_clear, s2),
#     (troop_get_slot, ":num_fit", "trp_stack_selection_amounts", 1),
#     (troop_get_slot, ":num_slots", "trp_stack_selection_amounts", 0),
#     (try_begin),
#       (gt, "$g_training_ground_training_success_ratio", 0),
#       (store_mul, ":xp_ratio_to_add", "$g_training_ground_training_success_ratio", "$g_training_ground_training_success_ratio"),
#       (try_begin),
#         (eq, "$g_training_ground_training_success_ratio", 100),
#         (val_mul, ":xp_ratio_to_add", 2), #2x when perfect
#       (try_end),
#       (try_begin),
#         (eq, "$g_mt_mode", ctm_melee),
#         (val_div, ":xp_ratio_to_add", 2),
#       (try_end),
#       (val_div, ":xp_ratio_to_add", 10), # value over 1000
#       (try_begin),
#         (gt, ":num_fit", 8),
#         (val_mul, ":xp_ratio_to_add", 3),
#         (assign, ":divisor", ":num_fit"),
#         (convert_to_fixed_point, ":divisor"),
#         (store_sqrt, ":divisor", ":divisor"),
#         (convert_to_fixed_point, ":xp_ratio_to_add"),
#         (val_div, ":xp_ratio_to_add", ":divisor"),
#       (try_end),
###       (assign, reg0, ":xp_ratio_to_add"),
###       (display_message, "@xp earn ratio: {reg0}/1000"),
#       (store_mul, ":xp_ratio_to_add_with_trainer_skill", ":xp_ratio_to_add", ":trainer_skill_multiplier"),
#       (val_div, ":xp_ratio_to_add_with_trainer_skill", 10),
#       (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
#       (store_add, ":end_cond", ":num_slots", 2),
#       (try_for_range, ":i_slot", 2, ":end_cond"),
#         (troop_get_slot, ":amount", "trp_stack_selection_amounts", ":i_slot"),
#         (troop_get_slot, ":troop_id", "trp_stack_selection_ids", ":i_slot"),
#         (assign, ":end_cond_2", ":num_stacks"),
#         (try_for_range, ":stack_no", 0, ":end_cond_2"),
#           (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
#           (eq, ":stack_troop", ":troop_id"),
#           (assign, ":end_cond_2", 0), #break
#           (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", ":amount", ":xp_ratio_to_add_with_trainer_skill"),
#           (str_store_troop_name_by_count, s1, ":troop_id", ":amount"),
#           (assign, reg1, ":amount"),
#           (str_store_string, s2, "@{s2}^{reg1} {s1} earned {reg0} experience."),
#         (try_end),
#       (try_end),
#       (try_begin),
#         (eq, "$g_mt_mode", ctm_melee),
#         (store_mul, ":special_xp_ratio_to_add", ":xp_ratio_to_add", 3),
#         (val_div, ":special_xp_ratio_to_add", 2),
#         (try_for_range, ":enemy_index", 0, "$g_training_ground_training_num_enemies"),
#           (troop_get_slot, ":troop_id", "trp_temp_array_a", ":enemy_index"),
#           (assign, ":end_cond_2", ":num_stacks"),
#           (try_for_range, ":stack_no", 0, ":end_cond_2"),
#             (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
#             (eq, ":stack_troop", ":troop_id"),
#             (assign, ":end_cond_2", 0), #break
#             (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", 1, ":special_xp_ratio_to_add"),
#             (str_store_troop_name, s1, ":troop_id"),
#             (str_store_string, s2, "@{s2}^{s1} earned an additional {reg0} experience."),
#           (try_end),
#         (try_end),
#       (try_end),
#       (try_begin),
#         (call_script, "script_cf_training_ground_sub_routine_for_training_result", "trp_player", -1, 1, ":xp_ratio_to_add"),
#         (str_store_string, s2, "@^You earned {reg0} experience.{s2}"),
#       (try_end),
#     (try_end),
#     (try_begin),
#      (eq, "$g_training_ground_training_success_ratio", 0),
#       (str_store_string, s7, "@The training didn't go well at all."),
#     (else_try),
#       (lt, "$g_training_ground_training_success_ratio", 25),
#       (str_store_string, s7, "@The training didn't go well at all."),
#     (else_try),
#       (lt, "$g_training_ground_training_success_ratio", 50),
#       (str_store_string, s7, "@The training didn't go very well."),
#     (else_try),
#       (lt, "$g_training_ground_training_success_ratio", 75),
#       (str_store_string, s7, "@The training went quite well."),
#     (else_try),
#       (lt, "$g_training_ground_training_success_ratio", 99),
#       (str_store_string, s7, "@The training went very well."),
#     (else_try),
#       (str_store_string, s7, "@The training went perfectly."),
#     (try_end),
#     
#     ],
#    [
#      ("continue",[],"Continue...",
#       [(jump_to_menu, "mnu_training_ground"),
#        ]
#       ),
#      ]
#   ),
  

#####################################################################
## Captivity....
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#
#  (
#    "captivity_start_castle_surrender",0,
#    "Stub",
#    "none",
#    [
#       (assign, "$g_player_is_captive", 1),
#       (assign,"$auto_menu",-1),
#       (assign, "$capturer_party", "$g_encountered_party"),
#       (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
#      ],
#    []
#  ),
#  (
#    "captivity_start_castle_defeat",0,
#    "Stub",
#    "none",
#    [
#       (assign, "$g_player_is_captive", 1),
#       (assign,"$auto_menu",-1),
#       (assign, "$capturer_party", "$g_encountered_party"),
#       (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
#      ],
#    []
#  ),
#  (
#    "captivity_start_under_siege_defeat",0,
#    "Your enemies take you prisoner.",
#    "none",
#    [
#       (assign, "$g_player_is_captive", 1),
#       (assign,"$auto_menu",-1),
#       (assign, "$capturer_party", "$g_encountered_party"),
#       (jump_to_menu, "mnu_captivity_castle_taken_prisoner"),
#    ],
#    []
#  ),
#  
#  (
#    "captivity_wilderness_taken_prisoner",mnf_scale_picture,
#    "Your enemies take you prisoner.",
#    "none",
#    [
#        (set_background_mesh, "mesh_pic_prisoner_wilderness"),
#     ],
#    [
#      ("continue",[],"Continue...",
#       [
#	     # Explanation of removing below code : heros are already being removed with 50% (was 75%, I decreased it) probability in mnu_total_defeat, why here there is additionally 30% removing of heros?
#		 # See codes linked to "mnu_captivity_start_wilderness_surrender" and "mnu_captivity_start_wilderness_defeat" which is connected with here they all also enter 
#		 # "mnu_total_defeat" and inside the "mnu_total_defeat" there is script_party_remove_all_companions which removes 50% (was 75%, I decreased it) of compainons from player party.		
#
#         #(try_for_range, ":npc", companions_begin, companions_end),
#         #  (main_party_has_troop, ":npc"),
#         #  (store_random_in_range, ":rand", 0, 100),
#         #  (lt, ":rand", 30),
#         #  (remove_member_from_party, ":npc", "p_main_party"),
#         #  (troop_set_slot, ":npc", slot_troop_occupation, 0),
#         #  (troop_set_slot, ":npc", slot_troop_playerparty_history, pp_history_scattered),
#         #  (assign, "$last_lost_companion", ":npc"),
#         #  (store_faction_of_party, ":victorious_faction", "$g_encountered_party"),
#         #  (troop_set_slot, ":npc", slot_troop_playerparty_history_string, ":victorious_faction"),
#         #  (troop_set_health, ":npc", 100),
#         #  (store_random_in_range, ":rand_town", towns_begin, towns_end),
#        #  (troop_set_slot, ":npc", slot_troop_cur_center, ":rand_town"),
#         #  (assign, ":nearest_town_dist", 1000),
#         #  (try_for_range, ":town_no", towns_begin, towns_end),
#         #    (store_faction_of_party, ":town_fac", ":town_no"),
#         #    (store_relation, ":reln", ":town_fac", "fac_player_faction"),
#         #    (ge, ":reln", 0),
#         #    (store_distance_to_party_from_party, ":dist", ":town_no", "p_main_party"),
#         #    (lt, ":dist", ":nearest_town_dist"),
#         #    (assign, ":nearest_town_dist", ":dist"),
#         #    (troop_set_slot, ":npc", slot_troop_cur_center, ":town_no"),
#         #  (try_end),
#         #(try_end),
#
#         (set_camera_follow_party, "$capturer_party"),
#         (assign, "$g_player_is_captive", 1),
#         (store_random_in_range, ":random_hours", 18, 30),         
#         (call_script, "script_event_player_captured_as_prisoner"),
#         (call_script, "script_stay_captive_for_hours", ":random_hours"),
#         (assign,"$auto_menu","mnu_captivity_wilderness_check"),
#         (change_screen_return),
#         ]),
#      ]
#  ),
  (
    "captivity_wilderness_check",0,
    "stub",
    "none",
    [(jump_to_menu,"mnu_captivity_end_wilderness_escape")],
    []
  ),
  (
    "captivity_end_wilderness_escape", mnf_scale_picture,
    "After painful days of being dragged about as a prisoner, you find a chance and escape from your captors!",
    "none",
    [
        (play_cue_track, "track_escape"),
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_escape_1_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_escape_1"),
        (try_end),
    ],
    [
      ("continue",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 0),
           (try_begin),
             (party_is_active, "$capturer_party"),
             (party_relocate_near_party, "p_main_party", "$capturer_party", 2),
           (try_end),
           (call_script, "script_set_parties_around_player_ignore_player", 8, 12), #it was radius:2 and hours:4, but players make lots of complains about consequent battle losses after releases from captivity then I changed this.
           (assign, "$g_player_icon_state", pis_normal),
           (set_camera_follow_party, "p_main_party"),
           (rest_for_hours, 0, 0, 0), #stop resting
           (change_screen_return),
        ]),
    ]
  ),
#  (
#    "captivity_castle_taken_prisoner",0,
#    "You are quickly surrounded by guards who take away your weapons. With curses and insults, they throw you into the dungeon where you must while away the miserable days of your captivity.",
#    "none",
#    [
#        (troop_get_type, ":is_female", "trp_player"),
#        (try_begin),
#          (eq, ":is_female", 1),
#          (set_background_mesh, "mesh_pic_prisoner_fem"),
#        (else_try),
#          (set_background_mesh, "mesh_pic_prisoner_man"),
#        (try_end),
#    ],
#    [
#      ("continue",[],"Continue...",
#       [
#           (assign, "$g_player_is_captive", 1),
#           (store_random_in_range, ":random_hours", 16, 22),
#           (call_script, "script_event_player_captured_as_prisoner"),
#           (call_script, "script_stay_captive_for_hours", ":random_hours"),
#           (assign,"$auto_menu", "mnu_captivity_castle_check"),
#           (change_screen_return)
#        ]),
#    ]
#  ),
#  (
#    "captivity_rescue_lord_taken_prisoner",0,
#    "You remain in disguise for as long as possible before revealing yourself.\
# The guards are outraged and beat you savagely before throwing you back into the cell for God knows how long...",
#    "none",
#    [
#        (troop_get_type, ":is_female", "trp_player"),
#        (try_begin),
#          (eq, ":is_female", 1),
#          (set_background_mesh, "mesh_pic_prisoner_fem"),
#        (else_try),
#          (set_background_mesh, "mesh_pic_prisoner_man"),
#        (try_end),
#   ],
#    [
#      ("continue",[],"Continue...",
#       [
#           (assign, "$g_player_is_captive", 1),
#           (store_random_in_range, ":random_hours", 16, 22),
#           (call_script, "script_event_player_captured_as_prisoner"),
#           (call_script, "script_stay_captive_for_hours", ":random_hours"),
#           (assign,"$auto_menu", "mnu_captivity_castle_check"),
#           (change_screen_return),
#        ]),
#    ]
#  ),
#  (
#    "captivity_castle_check",0,
#    "stub",
#    "none",
#    [
#        (store_random_in_range, reg(7), 0, 10),
#        (try_begin),
#		  (party_is_active, "$capturer_party"),
#		  (store_faction_of_party, ":capturer_faction", "$capturer_party"),
#		  (is_between, ":capturer_faction", kingdoms_begin, kingdoms_end),
#		  (store_relation, ":relation_w_player_faction", ":capturer_faction", "fac_player_faction"),
#		  (ge, ":relation_w_player_faction", 0),
#          (jump_to_menu,"mnu_captivity_end_exchanged_with_prisoner"),
#		(else_try),
#          (lt, reg(7), 4),
#                              
#          (store_character_level, ":player_level", "trp_player"),
#          (store_mul, "$player_ransom_amount", ":player_level", 50),
#          (val_add, "$player_ransom_amount", 100),                    
#          (store_troop_gold, reg3, "trp_player"),          
#          (store_div, ":player_gold_div_20", reg3, 20),
#          (val_add, "$player_ransom_amount", ":player_gold_div_20"),          
#          
#          (gt, reg3, "$player_ransom_amount"),
#          (jump_to_menu,"mnu_captivity_end_propose_ransom"),
#        (else_try),
#          (lt, reg7, 7),
#          (jump_to_menu,"mnu_captivity_end_exchanged_with_prisoner"),
#        (else_try),
#          (jump_to_menu,"mnu_captivity_castle_remain"),
#        (try_end),
#    ],
#    []
#  ),
#  (
#    "captivity_end_exchanged_with_prisoner",0,
#    "After days of imprisonment, you are finally set free when your captors exchange you with another prisoner.",
#    "none",
#    [
#      (play_cue_track, "track_escape"),
#      ],
#    [
#      ("continue",[],"Continue...",
#       [
#           (assign, "$g_player_is_captive", 0),
#           (try_begin),
#             (party_is_active, "$capturer_party"),
#             (party_relocate_near_party, "p_main_party", "$capturer_party", 2),
#           (try_end),
#           (call_script, "script_set_parties_around_player_ignore_player", 8, 12), #it was radius:2 and hours:12, but players make lots of complains about consequent battle losses after releases from captivity then I changed this.
#           (assign, "$g_player_icon_state", pis_normal),
#           (set_camera_follow_party, "p_main_party"),
#           (rest_for_hours, 0, 0, 0), #stop resting
#           (change_screen_return),
#        ]),
#    ]
#  ),
#  (
#    "captivity_end_propose_ransom",0,
#    "You spend long hours in the sunless dank of the dungeon, more than you can count.\
# Suddenly one of your captors enters your cell with an offer;\
# he proposes to free you in return for {reg5} denars of your hidden wealth. You decide to...",
#    "none",
#    [
#      (assign, reg5, "$player_ransom_amount"),
#    ],
#    [
#      ("captivity_end_ransom_accept",
#      [
#        (store_troop_gold,":player_gold", "trp_player"),
#        (ge, ":player_gold","$player_ransom_amount")
#      ],"Accept the offer.",
#      [
#        (play_cue_track, "track_escape"),
#        (assign, "$g_player_is_captive", 0),
#        (troop_remove_gold, "trp_player", "$player_ransom_amount"), 
#        (try_begin),
#          (party_is_active, "$capturer_party"),
#          (party_relocate_near_party, "p_main_party", "$capturer_party", 1),
#        (try_end),
#        (call_script, "script_set_parties_around_player_ignore_player", 8, 12), #it was radius:2 and hours:6, but players make lots of complains about consequent battle losses after releases from captivity then I changed this.
#        (assign, "$g_player_icon_state", pis_normal),
#        (set_camera_follow_party, "p_main_party"),
#        (rest_for_hours, 0, 0, 0), #stop resting
#        (change_screen_return),
#      ]),
#      ("captivity_end_ransom_deny",
#      [
#      ],"Refuse him, wait for something better.",
#      [
#        (assign, "$g_player_is_captive", 1),
#        (store_random_in_range, reg(8), 16, 22),
#        (call_script, "script_stay_captive_for_hours", reg8),
#        (assign,"$auto_menu", "mnu_captivity_castle_check"),
#        (change_screen_return),
#      ]),
#    ]
#  ),
#  (
#    "captivity_castle_remain",mnf_scale_picture|mnf_disable_all_keys,
#    "More days pass in the darkness of your cell. You get through them as best you can,\
# enduring the kicks and curses of the guards, watching your underfed body waste away more and more...",
#    "none",
#    [
#        (troop_get_type, ":is_female", "trp_player"),
#        (try_begin),
#          (eq, ":is_female", 1),
#          (set_background_mesh, "mesh_pic_prisoner_fem"),
#        (else_try),
#          (set_background_mesh, "mesh_pic_prisoner_man"),
#        (try_end),
#        (store_random_in_range, ":random_hours", 16, 22),
#        (call_script, "script_stay_captive_for_hours", ":random_hours"),
#        (assign,"$auto_menu", "mnu_captivity_castle_check"),
#        
#    ],
#    [
#      ("continue",[],"Continue...",
#       [
#           (assign, "$g_player_is_captive", 1),
#           (change_screen_return),
#        ]),
#    ]
#  ),


  
  (
    "notification_lord_defects",0,
    "Defection: {s4} has abandoned the {s5} and joined the {s7}, taking {reg4?her:his} his fiefs with him",
    "none",
	[
	  (assign, ":defecting_lord", "$g_notification_menu_var1"),
	  (assign, ":old_faction", "$g_notification_menu_var2"),
	  (str_store_troop_name, s4, ":defecting_lord"),
	  (str_store_faction_name, s5, ":old_faction"),
	  (store_faction_of_troop, ":new_faction", ":defecting_lord"),
	  (str_store_faction_name, s7, ":new_faction"),
	  (troop_get_type, reg4, ":defecting_lord"),
	  
	],
    [
      ("continue",[],"Continue",
       [
	   (change_screen_return),
        ]),
     ]
	),
	
	
#  (
#    "notification_treason_indictment",0,
#    "Treason Indictment^^{s9}",
#    "none",
#    [
#	  (assign, ":indicted_lord", "$g_notification_menu_var1"),
#	  (assign, ":former_faction", "$g_notification_menu_var2"),
#	  (faction_get_slot, ":former_faction_leader", ":former_faction", slot_faction_leader),
#	  
#	  #Set up string
#	  (try_begin),
#			(eq, ":indicted_lord", "trp_player"),
#			(str_store_troop_name, s7, ":former_faction_leader"),
#			(str_store_string, s9, "str_you_have_been_indicted_for_treason_to_s7_your_properties_have_been_confiscated_and_you_would_be_well_advised_to_flee_for_your_life"),
#	  (else_try),	
#			(str_store_troop_name, s4, ":indicted_lord"),
#			(str_store_faction_name, s5, ":former_faction"),
#			(str_store_troop_name, s6, ":former_faction_leader"),
#		
#			(troop_get_type, reg4, ":indicted_lord"),
#			(store_faction_of_troop, ":new_faction", ":indicted_lord"),
#			(try_begin),
#				(is_between, ":new_faction", kingdoms_begin, kingdoms_end),
#				(str_store_faction_name, s10, ":new_faction"),
#				(str_store_string, s11, "str_with_the_s10"),
#			(else_try),
#				(str_store_string, s11, "str_outside_calradia"),
#			(try_end),
#			(str_store_string, s9, "str_by_order_of_s6_s4_of_the_s5_has_been_indicted_for_treason_the_lord_has_been_stripped_of_all_reg4herhis_properties_and_has_fled_for_reg4herhis_life_he_is_rumored_to_have_gone_into_exile_s11"),
#		(try_end),
#	  
#	  
#	],
#    [
#      ("continue",[],"Continue",
#       [
#	   (change_screen_return),
#        ]),
#     ]
#	),


	
#  (
#    "notification_player_faction_active",0,
#    "You now possess land in your name, without being tied to any kingdom. This makes you a monarch in your own right, with your court temporarily located at {s12}. However, the other kings in Calradia will at first consider you a threat, for if any upstart warlord can grab a throne, then their own legitimacy is called into question.^^You may find it desirable at this time to pledge yourself to an existing kingdom. If you want to continue as a sovereign monarch, then your first priority should be to establish an independent right to rule. You can establish your right to rule through several means -- marrying into a high-born family, recruiting new lords, governing your lands, treating with other kings, or dispatching your companions on missions.^^At any rate, your first step should be to appoint a chief minister from among your companions, to handle affairs of state. Different companions have different capabilities.^You may appoint new ministers from time to time. You may also change the location of your court, by speaking to the minister.",
#    "none",
#    [
#      (set_fixed_point_multiplier, 100),
#      (position_set_x, pos0, 65),
#      (position_set_y, pos0, 30),
#      (position_set_z, pos0, 170),
#      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),
#      
#      (unlock_achievement, ACHIEVEMENT_CALRADIAN_TEA_PARTY),
#      (play_track, "track_coronation"),
#	  
#	  (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
#	    (lt, "$g_player_court", walled_centers_begin),
#		(store_faction_of_party, ":walled_center_faction", ":walled_center"),
#	    (eq, ":walled_center_faction", "fac_player_supporters_faction"),
#		(assign, "$g_player_court", ":walled_center"),
#		
#		(try_begin),
#			(troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
#			(is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
#			(troop_set_slot, ":spouse", slot_troop_cur_center, "$g_player_court"),
#		(try_end),
#		
#		(str_store_party_name, s12, "$g_player_court"),
#	  (try_end),
#	  
#      ],
#    [
#      ("appoint_spouse",[
#	  (troop_slot_ge, "trp_player", slot_troop_spouse, 1),
#	  (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
#	  (neg|troop_slot_eq, ":player_spouse", slot_troop_occupation, slto_kingdom_hero),
#	  (str_store_troop_name, s10, ":player_spouse"),
#	  ],"Appoint your wife, {s10}...",
#       [
#	   (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
#	   (assign, "$g_player_minister", ":player_spouse"),
#	   (jump_to_menu, "mnu_minister_confirm"),
#	   ]),
#
#      ("appoint_npc1",[
#	  (main_party_has_troop, "trp_npc1"),
#	  (str_store_troop_name, s10, "trp_npc1"),
#	  ],"Appoint {s10}",
#       [
#	   (assign, "$g_player_minister", "trp_npc1"),
#	   (jump_to_menu, "mnu_minister_confirm"),
#	   ]),
#	   
#      ("appoint_npc16",[
#	  (main_party_has_troop, "trp_npc16"),
#	  (str_store_troop_name, s10, "trp_npc16"),
#	  ],"Appoint {s10}",
#       [
#	   (assign, "$g_player_minister", "trp_npc16"),
#	   (jump_to_menu, "mnu_minister_confirm"), ]),
#
#      ("appoint_default",[],"Appoint a prominent citizen from the area...",
#       [
#	   (assign, "$g_player_minister", "trp_temporary_minister"),
#	   (troop_set_faction, "trp_temporary_minister", "fac_player_supporters_faction"),
#	   (jump_to_menu, "mnu_minister_confirm"),
#        ]),				
#     ]
#  ),  
  
  
  (
    "notification_player_faction_deactive",0,
    "Your kingdom no longer holds any land.",
    "none",
    [
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [
	   
	   (try_begin),
	   
	   
	   (try_end),
	   (assign, "$g_player_minister", -1),
	   (change_screen_return),
        ]),
     ]
  ),

  

  
  
  
#  (
#    "notification_center_under_siege",0,
#    "{s1} has been besieged by {s2} of {s3}!",
#    "none",
#    [
#      (str_store_party_name, s1, "$g_notification_menu_var1"),
#      (str_store_troop_name, s2, "$g_notification_menu_var2"),
#      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
#      (str_store_faction_name, s3, ":troop_faction"),
#      (set_fixed_point_multiplier, 100),
#      (position_set_x, pos0, 62),
#      (position_set_y, pos0, 30),
#      (position_set_z, pos0, 170),
#      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
#      ],
#    [
#      ("continue",[],"Continue...",
#       [(change_screen_return),
#        ]),
#     ]
#  ),  
#
#  (
#    "notification_village_raided",0,
#    "Enemies have Laid Waste to a Fief^^{s1} has been raided by {s2} of {s3}!",
#    "none",
#    [
#      (str_store_party_name, s1, "$g_notification_menu_var1"),
#      (str_store_troop_name, s2, "$g_notification_menu_var2"),
#      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
#      (str_store_faction_name, s3, ":troop_faction"),
#      (set_fixed_point_multiplier, 100),
#      (position_set_x, pos0, 62),
#      (position_set_y, pos0, 30),
#      (position_set_z, pos0, 170),
#      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
#      ],
#    [
#      ("continue",[],"Continue...",
#       [(change_screen_return),
#        ]),
#     ]
#  ),  
#
#  (
#    "notification_village_raid_started",0,
#    "Your Village is under Attack!^^{s2} of {s3} is laying waste to {s1}.",
#    "none",
#    [
#      (str_store_party_name, s1, "$g_notification_menu_var1"),
#      (str_store_troop_name, s2, "$g_notification_menu_var2"),
#      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
#      (str_store_faction_name, s3, ":troop_faction"),
#      (set_fixed_point_multiplier, 100),
#      (position_set_x, pos0, 62),
#      (position_set_y, pos0, 30),
#      (position_set_z, pos0, 170),
#      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
#      ],
#    [
#      ("continue",[],"Continue...",
#       [(change_screen_return),
#        ]),
#     ]
#  ),

  (
    "notification_one_faction_left",0,
    "Calradia Conquered by One Kingdom^^{s1} has defeated all rivals and stands as the sole kingdom.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
#      (try_begin),
#        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
#        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
#      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
#      (try_end),
	  (try_begin),
		(faction_slot_eq, "$g_notification_menu_var1", slot_faction_leader, "trp_player"),
		(unlock_achievement, ACHIEVEMENT_THE_GOLDEN_THRONE),
	  (else_try),
		(unlock_achievement, ACHIEVEMENT_MANIFEST_DESTINY),
	  (try_end),

        (try_begin),
            (troop_get_type, ":is_female", "trp_player"),
            (eq, ":is_female", 1),
            (unlock_achievement, ACHIEVEMENT_EMPRESS),
        (try_end),	  
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),
  
#  (
#    "notification_oath_renounced_faction_defeated",0,
#    "Your Old Faction was Defeated^^You won the battle against {s1}! This ends your struggle which started after you renounced your oath to them.",
#    "none",
#    [
#      (str_store_faction_name, s1, "$g_notification_menu_var1"),
#      (set_fixed_point_multiplier, 100),
#      (position_set_x, pos0, 65),
#      (position_set_y, pos0, 30),
#      (position_set_z, pos0, 170),
#      (try_begin),
#        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
#        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
#      (else_try),
#        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
#      (try_end),
#      ],
#    [
#      ("continue",[],"Continue...",
#       [(change_screen_return),
#        ]),
#     ]
#  ),

#  (
#    "notification_center_lost",0,
#    "An Estate was Lost^^You have lost {s1} to {s2}.",
#    "none",
#    [
#      (str_store_party_name, s1, "$g_notification_menu_var1"),
#      (str_store_faction_name, s2, "$g_notification_menu_var2"),
#      (set_fixed_point_multiplier, 100),
#      (position_set_x, pos0, 62),
#      (position_set_y, pos0, 30),
#      (position_set_z, pos0, 170),
#      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
#      ],
#    [
#      ("continue",[],"Continue...",
#       [(change_screen_return),
#        ]),
#     ]
#  ),


  (
    "notification_troop_left_players_faction",0,
    "Betrayal!^^{s1} has left {s2} and joined {s3}.",
    "none",
    [
      (str_store_troop_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$players_kingdom"),
      (str_store_faction_name, s3, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 55),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
      (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_troop_joined_players_faction",0,
    "Good news!^^ {s1} has left {s2} and joined {s3}.",
    "none",
    [
      (str_store_troop_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (str_store_faction_name, s3, "$players_kingdom"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 55),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
      (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_war_declared",0,
    "Declaration of War^^{s1} has declared war against {s2}!",
    "none",
    [

#	  (try_begin),
#		(eq, "$g_include_diplo_explanation", "$g_notification_menu_var1"),
#		(assign, "$g_include_diplo_explanation", 0),
#		(str_store_string, s57, "$g_notification_menu_var1"),
#	  (else_try),
#	    (str_clear, s57),
#	  (try_end),

	
	#to do the reason, have war_damage = 0 yield pre-war reasons
      (try_begin),
#        (eq, "$g_notification_menu_var1", "fac_player_supporters_faction"),
#        (str_store_faction_name, s1, "$g_notification_menu_var2"),
#        (str_store_string, s2, "@you"),
#      (else_try),
#        (eq, "$g_notification_menu_var2", "fac_player_supporters_faction"),
#        (str_store_faction_name, s1, "$g_notification_menu_var1"),
#        (str_store_string, s2, "@you"),
#      (else_try),
        (str_store_faction_name, s1, "$g_notification_menu_var1"),
        (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (try_end),
	  
	  
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_peace_declared",0,
    "Peace Agreement^^{s1} and {s2} have made peace!^{s57}",
    "none",
    [

	  (try_begin),
		(eq, 1, 0), #Alas, this does not seem to work
		(eq, "$g_include_diplo_explanation", "$g_notification_menu_var1"),
		(assign, "$g_include_diplo_explanation", 0),
	  (else_try),
	    (str_clear, s57),
	  (try_end),
	
	  (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":faction_1", "$g_notification_menu_var1", kingdoms_begin),
      (store_sub, ":faction_2", "$g_notification_menu_var2", kingdoms_begin),
      (val_mul, ":faction_1", 128),
      (val_add, ":faction_1", ":faction_2"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":faction_1", pos0),
      ],
    [
      ("continue",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  
  (
    "notification_faction_defeated",0,
    "Faction Eliminated^^{s1} is no more!",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
#      (try_begin),
#        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
#        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
#      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
#      (try_end),
      ],
    [
      ("continue",[],"Continue...",
       [
         (change_screen_return),
        ]),
     ]
  ),

  
#  (
#    "notification_rebels_switched_to_faction",0,
#    "Rebellion Success^^ Your rebellion is victorious! Your faction now has the sole claim to the title of {s11}, with {s12} as the single ruler.",
#    "none",
#    [
#      (str_store_faction_name, s11, "$g_notification_menu_var1"),
#      (str_store_troop_name, s12, "$g_notification_menu_var2"),
#      (set_fixed_point_multiplier, 100),
#      (position_set_x, pos0, 65),
#      (position_set_y, pos0, 30),
#      (position_set_z, pos0, 170),
#      (try_begin),
#        (is_between, "$g_notification_menu_var1", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
#        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
#      (else_try),
#        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
#      (try_end),
#      ],
#    [
#      ("continue",[],"Continue...",
#       [
#         (assign, "$talk_context", tc_rebel_thanks),
#         (start_map_conversation, "$g_notification_menu_var2", -1),
#         (change_screen_return),
#        ]),
#     ]
#  ),
#
#
#  (
#    "notification_player_should_consult",0,
#    "Your minister send words that there are problems brewing in the realm which, if left untreated, could sap your authority. You should consult with him at your earliest convenience",
#    "none",
#    [
#      ],
#    [
#      ("continue",[],"Continue...",
#       [
#	    (setup_quest_text, "qst_consult_with_minister"),
#
#        (str_store_troop_name, s11, "$g_player_minister"),
#        (str_store_party_name, s12, "$g_player_court"),
#	   
#		(str_store_string, s2, "str_consult_with_s11_at_your_court_in_s12"),
#	    (call_script, "script_start_quest", "qst_consult_with_minister", -1),
#		
#		
#		(quest_set_slot, "qst_consult_with_minister", slot_quest_expiration_days, 30),
#		(quest_set_slot, "qst_consult_with_minister", slot_quest_giver_troop, "$g_player_minister"),
#
#
#	    (change_screen_return),
#        ]),
#     ]
#  ),


    (
    "debug_alert_from_s65",0,
    "DEBUG ALERT: {s65}",
    "none",
    [
    ],
    [
      ("continue",[],"Continue...",
       [
		(assign, "$debug_message_in_queue", 0),
        (change_screen_return),
        ]),
     ]
  ),
      
  (
    "auto_return_to_map",0,
    "stub",
    "none",
    [(change_screen_map)],
    []
  ),

    (
    "bandit_lair",0,
    "{s3}",
    "none",
    [
      (try_begin),
        (eq, "$loot_screen_shown", 1),
		
        (try_for_range, ":bandit_template", "pt_steppe_bandits", "pt_deserters"),
          (party_template_slot_eq, ":bandit_template", slot_party_template_lair_party, "$g_encountered_party"),
          (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
        (try_end),
        
        (try_begin),
          (ge, "$g_encountered_party", 0),
          (party_is_active, "$g_encountered_party"),
          (party_get_template_id, ":template", "$g_encountered_party"),	    
	      (neq, ":template", "pt_looter_lair"),
          (remove_party, "$g_encountered_party"),
        (try_end),  
		
        (assign, "$g_leave_encounter", 0),
        (change_screen_return),
		
      (else_try),        
        (party_stack_get_troop_id, ":bandit_type", "$g_encountered_party", 0),
        (str_store_troop_name_plural, s4, ":bandit_type"),
        (str_store_string, s5, "str_bandit_approach_defile"),
		
        (try_begin),
          (eq, ":bandit_type", "trp_desert_bandit"),
          (str_store_string, s5, "str_bandit_approach_defile"),
        (else_try),
          (eq, ":bandit_type", "trp_mountain_bandit"),
          (str_store_string, s5, "str_bandit_approach_cliffs"),
        (else_try),
          (eq, ":bandit_type", "trp_forest_bandit"),
          (str_store_string, s5, "str_bandit_approach_swamp"),
        (else_try),
          (eq, ":bandit_type", "trp_taiga_bandit"),
          (str_store_string, s5, "str_bandit_approach_swamp"),
        (else_try),
          (eq, ":bandit_type", "trp_steppe_bandit"),
          (str_store_string, s5, "str_bandit_approach_thickets"),
        (else_try),
          (eq, ":bandit_type", "trp_sea_raider"),
          (str_store_string, s5, "str_bandit_approach_cove"),
        (try_end),
      
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0), #used in place of global variable
          (str_store_string, s3, "str_bandit_hideout_preattack"),
        (else_try),
          (party_get_template_id, ":template", "$g_encountered_party"),	    
	      (eq, ":template", "pt_looter_lair"),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1), #used in place of global variable
          (str_store_string, s3, "str_lost_startup_hideout_attack"),
		(else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1), #used in place of global variable
          (str_store_string, s3, "str_bandit_hideout_failure"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 2), #used in place of global variable
          (str_store_string, s3, "str_bandit_hideout_success"),
        (try_end),	
      (try_end),      
    ],
    [
#      ("continue_1",
#      [
#        (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0), #used in place of global variable
#	  ],
#	  "Attack the hideout...",
#	  
#	  [
#	    (party_set_slot, "$g_encountered_party", slot_party_ai_substate, 1),
#	    (party_get_template_id, ":template", "$g_encountered_party"),
#	    (assign, "$g_enemy_party", "$g_encountered_party"),
#	    	    
#	    (try_begin),
#	      (eq, ":template", "pt_sea_raider_lair"),
#	      (assign, ":bandit_troop", "trp_sea_raider"),
#	      (assign, ":scene_to_use", "scn_lair_sea_raiders"),
#	    (else_try),	
#	      (eq, ":template", "pt_forest_bandit_lair"),
#	      (assign, ":bandit_troop", "trp_forest_bandit"),
#	      (assign, ":scene_to_use", "scn_lair_forest_bandits"),
#	    (else_try),
#	      (eq, ":template", "pt_desert_bandit_lair"),
#	      (assign, ":bandit_troop", "trp_desert_bandit"),
#	      (assign, ":scene_to_use", "scn_lair_desert_bandits"),
#	    (else_try),
#	      (eq, ":template", "pt_mountain_bandit_lair"),
#	      (assign, ":bandit_troop", "trp_mountain_bandit"),
#	      (assign, ":scene_to_use", "scn_lair_mountain_bandits"),
#	    (else_try),
#	      (eq, ":template", "pt_taiga_bandit_lair"),
#	      (assign, ":bandit_troop", "trp_taiga_bandit"),
#	      (assign, ":scene_to_use", "scn_lair_taiga_bandits"),
#	    (else_try),
#	      (eq, ":template", "pt_steppe_bandit_lair"),
#	      (assign, ":bandit_troop", "trp_steppe_bandit"),
#	      (assign, ":scene_to_use", "scn_lair_steppe_bandits"),
#	    (else_try),
#	      (eq, ":template", "pt_looter_lair"),
#	      (assign, ":bandit_troop", "trp_looter"),
#	      
#	      (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),
#	      
#	      (try_begin),
#	        (eq, ":starting_town_faction", "fac_kingdom_1"), #player selected swadian city as starting town.
#	        (assign, ":scene_to_use", "scn_lair_forest_bandits"),	    
#	      (else_try),
#	        (eq, ":starting_town_faction", "fac_kingdom_2"), #player selected Vaegir city as starting town.
#	        (assign, ":scene_to_use", "scn_lair_taiga_bandits"),	    
#	      (else_try),
#	        (eq, ":starting_town_faction", "fac_kingdom_3"), #player selected Khergit city as starting town.
#	        (assign, ":scene_to_use", "scn_lair_steppe_bandits"),	    
#	      (else_try),
#	        (eq, ":starting_town_faction", "fac_kingdom_4"), #player selected Nord city as starting town.
#	        (assign, ":scene_to_use", "scn_lair_sea_raiders"),
#	      (else_try),
#	        (eq, ":starting_town_faction", "fac_kingdom_5"), #player selected Rhodok city as starting town.
#	        (assign, ":scene_to_use", "scn_lair_mountain_bandits"),
#	      (else_try),
#	        (eq, ":starting_town_faction", "fac_kingdom_6"), #player selected Sarranid city as starting town.
#	        (assign, ":scene_to_use", "scn_lair_desert_bandits"),	    
#	      (try_end),  
#	    (try_end),
#	    
#	    (modify_visitors_at_site,":scene_to_use"),
#	    (reset_visitors),	    
#
#        (store_character_level, ":player_level", "trp_player"),                   
#        (store_add, ":number_of_bandits_will_be_spawned_at_each_period", 5, ":player_level"),
#        (val_div, ":number_of_bandits_will_be_spawned_at_each_period", 3),
#	    
#	    (try_for_range, ":unused", 0, ":number_of_bandits_will_be_spawned_at_each_period"),
#	      (store_random_in_range, ":random_entry_point", 2, 11),	      
#	      (set_visitor, ":random_entry_point", ":bandit_troop", 1),	      
#	    (try_end),
#	    
#	    (party_clear, "p_temp_casualties"),
#	    
#	    (set_party_battle_mode),
#        (set_battle_advantage, 0),
#        (assign, "$g_battle_result", 0),
#        (set_jump_mission,"mt_bandit_lair"),
#        
#        (jump_to_scene, ":scene_to_use"),        
#        (change_screen_mission),        
#	  ]),
		
      ("leave_no_attack",
      [
	    (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 0),
	  ],
	  "Leave...",
      [
        (change_screen_return),
      ]),            
		
#	  ("leave_victory",
#	  [
#	    (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 2),
#	  ],
#	  "Continue...",
#      [      
#        (try_for_range, ":bandit_template", "pt_steppe_bandits", "pt_deserters"),
#          (party_template_slot_eq, ":bandit_template", slot_party_template_lair_party, "$g_encountered_party"),
#          (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
#        (try_end),
#         
#        (party_get_template_id, ":template", "$g_encountered_party"),
#        (try_begin),
#          (neq, ":template", "pt_looter_lair"),
#          (check_quest_active, "qst_destroy_bandit_lair"),
#          (quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_target_party, "$g_encountered_party"),
#          (call_script, "script_succeed_quest", "qst_destroy_bandit_lair"),
#        (try_end),
#                 
#        (assign, "$g_leave_encounter", 0),
#        (change_screen_return),
#
#        (try_begin),
#          (eq, "$loot_screen_shown", 0),
#          (assign, "$loot_screen_shown", 1),
##          (try_begin),
##            (gt, "$g_ally_party", 0),
##            (call_script, "script_party_add_party", "$g_ally_party", "p_temp_party"), #Add remaining prisoners to ally TODO: FIX it.
##          (else_try),
##            (party_get_num_attached_parties, ":num_quick_attachments", "p_main_party"),
##            (gt, ":num_quick_attachments", 0),
##            (party_get_attached_party_with_rank, ":helper_party", "p_main_party", 0),
##            (call_script, "script_party_add_party", ":helper_party", "p_temp_party"), #Add remaining prisoners to our reinforcements
##          (try_end),
#          (troop_clear_inventory, "trp_temp_troop"),
#          
#          (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"), 
#          (try_for_range, ":stack_no", 0, ":num_stacks"),
#            (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"), 
#            (try_begin),              
#              (party_stack_get_size, ":stack_size", "p_temp_casualties", ":stack_no"),
#              (party_stack_get_troop_id, ":stack_troop", "p_temp_casualties", ":stack_no"),
#              (gt, ":stack_size", 0),              
#              (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_size"), #addition_to_p_total_enemy_casualties
#              (party_stack_get_num_wounded, ":stack_wounded_size", "p_temp_casualties", ":stack_no"),
#              (gt, ":stack_wounded_size", 0),
#              (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded_size"),
#            (try_end),
#          (try_end),
#                    
#          (call_script, "script_party_calculate_loot", "p_total_enemy_casualties"), #p_encountered_party_backup changed to total_enemy_casualties          
#          (gt, reg0, 0),          
#          (troop_sort_inventory, "trp_temp_troop"),
#          (change_screen_loot, "trp_temp_troop"),
#        (try_end),
#        
#        (try_begin),
#          (ge, "$g_encountered_party", 0),
#          (party_is_active, "$g_encountered_party"),
#          (party_get_template_id, ":template", "$g_encountered_party"),	    
#	      (eq, ":template", "pt_looter_lair"),
#          (remove_party, "$g_encountered_party"),
#        (try_end),          
#      ]),
#		
#	  ("leave_defeat",
#	  [
#	    (party_slot_eq, "$g_encountered_party", slot_party_ai_substate, 1),
#	  ],
#	  "Continue...",
#      [
#        (try_for_range, ":bandit_template", "pt_steppe_bandits", "pt_deserters"),
#          (party_template_slot_eq, ":bandit_template", slot_party_template_lair_party, "$g_encountered_party"),
#          (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
#        (try_end),
#        
#        (try_begin),
#          (party_get_template_id, ":template", "$g_encountered_party"),
#          (neq, ":template", "pt_looter_lair"),
#          (check_quest_active, "qst_destroy_bandit_lair"),
#          (quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_target_party, "$g_encountered_party"),
#          (call_script, "script_fail_quest", "qst_destroy_bandit_lair"),
#        (try_end),
#        
#        (try_begin),
#          (ge, "$g_encountered_party", 0),
#          (party_is_active, "$g_encountered_party"),
#          (party_get_template_id, ":template", "$g_encountered_party"),	    
#	      (neq, ":template", "pt_looter_lair"),
#          (remove_party, "$g_encountered_party"),
#        (try_end),  
#
#        (assign, "$g_leave_encounter", 0),
#        
#		(try_begin),
#			(party_is_active, "$g_encountered_party"),
#			(party_set_slot, "$g_encountered_party", slot_party_ai_substate, 0),
#        (try_end),
#		
#        (change_screen_return),
#        ]),
		
     ]
  ),


  (
    "notification_player_faction_political_issue_resolved",0,
    "After consulting with the peers of the realm, {s10} has decided to confer {s11} on {s12}.",
    "none",
    [
	(assign, ":faction_issue_resolved", "$g_notification_menu_var1"),
	(assign, ":faction_decision", "$g_notification_menu_var2"),
	(faction_get_slot, ":leader", "$players_kingdom", slot_faction_leader),
	(str_store_troop_name, s10, ":leader"),
	(try_begin),
		(eq, ":faction_issue_resolved", 1),
		(str_store_string, s11, "str_the_marshalship"),
	(else_try),
		(str_store_party_name, s11, ":faction_issue_resolved"),
	(try_end),
	(str_store_troop_name, s12, ":faction_decision"),

	],
    [
	   ("continue",
	   [],"Continue...",
       [
        (change_screen_return),
        ]),		
	
	
	]
  ),
  
  (
    "notification_player_faction_political_issue_resolved_for_player",0,
    "After consulting with the peers of the realm, {s10} has decided to confer {s11} on you. You may decline the honor, but it will probably mean that you will not receive other awards for a little while.{s12}",
    "none",
    [
	(faction_get_slot, ":leader", "$players_kingdom", slot_faction_leader),
	(str_store_troop_name, s10, ":leader"),
	(faction_get_slot, ":issue", "$players_kingdom", slot_faction_political_issue),
	(try_begin),
		(eq, ":issue", 1),
		(str_store_string, s11, "str_the_marshalship"),
		(str_store_string, s12, "@^^Note that so long as you remain marshal, the lords of the realm will be expecting you to lead them on campaign. So, if you are awaiting a feast, either for a wedding or for other purposes, you may wish to resign the marshalship by speaking to your liege."),
	(else_try),
		(str_clear, s12),
		(str_store_party_name, s11, ":issue"),
	(try_end),	
	],
    [
	   ("accept",
	   [],"Accept the honor",
       [
	    (faction_get_slot, ":issue", "$players_kingdom", slot_faction_political_issue),
		
		(try_begin),
			(eq, ":issue", 1),
		    (call_script, "script_check_and_finish_active_army_quests_for_faction", "$players_kingdom"),       
			(call_script, "script_appoint_faction_marshall", "$players_kingdom", "trp_player"), 
			(unlock_achievement, ACHIEVEMENT_AUTONOMOUS_COLLECTIVE),
		(else_try),
			(call_script, "script_give_center_to_lord", ":issue", "trp_player", 0), #Zero means don't add garrison
		(try_end),
				
		(faction_set_slot, "$players_kingdom", slot_faction_political_issue, 0),
		(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
			(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
			(eq, ":active_npc_faction", "$players_kingdom"),
			(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
		(try_end),
        (change_screen_return),
        ]),	

	   ("decline",
	   [],"Decline the honor",
       [
	    (faction_get_slot, ":issue", "$players_kingdom", slot_faction_political_issue),
		(try_begin),
			(is_between, ":issue", centers_begin, centers_end),
			(assign, "$g_dont_give_fief_to_player_days", 30),
		(else_try),
			(assign, "$g_dont_give_marshalship_to_player_days", 30),
		(try_end),
		
		(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
			(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
			(eq, ":active_npc_faction", "$players_kingdom"),
			(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
		(try_end),
        (change_screen_return),
        ]),			
	]
  ),
  


#  ("lost_tavern_duel",mnf_disable_all_keys,
#    "{s11}",
#    "none",
#    [
#	(try_begin),
#		(agent_get_troop_id, ":type", "$g_main_attacker_agent"),
#		(eq, ":type", "trp_belligerent_drunk"),
#		(str_store_string, s11, "str_lost_tavern_duel_ordinary"),
#	(else_try),
#		(agent_get_troop_id, ":type", "$g_main_attacker_agent"),
#		(eq, ":type", "trp_hired_assassin"),
#		(str_store_string, s11, "str_lost_tavern_duel_assassin"),
#	(try_end),
#	(troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, -1),
#    ],
#    [
#      ("continue",[],"Continue...",
#       [         
#         (jump_to_menu, "mnu_town"),         
#       ]),       
#    ]
#  ),

  
] # GAME MENUS END

