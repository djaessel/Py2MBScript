# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")

from tableau_material import TableauMaterial


game_character_sheet = TableauMaterial("game_character_sheet", "tableau_with_transparency", 1024, 1024, 0, 0, 266, 532)
def code(troop_no):
    cur_tableau_set_background_color(0xFF888888)
    cur_tableau_set_ambient_light(10,11,15)
    set_fixed_point_multiplier(100)
    cur_tableau_set_camera_parameters(0, 40, 40, 0, 100000)#

    init_position(pos1)
    position_set_z(pos1, 100)
    position_set_x(pos1, -20)
    position_set_y(pos1, -20)
    cur_tableau_add_tableau_mesh("tableau_troop_character_color", troop_no, pos1, 0, 0)
    position_set_z(pos1, 200)
    cur_tableau_add_tableau_mesh("tableau_troop_character_alpha_mask", troop_no, pos1, 0, 0)
    position_set_z(pos1, 300)
game_character_sheet.codeBlock = code


game_inventory_window = TableauMaterial("game_inventory_window", "tableau_with_transparency", 1024, 1024, 0, 0, 180, 270)
def code(troop_no):
    cur_tableau_set_background_color(0xFF888888)
    cur_tableau_set_ambient_light(10,11,15)
    set_fixed_point_multiplier(100)
    cur_tableau_set_camera_parameters(0, 40, 40, 0, 100000)#

    init_position(pos1)
    position_set_z(pos1, 100)
    position_set_x(pos1, -20)
    position_set_y(pos1, -20)
    cur_tableau_add_tableau_mesh("tableau_troop_character_color", troop_no, pos1, 0, 0)
    position_set_z(pos1, 200)
    cur_tableau_add_tableau_mesh("tableau_troop_character_alpha_mask", troop_no, pos1, 0, 0)
    position_set_z(pos1, 300)
game_inventory_window.codeBlock = code


troop_character_color = TableauMaterial("troop_character_color", "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400)
def code(troop_no):
    cur_tableau_set_background_color(0xFFE0CFB1)
    cur_tableau_set_ambient_light(10,11,15)
    add_troop_to_cur_tableau_for_character(troop_no)
troop_character_color.codeBlock = code


troop_character_alpha_mask = TableauMaterial("troop_character_alpha_mask", "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400)
def code(troop_no):
    cur_tableau_set_background_color(0x00888888)
    cur_tableau_set_ambient_light(10,11,15)
    cur_tableau_render_as_alpha_mask()
    add_troop_to_cur_tableau_for_character(troop_no)
troop_character_alpha_mask.codeBlock = code



