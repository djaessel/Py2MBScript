# This Python file uses the following encoding: utf-8

from MBParty import MBParty, PartyFlag
import map_icons as icon
import factions as fac
import troops as trp


main_party = MBParty("main_party", name="Main Party", faction=fac.player_faction, initial_cords=(17.0, 52.5))
main_party.add_flag(PartyFlag.LABEL_SMALL)
main_party.add_flag(PartyFlag.LIMIT_MEMBERS)
main_party.add_members(trp.player, 1)


temp_party = MBParty("temp_party", name="{!}temp party", faction=fac.commoners)
temp_party.add_flag(PartyFlag.IS_DISABLED)
temp_party.add_flag(PartyFlag.LABEL_SMALL)


camp_bandits = MBParty("camp_bandits", name="{!}camp bandits", faction=fac.outlaws, initial_cords=(1.0, 1.0))
camp_bandits.add_flag(PartyFlag.IS_DISABLED)
camp_bandits.add_flag(PartyFlag.LABEL_SMALL)
camp_bandits.add_members(trp.temp_troop, 3)


###################################################################
# Parties above this point are hardwired/hardcoded into the game! #
###################################################################


temp_party_2 = MBParty("temp_party_2", name="{!}temp party 2", faction=fac.commoners)
temp_party_2.add_flag(PartyFlag.IS_DISABLED)
temp_party_2.add_flag(PartyFlag.LABEL_SMALL)


temp_casualties = MBParty("temp_casualties", name="{!}casualties", faction=fac.neutral, initial_cords=(1.0, 1.0))
temp_casualties.add_flag(PartyFlag.IS_DISABLED)
temp_casualties.add_flag(PartyFlag.LABEL_SMALL)


temp_casualties_2 = MBParty("temp_casualties_2", name="{!}casualties", faction=fac.neutral, initial_cords=(1.0, 1.0))
temp_casualties_2.add_flag(PartyFlag.IS_DISABLED)
temp_casualties_2.add_flag(PartyFlag.LABEL_SMALL)


temp_casualties_3 = MBParty("temp_casualties_3", name="{!}casualties", faction=fac.neutral, initial_cords=(1.0, 1.0))
temp_casualties_3.add_flag(PartyFlag.IS_DISABLED)
temp_casualties_3.add_flag(PartyFlag.LABEL_SMALL)


temp_wounded = MBParty("temp_wounded", name="{!}enemies wounded", faction=fac.neutral, initial_cords=(1.0, 1.0))
temp_wounded.add_flag(PartyFlag.IS_DISABLED)
temp_wounded.add_flag(PartyFlag.LABEL_SMALL)


temp_killed = MBParty("temp_killed", name="{!}enemies killed", faction=fac.neutral, initial_cords=(1.0, 1.0))
temp_killed.add_flag(PartyFlag.IS_DISABLED)
temp_killed.add_flag(PartyFlag.LABEL_SMALL)


main_party_backup = MBParty("main_party_backup", name="{!} ", faction=fac.neutral, initial_cords=(1.0, 1.0))
main_party_backup.add_flag(PartyFlag.IS_DISABLED)
main_party_backup.add_flag(PartyFlag.LABEL_SMALL)


encountered_party_backup = MBParty("encountered_party_backup", name="{!} ", faction=fac.neutral, initial_cords=(1.0, 1.0))
encountered_party_backup.add_flag(PartyFlag.IS_DISABLED)
encountered_party_backup.add_flag(PartyFlag.LABEL_SMALL)


collective_friends_backup = MBParty("collective_friends_backup", name="{!} ", faction=fac.neutral, initial_cords=(1.0, 1.0))
collective_friends_backup.add_flag(PartyFlag.IS_DISABLED)
collective_friends_backup.add_flag(PartyFlag.LABEL_SMALL)


player_casualties = MBParty("player_casualties", name="{!} ", faction=fac.neutral, initial_cords=(1.0, 1.0))
player_casualties.add_flag(PartyFlag.IS_DISABLED)
player_casualties.add_flag(PartyFlag.LABEL_SMALL)


enemy_casualties = MBParty("enemy_casualties", name="{!} ", faction=fac.neutral, initial_cords=(1.0, 1.0))
enemy_casualties.add_flag(PartyFlag.IS_DISABLED)
enemy_casualties.add_flag(PartyFlag.LABEL_SMALL)


ally_casualties = MBParty("ally_casualties", name="{!} ", faction=fac.neutral, initial_cords=(1.0, 1.0))
ally_casualties.add_flag(PartyFlag.IS_DISABLED)
ally_casualties.add_flag(PartyFlag.LABEL_SMALL)


collective_enemy = MBParty("collective_enemy", name="{!}collective enemy", faction=fac.neutral, initial_cords=(1.0, 1.0))
collective_enemy.add_flag(PartyFlag.IS_DISABLED)
collective_enemy.add_flag(PartyFlag.LABEL_SMALL)


collective_ally = MBParty("collective_ally", name="{!}collective ally", faction=fac.neutral, initial_cords=(1.0, 1.0))
collective_ally.add_flag(PartyFlag.IS_DISABLED)
collective_ally.add_flag(PartyFlag.LABEL_SMALL)


collective_friends = MBParty("collective_friends", name="{!}collective ally", faction=fac.neutral, initial_cords=(1.0, 1.0))
collective_friends.add_flag(PartyFlag.IS_DISABLED)
collective_friends.add_flag(PartyFlag.LABEL_SMALL)


total_enemy_casualties = MBParty("total_enemy_casualties", name="{!} ", faction=fac.neutral, initial_cords=(1.0, 1.0))
total_enemy_casualties.add_flag(PartyFlag.IS_DISABLED)
total_enemy_casualties.add_flag(PartyFlag.LABEL_SMALL)


routed_enemies = MBParty("routed_enemies", name="{!}routed enemies", faction=fac.neutral, initial_cords=(1.0, 1.0))
routed_enemies.add_flag(PartyFlag.IS_DISABLED)
routed_enemies.add_flag(PartyFlag.LABEL_SMALL)


zendar = MBParty("zendar", name="Zendar", faction=fac.neutral, initial_cords=(18.0, 60.0))
zendar.add_flag(PartyFlag.IS_DISABLED)
zendar.add_flag(PartyFlag.IS_STATIC)
zendar.add_flag(PartyFlag.LABEL_SMALL)
zendar.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
zendar.add_flag(PartyFlag.HIDE_DEFENDERS)
zendar.set_icon(icon.town)


town_1 = MBParty("town_1", name="Sargoth", faction=fac.neutral, initial_cords=(-17.6, 79.7), direction=170.0)
town_1.add_flag(PartyFlag.IS_STATIC)
town_1.add_flag(PartyFlag.LABEL_SMALL)
town_1.add_flag(PartyFlag.LABEL_LARGE)
town_1.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_1.add_flag(PartyFlag.SHOW_FACTION)
town_1.set_icon(icon.town)


town_2 = MBParty("town_2", name="Tihr", faction=fac.neutral, initial_cords=(-53.5, 78.4), direction=120.0)
town_2.add_flag(PartyFlag.IS_STATIC)
town_2.add_flag(PartyFlag.LABEL_SMALL)
town_2.add_flag(PartyFlag.LABEL_LARGE)
town_2.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_2.add_flag(PartyFlag.SHOW_FACTION)
town_2.set_icon(icon.town)


town_3 = MBParty("town_3", name="Veluca", faction=fac.neutral, initial_cords=(-57.4, -44.5), direction=80.0)
town_3.add_flag(PartyFlag.IS_STATIC)
town_3.add_flag(PartyFlag.LABEL_SMALL)
town_3.add_flag(PartyFlag.LABEL_LARGE)
town_3.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_3.add_flag(PartyFlag.SHOW_FACTION)
town_3.set_icon(icon.town)


town_4 = MBParty("town_4", name="Suno", faction=fac.neutral, initial_cords=(-70.0, 15.4), direction=290.0)
town_4.add_flag(PartyFlag.IS_STATIC)
town_4.add_flag(PartyFlag.LABEL_SMALL)
town_4.add_flag(PartyFlag.LABEL_LARGE)
town_4.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_4.add_flag(PartyFlag.SHOW_FACTION)
town_4.set_icon(icon.town)


town_5 = MBParty("town_5", name="Jelkala", faction=fac.neutral, initial_cords=(-74.6, -79.7), direction=90.0)
town_5.add_flag(PartyFlag.IS_STATIC)
town_5.add_flag(PartyFlag.LABEL_SMALL)
town_5.add_flag(PartyFlag.LABEL_LARGE)
town_5.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_5.add_flag(PartyFlag.SHOW_FACTION)
town_5.set_icon(icon.town)


town_6 = MBParty("town_6", name="Praven", faction=fac.neutral, initial_cords=(-96.0, 26.4), direction=155.0)
town_6.add_flag(PartyFlag.IS_STATIC)
town_6.add_flag(PartyFlag.LABEL_SMALL)
town_6.add_flag(PartyFlag.LABEL_LARGE)
town_6.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_6.add_flag(PartyFlag.SHOW_FACTION)
town_6.set_icon(icon.town)


town_7 = MBParty("town_7", name="Uxkhal", faction=fac.neutral, initial_cords=(-50.0, -8.5), direction=240.0)
town_7.add_flag(PartyFlag.IS_STATIC)
town_7.add_flag(PartyFlag.LABEL_SMALL)
town_7.add_flag(PartyFlag.LABEL_LARGE)
town_7.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_7.add_flag(PartyFlag.SHOW_FACTION)
town_7.set_icon(icon.town)


town_8 = MBParty("town_8", name="Reyvadin", faction=fac.neutral, initial_cords=(48.44, 39.3), direction=175.0)
town_8.add_flag(PartyFlag.IS_STATIC)
town_8.add_flag(PartyFlag.LABEL_SMALL)
town_8.add_flag(PartyFlag.LABEL_LARGE)
town_8.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_8.add_flag(PartyFlag.SHOW_FACTION)
town_8.set_icon(icon.town)


town_9 = MBParty("town_9", name="Khudan", faction=fac.neutral, initial_cords=(94.0, 65.2), direction=90.0)
town_9.add_flag(PartyFlag.IS_STATIC)
town_9.add_flag(PartyFlag.LABEL_SMALL)
town_9.add_flag(PartyFlag.LABEL_LARGE)
town_9.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_9.add_flag(PartyFlag.SHOW_FACTION)
town_9.set_icon(icon.town_snow)


town_10 = MBParty("town_10", name="Tulga", faction=fac.neutral, initial_cords=(135.5, -22.0), direction=310.0)
town_10.add_flag(PartyFlag.IS_STATIC)
town_10.add_flag(PartyFlag.LABEL_SMALL)
town_10.add_flag(PartyFlag.LABEL_LARGE)
town_10.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_10.add_flag(PartyFlag.SHOW_FACTION)
town_10.set_icon(icon.town_steppe)


town_11 = MBParty("town_11", name="Curaw", faction=fac.neutral, initial_cords=(43.0, 67.5), direction=150.0)
town_11.add_flag(PartyFlag.IS_STATIC)
town_11.add_flag(PartyFlag.LABEL_SMALL)
town_11.add_flag(PartyFlag.LABEL_LARGE)
town_11.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_11.add_flag(PartyFlag.SHOW_FACTION)
town_11.set_icon(icon.town_snow)


town_12 = MBParty("town_12", name="Wercheg", faction=fac.neutral, initial_cords=(-1.2, 108.9), direction=25.0)
town_12.add_flag(PartyFlag.IS_STATIC)
town_12.add_flag(PartyFlag.LABEL_SMALL)
town_12.add_flag(PartyFlag.LABEL_LARGE)
town_12.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_12.add_flag(PartyFlag.SHOW_FACTION)
town_12.set_icon(icon.town)


town_13 = MBParty("town_13", name="Rivacheg", faction=fac.neutral, initial_cords=(64.8, 113.7), direction=60.0)
town_13.add_flag(PartyFlag.IS_STATIC)
town_13.add_flag(PartyFlag.LABEL_SMALL)
town_13.add_flag(PartyFlag.LABEL_LARGE)
town_13.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_13.add_flag(PartyFlag.SHOW_FACTION)
town_13.set_icon(icon.town)


town_14 = MBParty("town_14", name="Halmar", faction=fac.neutral, initial_cords=(55.5, -45.0), direction=135.0)
town_14.add_flag(PartyFlag.IS_STATIC)
town_14.add_flag(PartyFlag.LABEL_SMALL)
town_14.add_flag(PartyFlag.LABEL_LARGE)
town_14.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_14.add_flag(PartyFlag.SHOW_FACTION)
town_14.set_icon(icon.town_steppe)


