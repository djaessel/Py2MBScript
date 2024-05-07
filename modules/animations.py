# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from animation import Animation, AnimationFlag, AnimationMasterFlag, AnimationSequence, AnimationSequenceFlag



__horse_move__ = 10000
__combat__     = 20000
__defend__     = 35000
__blow__       = 40000


__attack_parried_duration__ = 0.6
__attack_blocked_duration__ = 0.3
__attack_blocked_duration_thrust__ = __attack_blocked_duration__ + 0.3
__attack_parried_duration_thrust__ = __attack_parried_duration__ + 0.1
__defend_parry_duration_1__ = 0.6
__defend_parry_duration_2__ = 0.6
__defend_parry_duration_3__ = 0.8
__ready_durn__     = 0.35
__defend_duration__ = 0.75
__defend_keep_duration__ = 2.0
__cancel_duration__ = 0.25




# stand Animation
stand = Animation("stand")
stand.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(3.0, "anim_human", 50, 52)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
stand.add_sequence(seq0)
# sequence 1
seq1 = AnimationSequence(3.0, "anim_human", 60, 62)
seq1.add_flag(AnimationSequenceFlag.CYCLIC)
seq1.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq1.setExtraVals(7, 0.75)
stand.add_sequence(seq1)
# sequence 2
seq2 = AnimationSequence(3.0, "anim_human", 70, 72)
seq2.add_flag(AnimationSequenceFlag.CYCLIC)
seq2.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq2.setExtraVals(7, 0.25)
stand.add_sequence(seq2)
# sequence 3
seq3 = AnimationSequence(3.0, "anim_human", 80, 82)
seq3.add_flag(AnimationSequenceFlag.TWO_HANDED_BLADE)
seq3.add_flag(AnimationSequenceFlag.CYCLIC)
seq3.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq3.setExtraVals(7, 0.5)
stand.add_sequence(seq3)


# stand_man Animation
stand_man = Animation("stand_man")
stand_man.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(11.0, "stand_man", 0, 315)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
stand_man.add_sequence(seq0)


# stand_player_first_person Animation
stand_player_first_person = Animation("stand_player_first_person")
stand_player_first_person.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(3.5, "anim_human", 90, 100)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
stand_player_first_person.add_sequence(seq0)
# sequence 1
seq1 = AnimationSequence(3.5, "anim_human", 110, 120)
seq1.add_flag(AnimationSequenceFlag.CYCLIC)
seq1.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq1.setExtraVals(7, 0.25)
stand_player_first_person.add_sequence(seq1)


# jump Animation
jump = Animation("jump")
jump.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
jump.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP)
jump.add_master_flag(AnimationMasterFlag.PRIORITY_RIDE)
jump.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
jump.add_master_flag(AnimationMasterFlag.PLAY)
jump.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(1.0, "jump", 22, 46)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
jump.add_sequence(seq0)


# jump_loop Animation
jump_loop = Animation("jump_loop")
jump_loop.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
jump_loop.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP)
jump_loop.add_master_flag(AnimationMasterFlag.PRIORITY_RIDE)
jump_loop.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
jump_loop.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.5, "jump_loop", 0, 14)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
jump_loop.add_sequence(seq0)


# jump_end Animation
jump_end = Animation("jump_end")
jump_end.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
jump_end.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
jump_end.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP_END)
jump_end.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
jump_end.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "jump", 48, 55)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
jump_end.add_sequence(seq0)


# jump_end_hard Animation
jump_end_hard = Animation("jump_end_hard")
jump_end_hard.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
jump_end_hard.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
jump_end_hard.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP_END)
jump_end_hard.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
jump_end_hard.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "jump_end_hard", 36, 54)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
jump_end_hard.add_sequence(seq0)


# stand_unarmed Animation
stand_unarmed = Animation("stand_unarmed")
stand_unarmed.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(8.0, "noweapon_cstance", 0, 100)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
stand_unarmed.add_sequence(seq0)


# stand_single Animation
stand_single = Animation("stand_single")
stand_single.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(9.0, "sword_loop01", 0, 200)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
stand_single.add_sequence(seq0)


# stand_greatsword Animation
stand_greatsword = Animation("stand_greatsword")
stand_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(6.0, "greatsword_cstance", 0, 91)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
stand_greatsword.add_sequence(seq0)


# stand_staff Animation
stand_staff = Animation("stand_staff")
stand_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "staff_cstance", 0, 60)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
stand_staff.add_sequence(seq0)


# stand_crossbow Animation
stand_crossbow = Animation("stand_crossbow")
stand_crossbow.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "staff_cstance", 0, 60)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
stand_crossbow.add_sequence(seq0)


# turn_right Animation
turn_right = Animation("turn_right")
turn_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
turn_right.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.95, "stand_man", 0, 30)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
turn_right.add_sequence(seq0)


# turn_left Animation
turn_left = Animation("turn_left")
turn_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
turn_left.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.95, "stand_man", 0, 30)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
turn_left.add_sequence(seq0)


# turn_right_single Animation
turn_right_single = Animation("turn_right_single")
turn_right_single.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_right_single.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
turn_right_single.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_onehanded", 0, 23)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_right_single.add_sequence(seq0)


# turn_left_single Animation
turn_left_single = Animation("turn_left_single")
turn_left_single.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_left_single.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
turn_left_single.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_onehanded", 30, 53)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_left_single.add_sequence(seq0)


# turn_right_staff Animation
turn_right_staff = Animation("turn_right_staff")
turn_right_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_right_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
turn_right_staff.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_staff", 0, 20)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_right_staff.add_sequence(seq0)


# turn_left_staff Animation
turn_left_staff = Animation("turn_left_staff")
turn_left_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_left_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
turn_left_staff.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_staff", 30, 50)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_left_staff.add_sequence(seq0)


# turn_right_greatsword Animation
turn_right_greatsword = Animation("turn_right_greatsword")
turn_right_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_right_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
turn_right_greatsword.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_greatsword", 0, 20)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_right_greatsword.add_sequence(seq0)


# turn_left_greatsword Animation
turn_left_greatsword = Animation("turn_left_greatsword")
turn_left_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_left_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
turn_left_greatsword.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_greatsword", 30, 50)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_left_greatsword.add_sequence(seq0)


# prepare_kick_0 Animation
prepare_kick_0 = Animation("prepare_kick_0")
prepare_kick_0.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
prepare_kick_0.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
prepare_kick_0.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP_END)
prepare_kick_0.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
prepare_kick_0.add_master_flag(AnimationMasterFlag.PLAY)
prepare_kick_0.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.05, "kick_rightleg", 10, 12)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
prepare_kick_0.add_sequence(seq0)


# prepare_kick_1 Animation
prepare_kick_1 = Animation("prepare_kick_1")
prepare_kick_1.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
prepare_kick_1.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
prepare_kick_1.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP_END)
prepare_kick_1.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
prepare_kick_1.add_master_flag(AnimationMasterFlag.PLAY)
prepare_kick_1.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.05, "kick_rightleg", 12, 12)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
prepare_kick_1.add_sequence(seq0)


# prepare_kick_2 Animation
prepare_kick_2 = Animation("prepare_kick_2")
prepare_kick_2.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
prepare_kick_2.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
prepare_kick_2.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP_END)
prepare_kick_2.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
prepare_kick_2.add_master_flag(AnimationMasterFlag.PLAY)
prepare_kick_2.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.05, "kick_rightleg", 12, 12)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
prepare_kick_2.add_sequence(seq0)


# prepare_kick_3 Animation
prepare_kick_3 = Animation("prepare_kick_3")
prepare_kick_3.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
prepare_kick_3.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
prepare_kick_3.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP_END)
prepare_kick_3.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
prepare_kick_3.add_master_flag(AnimationMasterFlag.PLAY)
prepare_kick_3.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.05, "kick_rightleg", 12, 12)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
prepare_kick_3.add_sequence(seq0)


# kick_right_leg Animation
kick_right_leg = Animation("kick_right_leg")
kick_right_leg.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
kick_right_leg.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
kick_right_leg.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP_END)
kick_right_leg.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
kick_right_leg.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.7, "kick_rightleg", 12, 33)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
kick_right_leg.add_sequence(seq0)


# kick_left_leg Animation
kick_left_leg = Animation("kick_left_leg")
kick_left_leg.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
kick_left_leg.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
kick_left_leg.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP_END)
kick_left_leg.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
kick_left_leg.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.7, "kick_rightleg", 12, 33)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
kick_left_leg.add_sequence(seq0)


# run_forward Animation
run_forward = Animation("run_forward")
run_forward.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_forward", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward.add_sequence(seq0)


# run_forward_onehanded Animation
run_forward_onehanded = Animation("run_forward_onehanded")
run_forward_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_forward_onehanded", 0, 24)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_onehanded.add_sequence(seq0)


# run_forward_staff Animation
run_forward_staff = Animation("run_forward_staff")
run_forward_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_staff.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_forward_staff", 0, 24)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_staff.add_sequence(seq0)


# run_forward_greatsword Animation
run_forward_greatsword = Animation("run_forward_greatsword")
run_forward_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_greatsword.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_forward_greatsword", 0, 24)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_greatsword.add_sequence(seq0)


# run_forward_hips_right Animation
run_forward_hips_right = Animation("run_forward_hips_right")
run_forward_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_forward_hips_right", 0, 22)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_hips_right.add_sequence(seq0)


# run_forward_hips_left Animation
run_forward_hips_left = Animation("run_forward_hips_left")
run_forward_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_forward_hips_left", 0, 22)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_hips_left.add_sequence(seq0)


# run_forward_right Animation
run_forward_right = Animation("run_forward_right")
run_forward_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_forward_right", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_right.add_sequence(seq0)


# run_forward_right_onehanded Animation
run_forward_right_onehanded = Animation("run_forward_right_onehanded")
run_forward_right_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_right_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_right_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_forward_right_onehanded", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_right_onehanded.add_sequence(seq0)


# run_forward_right_staff Animation
run_forward_right_staff = Animation("run_forward_right_staff")
run_forward_right_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_right_staff.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_right_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_forward_right_stuff", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_right_staff.add_sequence(seq0)


# run_forward_right_greatsword Animation
run_forward_right_greatsword = Animation("run_forward_right_greatsword")
run_forward_right_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_right_greatsword.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_right_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_forward_right_greatsword", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_right_greatsword.add_sequence(seq0)


# run_forward_right_hips_right Animation
run_forward_right_hips_right = Animation("run_forward_right_hips_right")
run_forward_right_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_right_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_right_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_forward_right_hips_right", 0, 22)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_right_hips_right.add_sequence(seq0)


# run_forward_right_hips_left Animation
run_forward_right_hips_left = Animation("run_forward_right_hips_left")
run_forward_right_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_right_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_right_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_forward_right_hips_left", 0, 19)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_right_hips_left.add_sequence(seq0)


# run_forward_left Animation
run_forward_left = Animation("run_forward_left")
run_forward_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_forward_left", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_left.add_sequence(seq0)


# run_forward_left_onehanded Animation
run_forward_left_onehanded = Animation("run_forward_left_onehanded")
run_forward_left_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_left_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_left_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_forward_left_onehanded", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_left_onehanded.add_sequence(seq0)


# run_forward_left_staff Animation
run_forward_left_staff = Animation("run_forward_left_staff")
run_forward_left_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_left_staff.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_left_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_forward_left_stuff", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_left_staff.add_sequence(seq0)


# run_forward_left_greatsword Animation
run_forward_left_greatsword = Animation("run_forward_left_greatsword")
run_forward_left_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_left_greatsword.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_left_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_forward_left_greatsword", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_left_greatsword.add_sequence(seq0)


# run_forward_left_hips_right Animation
run_forward_left_hips_right = Animation("run_forward_left_hips_right")
run_forward_left_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_left_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_left_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.6, "run_forward_left_hips_right", 0, 19)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_left_hips_right.add_sequence(seq0)


# run_forward_left_hips_left Animation
run_forward_left_hips_left = Animation("run_forward_left_hips_left")
run_forward_left_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_left_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_left_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_forward_left_hips_left", 0, 22)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_left_hips_left.add_sequence(seq0)


# run_backward Animation
run_backward = Animation("run_backward")
run_backward.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward.add_sequence(seq0)


# run_backward_onehanded Animation
run_backward_onehanded = Animation("run_backward_onehanded")
run_backward_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_onehanded.add_sequence(seq0)


# run_backward_staff Animation
run_backward_staff = Animation("run_backward_staff")
run_backward_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_staff.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_staff", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_staff.add_sequence(seq0)


# run_backward_greatsword Animation
run_backward_greatsword = Animation("run_backward_greatsword")
run_backward_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_greatsword.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_twohanded", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_greatsword.add_sequence(seq0)


# run_backward_hips_right Animation
run_backward_hips_right = Animation("run_backward_hips_right")
run_backward_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_hips_right", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_hips_right.add_sequence(seq0)


# run_backward_hips_left Animation
run_backward_hips_left = Animation("run_backward_hips_left")
run_backward_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_hips_left", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_hips_left.add_sequence(seq0)


# run_backward_right Animation
run_backward_right = Animation("run_backward_right")
run_backward_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_right", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_right.add_sequence(seq0)


# run_backward_right_onehanded Animation
run_backward_right_onehanded = Animation("run_backward_right_onehanded")
run_backward_right_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_right_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_right_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_right", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_right_onehanded.add_sequence(seq0)


# run_backward_right_staff Animation
run_backward_right_staff = Animation("run_backward_right_staff")
run_backward_right_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_right_staff.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_right_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_staff_right", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_right_staff.add_sequence(seq0)


# run_backward_right_greatsword Animation
run_backward_right_greatsword = Animation("run_backward_right_greatsword")
run_backward_right_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_right_greatsword.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_right_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_twohanded_right", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_right_greatsword.add_sequence(seq0)


# run_backward_right_hips_right Animation
run_backward_right_hips_right = Animation("run_backward_right_hips_right")
run_backward_right_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_right_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_right_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_right_hips_right", 0, 19)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_right_hips_right.add_sequence(seq0)


# run_backward_right_hips_left Animation
run_backward_right_hips_left = Animation("run_backward_right_hips_left")
run_backward_right_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_right_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_right_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_right_hips_left", 0, 22)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_right_hips_left.add_sequence(seq0)


# run_backward_left Animation
run_backward_left = Animation("run_backward_left")
run_backward_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_left", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_left.add_sequence(seq0)


# run_backward_left_onehanded Animation
run_backward_left_onehanded = Animation("run_backward_left_onehanded")
run_backward_left_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_left_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_left_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_left", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_left_onehanded.add_sequence(seq0)


# run_backward_left_staff Animation
run_backward_left_staff = Animation("run_backward_left_staff")
run_backward_left_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_left_staff.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_left_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_staff_left", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_left_staff.add_sequence(seq0)


# run_backward_left_greatsword Animation
run_backward_left_greatsword = Animation("run_backward_left_greatsword")
run_backward_left_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_left_greatsword.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_left_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_twohanded_left", 0, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_left_greatsword.add_sequence(seq0)


# run_backward_left_hips_right Animation
run_backward_left_hips_right = Animation("run_backward_left_hips_right")
run_backward_left_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_left_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_left_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_left_hips_right", 0, 22)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_left_hips_right.add_sequence(seq0)


# run_backward_left_hips_left Animation
run_backward_left_hips_left = Animation("run_backward_left_hips_left")
run_backward_left_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_left_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_left_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_left_hips_left", 0, 19)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_left_hips_left.add_sequence(seq0)


# run_right Animation
run_right = Animation("run_right")
run_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_right", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_right.add_sequence(seq0)


# run_right_onehanded Animation
run_right_onehanded = Animation("run_right_onehanded")
run_right_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_right_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_right_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_right_onehanded", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_right_onehanded.add_sequence(seq0)


# run_right_twohanded Animation
run_right_twohanded = Animation("run_right_twohanded")
run_right_twohanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_right_twohanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_right_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_right_greatsword", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_right_twohanded.add_sequence(seq0)


# run_right_polearm Animation
run_right_polearm = Animation("run_right_polearm")
run_right_polearm.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_right_polearm.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_right_polearm.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_right_stuff", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_right_polearm.add_sequence(seq0)


# run_right_hips_right Animation
run_right_hips_right = Animation("run_right_hips_right")
run_right_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_right_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_right_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_right_stuff", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_right_hips_right.add_sequence(seq0)


# run_right_hips_left Animation
run_right_hips_left = Animation("run_right_hips_left")
run_right_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_right_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_right_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_right_hips_left", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_right_hips_left.add_sequence(seq0)


# run_left Animation
run_left = Animation("run_left")
run_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_left", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_left.add_sequence(seq0)


# run_left_onehanded Animation
run_left_onehanded = Animation("run_left_onehanded")
run_left_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_left_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_left_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_left_onehanded", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_left_onehanded.add_sequence(seq0)


# run_left_twohanded Animation
run_left_twohanded = Animation("run_left_twohanded")
run_left_twohanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_left_twohanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_left_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_left_greatsword", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_left_twohanded.add_sequence(seq0)


# run_left_polearm Animation
run_left_polearm = Animation("run_left_polearm")
run_left_polearm.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_left_polearm.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_left_polearm.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_left_stuff", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_left_polearm.add_sequence(seq0)


# run_left_hips_right Animation
run_left_hips_right = Animation("run_left_hips_right")
run_left_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_left_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_left_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_left_hips_right", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_left_hips_right.add_sequence(seq0)


# run_left_hips_left Animation
run_left_hips_left = Animation("run_left_hips_left")
run_left_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_left_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_left_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_left_stuff", 0, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_left_hips_left.add_sequence(seq0)


# walk_forward Animation
walk_forward = Animation("walk_forward")
walk_forward.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "man_walk", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward.add_sequence(seq0)


# walk_forward_onehanded Animation
walk_forward_onehanded = Animation("walk_forward_onehanded")
walk_forward_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "man_walk", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_onehanded.add_sequence(seq0)


# walk_forward_staff Animation
walk_forward_staff = Animation("walk_forward_staff")
walk_forward_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_staff.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "man_walk_staff", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_staff.add_sequence(seq0)


# walk_forward_greatsword Animation
walk_forward_greatsword = Animation("walk_forward_greatsword")
walk_forward_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_greatsword.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "man_walk_greatsword", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_greatsword.add_sequence(seq0)


# walk_forward_hips_right Animation
walk_forward_hips_right = Animation("walk_forward_hips_right")
walk_forward_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_forward_hips_right", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_hips_right.add_sequence(seq0)


# walk_forward_hips_left Animation
walk_forward_hips_left = Animation("walk_forward_hips_left")
walk_forward_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_forward_hips_left", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_hips_left.add_sequence(seq0)


# walk_backward Animation
walk_backward = Animation("walk_backward")
walk_backward.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_backward", 0, 30)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward.add_sequence(seq0)


# walk_backward_onehanded Animation
walk_backward_onehanded = Animation("walk_backward_onehanded")
walk_backward_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "man_walk", 32, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_onehanded.add_sequence(seq0)


# walk_backward_staff Animation
walk_backward_staff = Animation("walk_backward_staff")
walk_backward_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_staff.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "man_walk_staff", 32, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_staff.add_sequence(seq0)


# walk_backward_greatsword Animation
walk_backward_greatsword = Animation("walk_backward_greatsword")
walk_backward_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_greatsword.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "man_walk_greatsword", 32, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_greatsword.add_sequence(seq0)


# walk_backward_hips_right Animation
walk_backward_hips_right = Animation("walk_backward_hips_right")
walk_backward_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_backward_hips_right", 0, 30)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_hips_right.add_sequence(seq0)


# walk_backward_hips_left Animation
walk_backward_hips_left = Animation("walk_backward_hips_left")
walk_backward_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_backward_hips_left", 0, 30)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_hips_left.add_sequence(seq0)


# walk_right Animation
walk_right = Animation("walk_right")
walk_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_right_normal", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_right.add_sequence(seq0)


# walk_right_onehanded Animation
walk_right_onehanded = Animation("walk_right_onehanded")
walk_right_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_right_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_right_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_right_onehanded_r", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_right_onehanded.add_sequence(seq0)


# walk_right_twohanded Animation
walk_right_twohanded = Animation("walk_right_twohanded")
walk_right_twohanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_right_twohanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_right_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_right_greatsword_r", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_right_twohanded.add_sequence(seq0)


# walk_right_polearm Animation
walk_right_polearm = Animation("walk_right_polearm")
walk_right_polearm.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_right_polearm.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_right_polearm.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_right_staff_r", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_right_polearm.add_sequence(seq0)


# walk_right_hips_right Animation
walk_right_hips_right = Animation("walk_right_hips_right")
walk_right_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_right_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_right_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_right_staff_r", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_right_hips_right.add_sequence(seq0)


# walk_right_hips_left Animation
walk_right_hips_left = Animation("walk_right_hips_left")
walk_right_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_right_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_right_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_right_hips_left", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_right_hips_left.add_sequence(seq0)


# walk_left Animation
walk_left = Animation("walk_left")
walk_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_left_normal", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_left.add_sequence(seq0)


# walk_left_onehanded Animation
walk_left_onehanded = Animation("walk_left_onehanded")
walk_left_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_left_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_left_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_left_onehanded_r", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_left_onehanded.add_sequence(seq0)


# walk_left_twohanded Animation
walk_left_twohanded = Animation("walk_left_twohanded")
walk_left_twohanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_left_twohanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_left_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_left_greatsword", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_left_twohanded.add_sequence(seq0)


# walk_left_polearm Animation
walk_left_polearm = Animation("walk_left_polearm")
walk_left_polearm.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_left_polearm.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_left_polearm.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_left_staff", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_left_polearm.add_sequence(seq0)


# walk_left_hips_right Animation
walk_left_hips_right = Animation("walk_left_hips_right")
walk_left_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_left_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_left_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_left_hips_right", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_left_hips_right.add_sequence(seq0)


# walk_left_hips_left Animation
walk_left_hips_left = Animation("walk_left_hips_left")
walk_left_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_left_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_left_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_left_staff", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_left_hips_left.add_sequence(seq0)


# walk_forward_right Animation
walk_forward_right = Animation("walk_forward_right")
walk_forward_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_normal", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_right.add_sequence(seq0)


# walk_forward_right_onehanded Animation
walk_forward_right_onehanded = Animation("walk_forward_right_onehanded")
walk_forward_right_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_right_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_right_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_onehanded", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_right_onehanded.add_sequence(seq0)


# walk_forward_right_twohanded Animation
walk_forward_right_twohanded = Animation("walk_forward_right_twohanded")
walk_forward_right_twohanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_right_twohanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_right_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_greatsword", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_right_twohanded.add_sequence(seq0)


# walk_forward_right_polearm Animation
walk_forward_right_polearm = Animation("walk_forward_right_polearm")
walk_forward_right_polearm.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_right_polearm.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_right_polearm.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_staff", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_right_polearm.add_sequence(seq0)


# walk_forward_right_hips_right Animation
walk_forward_right_hips_right = Animation("walk_forward_right_hips_right")
walk_forward_right_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_right_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_right_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_forward_right_hips_right", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_right_hips_right.add_sequence(seq0)


# walk_forward_right_hips_left Animation
walk_forward_right_hips_left = Animation("walk_forward_right_hips_left")
walk_forward_right_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_right_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_right_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_forward_right_hips_left", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_right_hips_left.add_sequence(seq0)


# walk_forward_left Animation
walk_forward_left = Animation("walk_forward_left")
walk_forward_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_normal", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_left.add_sequence(seq0)


# walk_forward_left_onehanded Animation
walk_forward_left_onehanded = Animation("walk_forward_left_onehanded")
walk_forward_left_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_left_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_left_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_onehanded", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_left_onehanded.add_sequence(seq0)


# walk_forward_left_twohanded Animation
walk_forward_left_twohanded = Animation("walk_forward_left_twohanded")
walk_forward_left_twohanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_left_twohanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_left_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_greatsword", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_left_twohanded.add_sequence(seq0)


