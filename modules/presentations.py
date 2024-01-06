# This Python file uses the following encoding: utf-8


import sys
sys.path.append("../data_objects/")

from presentation import Presentation, LoadEvent, MouseEnterLeaveEvent, RunEvent, MousePressEvent, StateChangedEvent
from simple_trigger import SimpleTrigger



# CUSTOM BATTLE MANAGER
game_custom_battle_designer = Presentation("game_custom_battle_designer", "mesh_cb_ui_main")
game_custom_battle_designer.set_manual_end_only()

event = LoadEvent()
def event_code():
    set_fixed_point_multiplier(1000)

    esc_info_text = MBTextOverlay(reg0, "@Press ESC to exit", tf_single_line)
    esc_info_text.set_color(0xFF000000)
    esc_info_text.set_size(2500, 2500)
    esc_info_text.set_position(100, 100)

    presentation_set_duration(999999)

event.codeBlock = event_code
game_custom_battle_designer.add_event(event)

event = MouseEnterLeaveEvent()
game_custom_battle_designer.add_event(event)

event = MousePressEvent()
game_custom_battle_designer.add_event(event)

event = RunEvent()
def event_code():
    if key_clicked(0x01): #or key_clicked(key_x):
        presentation_set_duration(0)
event.codeBlock = event_code
game_custom_battle_designer.add_event(event)



# TODO: add more from original game
