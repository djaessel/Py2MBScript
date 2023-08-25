from header_operations import *
from header_common import *

simple_triggers = [

(24, [
(try_begin),
    (is_edit_mode_enabled),
    (display_message, "@Hello World"),
(try_end),
]),

(12, [
(assign,":fishCount",1),
(assign,":waterLevel",1),
(get_operation_set_version, ":versionx"),
(try_begin),
    (gt,":versionx",0),
    (le,":versionx",1101),
    (profile_get_banner_id, ":banner_id"),
    (try_begin),
        (this_or_next|gt,":banner_id",20),
        (this_or_next|eq,":banner_id",0),
        (eq,":banner_id",10),
        (assign, reg0, ":versionx"),
        (display_message, "@{reg0}"),
        (try_begin),
            (eq,":versionx",1011),
            (display_message, "@YES!"),
        (else_try),
            (display_message, "@Nope"),
            (display_message, "@DOPE"),
        (try_end),
    (try_end),
(try_end),
]),

]
