# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")


from skill import Skill, SkillFlag


trade = Skill("trade", "Trade", 10)
trade.set_description("Every level of this skill reduces your trade penalty by 5%%. (Party skill)")
trade.add_flag(SkillFlag.BASE_AT_CHA)
trade.add_flag(SkillFlag.EFFECTS_PARTY)

leadership = Skill("leadership", "Leadership", 10)
leadership.set_description("Every point increases maximum number of troops you can command by 5, increases your party morale and reduces troop wages by 5%%. (Leader skill)")
leadership.add_flag(SkillFlag.BASE_AT_CHA)

prisoner_mgmt = Skill("prisoner_management", "Prisoner Management", 10)
prisoner_mgmt.set_description("Every level of this skill increases maximum number of prisoners by %d. (Leader skill)")
prisoner_mgmt.add_flag(SkillFlag.BASE_AT_CHA)

reserved_1 = Skill("reserved_1", "Reserved Skill 1", 10)
reserved_1.set_description("This is a reserved skill.")
reserved_1.add_flag(SkillFlag.BASE_AT_CHA)
reserved_1.add_flag(SkillFlag.IS_INACTIVE)

reserved_2 = Skill("reserved_2", "Reserved Skill 2", 10)
reserved_2.set_description("This is a reserved skill.")
reserved_2.add_flag(SkillFlag.BASE_AT_CHA)
reserved_2.add_flag(SkillFlag.IS_INACTIVE)

reserved_3 = Skill("reserved_3", "Reserved Skill 3", 10)
reserved_3.set_description("This is a reserved skill.")
reserved_3.add_flag(SkillFlag.BASE_AT_CHA)
reserved_3.add_flag(SkillFlag.IS_INACTIVE)

reserved_4 = Skill("reserved_4", "Reserved Skill 4", 10)
reserved_4.set_description("This is a reserved skill.")
reserved_4.add_flag(SkillFlag.BASE_AT_CHA)
reserved_4.add_flag(SkillFlag.IS_INACTIVE)

persuasion = Skill("persuasion", "Persuasion", 10)
persuasion.set_description("This skill helps you make other people accept your point of view. It also lowers the minimum level of relationship needed to get NPCs to do what you want. (Personal skill)")
persuasion.add_flag(SkillFlag.BASE_AT_INT)

engineer = Skill("engineer", "Engineer", 10)
engineer.set_description("This skill allows you to construct siege equipment and fief improvements more efficiently. (Party skill)")
engineer.add_flag(SkillFlag.BASE_AT_INT)
engineer.add_flag(SkillFlag.EFFECTS_PARTY)

first_aid = Skill("first_aid", "First Aid", 10)
first_aid.set_description("Heroes regain 5%% per skill level of hit-points lost during mission. (Party skill)")
first_aid.add_flag(SkillFlag.BASE_AT_INT)
first_aid.add_flag(SkillFlag.EFFECTS_PARTY)

surgery = Skill("surgery", "Surgery", 10)
surgery.set_description("Each point to this skill gives a 4%% chance that a mortally struck party member will be wounded rather than killed. (Party skill)")
surgery.add_flag(SkillFlag.BASE_AT_INT)
surgery.add_flag(SkillFlag.EFFECTS_PARTY)

wound_treatment = Skill("wound_treatment", "Wound Treatment", 10)
wound_treatment.set_description("Party healing speed is increased by 20%% per level of this skill. (Party skill)")
wound_treatment.add_flag(SkillFlag.BASE_AT_INT)
wound_treatment.add_flag(SkillFlag.EFFECTS_PARTY)

inventory_management = Skill("inventory_management", "Inventory Management", 10)
inventory_management.set_description("Increases inventory capacity by +6 per skill level. (Leader skill)")
inventory_management.add_flag(SkillFlag.BASE_AT_INT)

