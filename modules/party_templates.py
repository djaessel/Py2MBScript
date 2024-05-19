# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")

from party_template import PartyTemplate, PartyFlag

import troops as trp
import factions as fac
import map_icons as icon


none = PartyTemplate("none", "none", faction=fac.commoners, personality="7")
none.add_flag(PartyFlag.LABEL_SMALL)
none.set_icon(icon.gray_knight)


rescued_prisoners = PartyTemplate("rescued_prisoners", "Rescued_Prisoners", faction=fac.commoners, personality="7")
rescued_prisoners.add_flag(PartyFlag.LABEL_SMALL)
rescued_prisoners.set_icon(icon.gray_knight)


enemy = PartyTemplate("enemy", "Enemy", faction=fac.undeads, personality="7")
enemy.add_flag(PartyFlag.LABEL_SMALL)
enemy.set_icon(icon.gray_knight)


hero_party = PartyTemplate("hero_party", "Hero_Party", faction=fac.commoners, personality="7")
hero_party.add_flag(PartyFlag.LABEL_SMALL)
hero_party.set_icon(icon.gray_knight)


village_defenders = PartyTemplate("village_defenders", "Village_Defenders", faction=fac.commoners, personality="7")
village_defenders.add_flag(PartyFlag.LABEL_SMALL)
village_defenders.set_icon(icon.peasant)
village_defenders.addStack(trp.farmer, min=10, max=20)
village_defenders.addStack(trp.peasant_woman, min=0, max=4)


cattle_herd = PartyTemplate("cattle_herd", "Cattle_Herd", faction=fac.neutral, personality="7")
cattle_herd.add_flag(PartyFlag.LABEL_SMALL)
cattle_herd.set_icon(icon.cattle)
cattle_herd.setCarriesGoods(10)
cattle_herd.addStack(trp.cattle, min=80, max=120)


looters = PartyTemplate("looters", "Looters", faction=fac.outlaws, personality="312")
looters.add_flag(PartyFlag.LABEL_SMALL)
looters.set_icon(icon.axeman)
looters.setCarriesGoods(8)
looters.addStack(trp.looter, min=3, max=45)


manhunters = PartyTemplate("manhunters", "Manhunters", faction=fac.manhunters, personality="137")
manhunters.add_flag(PartyFlag.LABEL_SMALL)
manhunters.set_icon(icon.gray_knight)
manhunters.addStack(trp.manhunter, min=9, max=40)


steppe_bandits = PartyTemplate("steppe_bandits", "Steppe_Bandits", faction=fac.outlaws, personality="312")
steppe_bandits.add_flag(PartyFlag.LABEL_SMALL)
steppe_bandits.set_icon(icon.khergit)
steppe_bandits.setCarriesGoods(2)
steppe_bandits.addStack(trp.steppe_bandit, min=4, max=58)


taiga_bandits = PartyTemplate("taiga_bandits", "Tundra_Bandits", faction=fac.outlaws, personality="312")
taiga_bandits.add_flag(PartyFlag.LABEL_SMALL)
taiga_bandits.set_icon(icon.axeman)
taiga_bandits.setCarriesGoods(2)
taiga_bandits.addStack(trp.taiga_bandit, min=4, max=58)


desert_bandits = PartyTemplate("desert_bandits", "Desert_Bandits", faction=fac.outlaws, personality="312")
desert_bandits.add_flag(PartyFlag.LABEL_SMALL)
desert_bandits.set_icon(icon.vaegir_knight)
desert_bandits.setCarriesGoods(2)
desert_bandits.addStack(trp.desert_bandit, min=4, max=58)


forest_bandits = PartyTemplate("forest_bandits", "Forest_Bandits", faction=fac.forest_bandits, personality="312")
forest_bandits.add_flag(PartyFlag.LABEL_SMALL)
forest_bandits.set_icon(icon.axeman)
forest_bandits.setCarriesGoods(2)
forest_bandits.addStack(trp.forest_bandit, min=4, max=52)


mountain_bandits = PartyTemplate("mountain_bandits", "Mountain_Bandits", faction=fac.mountain_bandits, personality="312")
mountain_bandits.add_flag(PartyFlag.LABEL_SMALL)
mountain_bandits.set_icon(icon.axeman)
mountain_bandits.setCarriesGoods(2)
mountain_bandits.addStack(trp.mountain_bandit, min=4, max=60)


