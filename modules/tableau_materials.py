# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")

from tableau_material import TableauMaterial


game_character_sheet = TableauMaterial("game_character_sheet", "tableau_with_transparency", 1024, 1024, 0, 0, 266, 532)
def code(var001):
    cur_tableau_set_background_color(4287137928)
    cur_tableau_set_ambient_light(10,11,15)
    set_fixed_point_multiplier(100)
    cur_tableau_set_camera_parameters(0,40,40,0,100000)
    init_position(1)
    position_set_z(1,100)
    position_set_x(1,-20)
    position_set_y(1,-20)
    cur_tableau_add_tableau_mesh(tab.troop_character_color,var001,1,0,0)
    position_set_z(1,200)
    cur_tableau_add_tableau_mesh(tab.troop_character_alpha_mask,var001,1,0,0)
    position_set_z(1,300)
game_character_sheet.codeBlock = code


game_inventory_window = TableauMaterial("game_inventory_window", "tableau_with_transparency", 1024, 1024, 0, 0, 180, 270)
def code(var001):
    cur_tableau_set_background_color(4287137928)
    cur_tableau_set_ambient_light(10,11,15)
    set_fixed_point_multiplier(100)
    cur_tableau_set_camera_parameters(0,40,40,0,100000)
    init_position(1)
    position_set_z(1,100)
    position_set_x(1,-20)
    position_set_y(1,-20)
    cur_tableau_add_tableau_mesh(tab.troop_inventory_color,var001,1,0,0)
    position_set_z(1,200)
    cur_tableau_add_tableau_mesh(tab.troop_inventory_alpha_mask,var001,1,0,0)
    position_set_z(1,300)
game_inventory_window.codeBlock = code


game_profile_window = TableauMaterial("game_profile_window", "tableau_with_transparency", 1024, 1024, 0, 0, 320, 480)
def code(var001):
    var002 = var001
    var002 %= 2
    if var002 == 0:
        troop_id_003 = trp.multiplayer_profile_troop_male
    else:
        troop_id_003 = trp.multiplayer_profile_troop_female
    #end
    troop_set_face_key_from_current_profile(troop_id_003)
    cur_tableau_set_background_color(4287137928)
    cur_tableau_set_ambient_light(10,11,15)
    set_fixed_point_multiplier(100)
    cur_tableau_set_camera_parameters(0,40,40,0,100000)
    init_position(1)
    position_set_z(1,100)
    position_set_x(1,-20)
    position_set_y(1,-20)
    cur_tableau_add_tableau_mesh(tab.troop_profile_color,troop_id_003,1,0,0)
    position_set_z(1,200)
    cur_tableau_add_tableau_mesh(tab.troop_profile_alpha_mask,troop_id_003,1,0,0)
game_profile_window.codeBlock = code


game_party_window = TableauMaterial("game_party_window", "tableau_with_transparency", 1024, 1024, 0, 0, 300, 300)
def code(var001):
    cur_tableau_set_background_color(4287137928)
    cur_tableau_set_ambient_light(10,11,15)
    set_fixed_point_multiplier(100)
    cur_tableau_set_camera_parameters(0,40,40,0,100000)
    init_position(1)
    position_set_z(1,100)
    position_set_x(1,-20)
    position_set_y(1,-20)
    cur_tableau_add_tableau_mesh(tab.troop_party_color,var001,1,0,0)
    position_set_z(1,200)
    cur_tableau_add_tableau_mesh(tab.troop_party_alpha_mask,var001,1,0,0)
    position_set_z(1,300)
game_party_window.codeBlock = code


game_troop_label_banner = TableauMaterial("game_troop_label_banner", "tableau_with_transparency", 256, 256, -128, 0, 128, 256)
def code(var001):
    cur_tableau_set_background_color(4287137928)
    set_fixed_point_multiplier(100)
    cur_tableau_set_camera_parameters(0,100,100,0,100000)
    init_position(1)
    position_set_y(1,120)
    cur_tableau_add_mesh(var001,1,120,0)
game_troop_label_banner.codeBlock = code


