# This Python file uses the following encoding: utf-8

from simple_trigger import SimpleTrigger


#ti_on_presentation_load  = -60.0 #can only be used in module_presentations triggers
#ti_on_presentation_run   = -61.0 #can only be used in module_presentations triggers
# Trigger Param 1: current time in miliseconds
#ti_on_presentation_event_state_change = -62.0 #can only be used in module_presentations triggers
# Trigger Param 1: id of the object that has the event
# Trigger Param 2: value (when available)
#ti_on_presentation_mouse_enter_leave  = -63.0 #can only be used in module_presentations triggers
# Trigger Param 1: id of the object that mouse enters/leaves
# Trigger Param 2: 0 if mouse enters, 1 if mouse leaves
#ti_on_presentation_mouse_press        = -64.0 #can only be used in module_presentations triggers
# Trigger Param 1: id of the object that mouse is pressed on
# Trigger Param 2: 0: left mouse button, 1 right mouse button, 2 middle mouse button



class Presentation:
    def __init__(self, id, mesh_id="0"):
        self.id = id
        self.mesh_id = mesh_id
        self.is_read_only = False
        self.has_manual_end_only = False
        self.triggers = []

        self.has_load_event = False
        self.has_run_event = False
        self.has_change_event = False
        self.has_mouse_enter_leave_event = False
        self.has_mouse_press_event = False


    def add_trigger(self, trigger : SimpleTrigger, remove_alt : bool = False):
        if trigger.triggerInterval == -60.0 and not self.has_load_event:
            self.triggers.append(trigger)
        elif trigger.triggerInterval == -60.0:
            print(self.id, "already has load event!")

        if trigger.triggerInterval == -61.0 and not self.has_run_event:
            self.triggers.append(trigger)
        elif trigger.triggerInterval == -61.0:
            print(self.id, "already has run event!")

        if trigger.triggerInterval == -62.0 and not self.has_change_event:
            self.triggers.append(trigger)
        elif trigger.triggerInterval == -62.0:
            print(self.id, "already has state changed event!")

        if trigger.triggerInterval == -63.0 and not self.has_mouse_enter_leave_event:
            self.triggers.append(trigger)
        elif trigger.triggerInterval == -63.0:
            print(self.id, "already has mouse enter leave event!")

        if trigger.triggerInterval == -64.0 and not self.has_mouse_press_event:
            self.triggers.append(trigger)
        elif trigger.triggerInterval == -64.0:
            print(self.id, "already has mouse press event!")

        if remove_alt:
            print("TODO: override old trigger with new one")


    def set_read_only(self, val : bool = True):
        self.is_read_only = val


    def set_manual_end_only(self, val : bool = True):
        self.has_manual_end_only = val

