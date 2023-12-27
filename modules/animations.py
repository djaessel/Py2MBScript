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