sea_raiders = PartyTemplate("sea_raiders", "Sea_Raiders", faction=fac.outlaws, personality="312")
sea_raiders.add_flag(PartyFlag.LABEL_SMALL)
sea_raiders.set_icon(icon.axeman)
sea_raiders.setCarriesGoods(2)
sea_raiders.addStack(trp.sea_raider, min=5, max=50)


deserters = PartyTemplate("deserters", "Deserters", faction=fac.deserters, personality="312")
deserters.add_flag(PartyFlag.LABEL_SMALL)
deserters.set_icon(icon.vaegir_knight)
deserters.setCarriesGoods(3)


merchant_caravan = PartyTemplate("merchant_caravan", "Merchant_Caravan", faction=fac.commoners, personality="11")
merchant_caravan.add_flag(PartyFlag.LABEL_SMALL)
merchant_caravan.add_flag(PartyFlag.AUTO_REMOVE_IN_TOWN)
merchant_caravan.add_flag(PartyFlag.IS_QUEST_PARTY)
merchant_caravan.set_icon(icon.gray_knight)
merchant_caravan.setCarriesGoods(20)
merchant_caravan.addStack(trp.caravan_master, min=1, max=1)
merchant_caravan.addStack(trp.caravan_guard, min=5, max=25)


troublesome_bandits = PartyTemplate("troublesome_bandits", "Troublesome_Bandits", faction=fac.outlaws, personality="312")
troublesome_bandits.add_flag(PartyFlag.LABEL_SMALL)
troublesome_bandits.add_flag(PartyFlag.IS_QUEST_PARTY)
troublesome_bandits.set_icon(icon.axeman)
troublesome_bandits.setCarriesGoods(9)
troublesome_bandits.addStack(trp.bandit, min=14, max=55)


bandits_awaiting_ransom = PartyTemplate("bandits_awaiting_ransom", "Bandits_Awaiting_Ransom", faction=fac.neutral, personality="312")
bandits_awaiting_ransom.add_flag(PartyFlag.LABEL_SMALL)
bandits_awaiting_ransom.add_flag(PartyFlag.AUTO_REMOVE_IN_TOWN)
bandits_awaiting_ransom.add_flag(PartyFlag.IS_QUEST_PARTY)
bandits_awaiting_ransom.set_icon(icon.axeman)
bandits_awaiting_ransom.setCarriesGoods(9)
bandits_awaiting_ransom.addStack(trp.bandit, min=24, max=58)
bandits_awaiting_ransom.addStack(trp.kidnapped_girl, min=1, max=1, are_prisoners=True)


kidnapped_girl = PartyTemplate("kidnapped_girl", "Kidnapped_Girl", faction=fac.neutral, personality="7")
kidnapped_girl.add_flag(PartyFlag.LABEL_SMALL)
kidnapped_girl.add_flag(PartyFlag.IS_QUEST_PARTY)
kidnapped_girl.set_icon(icon.woman)
kidnapped_girl.addStack(trp.kidnapped_girl, min=1, max=1)


village_farmers = PartyTemplate("village_farmers", "Village_Farmers", faction=fac.innocents, personality="7")
village_farmers.add_flag(PartyFlag.LABEL_SMALL)
village_farmers.add_flag(PartyFlag.IS_CIVILIAN)
village_farmers.set_icon(icon.peasant)
village_farmers.addStack(trp.farmer, min=5, max=10)
village_farmers.addStack(trp.peasant_woman, min=3, max=8)


spy_partners = PartyTemplate("spy_partners", "Unremarkable_Travellers", faction=fac.neutral, personality="7")
spy_partners.add_flag(PartyFlag.LABEL_SMALL)
spy_partners.add_flag(PartyFlag.HAS_DEFAULT_BEHAVIOR)
spy_partners.add_flag(PartyFlag.IS_QUEST_PARTY)
spy_partners.set_icon(icon.gray_knight)
spy_partners.setCarriesGoods(10)
spy_partners.addStack(trp.spy_partner, min=1, max=1)
spy_partners.addStack(trp.caravan_guard, min=5, max=11)


runaway_serfs = PartyTemplate("runaway_serfs", "Runaway_Serfs", faction=fac.neutral, personality="7")
runaway_serfs.add_flag(PartyFlag.LABEL_SMALL)
runaway_serfs.add_flag(PartyFlag.HAS_DEFAULT_BEHAVIOR)
runaway_serfs.add_flag(PartyFlag.IS_QUEST_PARTY)
runaway_serfs.set_icon(icon.peasant)
runaway_serfs.setCarriesGoods(8)
runaway_serfs.addStack(trp.farmer, min=6, max=7)
runaway_serfs.addStack(trp.peasant_woman, min=3, max=3)