town_15 = MBParty("town_15", name="Yalen", faction=fac.neutral, initial_cords=(-132.8, -47.3), direction=45.0)
town_15.add_flag(PartyFlag.IS_STATIC)
town_15.add_flag(PartyFlag.LABEL_SMALL)
town_15.add_flag(PartyFlag.LABEL_LARGE)
town_15.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_15.add_flag(PartyFlag.SHOW_FACTION)
town_15.set_icon(icon.town)


town_16 = MBParty("town_16", name="Dhirim", faction=fac.neutral, initial_cords=(14.0, -2.0))
town_16.add_flag(PartyFlag.IS_STATIC)
town_16.add_flag(PartyFlag.LABEL_SMALL)
town_16.add_flag(PartyFlag.LABEL_LARGE)
town_16.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_16.add_flag(PartyFlag.SHOW_FACTION)
town_16.set_icon(icon.town)


town_17 = MBParty("town_17", name="Ichamur", faction=fac.neutral, initial_cords=(121.8, 8.6), direction=90.0)
town_17.add_flag(PartyFlag.IS_STATIC)
town_17.add_flag(PartyFlag.LABEL_SMALL)
town_17.add_flag(PartyFlag.LABEL_LARGE)
town_17.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_17.add_flag(PartyFlag.SHOW_FACTION)
town_17.set_icon(icon.town_steppe)


town_18 = MBParty("town_18", name="Narra", faction=fac.neutral, initial_cords=(88.0, -26.5), direction=135.0)
town_18.add_flag(PartyFlag.IS_STATIC)
town_18.add_flag(PartyFlag.LABEL_SMALL)
town_18.add_flag(PartyFlag.LABEL_LARGE)
town_18.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_18.add_flag(PartyFlag.SHOW_FACTION)
town_18.set_icon(icon.town_steppe)


town_19 = MBParty("town_19", name="Shariz", faction=fac.neutral, initial_cords=(15.0, -107.0), direction=45.0)
town_19.add_flag(PartyFlag.IS_STATIC)
town_19.add_flag(PartyFlag.LABEL_SMALL)
town_19.add_flag(PartyFlag.LABEL_LARGE)
town_19.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_19.add_flag(PartyFlag.SHOW_FACTION)
town_19.set_icon(icon.town_desert)


town_20 = MBParty("town_20", name="Durquba", faction=fac.neutral, initial_cords=(90.0, -95.1), direction=270.0)
town_20.add_flag(PartyFlag.IS_STATIC)
town_20.add_flag(PartyFlag.LABEL_SMALL)
town_20.add_flag(PartyFlag.LABEL_LARGE)
town_20.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_20.add_flag(PartyFlag.SHOW_FACTION)
town_20.set_icon(icon.town_desert)


town_21 = MBParty("town_21", name="Ahmerrad", faction=fac.neutral, initial_cords=(130.5, -78.5), direction=330.0)
town_21.add_flag(PartyFlag.IS_STATIC)
town_21.add_flag(PartyFlag.LABEL_SMALL)
town_21.add_flag(PartyFlag.LABEL_LARGE)
town_21.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_21.add_flag(PartyFlag.SHOW_FACTION)
town_21.set_icon(icon.town_desert)


town_22 = MBParty("town_22", name="Bariyye", faction=fac.neutral, initial_cords=(165.0, -106.7), direction=225.0)
town_22.add_flag(PartyFlag.IS_STATIC)
town_22.add_flag(PartyFlag.LABEL_SMALL)
town_22.add_flag(PartyFlag.LABEL_LARGE)
town_22.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
town_22.add_flag(PartyFlag.SHOW_FACTION)
town_22.set_icon(icon.town_desert)


castle_1 = MBParty("castle_1", name="Culmarr Castle", faction=fac.neutral, initial_cords=(-101.3, -21.0), direction=50.0)
castle_1.add_flag(PartyFlag.IS_STATIC)
castle_1.add_flag(PartyFlag.LABEL_SMALL)
castle_1.add_flag(PartyFlag.LABEL_MEDIUM)
castle_1.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_1.add_flag(PartyFlag.SHOW_FACTION)
castle_1.set_icon(icon.castle_a)


castle_2 = MBParty("castle_2", name="Malayurg Castle", faction=fac.neutral, initial_cords=(97.5, -2.2), direction=75.0)
castle_2.add_flag(PartyFlag.IS_STATIC)
castle_2.add_flag(PartyFlag.LABEL_SMALL)
castle_2.add_flag(PartyFlag.LABEL_MEDIUM)
castle_2.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_2.add_flag(PartyFlag.SHOW_FACTION)
castle_2.set_icon(icon.castle_b)


castle_3 = MBParty("castle_3", name="Bulugha Castle", faction=fac.neutral, initial_cords=(47.5, 111.3), direction=100.0)
castle_3.add_flag(PartyFlag.IS_STATIC)
castle_3.add_flag(PartyFlag.LABEL_SMALL)
castle_3.add_flag(PartyFlag.LABEL_MEDIUM)
castle_3.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_3.add_flag(PartyFlag.SHOW_FACTION)
castle_3.set_icon(icon.castle_a)


castle_4 = MBParty("castle_4", name="Radoghir Castle", faction=fac.neutral, initial_cords=(32.5, 47.8), direction=180.0)
castle_4.add_flag(PartyFlag.IS_STATIC)
castle_4.add_flag(PartyFlag.LABEL_SMALL)
castle_4.add_flag(PartyFlag.LABEL_MEDIUM)
castle_4.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_4.add_flag(PartyFlag.SHOW_FACTION)
castle_4.set_icon(icon.castle_c)


castle_5 = MBParty("castle_5", name="Tehlrog Castle", faction=fac.neutral, initial_cords=(-4.8, 63.7), direction=90.0)
castle_5.add_flag(PartyFlag.IS_STATIC)
castle_5.add_flag(PartyFlag.LABEL_SMALL)
castle_5.add_flag(PartyFlag.LABEL_MEDIUM)
castle_5.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_5.add_flag(PartyFlag.SHOW_FACTION)
castle_5.set_icon(icon.castle_c)


castle_6 = MBParty("castle_6", name="Tilbaut Castle", faction=fac.neutral, initial_cords=(37.6, 17.1), direction=55.0)
castle_6.add_flag(PartyFlag.IS_STATIC)
castle_6.add_flag(PartyFlag.LABEL_SMALL)
castle_6.add_flag(PartyFlag.LABEL_MEDIUM)
castle_6.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_6.add_flag(PartyFlag.SHOW_FACTION)
castle_6.set_icon(icon.castle_a)


castle_7 = MBParty("castle_7", name="Sungetche Castle", faction=fac.neutral, initial_cords=(109.5, 41.5), direction=45.0)
castle_7.add_flag(PartyFlag.IS_STATIC)
castle_7.add_flag(PartyFlag.LABEL_SMALL)
castle_7.add_flag(PartyFlag.LABEL_MEDIUM)
castle_7.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_7.add_flag(PartyFlag.SHOW_FACTION)
castle_7.set_icon(icon.castle_snow_a)


castle_8 = MBParty("castle_8", name="Jeirbe Castle", faction=fac.neutral, initial_cords=(35.2, 89.0), direction=30.0)
castle_8.add_flag(PartyFlag.IS_STATIC)
castle_8.add_flag(PartyFlag.LABEL_SMALL)
castle_8.add_flag(PartyFlag.LABEL_MEDIUM)
castle_8.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_8.add_flag(PartyFlag.SHOW_FACTION)
castle_8.set_icon(icon.castle_a)


castle_9 = MBParty("castle_9", name="Jamiche Castle", faction=fac.neutral, initial_cords=(-7.5, -82.6), direction=100.0)
castle_9.add_flag(PartyFlag.IS_STATIC)
castle_9.add_flag(PartyFlag.LABEL_SMALL)
castle_9.add_flag(PartyFlag.LABEL_MEDIUM)
castle_9.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_9.add_flag(PartyFlag.SHOW_FACTION)
castle_9.set_icon(icon.castle_a)


castle_10 = MBParty("castle_10", name="Alburq Castle", faction=fac.neutral, initial_cords=(24.2, 96.85), direction=110.0)
castle_10.add_flag(PartyFlag.IS_STATIC)
castle_10.add_flag(PartyFlag.LABEL_SMALL)
castle_10.add_flag(PartyFlag.LABEL_MEDIUM)
castle_10.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_10.add_flag(PartyFlag.SHOW_FACTION)
castle_10.set_icon(icon.castle_a)


castle_11 = MBParty("castle_11", name="Curin Castle", faction=fac.neutral, initial_cords=(-27.5, 83.46), direction=75.0)
castle_11.add_flag(PartyFlag.IS_STATIC)
castle_11.add_flag(PartyFlag.LABEL_SMALL)
castle_11.add_flag(PartyFlag.LABEL_MEDIUM)
castle_11.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_11.add_flag(PartyFlag.SHOW_FACTION)
castle_11.set_icon(icon.castle_a)


castle_12 = MBParty("castle_12", name="Chalbek Castle", faction=fac.neutral, initial_cords=(-84.75, 105.5), direction=95.0)
castle_12.add_flag(PartyFlag.IS_STATIC)
castle_12.add_flag(PartyFlag.LABEL_SMALL)
castle_12.add_flag(PartyFlag.LABEL_MEDIUM)
castle_12.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_12.add_flag(PartyFlag.SHOW_FACTION)
castle_12.set_icon(icon.castle_b)


castle_13 = MBParty("castle_13", name="Kelredan Castle", faction=fac.neutral, initial_cords=(-10.6, 17.6), direction=115.0)
castle_13.add_flag(PartyFlag.IS_STATIC)
castle_13.add_flag(PartyFlag.LABEL_SMALL)
castle_13.add_flag(PartyFlag.LABEL_MEDIUM)
castle_13.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_13.add_flag(PartyFlag.SHOW_FACTION)
castle_13.set_icon(icon.castle_a)


castle_14 = MBParty("castle_14", name="Maras Castle", faction=fac.neutral, initial_cords=(-122.4, -18.1), direction=90.0)
castle_14.add_flag(PartyFlag.IS_STATIC)
castle_14.add_flag(PartyFlag.LABEL_SMALL)
castle_14.add_flag(PartyFlag.LABEL_MEDIUM)
castle_14.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_14.add_flag(PartyFlag.SHOW_FACTION)
castle_14.set_icon(icon.castle_c)


castle_15 = MBParty("castle_15", name="Ergellon Castle", faction=fac.neutral, initial_cords=(-52.5, -28.0), direction=235.0)
castle_15.add_flag(PartyFlag.IS_STATIC)
castle_15.add_flag(PartyFlag.LABEL_SMALL)
castle_15.add_flag(PartyFlag.LABEL_MEDIUM)
castle_15.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_15.add_flag(PartyFlag.SHOW_FACTION)
castle_15.set_icon(icon.castle_a)


castle_16 = MBParty("castle_16", name="Almerra Castle", faction=fac.neutral, initial_cords=(-10.6, -65.6), direction=45.0)
castle_16.add_flag(PartyFlag.IS_STATIC)
castle_16.add_flag(PartyFlag.LABEL_SMALL)
castle_16.add_flag(PartyFlag.LABEL_MEDIUM)
castle_16.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_16.add_flag(PartyFlag.SHOW_FACTION)
castle_16.set_icon(icon.castle_c)


castle_17 = MBParty("castle_17", name="Distar Castle", faction=fac.neutral, initial_cords=(140.3, -10.8), direction=15.0)
castle_17.add_flag(PartyFlag.IS_STATIC)
castle_17.add_flag(PartyFlag.LABEL_SMALL)
castle_17.add_flag(PartyFlag.LABEL_MEDIUM)
castle_17.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_17.add_flag(PartyFlag.SHOW_FACTION)
castle_17.set_icon(icon.castle_a)


castle_18 = MBParty("castle_18", name="Ismirala Castle", faction=fac.neutral, initial_cords=(14.4, 70.1), direction=300.0)
castle_18.add_flag(PartyFlag.IS_STATIC)
castle_18.add_flag(PartyFlag.LABEL_SMALL)
castle_18.add_flag(PartyFlag.LABEL_MEDIUM)
castle_18.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_18.add_flag(PartyFlag.SHOW_FACTION)
castle_18.set_icon(icon.castle_snow_a)


