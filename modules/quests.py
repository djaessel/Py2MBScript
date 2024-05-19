# This Python file uses the following encoding: utf-8

import sys
sys.path.append("../data_objects/")

from quest import Quest





deliver_message = Quest("deliver_message", name="Deliver Message to {s13}", description="{!}{s9} asked you to take a message to {s13}. {s13} was at {s4} when you were given this quest.")


deliver_message_to_enemy_lord = Quest("deliver_message_to_enemy_lord", name="Deliver Message to {s13}", description="{!}{s9} asked you to take a message to {s13} of {s15}. {s13} was at {s4} when you were given this quest.")


raise_troops = Quest("raise_troops", name="Raise {reg1} {s14}", description="{!}{s9} asked you to raise {reg1} {s14} and bring them to him.")


escort_lady = Quest("escort_lady", name="Escort {s13} to {s14}", description="{!}None")


deal_with_bandits_at_lords_village = Quest("deal_with_bandits_at_lords_village", name="Save the Village of {s15} from Marauding Bandits", description="{!}{s13} asked you to deal with the bandits who took refuge in his village of {s15} and then report back to him.")


collect_taxes = Quest("collect_taxes", name="Collect Taxes from {s3}", description="{!}{s9} asked you to collect taxes from {s3}. He offered to leave you one-fifth of all the money you collect there.")


hunt_down_fugitive = Quest("hunt_down_fugitive", name="Hunt Down {s4}", description="{!}{s9} asked you to hunt down the fugitive named {s4}. He is currently believed to be at {s3}.")


kill_local_merchant = Quest("kill_local_merchant", name="Assassinate Local Merchant at {s3}", description="{!}{s9} asked you to assassinate a local merchant at {s3}.")


bring_back_runaway_serfs = Quest("bring_back_runaway_serfs", name="Bring Back Runaway Serfs", description="{!}{s9} asked you to bring back the three groups of runaway serfs back to {s2}. He said all three groups must be running away in the direction of {s3}.")


follow_spy = Quest("follow_spy", name="Follow the Spy to Meeting", description="{!}{s11} asked you to follow the spy that will leave {s12}. You must be careful not to be seen by the spy during his travel, or else he may get suspicious and turn back. Once the spy meets with his accomplice, you are to ambush and capture them and bring them both back to {s11}.")


capture_enemy_hero = Quest("capture_enemy_hero", name="Capture a Lord from {s13}", description="{!}TODO: {s11} asked you to capture a lord from {s13}.")


lend_companion = Quest("lend_companion", name="Lend Your Companion {s3} to {s9}", description="{!}{s9} asked you to lend your companion {s3} to him for a week.")


collect_debt = Quest("collect_debt", name="Collect the Debt {s3} Owes to {s9}", description="{!}{s9} asked you to collect the debt of {reg4} denars {s3} owes to him.")


incriminate_loyal_commander = Quest("incriminate_loyal_commander", name="Incriminate the Loyal Commander of {s13}, {s16}", description="{!}None")


meet_spy_in_enemy_town = Quest("meet_spy_in_enemy_town", name="Meet Spy in {s13}", description="{!}None")


capture_prisoners = Quest("capture_prisoners", name="Bring {reg1} {s3} Prisoners", description="{!}{s9} wanted you to bring him {reg1} {s3} as prisoners.")


lend_surgeon = Quest("lend_surgeon", name="Lend Your Surgeon {s3} to {s1}", description="{!}Lend your experienced surgeon {s3} to {s1}.")


follow_army = Quest("follow_army", name="Follow {s9}'s Army", description="{!}None")


report_to_army = Quest("report_to_army", name="Report to {s13}, the Marshall", description="{!}None")


deliver_cattle_to_army = Quest("deliver_cattle_to_army", name="Deliver {reg3} Heads of Cattle to {s13}", description="{!}None")


join_siege_with_army = Quest("join_siege_with_army", name="Join the Siege of {s14}", description="{!}None")


screen_army = Quest("screen_army", name="Screen the Advance of {s13}'s Army", description="{!}None")


scout_waypoints = Quest("scout_waypoints", name="Scout {s13}, {s14} and {s15}", description="{!}None")


rescue_lord_by_replace = Quest("rescue_lord_by_replace", name="Rescue {s13} from {s14}", description="{!}None")


deliver_message_to_prisoner_lord = Quest("deliver_message_to_prisoner_lord", name="Deliver Message to {s13} at {s14}", description="{!}None")


duel_for_lady = Quest("duel_for_lady", name="Challenge {s13} to a Trial of Arms", description="{!}None")


duel_courtship_rival = Quest("duel_courtship_rival", name="Challenge {s13} to a Trial of Arms (optional)", description="{!}None")


