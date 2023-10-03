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

riding = Skill("riding", "Riding", 10)
riding.set_description("Enables you to ride horses of higher difficulty levels and increases your riding speed and manuever. (Personal skill)")
riding.add_flag(SkillFlag.BASE_AT_AGI)

inventory_mgmt = Skill("inventory_management", "Inventory Management", 10)
inventory_mgmt.set_description("Increases inventory capacity by +6 per skill level. (Leader skill)")
inventory_mgmt.add_flag(SkillFlag.BASE_AT_INT)


