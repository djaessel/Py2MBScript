from MBPlayer import MBPlayer
from MBOptions import MBOptions
from MBParty import MBParty
from item import Item



#def game_get_use_string(instance_id):
#    scene_prop_id = prop_instance_get_scene_prop_kind(instance_id)
#
#    winches_list = ["spr_winch_b", "spr_winch"]
#    door_ladder_list = ["spr_door_destructible", "spr_castle_f_door_b", "spr_siege_ladder_move_14m"]
#    if scene_prop_id in winches_list:
#        effected_object = "spr_portcullis"
#    elif scene_prop_id in door_ladder_list:
#        effected_object = scene_prop_id
#    #end
#    print("Effected object:", effected_object)


def game_start():
    script1(25,50)



def game_event_party_encounter(_g_encountered_party, _g_encountered_party_2):
    _g_encountered_party_faction = store_faction_of_party(_g_encountered_party)
    _g_encountered_party_relation = store_relation(_g_encountered_party_faction, "fac_player_faction")
    jump_to_menu("mnu_town")

 #   ("game_event_party_encounter",
 #    [
 #        (store_script_param_1, "$g_encountered_party"),
 #        (store_script_param_2, "$g_encountered_party_2"),# encountered_party2 is set when we come across a battle or siege, otherwise it's a negative value
 #        (store_faction_of_party, "$g_encountered_party_faction","$g_encountered_party"),
 #        (store_relation, "$g_encountered_party_relation", "$g_encountered_party_faction", "fac_player_faction"),
 #
 #        (party_get_slot, "$g_encountered_party_type", "$g_encountered_party", slot_party_type),
 #        (party_get_template_id,"$g_encountered_party_template","$g_encountered_party"),
 #
  #NPC companion changes begin
#         (call_script, "script_party_count_fit_regulars", "p_main_party"),
#         (assign, "$playerparty_prebattle_regulars", reg0),
#
#         (assign, "$g_last_rest_center", -1),
#         (assign, "$talk_context", 0),
#         (assign,"$g_player_surrenders",0),
#         (assign,"$g_enemy_surrenders",0),
#         (assign, "$g_leave_encounter",0),
#         (assign, "$g_engaged_enemy", 0),
#         (try_begin),
#           (neg|is_between, "$g_encountered_party", centers_begin, centers_end),
#           (rest_for_hours, 0), #stop waiting
#           (assign, "$g_infinite_camping", 0),
#         (try_end),
#         (assign, "$new_encounter", 1), #check this in the menu.
 #        (try_begin),
 #          (lt, "$g_encountered_party_2",0), #Normal encounter. Not battle or siege.
 #          (try_begin),
 #            (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
 #            (jump_to_menu, "mnu_castle_outside"),
 #          (else_try),
 #            (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
 #            (jump_to_menu, "mnu_castle_outside"),
 #          (else_try),
 #            (party_slot_eq, "$g_encountered_party", slot_party_type, spt_ship),
  #           (jump_to_menu, "mnu_ship_reembark"),
  #         (else_try),
 #            (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
#             (jump_to_menu, "mnu_village"),
#           (else_try),
#             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_cattle_herd),
#             (jump_to_menu, "mnu_cattle_herd"),
#         (else_try),
#           (eq, "$g_encountered_party", "p_camp_bandits"),
#           (jump_to_menu, "mnu_camp"),
#         (else_try),
#           (jump_to_menu, "mnu_simple_encounter"),
#         (try_end),
#       (else_try), #Battle or siege
#         (try_begin),
#           (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
#           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
#           (try_begin),
#             (eq, "$auto_enter_town", "$g_encountered_party"),
#             (jump_to_menu, "mnu_town"),
#           (try_end),
#         (else_try),
#           (jump_to_menu, "mnu_pre_join"),
#         (try_end),
#       (try_end),
#       (assign,"$auto_enter_town",0),
#       (assign,"$auto_besiege_town",0),




def script1(waterLevel, fishCount):
    versionx = get_operation_set_version()
    if versionx > 0 and versionx <= 1101:
        banner_id = profile_get_banner_id()
        if banner_id > 20 or banner_id == 0 or banner_id == 10:
            print(versionx)
            if versionx == 1011:
                print("YES!")
            else:
                print("Nope")

    if fishCount == 1 and is_edit_mode_enabled():
        print("Test1")
    elif is_edit_mode_enabled() or versionx > 1011:
        print("Test4")

    if waterLevel == 2 or fishCount == 1:
        print("TEST2")
    else:
        print("TEST3")

    print("Hello World!")


def helloWorld():
    optionx = MBOptions()
    ai_strength = optionx.get_campaign_ai()
    if is_edit_mode_enabled():
        print("Hello World!")
    #fi
    ai_strength *= 5
    sun = 10
    water = sun + 2
    ai_strength /= water
    optionx.set_damage_to_friends(ai_strength)
    sun = sun / 2
    s0 = "LOL"
    if is_edit_mode_enabled():
        print("Strength:", ai_strength, "Water:", water, s0)
    else:
        script1(water, ai_strength)


def loopy():
    for i in range(2, 10):
        print(i)

    for i in range(5):
        optionx = MBOptions()
        ai_strength = optionx.get_campaign_ai()
        if ai_strength == 1: # test 1
            print("YES!")

    for x in range(200, 0, -1): # test 2
        reg0 = x
        print("Backwards: {reg0}")


def whoIsMyPlayerTeam(playerId):
    playerx = MBPlayer(playerId)
    team_no = playerx.get_team_no()
    reg0 = team_no
    print(reg0)


def itemx(playerId, item):
    playerx = MBPlayer(playerId)
    playerx.add_spawn_item(0, item)
    teamNo = playerx.get_team_no()
    entry_point = multiplayer_find_spawn_point(teamNo, 1, 0)
    print("Spawn point")
    print(entry_point)


def setNewTeam(playerId, teamNo):
    playerx = MBPlayer(playerId)
    playerx.set_team_no(teamNo)
    reg0 = playerId
    reg1 = teamNo
    print("{reg0} has team {reg1}")


def changeFactionIfActive(partyId, newFactionNo):
    partaaay = MBParty(partyId)
    if partaaay.is_active():
        partaaay.set_faction(newFactionNo)
        #partaaay.add_template("pt_sea_raiders")
        partaaay.add_members("trp_looter", 15)
    else:
        print("Party", partyId, "is inactive")


def tryAgain(randomVal):
    try:
        is_edit_mode_enabled()

        # has problems
        waterLevel = 5
        if not randomVal == 3:
            waterLevel-=2
        else:
            waterLevel += 1
        print(waterLevel)
    except:
        print("There was an error!")


def well(water):
    if water > 10:
        print("Well...", "well!")
    elif water > 3:
        print("Well!")
    else:
        print("Well...")


def prepareItem(item_id):
    my_item = Item(item_id)
    diffy = my_item.get_difficulty()
    if diffy < 10:
        armor = my_item.get_body_armor()
        print(armor, "armor!")
    else:
        print(diffy, " too high!")