castle_19 = MBParty("castle_19", name="Yruma Castle", faction=fac.neutral, initial_cords=(69.5, 55.6), direction=280.0)
castle_19.add_flag(PartyFlag.IS_STATIC)
castle_19.add_flag(PartyFlag.LABEL_SMALL)
castle_19.add_flag(PartyFlag.LABEL_MEDIUM)
castle_19.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_19.add_flag(PartyFlag.SHOW_FACTION)
castle_19.set_icon(icon.castle_snow_a)


castle_20 = MBParty("castle_20", name="Derchios Castle", faction=fac.neutral, initial_cords=(16.0, 11.5), direction=260.0)
castle_20.add_flag(PartyFlag.IS_STATIC)
castle_20.add_flag(PartyFlag.LABEL_SMALL)
castle_20.add_flag(PartyFlag.LABEL_MEDIUM)
castle_20.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_20.add_flag(PartyFlag.SHOW_FACTION)
castle_20.set_icon(icon.castle_a)


castle_21 = MBParty("castle_21", name="Ibdeles Castle", faction=fac.neutral, initial_cords=(-73.0, -89.5), direction=260.0)
castle_21.add_flag(PartyFlag.IS_STATIC)
castle_21.add_flag(PartyFlag.LABEL_SMALL)
castle_21.add_flag(PartyFlag.LABEL_MEDIUM)
castle_21.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_21.add_flag(PartyFlag.SHOW_FACTION)
castle_21.set_icon(icon.castle_a)


castle_22 = MBParty("castle_22", name="Unuzdaq Castle", faction=fac.neutral, initial_cords=(33.0, -64.0), direction=260.0)
castle_22.add_flag(PartyFlag.IS_STATIC)
castle_22.add_flag(PartyFlag.LABEL_SMALL)
castle_22.add_flag(PartyFlag.LABEL_MEDIUM)
castle_22.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_22.add_flag(PartyFlag.SHOW_FACTION)
castle_22.set_icon(icon.castle_a)


castle_23 = MBParty("castle_23", name="Tevarin Castle", faction=fac.neutral, initial_cords=(-124.8, 44.3), direction=80.0)
castle_23.add_flag(PartyFlag.IS_STATIC)
castle_23.add_flag(PartyFlag.LABEL_SMALL)
castle_23.add_flag(PartyFlag.LABEL_MEDIUM)
castle_23.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_23.add_flag(PartyFlag.SHOW_FACTION)
castle_23.set_icon(icon.castle_a)


castle_24 = MBParty("castle_24", name="Reindi Castle", faction=fac.neutral, initial_cords=(24.9, -35.6), direction=260.0)
castle_24.add_flag(PartyFlag.IS_STATIC)
castle_24.add_flag(PartyFlag.LABEL_SMALL)
castle_24.add_flag(PartyFlag.LABEL_MEDIUM)
castle_24.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_24.add_flag(PartyFlag.SHOW_FACTION)
castle_24.set_icon(icon.castle_a)


castle_25 = MBParty("castle_25", name="Ryibelet Castle", faction=fac.neutral, initial_cords=(-57.0, 30.6), direction=260.0)
castle_25.add_flag(PartyFlag.IS_STATIC)
castle_25.add_flag(PartyFlag.LABEL_SMALL)
castle_25.add_flag(PartyFlag.LABEL_MEDIUM)
castle_25.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_25.add_flag(PartyFlag.SHOW_FACTION)
castle_25.set_icon(icon.castle_a)


castle_26 = MBParty("castle_26", name="Senuzgda Castle", faction=fac.neutral, initial_cords=(-2.5, -9.5), direction=260.0)
castle_26.add_flag(PartyFlag.IS_STATIC)
castle_26.add_flag(PartyFlag.LABEL_SMALL)
castle_26.add_flag(PartyFlag.LABEL_MEDIUM)
castle_26.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_26.add_flag(PartyFlag.SHOW_FACTION)
castle_26.set_icon(icon.castle_a)


castle_27 = MBParty("castle_27", name="Rindyar Castle", faction=fac.neutral, initial_cords=(63.3, -2.0), direction=260.0)
castle_27.add_flag(PartyFlag.IS_STATIC)
castle_27.add_flag(PartyFlag.LABEL_SMALL)
castle_27.add_flag(PartyFlag.LABEL_MEDIUM)
castle_27.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_27.add_flag(PartyFlag.SHOW_FACTION)
castle_27.set_icon(icon.castle_a)


castle_28 = MBParty("castle_28", name="Grunwalder Castle", faction=fac.neutral, initial_cords=(-36.4, -39.3), direction=260.0)
castle_28.add_flag(PartyFlag.IS_STATIC)
castle_28.add_flag(PartyFlag.LABEL_SMALL)
castle_28.add_flag(PartyFlag.LABEL_MEDIUM)
castle_28.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_28.add_flag(PartyFlag.SHOW_FACTION)
castle_28.set_icon(icon.castle_a)


castle_29 = MBParty("castle_29", name="Nelag Castle", faction=fac.neutral, initial_cords=(147.7, 50.4), direction=280.0)
castle_29.add_flag(PartyFlag.IS_STATIC)
castle_29.add_flag(PartyFlag.LABEL_SMALL)
castle_29.add_flag(PartyFlag.LABEL_MEDIUM)
castle_29.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_29.add_flag(PartyFlag.SHOW_FACTION)
castle_29.set_icon(icon.castle_snow_a)


castle_30 = MBParty("castle_30", name="Asugan Castle", faction=fac.neutral, initial_cords=(176.0, -47.0), direction=260.0)
castle_30.add_flag(PartyFlag.IS_STATIC)
castle_30.add_flag(PartyFlag.LABEL_SMALL)
castle_30.add_flag(PartyFlag.LABEL_MEDIUM)
castle_30.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_30.add_flag(PartyFlag.SHOW_FACTION)
castle_30.set_icon(icon.castle_d)


castle_31 = MBParty("castle_31", name="Vyincourd Castle", faction=fac.neutral, initial_cords=(-65.7, -12.5), direction=260.0)
castle_31.add_flag(PartyFlag.IS_STATIC)
castle_31.add_flag(PartyFlag.LABEL_SMALL)
castle_31.add_flag(PartyFlag.LABEL_MEDIUM)
castle_31.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_31.add_flag(PartyFlag.SHOW_FACTION)
castle_31.set_icon(icon.castle_a)


castle_32 = MBParty("castle_32", name="Knudarr Castle", faction=fac.neutral, initial_cords=(2.0, 30.1), direction=260.0)
castle_32.add_flag(PartyFlag.IS_STATIC)
castle_32.add_flag(PartyFlag.LABEL_SMALL)
castle_32.add_flag(PartyFlag.LABEL_MEDIUM)
castle_32.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_32.add_flag(PartyFlag.SHOW_FACTION)
castle_32.set_icon(icon.castle_a)


castle_33 = MBParty("castle_33", name="Etrosq Castle", faction=fac.neutral, initial_cords=(-101.4, -32.1), direction=80.0)
castle_33.add_flag(PartyFlag.IS_STATIC)
castle_33.add_flag(PartyFlag.LABEL_SMALL)
castle_33.add_flag(PartyFlag.LABEL_MEDIUM)
castle_33.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_33.add_flag(PartyFlag.SHOW_FACTION)
castle_33.set_icon(icon.castle_a)


castle_34 = MBParty("castle_34", name="Hrus Castle", faction=fac.neutral, initial_cords=(-72.5, 78.6), direction=260.0)
castle_34.add_flag(PartyFlag.IS_STATIC)
castle_34.add_flag(PartyFlag.LABEL_SMALL)
castle_34.add_flag(PartyFlag.LABEL_MEDIUM)
castle_34.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_34.add_flag(PartyFlag.SHOW_FACTION)
castle_34.set_icon(icon.castle_a)


castle_35 = MBParty("castle_35", name="Haringoth Castle", faction=fac.neutral, initial_cords=(-110.0, 0.0), direction=260.0)
castle_35.add_flag(PartyFlag.IS_STATIC)
castle_35.add_flag(PartyFlag.LABEL_SMALL)
castle_35.add_flag(PartyFlag.LABEL_MEDIUM)
castle_35.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_35.add_flag(PartyFlag.SHOW_FACTION)
castle_35.set_icon(icon.castle_a)


castle_36 = MBParty("castle_36", name="Jelbegi Castle", faction=fac.neutral, initial_cords=(-47.3, 53.2), direction=260.0)
castle_36.add_flag(PartyFlag.IS_STATIC)
castle_36.add_flag(PartyFlag.LABEL_SMALL)
castle_36.add_flag(PartyFlag.LABEL_MEDIUM)
castle_36.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_36.add_flag(PartyFlag.SHOW_FACTION)
castle_36.set_icon(icon.castle_a)


castle_37 = MBParty("castle_37", name="Dramug Castle", faction=fac.neutral, initial_cords=(55.3, 23.0), direction=260.0)
castle_37.add_flag(PartyFlag.IS_STATIC)
castle_37.add_flag(PartyFlag.LABEL_SMALL)
castle_37.add_flag(PartyFlag.LABEL_MEDIUM)
castle_37.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_37.add_flag(PartyFlag.SHOW_FACTION)
castle_37.set_icon(icon.castle_c)


castle_38 = MBParty("castle_38", name="Tulbuk Castle", faction=fac.neutral, initial_cords=(141.7, 33.3), direction=260.0)
castle_38.add_flag(PartyFlag.IS_STATIC)
castle_38.add_flag(PartyFlag.LABEL_SMALL)
castle_38.add_flag(PartyFlag.LABEL_MEDIUM)
castle_38.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_38.add_flag(PartyFlag.SHOW_FACTION)
castle_38.set_icon(icon.castle_d)


castle_39 = MBParty("castle_39", name="Slezkh Castle", faction=fac.neutral, initial_cords=(56.8, 74.5), direction=280.0)
castle_39.add_flag(PartyFlag.IS_STATIC)
castle_39.add_flag(PartyFlag.LABEL_SMALL)
castle_39.add_flag(PartyFlag.LABEL_MEDIUM)
castle_39.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_39.add_flag(PartyFlag.SHOW_FACTION)
castle_39.set_icon(icon.castle_snow_a)


castle_40 = MBParty("castle_40", name="Uhhun Castle", faction=fac.neutral, initial_cords=(62.9, -26.0), direction=260.0)
castle_40.add_flag(PartyFlag.IS_STATIC)
castle_40.add_flag(PartyFlag.LABEL_SMALL)
castle_40.add_flag(PartyFlag.LABEL_MEDIUM)
castle_40.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_40.add_flag(PartyFlag.SHOW_FACTION)
castle_40.set_icon(icon.castle_d)


castle_41 = MBParty("castle_41", name="Jameyyed Castle", faction=fac.neutral, initial_cords=(71.3, -71.1), direction=260.0)
castle_41.add_flag(PartyFlag.IS_STATIC)
castle_41.add_flag(PartyFlag.LABEL_SMALL)
castle_41.add_flag(PartyFlag.LABEL_MEDIUM)
castle_41.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_41.add_flag(PartyFlag.SHOW_FACTION)
castle_41.set_icon(icon.castle_d)


castle_42 = MBParty("castle_42", name="Teramma Castle", faction=fac.neutral, initial_cords=(70.0, -96.0), direction=80.0)
castle_42.add_flag(PartyFlag.IS_STATIC)
castle_42.add_flag(PartyFlag.LABEL_SMALL)
castle_42.add_flag(PartyFlag.LABEL_MEDIUM)
castle_42.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_42.add_flag(PartyFlag.SHOW_FACTION)
castle_42.set_icon(icon.castle_d)


castle_43 = MBParty("castle_43", name="Sharwa Castle", faction=fac.neutral, initial_cords=(172.0, -65.0), direction=260.0)
castle_43.add_flag(PartyFlag.IS_STATIC)
castle_43.add_flag(PartyFlag.LABEL_SMALL)
castle_43.add_flag(PartyFlag.LABEL_MEDIUM)
castle_43.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_43.add_flag(PartyFlag.SHOW_FACTION)
castle_43.set_icon(icon.castle_d)


castle_44 = MBParty("castle_44", name="Durrin Castle", faction=fac.neutral, initial_cords=(128.0, -87.0), direction=260.0)
castle_44.add_flag(PartyFlag.IS_STATIC)
castle_44.add_flag(PartyFlag.LABEL_SMALL)
castle_44.add_flag(PartyFlag.LABEL_MEDIUM)
castle_44.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_44.add_flag(PartyFlag.SHOW_FACTION)
castle_44.set_icon(icon.castle_d)


