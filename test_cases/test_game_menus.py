# This Python file uses the following encoding: utf-8
from MBPlayer import MBPlayer
from MBOptions import MBOptions
from MBParty import MBParty
from game_menu import GameMenu, MenuOption


game_start_0 = GameMenu("start_game_0", 0,
"Welcome adventurer, hopefully you will enjoy this new adventure through another world."
)

class GameStartContinue(MenuOption):
    def consequenceBlock(self):
        reg12 = 255
        reg13 = 500
        s0 = "Current gold: {reg13}"
        s1 = "Current xp: {reg12}"
        s2 = "str_yes"
        helloWorld()
        change_screen_return(0)
        set_show_messages(1)
        #jump_to_menu("mnu_start_game_1")

#class GameStartGoBack(MenuOption):
#    def consequenceBlock(self):
#        change_screen_quit()



game_start_0.menuOptions.append(GameStartContinue("continue", "Continue..."))

game_start_go_back = MenuOption("go_back", "Go back...")

def game_start_go_back_conseq():
    if is_edit_mode_enabled():
        # do nothing
        pass
    else:
        change_screen_quit()

game_start_go_back.consequenceBlock = game_start_go_back_conseq
game_start_0.menuOptions.append(game_start_go_back)


game_start_hack = MenuOption("hack", "I hacked it!")

def condition():
    if is_edit_mode_enabled():
        pass

def consequence():
    print("LOL")

game_start_hack.conditionBlock = condition
game_start_hack.consequenceBlock = consequence
game_start_0.menuOptions.append(game_start_hack)