spy = PartyTemplate("spy", "Ordinary_Townsman", faction=fac.neutral, personality="7")
spy.add_flag(PartyFlag.LABEL_SMALL)
spy.add_flag(PartyFlag.HAS_DEFAULT_BEHAVIOR)
spy.add_flag(PartyFlag.IS_QUEST_PARTY)
spy.set_icon(icon.gray_knight)
spy.setCarriesGoods(4)
spy.addStack(trp.spy, min=1, max=1)


sacrificed_messenger = PartyTemplate("sacrificed_messenger", "Sacrificed_Messenger", faction=fac.neutral, personality="7")
sacrificed_messenger.add_flag(PartyFlag.LABEL_SMALL)
sacrificed_messenger.add_flag(PartyFlag.HAS_DEFAULT_BEHAVIOR)
sacrificed_messenger.add_flag(PartyFlag.IS_QUEST_PARTY)
sacrificed_messenger.set_icon(icon.gray_knight)
sacrificed_messenger.setCarriesGoods(3)


forager_party = PartyTemplate("forager_party", "Foraging_Party", faction=fac.commoners, personality="7")
forager_party.add_flag(PartyFlag.LABEL_SMALL)
forager_party.add_flag(PartyFlag.SHOW_FACTION)
forager_party.set_icon(icon.gray_knight)
forager_party.setCarriesGoods(5)


scout_party = PartyTemplate("scout_party", "Scouts", faction=fac.commoners, personality="312")
scout_party.add_flag(PartyFlag.LABEL_SMALL)
scout_party.add_flag(PartyFlag.SHOW_FACTION)
scout_party.set_icon(icon.gray_knight)
scout_party.setCarriesGoods(1)


patrol_party = PartyTemplate("patrol_party", "Patrol", faction=fac.commoners, personality="137")
patrol_party.add_flag(PartyFlag.LABEL_SMALL)
patrol_party.add_flag(PartyFlag.SHOW_FACTION)
patrol_party.set_icon(icon.gray_knight)
patrol_party.setCarriesGoods(2)


messenger_party = PartyTemplate("messenger_party", "Messenger", faction=fac.commoners, personality="7")
messenger_party.add_flag(PartyFlag.LABEL_SMALL)
messenger_party.add_flag(PartyFlag.SHOW_FACTION)
messenger_party.set_icon(icon.gray_knight)


raider_party = PartyTemplate("raider_party", "Raiders", faction=fac.commoners, personality="312")
raider_party.add_flag(PartyFlag.LABEL_SMALL)
raider_party.add_flag(PartyFlag.IS_QUEST_PARTY)
raider_party.set_icon(icon.gray_knight)
raider_party.setCarriesGoods(16)


raider_captives = PartyTemplate("raider_captives", "Raider_Captives", faction=fac.commoners)
raider_captives.add_flag(PartyFlag.LABEL_SMALL)
raider_captives.addStack(trp.peasant_woman, min=6, max=30, are_prisoners=True)


kingdom_caravan_party = PartyTemplate("kingdom_caravan_party", "Caravan", faction=fac.commoners, personality="7")
kingdom_caravan_party.add_flag(PartyFlag.LABEL_SMALL)
kingdom_caravan_party.add_flag(PartyFlag.SHOW_FACTION)
kingdom_caravan_party.set_icon(icon.mule)
kingdom_caravan_party.setCarriesGoods(25)
kingdom_caravan_party.addStack(trp.caravan_master, min=1, max=1)
kingdom_caravan_party.addStack(trp.caravan_guard, min=12, max=40)


prisoner_train_party = PartyTemplate("prisoner_train_party", "Prisoner_Train", faction=fac.commoners, personality="7")
prisoner_train_party.add_flag(PartyFlag.LABEL_SMALL)
prisoner_train_party.add_flag(PartyFlag.SHOW_FACTION)
prisoner_train_party.set_icon(icon.gray_knight)
prisoner_train_party.setCarriesGoods(5)


default_prisoners = PartyTemplate("default_prisoners", "Default_Prisoners", faction=fac.commoners)
default_prisoners.add_flag(PartyFlag.LABEL_SMALL)
default_prisoners.addStack(trp.bandit, min=5, max=10, are_prisoners=True)


routed_warriors = PartyTemplate("routed_warriors", "Routed_Enemies", faction=fac.commoners, personality="137")
routed_warriors.add_flag(PartyFlag.LABEL_SMALL)
routed_warriors.set_icon(icon.vaegir_knight)


