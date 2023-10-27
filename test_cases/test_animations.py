# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("./data_objects/")


from animation import Animation, AnimationSequence, AnimationFlag, AnimationMasterFlag, AnimationSequenceFlag


anim1 = Animation("stand_player_first_person")
anim1.add_master_flag(AnimationMasterFlag.CLIENT_PREDICTION)

seqx = AnimationSequence(3.5, "anim_human", 90, 100)
seqx.setExtraVals(7, 0.25)
seqx.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seqx.add_flag(AnimationSequenceFlag.CYCLIC)
anim1.add_sequence(seqx)

seqx = AnimationSequence(3.5, "anim_human", 110, 120)
seqx.setExtraVals(7, 0.25)
seqx.add_flag(AnimationSequenceFlag.USE_STAND_PROGRESS)
seqx.add_flag(AnimationSequenceFlag.CYCLIC)
anim1.add_sequence(seqx)


