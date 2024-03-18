# This Python file uses the following encoding: utf-8

#import sys
#sys.path.append("../data_objects/")

from MBPlayer import MBPlayer
from MBOptions import MBOptions
from MBParty import MBParty
from game_menu import GameMenu, MenuOption

from scripts import *


game_start_0 = GameMenu("start_game_0", 0,
"Welcome adventurer, hopefully you will enjoy this new adventure through another world."
)

class GameStartContinue(MenuOption):
    def consequenceBlock(self):
        set_show_messages(1)
        jump_to_menu("mnu_start_game_1")

game_start_0.menuOptions.append(GameStartContinue("continue", "Continue..."))

game_start_go_back = MenuOption("go_back", "Go back...")

def game_start_go_back_conseq():
    change_screen_quit()

game_start_go_back.consequenceBlock = game_start_go_back_conseq
game_start_0.menuOptions.append(game_start_go_back)



# the second menu will always be used for display on the map after all is done, for some reason
welcome_menu = GameMenu("welcome_menu", 0, "Welcome on the map!")
welcome_menu_continue = MenuOption("continue", "Continue...")
def conseq():
    change_screen_return()
welcome_menu_continue.consequenceBlock = conseq
welcome_menu.menuOptions.append(welcome_menu_continue)



#("start_game_1",menu_text_color(0xFF000000)|mnf_disable_all_keys,
game_start_1 = GameMenu("start_game_1", 0, "Select your skin.")
game_start_1_male = MenuOption("start_male", "Skin1 | Male")
def setSkinMale():
    troop_set_type("trp_player", 0)
    change_screen_return()
game_start_1_male.consequenceBlock = setSkinMale
game_start_1.menuOptions.append(game_start_1_male)
game_start_1_female = MenuOption("start_female", "Skin2 | Female")
def setSkinFemale():
    troop_set_type("trp_player", 1)
    change_screen_return()
game_start_1_female.consequenceBlock = setSkinFemale
game_start_1.menuOptions.append(game_start_1_female)
#game_start_1_undead = MenuOption("start_undead", "Skin3 | Undead")
#def setSkin3():
#    troop_set_type("trp_player", 2)
#    change_screen_return()
#game_start_1_undead.consequenceBlock = setSkin3
#game_start_1.menuOptions.append(game_start_1_undead)



reports = GameMenu("reports", 0, "Reports test {reg1}")
def condition():
    reg1 = 123456
reports.conditionBlock = condition

reports_continue = MenuOption("continue", "Continue...")
def conseq():
    change_screen_return()
reports_continue.consequenceBlock = conseq
reports.menuOptions.append(reports_continue)


town_menu = GameMenu("town", 0, "Test Town")

town_leave = MenuOption("town_leave", "Leave...")
town_leave.consequenceBlock = conseq
town_menu.menuOptions.append(town_leave)

town_leave = MenuOption("test_position", "TEST POSITION")
def conseq():
    for partyx in __all_parties__:
        partyx = MBParty(partyx)
        if partyx.is_active():
            partyx.get_position(pos1)
            position_get_x(x, pos1)
            x += 100
            position_set_x(pos1, x)
            partyx.set_position(pos1)
            print("DEBUG -", pos1)
town_leave.consequenceBlock = conseq
town_menu.menuOptions.append(town_leave)


town_list_test = MenuOption("test_mission", "TEST MISSION")
def conseq():
    set_jump_mission("mt_village_training")
    modify_visitors_at_site("scn_random_scene")
    reset_visitors(),
    set_visitor(0, "trp_player", 1)
    set_visitors(1, "trp_looter", 2)
    jump_to_scene("scn_random_scene",0)
    change_screen_mission()
town_list_test.consequenceBlock = conseq
town_menu.menuOptions.append(town_list_test)


simple_encounter = GameMenu("simple_encounter", 0, "Simple Encounter here.")
leave_m = MenuOption("leave", "Leave...")
def conseq():
    change_screen_return()
leave_m.consequenceBlock = conseq
simple_encounter.menuOptions.append(leave_m)