center_reinforcements = PartyTemplate("center_reinforcements", "Reinforcements", faction=fac.commoners, personality="137")
center_reinforcements.add_flag(PartyFlag.LABEL_SMALL)
center_reinforcements.set_icon(icon.axeman)
center_reinforcements.setCarriesGoods(16)
center_reinforcements.addStack(trp.townsman, min=5, max=30)
center_reinforcements.addStack(trp.watchman, min=4, max=20)


kingdom_hero_party = PartyTemplate("kingdom_hero_party", "War_Party", faction=fac.commoners, personality="137")
kingdom_hero_party.add_flag(PartyFlag.LABEL_SMALL)
kingdom_hero_party.add_flag(PartyFlag.HAS_DEFAULT_BEHAVIOR)
kingdom_hero_party.add_flag(PartyFlag.SHOW_FACTION)
kingdom_hero_party.set_icon(icon.flagbearer_a)


kingdom_1_reinforcements_a = PartyTemplate("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", faction=fac.commoners)
kingdom_1_reinforcements_a.add_flag(PartyFlag.LABEL_SMALL)
kingdom_1_reinforcements_a.addStack(trp.swadian_recruit, min=5, max=10)
kingdom_1_reinforcements_a.addStack(trp.swadian_militia, min=2, max=4)


kingdom_1_reinforcements_b = PartyTemplate("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", faction=fac.commoners)
kingdom_1_reinforcements_b.add_flag(PartyFlag.LABEL_SMALL)
kingdom_1_reinforcements_b.addStack(trp.swadian_footman, min=3, max=6)
kingdom_1_reinforcements_b.addStack(trp.swadian_skirmisher, min=2, max=4)


kingdom_1_reinforcements_c = PartyTemplate("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", faction=fac.commoners)
kingdom_1_reinforcements_c.add_flag(PartyFlag.LABEL_SMALL)
kingdom_1_reinforcements_c.addStack(trp.swadian_man_at_arms, min=2, max=4)
kingdom_1_reinforcements_c.addStack(trp.swadian_crossbowman, min=1, max=2)


kingdom_2_reinforcements_a = PartyTemplate("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", faction=fac.commoners)
kingdom_2_reinforcements_a.add_flag(PartyFlag.LABEL_SMALL)
kingdom_2_reinforcements_a.addStack(trp.vaegir_recruit, min=5, max=10)
kingdom_2_reinforcements_a.addStack(trp.vaegir_footman, min=2, max=4)


kingdom_2_reinforcements_b = PartyTemplate("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", faction=fac.commoners)
kingdom_2_reinforcements_b.add_flag(PartyFlag.LABEL_SMALL)
kingdom_2_reinforcements_b.addStack(trp.vaegir_veteran, min=2, max=4)
kingdom_2_reinforcements_b.addStack(trp.vaegir_skirmisher, min=2, max=4)
kingdom_2_reinforcements_b.addStack(trp.vaegir_footman, min=1, max=2)


kingdom_2_reinforcements_c = PartyTemplate("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", faction=fac.commoners)
kingdom_2_reinforcements_c.add_flag(PartyFlag.LABEL_SMALL)
kingdom_2_reinforcements_c.addStack(trp.vaegir_horseman, min=2, max=3)
kingdom_2_reinforcements_c.addStack(trp.vaegir_infantry, min=1, max=2)


kingdom_3_reinforcements_a = PartyTemplate("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", faction=fac.commoners)
kingdom_3_reinforcements_a.add_flag(PartyFlag.LABEL_SMALL)
kingdom_3_reinforcements_a.addStack(trp.khergit_tribesman, min=3, max=5)
kingdom_3_reinforcements_a.addStack(trp.khergit_skirmisher, min=4, max=9)


kingdom_3_reinforcements_b = PartyTemplate("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", faction=fac.commoners)
kingdom_3_reinforcements_b.add_flag(PartyFlag.LABEL_SMALL)
kingdom_3_reinforcements_b.addStack(trp.khergit_horseman, min=2, max=4)
kingdom_3_reinforcements_b.addStack(trp.khergit_horse_archer, min=2, max=4)
kingdom_3_reinforcements_b.addStack(trp.khergit_skirmisher, min=1, max=2)


