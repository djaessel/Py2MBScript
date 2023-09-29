# This Python file uses the following encoding: utf-8
from MBPlayer import MBPlayer
from MBOptions import MBOptions
from MBParty import MBParty
from game_menu import GameMenu, MenuOption


game_start_0 = GameMenu(
"start_game_0", 0,
"Welcome adventurer, hopefully you will enjoy this new adventure through another world."
)

class GameStartContinue(MenuOption):
    def consequenceBlock(self):
        jump_to_menu("mnu_start_game_1")

class GameStartGoBack(MenuOption):
    def consequenceBlock(self):
        change_screen_quit()

game_start_0.menuOptions.append(GameStartContinue("continue", "Continue..."))
game_start_0.menuOptions.append(GameStartContinue("go_back", "Go back..."))
