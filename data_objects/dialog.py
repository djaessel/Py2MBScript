# This Python file uses the following encoding: utf-8


class Dialog:
    # During a dialog, the dialog lines are scanned from top to bottom.
    # If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
    # If the dialog-line is spoken by another, the first (top-most) matching line is selected.
    #
    #  Each dialog line contains the following fields:
    # 1) Dialogue partner: This should match the person player is talking to.
    #    Usually this is a troop-id.
    #    You can also use a party-template-id by appending '|party_tpl' to this field.
    #    Use the constant 'anyone' if you'd like the line to match anybody.
    #    Appending '|plyr' to this field means that the actual line is spoken by the player
    #    Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
    #       (You must make sure that this third person is present on the scene)
    #
    # 2) Starting dialog-state:
    #    During a dialog there's always an active Dialog-state.
    #    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
    #    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
    #    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
    #    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
    #    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
    #    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
    #    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
    # 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.
    # 4) Dialog Text (string):
    # 5) Ending dialog-state:
    #    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
    # 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
    # 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over

    def __init__(self, dialog_partner : str, text : str, starting_state : str = "start", ending_state : str = "close_window", voice_over : str = ""):
        self.dialog_partner = dialog_partner
        self.text = text
        self.starting_state = starting_state
        self.ending_state = ending_state
        self.voice_over = voice_over


    def conditionBlock(self):
        pass


    def consequenceBlock(self):
        pass