spotting = Skill("spotting", "Spotting", 10)
spotting.set_description("Party seeing range is increased by 10%% per skill level. (Party skill)")
spotting.add_flag(SkillFlag.BASE_AT_INT)
spotting.add_flag(SkillFlag.EFFECTS_PARTY)

pathfinding = Skill("pathfinding", "Path-finding", 10)
pathfinding.set_description("Party map speed is increased by 3%% per skill level. (Party skill)")
pathfinding.add_flag(SkillFlag.BASE_AT_INT)
pathfinding.add_flag(SkillFlag.EFFECTS_PARTY)

tactics = Skill("tactics", "Tactics", 10)
tactics.set_description("Every two levels of this skill increases starting battle advantage by 1. (Party skill)")
tactics.add_flag(SkillFlag.BASE_AT_INT)
tactics.add_flag(SkillFlag.EFFECTS_PARTY)

tracking = Skill("tracking", "Tracking", 10)
tracking.set_description("Tracks become more informative. (Party skill)")
tracking.add_flag(SkillFlag.BASE_AT_INT)
tracking.add_flag(SkillFlag.EFFECTS_PARTY)

trainer = Skill("trainer", "Trainer", 10)
trainer.set_description("Every day, each hero with this skill adds some experience to every other member of the party whose level is lower than his/hers. Experience gained goes as: {0,4,10,16,23,30,38,46,55,65,80}. (Personal skill)")
trainer.add_flag(SkillFlag.BASE_AT_INT)

reserved_5 = Skill("reserved_5", "Reserved Skill 5", 10)
reserved_5.set_description("This is a reserved skill.")
reserved_5.add_flag(SkillFlag.BASE_AT_INT)
reserved_5.add_flag(SkillFlag.IS_INACTIVE)

reserved_6 = Skill("reserved_6", "Reserved Skill 6", 10)
reserved_6.set_description("This is a reserved skill.")
reserved_6.add_flag(SkillFlag.BASE_AT_INT)
reserved_6.add_flag(SkillFlag.IS_INACTIVE)

reserved_7 = Skill("reserved_7", "Reserved Skill 7", 10)
reserved_7.set_description("This is a reserved skill.")
reserved_7.add_flag(SkillFlag.BASE_AT_INT)
reserved_7.add_flag(SkillFlag.IS_INACTIVE)

reserved_8 = Skill("reserved_8", "Reserved Skill 8", 10)
reserved_8.set_description("This is a reserved skill.")
reserved_8.add_flag(SkillFlag.BASE_AT_INT)
reserved_8.add_flag(SkillFlag.IS_INACTIVE)

looting = Skill("looting", "Looting", 10)
looting.set_description("This skill increases the amount of loot obtained by 10%% per skill level. (Party skill)")
looting.add_flag(SkillFlag.BASE_AT_AGI)
looting.add_flag(SkillFlag.EFFECTS_PARTY)

horse_archery = Skill("horse_archery", "Horse Archery", 10)
horse_archery.set_description("Reduces damage and accuracy penalties for archery and throwing from horseback. (Personal skill)")
horse_archery.add_flag(SkillFlag.BASE_AT_AGI)

riding = Skill("riding", "Riding", 10)
riding.set_description("Enables you to ride horses of higher difficulty levels and increases your riding speed and manuever. (Personal skill)")
riding.add_flag(SkillFlag.BASE_AT_AGI)

athletics = Skill("athletics", "Athletics", 10)
athletics.set_description("Improves your running speed. (Personal skill)")
athletics.add_flag(SkillFlag.BASE_AT_AGI)

shield = Skill("shield", "Shield", 10)
shield.set_description("Reduces damage to shields (by 8%% per skill level) and improves shield speed and coverage. (Personal skill)")
shield.add_flag(SkillFlag.BASE_AT_AGI)

weapon_master = Skill("weapon_master", "Weapon Master", 10)
weapon_master.set_description("Makes it easier to learn weapon proficiencies and increases the proficiency limits. Limits go as: 60, 100, 140, 180, 220, 260, 300, 340, 380, 420. (Personal skill)")
weapon_master.add_flag(SkillFlag.BASE_AT_AGI)

