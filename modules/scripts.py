# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")


from MBParty import MBParty
#import ID_animations as animID


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


def add_troop_to_cur_tableau_for_character(troop_no):
    set_fixed_point_multiplier(100)

    cur_tableau_clear_override_items()
    #cur_tableau_set_override_flags(af_override_fullhelm)

    init_position(pos2)
    cur_tableau_set_camera_parameters(1, 4, 8, 10, 10000)

    init_position(pos5)
    cam_height = 150
    camera_distance = 360
    camera_yaw = -15
    camera_pitch = -18
    animation = 1 # animID.anim_stand_man

    position_set_z(pos5, cam_height)

    # camera looks towards -z axis
    position_rotate_x(pos5, -90)
    position_rotate_z(pos5, 180,0)

    # now apply yaw and pitch
    position_rotate_y(pos5, camera_yaw)
    position_rotate_x(pos5, camera_pitch)
    position_move_z(pos5, camera_distance, 0)
    position_move_x(pos5, 5, 0)

    if troop_is_hero(troop_no):
        cur_tableau_add_troop(troop_no, pos2, animation, -1)
    else:
      random_seed = troop_no * 126233
      random_seed %= 1000
      random_seed += 1
      cur_tableau_add_troop(troop_no, pos2, animation, random_seed)

    cur_tableau_set_camera_position(pos5)

    copy_position(pos8, pos5)
    #y axis aligned with camera now. z is up
    position_rotate_x(pos8, -90)
    position_rotate_z(pos8, 30,0)
    position_rotate_x(pos8, -60)
    cur_tableau_add_sun_light(0, pos8, 175,150,125)