castle_45 = MBParty("castle_45", name="Caraf Castle", faction=fac.neutral, initial_cords=(30.6, -110.6), direction=260.0)
castle_45.add_flag(PartyFlag.IS_STATIC)
castle_45.add_flag(PartyFlag.LABEL_SMALL)
castle_45.add_flag(PartyFlag.LABEL_MEDIUM)
castle_45.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_45.add_flag(PartyFlag.SHOW_FACTION)
castle_45.set_icon(icon.castle_d)


castle_46 = MBParty("castle_46", name="Weyyah Castle", faction=fac.neutral, initial_cords=(13.3, -84.4), direction=260.0)
castle_46.add_flag(PartyFlag.IS_STATIC)
castle_46.add_flag(PartyFlag.LABEL_SMALL)
castle_46.add_flag(PartyFlag.LABEL_MEDIUM)
castle_46.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_46.add_flag(PartyFlag.SHOW_FACTION)
castle_46.set_icon(icon.castle_d)


castle_47 = MBParty("castle_47", name="Samarra Castle", faction=fac.neutral, initial_cords=(116.0, -74.0), direction=260.0)
castle_47.add_flag(PartyFlag.IS_STATIC)
castle_47.add_flag(PartyFlag.LABEL_SMALL)
castle_47.add_flag(PartyFlag.LABEL_MEDIUM)
castle_47.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_47.add_flag(PartyFlag.SHOW_FACTION)
castle_47.set_icon(icon.castle_d)


castle_48 = MBParty("castle_48", name="Bardaq Castle", faction=fac.neutral, initial_cords=(157.0, -80.0), direction=260.0)
castle_48.add_flag(PartyFlag.IS_STATIC)
castle_48.add_flag(PartyFlag.LABEL_SMALL)
castle_48.add_flag(PartyFlag.LABEL_MEDIUM)
castle_48.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
castle_48.add_flag(PartyFlag.SHOW_FACTION)
castle_48.set_icon(icon.castle_d)


village_1 = MBParty("village_1", name="Yaragar", faction=fac.neutral, initial_cords=(-60.0, -9.5), direction=100.0)
village_1.add_flag(PartyFlag.IS_STATIC)
village_1.add_flag(PartyFlag.LABEL_SMALL)
village_1.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_1.add_flag(PartyFlag.HIDE_DEFENDERS)
village_1.set_icon(icon.village_a)


village_2 = MBParty("village_2", name="Burglen", faction=fac.neutral, initial_cords=(-13.5, 3.5), direction=110.0)
village_2.add_flag(PartyFlag.IS_STATIC)
village_2.add_flag(PartyFlag.LABEL_SMALL)
village_2.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_2.add_flag(PartyFlag.HIDE_DEFENDERS)
village_2.set_icon(icon.village_a)


village_3 = MBParty("village_3", name="Azgad", faction=fac.neutral, initial_cords=(-97.4, 36.0), direction=120.0)
village_3.add_flag(PartyFlag.IS_STATIC)
village_3.add_flag(PartyFlag.LABEL_SMALL)
village_3.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_3.add_flag(PartyFlag.HIDE_DEFENDERS)
village_3.set_icon(icon.village_a)


village_4 = MBParty("village_4", name="Nomar", faction=fac.neutral, initial_cords=(-36.6, -13.2), direction=130.0)
village_4.add_flag(PartyFlag.IS_STATIC)
village_4.add_flag(PartyFlag.LABEL_SMALL)
village_4.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_4.add_flag(PartyFlag.HIDE_DEFENDERS)
village_4.set_icon(icon.village_a)


village_5 = MBParty("village_5", name="Kulum", faction=fac.neutral, initial_cords=(-122.7, 106.3), direction=170.0)
village_5.add_flag(PartyFlag.IS_STATIC)
village_5.add_flag(PartyFlag.LABEL_SMALL)
village_5.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_5.add_flag(PartyFlag.HIDE_DEFENDERS)
village_5.set_icon(icon.village_a)


village_6 = MBParty("village_6", name="Emirin", faction=fac.neutral, initial_cords=(5.5, -2.5), direction=100.0)
village_6.add_flag(PartyFlag.IS_STATIC)
village_6.add_flag(PartyFlag.LABEL_SMALL)
village_6.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_6.add_flag(PartyFlag.HIDE_DEFENDERS)
village_6.set_icon(icon.village_a)


village_7 = MBParty("village_7", name="Amere", faction=fac.neutral, initial_cords=(39.3, -5.25), direction=110.0)
village_7.add_flag(PartyFlag.IS_STATIC)
village_7.add_flag(PartyFlag.LABEL_SMALL)
village_7.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_7.add_flag(PartyFlag.HIDE_DEFENDERS)
village_7.set_icon(icon.village_a)


village_8 = MBParty("village_8", name="Haen", faction=fac.neutral, initial_cords=(-49.7, 74.0), direction=120.0)
village_8.add_flag(PartyFlag.IS_STATIC)
village_8.add_flag(PartyFlag.LABEL_SMALL)
village_8.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_8.add_flag(PartyFlag.HIDE_DEFENDERS)
village_8.set_icon(icon.village_a)


village_9 = MBParty("village_9", name="Buvran", faction=fac.neutral, initial_cords=(-85.0, -75.35), direction=130.0)
village_9.add_flag(PartyFlag.IS_STATIC)
village_9.add_flag(PartyFlag.LABEL_SMALL)
village_9.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_9.add_flag(PartyFlag.HIDE_DEFENDERS)
village_9.set_icon(icon.village_a)


village_10 = MBParty("village_10", name="Mechin", faction=fac.neutral, initial_cords=(8.8, 34.75), direction=170.0)
village_10.add_flag(PartyFlag.IS_STATIC)
village_10.add_flag(PartyFlag.LABEL_SMALL)
village_10.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_10.add_flag(PartyFlag.HIDE_DEFENDERS)
village_10.set_icon(icon.village_a)


village_11 = MBParty("village_11", name="Dusturil", faction=fac.neutral, initial_cords=(137.2, -36.5), direction=100.0)
village_11.add_flag(PartyFlag.IS_STATIC)
village_11.add_flag(PartyFlag.LABEL_SMALL)
village_11.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_11.add_flag(PartyFlag.HIDE_DEFENDERS)
village_11.set_icon(icon.village_a)


village_12 = MBParty("village_12", name="Emer", faction=fac.neutral, initial_cords=(-45.8, -58.5), direction=110.0)
village_12.add_flag(PartyFlag.IS_STATIC)
village_12.add_flag(PartyFlag.LABEL_SMALL)
village_12.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_12.add_flag(PartyFlag.HIDE_DEFENDERS)
village_12.set_icon(icon.village_a)


village_13 = MBParty("village_13", name="Nemeja", faction=fac.neutral, initial_cords=(-119.0, 3.0), direction=120.0)
village_13.add_flag(PartyFlag.IS_STATIC)
village_13.add_flag(PartyFlag.LABEL_SMALL)
village_13.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_13.add_flag(PartyFlag.HIDE_DEFENDERS)
village_13.set_icon(icon.village_a)


village_14 = MBParty("village_14", name="Sumbuja", faction=fac.neutral, initial_cords=(40.0, 52.0), direction=130.0)
village_14.add_flag(PartyFlag.IS_STATIC)
village_14.add_flag(PartyFlag.LABEL_SMALL)
village_14.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_14.add_flag(PartyFlag.HIDE_DEFENDERS)
village_14.set_icon(icon.village_a)


village_15 = MBParty("village_15", name="Ryibelet", faction=fac.neutral, initial_cords=(-49.3, 26.25), direction=170.0)
village_15.add_flag(PartyFlag.IS_STATIC)
village_15.add_flag(PartyFlag.LABEL_SMALL)
village_15.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_15.add_flag(PartyFlag.HIDE_DEFENDERS)
village_15.set_icon(icon.village_a)


village_16 = MBParty("village_16", name="Shapeshte", faction=fac.neutral, initial_cords=(74.0, 86.8), direction=170.0)
village_16.add_flag(PartyFlag.IS_STATIC)
village_16.add_flag(PartyFlag.LABEL_SMALL)
village_16.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_16.add_flag(PartyFlag.HIDE_DEFENDERS)
village_16.set_icon(icon.village_snow_a)


village_17 = MBParty("village_17", name="Mazen", faction=fac.neutral, initial_cords=(44.7, 91.4), direction=35.0)
village_17.add_flag(PartyFlag.IS_STATIC)
village_17.add_flag(PartyFlag.LABEL_SMALL)
village_17.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_17.add_flag(PartyFlag.HIDE_DEFENDERS)
village_17.set_icon(icon.village_snow_a)


village_18 = MBParty("village_18", name="Ulburban", faction=fac.neutral, initial_cords=(73.7, 30.1), direction=170.0)
village_18.add_flag(PartyFlag.IS_STATIC)
village_18.add_flag(PartyFlag.LABEL_SMALL)
village_18.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_18.add_flag(PartyFlag.HIDE_DEFENDERS)
village_18.set_icon(icon.village_snow_a)


village_19 = MBParty("village_19", name="Hanun", faction=fac.neutral, initial_cords=(152.3, 53.5), direction=170.0)
village_19.add_flag(PartyFlag.IS_STATIC)
village_19.add_flag(PartyFlag.LABEL_SMALL)
village_19.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_19.add_flag(PartyFlag.HIDE_DEFENDERS)
village_19.set_icon(icon.village_snow_a)


village_20 = MBParty("village_20", name="Uslum", faction=fac.neutral, initial_cords=(116.0, 80.3), direction=170.0)
village_20.add_flag(PartyFlag.IS_STATIC)
village_20.add_flag(PartyFlag.LABEL_SMALL)
village_20.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_20.add_flag(PartyFlag.HIDE_DEFENDERS)
village_20.set_icon(icon.village_snow_a)


village_21 = MBParty("village_21", name="Bazeck", faction=fac.neutral, initial_cords=(60.4, 85.0), direction=100.0)
village_21.add_flag(PartyFlag.IS_STATIC)
village_21.add_flag(PartyFlag.LABEL_SMALL)
village_21.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_21.add_flag(PartyFlag.HIDE_DEFENDERS)
village_21.set_icon(icon.village_snow_a)


village_22 = MBParty("village_22", name="Shulus", faction=fac.neutral, initial_cords=(125.4, 64.0), direction=110.0)
village_22.add_flag(PartyFlag.IS_STATIC)
village_22.add_flag(PartyFlag.LABEL_SMALL)
village_22.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_22.add_flag(PartyFlag.HIDE_DEFENDERS)
village_22.set_icon(icon.village_snow_a)


village_23 = MBParty("village_23", name="Ilvia", faction=fac.neutral, initial_cords=(-133.3, -37.6), direction=120.0)
village_23.add_flag(PartyFlag.IS_STATIC)
village_23.add_flag(PartyFlag.LABEL_SMALL)
village_23.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_23.add_flag(PartyFlag.HIDE_DEFENDERS)
village_23.set_icon(icon.village_a)


village_24 = MBParty("village_24", name="Ruldi", faction=fac.neutral, initial_cords=(-57.6, -73.0), direction=130.0)
village_24.add_flag(PartyFlag.IS_STATIC)
village_24.add_flag(PartyFlag.LABEL_SMALL)
village_24.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_24.add_flag(PartyFlag.HIDE_DEFENDERS)
village_24.set_icon(icon.village_a)


village_25 = MBParty("village_25", name="Dashbigha", faction=fac.neutral, initial_cords=(125.2, -8.0), direction=170.0)
village_25.add_flag(PartyFlag.IS_STATIC)
village_25.add_flag(PartyFlag.LABEL_SMALL)
village_25.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_25.add_flag(PartyFlag.HIDE_DEFENDERS)
village_25.set_icon(icon.village_a)


village_26 = MBParty("village_26", name="Pagundur", faction=fac.neutral, initial_cords=(-58.5, -30.8), direction=170.0)
village_26.add_flag(PartyFlag.IS_STATIC)
village_26.add_flag(PartyFlag.LABEL_SMALL)
village_26.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_26.add_flag(PartyFlag.HIDE_DEFENDERS)
village_26.set_icon(icon.village_a)