# walk_forward_left_polearm Animation
walk_forward_left_polearm = Animation("walk_forward_left_polearm")
walk_forward_left_polearm.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_left_polearm.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_left_polearm.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_staff", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_left_polearm.add_sequence(seq0)


# walk_forward_left_hips_right Animation
walk_forward_left_hips_right = Animation("walk_forward_left_hips_right")
walk_forward_left_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_left_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_left_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_forward_left_hips_right", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_left_hips_right.add_sequence(seq0)


# walk_forward_left_hips_left Animation
walk_forward_left_hips_left = Animation("walk_forward_left_hips_left")
walk_forward_left_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_left_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_left_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_forward_left_hips_left", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_left_hips_left.add_sequence(seq0)


# walk_backward_left Animation
walk_backward_left = Animation("walk_backward_left")
walk_backward_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_normal", 32, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_left.add_sequence(seq0)


# walk_backward_left_onehanded Animation
walk_backward_left_onehanded = Animation("walk_backward_left_onehanded")
walk_backward_left_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_left_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_left_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_onehanded", 32, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_left_onehanded.add_sequence(seq0)


# walk_backward_left_twohanded Animation
walk_backward_left_twohanded = Animation("walk_backward_left_twohanded")
walk_backward_left_twohanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_left_twohanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_left_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_greatsword", 32, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_left_twohanded.add_sequence(seq0)


# walk_backward_left_polearm Animation
walk_backward_left_polearm = Animation("walk_backward_left_polearm")
walk_backward_left_polearm.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_left_polearm.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_left_polearm.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_staff", 32, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_left_polearm.add_sequence(seq0)


# walk_backward_left_hips_right Animation
walk_backward_left_hips_right = Animation("walk_backward_left_hips_right")
walk_backward_left_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_left_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_left_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_backward_left_hips_right", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_left_hips_right.add_sequence(seq0)


# walk_backward_left_hips_left Animation
walk_backward_left_hips_left = Animation("walk_backward_left_hips_left")
walk_backward_left_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_left_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_left_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_backward_left_hips_left", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_left_hips_left.add_sequence(seq0)


# walk_backward_right Animation
walk_backward_right = Animation("walk_backward_right")
walk_backward_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_normal", 32, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_right.add_sequence(seq0)


# walk_backward_right_onehanded Animation
walk_backward_right_onehanded = Animation("walk_backward_right_onehanded")
walk_backward_right_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_right_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_right_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_onehanded", 32, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_right_onehanded.add_sequence(seq0)


# walk_backward_right_twohanded Animation
walk_backward_right_twohanded = Animation("walk_backward_right_twohanded")
walk_backward_right_twohanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_right_twohanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_right_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_greatsword", 32, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_right_twohanded.add_sequence(seq0)


# walk_backward_right_polearm Animation
walk_backward_right_polearm = Animation("walk_backward_right_polearm")
walk_backward_right_polearm.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_right_polearm.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_right_polearm.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_staff", 32, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_right_polearm.add_sequence(seq0)


# walk_backward_right_hips_right Animation
walk_backward_right_hips_right = Animation("walk_backward_right_hips_right")
walk_backward_right_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_right_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_right_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_backward_right_hips_right", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_right_hips_right.add_sequence(seq0)


# walk_backward_right_hips_left Animation
walk_backward_right_hips_left = Animation("walk_backward_right_hips_left")
walk_backward_right_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_right_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_right_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_backward_right_hips_left", 0, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_right_hips_left.add_sequence(seq0)


# walk_forward_crouch Animation
walk_forward_crouch = Animation("walk_forward_crouch")
walk_forward_crouch.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
# sequence 0
seq0 = AnimationSequence(1.7, "low_walk", 0, 48)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_crouch.add_sequence(seq0)


# stand_to_crouch Animation
stand_to_crouch = Animation("stand_to_crouch")
stand_to_crouch.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
# sequence 0
seq0 = AnimationSequence(1.3, "crouch_down", 0, 50)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
stand_to_crouch.add_sequence(seq0)


# crouch_to_stand Animation
crouch_to_stand = Animation("crouch_to_stand")
crouch_to_stand.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
# sequence 0
seq0 = AnimationSequence(1.0, "crouch_down", 56, 91)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
crouch_to_stand.add_sequence(seq0)


# ride_0 Animation
ride_0 = Animation("ride_0")
ride_0.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
ride_0.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(15.0, "stand_onhorse", 0, 456)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
ride_0.add_sequence(seq0)


# ride_1 Animation
ride_1 = Animation("ride_1")
ride_1.add_flag(AnimationFlag.SYNC_WITH_HORSE)
ride_1.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
ride_1.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human_02", 0, 31)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
ride_1.add_sequence(seq0)


# lancer_ride_1 Animation
lancer_ride_1 = Animation("lancer_ride_1")
lancer_ride_1.add_flag(AnimationFlag.SYNC_WITH_HORSE)
lancer_ride_1.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
lancer_ride_1.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP)
lancer_ride_1.add_master_flag(AnimationMasterFlag.PRIORITY_RIDE)
lancer_ride_1.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
lancer_ride_1.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.0, "lancer_ride1", 0, 31)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
lancer_ride_1.add_sequence(seq0)


# lancer_charge_parried Animation
lancer_charge_parried = Animation("lancer_charge_parried")
lancer_charge_parried.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
lancer_charge_parried.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
lancer_charge_parried.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
lancer_charge_parried.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
lancer_charge_parried.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
lancer_charge_parried.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
lancer_charge_parried.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 10210, 10220)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_32)
lancer_charge_parried.add_sequence(seq0)


# ride_2 Animation
ride_2 = Animation("ride_2")
ride_2.add_flag(AnimationFlag.SYNC_WITH_HORSE)
ride_2.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
ride_2.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human_02", 50, 69)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
ride_2.add_sequence(seq0)


# ride_3 Animation
ride_3 = Animation("ride_3")
ride_3.add_flag(AnimationFlag.SYNC_WITH_HORSE)
ride_3.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
ride_3.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human_02", 100, 116)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
ride_3.add_sequence(seq0)


# ride_4 Animation
ride_4 = Animation("ride_4")
ride_4.add_flag(AnimationFlag.SYNC_WITH_HORSE)
ride_4.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
ride_4.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.5, "anim_human_02", 150, 165)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_32)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
ride_4.add_sequence(seq0)


# lancer_ride_4 Animation
lancer_ride_4 = Animation("lancer_ride_4", 30)
lancer_ride_4.add_flag(AnimationFlag.SYNC_WITH_HORSE)
lancer_ride_4.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
lancer_ride_4.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
lancer_ride_4.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP)
lancer_ride_4.add_master_flag(AnimationMasterFlag.PRIORITY_RIDE)
lancer_ride_4.add_master_flag(AnimationMasterFlag.RIDER_ROT_COUCHED_LANCE)
lancer_ride_4.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
lancer_ride_4.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.5, "lancer_ride4", 0, 15)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_128)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
lancer_ride_4.add_sequence(seq0)


# lancer_ride_4_no_shield Animation
lancer_ride_4_no_shield = Animation("lancer_ride_4_no_shield", 30)
lancer_ride_4_no_shield.add_flag(AnimationFlag.SYNC_WITH_HORSE)
lancer_ride_4_no_shield.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
lancer_ride_4_no_shield.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
lancer_ride_4_no_shield.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP)
lancer_ride_4_no_shield.add_master_flag(AnimationMasterFlag.PRIORITY_RIDE)
lancer_ride_4_no_shield.add_master_flag(AnimationMasterFlag.RIDER_ROT_COUCHED_LANCE)
lancer_ride_4_no_shield.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
lancer_ride_4_no_shield.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.5, "lancer_ride4_no_shield", 0, 15)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_128)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
lancer_ride_4_no_shield.add_sequence(seq0)


# ride_rear Animation
ride_rear = Animation("ride_rear")
ride_rear.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
ride_rear.add_flag(AnimationFlag.IGNORE_SLOPE)
ride_rear.add_master_flag(AnimationMasterFlag.PRIORITY_MOUNT)
ride_rear.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
ride_rear.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.7, "anim_human_02", 265, 297)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
ride_rear.add_sequence(seq0)


# ride_spur Animation
ride_spur = Animation("ride_spur")
ride_spur.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
ride_spur.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP)
ride_spur.add_master_flag(AnimationMasterFlag.PRIORITY_RIDE)
ride_spur.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 10860, 10865)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
ride_spur.add_sequence(seq0)


# ride_jump Animation
ride_jump = Animation("ride_jump")
ride_jump.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
ride_jump.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.6, "anim_human_02", 205, 222)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_4)
ride_jump.add_sequence(seq0)


# ride_jump_end Animation
ride_jump_end = Animation("ride_jump_end")
ride_jump_end.add_flag(AnimationFlag.ENFORCE_ALL)
ride_jump_end.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.1, "anim_human_02", 222, 224)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_16)
ride_jump_end.add_sequence(seq0)


# ride_turn_right Animation
ride_turn_right = Animation("ride_turn_right")
ride_turn_right.add_flag(AnimationFlag.SYNC_WITH_HORSE)
ride_turn_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
ride_turn_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human_02", 500, 533)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
ride_turn_right.add_sequence(seq0)


# ride_turn_left Animation
ride_turn_left = Animation("ride_turn_left")
ride_turn_left.add_flag(AnimationFlag.SYNC_WITH_HORSE)
ride_turn_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
ride_turn_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human_02", 450, 483)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
ride_turn_left.add_sequence(seq0)


# mount_horse Animation
mount_horse = Animation("mount_horse")
mount_horse.add_flag(AnimationFlag.ENFORCE_ALL)
mount_horse.add_master_flag(AnimationMasterFlag.PRIORITY_MOUNT)
mount_horse.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
mount_horse.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.3, "anim_human", 11003, 11045)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
mount_horse.add_sequence(seq0)


# dismount_horse Animation
dismount_horse = Animation("dismount_horse")
dismount_horse.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
dismount_horse.add_flag(AnimationFlag.DISPLACE_POSITION)
dismount_horse.add_master_flag(AnimationMasterFlag.PRIORITY_MOUNT)
dismount_horse.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
dismount_horse.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
dismount_horse.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.1, "anim_human", 11103, 11145)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
seq0.setExtraVals(4, -0.5)
dismount_horse.add_sequence(seq0)


# lancer_ride_0 Animation
lancer_ride_0 = Animation("lancer_ride_0")
lancer_ride_0.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
lancer_ride_0.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP)
lancer_ride_0.add_master_flag(AnimationMasterFlag.PRIORITY_RIDE)
lancer_ride_0.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
lancer_ride_0.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(43.0, "stand_onhorse_staff", 0, 1300)
seq0.add_flag(AnimationSequenceFlag.LANCER)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
lancer_ride_0.add_sequence(seq0)


# equip_default Animation
equip_default = Animation("equip_default")
equip_default.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_default.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_default.add_master_flag(AnimationMasterFlag.PLAY)
equip_default.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "equip_arms", 206, 221)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_default.add_sequence(seq0)


# unequip_default Animation
unequip_default = Animation("unequip_default")
unequip_default.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_default.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_default.add_master_flag(AnimationMasterFlag.PLAY)
unequip_default.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_arms", 207, 200)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_default.add_sequence(seq0)


# equip_sword Animation
equip_sword = Animation("equip_sword")
equip_sword.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_sword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_sword.add_master_flag(AnimationMasterFlag.PLAY)
equip_sword.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "equip_sword", 0, 27)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_sword.add_sequence(seq0)


# unequip_sword Animation
unequip_sword = Animation("unequip_sword")
unequip_sword.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_sword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_sword.add_master_flag(AnimationMasterFlag.PLAY)
unequip_sword.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_sword", 6, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_sword.add_sequence(seq0)


# equip_greatsword Animation
equip_greatsword = Animation("equip_greatsword")
equip_greatsword.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_greatsword.add_master_flag(AnimationMasterFlag.PLAY)
equip_greatsword.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(1.2, "draw_greatsword", 0, 35)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_greatsword.add_sequence(seq0)


# unequip_greatsword Animation
unequip_greatsword = Animation("unequip_greatsword")
unequip_greatsword.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_greatsword.add_master_flag(AnimationMasterFlag.PLAY)
unequip_greatsword.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "draw_greatsword", 10, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_greatsword.add_sequence(seq0)


# equip_axe_left_hip Animation
equip_axe_left_hip = Animation("equip_axe_left_hip")
equip_axe_left_hip.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_axe_left_hip.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_axe_left_hip.add_master_flag(AnimationMasterFlag.PLAY)
equip_axe_left_hip.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "draw_axe", 0, 16)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_axe_left_hip.add_sequence(seq0)


# unequip_axe_left_hip Animation
unequip_axe_left_hip = Animation("unequip_axe_left_hip")
unequip_axe_left_hip.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_axe_left_hip.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_axe_left_hip.add_master_flag(AnimationMasterFlag.PLAY)
unequip_axe_left_hip.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "draw_axe", 6, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_axe_left_hip.add_sequence(seq0)


# equip_crossbow Animation
equip_crossbow = Animation("equip_crossbow")
equip_crossbow.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_crossbow.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_crossbow.add_master_flag(AnimationMasterFlag.PLAY)
equip_crossbow.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(1.2, "equip_greataxe", 0, 20)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_crossbow.add_sequence(seq0)


# unequip_crossbow Animation
unequip_crossbow = Animation("unequip_crossbow")
unequip_crossbow.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_crossbow.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_crossbow.add_master_flag(AnimationMasterFlag.PLAY)
unequip_crossbow.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_greataxe", 10, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_crossbow.add_sequence(seq0)


# equip_spear Animation
equip_spear = Animation("equip_spear")
equip_spear.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_spear.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_spear.add_master_flag(AnimationMasterFlag.PLAY)
equip_spear.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "equip_arms", 17, 34)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_spear.add_sequence(seq0)


# unequip_spear Animation
unequip_spear = Animation("unequip_spear")
unequip_spear.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_spear.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_spear.add_master_flag(AnimationMasterFlag.PLAY)
unequip_spear.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_arms", 15, 10)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_spear.add_sequence(seq0)


# equip_dagger_front_left Animation
equip_dagger_front_left = Animation("equip_dagger_front_left")
equip_dagger_front_left.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_dagger_front_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_dagger_front_left.add_master_flag(AnimationMasterFlag.PLAY)
equip_dagger_front_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "equip_arms", 253, 276)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_dagger_front_left.add_sequence(seq0)


# unequip_dagger_front_left Animation
unequip_dagger_front_left = Animation("unequip_dagger_front_left")
unequip_dagger_front_left.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_dagger_front_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_dagger_front_left.add_master_flag(AnimationMasterFlag.PLAY)
unequip_dagger_front_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.2, "equip_arms", 254, 250)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_dagger_front_left.add_sequence(seq0)


# equip_dagger_front_right Animation
equip_dagger_front_right = Animation("equip_dagger_front_right")
equip_dagger_front_right.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_dagger_front_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_dagger_front_right.add_master_flag(AnimationMasterFlag.PLAY)
equip_dagger_front_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "equip_arms", 305, 333)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_dagger_front_right.add_sequence(seq0)


# unequip_dagger_front_right Animation
unequip_dagger_front_right = Animation("unequip_dagger_front_right")
unequip_dagger_front_right.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_dagger_front_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_dagger_front_right.add_master_flag(AnimationMasterFlag.PLAY)
unequip_dagger_front_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.4, "equip_arms", 306, 300)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_dagger_front_right.add_sequence(seq0)


# equip_axe_back Animation
equip_axe_back = Animation("equip_axe_back")
equip_axe_back.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_axe_back.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_axe_back.add_master_flag(AnimationMasterFlag.PLAY)
equip_axe_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(1.0, "equip_greataxe", 0, 17)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_axe_back.add_sequence(seq0)


# unequip_axe_back Animation
unequip_axe_back = Animation("unequip_axe_back")
unequip_axe_back.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_axe_back.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_axe_back.add_master_flag(AnimationMasterFlag.PLAY)
unequip_axe_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_greataxe", 7, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_axe_back.add_sequence(seq0)


# equip_revolver_right Animation
equip_revolver_right = Animation("equip_revolver_right")
equip_revolver_right.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_revolver_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_revolver_right.add_master_flag(AnimationMasterFlag.PLAY)
equip_revolver_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "equip_arms", 352, 365)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_revolver_right.add_sequence(seq0)


# unequip_revolver_right Animation
unequip_revolver_right = Animation("unequip_revolver_right")
unequip_revolver_right.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_revolver_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_revolver_right.add_master_flag(AnimationMasterFlag.PLAY)
unequip_revolver_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_arms", 354, 350)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_revolver_right.add_sequence(seq0)


# equip_pistol_front_left Animation
equip_pistol_front_left = Animation("equip_pistol_front_left")
equip_pistol_front_left.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_pistol_front_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_pistol_front_left.add_master_flag(AnimationMasterFlag.PLAY)
equip_pistol_front_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "equip_arms", 253, 276)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_pistol_front_left.add_sequence(seq0)


# unequip_pistol_front_left Animation
unequip_pistol_front_left = Animation("unequip_pistol_front_left")
unequip_pistol_front_left.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_pistol_front_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_pistol_front_left.add_master_flag(AnimationMasterFlag.PLAY)
unequip_pistol_front_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.2, "equip_arms", 254, 250)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_pistol_front_left.add_sequence(seq0)


# equip_katana Animation
equip_katana = Animation("equip_katana")
equip_katana.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_katana.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_katana.add_master_flag(AnimationMasterFlag.PLAY)
equip_katana.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 20030, 20045)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_katana.add_sequence(seq0)


# unequip_katana Animation
unequip_katana = Animation("unequip_katana")
unequip_katana.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_katana.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_katana.add_master_flag(AnimationMasterFlag.PLAY)
unequip_katana.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 20010, 20000)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_katana.add_sequence(seq0)


# equip_wakizashi Animation
equip_wakizashi = Animation("equip_wakizashi")
equip_wakizashi.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_wakizashi.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_wakizashi.add_master_flag(AnimationMasterFlag.PLAY)
equip_wakizashi.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 20030, 20045)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_wakizashi.add_sequence(seq0)


# unequip_wakizashi Animation
unequip_wakizashi = Animation("unequip_wakizashi")
unequip_wakizashi.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_wakizashi.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_wakizashi.add_master_flag(AnimationMasterFlag.PLAY)
unequip_wakizashi.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 20010, 20000)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_wakizashi.add_sequence(seq0)


# equip_shield Animation
equip_shield = Animation("equip_shield")
equip_shield.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_shield.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_shield.add_master_flag(AnimationMasterFlag.PLAY)
equip_shield.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "equip_arms", 68, 84)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_shield.add_sequence(seq0)


# unequip_shield Animation
unequip_shield = Animation("unequip_shield")
unequip_shield.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_shield.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_shield.add_master_flag(AnimationMasterFlag.PLAY)
unequip_shield.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.4, "equip_arms", 62, 50)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_shield.add_sequence(seq0)


# equip_bow_back Animation
equip_bow_back = Animation("equip_bow_back")
equip_bow_back.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_bow_back.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_bow_back.add_master_flag(AnimationMasterFlag.PLAY)
equip_bow_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.7, "equip_arms", 161, 179)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_bow_back.add_sequence(seq0)


# unequip_bow_back Animation
unequip_bow_back = Animation("unequip_bow_back")
unequip_bow_back.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_bow_back.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_bow_back.add_master_flag(AnimationMasterFlag.PLAY)
unequip_bow_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_arms", 163, 150)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_bow_back.add_sequence(seq0)


# equip_bow_left_hip Animation
equip_bow_left_hip = Animation("equip_bow_left_hip")
equip_bow_left_hip.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_bow_left_hip.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_bow_left_hip.add_master_flag(AnimationMasterFlag.PLAY)
equip_bow_left_hip.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.7, "equip_arms", 110, 148)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_bow_left_hip.add_sequence(seq0)


# unequip_bow_left_hip Animation
unequip_bow_left_hip = Animation("unequip_bow_left_hip")
unequip_bow_left_hip.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_bow_left_hip.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_bow_left_hip.add_master_flag(AnimationMasterFlag.PLAY)
unequip_bow_left_hip.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_arms", 115, 108)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_bow_left_hip.add_sequence(seq0)


# cancel_attack_onehanded Animation
cancel_attack_onehanded = Animation("cancel_attack_onehanded")
cancel_attack_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_CANCEL)
cancel_attack_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
cancel_attack_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
cancel_attack_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
cancel_attack_onehanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.25, "sword_loop01", 10, 11)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
cancel_attack_onehanded.add_sequence(seq0)


# cancel_attack_twohanded Animation
cancel_attack_twohanded = Animation("cancel_attack_twohanded")
cancel_attack_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_CANCEL)
cancel_attack_twohanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
cancel_attack_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
cancel_attack_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
cancel_attack_twohanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.25, "greatsword_cstance", 10, 11)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
cancel_attack_twohanded.add_sequence(seq0)


# cancel_attack_polearm Animation
cancel_attack_polearm = Animation("cancel_attack_polearm")
cancel_attack_polearm.add_master_flag(AnimationMasterFlag.PRIORITY_CANCEL)
cancel_attack_polearm.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
cancel_attack_polearm.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
cancel_attack_polearm.add_master_flag(AnimationMasterFlag.PLAY)
cancel_attack_polearm.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.25, "staff_cstance", 10, 11)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
cancel_attack_polearm.add_sequence(seq0)


# ready_bow Animation
ready_bow = Animation("ready_bow", 100)
ready_bow.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_bow.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_bow.add_master_flag(AnimationMasterFlag.RIDER_ROT_BOW)
ready_bow.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_bow.add_master_flag(AnimationMasterFlag.KEEP)
ready_bow.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.5, "anim_human", 20500, 20530)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.14)
seq0.setExtraVals(1, 0.44)
ready_bow.add_sequence(seq0)


# release_bow Animation
release_bow = Animation("release_bow", 100)
release_bow.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_bow.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_bow.add_master_flag(AnimationMasterFlag.RIDER_ROT_BOW)
release_bow.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_bow.add_master_flag(AnimationMasterFlag.PLAY)
release_bow.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 20530, 20532)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
release_bow.add_sequence(seq0)


# ready_bow_mounted Animation
ready_bow_mounted = Animation("ready_bow_mounted", 100)
ready_bow_mounted.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_bow_mounted.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_bow_mounted.add_master_flag(AnimationMasterFlag.RIDER_ROT_BOW)
ready_bow_mounted.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_bow_mounted.add_master_flag(AnimationMasterFlag.KEEP)
ready_bow_mounted.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.5, "anim_human", 20800, 20830)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.1)
seq0.setExtraVals(1, 0.4)
ready_bow_mounted.add_sequence(seq0)


# release_bow_mounted Animation
release_bow_mounted = Animation("release_bow_mounted", 100)
release_bow_mounted.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_bow_mounted.add_master_flag(AnimationMasterFlag.RIDER_ROT_BOW)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 20830, 20832)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
release_bow_mounted.add_sequence(seq0)


# ready_crossbow Animation
ready_crossbow = Animation("ready_crossbow", 100)
ready_crossbow.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_crossbow.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_crossbow.add_master_flag(AnimationMasterFlag.RIDER_ROT_CROSSBOW)
ready_crossbow.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_crossbow.add_master_flag(AnimationMasterFlag.KEEP)
ready_crossbow.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.5, "anim_human", 21300, 21320)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_crossbow.add_sequence(seq0)


# release_crossbow Animation
release_crossbow = Animation("release_crossbow", 100)
release_crossbow.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_crossbow.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_crossbow.add_master_flag(AnimationMasterFlag.RIDER_ROT_CROSSBOW)
release_crossbow.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_crossbow.add_master_flag(AnimationMasterFlag.PLAY)
release_crossbow.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.2, "anim_human", 21330, 21331)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_crossbow.add_sequence(seq0)


# reload_crossbow Animation
reload_crossbow = Animation("reload_crossbow")
reload_crossbow.add_master_flag(AnimationMasterFlag.PRIORITY_RELOAD)
reload_crossbow.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
reload_crossbow.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 21700, 21750)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.94)
reload_crossbow.add_sequence(seq0)


