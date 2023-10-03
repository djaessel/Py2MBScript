from header_operations import *
from header_common import *

presentations = [

("test1",0,0,[

(ti_on_presentation_load, [
(display_message, "@Hello World! - {s0}"),
]),

(ti_on_presentation_event_state_change, [
(display_message, "@Hello World!!!"),
]),

]),

] # PRESENTATIONS END