round_shield_1 = TableauMaterial("round_shield_1", "sample_shield_round_1", 512, 256, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-50)
    position_set_y(1,125)
    cur_tableau_add_mesh(var001,1,120,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_round_1,1,0,0)
    cur_tableau_set_camera_parameters(0,200,100,0,100000)
round_shield_1.codeBlock = code


round_shield_2 = TableauMaterial("round_shield_2", "sample_shield_matte", 512, 256, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-50)
    position_set_y(1,120)
    cur_tableau_add_mesh(var001,1,116,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_round_2,1,0,0)
    cur_tableau_set_camera_parameters(0,200,100,0,100000)
round_shield_2.codeBlock = code


round_shield_3 = TableauMaterial("round_shield_3", "sample_shield_matte", 512, 256, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-50)
    position_set_y(1,120)
    cur_tableau_add_mesh(var001,1,116,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_round_3,1,0,0)
    cur_tableau_set_camera_parameters(0,200,100,0,100000)
round_shield_3.codeBlock = code


round_shield_4 = TableauMaterial("round_shield_4", "sample_shield_matte", 512, 256, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-50)
    position_set_y(1,125)
    cur_tableau_add_mesh(var001,1,123,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_round_4,1,0,0)
    cur_tableau_set_camera_parameters(0,200,100,0,100000)
round_shield_4.codeBlock = code


round_shield_5 = TableauMaterial("round_shield_5", "sample_shield_matte", 512, 256, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-50)
    position_set_y(1,125)
    cur_tableau_add_mesh(var001,1,122,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_round_5,1,0,0)
    cur_tableau_set_camera_parameters(0,200,100,0,100000)
round_shield_5.codeBlock = code


small_round_shield_1 = TableauMaterial("small_round_shield_1", "sample_shield_small_round_1", 512, 256, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-50)
    position_set_y(1,130)
    cur_tableau_add_mesh(var001,1,127,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_small_round_1,1,0,0)
    cur_tableau_set_camera_parameters(0,200,100,0,100000)
small_round_shield_1.codeBlock = code


small_round_shield_2 = TableauMaterial("small_round_shield_2", "sample_shield_small_round_2", 512, 256, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-50)
    position_set_y(1,130)
    cur_tableau_add_mesh(var001,1,127,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_small_round_2,1,0,0)
    cur_tableau_set_camera_parameters(0,200,100,0,100000)
small_round_shield_2.codeBlock = code


small_round_shield_3 = TableauMaterial("small_round_shield_3", "sample_shield_matte", 512, 256, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-50)
    position_set_y(1,130)
    cur_tableau_add_mesh(var001,1,127,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_small_round_3,1,0,0)
    cur_tableau_set_camera_parameters(0,200,100,0,100000)
small_round_shield_3.codeBlock = code