duel_avenge_insult = Quest("duel_avenge_insult", name="Challenge {s13} to a Trial of Arms", description="{!}None")


move_cattle_herd = Quest("move_cattle_herd", name="Move Cattle Herd to {s13}", description="{!}Guildmaster of {s10} asked you to move a cattle herd to {s13}.")


escort_merchant_caravan = Quest("escort_merchant_caravan", name="Escort Merchant Caravan to {s8}", description="{!}Escort the merchant caravan to the town of {s8}.")


deliver_wine = Quest("deliver_wine", name="Deliver {reg5} Units of {s6} to {s4}", description="{!}{s9} of {s3} asked you to deliver {reg5} units of {s6} to the tavern in {s4} in 7 days.")


troublesome_bandits = Quest("troublesome_bandits", name="Hunt Down Troublesome Bandits", description="{!}{s9} of {s4} asked you to hunt down the troublesome bandits in the vicinity of the town.")


kidnapped_girl = Quest("kidnapped_girl", name="Ransom Girl from Bandits", description="{!}Guildmaster of {s4} gave you {reg12} denars to pay the ransom of a girl kidnapped by bandits. You are to meet the bandits near {s3} and pay them the ransom fee. After that you are to bring the girl back to {s4}.")


persuade_lords_to_make_peace = Quest("persuade_lords_to_make_peace", name="Make Sure Two Lords Do Not Object to Peace", description="{!}Guildmaster of {s4} promised you {reg12} denars if you can make sure that {s12} and {s13} no longer pose a threat to a peace settlement between {s15} and {s14}. In order to do that, you must either convince them or make sure they fall captive and remain so until a peace agreement is made.")


deal_with_looters = Quest("deal_with_looters", name="Deal with Looters", description="{!}The Guildmaster of {s4} has asked you to deal with several bands of looters around {s4}, and bring back any goods you recover.")


deal_with_night_bandits = Quest("deal_with_night_bandits", name="Deal with Night Bandits", description="{!}TODO: The Guildmaster of {s14} has asked you to deal with night bandits at {s14}.")


deliver_grain = Quest("deliver_grain", name="Bring wheat to {s3}", description="{!}The elder of the village of {s3} asked you to bring them {reg5} packs of wheat..")


deliver_cattle = Quest("deliver_cattle", name="Deliver {reg5} Heads of Cattle to {s3}", description="{!}The elder of the village of {s3} asked you to bring {reg5} heads of cattle.")


train_peasants_against_bandits = Quest("train_peasants_against_bandits", name="Train the Peasants of {s13} Against Bandits.", description="{!}None")


eliminate_bandits_infesting_village = Quest("eliminate_bandits_infesting_village", name="Save the Village of {s7} from Marauding Bandits", description="{!}A villager from {s7} begged you to save their village from the bandits that took refuge there.")


visit_lady = Quest("visit_lady", name="Visit Lady", description="{!}None")


formal_marriage_proposal = Quest("formal_marriage_proposal", name="Formal Marriage Proposal", description="{!}None")


obtain_liege_blessing = Quest("obtain_liege_blessing", name="Formal Marriage Proposal", description="{!}None")


wed_betrothed = Quest("wed_betrothed", name="Wed Your Betrothed", description="{!}None")


wed_betrothed_female = Quest("wed_betrothed_female", name="Wed Your Betrothed", description="{!}None")


join_faction = Quest("join_faction", name="Give Oath of Homage to {s1}", description="{!}Find {s1} and give him your oath of homage.")


rebel_against_kingdom = Quest("rebel_against_kingdom", name="Help {s13} Claim the Throne of {s14}", description="{!}None")


consult_with_minister = Quest("consult_with_minister", name="Consult With Minister", description="{!}Consult your minister, {s11}, currently at {s12}")


organize_feast = Quest("organize_feast", name="Organize Feast", description="{!}Bring goods for a feast to your spouse {s11}, currently at {s12}")


resolve_dispute = Quest("resolve_dispute", name="Resolve Dispute", description="{!}Resolve the dispute between {s11} and {s12}")


offer_gift = Quest("offer_gift", name="Procure Gift", description="{!}Give {s10} a gift to provide to {reg4?her:his} {s11}, {s12}")


denounce_lord = Quest("denounce_lord", name="Denounce Lord", description="{!}Denounce {s11} in Public")


intrigue_against_lord = Quest("intrigue_against_lord", name="Intrigue against Lord", description="{!}Criticize {s11} in Private")


track_down_bandits = Quest("track_down_bandits", name="Track Down Bandits", description="{!}{s9} of {s4} asked you to track down {s6}, who attacked travellers on the roads near town.")


