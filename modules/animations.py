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




# STAND ANIMATIONS 1

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




# JUMP ANIMATIONS

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




# STAND ANIMATIONS 2

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




# TURN LEFT, TURN RIGHT ANIMATIONS

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




# KICK ANIMATIONS

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




# RUN FORWARD ANIMATIONS

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


# run_forward_right_staff Animation
run_forward_right_staff = Animation("run_forward_right_staff")
run_forward_right_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_forward_right_staff.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_forward_right_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_forward_right_stuff", 0, 24)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_forward_left_hips_left.add_sequence(seq0)




# RUN BACKWARDS ANIMATIONS

# run_backward Animation
run_backward = Animation("run_backward")
run_backward.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward", 0, 21)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_staff.add_sequence(seq0)


# run_backward_greatsword Animation
run_backward_greatsword = Animation("run_backward_staff")
run_backward_greatsword.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_greatsword.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_twohanded", 0, 21)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_right_staff.add_sequence(seq0)


# run_backward_right_staff Animation
run_backward_right_staff = Animation("run_backward_right_staff")
run_backward_right_staff.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_backward_right_staff.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_backward_right_staff.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.7, "run_backward_staff_right", 0, 21)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
seq0.setExtraVals(7, 0.4)
run_backward_left_hips_left.add_sequence(seq0)




# RUN RIGHT ANIMATIONS

# run_right Animation
run_right = Animation("run_right")
run_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_right", 0, 24)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_right_polearm.add_sequence(seq0)


# run_right_hips_right Animation
run_right_hips_right = Animation("run_right_hips_right")
run_right_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_right_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_right_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_right_stuff", 0, 24) # TODO: Check if correct!
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_right_hips_left.add_sequence(seq0)




# RUN LEFT ANIMATIONS

# run_left Animation
run_left = Animation("run_left")
run_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_left", 0, 24)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_left_hips_right.add_sequence(seq0)


# run_left_hips_left Animation
run_left_hips_left = Animation("run_left_hips_left")
run_left_hips_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
run_left_hips_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
run_left_hips_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(0.8, "run_man_left_stuff", 0, 24) # TODO: Check correct!
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
run_left_hips_left.add_sequence(seq0)




# WALK FORWARD ANIMATIONS

# walk_forward Animation
walk_forward = Animation("walk_forward")
walk_forward.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "man_walk", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_hips_left.add_sequence(seq0)




# WALK BACKWARD ANIMATIONS

# walk_backward Animation
walk_backward = Animation("walk_backward")
walk_backward.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_backward", 0, 30)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_hips_left.add_sequence(seq0)




# WALK RIGHT ANIMATIONS

# walk_right Animation
walk_right = Animation("walk_right")
walk_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_right_normal", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_right_polearm.add_sequence(seq0)


# walk_right_hips_right Animation
walk_right_hips_right = Animation("walk_right_hips_right")
walk_right_hips_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_right_hips_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_right_hips_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_right_staff_r", 0, 32) # TODO: check correct?
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_right_hips_left.add_sequence(seq0)




# WALK LEFT ANIMATIONS

# walk_left Animation
walk_left = Animation("walk_left")
walk_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_left_normal", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_left_hips_left.add_sequence(seq0)




# WALK FORWARD RIGHT ANIMATIONS

# walk_forward_right Animation
walk_forward_right = Animation("walk_forward_right")
walk_forward_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_normal", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_right_hips_left.add_sequence(seq0)




# WALK FORWARD LEFT ANIMATIONS

# walk_forward_left Animation
walk_forward_left = Animation("walk_forward_left")
walk_forward_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_forward_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_forward_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_normal", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_forward_left_hips_left.add_sequence(seq0)




# WALK BACKWARDS LEFT ANIMATIONS

# walk_backward_left Animation
walk_backward_left = Animation("walk_backward_left")
walk_backward_left.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_left.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_left.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_normal", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_left.add_sequence(seq0)


# walk_backward_left_onehanded Animation
walk_backward_left_onehanded = Animation("walk_backward_left_onehanded")
walk_backward_left_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_left_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_left_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_onehanded", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_left_onehanded.add_sequence(seq0)


# walk_backward_left_twohanded Animation
walk_backward_left_twohanded = Animation("walk_backward_left_twohanded")
walk_backward_left_twohanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_left_twohanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_left_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_greatsword", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_left_twohanded.add_sequence(seq0)


# walk_backward_left_polearm Animation
walk_backward_left_polearm = Animation("walk_backward_left_polearm")
walk_backward_left_polearm.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_left_polearm.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_left_polearm.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossright_staff", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_left_hips_left.add_sequence(seq0)




# WALK BACKWARD RIGHT ANIMATIONS