kite_shield_1 = TableauMaterial("kite_shield_1", "sample_shield_matte", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-60)
    position_set_y(1,140)
    cur_tableau_add_mesh(var001,1,116,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_kite_1,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
kite_shield_1.codeBlock = code


kite_shield_2 = TableauMaterial("kite_shield_2", "sample_shield_matte", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-57)
    position_set_y(1,140)
    cur_tableau_add_mesh(var001,1,116,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_kite_2,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
kite_shield_2.codeBlock = code


kite_shield_3 = TableauMaterial("kite_shield_3", "sample_shield_matte", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-57)
    position_set_y(1,140)
    cur_tableau_add_mesh(var001,1,116,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_kite_3,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
kite_shield_3.codeBlock = code


kite_shield_4 = TableauMaterial("kite_shield_4", "sample_shield_matte", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-50)
    position_set_y(1,160)
    cur_tableau_add_mesh(var001,1,120,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_kite_4,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
kite_shield_4.codeBlock = code


heater_shield_1 = TableauMaterial("heater_shield_1", "sample_shield_matte", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-60)
    position_set_y(1,151)
    cur_tableau_add_mesh(var001,1,116,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_heater_1,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
heater_shield_1.codeBlock = code


heater_shield_2 = TableauMaterial("heater_shield_2", "sample_shield_matte", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-50)
    position_set_y(1,150)
    cur_tableau_add_mesh(var001,1,116,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_heater_2,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
heater_shield_2.codeBlock = code


pavise_shield_1 = TableauMaterial("pavise_shield_1", "sample_shield_matte", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-54)
    position_set_y(1,120)
    cur_tableau_add_mesh(var001,1,118,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_pavise_1,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
pavise_shield_1.codeBlock = code


pavise_shield_2 = TableauMaterial("pavise_shield_2", "sample_shield_matte", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    position_set_x(1,-54)
    position_set_y(1,120)
    cur_tableau_add_mesh(var001,1,116,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_shield_pavise_2,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
pavise_shield_2.codeBlock = code


heraldic_armor_a = TableauMaterial("heraldic_armor_a", "sample_heraldic_armor_a", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    slot_no_002 = var001 - mesh.arms_a01
    troop_slot_003 = troop_get_slot(trp.banner_background_color_array,slot_no_002)
    cur_tableau_set_background_color(troop_slot_003)
    init_position(1)
    cur_tableau_add_mesh_with_vertex_color(mesh.heraldic_armor_bg,1,200,100,troop_slot_003)
    init_position(1)
    position_set_z(1,50)
    position_set_x(1,-25)
    position_set_y(1,130)
    cur_tableau_add_mesh(var001,1,103,0)
    init_position(1)
    position_set_z(1,100)
    cur_tableau_add_mesh(mesh.tableau_mesh_heraldic_armor_a,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
heraldic_armor_a.codeBlock = code


heraldic_armor_b = TableauMaterial("heraldic_armor_b", "sample_heraldic_armor_b", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    slot_no_002 = var001 - mesh.arms_a01
    troop_slot_003 = troop_get_slot(trp.banner_background_color_array,slot_no_002)
    cur_tableau_set_background_color(troop_slot_003)
    init_position(1)
    cur_tableau_add_mesh_with_vertex_color(mesh.heraldic_armor_bg,1,200,100,troop_slot_003)
    init_position(1)
    position_set_z(1,10)
    position_set_x(1,-5)
    position_set_y(1,130)
    cur_tableau_add_mesh(var001,1,113,0)
    init_position(1)
    position_set_z(1,100)
    cur_tableau_add_mesh(mesh.tableau_mesh_heraldic_armor_b,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
heraldic_armor_b.codeBlock = code


heraldic_armor_c = TableauMaterial("heraldic_armor_c", "sample_heraldic_armor_c", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    slot_no_002 = var001 - mesh.arms_a01
    troop_slot_003 = troop_get_slot(trp.banner_background_color_array,slot_no_002)
    cur_tableau_set_background_color(troop_slot_003)
    init_position(1)
    cur_tableau_add_mesh_with_vertex_color(mesh.heraldic_armor_bg,1,200,100,troop_slot_003)
    init_position(1)
    position_set_z(1,10)
    position_set_x(1,0)
    position_set_y(1,130)
    cur_tableau_add_mesh(var001,1,115,0)
    init_position(1)
    position_set_z(1,100)
    cur_tableau_add_mesh(mesh.tableau_mesh_heraldic_armor_c,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
heraldic_armor_c.codeBlock = code


heraldic_armor_d = TableauMaterial("heraldic_armor_d", "sample_heraldic_armor_d", 512, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    slot_no_002 = var001 - mesh.arms_a01
    troop_slot_003 = troop_get_slot(trp.banner_background_color_array,slot_no_002)
    cur_tableau_set_background_color(troop_slot_003)
    init_position(1)
    cur_tableau_add_mesh_with_vertex_color(mesh.heraldic_armor_bg,1,200,100,troop_slot_003)
    init_position(1)
    position_set_z(1,10)
    position_set_x(1,0)
    position_set_y(1,130)
    cur_tableau_add_mesh(var001,1,113,0)
    init_position(1)
    position_set_z(1,100)
    cur_tableau_add_mesh(mesh.tableau_mesh_heraldic_armor_d,1,0,0)
    cur_tableau_set_camera_parameters(0,200,200,0,100000)
heraldic_armor_d.codeBlock = code


troop_note_alpha_mask = TableauMaterial("troop_note_alpha_mask", "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400)
def code(var001):
    cur_tableau_set_background_color(8947848)
    cur_tableau_set_ambient_light(10,11,15)
    cur_tableau_render_as_alpha_mask()
    add_troop_to_cur_tableau(var001)
troop_note_alpha_mask.codeBlock = code


troop_note_color = TableauMaterial("troop_note_color", "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400)
def code(var001):
    cur_tableau_set_background_color(4291214228)
    cur_tableau_set_ambient_light(10,11,15)
    add_troop_to_cur_tableau(var001)
troop_note_color.codeBlock = code


troop_character_alpha_mask = TableauMaterial("troop_character_alpha_mask", "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400)
def code(var001):
    cur_tableau_set_background_color(8947848)
    cur_tableau_set_ambient_light(10,11,15)
    cur_tableau_render_as_alpha_mask()
    add_troop_to_cur_tableau_for_character(var001)
troop_character_alpha_mask.codeBlock = code


troop_character_color = TableauMaterial("troop_character_color", "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400)
def code(var001):
    cur_tableau_set_background_color(4292923313)
    cur_tableau_set_ambient_light(10,11,15)
    add_troop_to_cur_tableau_for_character(var001)
troop_character_color.codeBlock = code


troop_inventory_alpha_mask = TableauMaterial("troop_inventory_alpha_mask", "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400)
def code(var001):
    cur_tableau_set_background_color(8947848)
    cur_tableau_set_ambient_light(10,11,15)
    cur_tableau_render_as_alpha_mask()
    add_troop_to_cur_tableau_for_inventory(var001)
troop_inventory_alpha_mask.codeBlock = code


troop_inventory_color = TableauMaterial("troop_inventory_color", "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400)
def code(var001):
    cur_tableau_set_background_color(4285159482)
    cur_tableau_set_ambient_light(10,11,15)
    add_troop_to_cur_tableau_for_inventory(var001)
troop_inventory_color.codeBlock = code


troop_profile_alpha_mask = TableauMaterial("troop_profile_alpha_mask", "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400)
def code(var001):
    cur_tableau_set_background_color(8947848)
    cur_tableau_set_ambient_light(10,11,15)
    cur_tableau_render_as_alpha_mask()
    add_troop_to_cur_tableau_for_profile(var001)
troop_profile_alpha_mask.codeBlock = code


troop_profile_color = TableauMaterial("troop_profile_color", "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400)
def code(var001):
    cur_tableau_set_background_color(4294567848)
    cur_tableau_set_ambient_light(10,11,15)
    add_troop_to_cur_tableau_for_profile(var001)
troop_profile_color.codeBlock = code


troop_party_alpha_mask = TableauMaterial("troop_party_alpha_mask", "mat_troop_portrait_mask", 1024, 1024, 0, 0, 400, 400)
def code(var001):
    cur_tableau_set_background_color(8947848)
    cur_tableau_set_ambient_light(10,11,15)
    cur_tableau_render_as_alpha_mask()
    add_troop_to_cur_tableau_for_party(var001)
troop_party_alpha_mask.codeBlock = code


troop_party_color = TableauMaterial("troop_party_color", "mat_troop_portrait_color", 1024, 1024, 0, 0, 400, 400)
def code(var001):
    cur_tableau_set_background_color(4290681970)
    cur_tableau_set_ambient_light(10,11,15)
    add_troop_to_cur_tableau_for_party(var001)
troop_party_color.codeBlock = code


troop_note_mesh = TableauMaterial("troop_note_mesh", "tableau_with_transparency", 1024, 1024, 0, 0, 350, 350)
def code(var001):
    cur_tableau_set_background_color(4287137928)
    cur_tableau_set_ambient_light(10,11,15)
    set_fixed_point_multiplier(100)
    cur_tableau_set_camera_parameters(0,40,40,0,100000)
    init_position(1)
    position_set_z(1,100)
    position_set_x(1,-20)
    position_set_y(1,-20)
    cur_tableau_add_tableau_mesh(tab.troop_note_color,var001,1,0,0)
    position_set_z(1,200)
    cur_tableau_add_tableau_mesh(tab.troop_note_alpha_mask,var001,1,0,0)
    position_set_z(1,300)
    cur_tableau_add_mesh(mesh.portrait_blend_out,1,0,0)
troop_note_mesh.codeBlock = code


center_note_mesh = TableauMaterial("center_note_mesh", "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200)
def code(var001):
    set_fixed_point_multiplier(100)
    cur_tableau_set_background_color(8947848)
    cur_tableau_set_ambient_light(10,11,15)
    init_position(8)
    position_set_x(8,-210)
    position_set_y(8,200)
    position_set_z(8,300)
    cur_tableau_add_point_light(0,8,550,500,450)
    cur_tableau_set_camera_parameters(1,10,10,10,10000)
    init_position(1)
    position_set_z(1,0)
    position_set_z(1,-500)
    init_position(1)
    position_set_y(1,-100)
    position_set_x(1,-100)
    position_set_z(1,100)
    position_rotate_z(1,200)
    party_icon_002 = party_get_icon(var001)
    if party_icon_002 >= 0:
        cur_tableau_add_map_icon(party_icon_002,1,0)
    #end
    init_position(5)
    position_set_x(5,-90)
    position_set_z(5,500)
    position_set_y(5,480)
    position_rotate_x(5,-90)
    position_rotate_z(5,180)
    position_rotate_x(5,-35)
    cur_tableau_set_camera_position(5)
center_note_mesh.codeBlock = code


faction_note_mesh_for_menu = TableauMaterial("faction_note_mesh_for_menu", "pic_arms_swadian", 1024, 512, 0, 0, 450, 225)
def code(var001):
    cur_tableau_set_background_color(4294967295)
    set_fixed_point_multiplier(100)
    if is_between(var001,fac.kingdom_1,fac.kingdoms_end):
        var002 = mesh.pic_arms_swadian
        var002 += var001
        var002 -= fac.kingdom_1
        init_position(1)
        position_set_y(1,-5)
        position_set_x(1,-45)
        cur_tableau_add_mesh(var002,1,0,0)
        cur_tableau_set_camera_parameters(0,160,80,0,100000)
    #end
faction_note_mesh_for_menu.codeBlock = code


faction_note_mesh = TableauMaterial("faction_note_mesh", "pic_arms_swadian", 1024, 512, 0, 0, 500, 250)
def code(var001):
    cur_tableau_set_background_color(4294967295)
    set_fixed_point_multiplier(100)
    if is_between(var001,fac.kingdom_1,fac.kingdoms_end):
        var002 = mesh.pic_arms_swadian
        var002 += var001
        var002 -= fac.kingdom_1
        init_position(1)
        position_set_y(1,-5)
        cur_tableau_add_mesh(var002,1,0,0)
        cur_tableau_set_camera_parameters(0,100,50,0,100000)
    #end
faction_note_mesh.codeBlock = code


faction_note_mesh_banner = TableauMaterial("faction_note_mesh_banner", "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200)
def code(faction_id_001):
    set_fixed_point_multiplier(100)
    if True:
        faction_slot_002 = faction_get_slot(faction_id_001,11)
        if faction_slot_002 >= 0:
            troop_slot_003 = troop_get_slot(faction_slot_002,13)
            var004 = spr.banner_f21
            var004 += 1
            if is_between(troop_slot_003,spr.banner_a,var004):
                troop_slot_003 -= spr.banner_a
                var005 = troop_slot_003 + mesh.banner_a01
                init_position(1)
                position_set_y(1,100)
                cur_tableau_add_mesh(var005,1,0,0)
                cur_tableau_set_camera_parameters(0,210,210,0,100000)
            #end
        #end
    #end
faction_note_mesh_banner.codeBlock = code


two_factions_mesh = TableauMaterial("2_factions_mesh", "tableau_with_transparency", 1024, 1024, 0, 0, 200, 200)
def code(faction_id_001):
    faction_id_002 = store_mod(faction_id_001,128)
    faction_id_001 /= 128
    faction_id_001 += fac.player_supporters_faction
    faction_id_002 += fac.player_supporters_faction
    set_fixed_point_multiplier(100)
    if True:
        faction_slot_003 = faction_get_slot(faction_id_001,11)
        if faction_slot_003 >= 0:
            troop_slot_004 = troop_get_slot(faction_slot_003,13)
            var005 = spr.banner_f21
            var005 += 1
            if is_between(troop_slot_004,spr.banner_a,var005):
                troop_slot_004 -= spr.banner_a
                var006 = troop_slot_004 + mesh.banner_a01
                init_position(1)
                position_set_x(1,-50)
                position_set_y(1,100)
                cur_tableau_add_mesh(var006,1,0,0)
            #end
        #end
    #end
    if True:
        faction_slot_003 = faction_get_slot(faction_id_002,11)
        if faction_slot_003 >= 0:
            troop_slot_004 = troop_get_slot(faction_slot_003,13)
            var005 = spr.banner_f21
            var005 += 1
            if is_between(troop_slot_004,spr.banner_a,var005):
                troop_slot_004 -= spr.banner_a
                var006 = troop_slot_004 + mesh.banner_a01
                init_position(1)
                position_set_x(1,50)
                position_set_y(1,100)
                cur_tableau_add_mesh(var006,1,0,0)
            #end
        #end
    #end
    cur_tableau_set_camera_parameters(0,210,210,0,100000)
two_factions_mesh.codeBlock = code


color_picker = TableauMaterial("color_picker", "missiles", 32, 32, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    init_position(1)
    cur_tableau_add_mesh(mesh.color_picker,1,0,0)
    position_move_z(1,1)
    position_move_x(1,-2)
    position_move_y(1,-2)
    cur_tableau_add_mesh_with_vertex_color(mesh.white_plane,1,200,0,var001)
    cur_tableau_set_camera_parameters(0,20,20,0,100000)
color_picker.codeBlock = code


custom_banner_square_no_mesh = TableauMaterial("custom_banner_square_no_mesh", "missiles", 512, 512, 0, 0, 300, 300)
def code(var001):
    set_fixed_point_multiplier(100)
    draw_banner_to_region(var001,0,0,10000,10000,9800,9800,10000,10000,0)
    cur_tableau_set_camera_parameters(0,100,100,0,100000)
custom_banner_square_no_mesh.codeBlock = code


custom_banner_default = TableauMaterial("custom_banner_default", "missiles", 512, 256, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    draw_banner_to_region(var001,-9,-2,7450,19400,7200,18000,9000,10000,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_custom_banner,1,0,0)
    cur_tableau_set_camera_parameters(0,100,200,0,100000)
custom_banner_default.codeBlock = code


custom_banner_tall = TableauMaterial("custom_banner_tall", "missiles", 512, 256, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    draw_banner_to_region(var001,-9,12,8250,18000,8000,21000,10000,10000,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_custom_banner,1,0,0)
    cur_tableau_set_camera_parameters(0,100,200,0,100000)
custom_banner_tall.codeBlock = code


custom_banner_square = TableauMaterial("custom_banner_square", "missiles", 256, 256, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    draw_banner_to_region(var001,-11,10,7700,7700,7500,7500,8300,10000,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_custom_banner_square,1,0,0)
    cur_tableau_set_camera_parameters(0,100,100,0,100000)
custom_banner_square.codeBlock = code


custom_banner_short = TableauMaterial("custom_banner_short", "missiles", 256, 512, 0, 0, 0, 0)
def code(var001):
    set_fixed_point_multiplier(100)
    draw_banner_to_region(var001,-10,0,8050,5000,4200,4800,6600,10000,0)
    init_position(1)
    position_set_z(1,10)
    cur_tableau_add_mesh(mesh.tableau_mesh_custom_banner_short,1,0,0)
    cur_tableau_set_camera_parameters(0,100,50,0,100000)
custom_banner_short.codeBlock = code


background_selection = TableauMaterial("background_selection", "missiles", 512, 512, 0, 0, 100, 100)
def code(var001):
    troop_slot_002 = troop_get_slot(trp.player,91)
    troop_set_slot(trp.player,91,var001)
    set_fixed_point_multiplier(100)
    draw_banner_to_region(trp.player,0,0,10000,10000,9800,9800,10000,10000,0)
    cur_tableau_set_camera_parameters(0,100,100,0,100000)
    troop_set_slot(trp.player,91,troop_slot_002)
background_selection.codeBlock = code


positioning_selection = TableauMaterial("positioning_selection", "missiles", 512, 512, 0, 0, 100, 100)
def code(var001):
    troop_slot_002 = troop_get_slot(trp.player,98)
    troop_set_slot(trp.player,98,var001)
    set_fixed_point_multiplier(100)
    draw_banner_to_region(trp.player,0,0,10000,10000,9800,9800,10000,10000,0)
    cur_tableau_set_camera_parameters(0,100,100,0,100000)
    troop_set_slot(trp.player,98,troop_slot_002)
positioning_selection.codeBlock = code


retired_troop_alpha_mask = TableauMaterial("retired_troop_alpha_mask", "mat_troop_portrait_mask", 2048, 2048, 0, 0, 600, 600)
def code(var001):
    cur_tableau_set_background_color(8947848)
    cur_tableau_set_ambient_light(10,11,15)
    cur_tableau_render_as_alpha_mask()
    add_troop_to_cur_tableau_for_retirement(var001)
retired_troop_alpha_mask.codeBlock = code


retired_troop_color = TableauMaterial("retired_troop_color", "mat_troop_portrait_color", 2048, 2048, 0, 0, 600, 600)
def code(var001):
    cur_tableau_set_background_color(4293383065)
    cur_tableau_set_ambient_light(10,11,15)
    add_troop_to_cur_tableau_for_retirement(var001)
retired_troop_color.codeBlock = code


retirement_troop = TableauMaterial("retirement_troop", "tableau_with_transparency", 2048, 2048, 0, 0, 600, 600)
def code(var001):
    cur_tableau_set_background_color(4287137928)
    cur_tableau_set_ambient_light(10,11,15)
    set_fixed_point_multiplier(100)
    cur_tableau_set_camera_parameters(0,40,40,0,100000)
    init_position(1)
    position_set_z(1,100)
    position_set_x(1,-20)
    position_set_y(1,-20)
    cur_tableau_add_tableau_mesh(tab.retired_troop_color,var001,1,0,0)
    position_set_z(1,200)
    cur_tableau_add_tableau_mesh(tab.retired_troop_alpha_mask,var001,1,0,0)
retirement_troop.codeBlock = code


coop_companion_select_alpha_mask = TableauMaterial("coop_companion_select_alpha_mask", "mat_troop_portrait_mask", 1024, 1024, 0, 0, 600, 600)
def code(var001):
    cur_tableau_set_background_color(8947848)
    cur_tableau_set_ambient_light(10,11,15)
    cur_tableau_render_as_alpha_mask()
    if var001 == -1:
        add_player_to_cur_tableau_for_coop(var001)
    else:
        add_troop_to_cur_tableau_for_coop(var001)
    #end
coop_companion_select_alpha_mask.codeBlock = code


coop_companion_select_color = TableauMaterial("coop_companion_select_color", "mat_troop_portrait_color", 1024, 1024, 0, 0, 600, 600)
def code(var001):
    cur_tableau_set_background_color(1140850688)
    cur_tableau_set_ambient_light(10,11,15)
    if var001 == -1:
        add_player_to_cur_tableau_for_coop(var001)
        cur_tableau_set_background_color(1140850688)
    else:
        add_troop_to_cur_tableau_for_coop(var001)
        cur_tableau_set_background_color(1140850688)
    #end
coop_companion_select_color.codeBlock = code


coop_companion_select_0 = TableauMaterial("coop_companion_select_0", "tableau_with_transparency", 1024, 1024, 0, 0, 300, 300)
def code(var001):
    cur_tableau_set_background_color(8947848)
    cur_tableau_set_ambient_light(10,11,15)
    set_fixed_point_multiplier(100)
    cur_tableau_set_camera_parameters(0,40,40,0,100000)
    init_position(1)
    position_set_z(1,100)
    position_set_x(1,-20)
    position_set_y(1,-20)
    cur_tableau_add_tableau_mesh(tab.coop_companion_select_color,var001,1,0,0)
    position_set_z(1,200)
    cur_tableau_add_tableau_mesh(tab.coop_companion_select_alpha_mask,var001,1,0,0)
coop_companion_select_0.codeBlock = code