track_down_provocateurs = Quest("track_down_provocateurs", name="Track Down Provocateurs", description="{!}{s9} of {s4} asked you to track down a group of thugs, hired to create a border incident between {s5} and {s6}.")


retaliate_for_border_incident = Quest("retaliate_for_border_incident", name="Retaliate for a Border Incident", description="{!}{s9} of {s4} asked you to defeat {s5} of the {s7} in battle, defusing tension in the {s8} to go to war.")


raid_caravan_to_start_war = Quest("raid_caravan_to_start_war", name="Attack a Neutral Caravan to Provoke War", description="{!}placeholder")


cause_provocation = Quest("cause_provocation", name="Give a Kingdom Provocation to Attack Another", description="{!}placeholder")


rescue_prisoner = Quest("rescue_prisoner", name="Rescue or Ransom a Prisoner", description="{!}placeholder")


destroy_bandit_lair = Quest("destroy_bandit_lair", name="Destroy Bandit Lair", description="{!}{s9} of {s4} asked you to discover a {s6} and destroy it.")


blank_quest_2 = Quest("blank_quest_2", name="{!}blank quest", description="{!}placeholder")


blank_quest_3 = Quest("blank_quest_3", name="{!}blank quest", description="{!}placeholder")


blank_quest_4 = Quest("blank_quest_4", name="{!}blank quest", description="{!}placeholder")


blank_quest_5 = Quest("blank_quest_5", name="{!}blank quest", description="{!}placeholder")


blank_quest_6 = Quest("blank_quest_6", name="{!}blank quest", description="{!}placeholder")


blank_quest_7 = Quest("blank_quest_7", name="{!}blank quest", description="{!}placeholder")


blank_quest_8 = Quest("blank_quest_8", name="{!}blank quest", description="{!}placeholder")


blank_quest_9 = Quest("blank_quest_9", name="{!}blank quest", description="{!}placeholder")


blank_quest_10 = Quest("blank_quest_10", name="{!}blank quest", description="{!}placeholder")


blank_quest_11 = Quest("blank_quest_11", name="{!}blank quest", description="{!}placeholder")


blank_quest_12 = Quest("blank_quest_12", name="{!}blank quest", description="{!}placeholder")


blank_quest_13 = Quest("blank_quest_13", name="{!}blank quest", description="{!}placeholder")


blank_quest_14 = Quest("blank_quest_14", name="{!}blank quest", description="{!}placeholder")


blank_quest_15 = Quest("blank_quest_15", name="{!}blank quest", description="{!}placeholder")


blank_quest_16 = Quest("blank_quest_16", name="{!}blank quest", description="{!}placeholder")


blank_quest_17 = Quest("blank_quest_17", name="{!}blank quest", description="{!}placeholder")


blank_quest_18 = Quest("blank_quest_18", name="{!}blank quest", description="{!}placeholder")


blank_quest_19 = Quest("blank_quest_19", name="{!}blank quest", description="{!}placeholder")


blank_quest_20 = Quest("blank_quest_20", name="{!}blank quest", description="{!}placeholder")


blank_quest_21 = Quest("blank_quest_21", name="{!}blank quest", description="{!}placeholder")


blank_quest_22 = Quest("blank_quest_22", name="{!}blank quest", description="{!}placeholder")


blank_quest_23 = Quest("blank_quest_23", name="{!}blank quest", description="{!}placeholder")


blank_quest_24 = Quest("blank_quest_24", name="{!}blank quest", description="{!}placeholder")


blank_quest_25 = Quest("blank_quest_25", name="{!}blank quest", description="{!}placeholder")


blank_quest_26 = Quest("blank_quest_26", name="{!}blank quest", description="{!}placeholder")


blank_quest_27 = Quest("blank_quest_27", name="{!}blank quest", description="{!}placeholder")


collect_men = Quest("collect_men", name="Collect Five Men", description="{!}{s9} asked you to collect at least 5 men before you move against the bandits threatening the townsmen. You can recruit soldiers from villages as well as town taverns. You can find {s9} at the tavern in {s4} when you have think you have enough men.", is_random=False)


learn_where_merchant_brother_is = Quest("learn_where_merchant_brother_is", name="Learn Where the Hostages are Held.", description="{!}placeholder.", is_random=False)


save_relative_of_merchant = Quest("save_relative_of_merchant", name="Attack the Bandit Lair", description="{!}placeholder.", is_random=False)


save_town_from_bandits = Quest("save_town_from_bandits", name="Save Town from Bandits", description="{!}placeholder.", is_random=False)


quests_end = Quest("quests_end", name="Quests End", description="{!}.", is_random=False)