# reload_crossbow_horseback Animation
reload_crossbow_horseback = Animation("reload_crossbow_horseback")
reload_crossbow_horseback.add_master_flag(AnimationMasterFlag.PRIORITY_RELOAD)
reload_crossbow_horseback.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
reload_crossbow_horseback.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.6, "anim_human", 21800, 21877)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.27)
seq0.setExtraVals(1, 0.94)
reload_crossbow_horseback.add_sequence(seq0)


# ready_javelin Animation
ready_javelin = Animation("ready_javelin")
ready_javelin.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_javelin.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_javelin.add_master_flag(AnimationMasterFlag.RIDER_ROT_THROW)
ready_javelin.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_javelin.add_master_flag(AnimationMasterFlag.KEEP)
ready_javelin.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.6, "throw_javelin2", 0, 30)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_javelin.add_sequence(seq0)


# release_javelin Animation
release_javelin = Animation("release_javelin")
release_javelin.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_javelin.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
release_javelin.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
release_javelin.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
release_javelin.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
release_javelin.add_master_flag(AnimationMasterFlag.RIDER_ROT_THROW)
release_javelin.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_javelin.add_master_flag(AnimationMasterFlag.PLAY)
release_javelin.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.9, "throw_javelin2", 55, 100)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
release_javelin.add_sequence(seq0)


# ready_throwing_knife Animation
ready_throwing_knife = Animation("ready_throwing_knife")
ready_throwing_knife.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_throwing_knife.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_throwing_knife.add_master_flag(AnimationMasterFlag.RIDER_ROT_THROW)
ready_throwing_knife.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_throwing_knife.add_master_flag(AnimationMasterFlag.KEEP)
ready_throwing_knife.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.6, "throw_knife", 10, 30)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_throwing_knife.add_sequence(seq0)


# release_throwing_knife Animation
release_throwing_knife = Animation("release_throwing_knife")
release_throwing_knife.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_throwing_knife.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
release_throwing_knife.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
release_throwing_knife.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
release_throwing_knife.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
release_throwing_knife.add_master_flag(AnimationMasterFlag.RIDER_ROT_THROW)
release_throwing_knife.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_throwing_knife.add_master_flag(AnimationMasterFlag.PLAY)
release_throwing_knife.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.9, "throw_knife", 30, 70)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
release_throwing_knife.add_sequence(seq0)


# ready_throwing_axe Animation
ready_throwing_axe = Animation("ready_throwing_axe")
ready_throwing_axe.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_throwing_axe.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_throwing_axe.add_master_flag(AnimationMasterFlag.RIDER_ROT_THROW)
ready_throwing_axe.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_throwing_axe.add_master_flag(AnimationMasterFlag.KEEP)
ready_throwing_axe.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.6, "throwing_axe", 7, 23)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_throwing_axe.add_sequence(seq0)


# release_throwing_axe Animation
release_throwing_axe = Animation("release_throwing_axe")
release_throwing_axe.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_throwing_axe.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
release_throwing_axe.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
release_throwing_axe.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
release_throwing_axe.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
release_throwing_axe.add_master_flag(AnimationMasterFlag.RIDER_ROT_THROW)
release_throwing_axe.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_throwing_axe.add_master_flag(AnimationMasterFlag.PLAY)
release_throwing_axe.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.9, "throwing_axe", 23, 60)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
release_throwing_axe.add_sequence(seq0)


# ready_stone Animation
ready_stone = Animation("ready_stone")
ready_stone.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_stone.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_stone.add_master_flag(AnimationMasterFlag.RIDER_ROT_THROW)
ready_stone.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_stone.add_master_flag(AnimationMasterFlag.KEEP)
ready_stone.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.6, "throwing_stone", 0, 20)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_stone.add_sequence(seq0)


# release_stone Animation
release_stone = Animation("release_stone")
release_stone.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_stone.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
release_stone.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
release_stone.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
release_stone.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
release_stone.add_master_flag(AnimationMasterFlag.RIDER_ROT_THROW)
release_stone.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_stone.add_master_flag(AnimationMasterFlag.PLAY)
release_stone.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.9, "throwing_stone", 20, 65)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
release_stone.add_sequence(seq0)


# ready_pistol Animation
ready_pistol = Animation("ready_pistol", 100)
ready_pistol.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
ready_pistol.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_pistol.add_master_flag(AnimationMasterFlag.RIDER_ROT_PISTOL)
ready_pistol.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_pistol.add_master_flag(AnimationMasterFlag.KEEP)
ready_pistol.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 22500, 22515)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
ready_pistol.add_sequence(seq0)


# release_pistol Animation
release_pistol = Animation("release_pistol", 100)
release_pistol.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
release_pistol.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_pistol.add_master_flag(AnimationMasterFlag.RIDER_ROT_PISTOL)
release_pistol.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_pistol.add_master_flag(AnimationMasterFlag.PLAY)
release_pistol.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 22520, 22527)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_pistol.add_sequence(seq0)


# reload_pistol Animation
reload_pistol = Animation("reload_pistol")
reload_pistol.add_master_flag(AnimationMasterFlag.PRIORITY_RELOAD)
reload_pistol.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
reload_pistol.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(2.0, "anim_human", 22650, 22860)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
reload_pistol.add_sequence(seq0)


# ready_musket Animation
ready_musket = Animation("ready_musket", 100)
ready_musket.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_musket.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_musket.add_master_flag(AnimationMasterFlag.RIDER_ROT_CROSSBOW)
ready_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_musket.add_master_flag(AnimationMasterFlag.KEEP)
ready_musket.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.5, "anim_human", 21300, 21320)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_musket.add_sequence(seq0)


# release_musket Animation
release_musket = Animation("release_musket", 100)
release_musket.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_musket.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_musket.add_master_flag(AnimationMasterFlag.RIDER_ROT_CROSSBOW)
release_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_musket.add_master_flag(AnimationMasterFlag.PLAY)
release_musket.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.2, "anim_human", 21330, 21331)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_musket.add_sequence(seq0)


# reload_musket Animation
reload_musket = Animation("reload_musket")
reload_musket.add_master_flag(AnimationMasterFlag.PRIORITY_RELOAD)
reload_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
reload_musket.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(2.0, "anim_human", 22650, 22860)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
reload_musket.add_sequence(seq0)


# ready_swingright_fist Animation
ready_swingright_fist = Animation("ready_swingright_fist")
ready_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_swingright_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
ready_swingright_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_swingright_fist.add_master_flag(AnimationMasterFlag.KEEP)
ready_swingright_fist.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.35, "right_swing", 0, 15)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_swingright_fist.add_sequence(seq0)


# release_swingright_fist Animation
release_swingright_fist = Animation("release_swingright_fist")
release_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_swingright_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
release_swingright_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_swingright_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.5, "right_swing", 15, 41)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_swingright_fist.add_sequence(seq0)


# release_swingright_fist_continue Animation
release_swingright_fist_continue = Animation("release_swingright_fist_continue")
release_swingright_fist_continue.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_swingright_fist_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
release_swingright_fist_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_swingright_fist_continue.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.5, "right_swing", 15, 41)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_swingright_fist_continue.add_sequence(seq0)


# blocked_swingright_fist Animation
blocked_swingright_fist = Animation("blocked_swingright_fist")
blocked_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_swingright_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
blocked_swingright_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_swingright_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 24013, 24008)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_swingright_fist.add_sequence(seq0)


# parried_swingright_fist Animation
parried_swingright_fist = Animation("parried_swingright_fist")
parried_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_swingright_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
parried_swingright_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_swingright_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 24013, 24008)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_swingright_fist.add_sequence(seq0)


# ready_swingleft_fist Animation
ready_swingleft_fist = Animation("ready_swingleft_fist")
ready_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_swingleft_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
ready_swingleft_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_swingleft_fist.add_master_flag(AnimationMasterFlag.KEEP)
ready_swingleft_fist.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.35, "anim_human", 24300, 24300)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_swingleft_fist.add_sequence(seq0)


# release_swingleft_fist Animation
release_swingleft_fist = Animation("release_swingleft_fist")
release_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_swingleft_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
release_swingleft_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_swingleft_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.5, "anim_human", 24300, 24335)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_swingleft_fist.add_sequence(seq0)


# release_swingleft_fist_continue Animation
release_swingleft_fist_continue = Animation("release_swingleft_fist_continue")
release_swingleft_fist_continue.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_swingleft_fist_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
release_swingleft_fist_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_swingleft_fist_continue.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.5, "anim_human", 24300, 24335)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_swingleft_fist_continue.add_sequence(seq0)


# blocked_swingleft_fist Animation
blocked_swingleft_fist = Animation("blocked_swingleft_fist")
blocked_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_swingleft_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
blocked_swingleft_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_swingleft_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 24313, 24308)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_swingleft_fist.add_sequence(seq0)


# parried_swingleft_fist Animation
parried_swingleft_fist = Animation("parried_swingleft_fist")
parried_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_swingleft_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
parried_swingleft_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_swingleft_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 24313, 24308)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_swingleft_fist.add_sequence(seq0)


# ready_direct_fist Animation
ready_direct_fist = Animation("ready_direct_fist")
ready_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_direct_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
ready_direct_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_direct_fist.add_master_flag(AnimationMasterFlag.KEEP)
ready_direct_fist.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.35, "direct_fist", 0, 16)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_direct_fist.add_sequence(seq0)


# release_direct_fist Animation
release_direct_fist = Animation("release_direct_fist")
release_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_direct_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
release_direct_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_direct_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.5, "direct_fist", 17, 36)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_direct_fist.add_sequence(seq0)


# release_direct_fist_continue Animation
release_direct_fist_continue = Animation("release_direct_fist_continue")
release_direct_fist_continue.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_direct_fist_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
release_direct_fist_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_direct_fist_continue.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.5, "direct_fist", 17, 36)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_direct_fist_continue.add_sequence(seq0)


# blocked_direct_fist Animation
blocked_direct_fist = Animation("blocked_direct_fist")
blocked_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_direct_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
blocked_direct_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_direct_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 24613, 24608)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_direct_fist.add_sequence(seq0)


# parried_direct_fist Animation
parried_direct_fist = Animation("parried_direct_fist")
parried_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_direct_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
parried_direct_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_direct_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 24613, 24608)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_direct_fist.add_sequence(seq0)


# ready_uppercut_fist Animation
ready_uppercut_fist = Animation("ready_uppercut_fist")
ready_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_uppercut_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
ready_uppercut_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_uppercut_fist.add_master_flag(AnimationMasterFlag.KEEP)
ready_uppercut_fist.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.35, "uppercut", 0, 17)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_uppercut_fist.add_sequence(seq0)


# release_uppercut_fist Animation
release_uppercut_fist = Animation("release_uppercut_fist")
release_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_uppercut_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
release_uppercut_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_uppercut_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.5, "uppercut", 17, 34)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_uppercut_fist.add_sequence(seq0)


# release_uppercut_fist_continue Animation
release_uppercut_fist_continue = Animation("release_uppercut_fist_continue")
release_uppercut_fist_continue.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_uppercut_fist_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
release_uppercut_fist_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_uppercut_fist_continue.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.5, "uppercut", 17, 34)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_uppercut_fist_continue.add_sequence(seq0)


# blocked_uppercut_fist Animation
blocked_uppercut_fist = Animation("blocked_uppercut_fist")
blocked_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_uppercut_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
blocked_uppercut_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_uppercut_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 24913, 24908)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_uppercut_fist.add_sequence(seq0)


# parried_uppercut_fist Animation
parried_uppercut_fist = Animation("parried_uppercut_fist")
parried_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_uppercut_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
parried_uppercut_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_uppercut_fist.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 24913, 24908)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_uppercut_fist.add_sequence(seq0)


# ready_slashright_twohanded Animation
ready_slashright_twohanded = Animation("ready_slashright_twohanded", 100)
ready_slashright_twohanded.add_flag(AnimationFlag.RIGHT_CUT)
ready_slashright_twohanded.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_slashright_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_slashright_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_slashright_twohanded.add_master_flag(AnimationMasterFlag.KEEP)
ready_slashright_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_slashright_twohanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "slashright_twohanded", 10, 18)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_slashright_twohanded.add_sequence(seq0)


# release_slashright_twohanded Animation
release_slashright_twohanded = Animation("release_slashright_twohanded", 100)
release_slashright_twohanded.add_flag(AnimationFlag.RIGHT_CUT)
release_slashright_twohanded.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_slashright_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_slashright_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashright_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
release_slashright_twohanded.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.61, "slashright_twohanded", 18, 38)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_slashright_twohanded.add_sequence(seq0)


# release_slashright_twohanded_continue Animation
release_slashright_twohanded_continue = Animation("release_slashright_twohanded_continue")
release_slashright_twohanded_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_slashright_twohanded_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashright_twohanded_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_slashright_twohanded_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.5, "slashright_twohanded", 38, 61)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_slashright_twohanded_continue.add_sequence(seq0)


# blocked_slashright_twohanded Animation
blocked_slashright_twohanded = Animation("blocked_slashright_twohanded", 100)
blocked_slashright_twohanded.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
blocked_slashright_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_slashright_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_slashright_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_slashright_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_slashright_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_slashright_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 25725, 25720)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_slashright_twohanded.add_sequence(seq0)


# parried_slashright_twohanded Animation
parried_slashright_twohanded = Animation("parried_slashright_twohanded", 100)
parried_slashright_twohanded.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
parried_slashright_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_slashright_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_slashright_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_slashright_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_slashright_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_slashright_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 25725, 25720)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_slashright_twohanded.add_sequence(seq0)


# ready_slashleft_twohanded Animation
ready_slashleft_twohanded = Animation("ready_slashleft_twohanded", 100)
ready_slashleft_twohanded.add_flag(AnimationFlag.RIGHT_CUT)
ready_slashleft_twohanded.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_slashleft_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_slashleft_twohanded.add_master_flag(AnimationMasterFlag.KEEP)
ready_slashleft_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_slashleft_twohanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "slashleft_twohanded", 12, 16)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_slashleft_twohanded.add_sequence(seq0)


# release_slashleft_twohanded Animation
release_slashleft_twohanded = Animation("release_slashleft_twohanded", 100)
release_slashleft_twohanded.add_flag(AnimationFlag.RIGHT_CUT)
release_slashleft_twohanded.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_slashleft_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
release_slashleft_twohanded.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.61, "slashleft_twohanded", 16, 38)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_slashleft_twohanded.add_sequence(seq0)


# release_slashleft_twohanded_continue Animation
release_slashleft_twohanded_continue = Animation("release_slashleft_twohanded_continue")
release_slashleft_twohanded_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_slashleft_twohanded_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashleft_twohanded_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_slashleft_twohanded_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.5, "slashleft_twohanded", 38, 52)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_slashleft_twohanded_continue.add_sequence(seq0)


# blocked_slashleft_twohanded Animation
blocked_slashleft_twohanded = Animation("blocked_slashleft_twohanded", 100)
blocked_slashleft_twohanded.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
blocked_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_slashleft_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 26425, 26420)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_slashleft_twohanded.add_sequence(seq0)


# parried_slashleft_twohanded Animation
parried_slashleft_twohanded = Animation("parried_slashleft_twohanded", 100)
parried_slashleft_twohanded.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
parried_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_slashleft_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_slashleft_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 26425, 26420)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_slashleft_twohanded.add_sequence(seq0)


# ready_thrust_twohanded Animation
ready_thrust_twohanded = Animation("ready_thrust_twohanded", 100)
ready_thrust_twohanded.add_flag(AnimationFlag.THRUST)
ready_thrust_twohanded.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_thrust_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_thrust_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_thrust_twohanded.add_master_flag(AnimationMasterFlag.KEEP)
ready_thrust_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_thrust_twohanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "anim_human", 26000, 26010)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_thrust_twohanded.add_sequence(seq0)


# release_thrust_twohanded Animation
release_thrust_twohanded = Animation("release_thrust_twohanded", 100)
release_thrust_twohanded.add_flag(AnimationFlag.THRUST)
release_thrust_twohanded.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_thrust_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_thrust_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
release_thrust_twohanded.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.61, "anim_human", 26010, 26031)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_thrust_twohanded.add_sequence(seq0)


# release_thrust_twohanded_continue Animation
release_thrust_twohanded_continue = Animation("release_thrust_twohanded_continue")
release_thrust_twohanded_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_thrust_twohanded_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_twohanded_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_thrust_twohanded_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.1, "anim_human", 26031, 26040)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_thrust_twohanded_continue.add_sequence(seq0)


# blocked_thrust_twohanded Animation
blocked_thrust_twohanded = Animation("blocked_thrust_twohanded")
blocked_thrust_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_thrust_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_thrust_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_thrust_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_thrust_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_thrust_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 26015, 26016)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_thrust_twohanded.add_sequence(seq0)


# parried_thrust_twohanded Animation
parried_thrust_twohanded = Animation("parried_thrust_twohanded")
parried_thrust_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_thrust_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_thrust_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_thrust_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_thrust_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_thrust_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.7, "anim_human", 26015, 26016)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_thrust_twohanded.add_sequence(seq0)


# ready_overswing_twohanded Animation
ready_overswing_twohanded = Animation("ready_overswing_twohanded")
ready_overswing_twohanded.add_flag(AnimationFlag.OVERSWING)
ready_overswing_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_overswing_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_overswing_twohanded.add_master_flag(AnimationMasterFlag.KEEP)
ready_overswing_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_overswing_twohanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_twohanded_overswing", 11, 26)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_overswing_twohanded.add_sequence(seq0)


# release_overswing_twohanded Animation
release_overswing_twohanded = Animation("release_overswing_twohanded")
release_overswing_twohanded.add_flag(AnimationFlag.OVERSWING)
release_overswing_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_overswing_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_overswing_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
release_overswing_twohanded.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.61, "attacks_twohanded_overswing", 26, 55)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_overswing_twohanded.add_sequence(seq0)


# release_overswing_twohanded_continue Animation
release_overswing_twohanded_continue = Animation("release_overswing_twohanded_continue")
release_overswing_twohanded_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_overswing_twohanded_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_overswing_twohanded_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_overswing_twohanded_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.5, "attacks_twohanded_overswing", 55, 66)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_overswing_twohanded_continue.add_sequence(seq0)


# blocked_overswing_twohanded Animation
blocked_overswing_twohanded = Animation("blocked_overswing_twohanded")
blocked_overswing_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_overswing_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_overswing_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_overswing_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_overswing_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_overswing_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 26215, 26212)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_overswing_twohanded.add_sequence(seq0)


# parried_overswing_twohanded Animation
parried_overswing_twohanded = Animation("parried_overswing_twohanded")
parried_overswing_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_overswing_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_overswing_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_overswing_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_overswing_twohanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_overswing_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 26215, 26212)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_overswing_twohanded.add_sequence(seq0)


# ready_thrust_onehanded Animation
ready_thrust_onehanded = Animation("ready_thrust_onehanded", 100)
ready_thrust_onehanded.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
ready_thrust_onehanded.add_flag(AnimationFlag.THRUST)
ready_thrust_onehanded.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
ready_thrust_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_thrust_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
ready_thrust_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_thrust_onehanded.add_master_flag(AnimationMasterFlag.KEEP)
ready_thrust_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_thrust_onehanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_thrust_onehanded", 5, 13)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_thrust_onehanded.add_sequence(seq0)


# release_thrust_onehanded Animation
release_thrust_onehanded = Animation("release_thrust_onehanded", 100)
release_thrust_onehanded.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
release_thrust_onehanded.add_flag(AnimationFlag.THRUST)
release_thrust_onehanded.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
release_thrust_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_thrust_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
release_thrust_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
release_thrust_onehanded.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.62, "attacks_thrust_onehanded", 12, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_thrust_onehanded.add_sequence(seq0)


# release_thrust_onehanded_continue Animation
release_thrust_onehanded_continue = Animation("release_thrust_onehanded_continue")
release_thrust_onehanded_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_thrust_onehanded_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
release_thrust_onehanded_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_onehanded_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_thrust_onehanded_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "attacks_thrust_onehanded", 32, 54)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_thrust_onehanded_continue.add_sequence(seq0)


# blocked_thrust_onehanded Animation
blocked_thrust_onehanded = Animation("blocked_thrust_onehanded")
blocked_thrust_onehanded.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
blocked_thrust_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_thrust_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_thrust_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_thrust_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_thrust_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
blocked_thrust_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_thrust_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 28515, 28513)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_thrust_onehanded.add_sequence(seq0)


# parried_thrust_onehanded Animation
parried_thrust_onehanded = Animation("parried_thrust_onehanded")
parried_thrust_onehanded.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
parried_thrust_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_thrust_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_thrust_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_thrust_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_thrust_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
parried_thrust_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_thrust_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.7, "anim_human", 28515, 28513)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_thrust_onehanded.add_sequence(seq0)


# ready_thrust_onehanded_horseback Animation
ready_thrust_onehanded_horseback = Animation("ready_thrust_onehanded_horseback", 100)
ready_thrust_onehanded_horseback.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
ready_thrust_onehanded_horseback.add_flag(AnimationFlag.THRUST)
ready_thrust_onehanded_horseback.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
ready_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
ready_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.KEEP)
ready_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_thrust_onehanded", 5, 13)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_thrust_onehanded_horseback.add_sequence(seq0)


# release_thrust_onehanded_horseback Animation
release_thrust_onehanded_horseback = Animation("release_thrust_onehanded_horseback", 100)
release_thrust_onehanded_horseback.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
release_thrust_onehanded_horseback.add_flag(AnimationFlag.THRUST)
release_thrust_onehanded_horseback.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
release_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
release_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PLAY)
release_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.62, "attacks_thrust_onehanded", 12, 32)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_thrust_onehanded_horseback.add_sequence(seq0)


# release_thrust_onehanded_horseback_continue Animation
release_thrust_onehanded_horseback_continue = Animation("release_thrust_onehanded_horseback_continue")
release_thrust_onehanded_horseback_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_thrust_onehanded_horseback_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
release_thrust_onehanded_horseback_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_onehanded_horseback_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_thrust_onehanded_horseback_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "attacks_thrust_onehanded", 32, 54)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_thrust_onehanded_horseback_continue.add_sequence(seq0)


# blocked_thrust_onehanded_horseback Animation
blocked_thrust_onehanded_horseback = Animation("blocked_thrust_onehanded_horseback")
blocked_thrust_onehanded_horseback.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
blocked_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
blocked_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 28515, 28513)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_thrust_onehanded_horseback.add_sequence(seq0)


# parried_thrust_onehanded_horseback Animation
parried_thrust_onehanded_horseback = Animation("parried_thrust_onehanded_horseback")
parried_thrust_onehanded_horseback.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
parried_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
parried_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_thrust_onehanded_horseback.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.7, "anim_human", 28515, 28513)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_thrust_onehanded_horseback.add_sequence(seq0)


# ready_thrust_onehanded_lance Animation
ready_thrust_onehanded_lance = Animation("ready_thrust_onehanded_lance", 100)
ready_thrust_onehanded_lance.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
ready_thrust_onehanded_lance.add_flag(AnimationFlag.THRUST)
ready_thrust_onehanded_lance.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
ready_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
ready_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.KEEP)
ready_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "thrust_onehanded_lance_hb", 5, 8)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_thrust_onehanded_lance.add_sequence(seq0)


# release_thrust_onehanded_lance Animation
release_thrust_onehanded_lance = Animation("release_thrust_onehanded_lance", 100)
release_thrust_onehanded_lance.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
release_thrust_onehanded_lance.add_flag(AnimationFlag.THRUST)
release_thrust_onehanded_lance.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
release_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
release_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PLAY)
release_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.62, "thrust_onehanded_lance_hb", 8, 33)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_thrust_onehanded_lance.add_sequence(seq0)


# release_thrust_onehanded_lance_continue Animation
release_thrust_onehanded_lance_continue = Animation("release_thrust_onehanded_lance_continue")
release_thrust_onehanded_lance_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_thrust_onehanded_lance_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
release_thrust_onehanded_lance_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_onehanded_lance_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_thrust_onehanded_lance_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.1, "thrust_onehanded_lance_hb", 33, 45)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_thrust_onehanded_lance_continue.add_sequence(seq0)