reserved_9 = Skill("reserved_9", "Reserved Skill 9", 10)
reserved_9.set_description("This is a reserved skill.")
reserved_9.add_flag(SkillFlag.BASE_AT_AGI)
reserved_9.add_flag(SkillFlag.IS_INACTIVE)

reserved_10 = Skill("reserved_10", "Reserved Skill 10", 10)
reserved_10.set_description("This is a reserved skill.")
reserved_10.add_flag(SkillFlag.BASE_AT_AGI)
reserved_10.add_flag(SkillFlag.IS_INACTIVE)

reserved_11 = Skill("reserved_11", "Reserved Skill 11", 10)
reserved_11.set_description("This is a reserved skill.")
reserved_11.add_flag(SkillFlag.BASE_AT_AGI)
reserved_11.add_flag(SkillFlag.IS_INACTIVE)

reserved_12 = Skill("reserved_12", "Reserved Skill 12", 10)
reserved_12.set_description("This is a reserved skill.")
reserved_12.add_flag(SkillFlag.BASE_AT_AGI)
reserved_12.add_flag(SkillFlag.IS_INACTIVE)

reserved_13 = Skill("reserved_13", "Reserved Skill 13", 10)
reserved_13.set_description("This is a reserved skill.")
reserved_13.add_flag(SkillFlag.BASE_AT_AGI)
reserved_13.add_flag(SkillFlag.IS_INACTIVE)

power_draw = Skill("power_draw", "Power Draw", 10)
power_draw.set_description("Lets character use more powerful bows. Each point to this skill (up to four plus power-draw requirement of the bow) increases bow damage by 14%%. (Personal skill)")
power_draw.add_flag(SkillFlag.BASE_AT_STR)

power_throw = Skill("power_throw", "Power Throw", 10)
power_throw.set_description("Each point to this skill increases throwing damage by 10%%. (Personal skill)")
power_throw.add_flag(SkillFlag.BASE_AT_STR)

power_strike = Skill("power_strike", "Power Draw", 10)
power_strike.set_description("Each point to this skill increases melee damage by 8%%. (Personal skill)")
power_strike.add_flag(SkillFlag.BASE_AT_STR)

ironflesh = Skill("ironflesh", "Ironflesh", 10)
ironflesh.set_description("Each point to this skill increases hit points by +2. (Personal skill)")
ironflesh.add_flag(SkillFlag.BASE_AT_STR)

reserved_14 = Skill("reserved_14", "Reserved Skill 14", 10)
reserved_14.set_description("This is a reserved skill.")
reserved_14.add_flag(SkillFlag.BASE_AT_STR)
reserved_14.add_flag(SkillFlag.IS_INACTIVE)

reserved_15 = Skill("reserved_15", "Reserved Skill 15", 10)
reserved_15.set_description("This is a reserved skill.")
reserved_15.add_flag(SkillFlag.BASE_AT_STR)
reserved_15.add_flag(SkillFlag.IS_INACTIVE)

reserved_16 = Skill("reserved_16", "Reserved Skill 16", 10)
reserved_16.set_description("This is a reserved skill.")
reserved_16.add_flag(SkillFlag.BASE_AT_STR)
reserved_16.add_flag(SkillFlag.IS_INACTIVE)

reserved_17 = Skill("reserved_17", "Reserved Skill 17", 10)
reserved_17.set_description("This is a reserved skill.")
reserved_17.add_flag(SkillFlag.BASE_AT_STR)
reserved_17.add_flag(SkillFlag.IS_INACTIVE)

reserved_18 = Skill("reserved_18", "Reserved Skill 18", 10)
reserved_18.set_description("This is a reserved skill.")
reserved_18.add_flag(SkillFlag.BASE_AT_STR)
reserved_18.add_flag(SkillFlag.IS_INACTIVE)