# walk_backward_right Animation
walk_backward_right = Animation("walk_backward_right")
walk_backward_right.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_right.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_right.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_normal", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_right.add_sequence(seq0)


# walk_backward_right_onehanded Animation
walk_backward_right_onehanded = Animation("walk_backward_right_onehanded")
walk_backward_right_onehanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_right_onehanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_right_onehanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_onehanded", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_right_onehanded.add_sequence(seq0)


# walk_backward_right_twohanded Animation
walk_backward_right_twohanded = Animation("walk_backward_right_twohanded")
walk_backward_right_twohanded.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_right_twohanded.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_right_twohanded.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_greatsword", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_right_twohanded.add_sequence(seq0)


# walk_backward_right_polearm Animation
walk_backward_right_polearm = Animation("walk_backward_right_polearm")
walk_backward_right_polearm.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
walk_backward_right_polearm.add_master_flag(AnimationMasterFlag.USE_CYCLE_PERIOD)
walk_backward_right_polearm.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# sequence 0
seq0 = AnimationSequence(1.0, "walk_crossleft_staff", 0, 32)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
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
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
seq0.add_flag(AnimationSequenceFlag.CYCLIC)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_WALK)
seq0.add_flag(AnimationSequenceFlag.MAKE_WALK_SOUND)
seq0.setExtraVals(0, 0.4)
seq0.setExtraVals(1, 0.9)
walk_backward_right_hips_left.add_sequence(seq0)




# CROUCH ANIMATIONS

# walk_forward_crouch Animation
walk_forward_crouch = Animation("walk_forward_crouch")
walk_forward_crouch.add_flag(AnimationFlag.ENFORCE_LOWERBODY)
# sequence 0
seq0 = AnimationSequence(1.7, "low_walk", 0, 48)
seq0.add_flag(AnimationSequenceFlag.USE_INV_WALK_PROGRESS)
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




# RIDE ANIMATIONS

'''
["ride_0", acf_enforce_lowerbody, amf_client_prediction,
  [15.0, "stand_onhorse", 0, 456, arf_cyclic],
 ],
["ride_1", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
  [1.0, "anim_human_02", 0, 31, arf_cyclic],
],
["lancer_ride_1", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction|amf_priority_ride|amf_play,
  [1.0, "lancer_ride1", 0, 31, arf_cyclic],
],
["lancer_charge_parried",acf_enforce_lowerbody, amf_priority_parried|amf_use_weapon_speed|amf_play,
  [1.0, "anim_human", horse_move+210, horse_move+220, arf_blend_in_32],
],
["ride_2", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
  [0.8, "anim_human_02", 50, 69, arf_cyclic],
],
["ride_3", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
  [0.6, "anim_human_02", 100, 116, arf_cyclic],
],
["ride_4", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
  [0.5, "anim_human_02", 150, 165, arf_cyclic|arf_blend_in_32],
],
["lancer_ride_4",  acf_enforce_lowerbody | acf_synch_with_horse | acf_rot_vertical_sword|acf_anim_length(30), amf_rider_rot_couched_lance|amf_client_prediction|amf_priority_ride|amf_play,
  [0.5, "lancer_ride4", 0, 15, arf_cyclic | arf_blend_in_128],
],
["lancer_ride_4_no_shield",  acf_enforce_lowerbody | acf_synch_with_horse | acf_rot_vertical_sword|acf_anim_length(30), amf_rider_rot_couched_lance|amf_client_prediction|amf_priority_ride|amf_play,
  [0.5, "lancer_ride4_no_shield", 0, 15, arf_cyclic | arf_blend_in_128],
],
["ride_rear", acf_enforce_lowerbody|acf_ignore_slope, amf_priority_mount|amf_play|amf_client_prediction,
  [1.7, "anim_human_02", 265, 297,  arf_blend_in_8],
],
["ride_spur", acf_enforce_lowerbody, amf_play|amf_priority_jump,
  [0.3, "anim_human", horse_move+860, horse_move+865,  arf_blend_in_8],
],
["ride_jump", acf_enforce_lowerbody, amf_client_prediction,
  [1.6, "anim_human_02", 205, 222,  arf_blend_in_4],#|arf_end_pos_0_25],
],
["ride_jump_end", acf_enforce_all, amf_client_prediction,
  [0.1, "anim_human_02", 222, 224,  arf_blend_in_16],
],
["ride_turn_right", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
  [1.0, "anim_human_02", 500, 533, arf_cyclic],
],
["ride_turn_left", acf_enforce_lowerbody | acf_synch_with_horse, amf_client_prediction,
  [1.0, "anim_human_02", 450, 483, arf_cyclic],
],

["mount_horse", acf_enforce_all, amf_priority_mount|amf_play|amf_client_prediction,
  [1.3, "anim_human", horse_move+1003, horse_move+1045,  arf_blend_in_1, 0, (0.0,0,0.0)],
],
["dismount_horse", acf_enforce_lowerbody|acf_displace_position, amf_priority_mount|amf_play|amf_accurate_body|amf_client_prediction,
  [1.1, "anim_human", horse_move+1103, horse_move+1145,  arf_blend_in_1, 0, (-0.5,0,0)],
],
["lancer_ride_0", acf_enforce_lowerbody, amf_priority_ride|amf_play|amf_client_prediction,
  [43.0, "stand_onhorse_staff", 0, 1300, arf_lancer|arf_cyclic],
],
''' and None




