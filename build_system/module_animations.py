from header_common import *
from header_animations import *

animations = [

["stand", 0, amf_client_prediction,
  [3.0, "anim_human", 50, 52, arf_use_stand_progress|arf_cyclic, 0, (0,0,0), 0.25],
  [3.0, "anim_human", 60, 62, arf_use_stand_progress|arf_cyclic, 0, (0,0,0), 0.75],
  [3.0, "anim_human", 70, 72, arf_use_stand_progress|arf_cyclic, 0, (0,0,0), 0.25],
  [3.0, "anim_human", 80, 82, arf_use_stand_progress|arf_cyclic|arf_two_handed_blade, 0, (0,0,0), 0.5],
],
["stand_man", 0, amf_client_prediction,
  [11.0, "stand_man", 0, 315, arf_use_stand_progress|arf_cyclic, 0, (0,0,0), 0.25],
],
["stand_player_first_person", 0, amf_client_prediction,
  [3.5, "anim_human", 90, 100, arf_use_stand_progress|arf_cyclic, 0, (0,0,0), 0.25],
  [3.5, "anim_human", 110, 120, arf_use_stand_progress|arf_cyclic, 0, (0,0,0), 0.25],
],
["jump", acf_enforce_lowerbody, amf_priority_jump|amf_play|amf_client_prediction|amf_continue_to_next,
  [1.0, "jump", 22, 46, arf_blend_in_1, ],
],
["jump_loop", acf_enforce_lowerbody, amf_priority_jump|amf_play|amf_client_prediction,
  [0.5, "jump_loop", 0, 14, arf_blend_in_3|arf_cyclic, ],
],
["jump_end", acf_enforce_lowerbody, amf_priority_jump_end|amf_play|amf_client_prediction,
  [0.3, "jump", 48, 55, arf_blend_in_2, ],
],
["jump_end_hard", acf_enforce_lowerbody, amf_priority_jump_end|amf_play|amf_client_prediction,
  [0.6, "jump_end_hard", 36, 54, arf_blend_in_1, ],
],
["stand_unarmed", 0, amf_client_prediction,
  [8, "noweapon_cstance", 0, 100, arf_use_stand_progress|arf_cyclic, 0, (0,0,0), 0.25],
],
["stand_single", 0, amf_client_prediction,
  [9.0, "sword_loop01", 0, 200, arf_use_stand_progress|arf_cyclic, 0, (0,0,0), 0.25],
],
["stand_greatsword", 0, amf_client_prediction,
  [6.0, "greatsword_cstance", 0, 91, arf_use_stand_progress|arf_cyclic, 0, (0,0,0), 0.25],
],
["stand_staff", 0, amf_client_prediction,
  [2.0, "staff_cstance", 0, 60, arf_use_stand_progress|arf_cyclic, ],
],
["stand_crossbow", 0, amf_client_prediction,
  [2.0, "staff_cstance", 0, 60, arf_use_stand_progress|arf_cyclic, ],
],
["turn_right", acf_enforce_lowerbody, amf_play|amf_client_prediction,
  [0.95, "stand_man", 0, 30, arf_use_stand_progress|arf_cyclic, ],
],
["turn_left", acf_enforce_lowerbody, amf_play|amf_client_prediction,
  [0.95, "stand_man", 0, 30, arf_use_stand_progress|arf_cyclic, ],
],
["turn_right_single", acf_enforce_lowerbody, amf_play|amf_client_prediction,
  [0.95, "turn_man_onehanded", 0, 23, arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["turn_left_single", acf_enforce_lowerbody, amf_play|amf_client_prediction,
  [0.95, "turn_man_onehanded", 30, 53, arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["turn_right_staff", acf_enforce_lowerbody, amf_play|amf_client_prediction,
  [0.95, "turn_man_staff", 0, 20, arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["turn_left_staff", acf_enforce_lowerbody, amf_play|amf_client_prediction,
  [0.95, "turn_man_staff", 30, 50, arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["turn_right_greatsword", acf_enforce_lowerbody, amf_play|amf_client_prediction,
  [0.95, "turn_man_greatsword", 0, 20, arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["turn_left_greatsword", acf_enforce_lowerbody, amf_play|amf_client_prediction,
  [0.95, "turn_man_greatsword", 30, 50, arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["prepare_kick_0", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction|amf_continue_to_next,
  [0.05, "kick_rightleg", 10, 12, arf_blend_in_3, ],
],
["prepare_kick_1", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction|amf_continue_to_next,
  [0.05, "kick_rightleg", 12, 12, arf_blend_in_3, ],
],
["prepare_kick_2", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction|amf_continue_to_next,
  [0.05, "kick_rightleg", 12, 12, arf_blend_in_3, ],
],
["prepare_kick_3", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction|amf_continue_to_next,
  [0.05, "kick_rightleg", 12, 12, arf_blend_in_3, ],
],
["kick_right_leg", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction,
  [0.7, "kick_rightleg", 12, 33, arf_blend_in_1, ],
],
["kick_left_leg", acf_enforce_lowerbody, amf_priority_kick|amf_play|amf_client_prediction,
  [0.7, "kick_rightleg", 12, 33, arf_blend_in_1, ],
],
["run_forward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_forward", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_forward_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_forward_staff", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_forward_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_forward_hips_right", 0, 22, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_forward_hips_left", 0, 22, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_forward_right", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_forward_right_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_right_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_forward_right_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_right_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_forward_right_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_forward_right_hips_right", 0, 22, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_forward_right_hips_left", 0, 19, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_forward_left", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_forward_left_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_left_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_forward_left_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_left_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_forward_left_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.6, "run_forward_left_hips_right", 0, 19, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_forward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_forward_left_hips_left", 0, 22, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_staff", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_twohanded", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_hips_right", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_hips_left", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_right", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_right", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_right_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_staff_right", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_right_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_twohanded_right", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_right_hips_right", 0, 19, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_right_hips_left", 0, 22, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_left", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_left", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_left_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_staff_left", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_left_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_twohanded_left", 0, 21, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_left_hips_right", 0, 22, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_backward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.7, "run_backward_left_hips_left", 0, 19, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), (0,0,0), 0.4],
],
["run_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_right", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["run_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_right_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["run_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_right_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["run_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_right_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["run_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_right_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["run_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_right_hips_left", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["run_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_left", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["run_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_left_onehanded", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["run_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_left_greatsword", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["run_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_left_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["run_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_left_hips_right", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["run_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [0.8, "run_man_left_stuff", 0, 24, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "man_walk", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "man_walk", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "man_walk_staff", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "man_walk_greatsword", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_forward_hips_right", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_forward_hips_left", 0, 32, arf_use_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_backward", 0, 30, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "man_walk", 32, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_staff", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "man_walk_staff", 32, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_greatsword", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "man_walk_greatsword", 32, 0, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_backward_hips_right", 0, 30, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_backward_hips_left", 0, 30, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_right_normal", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_right_onehanded_r", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_right_greatsword_r", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_right_staff_r", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_right_staff_r", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_right_hips_left", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_left_normal", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_left_onehanded_r", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_left_greatsword", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_left_staff", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_left_hips_right", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_left_staff", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossright_normal", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossright_onehanded", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossright_greatsword", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossright_staff", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_forward_right_hips_right", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_forward_right_hips_left", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossleft_normal", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossleft_onehanded", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossleft_greatsword", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossleft_staff", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_forward_left_hips_right", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_forward_left_hips_left", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossright_normal", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_left_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossright_onehanded", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_left_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossright_greatsword", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_left_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossright_staff", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_left_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_backward_left_hips_right", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_left_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_backward_left_hips_left", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossleft_normal", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_right_onehanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossleft_onehanded", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_right_twohanded", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossleft_greatsword", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_right_polearm", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_crossleft_staff", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_right_hips_right", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_backward_right_hips_right", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_backward_right_hips_left", acf_enforce_lowerbody, amf_use_cycle_period|amf_client_prediction,
  [1.0, "walk_backward_right_hips_left", 0, 32, arf_use_inv_walk_progress|arf_cyclic|blend_in_walk|arf_make_walk_sound, pack2f(0.4,0.9), ],
],
["walk_forward_crouch", acf_enforce_lowerbody, 0,
  [1.7, "low_walk", 0, 48, arf_use_inv_walk_progress, pack2f(0.4,0.9), ],
],
["stand_to_crouch", acf_enforce_lowerbody, 0,
  [1.3, "crouch_down", 0, 50, arf_blend_in_1, ],
],
["crouch_to_stand", acf_enforce_lowerbody, 0,
  [1.0, "crouch_down", 56, 91, arf_blend_in_1, ],
],
["equip_default", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.6, "equip_arms", 206, 221, arf_blend_in_0, ],
],
["unequip_default", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "equip_arms", 207, 200, arf_blend_in_0, ],
],
["equip_sword", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.8, "equip_sword", 0, 27, arf_blend_in_0, ],
],
["unequip_sword", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "equip_sword", 6, 0, arf_blend_in_0, ],
],
["equip_greatsword", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [1.2, "draw_greatsword", 0, 35, arf_blend_in_0, ],
],
["unequip_greatsword", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "draw_greatsword", 10, 0, arf_blend_in_0, ],
],
["ready_musket", acf_anim_length(100)|acf_rot_vertical_bow, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_crossbow,
  [1.5, "anim_human", 21300, 21320, blend_in_ready, ],
],
["release_musket", acf_anim_length(100)|acf_rot_vertical_bow, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_crossbow,
  [0.2, "anim_human", 21330, 21331, arf_blend_in_1, ],
],
["reload_musket", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
  [2.0, "anim_human", 22650, 22860, arf_blend_in_8, ],
],
["ready_swingright_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_swing_right,
  [0.35, "right_swing", 0, 15, blend_in_ready, ],
],
["release_swingright_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
  [0.5, "right_swing", 15, 41, blend_in_release, ],
],
["release_swingright_fist_continue", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
  [0.5, "right_swing", 15, 41, blend_in_release, ],
],
["blocked_swingright_fist", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
  [0.3, "anim_human", 24013, 24008, blend_in_parry, ],
],
["parried_swingright_fist", 0, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_right,
  [0.6, "anim_human", 24013, 24008, blend_in_parry, ],
],
["ready_swingleft_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_swing_left,
  [0.35, "anim_human", 24300, 24300, blend_in_ready, ],
],
["release_swingleft_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
  [0.5, "anim_human", 24300, 24335, blend_in_release, ],
],
["release_swingleft_fist_continue", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
  [0.5, "anim_human", 24300, 24335, blend_in_release, ],
],
["blocked_swingleft_fist", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
  [0.3, "anim_human", 24313, 24308, blend_in_parry, ],
],
["parried_swingleft_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_swing_left,
  [0.6, "anim_human", 24313, 24308, blend_in_parry, ],
],
["ready_direct_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_thrust,
  [0.35, "direct_fist", 0, 16, blend_in_ready, ],
],
["release_direct_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [0.5, "direct_fist", 17, 36, blend_in_release, ],
],
["release_direct_fist_continue", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [0.5, "direct_fist", 17, 36, blend_in_release, ],
],
["blocked_direct_fist", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [0.3, "anim_human", 24613, 24608, blend_in_parry, ],
],
["parried_direct_fist", 0, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [0.6, "anim_human", 24613, 24608, blend_in_parry, ],
],
["ready_uppercut_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_thrust,
  [0.35, "uppercut", 0, 17, blend_in_ready, ],
],
["release_uppercut_fist", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [0.5, "uppercut", 17, 34, blend_in_release, ],
],
["release_uppercut_fist_continue", 0, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [0.5, "uppercut", 17, 34, blend_in_release, ],
],
["blocked_uppercut_fist", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [0.3, "anim_human", 24913, 24908, blend_in_parry, ],
],
["parried_uppercut_fist", 0, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [0.6, "anim_human", 24913, 24908, blend_in_parry, ],
],

] # ANIMATIONS END