# blocked_thrust_onehanded_lance Animation
blocked_thrust_onehanded_lance = Animation("blocked_thrust_onehanded_lance")
blocked_thrust_onehanded_lance.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
blocked_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
blocked_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 29515, 29513)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_thrust_onehanded_lance.add_sequence(seq0)


# parried_thrust_onehanded_lance Animation
parried_thrust_onehanded_lance = Animation("parried_thrust_onehanded_lance")
parried_thrust_onehanded_lance.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
parried_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
parried_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_thrust_onehanded_lance.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.7, "anim_human", 29515, 29513)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_thrust_onehanded_lance.add_sequence(seq0)


# ready_slashright_onehanded Animation
ready_slashright_onehanded = Animation("ready_slashright_onehanded", 100)
ready_slashright_onehanded.add_flag(AnimationFlag.RIGHT_CUT)
ready_slashright_onehanded.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
ready_slashright_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_slashright_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_slashright_onehanded.add_master_flag(AnimationMasterFlag.KEEP)
ready_slashright_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_slashright_onehanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_single_righttoleft", 2, 5)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_slashright_onehanded.add_sequence(seq0)


# release_slashright_onehanded Animation
release_slashright_onehanded = Animation("release_slashright_onehanded", 100)
release_slashright_onehanded.add_flag(AnimationFlag.RIGHT_CUT)
release_slashright_onehanded.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
release_slashright_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_slashright_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashright_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
release_slashright_onehanded.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.6, "attacks_single_righttoleft", 5, 28)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_slashright_onehanded.add_sequence(seq0)


# release_slashright_onehanded_continue Animation
release_slashright_onehanded_continue = Animation("release_slashright_onehanded_continue")
release_slashright_onehanded_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_slashright_onehanded_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashright_onehanded_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_slashright_onehanded_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.4, "attacks_single_righttoleft", 28, 44)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_slashright_onehanded_continue.add_sequence(seq0)


# blocked_slashright_onehanded Animation
blocked_slashright_onehanded = Animation("blocked_slashright_onehanded")
blocked_slashright_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_slashright_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_slashright_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_slashright_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_slashright_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_slashright_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "parry_single_righttoleft", 0, 14)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_slashright_onehanded.add_sequence(seq0)


# parried_slashright_onehanded Animation
parried_slashright_onehanded = Animation("parried_slashright_onehanded")
parried_slashright_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_slashright_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_slashright_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_slashright_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_slashright_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_slashright_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "parry_single_righttoleft", 0, 14)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_slashright_onehanded.add_sequence(seq0)


# ready_slashleft_onehanded Animation
ready_slashleft_onehanded = Animation("ready_slashleft_onehanded", 100)
ready_slashleft_onehanded.add_flag(AnimationFlag.LEFT_CUT)
ready_slashleft_onehanded.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
ready_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_slashleft_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_slashleft_onehanded.add_master_flag(AnimationMasterFlag.KEEP)
ready_slashleft_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_slashleft_onehanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_single_lefttoright", 4, 11)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_slashleft_onehanded.add_sequence(seq0)


# release_slashleft_onehanded Animation
release_slashleft_onehanded = Animation("release_slashleft_onehanded", 100)
release_slashleft_onehanded.add_flag(AnimationFlag.LEFT_CUT)
release_slashleft_onehanded.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
release_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_slashleft_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
release_slashleft_onehanded.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.61, "attacks_single_lefttoright", 11, 29)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_slashleft_onehanded.add_sequence(seq0)


# release_slashleft_onehanded_continue Animation
release_slashleft_onehanded_continue = Animation("release_slashleft_onehanded_continue")
release_slashleft_onehanded_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_slashleft_onehanded_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashleft_onehanded_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_slashleft_onehanded_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.4, "attacks_single_lefttoright", 29, 43)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_slashleft_onehanded_continue.add_sequence(seq0)


# blocked_slashleft_onehanded Animation
blocked_slashleft_onehanded = Animation("blocked_slashleft_onehanded")
blocked_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_slashleft_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "parry_single_lefttoright", 0, 75)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_slashleft_onehanded.add_sequence(seq0)


# parried_slashleft_onehanded Animation
parried_slashleft_onehanded = Animation("parried_slashleft_onehanded")
parried_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_slashleft_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_slashleft_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "parry_single_lefttoright", 0, 75)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_slashleft_onehanded.add_sequence(seq0)


# ready_overswing_onehanded Animation
ready_overswing_onehanded = Animation("ready_overswing_onehanded")
ready_overswing_onehanded.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
ready_overswing_onehanded.add_flag(AnimationFlag.OVERSWING)
ready_overswing_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_overswing_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_OVERSWING)
ready_overswing_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_overswing_onehanded.add_master_flag(AnimationMasterFlag.KEEP)
ready_overswing_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_overswing_onehanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_single_overswing", 5, 16)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_overswing_onehanded.add_sequence(seq0)


# release_overswing_onehanded Animation
release_overswing_onehanded = Animation("release_overswing_onehanded")
release_overswing_onehanded.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
release_overswing_onehanded.add_flag(AnimationFlag.OVERSWING)
release_overswing_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_overswing_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_OVERSWING)
release_overswing_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_overswing_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
release_overswing_onehanded.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.6, "attacks_single_overswing", 16, 37)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_overswing_onehanded.add_sequence(seq0)


# release_overswing_onehanded_continue Animation
release_overswing_onehanded_continue = Animation("release_overswing_onehanded_continue")
release_overswing_onehanded_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_overswing_onehanded_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_OVERSWING)
release_overswing_onehanded_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_overswing_onehanded_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_overswing_onehanded_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.2, "attacks_single_overswing", 37, 40)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_overswing_onehanded_continue.add_sequence(seq0)


# blocked_overswing_onehanded Animation
blocked_overswing_onehanded = Animation("blocked_overswing_onehanded")
blocked_overswing_onehanded.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
blocked_overswing_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_overswing_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_overswing_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_overswing_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_overswing_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_OVERSWING)
blocked_overswing_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_overswing_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 29315, 29310)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_overswing_onehanded.add_sequence(seq0)


# parried_overswing_onehanded Animation
parried_overswing_onehanded = Animation("parried_overswing_onehanded")
parried_overswing_onehanded.add_flag(AnimationFlag.ENFORCE_RIGHTSIDE)
parried_overswing_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_overswing_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_overswing_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_overswing_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_overswing_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_OVERSWING)
parried_overswing_onehanded.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_overswing_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 29315, 29310)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_overswing_onehanded.add_sequence(seq0)


# ready_slash_horseback_right Animation
ready_slash_horseback_right = Animation("ready_slash_horseback_right", 100)
ready_slash_horseback_right.add_flag(AnimationFlag.RIGHT_CUT)
ready_slash_horseback_right.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
ready_slash_horseback_right.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_slash_horseback_right.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
ready_slash_horseback_right.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_slash_horseback_right.add_master_flag(AnimationMasterFlag.KEEP)
ready_slash_horseback_right.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_slash_horseback_right.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_single_righttoleft_horseback", 8, 17)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_slash_horseback_right.add_sequence(seq0)


# release_slash_horseback_right Animation
release_slash_horseback_right = Animation("release_slash_horseback_right", 100)
release_slash_horseback_right.add_flag(AnimationFlag.RIGHT_CUT)
release_slash_horseback_right.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
release_slash_horseback_right.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_slash_horseback_right.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
release_slash_horseback_right.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slash_horseback_right.add_master_flag(AnimationMasterFlag.PLAY)
release_slash_horseback_right.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.7, "attacks_single_righttoleft_horseback", 17, 39)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_slash_horseback_right.add_sequence(seq0)


# release_slash_horseback_right_continue Animation
release_slash_horseback_right_continue = Animation("release_slash_horseback_right_continue")
release_slash_horseback_right_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_slash_horseback_right_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
release_slash_horseback_right_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slash_horseback_right_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_slash_horseback_right_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.4, "attacks_single_righttoleft_horseback", 39, 54)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_slash_horseback_right_continue.add_sequence(seq0)


# blocked_slash_horseback_right Animation
blocked_slash_horseback_right = Animation("blocked_slash_horseback_right", 100)
blocked_slash_horseback_right.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
blocked_slash_horseback_right.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_slash_horseback_right.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_slash_horseback_right.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_slash_horseback_right.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_slash_horseback_right.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
blocked_slash_horseback_right.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_slash_horseback_right.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "parry_single_righttoleft", 0, 14)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_slash_horseback_right.add_sequence(seq0)


# parried_slash_horseback_right Animation
parried_slash_horseback_right = Animation("parried_slash_horseback_right", 100)
parried_slash_horseback_right.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
parried_slash_horseback_right.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_slash_horseback_right.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_slash_horseback_right.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_slash_horseback_right.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_slash_horseback_right.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
parried_slash_horseback_right.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_slash_horseback_right.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "parry_single_righttoleft", 0, 14)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_slash_horseback_right.add_sequence(seq0)


# ready_slash_horseback_left Animation
ready_slash_horseback_left = Animation("ready_slash_horseback_left", 100)
ready_slash_horseback_left.add_flag(AnimationFlag.LEFT_CUT)
ready_slash_horseback_left.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
ready_slash_horseback_left.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_slash_horseback_left.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
ready_slash_horseback_left.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_slash_horseback_left.add_master_flag(AnimationMasterFlag.KEEP)
ready_slash_horseback_left.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_slash_horseback_left.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_single_lefttoright_horseback", 7, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_slash_horseback_left.add_sequence(seq0)


# release_slash_horseback_left Animation
release_slash_horseback_left = Animation("release_slash_horseback_left", 100)
release_slash_horseback_left.add_flag(AnimationFlag.LEFT_CUT)
release_slash_horseback_left.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
release_slash_horseback_left.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_slash_horseback_left.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
release_slash_horseback_left.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slash_horseback_left.add_master_flag(AnimationMasterFlag.PLAY)
release_slash_horseback_left.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.7, "attacks_single_lefttoright_horseback", 21, 43)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_slash_horseback_left.add_sequence(seq0)


# release_slash_horseback_left_continue Animation
release_slash_horseback_left_continue = Animation("release_slash_horseback_left_continue")
release_slash_horseback_left_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_slash_horseback_left_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
release_slash_horseback_left_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slash_horseback_left_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_slash_horseback_left_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "attacks_single_lefttoright_horseback", 43, 51)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_slash_horseback_left_continue.add_sequence(seq0)


# blocked_slash_horseback_left Animation
blocked_slash_horseback_left = Animation("blocked_slash_horseback_left", 100)
blocked_slash_horseback_left.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
blocked_slash_horseback_left.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_slash_horseback_left.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_slash_horseback_left.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_slash_horseback_left.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_slash_horseback_left.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
blocked_slash_horseback_left.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_slash_horseback_left.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "parry_single_lefttoright", 0, 75)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_slash_horseback_left.add_sequence(seq0)


# parried_slash_horseback_left Animation
parried_slash_horseback_left = Animation("parried_slash_horseback_left", 100)
parried_slash_horseback_left.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
parried_slash_horseback_left.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_slash_horseback_left.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_slash_horseback_left.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_slash_horseback_left.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_slash_horseback_left.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
parried_slash_horseback_left.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_slash_horseback_left.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "parry_single_lefttoright", 0, 75)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_slash_horseback_left.add_sequence(seq0)


# ready_slash_horseback_polearm_right Animation
ready_slash_horseback_polearm_right = Animation("ready_slash_horseback_polearm_right", 100)
ready_slash_horseback_polearm_right.add_flag(AnimationFlag.RIGHT_CUT)
ready_slash_horseback_polearm_right.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
ready_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
ready_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.KEEP)
ready_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_staff_righttoleft", 6, 16)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_slash_horseback_polearm_right.add_sequence(seq0)


# release_slash_horseback_polearm_right Animation
release_slash_horseback_polearm_right = Animation("release_slash_horseback_polearm_right", 100)
release_slash_horseback_polearm_right.add_flag(AnimationFlag.RIGHT_CUT)
release_slash_horseback_polearm_right.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
release_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
release_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PLAY)
release_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.7, "attacks_staff_righttoleft", 16, 40)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_slash_horseback_polearm_right.add_sequence(seq0)


# release_slash_horseback_polearm_right_continue Animation
release_slash_horseback_polearm_right_continue = Animation("release_slash_horseback_polearm_right_continue")
release_slash_horseback_polearm_right_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_slash_horseback_polearm_right_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
release_slash_horseback_polearm_right_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slash_horseback_polearm_right_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_slash_horseback_polearm_right_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.4, "attacks_staff_righttoleft", 40, 48)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_slash_horseback_polearm_right_continue.add_sequence(seq0)


# blocked_slash_horseback_polearm_right Animation
blocked_slash_horseback_polearm_right = Animation("blocked_slash_horseback_polearm_right", 100)
blocked_slash_horseback_polearm_right.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
blocked_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
blocked_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 27915, 27913)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
blocked_slash_horseback_polearm_right.add_sequence(seq0)


# parried_slash_horseback_polearm_right Animation
parried_slash_horseback_polearm_right = Animation("parried_slash_horseback_polearm_right", 100)
parried_slash_horseback_polearm_right.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
parried_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
parried_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_slash_horseback_polearm_right.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 27915, 27913)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
parried_slash_horseback_polearm_right.add_sequence(seq0)


# ready_slash_horseback_polearm_left Animation
ready_slash_horseback_polearm_left = Animation("ready_slash_horseback_polearm_left", 100)
ready_slash_horseback_polearm_left.add_flag(AnimationFlag.LEFT_CUT)
ready_slash_horseback_polearm_left.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
ready_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
ready_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.KEEP)
ready_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_staff_lefttoright", 10, 16)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_slash_horseback_polearm_left.add_sequence(seq0)


# release_slash_horseback_polearm_left Animation
release_slash_horseback_polearm_left = Animation("release_slash_horseback_polearm_left", 100)
release_slash_horseback_polearm_left.add_flag(AnimationFlag.LEFT_CUT)
release_slash_horseback_polearm_left.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
release_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
release_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PLAY)
release_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.7, "attacks_staff_lefttoright", 16, 41)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_slash_horseback_polearm_left.add_sequence(seq0)


# release_slash_horseback_polearm_left_continue Animation
release_slash_horseback_polearm_left_continue = Animation("release_slash_horseback_polearm_left_continue")
release_slash_horseback_polearm_left_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_slash_horseback_polearm_left_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
release_slash_horseback_polearm_left_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slash_horseback_polearm_left_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_slash_horseback_polearm_left_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "attacks_staff_lefttoright", 41, 55)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_slash_horseback_polearm_left_continue.add_sequence(seq0)


# blocked_slash_horseback_polearm_left Animation
blocked_slash_horseback_polearm_left = Animation("blocked_slash_horseback_polearm_left", 100)
blocked_slash_horseback_polearm_left.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
blocked_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
blocked_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 27615, 27613)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
blocked_slash_horseback_polearm_left.add_sequence(seq0)


# parried_slash_horseback_polearm_left Animation
parried_slash_horseback_polearm_left = Animation("parried_slash_horseback_polearm_left", 100)
parried_slash_horseback_polearm_left.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
parried_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
parried_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_slash_horseback_polearm_left.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 27615, 27613)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
parried_slash_horseback_polearm_left.add_sequence(seq0)


# ready_overswing_staff Animation
ready_overswing_staff = Animation("ready_overswing_staff")
ready_overswing_staff.add_flag(AnimationFlag.OVERSWING)
ready_overswing_staff.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_overswing_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_overswing_staff.add_master_flag(AnimationMasterFlag.KEEP)
ready_overswing_staff.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_overswing_staff.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_staff_uptodown", 9, 26)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_overswing_staff.add_sequence(seq0)


# release_overswing_staff Animation
release_overswing_staff = Animation("release_overswing_staff")
release_overswing_staff.add_flag(AnimationFlag.OVERSWING)
release_overswing_staff.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_overswing_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_overswing_staff.add_master_flag(AnimationMasterFlag.PLAY)
release_overswing_staff.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.6, "attacks_staff_uptodown", 26, 61)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_overswing_staff.add_sequence(seq0)


# release_overswing_staff_continue Animation
release_overswing_staff_continue = Animation("release_overswing_staff_continue")
release_overswing_staff_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_overswing_staff_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_overswing_staff_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_overswing_staff_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "attacks_staff_uptodown", 61, 68)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_overswing_staff_continue.add_sequence(seq0)


# blocked_overswing_staff Animation
blocked_overswing_staff = Animation("blocked_overswing_staff")
blocked_overswing_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_overswing_staff.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_overswing_staff.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_overswing_staff.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_overswing_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_overswing_staff.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 27017, 27014)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
blocked_overswing_staff.add_sequence(seq0)


# parried_overswing_staff Animation
parried_overswing_staff = Animation("parried_overswing_staff")
parried_overswing_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_overswing_staff.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_overswing_staff.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_overswing_staff.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_overswing_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_overswing_staff.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 27017, 27014)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
parried_overswing_staff.add_sequence(seq0)


# ready_thrust_staff Animation
ready_thrust_staff = Animation("ready_thrust_staff", 100)
ready_thrust_staff.add_flag(AnimationFlag.THRUST)
ready_thrust_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_thrust_staff.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_thrust_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_thrust_staff.add_master_flag(AnimationMasterFlag.KEEP)
ready_thrust_staff.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_thrust_staff.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_staff_thrust", 14, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_thrust_staff.add_sequence(seq0)


# release_thrust_staff Animation
release_thrust_staff = Animation("release_thrust_staff", 100)
release_thrust_staff.add_flag(AnimationFlag.THRUST)
release_thrust_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_thrust_staff.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_thrust_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_staff.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "attacks_staff_thrust", 21, 40)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_thrust_staff.add_sequence(seq0)


# release_thrust_staff_continue Animation
release_thrust_staff_continue = Animation("release_thrust_staff_continue", 100)
release_thrust_staff_continue.add_flag(AnimationFlag.THRUST)
release_thrust_staff_continue.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_thrust_staff_continue.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_thrust_staff_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_staff_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_thrust_staff_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.6, "attacks_staff_thrust", 40, 58)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_thrust_staff_continue.add_sequence(seq0)


# blocked_thrust_staff Animation
blocked_thrust_staff = Animation("blocked_thrust_staff", 100)
blocked_thrust_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
blocked_thrust_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_thrust_staff.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_thrust_staff.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_thrust_staff.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_thrust_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_thrust_staff.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 27316, 27313)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
blocked_thrust_staff.add_sequence(seq0)


# parried_thrust_staff Animation
parried_thrust_staff = Animation("parried_thrust_staff", 100)
parried_thrust_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
parried_thrust_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_thrust_staff.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_thrust_staff.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_thrust_staff.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_thrust_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_thrust_staff.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.7, "anim_human", 27316, 27313)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
parried_thrust_staff.add_sequence(seq0)


# ready_slashleft_staff Animation
ready_slashleft_staff = Animation("ready_slashleft_staff", 100)
ready_slashleft_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_slashleft_staff.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_slashleft_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_slashleft_staff.add_master_flag(AnimationMasterFlag.KEEP)
ready_slashleft_staff.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_slashleft_staff.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_staff_lefttoright", 10, 16)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_slashleft_staff.add_sequence(seq0)


# release_slashleft_staff Animation
release_slashleft_staff = Animation("release_slashleft_staff", 100)
release_slashleft_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_slashleft_staff.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_slashleft_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashleft_staff.add_master_flag(AnimationMasterFlag.PLAY)
release_slashleft_staff.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.6, "attacks_staff_lefttoright", 16, 44)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_slashleft_staff.add_sequence(seq0)


# release_slashleft_staff_continue Animation
release_slashleft_staff_continue = Animation("release_slashleft_staff_continue")
release_slashleft_staff_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_slashleft_staff_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashleft_staff_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_slashleft_staff_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "attacks_staff_lefttoright", 44, 55)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_slashleft_staff_continue.add_sequence(seq0)


# blocked_slashleft_staff Animation
blocked_slashleft_staff = Animation("blocked_slashleft_staff", 100)
blocked_slashleft_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
blocked_slashleft_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_slashleft_staff.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_slashleft_staff.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_slashleft_staff.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_slashleft_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_slashleft_staff.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 27615, 27613)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
blocked_slashleft_staff.add_sequence(seq0)


# parried_slashleft_staff Animation
parried_slashleft_staff = Animation("parried_slashleft_staff", 100)
parried_slashleft_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
parried_slashleft_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_slashleft_staff.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_slashleft_staff.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_slashleft_staff.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_slashleft_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_slashleft_staff.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 27615, 27613)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
parried_slashleft_staff.add_sequence(seq0)


# ready_slashright_staff Animation
ready_slashright_staff = Animation("ready_slashright_staff", 100)
ready_slashright_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_slashright_staff.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_slashright_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_slashright_staff.add_master_flag(AnimationMasterFlag.KEEP)
ready_slashright_staff.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_slashright_staff.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "attacks_staff_righttoleft", 6, 16)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_slashright_staff.add_sequence(seq0)


# release_slashright_staff Animation
release_slashright_staff = Animation("release_slashright_staff", 100)
release_slashright_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_slashright_staff.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_slashright_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashright_staff.add_master_flag(AnimationMasterFlag.PLAY)
release_slashright_staff.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.6, "attacks_staff_righttoleft", 16, 40)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_slashright_staff.add_sequence(seq0)


# release_slashright_staff_continue Animation
release_slashright_staff_continue = Animation("release_slashright_staff_continue")
release_slashright_staff_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_slashright_staff_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_slashright_staff_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_slashright_staff_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.4, "attacks_staff_righttoleft", 40, 48)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_slashright_staff_continue.add_sequence(seq0)


# blocked_slashright_staff Animation
blocked_slashright_staff = Animation("blocked_slashright_staff", 100)
blocked_slashright_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
blocked_slashright_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_slashright_staff.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_slashright_staff.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_slashright_staff.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_slashright_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_slashright_staff.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "anim_human", 27915, 27913)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
blocked_slashright_staff.add_sequence(seq0)


# parried_slashright_staff Animation
parried_slashright_staff = Animation("parried_slashright_staff", 100)
parried_slashright_staff.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
parried_slashright_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_slashright_staff.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_slashright_staff.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_slashright_staff.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_slashright_staff.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_slashright_staff.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 27915, 27913)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
parried_slashright_staff.add_sequence(seq0)


# defend_fist Animation
defend_fist = Animation("defend_fist")
defend_fist.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_fist.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_fist.add_master_flag(AnimationMasterFlag.PLAY)
defend_fist.add_master_flag(AnimationMasterFlag.KEEP)
defend_fist.add_master_flag(AnimationMasterFlag.RESTART)
defend_fist.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.75, "anim_human", 24950, 24960)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_fist.add_sequence(seq0)


# defend_fist_keep Animation
defend_fist_keep = Animation("defend_fist_keep")
defend_fist_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_fist_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_fist_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_fist_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "anim_human", 24950, 24960)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_fist_keep.add_sequence(seq0)


# defend_fist_parry_1 Animation
defend_fist_parry_1 = Animation("defend_fist_parry_1")
defend_fist_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_fist_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_fist_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_fist_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_fist_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_fist_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_fist_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 24962, 24970)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
defend_fist_parry_1.add_sequence(seq0)


# defend_fist_parry_2 Animation
defend_fist_parry_2 = Animation("defend_fist_parry_2")
defend_fist_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_fist_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_fist_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_fist_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_fist_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_fist_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_fist_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 24962, 24970)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
defend_fist_parry_2.add_sequence(seq0)


# defend_fist_parry_3 Animation
defend_fist_parry_3 = Animation("defend_fist_parry_3")
defend_fist_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_fist_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_fist_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_fist_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_fist_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_fist_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_fist_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 24962, 24970)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
defend_fist_parry_3.add_sequence(seq0)