# EQUIP ANIMATIONS / UNEQUIP ANIMATIONS

# equip_default Animation
equip_default = Animation("equip_default")
equip_default.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_default.add_master_flag(AnimationMasterFlag.PLAY)
equip_default.add_master_flag(AnimationMasterFlag.RESTART)
equip_default.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# seq0
seq0 = AnimationSequence(0.6, "equip_arms", 206, 221)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_default.add_sequence(seq0)


# unequip_default Animation
unequip_default = Animation("unequip_default")
unequip_default.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_default.add_master_flag(AnimationMasterFlag.PLAY)
unequip_default.add_master_flag(AnimationMasterFlag.RESTART)
unequip_default.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# seq0
seq0 = AnimationSequence(0.3, "equip_arms", 207, 200)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_default.add_sequence(seq0)


# equip_sword Animation
equip_sword = Animation("equip_sword")
equip_sword.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_sword.add_master_flag(AnimationMasterFlag.PLAY)
equip_sword.add_master_flag(AnimationMasterFlag.RESTART)
equip_sword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# seq0
seq0 = AnimationSequence(0.8, "equip_sword", 0, 27)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_sword.add_sequence(seq0)


# unequip_sword Animation
unequip_sword = Animation("unequip_sword")
unequip_sword.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_sword.add_master_flag(AnimationMasterFlag.PLAY)
unequip_sword.add_master_flag(AnimationMasterFlag.RESTART)
unequip_sword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# seq0
seq0 = AnimationSequence(0.3, "equip_sword", 6, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_sword.add_sequence(seq0)


# equip_greatsword Animation
equip_greatsword = Animation("equip_greatsword")
equip_greatsword.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
equip_greatsword.add_master_flag(AnimationMasterFlag.PLAY)
equip_greatsword.add_master_flag(AnimationMasterFlag.RESTART)
equip_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# seq0
seq0 = AnimationSequence(1.2, "draw_greatsword", 0, 35)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
equip_greatsword.add_sequence(seq0)


# unequip_greatsword Animation
unequip_greatsword = Animation("unequip_greatsword")
unequip_greatsword.add_master_flag(AnimationMasterFlag.PRIORITY_EQUIP)
unequip_greatsword.add_master_flag(AnimationMasterFlag.PLAY)
unequip_greatsword.add_master_flag(AnimationMasterFlag.RESTART)
unequip_greatsword.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)
# seq0
seq0 = AnimationSequence(0.3, "draw_greatsword", 10, 0)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_0)
unequip_greatsword.add_sequence(seq0)


'''
["equip_axe_left_hip", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.8, "draw_axe", 0, 16, arf_blend_in_0],
],
["unequip_axe_left_hip", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "draw_axe", 6, 0, arf_blend_in_0],
],
["equip_crossbow", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [1.2, "equip_greataxe", 0, 20, arf_blend_in_0],
],
["unequip_crossbow", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "equip_greataxe", 10, 0, arf_blend_in_0],
],
["equip_spear", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.8, "equip_arms", 17, 34, arf_blend_in_0],
],
["unequip_spear", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "equip_arms", 15, 10, arf_blend_in_0],
],
["equip_dagger_front_left", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.8, "equip_arms", 253, 276, arf_blend_in_0],
],
["unequip_dagger_front_left", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.2, "equip_arms", 254, 250, arf_blend_in_0],
],
["equip_dagger_front_right", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.8, "equip_arms", 305, 333, arf_blend_in_0],
],
["unequip_dagger_front_right", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.4, "equip_arms", 306, 300, arf_blend_in_0],
],
["equip_axe_back", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [1.0, "equip_greataxe", 0, 17, arf_blend_in_0],
],
["unequip_axe_back", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "equip_greataxe", 7, 0, arf_blend_in_0],
],
["equip_revolver_right", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.6, "equip_arms", 352, 365, arf_blend_in_0],
],
["unequip_revolver_right", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "equip_arms", 354, 350, arf_blend_in_0],
],
["equip_pistol_front_left", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.8, "equip_arms", 253, 276, arf_blend_in_0],
],
["unequip_pistol_front_left", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.2, "equip_arms", 254, 250, arf_blend_in_0],
],
["equip_katana", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.8, "anim_human", combat+30, combat+45, arf_blend_in_0],
],
["unequip_katana", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
],
["equip_wakizashi", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.8, "anim_human", combat+30, combat+45, arf_blend_in_0],
],
["unequip_wakizashi", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "anim_human", combat+10, combat+0, arf_blend_in_0],
],
["equip_shield", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.8, "equip_arms", 68, 84, arf_blend_in_0],
],
["unequip_shield", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.4, "equip_arms", 62, 50, arf_blend_in_0],
],
["equip_bow_back", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.7, "equip_arms", 161, 179, arf_blend_in_0],
],
["unequip_bow_back", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "equip_arms", 163, 150, arf_blend_in_0],
],
["equip_bow_left_hip", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.7, "equip_arms", 110, 148, arf_blend_in_0],
],
["unequip_bow_left_hip", 0, amf_priority_equip|amf_play|amf_restart|amf_client_prediction,
  [0.3, "equip_arms", 115, 108, arf_blend_in_0],
],
''' and None