kingdom_3_reinforcements_c = PartyTemplate("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", faction=fac.commoners)
kingdom_3_reinforcements_c.add_flag(PartyFlag.LABEL_SMALL)
kingdom_3_reinforcements_c.addStack(trp.khergit_horseman, min=2, max=4)
kingdom_3_reinforcements_c.addStack(trp.khergit_veteran_horse_archer, min=2, max=3)


kingdom_4_reinforcements_a = PartyTemplate("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", faction=fac.commoners)
kingdom_4_reinforcements_a.add_flag(PartyFlag.LABEL_SMALL)
kingdom_4_reinforcements_a.addStack(trp.nord_footman, min=5, max=10)
kingdom_4_reinforcements_a.addStack(trp.nord_recruit, min=2, max=4)


kingdom_4_reinforcements_b = PartyTemplate("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", faction=fac.commoners)
kingdom_4_reinforcements_b.add_flag(PartyFlag.LABEL_SMALL)
kingdom_4_reinforcements_b.addStack(trp.nord_huntsman, min=2, max=5)
kingdom_4_reinforcements_b.addStack(trp.nord_archer, min=2, max=3)
kingdom_4_reinforcements_b.addStack(trp.nord_footman, min=1, max=2)


kingdom_4_reinforcements_c = PartyTemplate("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", faction=fac.commoners)
kingdom_4_reinforcements_c.add_flag(PartyFlag.LABEL_SMALL)
kingdom_4_reinforcements_c.addStack(trp.nord_warrior, min=3, max=5)


kingdom_5_reinforcements_a = PartyTemplate("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", faction=fac.commoners)
kingdom_5_reinforcements_a.add_flag(PartyFlag.LABEL_SMALL)
kingdom_5_reinforcements_a.addStack(trp.rhodok_tribesman, min=5, max=10)
kingdom_5_reinforcements_a.addStack(trp.rhodok_spearman, min=2, max=4)


kingdom_5_reinforcements_b = PartyTemplate("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", faction=fac.commoners)
kingdom_5_reinforcements_b.add_flag(PartyFlag.LABEL_SMALL)
kingdom_5_reinforcements_b.addStack(trp.rhodok_crossbowman, min=3, max=6)
kingdom_5_reinforcements_b.addStack(trp.rhodok_trained_crossbowman, min=2, max=4)


kingdom_5_reinforcements_c = PartyTemplate("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", faction=fac.commoners)
kingdom_5_reinforcements_c.add_flag(PartyFlag.LABEL_SMALL)
kingdom_5_reinforcements_c.addStack(trp.rhodok_veteran_spearman, min=2, max=3)
kingdom_5_reinforcements_c.addStack(trp.rhodok_veteran_crossbowman, min=1, max=2)


kingdom_6_reinforcements_a = PartyTemplate("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", faction=fac.commoners)
kingdom_6_reinforcements_a.add_flag(PartyFlag.LABEL_SMALL)
kingdom_6_reinforcements_a.addStack(trp.sarranid_recruit, min=5, max=10)
kingdom_6_reinforcements_a.addStack(trp.sarranid_footman, min=2, max=4)


kingdom_6_reinforcements_b = PartyTemplate("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", faction=fac.commoners)
kingdom_6_reinforcements_b.add_flag(PartyFlag.LABEL_SMALL)
kingdom_6_reinforcements_b.addStack(trp.sarranid_skirmisher, min=2, max=4)
kingdom_6_reinforcements_b.addStack(trp.sarranid_veteran_footman, min=2, max=3)
kingdom_6_reinforcements_b.addStack(trp.sarranid_footman, min=1, max=3)


kingdom_6_reinforcements_c = PartyTemplate("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", faction=fac.commoners)
kingdom_6_reinforcements_c.add_flag(PartyFlag.LABEL_SMALL)
kingdom_6_reinforcements_c.addStack(trp.sarranid_horseman, min=3, max=5)


steppe_bandit_lair = PartyTemplate("steppe_bandit_lair", "Steppe_Bandit_Lair", faction=fac.neutral, personality="312")
steppe_bandit_lair.add_flag(PartyFlag.IS_STATIC)
steppe_bandit_lair.add_flag(PartyFlag.LABEL_SMALL)
steppe_bandit_lair.add_flag(PartyFlag.HIDE_DEFENDERS)
steppe_bandit_lair.set_icon(icon.bandit_lair)
steppe_bandit_lair.setCarriesGoods(2)
steppe_bandit_lair.addStack(trp.steppe_bandit, min=15, max=58)


