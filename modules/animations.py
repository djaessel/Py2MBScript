# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from animation import Animation, AnimationFlag, AnimationMasterFlag, AnimationSequence, AnimationSequenceFlag




# stand Animation
stand = Animation("stand")
stand.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(3.0, "anim_human", 50, 52)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.setExtraVals(7, 0.25)
stand.add_sequence(seq0)
# sequence 1
seq1 = AnimationSequence(3.0, "anim_human", 60, 62)
seq1.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq1.add_flag(AnimationSequenceFlag.CYCLIC)
seq1.setExtraVals(7, 0.75)
stand.add_sequence(seq1)
# sequence 2
seq2 = AnimationSequence(3.0, "anim_human", 70, 72)
seq2.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq2.add_flag(AnimationSequenceFlag.CYCLIC)
seq2.setExtraVals(7, 0.25)
stand.add_sequence(seq2)
# sequence 3
seq3 = AnimationSequence(3.0, "anim_human", 80, 82)
seq3.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq3.add_flag(AnimationSequenceFlag.CYCLIC)
seq3.add_flag(AnimationSequenceFlag.TWO_HANDED_BLADE)
seq3.setExtraVals(7, 0.5)
stand.add_sequence(seq3)


# stand_man Animation
stand_man = Animation("stand_man")
stand_man.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(11.0, "stand_man", 0, 315)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.setExtraVals(7, 0.25)
stand_man.add_sequence(seq0)


# stand_player_first_person Animation
stand_player_first_person = Animation("stand_player_first_person")
stand_player_first_person.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(3.5, "anim_human", 90, 100)
seq0.setExtraVals(7, 0.25)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
stand_player_first_person.add_sequence(seq0)
# sequence 1
seq1 = AnimationSequence(3.5, "anim_human", 110, 120)
seq1.setExtraVals(7, 0.25)
seq1.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq1.add_flag(AnimationSequenceFlag.CYCLIC)
stand_player_first_person.add_sequence(seq1)




# jump Animation
jump = Animation("jump")
jump.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
jump.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP)
jump.add_master_flag(AnimationMasterFlag.PLAY)
jump.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
jump.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(1.0, "jump", 22, 46)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
jump.add_sequence(seq0)


# jump_loop Animation
jump_loop = Animation("jump_loop")
jump_loop.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
jump_loop.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP)
jump_loop.add_master_flag(AnimationMasterFlag.PLAY)
jump_loop.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.5, "jump_loop", 0, 14)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
jump_loop.add_sequence(seq0)


# jump_end Animation
jump_end = Animation("jump_end")
jump_end.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
jump_end.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP_END)
jump_end.add_master_flag(AnimationMasterFlag.PLAY)
jump_end.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.3, "jump", 48, 55)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_2)
jump_end.add_sequence(seq0)


# jump_end_hard Animation
jump_end_hard = Animation("jump_end_hard")
jump_end_hard.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
jump_end_hard.add_master_flag(AnimationMasterFlag.PRIORITY_JUMP_END)
jump_end_hard.add_master_flag(AnimationMasterFlag.PLAY)
jump_end_hard.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.6, "jump_end_hard", 36, 54)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
jump_end_hard.add_sequence(seq0)




# stand_unarmed Animation
stand_unarmed = Animation("stand_unarmed")
stand_unarmed.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(8, "noweapon_cstance", 0, 100)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.setExtraVals(7, 0.25)
stand_unarmed.add_sequence(seq0)


# stand_single Animation
stand_single = Animation("stand_single")
stand_single.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(9.0, "sword_loop01", 0, 200)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.setExtraVals(7, 0.25)
stand_single.add_sequence(seq0)


# stand_greatsword Animation
stand_greatsword = Animation("stand_greatsword")
stand_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(6.0, "greatsword_cstance", 0, 91)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.setExtraVals(7, 0.25)
stand_greatsword.add_sequence(seq0)


# stand_staff Animation
stand_staff = Animation("stand_staff")
stand_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "staff_cstance", 0, 60)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
stand_staff.add_sequence(seq0)


# stand_staff Animation
stand_crossbow = Animation("stand_crossbow")
stand_crossbow.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(2.0, "staff_cstance", 0, 60)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
stand_crossbow.add_sequence(seq0)




# turn_right Animation # TODO
turn_right = Animation("turn_right")
turn_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_right.add_master_flag(AnimationMasterFlag.PLAY)
turn_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.95, "stand_man", 0, 30)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
turn_right.add_sequence(seq0)