# CANCEL ATTACK ANIMATIONS

'''
["cancel_attack_onehanded", 0, amf_priority_cancel|amf_use_weapon_speed|amf_use_inertia|amf_play|amf_rider_rot_thrust,
  [cancel_duration, "sword_loop01", 10, 11, arf_blend_in_8],
],
["cancel_attack_twohanded", 0, amf_priority_cancel|amf_use_weapon_speed|amf_use_inertia|amf_play|amf_rider_rot_thrust,
  [cancel_duration, "greatsword_cstance", 10, 11, arf_blend_in_8],
],
["cancel_attack_polearm", 0, amf_priority_cancel|amf_use_weapon_speed|amf_use_inertia|amf_play|amf_rider_rot_thrust,
  [cancel_duration, "staff_cstance", 10, 11, arf_blend_in_8],
],
''' and None




#TODO: ready bow, release javelin and reload crossbow should have the same time
# duration and controlled via weapon speed.

# BOW ANIMATIONS

'''
 ["ready_bow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_bow,
   [1.5, "anim_human", combat+500, combat+530, blend_in_ready|arf_make_custom_sound, pack2f(0.14, 0.44)],
 ],
 ["release_bow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_bow,
   [0.3, "anim_human", combat+530, combat+532, arf_blend_in_2],
 ],
 #not used
 ["ready_bow_mounted", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_bow,
   [1.5, "anim_human", combat+800, combat+830, blend_in_ready|arf_make_custom_sound, pack2f(0.10, 0.40)],
 ],
 #not used
 ["release_bow_mounted", acf_rot_vertical_bow|acf_anim_length(100), amf_rider_rot_bow,
   [0.3, "anim_human", combat+830, combat+832, arf_blend_in_2],
 ],
''' and None




# CROSSBOW ANIMATIONS

'''
 ["ready_crossbow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_crossbow,
   [1.5, "anim_human", combat+1300, combat+1320, blend_in_ready],
 ],
 ["release_crossbow", acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_crossbow,
   [0.2, "anim_human", combat+1330, combat+1331, arf_blend_in_1],
 ],
 ["reload_crossbow", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
   [1.0, "anim_human", combat+1700, combat+1750, arf_blend_in_8|arf_make_custom_sound, pack2f(0.40, 0.94)],
 ],
 ["reload_crossbow_horseback", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
   [1.6, "anim_human", combat+1800, combat+1877, arf_blend_in_8|arf_make_custom_sound, pack2f(0.27, 0.94)],
 ],
''' and None




# JAVELIN ANIMATIONS

'''
 ["ready_javelin", acf_rot_vertical_bow, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.6, "throw_javelin2", 0, 30, blend_in_ready],
 ],
 ["release_javelin", acf_rot_vertical_bow, amf_priority_throw|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.9, "throw_javelin2", 55, 100, arf_blend_in_0],
 ],
''' and None




# THROWING KNIFE ANIMATIONS

'''
 ["ready_throwing_knife", acf_rot_vertical_bow, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.6, "throw_knife", 10, 30, blend_in_ready],
 ],
 ["release_throwing_knife", acf_rot_vertical_bow, amf_priority_throw|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.9, "throw_knife", 30, 70, arf_blend_in_0],
 ],
''' and None




# THROWING AXE ANIMATIONS