village_27 = MBParty("village_27", name="Glunmar", faction=fac.neutral, initial_cords=(-146.3, -16.6), direction=170.0)
village_27.add_flag(PartyFlag.IS_STATIC)
village_27.add_flag(PartyFlag.LABEL_SMALL)
village_27.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_27.add_flag(PartyFlag.HIDE_DEFENDERS)
village_27.set_icon(icon.village_a)


village_28 = MBParty("village_28", name="Tash Kulun", faction=fac.neutral, initial_cords=(95.0, -11.4), direction=170.0)
village_28.add_flag(PartyFlag.IS_STATIC)
village_28.add_flag(PartyFlag.LABEL_SMALL)
village_28.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_28.add_flag(PartyFlag.HIDE_DEFENDERS)
village_28.set_icon(icon.village_a)


village_29 = MBParty("village_29", name="Buillin", faction=fac.neutral, initial_cords=(-90.6, 110.9), direction=170.0)
village_29.add_flag(PartyFlag.IS_STATIC)
village_29.add_flag(PartyFlag.LABEL_SMALL)
village_29.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_29.add_flag(PartyFlag.HIDE_DEFENDERS)
village_29.set_icon(icon.village_a)


village_30 = MBParty("village_30", name="Ruvar", faction=fac.neutral, initial_cords=(29.2, 114.3), direction=170.0)
village_30.add_flag(PartyFlag.IS_STATIC)
village_30.add_flag(PartyFlag.LABEL_SMALL)
village_30.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_30.add_flag(PartyFlag.HIDE_DEFENDERS)
village_30.set_icon(icon.village_a)


village_31 = MBParty("village_31", name="Ambean", faction=fac.neutral, initial_cords=(-24.0, 53.0), direction=100.0)
village_31.add_flag(PartyFlag.IS_STATIC)
village_31.add_flag(PartyFlag.LABEL_SMALL)
village_31.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_31.add_flag(PartyFlag.HIDE_DEFENDERS)
village_31.set_icon(icon.village_a)


village_32 = MBParty("village_32", name="Tosdhar", faction=fac.neutral, initial_cords=(8.3, 14.5), direction=110.0)
village_32.add_flag(PartyFlag.IS_STATIC)
village_32.add_flag(PartyFlag.LABEL_SMALL)
village_32.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_32.add_flag(PartyFlag.HIDE_DEFENDERS)
village_32.set_icon(icon.village_a)


village_33 = MBParty("village_33", name="Ruluns", faction=fac.neutral, initial_cords=(-59.0, 10.6), direction=120.0)
village_33.add_flag(PartyFlag.IS_STATIC)
village_33.add_flag(PartyFlag.LABEL_SMALL)
village_33.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_33.add_flag(PartyFlag.HIDE_DEFENDERS)
village_33.set_icon(icon.village_a)


village_34 = MBParty("village_34", name="Ehlerdah", faction=fac.neutral, initial_cords=(34.15, -30.0), direction=130.0)
village_34.add_flag(PartyFlag.IS_STATIC)
village_34.add_flag(PartyFlag.LABEL_SMALL)
village_34.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_34.add_flag(PartyFlag.HIDE_DEFENDERS)
village_34.set_icon(icon.village_a)


village_35 = MBParty("village_35", name="Fearichen", faction=fac.neutral, initial_cords=(2.14, 86.9), direction=170.0)
village_35.add_flag(PartyFlag.IS_STATIC)
village_35.add_flag(PartyFlag.LABEL_SMALL)
village_35.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_35.add_flag(PartyFlag.HIDE_DEFENDERS)
village_35.set_icon(icon.village_a)


village_36 = MBParty("village_36", name="Jayek", faction=fac.neutral, initial_cords=(17.4, 100.7), direction=170.0)
village_36.add_flag(PartyFlag.IS_STATIC)
village_36.add_flag(PartyFlag.LABEL_SMALL)
village_36.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_36.add_flag(PartyFlag.HIDE_DEFENDERS)
village_36.set_icon(icon.village_a)


village_37 = MBParty("village_37", name="Ada Kulun", faction=fac.neutral, initial_cords=(164.4, 26.0), direction=170.0)
village_37.add_flag(PartyFlag.IS_STATIC)
village_37.add_flag(PartyFlag.LABEL_SMALL)
village_37.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_37.add_flag(PartyFlag.HIDE_DEFENDERS)
village_37.set_icon(icon.village_a)


village_38 = MBParty("village_38", name="Ibiran", faction=fac.neutral, initial_cords=(-42.8, 11.25), direction=170.0)
village_38.add_flag(PartyFlag.IS_STATIC)
village_38.add_flag(PartyFlag.LABEL_SMALL)
village_38.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_38.add_flag(PartyFlag.HIDE_DEFENDERS)
village_38.set_icon(icon.village_a)


village_39 = MBParty("village_39", name="Reveran", faction=fac.neutral, initial_cords=(-124.3, -29.5), direction=170.0)
village_39.add_flag(PartyFlag.IS_STATIC)
village_39.add_flag(PartyFlag.LABEL_SMALL)
village_39.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_39.add_flag(PartyFlag.HIDE_DEFENDERS)
village_39.set_icon(icon.village_a)


village_40 = MBParty("village_40", name="Saren", faction=fac.neutral, initial_cords=(-12.0, -53.0), direction=170.0)
village_40.add_flag(PartyFlag.IS_STATIC)
village_40.add_flag(PartyFlag.LABEL_SMALL)
village_40.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_40.add_flag(PartyFlag.HIDE_DEFENDERS)
village_40.set_icon(icon.village_a)


village_41 = MBParty("village_41", name="Dugan", faction=fac.neutral, initial_cords=(175.0, -39.5), direction=100.0)
village_41.add_flag(PartyFlag.IS_STATIC)
village_41.add_flag(PartyFlag.LABEL_SMALL)
village_41.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_41.add_flag(PartyFlag.HIDE_DEFENDERS)
village_41.set_icon(icon.village_a)


village_42 = MBParty("village_42", name="Dirigh Aban", faction=fac.neutral, initial_cords=(115.4, 21.6), direction=110.0)
village_42.add_flag(PartyFlag.IS_STATIC)
village_42.add_flag(PartyFlag.LABEL_SMALL)
village_42.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_42.add_flag(PartyFlag.HIDE_DEFENDERS)
village_42.set_icon(icon.village_a)


village_43 = MBParty("village_43", name="Zagush", faction=fac.neutral, initial_cords=(99.4, -21.3), direction=120.0)
village_43.add_flag(PartyFlag.IS_STATIC)
village_43.add_flag(PartyFlag.LABEL_SMALL)
village_43.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_43.add_flag(PartyFlag.HIDE_DEFENDERS)
village_43.set_icon(icon.village_a)


village_44 = MBParty("village_44", name="Peshmi", faction=fac.neutral, initial_cords=(51.8, -50.0), direction=130.0)
village_44.add_flag(PartyFlag.IS_STATIC)
village_44.add_flag(PartyFlag.LABEL_SMALL)
village_44.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_44.add_flag(PartyFlag.HIDE_DEFENDERS)
village_44.set_icon(icon.village_a)


village_45 = MBParty("village_45", name="Bulugur", faction=fac.neutral, initial_cords=(151.5, -3.0), direction=170.0)
village_45.add_flag(PartyFlag.IS_STATIC)
village_45.add_flag(PartyFlag.LABEL_SMALL)
village_45.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_45.add_flag(PartyFlag.HIDE_DEFENDERS)
village_45.set_icon(icon.village_a)


village_46 = MBParty("village_46", name="Fedner", faction=fac.neutral, initial_cords=(-82.4, -48.8), direction=170.0)
village_46.add_flag(PartyFlag.IS_STATIC)
village_46.add_flag(PartyFlag.LABEL_SMALL)
village_46.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_46.add_flag(PartyFlag.HIDE_DEFENDERS)
village_46.set_icon(icon.village_a)


village_47 = MBParty("village_47", name="Epeshe", faction=fac.neutral, initial_cords=(-101.2, -53.7), direction=170.0)
village_47.add_flag(PartyFlag.IS_STATIC)
village_47.add_flag(PartyFlag.LABEL_SMALL)
village_47.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_47.add_flag(PartyFlag.HIDE_DEFENDERS)
village_47.set_icon(icon.village_a)


village_48 = MBParty("village_48", name="Veidar", faction=fac.neutral, initial_cords=(-103.0, 15.3), direction=170.0)
village_48.add_flag(PartyFlag.IS_STATIC)
village_48.add_flag(PartyFlag.LABEL_SMALL)
village_48.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_48.add_flag(PartyFlag.HIDE_DEFENDERS)
village_48.set_icon(icon.village_a)


village_49 = MBParty("village_49", name="Tismirr", faction=fac.neutral, initial_cords=(90.8, 60.5), direction=10.0)
village_49.add_flag(PartyFlag.IS_STATIC)
village_49.add_flag(PartyFlag.LABEL_SMALL)
village_49.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_49.add_flag(PartyFlag.HIDE_DEFENDERS)
village_49.set_icon(icon.village_snow_a)


village_50 = MBParty("village_50", name="Karindi", faction=fac.neutral, initial_cords=(64.1, 55.9), direction=170.0)
village_50.add_flag(PartyFlag.IS_STATIC)
village_50.add_flag(PartyFlag.LABEL_SMALL)
village_50.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_50.add_flag(PartyFlag.HIDE_DEFENDERS)
village_50.set_icon(icon.village_snow_a)


village_51 = MBParty("village_51", name="Jelbegi", faction=fac.neutral, initial_cords=(-40.0, 62.0), direction=100.0)
village_51.add_flag(PartyFlag.IS_STATIC)
village_51.add_flag(PartyFlag.LABEL_SMALL)
village_51.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_51.add_flag(PartyFlag.HIDE_DEFENDERS)
village_51.set_icon(icon.village_a)


village_52 = MBParty("village_52", name="Amashke", faction=fac.neutral, initial_cords=(38.2, -67.7), direction=110.0)
village_52.add_flag(PartyFlag.IS_STATIC)
village_52.add_flag(PartyFlag.LABEL_SMALL)
village_52.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_52.add_flag(PartyFlag.HIDE_DEFENDERS)
village_52.set_icon(icon.village_a)


village_53 = MBParty("village_53", name="Balanli", faction=fac.neutral, initial_cords=(-130.3, 42.0), direction=120.0)
village_53.add_flag(PartyFlag.IS_STATIC)
village_53.add_flag(PartyFlag.LABEL_SMALL)
village_53.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_53.add_flag(PartyFlag.HIDE_DEFENDERS)
village_53.set_icon(icon.village_a)


village_54 = MBParty("village_54", name="Chide", faction=fac.neutral, initial_cords=(-19.0, 15.5), direction=130.0)
village_54.add_flag(PartyFlag.IS_STATIC)
village_54.add_flag(PartyFlag.LABEL_SMALL)
village_54.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_54.add_flag(PartyFlag.HIDE_DEFENDERS)
village_54.set_icon(icon.village_a)


village_55 = MBParty("village_55", name="Tadsamesh", faction=fac.neutral, initial_cords=(37.3, 23.7), direction=170.0)
village_55.add_flag(PartyFlag.IS_STATIC)
village_55.add_flag(PartyFlag.LABEL_SMALL)
village_55.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_55.add_flag(PartyFlag.HIDE_DEFENDERS)
village_55.set_icon(icon.village_a)


village_56 = MBParty("village_56", name="Fenada", faction=fac.neutral, initial_cords=(-5.55, 75.5), direction=170.0)
village_56.add_flag(PartyFlag.IS_STATIC)
village_56.add_flag(PartyFlag.LABEL_SMALL)
village_56.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_56.add_flag(PartyFlag.HIDE_DEFENDERS)
village_56.set_icon(icon.village_a)


village_57 = MBParty("village_57", name="Ushkuru", faction=fac.neutral, initial_cords=(24.75, -7.7), direction=170.0)
village_57.add_flag(PartyFlag.IS_STATIC)
village_57.add_flag(PartyFlag.LABEL_SMALL)
village_57.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_57.add_flag(PartyFlag.HIDE_DEFENDERS)
village_57.set_icon(icon.village_a)


village_58 = MBParty("village_58", name="Vezin", faction=fac.neutral, initial_cords=(78.5, 118.3), direction=170.0)
village_58.add_flag(PartyFlag.IS_STATIC)
village_58.add_flag(PartyFlag.LABEL_SMALL)
village_58.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_58.add_flag(PartyFlag.HIDE_DEFENDERS)
village_58.set_icon(icon.village_a)