# defend_shield_forward Animation
defend_shield_forward = Animation("defend_shield_forward")
defend_shield_forward.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_shield_forward.add_master_flag(AnimationMasterFlag.RIDER_ROT_SHIELD)
defend_shield_forward.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_shield_forward.add_master_flag(AnimationMasterFlag.PLAY)
defend_shield_forward.add_master_flag(AnimationMasterFlag.RESTART)
defend_shield_forward.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_shield_forward.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "defend_shield_forward", 6, 25)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_shield_forward.add_sequence(seq0)


# defend_shield_up Animation
defend_shield_up = Animation("defend_shield_up")
defend_shield_up.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_shield_up.add_master_flag(AnimationMasterFlag.RIDER_ROT_SHIELD)
defend_shield_up.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_shield_up.add_master_flag(AnimationMasterFlag.PLAY)
defend_shield_up.add_master_flag(AnimationMasterFlag.RESTART)
defend_shield_up.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_shield_up.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "defend_shield_up", 1, 27)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_shield_up.add_sequence(seq0)


# defend_shield_right Animation
defend_shield_right = Animation("defend_shield_right")
defend_shield_right.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_shield_right.add_master_flag(AnimationMasterFlag.RIDER_ROT_SHIELD)
defend_shield_right.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_shield_right.add_master_flag(AnimationMasterFlag.PLAY)
defend_shield_right.add_master_flag(AnimationMasterFlag.RESTART)
defend_shield_right.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_shield_right.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "defend_shield_right", 5, 26)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_shield_right.add_sequence(seq0)


# defend_shield_left Animation
defend_shield_left = Animation("defend_shield_left")
defend_shield_left.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_shield_left.add_master_flag(AnimationMasterFlag.RIDER_ROT_SHIELD)
defend_shield_left.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_shield_left.add_master_flag(AnimationMasterFlag.PLAY)
defend_shield_left.add_master_flag(AnimationMasterFlag.RESTART)
defend_shield_left.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_shield_left.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "defend_shield_left", 5, 26)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_shield_left.add_sequence(seq0)


# defend_shield Animation
defend_shield = Animation("defend_shield")
defend_shield.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_shield.add_master_flag(AnimationMasterFlag.RIDER_ROT_SHIELD)
defend_shield.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_shield.add_master_flag(AnimationMasterFlag.PLAY)
defend_shield.add_master_flag(AnimationMasterFlag.RESTART)
defend_shield.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_shield.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "defend_shield_up", 1, 17)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_shield.add_sequence(seq0)


# defend_shield_keep Animation
defend_shield_keep = Animation("defend_shield_keep", 100)
defend_shield_keep.add_flag(AnimationFlag.PARALLELS_FOR_LOOK_SLOPE)
defend_shield_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_shield_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_shield_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_shield_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "anim_human", 35118, 35120)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_4)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_shield_keep.add_sequence(seq0)


# defend_shield_parry_1 Animation
defend_shield_parry_1 = Animation("defend_shield_parry_1", 100)
defend_shield_parry_1.add_flag(AnimationFlag.PARALLELS_FOR_LOOK_SLOPE)
defend_shield_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_shield_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_shield_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_shield_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_shield_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_SHIELD)
defend_shield_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_shield_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 35121, 35130)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_shield_parry_1.add_sequence(seq0)


# defend_shield_parry_2 Animation
defend_shield_parry_2 = Animation("defend_shield_parry_2", 100)
defend_shield_parry_2.add_flag(AnimationFlag.PARALLELS_FOR_LOOK_SLOPE)
defend_shield_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_shield_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_shield_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_shield_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_shield_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_SHIELD)
defend_shield_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_shield_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 35121, 35130)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_shield_parry_2.add_sequence(seq0)


# defend_shield_parry_3 Animation
defend_shield_parry_3 = Animation("defend_shield_parry_3", 100)
defend_shield_parry_3.add_flag(AnimationFlag.PARALLELS_FOR_LOOK_SLOPE)
defend_shield_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_shield_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_shield_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_shield_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_shield_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_SHIELD)
defend_shield_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_shield_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 35121, 35130)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_shield_parry_3.add_sequence(seq0)


# defend_forward_greatsword Animation
defend_forward_greatsword = Animation("defend_forward_greatsword")
defend_forward_greatsword.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_forward_greatsword.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_greatsword.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_forward_greatsword.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_greatsword.add_master_flag(AnimationMasterFlag.KEEP)
defend_forward_greatsword.add_master_flag(AnimationMasterFlag.RESTART)
defend_forward_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_forward_greatsword.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "defend_twohanded", 0, 20)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_forward_greatsword.add_sequence(seq0)


# defend_forward_greatsword_keep Animation
defend_forward_greatsword_keep = Animation("defend_forward_greatsword_keep")
defend_forward_greatsword_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_forward_greatsword_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_greatsword_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_forward_greatsword_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_forward_greatsword_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "defend_twohanded", 170, 170)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_forward_greatsword_keep.add_sequence(seq0)


# defend_forward_greatsword_parry_1 Animation
defend_forward_greatsword_parry_1 = Animation("defend_forward_greatsword_parry_1")
defend_forward_greatsword_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_forward_greatsword_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_forward_greatsword_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_forward_greatsword_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_forward_greatsword_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_greatsword_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_greatsword_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "defend_twohanded", 350, 367)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_forward_greatsword_parry_1.add_sequence(seq0)


# defend_forward_greatsword_parry_2 Animation
defend_forward_greatsword_parry_2 = Animation("defend_forward_greatsword_parry_2")
defend_forward_greatsword_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_forward_greatsword_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_forward_greatsword_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_forward_greatsword_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_forward_greatsword_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_greatsword_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_greatsword_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "defend_twohanded", 350, 367)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_forward_greatsword_parry_2.add_sequence(seq0)


# defend_forward_greatsword_parry_3 Animation
defend_forward_greatsword_parry_3 = Animation("defend_forward_greatsword_parry_3")
defend_forward_greatsword_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_forward_greatsword_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_forward_greatsword_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_forward_greatsword_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_forward_greatsword_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_greatsword_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_greatsword_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "defend_twohanded", 350, 367)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_forward_greatsword_parry_3.add_sequence(seq0)


# defend_up_twohanded Animation
defend_up_twohanded = Animation("defend_up_twohanded")
defend_up_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_up_twohanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_twohanded.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_up_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_twohanded.add_master_flag(AnimationMasterFlag.KEEP)
defend_up_twohanded.add_master_flag(AnimationMasterFlag.RESTART)
defend_up_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_up_twohanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "anim_human", 35403, 35410)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_up_twohanded.add_sequence(seq0)


# defend_up_twohanded_keep Animation
defend_up_twohanded_keep = Animation("defend_up_twohanded_keep")
defend_up_twohanded_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_up_twohanded_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_twohanded_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_up_twohanded_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_up_twohanded_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "anim_human", 35410, 35410)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_up_twohanded_keep.add_sequence(seq0)


# defend_up_twohanded_parry_1 Animation
defend_up_twohanded_parry_1 = Animation("defend_up_twohanded_parry_1")
defend_up_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_up_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_up_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_up_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_up_twohanded_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_twohanded_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 35411, 35418)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_up_twohanded_parry_1.add_sequence(seq0)


# defend_up_twohanded_parry_2 Animation
defend_up_twohanded_parry_2 = Animation("defend_up_twohanded_parry_2")
defend_up_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_up_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_up_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_up_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_up_twohanded_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_twohanded_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 35411, 35418)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_up_twohanded_parry_2.add_sequence(seq0)


# defend_up_twohanded_parry_3 Animation
defend_up_twohanded_parry_3 = Animation("defend_up_twohanded_parry_3")
defend_up_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_up_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_up_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_up_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_up_twohanded_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_twohanded_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 35411, 35418)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_up_twohanded_parry_3.add_sequence(seq0)


# defend_right_twohanded Animation
defend_right_twohanded = Animation("defend_right_twohanded")
defend_right_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_right_twohanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_twohanded.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_right_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_twohanded.add_master_flag(AnimationMasterFlag.KEEP)
defend_right_twohanded.add_master_flag(AnimationMasterFlag.RESTART)
defend_right_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_right_twohanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "anim_human", 35510, 35520)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_right_twohanded.add_sequence(seq0)


# defend_right_twohanded_keep Animation
defend_right_twohanded_keep = Animation("defend_right_twohanded_keep")
defend_right_twohanded_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_right_twohanded_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_twohanded_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_right_twohanded_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_right_twohanded_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "anim_human", 35520, 35520)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_right_twohanded_keep.add_sequence(seq0)


# defend_right_twohanded_parry_1 Animation
defend_right_twohanded_parry_1 = Animation("defend_right_twohanded_parry_1")
defend_right_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_right_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_right_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_right_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_right_twohanded_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_twohanded_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 35521, 35528)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_right_twohanded_parry_1.add_sequence(seq0)


# defend_right_twohanded_parry_2 Animation
defend_right_twohanded_parry_2 = Animation("defend_right_twohanded_parry_2")
defend_right_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_right_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_right_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_right_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_right_twohanded_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_twohanded_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 35521, 35528)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_right_twohanded_parry_2.add_sequence(seq0)


# defend_right_twohanded_parry_3 Animation
defend_right_twohanded_parry_3 = Animation("defend_right_twohanded_parry_3")
defend_right_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_right_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_right_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_right_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_right_twohanded_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_twohanded_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 35521, 35528)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_right_twohanded_parry_3.add_sequence(seq0)


# defend_left_twohanded Animation
defend_left_twohanded = Animation("defend_left_twohanded")
defend_left_twohanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_left_twohanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_twohanded.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_left_twohanded.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_twohanded.add_master_flag(AnimationMasterFlag.KEEP)
defend_left_twohanded.add_master_flag(AnimationMasterFlag.RESTART)
defend_left_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_left_twohanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "anim_human", 35610, 35620)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_left_twohanded.add_sequence(seq0)


# defend_left_twohanded_keep Animation
defend_left_twohanded_keep = Animation("defend_left_twohanded_keep")
defend_left_twohanded_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_left_twohanded_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_twohanded_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_left_twohanded_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_left_twohanded_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "anim_human", 35620, 35620)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_left_twohanded_keep.add_sequence(seq0)


# defend_left_twohanded_parry_1 Animation
defend_left_twohanded_parry_1 = Animation("defend_left_twohanded_parry_1")
defend_left_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_left_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_left_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_left_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_left_twohanded_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_twohanded_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_twohanded_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 35620, 35630)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_left_twohanded_parry_1.add_sequence(seq0)


# defend_left_twohanded_parry_2 Animation
defend_left_twohanded_parry_2 = Animation("defend_left_twohanded_parry_2")
defend_left_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_left_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_left_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_left_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_left_twohanded_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_twohanded_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_twohanded_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 35620, 35630)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_left_twohanded_parry_2.add_sequence(seq0)


# defend_left_twohanded_parry_3 Animation
defend_left_twohanded_parry_3 = Animation("defend_left_twohanded_parry_3")
defend_left_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_left_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_left_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_left_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_left_twohanded_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_twohanded_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_twohanded_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 35620, 35630)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_left_twohanded_parry_3.add_sequence(seq0)


# defend_forward_onehanded Animation
defend_forward_onehanded = Animation("defend_forward_onehanded")
defend_forward_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_forward_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_onehanded.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_forward_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_onehanded.add_master_flag(AnimationMasterFlag.KEEP)
defend_forward_onehanded.add_master_flag(AnimationMasterFlag.RESTART)
defend_forward_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_forward_onehanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "defend_forward_onehanded", 20, 41)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_forward_onehanded.add_sequence(seq0)


# defend_forward_onehanded_keep Animation
defend_forward_onehanded_keep = Animation("defend_forward_onehanded_keep")
defend_forward_onehanded_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_forward_onehanded_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_onehanded_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_forward_onehanded_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_forward_onehanded_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(5.0, "defend_onehanded", 15, 70)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_forward_onehanded_keep.add_sequence(seq0)


# defend_forward_onehanded_parry_1 Animation
defend_forward_onehanded_parry_1 = Animation("defend_forward_onehanded_parry_1")
defend_forward_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_forward_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_forward_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_forward_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_forward_onehanded_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_onehanded_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "defend_onehanded", 75, 85)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_forward_onehanded_parry_1.add_sequence(seq0)


# defend_forward_onehanded_parry_2 Animation
defend_forward_onehanded_parry_2 = Animation("defend_forward_onehanded_parry_2")
defend_forward_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_forward_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_forward_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_forward_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_forward_onehanded_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_onehanded_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "defend_onehanded", 75, 85)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_forward_onehanded_parry_2.add_sequence(seq0)


# defend_forward_onehanded_parry_3 Animation
defend_forward_onehanded_parry_3 = Animation("defend_forward_onehanded_parry_3")
defend_forward_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_forward_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_forward_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_forward_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_forward_onehanded_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_onehanded_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "defend_onehanded", 75, 85)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_forward_onehanded_parry_3.add_sequence(seq0)


# defend_up_onehanded Animation
defend_up_onehanded = Animation("defend_up_onehanded")
defend_up_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_up_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_onehanded.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_up_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_onehanded.add_master_flag(AnimationMasterFlag.KEEP)
defend_up_onehanded.add_master_flag(AnimationMasterFlag.RESTART)
defend_up_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_up_onehanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "defend_up_onehanded", 9, 25)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_up_onehanded.add_sequence(seq0)


# defend_up_onehanded_keep Animation
defend_up_onehanded_keep = Animation("defend_up_onehanded_keep")
defend_up_onehanded_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_up_onehanded_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_onehanded_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_up_onehanded_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_up_onehanded_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.8, "defend_up_onehanded_keep", 1, 87)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_up_onehanded_keep.add_sequence(seq0)


# defend_up_onehanded_parry_1 Animation
defend_up_onehanded_parry_1 = Animation("defend_up_onehanded_parry_1")
defend_up_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_up_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_up_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_up_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_up_onehanded_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_onehanded_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 36121, 36130)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_up_onehanded_parry_1.add_sequence(seq0)


# defend_up_onehanded_parry_2 Animation
defend_up_onehanded_parry_2 = Animation("defend_up_onehanded_parry_2")
defend_up_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_up_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_up_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_up_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_up_onehanded_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_onehanded_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 36121, 36130)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_up_onehanded_parry_2.add_sequence(seq0)


# defend_up_onehanded_parry_3 Animation
defend_up_onehanded_parry_3 = Animation("defend_up_onehanded_parry_3")
defend_up_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_up_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_up_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_up_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_up_onehanded_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_onehanded_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 36121, 36130)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_up_onehanded_parry_3.add_sequence(seq0)


# defend_right_onehanded Animation
defend_right_onehanded = Animation("defend_right_onehanded")
defend_right_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_right_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_onehanded.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_right_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_onehanded.add_master_flag(AnimationMasterFlag.KEEP)
defend_right_onehanded.add_master_flag(AnimationMasterFlag.RESTART)
defend_right_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_right_onehanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "defend_right_onehanded", 14, 31)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_right_onehanded.add_sequence(seq0)


# defend_right_onehanded_keep Animation
defend_right_onehanded_keep = Animation("defend_right_onehanded_keep")
defend_right_onehanded_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_right_onehanded_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_onehanded_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_right_onehanded_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_right_onehanded_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.5, "defend_right_onehanded_keep", 0, 79)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_right_onehanded_keep.add_sequence(seq0)


# defend_right_onehanded_parry_1 Animation
defend_right_onehanded_parry_1 = Animation("defend_right_onehanded_parry_1")
defend_right_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_right_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_right_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_right_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_right_onehanded_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_onehanded_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 36221, 36230)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_right_onehanded_parry_1.add_sequence(seq0)


# defend_right_onehanded_parry_2 Animation
defend_right_onehanded_parry_2 = Animation("defend_right_onehanded_parry_2")
defend_right_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_right_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_right_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_right_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_right_onehanded_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_onehanded_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 36221, 36230)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_right_onehanded_parry_2.add_sequence(seq0)


# defend_right_onehanded_parry_3 Animation
defend_right_onehanded_parry_3 = Animation("defend_right_onehanded_parry_3")
defend_right_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_right_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_right_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_right_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_right_onehanded_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_onehanded_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 36221, 36230)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_right_onehanded_parry_3.add_sequence(seq0)


# defend_left_onehanded Animation
defend_left_onehanded = Animation("defend_left_onehanded")
defend_left_onehanded.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_left_onehanded.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_onehanded.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_left_onehanded.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_onehanded.add_master_flag(AnimationMasterFlag.KEEP)
defend_left_onehanded.add_master_flag(AnimationMasterFlag.RESTART)
defend_left_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_left_onehanded.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "defend_left_onehanded", 12, 28)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_left_onehanded.add_sequence(seq0)


# defend_left_onehanded_keep Animation
defend_left_onehanded_keep = Animation("defend_left_onehanded_keep")
defend_left_onehanded_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_left_onehanded_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_onehanded_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_left_onehanded_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_left_onehanded_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.2, "defend_left_onehanded_keep", 1, 71)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_left_onehanded_keep.add_sequence(seq0)


# defend_left_onehanded_parry_1 Animation
defend_left_onehanded_parry_1 = Animation("defend_left_onehanded_parry_1")
defend_left_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_left_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_left_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_left_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_left_onehanded_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_onehanded_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_onehanded_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 36321, 36330)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_left_onehanded_parry_1.add_sequence(seq0)


# defend_left_onehanded_parry_2 Animation
defend_left_onehanded_parry_2 = Animation("defend_left_onehanded_parry_2")
defend_left_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_left_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_left_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_left_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_left_onehanded_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_onehanded_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_onehanded_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 36321, 36330)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_left_onehanded_parry_2.add_sequence(seq0)


# defend_left_onehanded_parry_3 Animation
defend_left_onehanded_parry_3 = Animation("defend_left_onehanded_parry_3")
defend_left_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_left_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_left_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_left_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_left_onehanded_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_onehanded_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_onehanded_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 36321, 36330)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_left_onehanded_parry_3.add_sequence(seq0)


# defend_forward_staff Animation
defend_forward_staff = Animation("defend_forward_staff")
defend_forward_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_forward_staff.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_staff.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_forward_staff.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_staff.add_master_flag(AnimationMasterFlag.KEEP)
defend_forward_staff.add_master_flag(AnimationMasterFlag.RESTART)
defend_forward_staff.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_forward_staff.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "defend_staff", 0, 5)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_forward_staff.add_sequence(seq0)


# defend_forward_staff_keep Animation
defend_forward_staff_keep = Animation("defend_forward_staff_keep")
defend_forward_staff_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_forward_staff_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_staff_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_forward_staff_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_forward_staff_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "defend_staff", 5, 5)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_forward_staff_keep.add_sequence(seq0)


# defend_forward_staff_parry_1 Animation
defend_forward_staff_parry_1 = Animation("defend_forward_staff_parry_1")
defend_forward_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_forward_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_forward_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_forward_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_forward_staff_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_staff_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_staff_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "defend_staff", 56, 70)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_forward_staff_parry_1.add_sequence(seq0)


# defend_forward_staff_parry_2 Animation
defend_forward_staff_parry_2 = Animation("defend_forward_staff_parry_2")
defend_forward_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_forward_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_forward_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_forward_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_forward_staff_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_staff_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_staff_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "defend_staff", 56, 70)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_forward_staff_parry_2.add_sequence(seq0)


# defend_forward_staff_parry_3 Animation
defend_forward_staff_parry_3 = Animation("defend_forward_staff_parry_3")
defend_forward_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_forward_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_forward_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_forward_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_forward_staff_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_forward_staff_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_forward_staff_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "defend_staff", 56, 70)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_forward_staff_parry_3.add_sequence(seq0)


# defend_up_staff Animation
defend_up_staff = Animation("defend_up_staff")
defend_up_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_up_staff.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_staff.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_up_staff.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_staff.add_master_flag(AnimationMasterFlag.KEEP)
defend_up_staff.add_master_flag(AnimationMasterFlag.RESTART)
defend_up_staff.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_up_staff.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "anim_human", 37110, 37120)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_up_staff.add_sequence(seq0)


# defend_up_staff_keep Animation
defend_up_staff_keep = Animation("defend_up_staff_keep")
defend_up_staff_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_up_staff_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_staff_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_up_staff_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_up_staff_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "anim_human", 37120, 37120)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_up_staff_keep.add_sequence(seq0)


# defend_up_staff_parry_1 Animation
defend_up_staff_parry_1 = Animation("defend_up_staff_parry_1")
defend_up_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_up_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_up_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_up_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_up_staff_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_staff_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_staff_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 37121, 37130)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_up_staff_parry_1.add_sequence(seq0)


# defend_up_staff_parry_2 Animation
defend_up_staff_parry_2 = Animation("defend_up_staff_parry_2")
defend_up_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_up_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_up_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_up_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_up_staff_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_staff_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_staff_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 37121, 37130)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_up_staff_parry_2.add_sequence(seq0)


# defend_up_staff_parry_3 Animation
defend_up_staff_parry_3 = Animation("defend_up_staff_parry_3")
defend_up_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_up_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_up_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_up_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_up_staff_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_up_staff_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_up_staff_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 37121, 37130)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_up_staff_parry_3.add_sequence(seq0)


# defend_right_staff Animation
defend_right_staff = Animation("defend_right_staff")
defend_right_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_right_staff.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_staff.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_right_staff.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_staff.add_master_flag(AnimationMasterFlag.KEEP)
defend_right_staff.add_master_flag(AnimationMasterFlag.RESTART)
defend_right_staff.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_right_staff.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "anim_human", 37210, 37220)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_right_staff.add_sequence(seq0)


# defend_right_staff_keep Animation
defend_right_staff_keep = Animation("defend_right_staff_keep")
defend_right_staff_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_right_staff_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_staff_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_right_staff_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_right_staff_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "anim_human", 37220, 37220)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_right_staff_keep.add_sequence(seq0)


# defend_right_staff_parry_1 Animation
defend_right_staff_parry_1 = Animation("defend_right_staff_parry_1")
defend_right_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_right_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_right_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_right_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_right_staff_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_staff_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_staff_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 37221, 37230)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_right_staff_parry_1.add_sequence(seq0)


# defend_right_staff_parry_2 Animation
defend_right_staff_parry_2 = Animation("defend_right_staff_parry_2")
defend_right_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_right_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_right_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_right_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_right_staff_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_staff_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_staff_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 37221, 37230)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_right_staff_parry_2.add_sequence(seq0)


# defend_right_staff_parry_3 Animation
defend_right_staff_parry_3 = Animation("defend_right_staff_parry_3")
defend_right_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_right_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_right_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_right_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_right_staff_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_right_staff_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_right_staff_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 37221, 37230)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_right_staff_parry_3.add_sequence(seq0)


# defend_left_staff Animation
defend_left_staff = Animation("defend_left_staff")
defend_left_staff.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_left_staff.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_staff.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_left_staff.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_staff.add_master_flag(AnimationMasterFlag.KEEP)
defend_left_staff.add_master_flag(AnimationMasterFlag.RESTART)
defend_left_staff.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
defend_left_staff.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.75, "anim_human", 37310, 37320)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
defend_left_staff.add_sequence(seq0)


# defend_left_staff_keep Animation
defend_left_staff_keep = Animation("defend_left_staff_keep")
defend_left_staff_keep.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND)
defend_left_staff_keep.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_staff_keep.add_master_flag(AnimationMasterFlag.USE_DEFEND_SPEED)
defend_left_staff_keep.add_master_flag(AnimationMasterFlag.KEEP)
defend_left_staff_keep.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "anim_human", 37320, 37320)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
defend_left_staff_keep.add_sequence(seq0)


# defend_left_staff_parry_1 Animation
defend_left_staff_parry_1 = Animation("defend_left_staff_parry_1")
defend_left_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_left_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_left_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_left_staff_parry_1.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_left_staff_parry_1.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_staff_parry_1.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_staff_parry_1.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 37321, 37330)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_left_staff_parry_1.add_sequence(seq0)


