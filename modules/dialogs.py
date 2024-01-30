# This Python file uses the following encoding: utf-8

import sys
sys.path.append("./data_objects/")

from dialog import Dialog

dialog_start = Dialog("anyone", "Hi there!", starting_state="start", ending_state="hello_world")
dialog_start_answer = Dialog("anyone", "Hi!", is_player_text=True, starting_state="hello_world")