village_59 = MBParty("village_59", name="Dumar", faction=fac.neutral, initial_cords=(-101.0, -45.0), direction=170.0)
village_59.add_flag(PartyFlag.IS_STATIC)
village_59.add_flag(PartyFlag.LABEL_SMALL)
village_59.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_59.add_flag(PartyFlag.HIDE_DEFENDERS)
village_59.set_icon(icon.village_a)


village_60 = MBParty("village_60", name="Tahlberl", faction=fac.neutral, initial_cords=(-26.6, 30.0), direction=170.0)
village_60.add_flag(PartyFlag.IS_STATIC)
village_60.add_flag(PartyFlag.LABEL_SMALL)
village_60.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_60.add_flag(PartyFlag.HIDE_DEFENDERS)
village_60.set_icon(icon.village_a)


village_61 = MBParty("village_61", name="Aldelen", faction=fac.neutral, initial_cords=(-99.8, 85.65), direction=100.0)
village_61.add_flag(PartyFlag.IS_STATIC)
village_61.add_flag(PartyFlag.LABEL_SMALL)
village_61.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_61.add_flag(PartyFlag.HIDE_DEFENDERS)
village_61.set_icon(icon.village_a)


village_62 = MBParty("village_62", name="Rebache", faction=fac.neutral, initial_cords=(36.7, 59.5), direction=100.0)
village_62.add_flag(PartyFlag.IS_STATIC)
village_62.add_flag(PartyFlag.LABEL_SMALL)
village_62.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_62.add_flag(PartyFlag.HIDE_DEFENDERS)
village_62.set_icon(icon.village_a)


village_63 = MBParty("village_63", name="Rduna", faction=fac.neutral, initial_cords=(70.75, 1.6), direction=100.0)
village_63.add_flag(PartyFlag.IS_STATIC)
village_63.add_flag(PartyFlag.LABEL_SMALL)
village_63.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_63.add_flag(PartyFlag.HIDE_DEFENDERS)
village_63.set_icon(icon.village_a)


village_64 = MBParty("village_64", name="Serindiar", faction=fac.neutral, initial_cords=(-41.5, -35.8), direction=100.0)
village_64.add_flag(PartyFlag.IS_STATIC)
village_64.add_flag(PartyFlag.LABEL_SMALL)
village_64.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_64.add_flag(PartyFlag.HIDE_DEFENDERS)
village_64.set_icon(icon.village_a)


village_65 = MBParty("village_65", name="Iyindah", faction=fac.neutral, initial_cords=(-86.3, 12.4), direction=100.0)
village_65.add_flag(PartyFlag.IS_STATIC)
village_65.add_flag(PartyFlag.LABEL_SMALL)
village_65.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_65.add_flag(PartyFlag.HIDE_DEFENDERS)
village_65.set_icon(icon.village_a)


village_66 = MBParty("village_66", name="Fisdnar", faction=fac.neutral, initial_cords=(109.0, 127.5), direction=100.0)
village_66.add_flag(PartyFlag.IS_STATIC)
village_66.add_flag(PartyFlag.LABEL_SMALL)
village_66.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_66.add_flag(PartyFlag.HIDE_DEFENDERS)
village_66.set_icon(icon.village_a)


village_67 = MBParty("village_67", name="Tebandra", faction=fac.neutral, initial_cords=(65.0, 23.0), direction=100.0)
village_67.add_flag(PartyFlag.IS_STATIC)
village_67.add_flag(PartyFlag.LABEL_SMALL)
village_67.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_67.add_flag(PartyFlag.HIDE_DEFENDERS)
village_67.set_icon(icon.village_a)


village_68 = MBParty("village_68", name="Ibdeles", faction=fac.neutral, initial_cords=(-72.6, -97.5), direction=100.0)
village_68.add_flag(PartyFlag.IS_STATIC)
village_68.add_flag(PartyFlag.LABEL_SMALL)
village_68.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_68.add_flag(PartyFlag.HIDE_DEFENDERS)
village_68.set_icon(icon.village_a)


village_69 = MBParty("village_69", name="Kwynn", faction=fac.neutral, initial_cords=(-26.5, 77.6), direction=100.0)
village_69.add_flag(PartyFlag.IS_STATIC)
village_69.add_flag(PartyFlag.LABEL_SMALL)
village_69.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_69.add_flag(PartyFlag.HIDE_DEFENDERS)
village_69.set_icon(icon.village_a)


village_70 = MBParty("village_70", name="Dirigsene", faction=fac.neutral, initial_cords=(-94.0, -27.0), direction=100.0)
village_70.add_flag(PartyFlag.IS_STATIC)
village_70.add_flag(PartyFlag.LABEL_SMALL)
village_70.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_70.add_flag(PartyFlag.HIDE_DEFENDERS)
village_70.set_icon(icon.village_a)


village_71 = MBParty("village_71", name="Tshibtin", faction=fac.neutral, initial_cords=(-9.0, -20.0), direction=20.0)
village_71.add_flag(PartyFlag.IS_STATIC)
village_71.add_flag(PartyFlag.LABEL_SMALL)
village_71.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_71.add_flag(PartyFlag.HIDE_DEFENDERS)
village_71.set_icon(icon.village_a)


village_72 = MBParty("village_72", name="Elberl", faction=fac.neutral, initial_cords=(-144.0, 16.15), direction=60.0)
village_72.add_flag(PartyFlag.IS_STATIC)
village_72.add_flag(PartyFlag.LABEL_SMALL)
village_72.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_72.add_flag(PartyFlag.HIDE_DEFENDERS)
village_72.set_icon(icon.village_a)


village_73 = MBParty("village_73", name="Chaeza", faction=fac.neutral, initial_cords=(-63.2, -51.4), direction=55.0)
village_73.add_flag(PartyFlag.IS_STATIC)
village_73.add_flag(PartyFlag.LABEL_SMALL)
village_73.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_73.add_flag(PartyFlag.HIDE_DEFENDERS)
village_73.set_icon(icon.village_a)


village_74 = MBParty("village_74", name="Ayyike", faction=fac.neutral, initial_cords=(49.0, 31.0), direction=15.0)
village_74.add_flag(PartyFlag.IS_STATIC)
village_74.add_flag(PartyFlag.LABEL_SMALL)
village_74.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_74.add_flag(PartyFlag.HIDE_DEFENDERS)
village_74.set_icon(icon.village_a)


village_75 = MBParty("village_75", name="Bhulaban", faction=fac.neutral, initial_cords=(110.2, 48.8), direction=10.0)
village_75.add_flag(PartyFlag.IS_STATIC)
village_75.add_flag(PartyFlag.LABEL_SMALL)
village_75.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_75.add_flag(PartyFlag.HIDE_DEFENDERS)
village_75.set_icon(icon.village_snow_a)


village_76 = MBParty("village_76", name="Kedelke", faction=fac.neutral, initial_cords=(91.5, -34.8), direction=35.0)
village_76.add_flag(PartyFlag.IS_STATIC)
village_76.add_flag(PartyFlag.LABEL_SMALL)
village_76.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_76.add_flag(PartyFlag.HIDE_DEFENDERS)
village_76.set_icon(icon.village_a)


village_77 = MBParty("village_77", name="Rizi", faction=fac.neutral, initial_cords=(-64.8, 81.5), direction=160.0)
village_77.add_flag(PartyFlag.IS_STATIC)
village_77.add_flag(PartyFlag.LABEL_SMALL)
village_77.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_77.add_flag(PartyFlag.HIDE_DEFENDERS)
village_77.set_icon(icon.village_a)


village_78 = MBParty("village_78", name="Sarimish", faction=fac.neutral, initial_cords=(-30.2, -53.3), direction=180.0)
village_78.add_flag(PartyFlag.IS_STATIC)
village_78.add_flag(PartyFlag.LABEL_SMALL)
village_78.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_78.add_flag(PartyFlag.HIDE_DEFENDERS)
village_78.set_icon(icon.village_a)


village_79 = MBParty("village_79", name="Istiniar", faction=fac.neutral, initial_cords=(-134.1, -5.5))
village_79.add_flag(PartyFlag.IS_STATIC)
village_79.add_flag(PartyFlag.LABEL_SMALL)
village_79.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_79.add_flag(PartyFlag.HIDE_DEFENDERS)
village_79.set_icon(icon.village_a)


village_80 = MBParty("village_80", name="Vayejeg", faction=fac.neutral, initial_cords=(-1.5, 56.0), direction=40.0)
village_80.add_flag(PartyFlag.IS_STATIC)
village_80.add_flag(PartyFlag.LABEL_SMALL)
village_80.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_80.add_flag(PartyFlag.HIDE_DEFENDERS)
village_80.set_icon(icon.village_a)


village_81 = MBParty("village_81", name="Odasan", faction=fac.neutral, initial_cords=(-17.2, 123.6), direction=20.0)
village_81.add_flag(PartyFlag.IS_STATIC)
village_81.add_flag(PartyFlag.LABEL_SMALL)
village_81.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_81.add_flag(PartyFlag.HIDE_DEFENDERS)
village_81.set_icon(icon.village_a)


village_82 = MBParty("village_82", name="Yalibe", faction=fac.neutral, initial_cords=(12.0, -26.0), direction=60.0)
village_82.add_flag(PartyFlag.IS_STATIC)
village_82.add_flag(PartyFlag.LABEL_SMALL)
village_82.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_82.add_flag(PartyFlag.HIDE_DEFENDERS)
village_82.set_icon(icon.village_a)


village_83 = MBParty("village_83", name="Gisim", faction=fac.neutral, initial_cords=(-79.9, 55.2), direction=55.0)
village_83.add_flag(PartyFlag.IS_STATIC)
village_83.add_flag(PartyFlag.LABEL_SMALL)
village_83.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_83.add_flag(PartyFlag.HIDE_DEFENDERS)
village_83.set_icon(icon.village_a)


village_84 = MBParty("village_84", name="Chelez", faction=fac.neutral, initial_cords=(-45.6, -83.0), direction=15.0)
village_84.add_flag(PartyFlag.IS_STATIC)
village_84.add_flag(PartyFlag.LABEL_SMALL)
village_84.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_84.add_flag(PartyFlag.HIDE_DEFENDERS)
village_84.set_icon(icon.village_a)


village_85 = MBParty("village_85", name="Ismirala", faction=fac.neutral, initial_cords=(22.8, 71.7), direction=10.0)
village_85.add_flag(PartyFlag.IS_STATIC)
village_85.add_flag(PartyFlag.LABEL_SMALL)
village_85.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_85.add_flag(PartyFlag.HIDE_DEFENDERS)
village_85.set_icon(icon.village_snow_a)


village_86 = MBParty("village_86", name="Slezkh", faction=fac.neutral, initial_cords=(60.5, 68.2), direction=35.0)
village_86.add_flag(PartyFlag.IS_STATIC)
village_86.add_flag(PartyFlag.LABEL_SMALL)
village_86.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_86.add_flag(PartyFlag.HIDE_DEFENDERS)
village_86.set_icon(icon.village_snow_a)


village_87 = MBParty("village_87", name="Udiniad", faction=fac.neutral, initial_cords=(52.3, 111.8), direction=160.0)
village_87.add_flag(PartyFlag.IS_STATIC)
village_87.add_flag(PartyFlag.LABEL_SMALL)
village_87.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_87.add_flag(PartyFlag.HIDE_DEFENDERS)
village_87.set_icon(icon.village_a)


village_88 = MBParty("village_88", name="Tulbuk", faction=fac.neutral, initial_cords=(135.8, 24.7), direction=180.0)
village_88.add_flag(PartyFlag.IS_STATIC)
village_88.add_flag(PartyFlag.LABEL_SMALL)
village_88.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_88.add_flag(PartyFlag.HIDE_DEFENDERS)
village_88.set_icon(icon.village_a)


village_89 = MBParty("village_89", name="Uhhun", faction=fac.neutral, initial_cords=(70.1, -27.9))
village_89.add_flag(PartyFlag.IS_STATIC)
village_89.add_flag(PartyFlag.LABEL_SMALL)
village_89.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_89.add_flag(PartyFlag.HIDE_DEFENDERS)
village_89.set_icon(icon.village_a)


village_90 = MBParty("village_90", name="Jamiche", faction=fac.neutral, initial_cords=(-12.7, -85.5), direction=40.0)
village_90.add_flag(PartyFlag.IS_STATIC)
village_90.add_flag(PartyFlag.LABEL_SMALL)
village_90.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_90.add_flag(PartyFlag.HIDE_DEFENDERS)
village_90.set_icon(icon.village_a)


