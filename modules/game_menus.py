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
        change_screen_return()
        set_show_messages(1)

game_start_0.menuOptions.append(GameStartContinue("continue", "Continue..."))

game_start_go_back = MenuOption("go_back", "Go back...")

def game_start_go_back_conseq():
    change_screen_quit()

game_start_go_back.consequenceBlock = game_start_go_back_conseq
game_start_0.menuOptions.append(game_start_go_back)


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




