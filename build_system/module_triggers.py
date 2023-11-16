from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *

from module_constants import *

triggers = [

(24, 0, 0, [
(assign,":water",1),
(try_begin),
    (eq,1,1),
    (assign,":water",4),
(try_end),
(assign, reg0, ":water"),
], [
(display_message, "@Hello World!"),
]),

(12, 0, 0, [
], [
(assign,":fishCount",1),
(assign,":waterLevel",1),
(get_operation_set_version, ":versionx"),
(try_begin),
    (gt,":versionx",0),
    (le,":versionx",1101),
    (assign, reg0, ":versionx"),
    (display_message, "@{reg0}"),
(try_end),
(try_for_range, ":waterLevel", ":waterLevel", 19),
    (assign, reg0, ":waterLevel"),
    (display_message, "@{reg0}"),
    (try_for_range, ":fishCount", ":fishCount", 12),
        (assign, reg0, ":fishCount"),
        (display_message, "@{reg0}"),
    (try_end),
(try_end),
]),

(0, 0, 128.0, [
(eq,1,0),
(display_message, "@DISABLED!"),
], [
(display_message, "@Pump water!"),
]),

]