village_91 = MBParty("village_91", name="Ayn Assuadi", faction=fac.neutral, initial_cords=(21.6, -95.3), direction=20.0)
village_91.add_flag(PartyFlag.IS_STATIC)
village_91.add_flag(PartyFlag.LABEL_SMALL)
village_91.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_91.add_flag(PartyFlag.HIDE_DEFENDERS)
village_91.set_icon(icon.village_c)


village_92 = MBParty("village_92", name="Dhibbain", faction=fac.neutral, initial_cords=(42.5, -111.6), direction=60.0)
village_92.add_flag(PartyFlag.IS_STATIC)
village_92.add_flag(PartyFlag.LABEL_SMALL)
village_92.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_92.add_flag(PartyFlag.HIDE_DEFENDERS)
village_92.set_icon(icon.village_c)


village_93 = MBParty("village_93", name="Qalyut", faction=fac.neutral, initial_cords=(50.0, -94.8), direction=55.0)
village_93.add_flag(PartyFlag.IS_STATIC)
village_93.add_flag(PartyFlag.LABEL_SMALL)
village_93.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_93.add_flag(PartyFlag.HIDE_DEFENDERS)
village_93.set_icon(icon.village_c)


village_94 = MBParty("village_94", name="Mazigh", faction=fac.neutral, initial_cords=(75.4, -61.65), direction=15.0)
village_94.add_flag(PartyFlag.IS_STATIC)
village_94.add_flag(PartyFlag.LABEL_SMALL)
village_94.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_94.add_flag(PartyFlag.HIDE_DEFENDERS)
village_94.set_icon(icon.village_c)


village_95 = MBParty("village_95", name="Tamnuh", faction=fac.neutral, initial_cords=(99.0, -90.5), direction=10.0)
village_95.add_flag(PartyFlag.IS_STATIC)
village_95.add_flag(PartyFlag.LABEL_SMALL)
village_95.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_95.add_flag(PartyFlag.HIDE_DEFENDERS)
village_95.set_icon(icon.village_c)


village_96 = MBParty("village_96", name="Habba", faction=fac.neutral, initial_cords=(107.0, -75.0), direction=35.0)
village_96.add_flag(PartyFlag.IS_STATIC)
village_96.add_flag(PartyFlag.LABEL_SMALL)
village_96.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_96.add_flag(PartyFlag.HIDE_DEFENDERS)
village_96.set_icon(icon.village_c)


village_97 = MBParty("village_97", name="Sekhtem", faction=fac.neutral, initial_cords=(82.3, -76.8), direction=160.0)
village_97.add_flag(PartyFlag.IS_STATIC)
village_97.add_flag(PartyFlag.LABEL_SMALL)
village_97.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_97.add_flag(PartyFlag.HIDE_DEFENDERS)
village_97.set_icon(icon.village_c)


village_98 = MBParty("village_98", name="Mawiti", faction=fac.neutral, initial_cords=(117.7, -62.2), direction=180.0)
village_98.add_flag(PartyFlag.IS_STATIC)
village_98.add_flag(PartyFlag.LABEL_SMALL)
village_98.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_98.add_flag(PartyFlag.HIDE_DEFENDERS)
village_98.set_icon(icon.village_c)


village_99 = MBParty("village_99", name="Fishara", faction=fac.neutral, initial_cords=(158.35, -98.0))
village_99.add_flag(PartyFlag.IS_STATIC)
village_99.add_flag(PartyFlag.LABEL_SMALL)
village_99.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_99.add_flag(PartyFlag.HIDE_DEFENDERS)
village_99.set_icon(icon.village_c)


village_100 = MBParty("village_100", name="Iqbayl", faction=fac.neutral, initial_cords=(150.0, -106.5), direction=40.0)
village_100.add_flag(PartyFlag.IS_STATIC)
village_100.add_flag(PartyFlag.LABEL_SMALL)
village_100.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_100.add_flag(PartyFlag.HIDE_DEFENDERS)
village_100.set_icon(icon.village_c)


village_101 = MBParty("village_101", name="Uzgha", faction=fac.neutral, initial_cords=(154.0, -69.5), direction=20.0)
village_101.add_flag(PartyFlag.IS_STATIC)
village_101.add_flag(PartyFlag.LABEL_SMALL)
village_101.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_101.add_flag(PartyFlag.HIDE_DEFENDERS)
village_101.set_icon(icon.village_c)


village_102 = MBParty("village_102", name="Shibal Zumr", faction=fac.neutral, initial_cords=(77.2, -91.0), direction=60.0)
village_102.add_flag(PartyFlag.IS_STATIC)
village_102.add_flag(PartyFlag.LABEL_SMALL)
village_102.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_102.add_flag(PartyFlag.HIDE_DEFENDERS)
village_102.set_icon(icon.village_c)


village_103 = MBParty("village_103", name="Mijayet", faction=fac.neutral, initial_cords=(121.0, -95.6), direction=55.0)
village_103.add_flag(PartyFlag.IS_STATIC)
village_103.add_flag(PartyFlag.LABEL_SMALL)
village_103.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_103.add_flag(PartyFlag.HIDE_DEFENDERS)
village_103.set_icon(icon.village_c)


village_104 = MBParty("village_104", name="Tazjunat", faction=fac.neutral, initial_cords=(159.0, -58.5), direction=15.0)
village_104.add_flag(PartyFlag.IS_STATIC)
village_104.add_flag(PartyFlag.LABEL_SMALL)
village_104.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_104.add_flag(PartyFlag.HIDE_DEFENDERS)
village_104.set_icon(icon.village_c)


village_105 = MBParty("village_105", name="Aab", faction=fac.neutral, initial_cords=(135.0, -88.5), direction=10.0)
village_105.add_flag(PartyFlag.IS_STATIC)
village_105.add_flag(PartyFlag.LABEL_SMALL)
village_105.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_105.add_flag(PartyFlag.HIDE_DEFENDERS)
village_105.set_icon(icon.village_c)


village_106 = MBParty("village_106", name="Hawaha", faction=fac.neutral, initial_cords=(10.3, -91.0), direction=35.0)
village_106.add_flag(PartyFlag.IS_STATIC)
village_106.add_flag(PartyFlag.LABEL_SMALL)
village_106.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_106.add_flag(PartyFlag.HIDE_DEFENDERS)
village_106.set_icon(icon.village_c)


village_107 = MBParty("village_107", name="Unriya", faction=fac.neutral, initial_cords=(156.6, -84.0), direction=160.0)
village_107.add_flag(PartyFlag.IS_STATIC)
village_107.add_flag(PartyFlag.LABEL_SMALL)
village_107.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_107.add_flag(PartyFlag.HIDE_DEFENDERS)
village_107.set_icon(icon.village_c)


village_108 = MBParty("village_108", name="Mit Nun", faction=fac.neutral, initial_cords=(28.8, -107.3), direction=180.0)
village_108.add_flag(PartyFlag.IS_STATIC)
village_108.add_flag(PartyFlag.LABEL_SMALL)
village_108.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_108.add_flag(PartyFlag.HIDE_DEFENDERS)
village_108.set_icon(icon.village_c)


village_109 = MBParty("village_109", name="Tilimsal", faction=fac.neutral, initial_cords=(53.0, -114.5))
village_109.add_flag(PartyFlag.IS_STATIC)
village_109.add_flag(PartyFlag.LABEL_SMALL)
village_109.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_109.add_flag(PartyFlag.HIDE_DEFENDERS)
village_109.set_icon(icon.village_c)


village_110 = MBParty("village_110", name="Rushdigh", faction=fac.neutral, initial_cords=(38.0, -104.0), direction=40.0)
village_110.add_flag(PartyFlag.IS_STATIC)
village_110.add_flag(PartyFlag.LABEL_SMALL)
village_110.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
village_110.add_flag(PartyFlag.HIDE_DEFENDERS)
village_110.set_icon(icon.village_c)


salt_mine = MBParty("salt_mine", name="Salt Mine", faction=fac.neutral, initial_cords=(14.2, -31.0))
salt_mine.add_flag(PartyFlag.IS_DISABLED)
salt_mine.add_flag(PartyFlag.IS_STATIC)
salt_mine.add_flag(PartyFlag.LABEL_SMALL)
salt_mine.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
salt_mine.add_flag(PartyFlag.HIDE_DEFENDERS)
salt_mine.set_icon(icon.village_a)


four_ways_inn = MBParty("four_ways_inn", name="Four Ways Inn", faction=fac.neutral, initial_cords=(4.8, -39.6))
four_ways_inn.add_flag(PartyFlag.IS_DISABLED)
four_ways_inn.add_flag(PartyFlag.IS_STATIC)
four_ways_inn.add_flag(PartyFlag.LABEL_SMALL)
four_ways_inn.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
four_ways_inn.add_flag(PartyFlag.HIDE_DEFENDERS)
four_ways_inn.set_icon(icon.village_a)


test_scene = MBParty("test_scene", name="test scene", faction=fac.neutral, initial_cords=(10.8, -19.6))
test_scene.add_flag(PartyFlag.IS_DISABLED)
test_scene.add_flag(PartyFlag.IS_STATIC)
test_scene.add_flag(PartyFlag.LABEL_SMALL)
test_scene.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
test_scene.add_flag(PartyFlag.HIDE_DEFENDERS)
test_scene.set_icon(icon.village_a)


battlefields = MBParty("battlefields", name="battlefields", faction=fac.neutral, initial_cords=(10.8, -16.6))
battlefields.add_flag(PartyFlag.IS_DISABLED)
battlefields.add_flag(PartyFlag.IS_STATIC)
battlefields.add_flag(PartyFlag.LABEL_SMALL)
battlefields.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
battlefields.add_flag(PartyFlag.HIDE_DEFENDERS)
battlefields.set_icon(icon.village_a)


dhorak_keep = MBParty("dhorak_keep", name="Dhorak Keep", faction=fac.neutral, initial_cords=(-50.0, -58.0))
dhorak_keep.add_flag(PartyFlag.IS_DISABLED)
dhorak_keep.add_flag(PartyFlag.IS_STATIC)
dhorak_keep.add_flag(PartyFlag.LABEL_SMALL)
dhorak_keep.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
dhorak_keep.add_flag(PartyFlag.HAS_NO_LABEL)
dhorak_keep.add_flag(PartyFlag.HIDE_DEFENDERS)
dhorak_keep.set_icon(icon.town)


training_ground = MBParty("training_ground", name="Training Ground", faction=fac.neutral, initial_cords=(3.0, -7.0))
training_ground.add_flag(PartyFlag.IS_DISABLED)
training_ground.add_flag(PartyFlag.IS_STATIC)
training_ground.add_flag(PartyFlag.LABEL_SMALL)
training_ground.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
training_ground.add_flag(PartyFlag.HIDE_DEFENDERS)
training_ground.set_icon(icon.training_ground)


training_ground_1 = MBParty("training_ground_1", name="Training Field", faction=fac.neutral, initial_cords=(37.4, 102.8), direction=100.0)
training_ground_1.add_flag(PartyFlag.IS_STATIC)
training_ground_1.add_flag(PartyFlag.LABEL_SMALL)
training_ground_1.add_flag(PartyFlag.LABEL_MEDIUM)
training_ground_1.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
training_ground_1.add_flag(PartyFlag.HIDE_DEFENDERS)
training_ground_1.set_icon(icon.training_ground)


training_ground_2 = MBParty("training_ground_2", name="Training Field", faction=fac.neutral, initial_cords=(-12.8, 33.0), direction=100.0)
training_ground_2.add_flag(PartyFlag.IS_STATIC)
training_ground_2.add_flag(PartyFlag.LABEL_SMALL)
training_ground_2.add_flag(PartyFlag.LABEL_MEDIUM)
training_ground_2.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
training_ground_2.add_flag(PartyFlag.HIDE_DEFENDERS)
training_ground_2.set_icon(icon.training_ground)


training_ground_3 = MBParty("training_ground_3", name="Training Field", faction=fac.neutral, initial_cords=(70.5, 72.0), direction=100.0)
training_ground_3.add_flag(PartyFlag.IS_STATIC)
training_ground_3.add_flag(PartyFlag.LABEL_SMALL)
training_ground_3.add_flag(PartyFlag.LABEL_MEDIUM)
training_ground_3.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
training_ground_3.add_flag(PartyFlag.HIDE_DEFENDERS)
training_ground_3.set_icon(icon.training_ground)