# defend_left_staff_parry_2 Animation
defend_left_staff_parry_2 = Animation("defend_left_staff_parry_2")
defend_left_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_left_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_left_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_left_staff_parry_2.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_left_staff_parry_2.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_staff_parry_2.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_staff_parry_2.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_human", 37321, 37330)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_left_staff_parry_2.add_sequence(seq0)


# defend_left_staff_parry_3 Animation
defend_left_staff_parry_3 = Animation("defend_left_staff_parry_3")
defend_left_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
defend_left_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
defend_left_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
defend_left_staff_parry_3.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
defend_left_staff_parry_3.add_master_flag(AnimationMasterFlag.RIDER_ROT_DEFEND)
defend_left_staff_parry_3.add_master_flag(AnimationMasterFlag.PLAY)
defend_left_staff_parry_3.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_human", 37321, 37330)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
defend_left_staff_parry_3.add_sequence(seq0)


# strike_head_left Animation
strike_head_left = Animation("strike_head_left")
strike_head_left.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_head_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_head_left.add_master_flag(AnimationMasterFlag.PLAY)
strike_head_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes", 55, 71)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_head_left.add_sequence(seq0)


# strike_head_right Animation
strike_head_right = Animation("strike_head_right")
strike_head_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_head_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_head_right.add_master_flag(AnimationMasterFlag.PLAY)
strike_head_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes", 4, 19)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_head_right.add_sequence(seq0)


# strike_head_front Animation
strike_head_front = Animation("strike_head_front")
strike_head_front.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_head_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_head_front.add_master_flag(AnimationMasterFlag.PLAY)
strike_head_front.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes", 180, 198)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_head_front.add_sequence(seq0)


# strike_head_back Animation
strike_head_back = Animation("strike_head_back")
strike_head_back.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_head_back.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_head_back.add_master_flag(AnimationMasterFlag.PLAY)
strike_head_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "strikes_back", 4, 25)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_head_back.add_sequence(seq0)


# strike_chest_left Animation
strike_chest_left = Animation("strike_chest_left")
strike_chest_left.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_chest_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_chest_left.add_master_flag(AnimationMasterFlag.PLAY)
strike_chest_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes", 706, 724)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_chest_left.add_sequence(seq0)


# strike_chest_right Animation
strike_chest_right = Animation("strike_chest_right")
strike_chest_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_chest_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_chest_right.add_master_flag(AnimationMasterFlag.PLAY)
strike_chest_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "strikes", 487, 512)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_chest_right.add_sequence(seq0)


# strike_chest_front Animation
strike_chest_front = Animation("strike_chest_front")
strike_chest_front.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_chest_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_chest_front.add_master_flag(AnimationMasterFlag.PLAY)
strike_chest_front.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "strikes", 881, 905)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_chest_front.add_sequence(seq0)


# strike_chest_back Animation
strike_chest_back = Animation("strike_chest_back")
strike_chest_back.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_chest_back.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_chest_back.add_master_flag(AnimationMasterFlag.PLAY)
strike_chest_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes_back", 401, 418)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_chest_back.add_sequence(seq0)


# strike_abdomen_left Animation
strike_abdomen_left = Animation("strike_abdomen_left")
strike_abdomen_left.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_abdomen_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_abdomen_left.add_master_flag(AnimationMasterFlag.PLAY)
strike_abdomen_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.58, "strikes", 1425, 1444)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_abdomen_left.add_sequence(seq0)


# strike_abdomen_right Animation
strike_abdomen_right = Animation("strike_abdomen_right")
strike_abdomen_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_abdomen_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_abdomen_right.add_master_flag(AnimationMasterFlag.PLAY)
strike_abdomen_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "strikes", 1168, 1188)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_abdomen_right.add_sequence(seq0)


# strike_abdomen_front Animation
strike_abdomen_front = Animation("strike_abdomen_front")
strike_abdomen_front.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_abdomen_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_abdomen_front.add_master_flag(AnimationMasterFlag.PLAY)
strike_abdomen_front.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "strikes", 1618, 1640)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_abdomen_front.add_sequence(seq0)


# strike_abdomen_back Animation
strike_abdomen_back = Animation("strike_abdomen_back")
strike_abdomen_back.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_abdomen_back.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_abdomen_back.add_master_flag(AnimationMasterFlag.PLAY)
strike_abdomen_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.53, "strikes_back", 886, 904)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_abdomen_back.add_sequence(seq0)


# strike_legs_left Animation
strike_legs_left = Animation("strike_legs_left")
strike_legs_left.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_legs_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_legs_left.add_master_flag(AnimationMasterFlag.PLAY)
strike_legs_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.55, "strikes", 2284, 2305)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_legs_left.add_sequence(seq0)


# strike_legs_right Animation
strike_legs_right = Animation("strike_legs_right")
strike_legs_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_legs_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_legs_right.add_master_flag(AnimationMasterFlag.PLAY)
strike_legs_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.56, "strikes", 1999, 2020)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_legs_right.add_sequence(seq0)


# strike_legs_front Animation
strike_legs_front = Animation("strike_legs_front")
strike_legs_front.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_legs_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_legs_front.add_master_flag(AnimationMasterFlag.PLAY)
strike_legs_front.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.56, "strikes", 2655, 2676)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_legs_front.add_sequence(seq0)


# strike_legs_back Animation
strike_legs_back = Animation("strike_legs_back")
strike_legs_back.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_legs_back.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_legs_back.add_master_flag(AnimationMasterFlag.PLAY)
strike_legs_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes_back", 1120, 1137)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_legs_back.add_sequence(seq0)


# strike2_head_left Animation
strike2_head_left = Animation("strike2_head_left")
strike2_head_left.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_head_left.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_head_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_head_left.add_master_flag(AnimationMasterFlag.PLAY)
strike2_head_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes", 55, 71)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_head_left.add_sequence(seq0)


# strike2_head_right Animation
strike2_head_right = Animation("strike2_head_right")
strike2_head_right.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_head_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_head_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_head_right.add_master_flag(AnimationMasterFlag.PLAY)
strike2_head_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes", 4, 19)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_head_right.add_sequence(seq0)


# strike2_head_front Animation
strike2_head_front = Animation("strike2_head_front")
strike2_head_front.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_head_front.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_head_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_head_front.add_master_flag(AnimationMasterFlag.PLAY)
strike2_head_front.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes", 180, 198)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_head_front.add_sequence(seq0)


# strike2_head_back Animation
strike2_head_back = Animation("strike2_head_back")
strike2_head_back.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_head_back.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_head_back.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_head_back.add_master_flag(AnimationMasterFlag.PLAY)
strike2_head_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.55, "strikes_back", 4, 25)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_head_back.add_sequence(seq0)


# strike2_chest_left Animation
strike2_chest_left = Animation("strike2_chest_left")
strike2_chest_left.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_chest_left.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_chest_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_chest_left.add_master_flag(AnimationMasterFlag.PLAY)
strike2_chest_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes", 706, 724)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_chest_left.add_sequence(seq0)


# strike2_chest_right Animation
strike2_chest_right = Animation("strike2_chest_right")
strike2_chest_right.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_chest_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_chest_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_chest_right.add_master_flag(AnimationMasterFlag.PLAY)
strike2_chest_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.55, "strikes", 487, 512)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_chest_right.add_sequence(seq0)


# strike2_chest_front Animation
strike2_chest_front = Animation("strike2_chest_front")
strike2_chest_front.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_chest_front.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_chest_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_chest_front.add_master_flag(AnimationMasterFlag.PLAY)
strike2_chest_front.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.55, "strikes", 881, 905)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_chest_front.add_sequence(seq0)


# strike2_chest_back Animation
strike2_chest_back = Animation("strike2_chest_back")
strike2_chest_back.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_chest_back.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_chest_back.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_chest_back.add_master_flag(AnimationMasterFlag.PLAY)
strike2_chest_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes_back", 401, 418)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_chest_back.add_sequence(seq0)


# strike2_abdomen_left Animation
strike2_abdomen_left = Animation("strike2_abdomen_left")
strike2_abdomen_left.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_abdomen_left.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_abdomen_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_abdomen_left.add_master_flag(AnimationMasterFlag.PLAY)
strike2_abdomen_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.55, "strikes", 1425, 1444)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_abdomen_left.add_sequence(seq0)


# strike2_abdomen_right Animation
strike2_abdomen_right = Animation("strike2_abdomen_right")
strike2_abdomen_right.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_abdomen_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_abdomen_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_abdomen_right.add_master_flag(AnimationMasterFlag.PLAY)
strike2_abdomen_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.55, "strikes", 1168, 1188)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_abdomen_right.add_sequence(seq0)


# strike2_abdomen_front Animation
strike2_abdomen_front = Animation("strike2_abdomen_front")
strike2_abdomen_front.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_abdomen_front.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_abdomen_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_abdomen_front.add_master_flag(AnimationMasterFlag.PLAY)
strike2_abdomen_front.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.55, "strikes", 1618, 1640)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_abdomen_front.add_sequence(seq0)


# strike2_abdomen_back Animation
strike2_abdomen_back = Animation("strike2_abdomen_back")
strike2_abdomen_back.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_abdomen_back.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_abdomen_back.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_abdomen_back.add_master_flag(AnimationMasterFlag.PLAY)
strike2_abdomen_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.53, "strikes_back", 886, 904)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_abdomen_back.add_sequence(seq0)


# strike2_legs_left Animation
strike2_legs_left = Animation("strike2_legs_left")
strike2_legs_left.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_legs_left.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_legs_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_legs_left.add_master_flag(AnimationMasterFlag.PLAY)
strike2_legs_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.55, "strikes", 2284, 2305)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_legs_left.add_sequence(seq0)


# strike2_legs_right Animation
strike2_legs_right = Animation("strike2_legs_right")
strike2_legs_right.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_legs_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_legs_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_legs_right.add_master_flag(AnimationMasterFlag.PLAY)
strike2_legs_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.56, "strikes", 1999, 2020)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_legs_right.add_sequence(seq0)


# strike2_legs_front Animation
strike2_legs_front = Animation("strike2_legs_front")
strike2_legs_front.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_legs_front.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_legs_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_legs_front.add_master_flag(AnimationMasterFlag.PLAY)
strike2_legs_front.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.56, "strikes", 2655, 2676)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_legs_front.add_sequence(seq0)


# strike2_legs_back Animation
strike2_legs_back = Animation("strike2_legs_back")
strike2_legs_back.add_flag(AnimationFlag.ENFORCE_ALL)
strike2_legs_back.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike2_legs_back.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike2_legs_back.add_master_flag(AnimationMasterFlag.PLAY)
strike2_legs_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.5, "strikes_back", 1120, 1137)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike2_legs_back.add_sequence(seq0)


# strike3_head_left Animation
strike3_head_left = Animation("strike3_head_left")
strike3_head_left.add_flag(AnimationFlag.ENFORCE_ALL)
strike3_head_left.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike3_head_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike3_head_left.add_master_flag(AnimationMasterFlag.PLAY)
strike3_head_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.99, "strikes3_head", 107, 146)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike3_head_left.add_sequence(seq0)


# strike3_head_right Animation
strike3_head_right = Animation("strike3_head_right")
strike3_head_right.add_flag(AnimationFlag.ENFORCE_ALL)
strike3_head_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike3_head_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike3_head_right.add_master_flag(AnimationMasterFlag.PLAY)
strike3_head_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.9, "strikes3_head", 208, 251)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike3_head_right.add_sequence(seq0)


# strike3_head_front Animation
strike3_head_front = Animation("strike3_head_front")
strike3_head_front.add_flag(AnimationFlag.ENFORCE_ALL)
strike3_head_front.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike3_head_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike3_head_front.add_master_flag(AnimationMasterFlag.PLAY)
strike3_head_front.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.9, "strikes3_head", 14, 48)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike3_head_front.add_sequence(seq0)


# strike3_head_back Animation
strike3_head_back = Animation("strike3_head_back")
strike3_head_back.add_flag(AnimationFlag.ENFORCE_ALL)
strike3_head_back.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike3_head_back.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike3_head_back.add_master_flag(AnimationMasterFlag.PLAY)
strike3_head_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.9, "strikes3_head", 309, 346)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike3_head_back.add_sequence(seq0)


# strike3_chest_left Animation
strike3_chest_left = Animation("strike3_chest_left")
strike3_chest_left.add_flag(AnimationFlag.ENFORCE_ALL)
strike3_chest_left.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike3_chest_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike3_chest_left.add_master_flag(AnimationMasterFlag.PLAY)
strike3_chest_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.9, "strikes3_chest", 61, 97)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike3_chest_left.add_sequence(seq0)


# strike3_chest_right Animation
strike3_chest_right = Animation("strike3_chest_right")
strike3_chest_right.add_flag(AnimationFlag.ENFORCE_ALL)
strike3_chest_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike3_chest_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike3_chest_right.add_master_flag(AnimationMasterFlag.PLAY)
strike3_chest_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.9, "strikes3_chest", 108, 145)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike3_chest_right.add_sequence(seq0)


# strike3_chest_front Animation
strike3_chest_front = Animation("strike3_chest_front")
strike3_chest_front.add_flag(AnimationFlag.ENFORCE_ALL)
strike3_chest_front.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike3_chest_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike3_chest_front.add_master_flag(AnimationMasterFlag.PLAY)
strike3_chest_front.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.8, "strikes3_chest", 3, 27)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike3_chest_front.add_sequence(seq0)


# strike3_abdomen_left Animation
strike3_abdomen_left = Animation("strike3_abdomen_left")
strike3_abdomen_left.add_flag(AnimationFlag.ENFORCE_ALL)
strike3_abdomen_left.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike3_abdomen_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike3_abdomen_left.add_master_flag(AnimationMasterFlag.PLAY)
strike3_abdomen_left.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.9, "strikes3_abdomen", 105, 150)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike3_abdomen_left.add_sequence(seq0)


# strike3_abdomen_right Animation
strike3_abdomen_right = Animation("strike3_abdomen_right")
strike3_abdomen_right.add_flag(AnimationFlag.ENFORCE_ALL)
strike3_abdomen_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike3_abdomen_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike3_abdomen_right.add_master_flag(AnimationMasterFlag.PLAY)
strike3_abdomen_right.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.9, "strikes3_abdomen", 63, 98)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike3_abdomen_right.add_sequence(seq0)


# strike3_abdomen_front Animation
strike3_abdomen_front = Animation("strike3_abdomen_front")
strike3_abdomen_front.add_flag(AnimationFlag.ENFORCE_ALL)
strike3_abdomen_front.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike3_abdomen_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike3_abdomen_front.add_master_flag(AnimationMasterFlag.PLAY)
strike3_abdomen_front.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.9, "strikes3_abdomen", 4, 43)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike3_abdomen_front.add_sequence(seq0)


# strike3_abdomen_back Animation
strike3_abdomen_back = Animation("strike3_abdomen_back")
strike3_abdomen_back.add_flag(AnimationFlag.ENFORCE_ALL)
strike3_abdomen_back.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike3_abdomen_back.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike3_abdomen_back.add_master_flag(AnimationMasterFlag.PLAY)
strike3_abdomen_back.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(1.08, "strikes3_abdomen_back", 0, 53)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike3_abdomen_back.add_sequence(seq0)


# strike_head_front_left_reloc Animation
strike_head_front_left_reloc = Animation("strike_head_front_left_reloc")
strike_head_front_left_reloc.add_flag(AnimationFlag.ENFORCE_ALL)
strike_head_front_left_reloc.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_head_front_left_reloc.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_head_front_left_reloc.add_master_flag(AnimationMasterFlag.PLAY)
strike_head_front_left_reloc.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.6, "strike_frontal", 0, 37)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_head_front_left_reloc.add_sequence(seq0)


# fall_face_hold Animation
fall_face_hold = Animation("fall_face_hold")
fall_face_hold.add_flag(AnimationFlag.ALIGN_WITH_GROUND)
fall_face_hold.add_flag(AnimationFlag.ENFORCE_ALL)
fall_face_hold.add_flag(AnimationFlag.LOCK_CAMERA)
fall_face_hold.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
fall_face_hold.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
fall_face_hold.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
fall_face_hold.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(2.2, "death_face", 8, 60)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_16)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.5)
seq0.setExtraVals(7, 0.6)
fall_face_hold.add_sequence(seq0)


# fall_chest_front Animation
fall_chest_front = Animation("fall_chest_front")
fall_chest_front.add_flag(AnimationFlag.ALIGN_WITH_GROUND)
fall_chest_front.add_flag(AnimationFlag.ENFORCE_ALL)
fall_chest_front.add_flag(AnimationFlag.LOCK_CAMERA)
fall_chest_front.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
fall_chest_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
fall_chest_front.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
fall_chest_front.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(1.0, "death_chest", 4, 37)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_16)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.9)
seq0.setExtraVals(7, 0.5)
fall_chest_front.add_sequence(seq0)


# fall_abdomen_hold_front Animation
fall_abdomen_hold_front = Animation("fall_abdomen_hold_front")
fall_abdomen_hold_front.add_flag(AnimationFlag.ALIGN_WITH_GROUND)
fall_abdomen_hold_front.add_flag(AnimationFlag.ENFORCE_ALL)
fall_abdomen_hold_front.add_flag(AnimationFlag.LOCK_CAMERA)
fall_abdomen_hold_front.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
fall_abdomen_hold_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
fall_abdomen_hold_front.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
fall_abdomen_hold_front.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(2.7, "death_abdomen", 5, 96)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_16)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(7, 0.5)
fall_abdomen_hold_front.add_sequence(seq0)


# fall_head_front Animation
fall_head_front = Animation("fall_head_front")
fall_head_front.add_flag(AnimationFlag.ALIGN_WITH_GROUND)
fall_head_front.add_flag(AnimationFlag.ENFORCE_ALL)
fall_head_front.add_flag(AnimationFlag.LOCK_CAMERA)
fall_head_front.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
fall_head_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
fall_head_front.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
fall_head_front.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(1.2, "anim_human", 40100, 40138)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_16)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.8)
seq0.setExtraVals(7, 0.8)
fall_head_front.add_sequence(seq0)


# fall_right_front Animation
fall_right_front = Animation("fall_right_front")
fall_right_front.add_flag(AnimationFlag.ALIGN_WITH_GROUND)
fall_right_front.add_flag(AnimationFlag.ENFORCE_ALL)
fall_right_front.add_flag(AnimationFlag.LOCK_CAMERA)
fall_right_front.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
fall_right_front.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
fall_right_front.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
fall_right_front.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(2.0, "death2", 0, 53)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_16)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.65)
seq0.setExtraVals(7, 1.0)
fall_right_front.add_sequence(seq0)


# fall_body_back Animation
fall_body_back = Animation("fall_body_back")
fall_body_back.add_flag(AnimationFlag.ALIGN_WITH_GROUND)
fall_body_back.add_flag(AnimationFlag.ENFORCE_ALL)
fall_body_back.add_flag(AnimationFlag.LOCK_CAMERA)
fall_body_back.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
fall_body_back.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
fall_body_back.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
fall_body_back.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(2.7, "death", 0, 83)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_16)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.47)
seq0.setExtraVals(1, 0.82)
seq0.setExtraVals(7, 1.8)
fall_body_back.add_sequence(seq0)


# fall_rider_right_forward Animation
fall_rider_right_forward = Animation("fall_rider_right_forward")
fall_rider_right_forward.add_flag(AnimationFlag.ENFORCE_ALL)
fall_rider_right_forward.add_flag(AnimationFlag.LOCK_CAMERA)
fall_rider_right_forward.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
fall_rider_right_forward.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
fall_rider_right_forward.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
fall_rider_right_forward.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(2.2, "anim_human", 40200, 40275)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.8)
seq0.setExtraVals(7, 0.3)
fall_rider_right_forward.add_sequence(seq0)


# fall_rider_right Animation
fall_rider_right = Animation("fall_rider_right")
fall_rider_right.add_flag(AnimationFlag.ENFORCE_ALL)
fall_rider_right.add_flag(AnimationFlag.LOCK_CAMERA)
fall_rider_right.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
fall_rider_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
fall_rider_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
fall_rider_right.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(2.2, "anim_human", 40200, 40275)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.8)
seq0.setExtraVals(7, 0.3)
fall_rider_right.add_sequence(seq0)


# fall_rider_left Animation
fall_rider_left = Animation("fall_rider_left")
fall_rider_left.add_flag(AnimationFlag.ENFORCE_ALL)
fall_rider_left.add_flag(AnimationFlag.LOCK_CAMERA)
fall_rider_left.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
fall_rider_left.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
fall_rider_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
fall_rider_left.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(2.2, "anim_human", 40200, 40275)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.8)
seq0.setExtraVals(7, 0.3)
fall_rider_left.add_sequence(seq0)


# rider_fall_right Animation
rider_fall_right = Animation("rider_fall_right")
rider_fall_right.add_flag(AnimationFlag.ENFORCE_ALL)
rider_fall_right.add_flag(AnimationFlag.DISPLACE_POSITION)
rider_fall_right.add_master_flag(AnimationMasterFlag.PRIORITY_FALL_FROM_HORSE)
rider_fall_right.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
rider_fall_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
rider_fall_right.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(2.5, "anim_human_02", 350, 382)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
seq0.setExtraVals(4, 0.8)
seq0.setExtraVals(5, -1.8)
seq0.setExtraVals(7, 0.5)
rider_fall_right.add_sequence(seq0)


# rider_fall_roll Animation
rider_fall_roll = Animation("rider_fall_roll")
rider_fall_roll.add_flag(AnimationFlag.ENFORCE_ALL)
rider_fall_roll.add_flag(AnimationFlag.DISPLACE_POSITION)
rider_fall_roll.add_master_flag(AnimationMasterFlag.PRIORITY_FALL_FROM_HORSE)
rider_fall_roll.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
rider_fall_roll.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
rider_fall_roll.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(2.5, "anim_human", 42000, 42084)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
seq0.setExtraVals(7, 1.0)
rider_fall_roll.add_sequence(seq0)


# strike_chest_front_stop Animation
strike_chest_front_stop = Animation("strike_chest_front_stop")
strike_chest_front_stop.add_flag(AnimationFlag.ENFORCE_ALL)
strike_chest_front_stop.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_chest_front_stop.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_chest_front_stop.add_master_flag(AnimationMasterFlag.PLAY)
strike_chest_front_stop.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.4, "anim_human", 45000, 45010)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
strike_chest_front_stop.add_sequence(seq0)


# strike_fall_back_rise Animation
strike_fall_back_rise = Animation("strike_fall_back_rise")
strike_fall_back_rise.add_flag(AnimationFlag.ALIGN_WITH_GROUND)
strike_fall_back_rise.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
strike_fall_back_rise.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_fall_back_rise.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_fall_back_rise.add_master_flag(AnimationMasterFlag.PLAY)
strike_fall_back_rise.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(1.7, "anim_human", 45400, 45453)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(7, 0.5)
strike_fall_back_rise.add_sequence(seq0)


# strike_fall_back_rise_upper Animation
strike_fall_back_rise_upper = Animation("strike_fall_back_rise_upper")
strike_fall_back_rise_upper.add_flag(AnimationFlag.ALIGN_WITH_GROUND)
strike_fall_back_rise_upper.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
strike_fall_back_rise_upper.add_master_flag(AnimationMasterFlag.ACCURATE_BODY)
strike_fall_back_rise_upper.add_master_flag(AnimationMasterFlag.PLAY)
strike_fall_back_rise_upper.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(1.44, "anim_human", 45400, 45445)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
strike_fall_back_rise_upper.add_sequence(seq0)


# cheer Animation
cheer = Animation("cheer")
cheer.add_master_flag(AnimationMasterFlag.PRIORITY_MOUNT)
cheer.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(6.0, "man_cheer", 0, 185)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
cheer.add_sequence(seq0)
# sequence 1
seq1 = AnimationSequence(3.0, "man_cheer", 200, 289)
seq1.add_flag(AnimationSequenceFlag.BLEND_IN_5)
cheer.add_sequence(seq1)
# sequence 2
seq2 = AnimationSequence(4.5, "man_cheer", 300, 437)
seq2.add_flag(AnimationSequenceFlag.BLEND_IN_5)
cheer.add_sequence(seq2)
# sequence 3
seq3 = AnimationSequence(5.5, "man_cheer", 450, 617)
seq3.add_flag(AnimationSequenceFlag.BLEND_IN_5)
cheer.add_sequence(seq3)