taiga_bandit_lair = PartyTemplate("taiga_bandit_lair", "Tundra_Bandit_Lair", faction=fac.neutral, personality="312")
taiga_bandit_lair.add_flag(PartyFlag.IS_STATIC)
taiga_bandit_lair.add_flag(PartyFlag.LABEL_SMALL)
taiga_bandit_lair.add_flag(PartyFlag.HIDE_DEFENDERS)
taiga_bandit_lair.set_icon(icon.bandit_lair)
taiga_bandit_lair.setCarriesGoods(2)
taiga_bandit_lair.addStack(trp.taiga_bandit, min=15, max=58)


desert_bandit_lair = PartyTemplate("desert_bandit_lair", "Desert_Bandit_Lair", faction=fac.neutral, personality="312")
desert_bandit_lair.add_flag(PartyFlag.IS_STATIC)
desert_bandit_lair.add_flag(PartyFlag.LABEL_SMALL)
desert_bandit_lair.add_flag(PartyFlag.HIDE_DEFENDERS)
desert_bandit_lair.set_icon(icon.bandit_lair)
desert_bandit_lair.setCarriesGoods(2)
desert_bandit_lair.addStack(trp.desert_bandit, min=15, max=58)


forest_bandit_lair = PartyTemplate("forest_bandit_lair", "Forest_Bandit_Camp", faction=fac.neutral, personality="312")
forest_bandit_lair.add_flag(PartyFlag.IS_STATIC)
forest_bandit_lair.add_flag(PartyFlag.LABEL_SMALL)
forest_bandit_lair.add_flag(PartyFlag.HIDE_DEFENDERS)
forest_bandit_lair.set_icon(icon.bandit_lair)
forest_bandit_lair.setCarriesGoods(2)
forest_bandit_lair.addStack(trp.forest_bandit, min=15, max=58)


mountain_bandit_lair = PartyTemplate("mountain_bandit_lair", "Mountain_Bandit_Hideout", faction=fac.neutral, personality="312")
mountain_bandit_lair.add_flag(PartyFlag.IS_STATIC)
mountain_bandit_lair.add_flag(PartyFlag.LABEL_SMALL)
mountain_bandit_lair.add_flag(PartyFlag.HIDE_DEFENDERS)
mountain_bandit_lair.set_icon(icon.bandit_lair)
mountain_bandit_lair.setCarriesGoods(2)
mountain_bandit_lair.addStack(trp.mountain_bandit, min=15, max=58)


sea_raider_lair = PartyTemplate("sea_raider_lair", "Sea_Raider_Landing", faction=fac.neutral, personality="312")
sea_raider_lair.add_flag(PartyFlag.IS_STATIC)
sea_raider_lair.add_flag(PartyFlag.LABEL_SMALL)
sea_raider_lair.add_flag(PartyFlag.HIDE_DEFENDERS)
sea_raider_lair.set_icon(icon.bandit_lair)
sea_raider_lair.setCarriesGoods(2)
sea_raider_lair.addStack(trp.sea_raider, min=15, max=50)


looter_lair = PartyTemplate("looter_lair", "Kidnappers'_Hideout", faction=fac.neutral, personality="312")
looter_lair.add_flag(PartyFlag.IS_STATIC)
looter_lair.add_flag(PartyFlag.LABEL_SMALL)
looter_lair.add_flag(PartyFlag.HIDE_DEFENDERS)
looter_lair.set_icon(icon.bandit_lair)
looter_lair.setCarriesGoods(2)
looter_lair.addStack(trp.looter, min=15, max=25)


bandit_lair_templates_end = PartyTemplate("bandit_lair_templates_end", "{!}bandit_lair_templates_end", faction=fac.outlaws, personality="312")
bandit_lair_templates_end.add_flag(PartyFlag.IS_STATIC)
bandit_lair_templates_end.add_flag(PartyFlag.LABEL_SMALL)
bandit_lair_templates_end.set_icon(icon.axeman)
bandit_lair_templates_end.setCarriesGoods(2)
bandit_lair_templates_end.addStack(trp.sea_raider, min=15, max=50)


leaded_looters = PartyTemplate("leaded_looters", "Band_of_robbers", faction=fac.neutral, personality="312")
leaded_looters.add_flag(PartyFlag.LABEL_SMALL)
leaded_looters.add_flag(PartyFlag.IS_QUEST_PARTY)
leaded_looters.set_icon(icon.axeman)
leaded_looters.setCarriesGoods(8)
leaded_looters.addStack(trp.looter_leader, min=1, max=1)
leaded_looters.addStack(trp.looter, min=3, max=3)