training_ground_4 = MBParty("training_ground_4", name="Training Field", faction=fac.neutral, initial_cords=(11.5, -75.2), direction=100.0)
training_ground_4.add_flag(PartyFlag.IS_STATIC)
training_ground_4.add_flag(PartyFlag.LABEL_SMALL)
training_ground_4.add_flag(PartyFlag.LABEL_MEDIUM)
training_ground_4.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
training_ground_4.add_flag(PartyFlag.HIDE_DEFENDERS)
training_ground_4.set_icon(icon.training_ground)


training_ground_5 = MBParty("training_ground_5", name="Training Field", faction=fac.neutral, initial_cords=(-125.8, 12.5), direction=100.0)
training_ground_5.add_flag(PartyFlag.IS_STATIC)
training_ground_5.add_flag(PartyFlag.LABEL_SMALL)
training_ground_5.add_flag(PartyFlag.LABEL_MEDIUM)
training_ground_5.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
training_ground_5.add_flag(PartyFlag.HIDE_DEFENDERS)
training_ground_5.set_icon(icon.training_ground)


bridge_1 = MBParty("bridge_1", name="{!}1", faction=fac.neutral, initial_cords=(39.37, 65.1), direction=-44.8)
bridge_1.add_flag(PartyFlag.IS_STATIC)
bridge_1.add_flag(PartyFlag.LABEL_SMALL)
bridge_1.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_1.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_1.set_icon(icon.bridge_snow_a)


bridge_2 = MBParty("bridge_2", name="{!}2", faction=fac.neutral, initial_cords=(56.44, 77.88), direction=4.28)
bridge_2.add_flag(PartyFlag.IS_STATIC)
bridge_2.add_flag(PartyFlag.LABEL_SMALL)
bridge_2.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_2.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_2.set_icon(icon.bridge_snow_a)


bridge_3 = MBParty("bridge_3", name="{!}3", faction=fac.neutral, initial_cords=(70.87, 87.95), direction=64.5)
bridge_3.add_flag(PartyFlag.IS_STATIC)
bridge_3.add_flag(PartyFlag.LABEL_SMALL)
bridge_3.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_3.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_3.set_icon(icon.bridge_snow_a)


bridge_4 = MBParty("bridge_4", name="{!}4", faction=fac.neutral, initial_cords=(93.71, 62.13), direction=-2.13)
bridge_4.add_flag(PartyFlag.IS_STATIC)
bridge_4.add_flag(PartyFlag.LABEL_SMALL)
bridge_4.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_4.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_4.set_icon(icon.bridge_snow_a)


bridge_5 = MBParty("bridge_5", name="{!}5", faction=fac.neutral, initial_cords=(11.02, 72.61), direction=21.5)
bridge_5.add_flag(PartyFlag.IS_STATIC)
bridge_5.add_flag(PartyFlag.LABEL_SMALL)
bridge_5.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_5.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_5.set_icon(icon.bridge_snow_a)


bridge_6 = MBParty("bridge_6", name="{!}6", faction=fac.neutral, initial_cords=(-8.83, 52.24), direction=-73.5)
bridge_6.add_flag(PartyFlag.IS_STATIC)
bridge_6.add_flag(PartyFlag.LABEL_SMALL)
bridge_6.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_6.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_6.set_icon(icon.bridge_b)


bridge_7 = MBParty("bridge_7", name="{!}7", faction=fac.neutral, initial_cords=(-29.79, 76.84), direction=-64.0)
bridge_7.add_flag(PartyFlag.IS_STATIC)
bridge_7.add_flag(PartyFlag.LABEL_SMALL)
bridge_7.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_7.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_7.set_icon(icon.bridge_b)


bridge_8 = MBParty("bridge_8", name="{!}8", faction=fac.neutral, initial_cords=(-64.05, -6.0), direction=1.72)
bridge_8.add_flag(PartyFlag.IS_STATIC)
bridge_8.add_flag(PartyFlag.LABEL_SMALL)
bridge_8.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_8.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_8.set_icon(icon.bridge_b)


bridge_9 = MBParty("bridge_9", name="{!}9", faction=fac.neutral, initial_cords=(-64.95, -9.6), direction=-33.76)
bridge_9.add_flag(PartyFlag.IS_STATIC)
bridge_9.add_flag(PartyFlag.LABEL_SMALL)
bridge_9.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_9.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_9.set_icon(icon.bridge_b)


bridge_10 = MBParty("bridge_10", name="{!}10", faction=fac.neutral, initial_cords=(-75.32, -75.27), direction=-44.07)
bridge_10.add_flag(PartyFlag.IS_STATIC)
bridge_10.add_flag(PartyFlag.LABEL_SMALL)
bridge_10.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_10.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_10.set_icon(icon.bridge_b)


bridge_11 = MBParty("bridge_11", name="{!}11", faction=fac.neutral, initial_cords=(-24.39, 67.82), direction=81.3)
bridge_11.add_flag(PartyFlag.IS_STATIC)
bridge_11.add_flag(PartyFlag.LABEL_SMALL)
bridge_11.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_11.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_11.set_icon(icon.bridge_a)


bridge_12 = MBParty("bridge_12", name="{!}12", faction=fac.neutral, initial_cords=(-114.33, -1.94), direction=-35.5)
bridge_12.add_flag(PartyFlag.IS_STATIC)
bridge_12.add_flag(PartyFlag.LABEL_SMALL)
bridge_12.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_12.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_12.set_icon(icon.bridge_a)


bridge_13 = MBParty("bridge_13", name="{!}13", faction=fac.neutral, initial_cords=(-84.02, -7.0), direction=-17.7)
bridge_13.add_flag(PartyFlag.IS_STATIC)
bridge_13.add_flag(PartyFlag.LABEL_SMALL)
bridge_13.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_13.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_13.set_icon(icon.bridge_a)


bridge_14 = MBParty("bridge_14", name="{!}14", faction=fac.neutral, initial_cords=(-23.36, 75.8), direction=66.6)
bridge_14.add_flag(PartyFlag.IS_STATIC)
bridge_14.add_flag(PartyFlag.LABEL_SMALL)
bridge_14.add_flag(PartyFlag.IS_ALWAYS_VISIBLE)
bridge_14.add_flag(PartyFlag.HAS_NO_LABEL)
bridge_14.set_icon(icon.bridge_a)


looter_spawn_point = MBParty("looter_spawn_point", name="{!}looter sp", faction=fac.outlaws, initial_cords=(26.0, 77.0))
looter_spawn_point.add_flag(PartyFlag.IS_DISABLED)
looter_spawn_point.add_flag(PartyFlag.IS_STATIC)
looter_spawn_point.add_flag(PartyFlag.LABEL_SMALL)
looter_spawn_point.add_members(trp.looter, 15)


steppe_bandit_spawn_point = MBParty("steppe_bandit_spawn_point", name="the steppes", faction=fac.outlaws, initial_cords=(125.0, 9.0))
steppe_bandit_spawn_point.add_flag(PartyFlag.IS_DISABLED)
steppe_bandit_spawn_point.add_flag(PartyFlag.IS_STATIC)
steppe_bandit_spawn_point.add_flag(PartyFlag.LABEL_SMALL)
steppe_bandit_spawn_point.add_members(trp.looter, 15)


taiga_bandit_spawn_point = MBParty("taiga_bandit_spawn_point", name="the tundra", faction=fac.outlaws, initial_cords=(78.0, 84.0))
taiga_bandit_spawn_point.add_flag(PartyFlag.IS_DISABLED)
taiga_bandit_spawn_point.add_flag(PartyFlag.IS_STATIC)
taiga_bandit_spawn_point.add_flag(PartyFlag.LABEL_SMALL)
taiga_bandit_spawn_point.add_members(trp.looter, 15)


forest_bandit_spawn_point = MBParty("forest_bandit_spawn_point", name="the forests", faction=fac.outlaws, initial_cords=(-35.0, 18.0))
forest_bandit_spawn_point.add_flag(PartyFlag.IS_DISABLED)
forest_bandit_spawn_point.add_flag(PartyFlag.IS_STATIC)
forest_bandit_spawn_point.add_flag(PartyFlag.LABEL_SMALL)
forest_bandit_spawn_point.add_members(trp.looter, 15)


mountain_bandit_spawn_point = MBParty("mountain_bandit_spawn_point", name="the highlands", faction=fac.outlaws, initial_cords=(-90.0, -26.8))
mountain_bandit_spawn_point.add_flag(PartyFlag.IS_DISABLED)
mountain_bandit_spawn_point.add_flag(PartyFlag.IS_STATIC)
mountain_bandit_spawn_point.add_flag(PartyFlag.LABEL_SMALL)
mountain_bandit_spawn_point.add_members(trp.looter, 15)


sea_raider_spawn_point_1 = MBParty("sea_raider_spawn_point_1", name="the coast", faction=fac.outlaws, initial_cords=(48.5, 110.0))
sea_raider_spawn_point_1.add_flag(PartyFlag.IS_DISABLED)
sea_raider_spawn_point_1.add_flag(PartyFlag.IS_STATIC)
sea_raider_spawn_point_1.add_flag(PartyFlag.LABEL_SMALL)
sea_raider_spawn_point_1.add_members(trp.looter, 15)


sea_raider_spawn_point_2 = MBParty("sea_raider_spawn_point_2", name="the coast", faction=fac.outlaws, initial_cords=(-42.0, 76.7))
sea_raider_spawn_point_2.add_flag(PartyFlag.IS_DISABLED)
sea_raider_spawn_point_2.add_flag(PartyFlag.IS_STATIC)
sea_raider_spawn_point_2.add_flag(PartyFlag.LABEL_SMALL)
sea_raider_spawn_point_2.add_members(trp.looter, 15)


desert_bandit_spawn_point = MBParty("desert_bandit_spawn_point", name="the deserts", faction=fac.outlaws, initial_cords=(110.0, -100.0))
desert_bandit_spawn_point.add_flag(PartyFlag.IS_DISABLED)
desert_bandit_spawn_point.add_flag(PartyFlag.IS_STATIC)
desert_bandit_spawn_point.add_flag(PartyFlag.LABEL_SMALL)
desert_bandit_spawn_point.add_members(trp.looter, 15)


spawn_points_end = MBParty("spawn_points_end", name="{!}last spawn point", faction=fac.commoners)
spawn_points_end.add_flag(PartyFlag.IS_DISABLED)
spawn_points_end.add_flag(PartyFlag.IS_STATIC)
spawn_points_end.add_flag(PartyFlag.LABEL_SMALL)
spawn_points_end.add_members(trp.looter, 15)


reserved_1 = MBParty("reserved_1", name="{!}last spawn point", faction=fac.commoners)
reserved_1.add_flag(PartyFlag.IS_DISABLED)
reserved_1.add_flag(PartyFlag.IS_STATIC)
reserved_1.add_flag(PartyFlag.LABEL_SMALL)
reserved_1.add_members(trp.looter, 15)


reserved_2 = MBParty("reserved_2", name="{!}last spawn point", faction=fac.commoners)
reserved_2.add_flag(PartyFlag.IS_DISABLED)
reserved_2.add_flag(PartyFlag.IS_STATIC)
reserved_2.add_flag(PartyFlag.LABEL_SMALL)
reserved_2.add_members(trp.looter, 15)


reserved_3 = MBParty("reserved_3", name="{!}last spawn point", faction=fac.commoners)
reserved_3.add_flag(PartyFlag.IS_DISABLED)
reserved_3.add_flag(PartyFlag.IS_STATIC)
reserved_3.add_flag(PartyFlag.LABEL_SMALL)
reserved_3.add_members(trp.looter, 15)


reserved_4 = MBParty("reserved_4", name="{!}last spawn point", faction=fac.commoners)
reserved_4.add_flag(PartyFlag.IS_DISABLED)
reserved_4.add_flag(PartyFlag.IS_STATIC)
reserved_4.add_flag(PartyFlag.LABEL_SMALL)
reserved_4.add_members(trp.looter, 15)


reserved_5 = MBParty("reserved_5", name="{!}last spawn point", faction=fac.commoners)
reserved_5.add_flag(PartyFlag.IS_DISABLED)
reserved_5.add_flag(PartyFlag.IS_STATIC)
reserved_5.add_flag(PartyFlag.LABEL_SMALL)
reserved_5.add_members(trp.looter, 15)