# cheer_stand Animation
cheer_stand = Animation("cheer_stand", 16)
cheer_stand.add_master_flag(AnimationMasterFlag.PRIORITY_MOUNT)
cheer_stand.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(31.5, "man_cheer", 650, 1597)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
cheer_stand.add_sequence(seq0)


# stand_townguard Animation
stand_townguard = Animation("stand_townguard")
# sequence 0
seq0 = AnimationSequence(79.0, "stand_guardsman", 0, 2397)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
stand_townguard.add_sequence(seq0)


# stand_lady Animation
stand_lady = Animation("stand_lady")
# sequence 0
seq0 = AnimationSequence(29.0, "lady_stand", 0, 863)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
stand_lady.add_sequence(seq0)


# stand_lord Animation
stand_lord = Animation("stand_lord")
# sequence 0
seq0 = AnimationSequence(10.0, "lord_stand", 0, 111)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
stand_lord.add_sequence(seq0)


# dance Animation
dance = Animation("dance")
# sequence 0
seq0 = AnimationSequence(20.0, "anim_human", 0, 387)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
dance.add_sequence(seq0)


# pose_1 Animation
pose_1 = Animation("pose_1")
# sequence 0
seq0 = AnimationSequence(3.0, "poses", 0, 0)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
pose_1.add_sequence(seq0)


# pose_2 Animation
pose_2 = Animation("pose_2")
# sequence 0
seq0 = AnimationSequence(3.0, "poses", 2, 2)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
pose_2.add_sequence(seq0)


# pose_3 Animation
pose_3 = Animation("pose_3")
# sequence 0
seq0 = AnimationSequence(3.0, "poses", 4, 4)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
pose_3.add_sequence(seq0)


# pose_4 Animation
pose_4 = Animation("pose_4")
# sequence 0
seq0 = AnimationSequence(3.0, "poses", 6, 6)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
pose_4.add_sequence(seq0)


# pose_5 Animation
pose_5 = Animation("pose_5")
# sequence 0
seq0 = AnimationSequence(3.0, "poses", 8, 8)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
pose_5.add_sequence(seq0)


# wedding_guest Animation
wedding_guest = Animation("wedding_guest")
wedding_guest.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
wedding_guest.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(30.0, "wedding_guest", 0, 906)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
wedding_guest.add_sequence(seq0)


# wedding_guest_notr Animation
wedding_guest_notr = Animation("wedding_guest_notr")
wedding_guest_notr.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
wedding_guest_notr.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(32.0, "wedding_guest_notr", 0, 962)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
wedding_guest_notr.add_sequence(seq0)


# wedding_guest_woman Animation
wedding_guest_woman = Animation("wedding_guest_woman")
wedding_guest_woman.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
wedding_guest_woman.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(27.5, "wedding_guest_woman", 0, 825)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
wedding_guest_woman.add_sequence(seq0)


# wedding_dad_stairs Animation
wedding_dad_stairs = Animation("wedding_dad_stairs")
wedding_dad_stairs.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
wedding_dad_stairs.add_master_flag(AnimationMasterFlag.START_INSTANTLY)
wedding_dad_stairs.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(10.0, "wedding_dad_stairs", 0, 300)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
wedding_dad_stairs.add_sequence(seq0)


# wedding_dad_walk Animation
wedding_dad_walk = Animation("wedding_dad_walk")
wedding_dad_walk.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
wedding_dad_walk.add_master_flag(AnimationMasterFlag.START_INSTANTLY)
wedding_dad_walk.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(4.5, "wedding_dad_walk", 0, 134)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
wedding_dad_walk.add_sequence(seq0)


# wedding_bride_stairs Animation
wedding_bride_stairs = Animation("wedding_bride_stairs")
wedding_bride_stairs.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
wedding_bride_stairs.add_master_flag(AnimationMasterFlag.START_INSTANTLY)
wedding_bride_stairs.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(10.0, "wedding_bride_stairs", 0, 300)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
wedding_bride_stairs.add_sequence(seq0)


# wedding_bride_walk Animation
wedding_bride_walk = Animation("wedding_bride_walk")
wedding_bride_walk.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
wedding_bride_walk.add_master_flag(AnimationMasterFlag.START_INSTANTLY)
wedding_bride_walk.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(4.5, "wedding_bride_walk", 0, 134)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
wedding_bride_walk.add_sequence(seq0)


# wedding_groom_wait Animation
wedding_groom_wait = Animation("wedding_groom_wait")
wedding_groom_wait.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
wedding_groom_wait.add_master_flag(AnimationMasterFlag.START_INSTANTLY)
wedding_groom_wait.add_master_flag(AnimationMasterFlag.PLAY)
wedding_groom_wait.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(10.0, "wedding_groom_last", 0, 2)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
wedding_groom_wait.add_sequence(seq0)


# wedding_groom_last Animation
wedding_groom_last = Animation("wedding_groom_last")
wedding_groom_last.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
wedding_groom_last.add_master_flag(AnimationMasterFlag.START_INSTANTLY)
wedding_groom_last.add_master_flag(AnimationMasterFlag.PLAY)
wedding_groom_last.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(10.0, "wedding_groom_last", 0, 300)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
wedding_groom_last.add_sequence(seq0)


# wedding_dad_last Animation
wedding_dad_last = Animation("wedding_dad_last")
wedding_dad_last.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
wedding_dad_last.add_master_flag(AnimationMasterFlag.START_INSTANTLY)
wedding_dad_last.add_master_flag(AnimationMasterFlag.PLAY)
wedding_dad_last.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(10.0, "wedding_dad_last", 0, 300)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
wedding_dad_last.add_sequence(seq0)


# wedding_bride_last Animation
wedding_bride_last = Animation("wedding_bride_last")
wedding_bride_last.add_master_flag(AnimationMasterFlag.PRIORITY_DIE)
wedding_bride_last.add_master_flag(AnimationMasterFlag.START_INSTANTLY)
wedding_bride_last.add_master_flag(AnimationMasterFlag.PLAY)
wedding_bride_last.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(10.0, "wedding_bride_last", 0, 300)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
wedding_bride_last.add_sequence(seq0)


# equip_bayonet Animation
equip_bayonet = Animation("equip_bayonet")
equip_bayonet.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_bayonet.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_bayonet.add_master_flag(AnimationMasterFlag.PLAY)
equip_bayonet.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_musket", 5, 13)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_bayonet.add_sequence(seq0)


# unequip_bayonet Animation
unequip_bayonet = Animation("unequip_bayonet")
unequip_bayonet.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_bayonet.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_bayonet.add_master_flag(AnimationMasterFlag.PLAY)
unequip_bayonet.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_musket", 5, 13)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_bayonet.add_sequence(seq0)


# crouch_unarmed Animation
crouch_unarmed = Animation("crouch_unarmed")
crouch_unarmed.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(11.0, "crouch_stand_man", 0, 315)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
crouch_unarmed.add_sequence(seq0)


# crouch_single Animation
crouch_single = Animation("crouch_single")
crouch_single.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(11.0, "crouch_stand_man", 0, 315)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
crouch_single.add_sequence(seq0)


# crouch_greatsword Animation
crouch_greatsword = Animation("crouch_greatsword")
crouch_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(6.0, "crouch_greatsword_cstance", 0, 170)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.setExtraVals(7, 0.25)
crouch_greatsword.add_sequence(seq0)


# crouch_staff Animation
crouch_staff = Animation("crouch_staff")
crouch_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(5.0, "crouch_staff_cstance", 0, 120)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
crouch_staff.add_sequence(seq0)


# crouch_crossbow Animation
crouch_crossbow = Animation("crouch_crossbow")
crouch_crossbow.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "staff_cstance", 0, 60)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
crouch_crossbow.add_sequence(seq0)


# crouch_ready_pistol Animation
crouch_ready_pistol = Animation("crouch_ready_pistol", 100)
crouch_ready_pistol.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
crouch_ready_pistol.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
crouch_ready_pistol.add_master_flag(AnimationMasterFlag.RIDER_ROT_PISTOL)
crouch_ready_pistol.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
crouch_ready_pistol.add_master_flag(AnimationMasterFlag.KEEP)
crouch_ready_pistol.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "crouch_fire_pistol", 1, 12)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
crouch_ready_pistol.add_sequence(seq0)


# crouch_release_pistol Animation
crouch_release_pistol = Animation("crouch_release_pistol", 100)
crouch_release_pistol.add_flag(AnimationFlag.ROT_VERTICAL_SWORD)
crouch_release_pistol.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
crouch_release_pistol.add_master_flag(AnimationMasterFlag.RIDER_ROT_PISTOL)
crouch_release_pistol.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
crouch_release_pistol.add_master_flag(AnimationMasterFlag.PLAY)
crouch_release_pistol.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "crouch_fire_pistol", 12, 21)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
crouch_release_pistol.add_sequence(seq0)


# reload_musket_full Animation
reload_musket_full = Animation("reload_musket_full")
reload_musket_full.add_master_flag(AnimationMasterFlag.PRIORITY_RELOAD)
reload_musket_full.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
reload_musket_full.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(2.5, "man_reload", 0, 340)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.STICK_ITEM_TO_LEFT_HAND)
reload_musket_full.add_sequence(seq0)


# reload_musket_two_third Animation
reload_musket_two_third = Animation("reload_musket_two_third")
reload_musket_two_third.add_master_flag(AnimationMasterFlag.PRIORITY_RELOAD)
reload_musket_two_third.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
reload_musket_two_third.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.7, "man_reload", 110, 340)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.STICK_ITEM_TO_LEFT_HAND)
reload_musket_two_third.add_sequence(seq0)


# reload_musket_one_third Animation
reload_musket_one_third = Animation("reload_musket_one_third")
reload_musket_one_third.add_master_flag(AnimationMasterFlag.PRIORITY_RELOAD)
reload_musket_one_third.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
reload_musket_one_third.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "man_reload", 270, 340)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.STICK_ITEM_TO_LEFT_HAND)
reload_musket_one_third.add_sequence(seq0)


# crouch_pike Animation
crouch_pike = Animation("crouch_pike")
crouch_pike.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(3.3, "crouch_staff_cstance_attack", 0, 100)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
crouch_pike.add_sequence(seq0)


# crouch_pike_recover Animation
crouch_pike_recover = Animation("crouch_pike_recover")
crouch_pike_recover.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
crouch_pike_recover.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
crouch_pike_recover.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
crouch_pike_recover.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
crouch_pike_recover.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
crouch_pike_recover.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.2, "crouch_staff_cstance_attack", 105, 137)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
crouch_pike_recover.add_sequence(seq0)


# ready_overswing_spear Animation
ready_overswing_spear = Animation("ready_overswing_spear")
ready_overswing_spear.add_flag(AnimationFlag.OVERSWING)
ready_overswing_spear.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_overswing_spear.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_overswing_spear.add_master_flag(AnimationMasterFlag.KEEP)
ready_overswing_spear.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_overswing_spear.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "spear_thrust_overhead", 0, 20)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_overswing_spear.add_sequence(seq0)


# release_overswing_spear Animation
release_overswing_spear = Animation("release_overswing_spear")
release_overswing_spear.add_flag(AnimationFlag.OVERSWING)
release_overswing_spear.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_overswing_spear.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_overswing_spear.add_master_flag(AnimationMasterFlag.PLAY)
release_overswing_spear.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.6, "spear_thrust_overhead", 20, 41)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_overswing_spear.add_sequence(seq0)


# release_overswing_spear_continue Animation
release_overswing_spear_continue = Animation("release_overswing_spear_continue")
release_overswing_spear_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_overswing_spear_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_overswing_spear_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_overswing_spear_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "spear_thrust_overhead", 41, 52)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
release_overswing_spear_continue.add_sequence(seq0)


# parried_overswing_spear Animation
parried_overswing_spear = Animation("parried_overswing_spear")
parried_overswing_spear.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_overswing_spear.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_overswing_spear.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_overswing_spear.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_overswing_spear.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_overswing_spear.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "spear_thrust_overhead", 26, 22)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
parried_overswing_spear.add_sequence(seq0)


# blocked_overswing_spear Animation
blocked_overswing_spear = Animation("blocked_overswing_spear")
blocked_overswing_spear.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_overswing_spear.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_overswing_spear.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_overswing_spear.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_overswing_spear.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_overswing_spear.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "spear_thrust_overhead", 26, 22)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
blocked_overswing_spear.add_sequence(seq0)


# reload_pistol_half Animation
reload_pistol_half = Animation("reload_pistol_half")
reload_pistol_half.add_master_flag(AnimationMasterFlag.PRIORITY_RELOAD)
reload_pistol_half.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
reload_pistol_half.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.2, "reload_pistol_new", 125, 250)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
reload_pistol_half.add_sequence(seq0)


# ready_overswing_musket Animation
ready_overswing_musket = Animation("ready_overswing_musket")
ready_overswing_musket.add_flag(AnimationFlag.OVERSWING)
ready_overswing_musket.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_overswing_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_overswing_musket.add_master_flag(AnimationMasterFlag.KEEP)
ready_overswing_musket.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_overswing_musket.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "musket_upper_swing", 12, 24)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_overswing_musket.add_sequence(seq0)


# release_overswing_musket Animation
release_overswing_musket = Animation("release_overswing_musket")
release_overswing_musket.add_flag(AnimationFlag.OVERSWING)
release_overswing_musket.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_overswing_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_overswing_musket.add_master_flag(AnimationMasterFlag.PLAY)
release_overswing_musket.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.55, "musket_upper_swing", 24, 40)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_overswing_musket.add_sequence(seq0)


# release_overswing_musket_continue Animation
release_overswing_musket_continue = Animation("release_overswing_musket_continue")
release_overswing_musket_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_overswing_musket_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_overswing_musket_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_overswing_musket_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.4, "musket_upper_swing", 40, 48)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
release_overswing_musket_continue.add_sequence(seq0)


# parried_overswing_musket Animation
parried_overswing_musket = Animation("parried_overswing_musket")
parried_overswing_musket.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_overswing_musket.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_overswing_musket.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_overswing_musket.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_overswing_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_overswing_musket.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "musket_upper_swing", 34, 30)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
parried_overswing_musket.add_sequence(seq0)


# blocked_overswing_musket Animation
blocked_overswing_musket = Animation("blocked_overswing_musket")
blocked_overswing_musket.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_overswing_musket.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_overswing_musket.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_overswing_musket.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_overswing_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_overswing_musket.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "musket_upper_swing", 34, 30)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
blocked_overswing_musket.add_sequence(seq0)


# ready_thrust_musket Animation
ready_thrust_musket = Animation("ready_thrust_musket")
ready_thrust_musket.add_flag(AnimationFlag.OVERSWING)
ready_thrust_musket.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_thrust_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_thrust_musket.add_master_flag(AnimationMasterFlag.KEEP)
ready_thrust_musket.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_thrust_musket.add_master_flag(AnimationMasterFlag.USE_INERTIA)
# sequence 0
seq0 = AnimationSequence(0.35, "musket_thrust_forward", 1, 19)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_6)
ready_thrust_musket.add_sequence(seq0)


# release_thrust_musket Animation
release_thrust_musket = Animation("release_thrust_musket")
release_thrust_musket.add_flag(AnimationFlag.OVERSWING)
release_thrust_musket.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_thrust_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_musket.add_master_flag(AnimationMasterFlag.PLAY)
release_thrust_musket.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.9, "musket_thrust_forward", 19, 50)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_5)
release_thrust_musket.add_sequence(seq0)


# release_thrust_musket_continue Animation
release_thrust_musket_continue = Animation("release_thrust_musket_continue")
release_thrust_musket_continue.add_master_flag(AnimationMasterFlag.PRIORITY_CONTINUE)
release_thrust_musket_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_thrust_musket_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_thrust_musket_continue.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.2, "musket_thrust_forward", 50, 54)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
release_thrust_musket_continue.add_sequence(seq0)


# parried_thrust_musket Animation
parried_thrust_musket = Animation("parried_thrust_musket")
parried_thrust_musket.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
parried_thrust_musket.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
parried_thrust_musket.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
parried_thrust_musket.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_thrust_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_thrust_musket.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.6, "musket_thrust_forward_parry", 1, 9)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
parried_thrust_musket.add_sequence(seq0)


# blocked_thrust_musket Animation
blocked_thrust_musket = Animation("blocked_thrust_musket")
blocked_thrust_musket.add_master_flag(AnimationMasterFlag.PRIORITY_DEFEND_PARRY)
blocked_thrust_musket.add_master_flag(AnimationMasterFlag.PRIORITY_THROW)
blocked_thrust_musket.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_thrust_musket.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
blocked_thrust_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_thrust_musket.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.3, "musket_thrust_forward_parry", 1, 9)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
blocked_thrust_musket.add_sequence(seq0)


# equip_pistol_melee Animation
equip_pistol_melee = Animation("equip_pistol_melee")
equip_pistol_melee.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_pistol_melee.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
equip_pistol_melee.add_master_flag(AnimationMasterFlag.PLAY)
equip_pistol_melee.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_pistol", 0, 10)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_pistol_melee.add_sequence(seq0)


# unequip_pistol_melee Animation
unequip_pistol_melee = Animation("unequip_pistol_melee")
unequip_pistol_melee.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_pistol_melee.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
unequip_pistol_melee.add_master_flag(AnimationMasterFlag.PLAY)
unequip_pistol_melee.add_master_flag(AnimationMasterFlag.RESTART)
# sequence 0
seq0 = AnimationSequence(0.3, "equip_pistol", 0, 10)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_pistol_melee.add_sequence(seq0)


# unused_human_anim_44 Animation
unused_human_anim_44 = Animation("unused_human_anim_44")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_44.add_sequence(seq0)


# unused_human_anim_45 Animation
unused_human_anim_45 = Animation("unused_human_anim_45")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_45.add_sequence(seq0)


# unused_human_anim_46 Animation
unused_human_anim_46 = Animation("unused_human_anim_46")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_46.add_sequence(seq0)


# unused_human_anim_47 Animation
unused_human_anim_47 = Animation("unused_human_anim_47")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_47.add_sequence(seq0)


# unused_human_anim_48 Animation
unused_human_anim_48 = Animation("unused_human_anim_48")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_48.add_sequence(seq0)


# unused_human_anim_49 Animation
unused_human_anim_49 = Animation("unused_human_anim_49")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_49.add_sequence(seq0)


# unused_human_anim_50 Animation
unused_human_anim_50 = Animation("unused_human_anim_50")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_50.add_sequence(seq0)


# unused_human_anim_51 Animation
unused_human_anim_51 = Animation("unused_human_anim_51")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_51.add_sequence(seq0)


# unused_human_anim_52 Animation
unused_human_anim_52 = Animation("unused_human_anim_52")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_52.add_sequence(seq0)


# unused_human_anim_53 Animation
unused_human_anim_53 = Animation("unused_human_anim_53")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_53.add_sequence(seq0)


# unused_human_anim_54 Animation
unused_human_anim_54 = Animation("unused_human_anim_54")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_54.add_sequence(seq0)


# unused_human_anim_55 Animation
unused_human_anim_55 = Animation("unused_human_anim_55")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_55.add_sequence(seq0)


# unused_human_anim_56 Animation
unused_human_anim_56 = Animation("unused_human_anim_56")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_56.add_sequence(seq0)


# unused_human_anim_57 Animation
unused_human_anim_57 = Animation("unused_human_anim_57")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_57.add_sequence(seq0)


# unused_human_anim_58 Animation
unused_human_anim_58 = Animation("unused_human_anim_58")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_58.add_sequence(seq0)


# unused_human_anim_59 Animation
unused_human_anim_59 = Animation("unused_human_anim_59")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_59.add_sequence(seq0)


# unused_human_anim_60 Animation
unused_human_anim_60 = Animation("unused_human_anim_60")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_60.add_sequence(seq0)


# unused_human_anim_61 Animation
unused_human_anim_61 = Animation("unused_human_anim_61")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_61.add_sequence(seq0)


# unused_human_anim_62 Animation
unused_human_anim_62 = Animation("unused_human_anim_62")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_62.add_sequence(seq0)


# unused_human_anim_63 Animation
unused_human_anim_63 = Animation("unused_human_anim_63")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_63.add_sequence(seq0)


# unused_human_anim_64 Animation
unused_human_anim_64 = Animation("unused_human_anim_64")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_64.add_sequence(seq0)


# unused_human_anim_65 Animation
unused_human_anim_65 = Animation("unused_human_anim_65")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_65.add_sequence(seq0)


# unused_human_anim_66 Animation
unused_human_anim_66 = Animation("unused_human_anim_66")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_66.add_sequence(seq0)


# unused_human_anim_67 Animation
unused_human_anim_67 = Animation("unused_human_anim_67")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_67.add_sequence(seq0)


# unused_human_anim_68 Animation
unused_human_anim_68 = Animation("unused_human_anim_68")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_68.add_sequence(seq0)


# unused_human_anim_69 Animation
unused_human_anim_69 = Animation("unused_human_anim_69")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_69.add_sequence(seq0)


# unused_human_anim_70 Animation
unused_human_anim_70 = Animation("unused_human_anim_70")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_70.add_sequence(seq0)


# unused_human_anim_71 Animation
unused_human_anim_71 = Animation("unused_human_anim_71")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_71.add_sequence(seq0)


# unused_human_anim_72 Animation
unused_human_anim_72 = Animation("unused_human_anim_72")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_72.add_sequence(seq0)


# unused_human_anim_73 Animation
unused_human_anim_73 = Animation("unused_human_anim_73")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_73.add_sequence(seq0)


# unused_human_anim_74 Animation
unused_human_anim_74 = Animation("unused_human_anim_74")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_74.add_sequence(seq0)


# unused_human_anim_75 Animation
unused_human_anim_75 = Animation("unused_human_anim_75")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_75.add_sequence(seq0)


# unused_human_anim_76 Animation
unused_human_anim_76 = Animation("unused_human_anim_76")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_76.add_sequence(seq0)


# unused_human_anim_77 Animation
unused_human_anim_77 = Animation("unused_human_anim_77")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_77.add_sequence(seq0)


# unused_human_anim_78 Animation
unused_human_anim_78 = Animation("unused_human_anim_78")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_78.add_sequence(seq0)


# unused_human_anim_79 Animation
unused_human_anim_79 = Animation("unused_human_anim_79")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_79.add_sequence(seq0)


# unused_human_anim_80 Animation
unused_human_anim_80 = Animation("unused_human_anim_80")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_80.add_sequence(seq0)


# unused_human_anim_81 Animation
unused_human_anim_81 = Animation("unused_human_anim_81")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_81.add_sequence(seq0)


# unused_human_anim_82 Animation
unused_human_anim_82 = Animation("unused_human_anim_82")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_82.add_sequence(seq0)


# unused_human_anim_83 Animation
unused_human_anim_83 = Animation("unused_human_anim_83")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_83.add_sequence(seq0)


# unused_human_anim_84 Animation
unused_human_anim_84 = Animation("unused_human_anim_84")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_84.add_sequence(seq0)


# unused_human_anim_85 Animation
unused_human_anim_85 = Animation("unused_human_anim_85")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_85.add_sequence(seq0)


# unused_human_anim_86 Animation
unused_human_anim_86 = Animation("unused_human_anim_86")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_86.add_sequence(seq0)


# unused_human_anim_87 Animation
unused_human_anim_87 = Animation("unused_human_anim_87")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_87.add_sequence(seq0)


# unused_human_anim_88 Animation
unused_human_anim_88 = Animation("unused_human_anim_88")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_88.add_sequence(seq0)


# unused_human_anim_89 Animation
unused_human_anim_89 = Animation("unused_human_anim_89")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_89.add_sequence(seq0)