'''
 ["ready_throwing_axe", acf_rot_vertical_bow, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.6, "throwing_axe", 7, 23, blend_in_ready],
 ],
 ["release_throwing_axe", acf_rot_vertical_bow, amf_priority_throw|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.9, "throwing_axe", 23, 60, arf_blend_in_0],
 ],
''' and None




# STONE ANIMATIONS

'''
 ["ready_stone", acf_rot_vertical_bow, amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.6, "throwing_stone", 0, 20, blend_in_ready],
 ],
 ["release_stone", acf_rot_vertical_bow, amf_priority_throw|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_throw,
   [0.9, "throwing_stone", 20, 65, arf_blend_in_0],
 ],
''' and None





# PISTOL ANIMATIONS

'''
["ready_pistol", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_keep|amf_client_owner_prediction|amf_rider_rot_pistol,
  [0.3, "anim_human", combat+2500, combat+2515, arf_blend_in_8],
],
["release_pistol", acf_rot_vertical_sword|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_client_owner_prediction|amf_rider_rot_pistol,
  [0.3, "anim_human", combat+2520, combat+2527, arf_blend_in_1],
],
["reload_pistol", 0, amf_priority_reload|amf_use_weapon_speed|amf_play,
  [2.0, "anim_human", combat+2650, combat+2860, arf_blend_in_8],
],
''' and None




# MUSKET ANIMATIONS

# ready_musket Animation
ready_musket = Animation("ready_musket", 100)
ready_musket.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
ready_musket.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_musket.add_master_flag(AnimationMasterFlag.KEEP)
ready_musket.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_musket.add_master_flag(AnimationMasterFlag.RIDER_ROT_CROSSBOW)
# seq0
seq0 = AnimationSequence(1.5, "anim_human", __combat__ + 1300, __combat__ + 1320)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_READY)
ready_musket.add_sequence(seq0)


# release_musket Animation
release_musket = Animation("release_musket", 100)
release_musket.add_flag(AnimationFlag.ROT_VERTICAL_BOW)
release_musket.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_musket.add_master_flag(AnimationMasterFlag.KEEP)
release_musket.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
release_musket.add_master_flag(AnimationMasterFlag.RIDER_ROT_CROSSBOW)
# seq0
seq0 = AnimationSequence(0.2, "anim_human", __combat__ + 1330, __combat__ + 1331)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_1)
release_musket.add_sequence(seq0)


# reload_musket Animation
reload_musket = Animation("reload_musket")
reload_musket.add_master_flag(AnimationMasterFlag.PRIORITY_RELOAD)
reload_musket.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
reload_musket.add_master_flag(AnimationMasterFlag.PLAY)
# seq0
seq0 = AnimationSequence(2.0, "anim_human", __combat__ + 2650, __combat__ + 2860)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_8)
reload_musket.add_sequence(seq0)




# SWING RIGHT FIST ANIMATIONS

# ready_swingright_fist Animation
ready_swingright_fist = Animation("ready_swingright_fist")
ready_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_swingright_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_swingright_fist.add_master_flag(AnimationMasterFlag.KEEP)
ready_swingright_fist.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_swingright_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
# seq0
seq0 = AnimationSequence(__ready_durn__, "right_swing", 0, 15)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_READY)
ready_swingright_fist.add_sequence(seq0)


# release_swingright_fist Animation
release_swingright_fist = Animation("release_swingright_fist")
release_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_swingright_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_swingright_fist.add_master_flag(AnimationMasterFlag.PLAY)
release_swingright_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
# seq0
seq0 = AnimationSequence(0.5, "right_swing", 15, 41)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_RELEASE)
release_swingright_fist.add_sequence(seq0)


# release_swingright_fist_continue Animation
release_swingright_fist_continue = Animation("release_swingright_fist_continue")
release_swingright_fist_continue.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_swingright_fist_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_swingright_fist_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_swingright_fist_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
# seq0
seq0 = AnimationSequence(0.5, "right_swing", 15, 41)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_RELEASE)
release_swingright_fist_continue.add_sequence(seq0)


# blocked_swingright_fist Animation
blocked_swingright_fist = Animation("blocked_swingright_fist")
blocked_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_swingright_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_swingright_fist.add_master_flag(AnimationMasterFlag.PLAY)
blocked_swingright_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
# seq0
seq0 = AnimationSequence(__attack_blocked_duration__, "anim_human", __combat__ + 4013, __combat__ + 4008)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_PARRY)
blocked_swingright_fist.add_sequence(seq0)


# parried_swingright_fist Animation
parried_swingright_fist = Animation("parried_swingright_fist")
parried_swingright_fist.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_swingright_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_swingright_fist.add_master_flag(AnimationMasterFlag.PLAY)
parried_swingright_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_RIGHT)
# seq0
seq0 = AnimationSequence(__attack_parried_duration__, "anim_human", __combat__ + 4013, __combat__ + 4008)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_PARRY)
parried_swingright_fist.add_sequence(seq0)