# turn_left Animation # TODO
turn_left = Animation("turn_left")
turn_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_left.add_master_flag(AnimationMasterFlag.PLAY)
turn_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.95, "stand_man", 0, 30)
seq0.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
turn_left.add_sequence(seq0)


# turn_right_single Animation
turn_right_single = Animation("turn_right_single")
turn_right_single.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_right_single.add_master_flag(AnimationMasterFlag.PLAY)
turn_right_single.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_onehanded", 0, 23)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_right_single.add_sequence(seq0)


# turn_left_single Animation
turn_left_single = Animation("turn_left_single")
turn_left_single.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_left_single.add_master_flag(AnimationMasterFlag.PLAY)
turn_left_single.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_onehanded", 30, 53)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_left_single.add_sequence(seq0)


# turn_right_staff Animation
turn_right_staff = Animation("turn_right_staff")
turn_right_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_right_staff.add_master_flag(AnimationMasterFlag.PLAY)
turn_right_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_staff", 0, 20)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_right_staff.add_sequence(seq0)


# turn_left_staff Animation
turn_left_staff = Animation("turn_left_staff")
turn_left_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_left_staff.add_master_flag(AnimationMasterFlag.PLAY)
turn_left_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_staff", 30, 50)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_left_staff.add_sequence(seq0)


# turn_right_greatsword Animation
turn_right_greatsword = Animation("turn_right_greatsword")
turn_right_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_right_greatsword.add_master_flag(AnimationMasterFlag.PLAY)
turn_right_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_greatsword", 0, 20)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_right_greatsword.add_sequence(seq0)


# turn_left_greatsword Animation
turn_left_greatsword = Animation("turn_left_greatsword")
turn_left_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
turn_left_greatsword.add_master_flag(AnimationMasterFlag.PLAY)
turn_left_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.95, "turn_man_greatsword", 30, 50)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
turn_left_greatsword.add_sequence(seq0)




# prepare_kick_0 Animation
prepare_kick_0 = Animation("prepare_kick_0")
prepare_kick_0.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
prepare_kick_0.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
prepare_kick_0.add_master_flag(AnimationMasterFlag.PLAY)
prepare_kick_0.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
prepare_kick_0.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.05, "kick_rightleg", 10, 12)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
prepare_kick_0.add_sequence(seq0)


# prepare_kick_1 Animation
prepare_kick_1 = Animation("prepare_kick_1")
prepare_kick_1.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
prepare_kick_1.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
prepare_kick_1.add_master_flag(AnimationMasterFlag.PLAY)
prepare_kick_1.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
prepare_kick_1.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.05, "kick_rightleg", 12, 12)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
prepare_kick_1.add_sequence(seq0)


# prepare_kick_2 Animation
prepare_kick_2 = Animation("prepare_kick_2")
prepare_kick_2.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
prepare_kick_2.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
prepare_kick_2.add_master_flag(AnimationMasterFlag.PLAY)
prepare_kick_2.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
prepare_kick_2.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.05, "kick_rightleg", 12, 12)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
prepare_kick_2.add_sequence(seq0)


# prepare_kick_3 Animation
prepare_kick_3 = Animation("prepare_kick_3")
prepare_kick_3.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
prepare_kick_3.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
prepare_kick_3.add_master_flag(AnimationMasterFlag.PLAY)
prepare_kick_3.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
prepare_kick_3.add_master_flag(AnimationMasterFlag.CONTINUE_TO_NEXT)
# sequence 0
seq0 = AnimationSequence(0.05, "kick_rightleg", 12, 12)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_3)
prepare_kick_3.add_sequence(seq0)


# kick_right_leg Animation
kick_right_leg = Animation("kick_right_leg")
kick_right_leg.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
kick_right_leg.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
kick_right_leg.add_master_flag(AnimationMasterFlag.PLAY)
kick_right_leg.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "kick_rightleg", 12, 33)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
kick_right_leg.add_sequence(seq0)


# kick_left_leg Animation
kick_left_leg = Animation("kick_left_leg")
kick_left_leg.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
kick_left_leg.add_master_flag(AnimationMasterFlag.PRIORITY_KICK)
kick_left_leg.add_master_flag(AnimationMasterFlag.PLAY)
kick_left_leg.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_right_onehanded.add_sequence(seq0)