# unused_human_anim_90 Animation
unused_human_anim_90 = Animation("unused_human_anim_90")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_90.add_sequence(seq0)


# unused_human_anim_91 Animation
unused_human_anim_91 = Animation("unused_human_anim_91")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_91.add_sequence(seq0)


# unused_human_anim_92 Animation
unused_human_anim_92 = Animation("unused_human_anim_92")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_92.add_sequence(seq0)


# unused_human_anim_93 Animation
unused_human_anim_93 = Animation("unused_human_anim_93")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_93.add_sequence(seq0)


# unused_human_anim_94 Animation
unused_human_anim_94 = Animation("unused_human_anim_94")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_94.add_sequence(seq0)


# unused_human_anim_95 Animation
unused_human_anim_95 = Animation("unused_human_anim_95")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_95.add_sequence(seq0)


# unused_human_anim_96 Animation
unused_human_anim_96 = Animation("unused_human_anim_96")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_96.add_sequence(seq0)


# unused_human_anim_97 Animation
unused_human_anim_97 = Animation("unused_human_anim_97")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_97.add_sequence(seq0)


# unused_human_anim_98 Animation
unused_human_anim_98 = Animation("unused_human_anim_98")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_98.add_sequence(seq0)


# unused_human_anim_99 Animation
unused_human_anim_99 = Animation("unused_human_anim_99")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_99.add_sequence(seq0)


# unused_human_anim_100 Animation
unused_human_anim_100 = Animation("unused_human_anim_100")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_human", 0, 1)
unused_human_anim_100.add_sequence(seq0)


# horse_stand Animation
horse_stand = Animation("horse_stand")
horse_stand.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.5, "anim_horse", 600, 644)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq0)
# sequence 1
seq1 = AnimationSequence(1.5, "anim_horse", 600, 644)
seq1.add_flag(AnimationSequenceFlag.CYCLIC)
seq1.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq1)
# sequence 2
seq2 = AnimationSequence(1.5, "anim_horse", 600, 644)
seq2.add_flag(AnimationSequenceFlag.CYCLIC)
seq2.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq2)
# sequence 3
seq3 = AnimationSequence(1.5, "anim_horse", 644, 688)
seq3.add_flag(AnimationSequenceFlag.CYCLIC)
seq3.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq3)
# sequence 4
seq4 = AnimationSequence(1.5, "anim_horse", 600, 644)
seq4.add_flag(AnimationSequenceFlag.CYCLIC)
seq4.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq4)
# sequence 5
seq5 = AnimationSequence(1.5, "anim_horse", 688, 732)
seq5.add_flag(AnimationSequenceFlag.CYCLIC)
seq5.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq5)
# sequence 6
seq6 = AnimationSequence(1.5, "anim_horse", 600, 644)
seq6.add_flag(AnimationSequenceFlag.CYCLIC)
seq6.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq6)
# sequence 7
seq7 = AnimationSequence(3.5, "anim_horse", 732, 820)
seq7.add_flag(AnimationSequenceFlag.CYCLIC)
seq7.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq7)
# sequence 8
seq8 = AnimationSequence(1.5, "anim_horse", 600, 644)
seq8.add_flag(AnimationSequenceFlag.CYCLIC)
seq8.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq8)
# sequence 9
seq9 = AnimationSequence(1.5, "anim_horse", 600, 644)
seq9.add_flag(AnimationSequenceFlag.CYCLIC)
seq9.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq9)
# sequence 10
seq10 = AnimationSequence(1.5, "anim_horse", 600, 644)
seq10.add_flag(AnimationSequenceFlag.CYCLIC)
seq10.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq10)
# sequence 11
seq11 = AnimationSequence(2.5, "anim_horse", 820, 908)
seq11.add_flag(AnimationSequenceFlag.CYCLIC)
seq11.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
horse_stand.add_sequence(seq11)


# horse_pace_1 Animation
horse_pace_1 = Animation("horse_pace_1")
horse_pace_1.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
horse_pace_1.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
horse_pace_1.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 31)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.25)
seq0.setExtraVals(1, 0.42)
seq0.setExtraVals(2, 0.75)
seq0.setExtraVals(3, 0.92)
seq0.setExtraVals(7, 0.25)
horse_pace_1.add_sequence(seq0)


# horse_pace_2 Animation
horse_pace_2 = Animation("horse_pace_2")
horse_pace_2.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
horse_pace_2.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
horse_pace_2.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "anim_horse", 50, 69)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.15)
seq0.setExtraVals(1, 0.16)
seq0.setExtraVals(2, 0.65)
seq0.setExtraVals(3, 0.66)
seq0.setExtraVals(7, 0.9)
horse_pace_2.add_sequence(seq0)


# horse_pace_3 Animation
horse_pace_3 = Animation("horse_pace_3")
horse_pace_3.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
horse_pace_3.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
horse_pace_3.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.6, "anim_horse", 100, 116)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.93)
seq0.setExtraVals(1, 0.95)
seq0.setExtraVals(2, 0.35)
seq0.setExtraVals(3, 0.42)
seq0.setExtraVals(7, 0.6)
horse_pace_3.add_sequence(seq0)


# horse_pace_4 Animation
horse_pace_4 = Animation("horse_pace_4")
horse_pace_4.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
horse_pace_4.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
horse_pace_4.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.5, "anim_horse", 150, 165)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.31)
seq0.setExtraVals(2, 0.79)
seq0.setExtraVals(3, 0.94)
seq0.setExtraVals(7, 0.2)
horse_pace_4.add_sequence(seq0)


# horse_walk_backward Animation
horse_walk_backward = Animation("horse_walk_backward")
horse_walk_backward.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
horse_walk_backward.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.9, "anim_horse", 31, 0)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.setExtraVals(0, 0.07)
seq0.setExtraVals(1, 0.13)
seq0.setExtraVals(2, 0.56)
seq0.setExtraVals(3, 0.63)
horse_walk_backward.add_sequence(seq0)


# horse_rear Animation
horse_rear = Animation("horse_rear")
horse_rear.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
horse_rear.add_flag(AnimationFlag.IGNORE_SLOPE)
horse_rear.add_master_flag(AnimationMasterFlag.PRIORITY_REAR)
horse_rear.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.7, "anim_horse", 265, 297)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
horse_rear.add_sequence(seq0)


# horse_jump Animation
horse_jump = Animation("horse_jump")
horse_jump.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
horse_jump.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP)
horse_jump.add_master_flag(AnimationMasterFlag.PRIORITY_RIDE)
horse_jump.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
horse_jump.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(1.6, "anim_horse", 205, 222)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_4)
horse_jump.add_sequence(seq0)


# horse_jump_end Animation
horse_jump_end = Animation("horse_jump_end")
horse_jump_end.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
horse_jump_end.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
horse_jump_end.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP_END)
horse_jump_end.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
horse_jump_end.add_master_flag(AnimationMasterFlag.PLAY)
# sequence 0
seq0 = AnimationSequence(0.1, "anim_horse", 222, 224)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
horse_jump_end.add_sequence(seq0)


# horse_turn_right Animation
horse_turn_right = Animation("horse_turn_right")
horse_turn_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 500, 533)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_4)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
horse_turn_right.add_sequence(seq0)


# horse_turn_left Animation
horse_turn_left = Animation("horse_turn_left")
horse_turn_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 450, 483)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_4)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
horse_turn_left.add_sequence(seq0)


# horse_turn_right_head Animation
horse_turn_right_head = Animation("horse_turn_right_head")
horse_turn_right_head.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 500, 533)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_4)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
horse_turn_right_head.add_sequence(seq0)


# horse_turn_left_head Animation
horse_turn_left_head = Animation("horse_turn_left_head")
horse_turn_left_head.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 450, 483)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_4)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
horse_turn_left_head.add_sequence(seq0)


# horse_slow Animation
horse_slow = Animation("horse_slow")
horse_slow.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(3.0, "anim_horse", 0, 31)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
horse_slow.add_sequence(seq0)
# sequence 1
seq1 = AnimationSequence(1.5, "anim_horse", 0, 31)
seq1.add_flag(AnimationSequenceFlag.CYCLIC)
horse_slow.add_sequence(seq1)


# horse_fall_in_place Animation
horse_fall_in_place = Animation("horse_fall_in_place")
horse_fall_in_place.add_flag(AnimationFlag.ALIGN_WITH_GROUND)
horse_fall_in_place.add_flag(AnimationFlag.ENFORCE_ALL)
horse_fall_in_place.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
horse_fall_in_place.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
horse_fall_in_place.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(4.0, "anim_horse", 0, 38)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_16)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
horse_fall_in_place.add_sequence(seq0)


# horse_fall_right Animation
horse_fall_right = Animation("horse_fall_right")
horse_fall_right.add_flag(AnimationFlag.ALIGN_WITH_GROUND)
horse_fall_right.add_flag(AnimationFlag.ENFORCE_ALL)
horse_fall_right.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
horse_fall_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
horse_fall_right.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(1.75, "anim_horse", 350, 375)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.6)
seq0.setExtraVals(7, 0.5)
horse_fall_right.add_sequence(seq0)


# horse_fall_roll Animation
horse_fall_roll = Animation("horse_fall_roll")
horse_fall_roll.add_flag(AnimationFlag.ALIGN_WITH_GROUND)
horse_fall_roll.add_flag(AnimationFlag.ENFORCE_ALL)
horse_fall_roll.add_master_flag(AnimationMasterFlag.PRIORITY_STRIKED)
horse_fall_roll.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
horse_fall_roll.add_master_flag(AnimationMasterFlag.KEEP)
# sequence 0
seq0 = AnimationSequence(2.5, "anim_horse", 400, 428)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
seq0.add_flag(AnimationSequenceFlag.MAKE_CUSTOM_SOUND)
seq0.setExtraVals(0, 0.3)
seq0.setExtraVals(7, 1.8)
horse_fall_roll.add_sequence(seq0)


# unused_horse_anim_1 Animation
unused_horse_anim_1 = Animation("unused_horse_anim_1")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_1.add_sequence(seq0)


# unused_horse_anim_2 Animation
unused_horse_anim_2 = Animation("unused_horse_anim_2")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_2.add_sequence(seq0)


# unused_horse_anim_3 Animation
unused_horse_anim_3 = Animation("unused_horse_anim_3")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_3.add_sequence(seq0)


# unused_horse_anim_4 Animation
unused_horse_anim_4 = Animation("unused_horse_anim_4")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_4.add_sequence(seq0)


# unused_horse_anim_5 Animation
unused_horse_anim_5 = Animation("unused_horse_anim_5")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_5.add_sequence(seq0)


# unused_horse_anim_6 Animation
unused_horse_anim_6 = Animation("unused_horse_anim_6")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_6.add_sequence(seq0)


# unused_horse_anim_7 Animation
unused_horse_anim_7 = Animation("unused_horse_anim_7")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_7.add_sequence(seq0)


# unused_horse_anim_8 Animation
unused_horse_anim_8 = Animation("unused_horse_anim_8")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_8.add_sequence(seq0)


# unused_horse_anim_9 Animation
unused_horse_anim_9 = Animation("unused_horse_anim_9")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_9.add_sequence(seq0)


# unused_horse_anim_10 Animation
unused_horse_anim_10 = Animation("unused_horse_anim_10")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_10.add_sequence(seq0)


# unused_horse_anim_11 Animation
unused_horse_anim_11 = Animation("unused_horse_anim_11")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_11.add_sequence(seq0)


# unused_horse_anim_12 Animation
unused_horse_anim_12 = Animation("unused_horse_anim_12")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_12.add_sequence(seq0)


# unused_horse_anim_13 Animation
unused_horse_anim_13 = Animation("unused_horse_anim_13")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_13.add_sequence(seq0)


# unused_horse_anim_14 Animation
unused_horse_anim_14 = Animation("unused_horse_anim_14")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_14.add_sequence(seq0)


# unused_horse_anim_15 Animation
unused_horse_anim_15 = Animation("unused_horse_anim_15")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_15.add_sequence(seq0)


# unused_horse_anim_16 Animation
unused_horse_anim_16 = Animation("unused_horse_anim_16")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_16.add_sequence(seq0)


# unused_horse_anim_17 Animation
unused_horse_anim_17 = Animation("unused_horse_anim_17")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_17.add_sequence(seq0)


# unused_horse_anim_18 Animation
unused_horse_anim_18 = Animation("unused_horse_anim_18")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_18.add_sequence(seq0)


# unused_horse_anim_19 Animation
unused_horse_anim_19 = Animation("unused_horse_anim_19")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_19.add_sequence(seq0)


# unused_horse_anim_20 Animation
unused_horse_anim_20 = Animation("unused_horse_anim_20")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_20.add_sequence(seq0)


# unused_horse_anim_21 Animation
unused_horse_anim_21 = Animation("unused_horse_anim_21")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_21.add_sequence(seq0)


# unused_horse_anim_22 Animation
unused_horse_anim_22 = Animation("unused_horse_anim_22")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_22.add_sequence(seq0)


# unused_horse_anim_23 Animation
unused_horse_anim_23 = Animation("unused_horse_anim_23")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_23.add_sequence(seq0)


# unused_horse_anim_24 Animation
unused_horse_anim_24 = Animation("unused_horse_anim_24")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_24.add_sequence(seq0)


# unused_horse_anim_25 Animation
unused_horse_anim_25 = Animation("unused_horse_anim_25")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_25.add_sequence(seq0)


# unused_horse_anim_26 Animation
unused_horse_anim_26 = Animation("unused_horse_anim_26")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_26.add_sequence(seq0)


# unused_horse_anim_27 Animation
unused_horse_anim_27 = Animation("unused_horse_anim_27")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_27.add_sequence(seq0)


# unused_horse_anim_28 Animation
unused_horse_anim_28 = Animation("unused_horse_anim_28")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_28.add_sequence(seq0)


# unused_horse_anim_29 Animation
unused_horse_anim_29 = Animation("unused_horse_anim_29")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_29.add_sequence(seq0)


# unused_horse_anim_30 Animation
unused_horse_anim_30 = Animation("unused_horse_anim_30")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_30.add_sequence(seq0)


# unused_horse_anim_31 Animation
unused_horse_anim_31 = Animation("unused_horse_anim_31")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_31.add_sequence(seq0)


# unused_horse_anim_32 Animation
unused_horse_anim_32 = Animation("unused_horse_anim_32")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_32.add_sequence(seq0)


# unused_horse_anim_33 Animation
unused_horse_anim_33 = Animation("unused_horse_anim_33")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_33.add_sequence(seq0)


# unused_horse_anim_34 Animation
unused_horse_anim_34 = Animation("unused_horse_anim_34")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_34.add_sequence(seq0)


# unused_horse_anim_35 Animation
unused_horse_anim_35 = Animation("unused_horse_anim_35")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_35.add_sequence(seq0)


# unused_horse_anim_36 Animation
unused_horse_anim_36 = Animation("unused_horse_anim_36")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_36.add_sequence(seq0)


# unused_horse_anim_37 Animation
unused_horse_anim_37 = Animation("unused_horse_anim_37")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_37.add_sequence(seq0)


# unused_horse_anim_38 Animation
unused_horse_anim_38 = Animation("unused_horse_anim_38")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_38.add_sequence(seq0)


# unused_horse_anim_39 Animation
unused_horse_anim_39 = Animation("unused_horse_anim_39")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_39.add_sequence(seq0)


# unused_horse_anim_40 Animation
unused_horse_anim_40 = Animation("unused_horse_anim_40")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_40.add_sequence(seq0)


# unused_horse_anim_41 Animation
unused_horse_anim_41 = Animation("unused_horse_anim_41")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_41.add_sequence(seq0)


# unused_horse_anim_42 Animation
unused_horse_anim_42 = Animation("unused_horse_anim_42")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_42.add_sequence(seq0)


# unused_horse_anim_43 Animation
unused_horse_anim_43 = Animation("unused_horse_anim_43")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_43.add_sequence(seq0)


# unused_horse_anim_44 Animation
unused_horse_anim_44 = Animation("unused_horse_anim_44")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_44.add_sequence(seq0)


# unused_horse_anim_45 Animation
unused_horse_anim_45 = Animation("unused_horse_anim_45")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_45.add_sequence(seq0)


# unused_horse_anim_46 Animation
unused_horse_anim_46 = Animation("unused_horse_anim_46")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_46.add_sequence(seq0)


# unused_horse_anim_47 Animation
unused_horse_anim_47 = Animation("unused_horse_anim_47")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_47.add_sequence(seq0)


# unused_horse_anim_48 Animation
unused_horse_anim_48 = Animation("unused_horse_anim_48")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_48.add_sequence(seq0)


# unused_horse_anim_49 Animation
unused_horse_anim_49 = Animation("unused_horse_anim_49")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_49.add_sequence(seq0)


# unused_horse_anim_50 Animation
unused_horse_anim_50 = Animation("unused_horse_anim_50")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_50.add_sequence(seq0)


# unused_horse_anim_51 Animation
unused_horse_anim_51 = Animation("unused_horse_anim_51")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_51.add_sequence(seq0)


# unused_horse_anim_52 Animation
unused_horse_anim_52 = Animation("unused_horse_anim_52")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_52.add_sequence(seq0)


# unused_horse_anim_53 Animation
unused_horse_anim_53 = Animation("unused_horse_anim_53")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_53.add_sequence(seq0)


# unused_horse_anim_54 Animation
unused_horse_anim_54 = Animation("unused_horse_anim_54")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_54.add_sequence(seq0)


# unused_horse_anim_55 Animation
unused_horse_anim_55 = Animation("unused_horse_anim_55")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_55.add_sequence(seq0)


# unused_horse_anim_56 Animation
unused_horse_anim_56 = Animation("unused_horse_anim_56")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_56.add_sequence(seq0)


# unused_horse_anim_57 Animation
unused_horse_anim_57 = Animation("unused_horse_anim_57")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_57.add_sequence(seq0)


# unused_horse_anim_58 Animation
unused_horse_anim_58 = Animation("unused_horse_anim_58")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_58.add_sequence(seq0)


# unused_horse_anim_59 Animation
unused_horse_anim_59 = Animation("unused_horse_anim_59")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_59.add_sequence(seq0)


# unused_horse_anim_60 Animation
unused_horse_anim_60 = Animation("unused_horse_anim_60")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_60.add_sequence(seq0)


# unused_horse_anim_61 Animation
unused_horse_anim_61 = Animation("unused_horse_anim_61")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_61.add_sequence(seq0)


# unused_horse_anim_62 Animation
unused_horse_anim_62 = Animation("unused_horse_anim_62")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_62.add_sequence(seq0)


# unused_horse_anim_63 Animation
unused_horse_anim_63 = Animation("unused_horse_anim_63")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_63.add_sequence(seq0)


# unused_horse_anim_64 Animation
unused_horse_anim_64 = Animation("unused_horse_anim_64")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_64.add_sequence(seq0)


# unused_horse_anim_65 Animation
unused_horse_anim_65 = Animation("unused_horse_anim_65")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_65.add_sequence(seq0)


# unused_horse_anim_66 Animation
unused_horse_anim_66 = Animation("unused_horse_anim_66")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_66.add_sequence(seq0)


# unused_horse_anim_67 Animation
unused_horse_anim_67 = Animation("unused_horse_anim_67")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_67.add_sequence(seq0)


# unused_horse_anim_68 Animation
unused_horse_anim_68 = Animation("unused_horse_anim_68")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_68.add_sequence(seq0)


# unused_horse_anim_69 Animation
unused_horse_anim_69 = Animation("unused_horse_anim_69")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_69.add_sequence(seq0)


# unused_horse_anim_70 Animation
unused_horse_anim_70 = Animation("unused_horse_anim_70")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_70.add_sequence(seq0)


# unused_horse_anim_71 Animation
unused_horse_anim_71 = Animation("unused_horse_anim_71")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_71.add_sequence(seq0)


# unused_horse_anim_72 Animation
unused_horse_anim_72 = Animation("unused_horse_anim_72")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_72.add_sequence(seq0)


# unused_horse_anim_73 Animation
unused_horse_anim_73 = Animation("unused_horse_anim_73")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_73.add_sequence(seq0)


# unused_horse_anim_74 Animation
unused_horse_anim_74 = Animation("unused_horse_anim_74")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_74.add_sequence(seq0)


# unused_horse_anim_75 Animation
unused_horse_anim_75 = Animation("unused_horse_anim_75")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_75.add_sequence(seq0)


# unused_horse_anim_76 Animation
unused_horse_anim_76 = Animation("unused_horse_anim_76")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_76.add_sequence(seq0)


# unused_horse_anim_77 Animation
unused_horse_anim_77 = Animation("unused_horse_anim_77")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_77.add_sequence(seq0)


# unused_horse_anim_78 Animation
unused_horse_anim_78 = Animation("unused_horse_anim_78")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_78.add_sequence(seq0)


# unused_horse_anim_79 Animation
unused_horse_anim_79 = Animation("unused_horse_anim_79")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_79.add_sequence(seq0)


# unused_horse_anim_80 Animation
unused_horse_anim_80 = Animation("unused_horse_anim_80")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_80.add_sequence(seq0)


# unused_horse_anim_81 Animation
unused_horse_anim_81 = Animation("unused_horse_anim_81")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_81.add_sequence(seq0)


# unused_horse_anim_82 Animation
unused_horse_anim_82 = Animation("unused_horse_anim_82")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_82.add_sequence(seq0)


# unused_horse_anim_83 Animation
unused_horse_anim_83 = Animation("unused_horse_anim_83")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_83.add_sequence(seq0)


# unused_horse_anim_84 Animation
unused_horse_anim_84 = Animation("unused_horse_anim_84")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_84.add_sequence(seq0)


# unused_horse_anim_85 Animation
unused_horse_anim_85 = Animation("unused_horse_anim_85")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_85.add_sequence(seq0)


# unused_horse_anim_86 Animation
unused_horse_anim_86 = Animation("unused_horse_anim_86")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_86.add_sequence(seq0)


# unused_horse_anim_87 Animation
unused_horse_anim_87 = Animation("unused_horse_anim_87")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_87.add_sequence(seq0)


# unused_horse_anim_88 Animation
unused_horse_anim_88 = Animation("unused_horse_anim_88")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_88.add_sequence(seq0)


# unused_horse_anim_89 Animation
unused_horse_anim_89 = Animation("unused_horse_anim_89")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_89.add_sequence(seq0)


# unused_horse_anim_90 Animation
unused_horse_anim_90 = Animation("unused_horse_anim_90")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_90.add_sequence(seq0)


# unused_horse_anim_91 Animation
unused_horse_anim_91 = Animation("unused_horse_anim_91")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_91.add_sequence(seq0)


# unused_horse_anim_92 Animation
unused_horse_anim_92 = Animation("unused_horse_anim_92")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_92.add_sequence(seq0)


# unused_horse_anim_93 Animation
unused_horse_anim_93 = Animation("unused_horse_anim_93")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_93.add_sequence(seq0)


# unused_horse_anim_94 Animation
unused_horse_anim_94 = Animation("unused_horse_anim_94")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_94.add_sequence(seq0)


# unused_horse_anim_95 Animation
unused_horse_anim_95 = Animation("unused_horse_anim_95")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_95.add_sequence(seq0)


# unused_horse_anim_96 Animation
unused_horse_anim_96 = Animation("unused_horse_anim_96")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_96.add_sequence(seq0)


# unused_horse_anim_97 Animation
unused_horse_anim_97 = Animation("unused_horse_anim_97")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_97.add_sequence(seq0)


# unused_horse_anim_98 Animation
unused_horse_anim_98 = Animation("unused_horse_anim_98")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_98.add_sequence(seq0)


# unused_horse_anim_99 Animation
unused_horse_anim_99 = Animation("unused_horse_anim_99")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_99.add_sequence(seq0)


# unused_horse_anim_100 Animation
unused_horse_anim_100 = Animation("unused_horse_anim_100")
# sequence 0
seq0 = AnimationSequence(1.0, "anim_horse", 0, 1)
unused_horse_anim_100.add_sequence(seq0)