# SWING LEFT FIST ANIMATIONS

# ready_swingleft_fist Animation
ready_swingleft_fist = Animation("ready_swingleft_fist")
ready_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_swingleft_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_swingleft_fist.add_master_flag(AnimationMasterFlag.KEEP)
ready_swingleft_fist.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_swingleft_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
# seq0
seq0 = AnimationSequence(__ready_durn__, "anim_human", __combat__ + 4300, __combat__ + 4300)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_READY)
ready_swingleft_fist.add_sequence(seq0)


# release_swingleft_fist Animation
release_swingleft_fist = Animation("release_swingleft_fist")
release_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_swingleft_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_swingleft_fist.add_master_flag(AnimationMasterFlag.PLAY)
release_swingleft_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
# seq0
seq0 = AnimationSequence(0.5, "anim_human", __combat__ + 4300, __combat__ + 4335)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_RELEASE)
release_swingleft_fist.add_sequence(seq0)


# release_swingleft_fist_continue Animation
release_swingleft_fist_continue = Animation("release_swingleft_fist_continue")
release_swingleft_fist_continue.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_swingleft_fist_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_swingleft_fist_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_swingleft_fist_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
# seq0
seq0 = AnimationSequence(0.5, "anim_human", __combat__ + 4300, __combat__ + 4335)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_RELEASE)
release_swingleft_fist_continue.add_sequence(seq0)


# blocked_swingleft_fist Animation
blocked_swingleft_fist = Animation("blocked_swingleft_fist")
blocked_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_swingleft_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_swingleft_fist.add_master_flag(AnimationMasterFlag.PLAY)
blocked_swingleft_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
# seq0
seq0 = AnimationSequence(__attack_blocked_duration__, "anim_human", __combat__ + 4313, __combat__ + 4308)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_PARRY)
blocked_swingleft_fist.add_sequence(seq0)


# parried_swingleft_fist Animation
parried_swingleft_fist = Animation("parried_swingleft_fist")
parried_swingleft_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
parried_swingleft_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_swingleft_fist.add_master_flag(AnimationMasterFlag.PLAY)
parried_swingleft_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_SWING_LEFT)
# seq0
seq0 = AnimationSequence(__attack_parried_duration__, "anim_human", __combat__ + 4313, __combat__ + 4308)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_PARRY)
parried_swingleft_fist.add_sequence(seq0)




# DIRECT FIST ANIMATIONS

# ready_direct_fist Animation
ready_direct_fist = Animation("ready_direct_fist")
ready_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_direct_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_direct_fist.add_master_flag(AnimationMasterFlag.KEEP)
ready_direct_fist.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_direct_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
# seq0
seq0 = AnimationSequence(__ready_durn__, "direct_fist", 0, 16)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_READY)
ready_direct_fist.add_sequence(seq0)


# release_direct_fist Animation
release_direct_fist = Animation("release_direct_fist")
release_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_direct_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_direct_fist.add_master_flag(AnimationMasterFlag.PLAY)
release_direct_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
# seq0
seq0 = AnimationSequence(0.5, "direct_fist", 17, 36)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_RELEASE)
release_direct_fist.add_sequence(seq0)


# release_direct_fist_continue Animation
release_direct_fist_continue = Animation("release_direct_fist_continue")
release_direct_fist_continue.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_direct_fist_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_direct_fist_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_direct_fist_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
# seq0
seq0 = AnimationSequence(0.5, "direct_fist", 17, 36)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_RELEASE)
release_direct_fist_continue.add_sequence(seq0)


# blocked_direct_fist Animation
blocked_direct_fist = Animation("blocked_direct_fist")
blocked_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_direct_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_direct_fist.add_master_flag(AnimationMasterFlag.PLAY)
blocked_direct_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
# seq0
seq0 = AnimationSequence(__attack_blocked_duration__, "anim_human", __combat__ + 4613, __combat__ + 4608)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_PARRY)
blocked_direct_fist.add_sequence(seq0)


# parried_direct_fist Animation
parried_direct_fist = Animation("parried_direct_fist")
parried_direct_fist.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_direct_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_direct_fist.add_master_flag(AnimationMasterFlag.PLAY)
parried_direct_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
# seq0
seq0 = AnimationSequence(__attack_parried_duration__, "anim_human", __combat__ + 4613, __combat__ + 4608)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_PARRY)
parried_direct_fist.add_sequence(seq0)




# UPPERCUT FIST ANIMATIONS

# ready_uppercut_fist Animation
ready_uppercut_fist = Animation("ready_uppercut_fist")
ready_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
ready_uppercut_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
ready_uppercut_fist.add_master_flag(AnimationMasterFlag.KEEP)
ready_uppercut_fist.add_master_flag(AnimationMasterFlag.CLIENT_OWNER_PREDICTION)
ready_uppercut_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
# seq0
seq0 = AnimationSequence(__ready_durn__, "uppercut", 0, 17)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_READY)
ready_uppercut_fist.add_sequence(seq0)


# release_uppercut_fist Animation
release_uppercut_fist = Animation("release_uppercut_fist")
release_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_uppercut_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_uppercut_fist.add_master_flag(AnimationMasterFlag.PLAY)
release_uppercut_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
# seq0
seq0 = AnimationSequence(0.5, "uppercut", 17, 34)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_RELEASE)
release_uppercut_fist.add_sequence(seq0)


# release_uppercut_fist_continue Animation
release_uppercut_fist_continue = Animation("release_uppercut_fist_continue")
release_uppercut_fist_continue.add_master_flag(AnimationMasterFlag.PRIORITY_ATTACK)
release_uppercut_fist_continue.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
release_uppercut_fist_continue.add_master_flag(AnimationMasterFlag.PLAY)
release_uppercut_fist_continue.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
# seq0
seq0 = AnimationSequence(0.5, "uppercut", 17, 34)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_RELEASE)
release_uppercut_fist_continue.add_sequence(seq0)


# blocked_uppercut_fist Animation
blocked_uppercut_fist = Animation("blocked_uppercut_fist")
blocked_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_BLOCKED)
blocked_uppercut_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
blocked_uppercut_fist.add_master_flag(AnimationMasterFlag.PLAY)
blocked_uppercut_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
# seq0
seq0 = AnimationSequence(__attack_blocked_duration__, "anim_human", __combat__ + 4913, __combat__ + 4908)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_PARRY)
blocked_uppercut_fist.add_sequence(seq0)


# parried_uppercut_fist Animation
parried_uppercut_fist = Animation("parried_uppercut_fist")
parried_uppercut_fist.add_master_flag(AnimationMasterFlag.PRIORITY_PARRIED)
parried_uppercut_fist.add_master_flag(AnimationMasterFlag.USE_WEAPON_SPEED)
parried_uppercut_fist.add_master_flag(AnimationMasterFlag.PLAY)
parried_uppercut_fist.add_master_flag(AnimationMasterFlag.RIDER_ROT_THRUST)
# seq0
seq0 = AnimationSequence(__attack_parried_duration__, "anim_human", __combat__ + 4913, __combat__ + 4908)
seq0.add_flag(AnimationSequenceFlag.BLEND_IN_PARRY)
parried_uppercut_fist.add_sequence(seq0)




# SLASH RIGHT TWOHANDED ANIMATIONS

'''
["ready_slashright_twohanded", acf_right_cut|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
  [ready_durn, "slashright_twohanded", 10, 18, blend_in_ready],
],
["release_slashright_twohanded", acf_right_cut|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
  [0.61, "slashright_twohanded", 18, 38, blend_in_release],
],
["release_slashright_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
  [0.5, "slashright_twohanded", 38, 61, blend_in_continue],
],
["blocked_slashright_twohanded",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play,
  [attack_blocked_duration, "anim_human", combat+5725, combat+5720, blend_in_parry],
],
["parried_slashright_twohanded",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play,
  [attack_parried_duration, "anim_human", combat+5725, combat+5720, blend_in_parry],
],
''' and None




# SLASH LEFT TWOHANDED ANIMATIONS

'''
["ready_slashleft_twohanded", acf_right_cut|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
  [ready_durn, "slashleft_twohanded", 12, 16, blend_in_ready],
],
["release_slashleft_twohanded", acf_right_cut|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
  [0.61, "slashleft_twohanded", 16, 38, blend_in_release],
],
["release_slashleft_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
  [0.5, "slashleft_twohanded", 38, 52, blend_in_continue],
],
["blocked_slashleft_twohanded",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_blocked|amf_use_weapon_speed|amf_play,
  [attack_blocked_duration, "anim_human", combat+6425, combat+6420, blend_in_parry],
],
["parried_slashleft_twohanded",acf_rot_vertical_bow|acf_anim_length(100), amf_priority_parried|amf_use_weapon_speed|amf_play,
  [attack_parried_duration, "anim_human", combat+6425, combat+6420, blend_in_parry],
],
''' and None




# THRUST TWOHANDED ANIMATIONS

'''
["ready_thrust_twohanded", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
  [ready_durn, "anim_human", combat+6000, combat+6010, blend_in_ready],
],
["release_thrust_twohanded", acf_thrust|acf_rot_vertical_bow|acf_anim_length(100), amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
  [0.61, "anim_human", combat+6010, combat+6031, blend_in_release],
],
["release_thrust_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
  [0.1, "anim_human", combat+6031, combat+6040, blend_in_continue],
],
["blocked_thrust_twohanded", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play,
  [attack_blocked_duration_thrust, "anim_human", combat+6015, combat+6016, blend_in_parry],
],
["parried_thrust_twohanded", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
  [attack_parried_duration_thrust, "anim_human", combat+6015, combat+6016, blend_in_parry],
],
''' and None




# OVERSWING TWOHANDED ANIMATIONS

'''
["ready_overswing_twohanded", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction,
  [ready_durn, "attacks_twohanded_overswing", 11, 26, blend_in_ready],
],
["release_overswing_twohanded", acf_overswing, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_continue_to_next,
  [0.61, "attacks_twohanded_overswing", 26, 55, blend_in_release],
],
["release_overswing_twohanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_client_owner_prediction,
  [0.5, "attacks_twohanded_overswing", 55, 66, blend_in_continue],
],
["blocked_overswing_twohanded", 0, amf_priority_blocked|amf_use_weapon_speed|amf_play,
  [attack_blocked_duration, "anim_human", combat+6215, combat+6212, blend_in_parry],
],
["parried_overswing_twohanded", 0, amf_priority_parried|amf_use_weapon_speed|amf_play,
  [attack_parried_duration, "anim_human", combat+6215, combat+6212, blend_in_parry],
],
''' and None




# THRUST ONEHANDED ANIMATIONS

'''
["ready_thrust_onehanded",   acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction|amf_rider_rot_thrust,
  [ready_durn, "attacks_thrust_onehanded", 5, 13, blend_in_ready],
],
["release_thrust_onehanded", acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_continue_to_next,
  [0.62, "attacks_thrust_onehanded", 12, 32, blend_in_release],
],
["release_thrust_onehanded_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_client_owner_prediction,
  [0.3, "attacks_thrust_onehanded", 32, 54, blend_in_continue],
],
["blocked_thrust_onehanded", acf_enforce_rightside, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [attack_blocked_duration_thrust, "anim_human", combat+8515, combat+8513, blend_in_parry],
],
["parried_thrust_onehanded", acf_enforce_rightside, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [attack_parried_duration_thrust, "anim_human", combat+8515, combat+8513, blend_in_parry],
],
''' and None




# THRUST ONEHANDED HORSEBACK ANIMATIONS

'''
 ["ready_thrust_onehanded_horseback",   acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction|amf_rider_rot_thrust,
  [ready_durn, "attacks_thrust_onehanded", 5, 13, blend_in_ready],
],
["release_thrust_onehanded_horseback", acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_continue_to_next,
  [0.62, "attacks_thrust_onehanded", 12, 32, blend_in_release],
],
["release_thrust_onehanded_horseback_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_client_owner_prediction,
  [0.3, "attacks_thrust_onehanded", 32, 54, blend_in_continue],
],
["blocked_thrust_onehanded_horseback", acf_enforce_rightside, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [attack_blocked_duration_thrust, "anim_human", combat+8515, combat+8513, blend_in_parry],
],
["parried_thrust_onehanded_horseback", acf_enforce_rightside, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [attack_parried_duration_thrust, "anim_human", combat+8515, combat+8513, blend_in_parry],
],
''' and None




# THRUST ONEHANDED LANCE ANIMATIONS

'''
["ready_thrust_onehanded_lance",   acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_use_inertia|amf_keep|amf_client_owner_prediction|amf_rider_rot_thrust,
  [ready_durn, "thrust_onehanded_lance_hb", 5, 8, blend_in_ready],
],
["release_thrust_onehanded_lance", acf_thrust|acf_rot_vertical_sword|acf_anim_length(100)|acf_enforce_rightside, amf_priority_attack|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_continue_to_next,
  [0.62, "thrust_onehanded_lance_hb", 8, 33, blend_in_release],
],
["release_thrust_onehanded_lance_continue", 0, amf_priority_continue|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust|amf_client_owner_prediction,
  [0.1, "thrust_onehanded_lance_hb", 33, 45, blend_in_continue],
],
["blocked_thrust_onehanded_lance", acf_enforce_rightside, amf_priority_blocked|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [attack_blocked_duration_thrust, "anim_human", combat+9515, combat+9513, blend_in_parry],
],
["parried_thrust_onehanded_lance", acf_enforce_rightside, amf_priority_parried|amf_use_weapon_speed|amf_play|amf_rider_rot_thrust,
  [attack_parried_duration_thrust, "anim_human", combat+9515, combat+9513, blend_in_parry],
],
''' and None





