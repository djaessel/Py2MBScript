import os
import sys


operations = dict()

conditionals = [
    "ge",
    "eq",
    "gt",
    "is_between",
    "entering_town",
    "map_free",
    "encountered_party_is_attacker",
    "conversation_screen_is_active",
    "in_meta_mission",
    "troop_is_hero",
    "troop_is_wounded",
    "key_is_down",
    "key_clicked",
    "game_key_is_down",
    "game_key_clicked",
    "hero_can_join",
    "hero_can_join_as_prisoner",
    "party_can_join",
    "party_can_join_as_prisoner",
    "troops_can_join",
    "troops_can_join_as_prisoner",
    "party_can_join_party",
    "main_party_has_troop",
    "party_is_in_town",
    "party_is_in_any_town",
    "party_is_active",
    "player_has_item",
    "troop_has_item_equipped",
    "troop_is_mounted",
    "troop_is_guarantee_ranged",
    "troop_is_guarantee_horse",
    "player_is_active",
    "multiplayer_is_server",
    "multiplayer_is_dedicated_server",
    "game_in_multiplayer_mode",
    "player_is_admin",
    "player_is_busy_with_menus",
    "player_item_slot_is_picked_up",
    "check_quest_active",
    "check_quest_finished",
    "check_quest_succeeded",
    "check_quest_failed",
    "check_quest_concluded",
    "is_trial_version",
    "is_edit_mode_enabled",
    "troop_slot_eq",
    "party_slot_eq",
    "faction_slot_eq",
    "scene_slot_eq",
    "party_template_slot_eq",
    "agent_slot_eq",
    "quest_slot_eq",
    "item_slot_eq",
    "player_slot_eq",
    "team_slot_eq",
    "scene_prop_slot_eq",
    "troop_slot_ge",
    "party_slot_ge",
    "faction_slot_ge",
    "scene_slot_ge",
    "party_template_slot_ge",
    "agent_slot_ge",
    "quest_slot_ge",
    "item_slot_ge",
    "player_slot_ge",
    "team_slot_ge",
    "scene_prop_slot_ge",
    "position_has_line_of_sight_to_position",
    "position_is_behind_position",
    "is_presentation_active",
    "all_enemies_defeated",
    "race_completed_by_player",
    "num_active_teams_le",
    "main_hero_fallen",
    "lt",
    "neq",
    "le",
    "teams_are_enemies",
    "agent_is_alive",
    "agent_is_wounded",
    "agent_is_human",
    "agent_is_ally",
    "agent_is_non_player",
    "agent_is_defender",
    "agent_is_active",
    "agent_is_routed",
    "agent_is_in_special_mode",
    "agent_is_in_parried_animation",
    "class_is_listening_order",
    "agent_check_offer_from_agent",
    "entry_point_is_auto_generated",
    "scene_prop_has_agent_on_it",
    "agent_is_alarmed",
    "agent_is_in_line_of_sight",
#    "scene_prop_get_instance",
#    "scene_item_get_instance",
    "scene_allows_mounted_units",
    "prop_instance_is_valid",
#    "cast_ray",
    "prop_instance_intersects_with_prop_instance",
    "agent_has_item_equipped",
    "map_get_land_position_around_position",
    "map_get_water_position_around_position",
    "mission_tpl_are_all_agents_spawned",
    "is_zoom_disabled",
    "is_currently_night",
#    "store_random_party_of_template",
    "str_is_empty",
    "item_has_property",
    "item_has_capability",
    "item_has_modifier",
    "item_has_faction",
]


LOCAL_MIN = 0x1100000000000000
LOCAL_MAX = 1224979098644775040 # max. 128 local variables

REG0 = 72057594037927936
REG127 = 72057594037928063 # max. 128 registers

QUICKSTRING_MIN = 1585267068834414592
QUICKSTRING_MAX = 1600000000000000000

GLOBAL_MIN = 144115188075855872
GLOBAL_MAX = 145000000000000000

# TYPES

TRP_PLAYER = 360287970189639680
TROOP_MAX = 370000000000000000

SCRIPT_MIN = 936748722493063168
SCRIPT_MAX = 940000000000000000

STRING_MIN = 216172782113783808
STRING_MAX = 217000000000000000

SPR_MIN = 1080863910568919040
SPR_MAX = 1100000000000000000

PRSNT_MIN = 1513209474796486656
PRSNT_MAX = 1513210000000000000

FAC_MIN = 432345564227567616
FAC_MAX = 433000000000000000

P_MAIN_PARTY = 648518346341351424
P_MAX = 648600000000000000

ITM_MIN = 288230376151711744
ITM_MAX = 290000000000000000

SCENE_MIN = 720575940379279360
SCENE_MAX = 720575940380000000

MESH_MIN = 1441151880758558720
MESH_MAX = 1450000000000000000

PT_MIN = 576460752303423488
PT_MAX = 576500000000000000

MT_MIN = 792633534417207296
MT_MAX = 792700000000000000

SKL_MIN = 1369094286720630784
SKL_MAX = 1369094286720700000

SND_MIN = 1152921504606846976
SND_MAX = 1152921504607000000

PSYS_MIN = 1008806316530991104
PSYS_MAX = 1009000000000000000

MENU_MIN = 864691128455135232
MENU_MAX = 865000000000000000

QUEST_MIN = 504403158265495552
QUEST_MAX = 504500000000000000

TABLEAU_MAT_MIN = 1729382256910270464
TABLEAU_MAT_MAX = 1730000000000000000

TRACK_MIN = 1657324662872342528
TRACK_MAX = 1660000000000000000

MAP_ICON_MIN = 129703669268270
MAP_ICON_MAX = 130000000000000

#INFO_PAGE
#DIALOG
#POST_FX

ANIM_MIN = 1801439850948198400
ANIM_MAX = 1810000000000000000 # public const ulong ANIM_MAX = ulong.MaxValue - int.MaxValue

globalVariables = []




def lookupData(data):
    d = data
    if is_int(data):
        x = int(data)
        if x >= LOCAL_MIN and x <= LOCAL_MAX:
            d = "\":var" + str(x - LOCAL_MIN + 1) + "\""
        elif x >= REG0 and x <= REG127:
            d = "reg" + str(x - REG0)
        elif x >= GLOBAL_MIN and x < GLOBAL_MAX:
            d = "\"$" + globalVariables[x - GLOBAL_MIN] + "\""
        else:
            pass
    return d


def readOperationsFile():
    with open("../build_system/header_operations.py") as f:
        for line in f:
            if "=" in line:
                tmp = line.replace(" ", "").split('#')[0].strip()
                if len(tmp) > 0:
                    tmp2 = tmp.split('=')
                    operations[tmp2[1]] = tmp2[0]


def readGlobalVariables():
    with open("variables.txt") as f:
        for line in f:
            globalVariables.append(line.rstrip('\n'))



def is_int(data):
    try:
        _ = int(data)
    except:
        return False
    return True


def decompileScript(name : str, show : bool = False):
    data = []
    with open("scripts.txt") as f:
        found = False
        for line in f:
            if line.startswith(name):
                found = True
            elif found:
                tmp = line.strip().split(' ')
                if show:
                    print(tmp)
                activeCount = -1
                for i in range(1, len(tmp)):
                    if activeCount <= 0:
                        itmp = int(tmp[i])

                        if (itmp & 0x40000000) == 0x40000000: # this_or_next
                            vv = str(itmp & 0xFFFF)
                            newData = "this_or_next|" + operations[vv] + ","
                        elif (itmp & 0x80000000) == 0x80000000: # neg
                            vv = str(itmp & 0xFFFF)
                            newData = "neg|" + operations[vv] + ","
                        else:
                            newData = operations[tmp[i]] + ","

                        activeCount = int(tmp[i+1]) + 1
                        for ix in range(i + 2, i + 1 + activeCount):
                            newData += lookupData(tmp[ix]) + ","
                        newData = newData.rstrip(',')
                        data.append(newData)
                    else:
                        activeCount -= 1
                break
    return data


def varI(v):
    if is_int(v):
        v = "s" + v
    return v


def convertToPy(data : list):
    data = convertToPy1(data)
    #print(formatGoodText(data))
    data = convertToPy2(data)
    return data


def convertToPy1(data : list):
    formatex = []
    curLine = ""
    condit = False
    lastWasCondit = False
    isInliner = False
    insertEnds = []
    for i in range(len(data)):
        code = data[i]
        firstCode = code.split(',')[0]

        if code == "try_begin":
            if condit:
                formatex.append(curLine)
            condit = True
            curLine = "if;"
        elif code == "else_try":
            if condit:
                formatex.append(curLine)
            condit = True
            curLine = "elif;"
        elif code == "try_end":
            formatex.append("#end")
            condit = False
        elif condit and (firstCode in conditionals or "this_or_next|" in firstCode or "neg|" in firstCode):
            lastWasCondit = True
            curLine += code + ";"
        elif firstCode in conditionals or "this_or_next|" in firstCode or "neg|" in firstCode:
            condit = True
            #lastWasCondit = True
            print("SELLE:", i, code)
            curLine = "if;" + code + ";"
            if not isInliner:
                insertEnds.append(len(formatex))
                isInliner = True
        elif "," in code:
            tmp = code.split(',')
            if "assign" == tmp[0]:
                xyz = varS(tmp[1]) + " = " + varS(tmp[2])
            elif "store" in tmp[0] or "get_" in tmp[0]:
                xyz = tmp[0] + "("
                for i in range(1, len(tmp)):
                    tmp[i] = varS(tmp[i])
                if len(tmp) > 2:
                    xyz += ",".join(tmp[2:])
                xyz = varI(tmp[1]) + " = " + xyz
                xyz += ")"
            elif "try_for_range" in tmp[0]:
                step = 1
                if "backwards" in tmp[0]:
                    step = -1
                formatex.append("for;" + ";".join(tmp[1:]) + ";" + str(step))
            elif "try_for_parties" == tmp[0]:
                formatex.append("for;" + tmp[1] + ";__all_parties__")
            elif "try_for_players" == tmp[0]:
                formatex.append("for;" + tmp[1] + ";__all_players__")
            elif "try_for_prop_instances" == tmp[0]:
                formatex.append("for;" + tmp[1] + ";__all_prop_instances__")
            elif "try_for_agents" == tmp[0]:
                formatex.append("for;" + tmp[1] + ";__all_agents__")
            else:
                xyz = tmp[0] + "("
                for i in range(1, len(tmp)):
                    tmp[i] = varS(tmp[i])
                if len(tmp) > 1:
                    xyz += ",".join(tmp[1:])
                xyz += ")"
            formatex.append(xyz)
            condit = False
        else:
            formatex.append(code)
            condit = False

        print("CURLINE:", curLine)

        if not condit and (lastWasCondit or curLine == "elif;"):
            if curLine == "elif;":
                curLine = "else"
            formatex.insert(len(formatex) - 1, curLine)
            curLine = ""
            lastWasCondit = False
            isInliner = False

    print(insertEnds)

    insertEnds.reverse()
    for i in insertEnds:
        for ix in range(i, len(formatex)):
            if formatex[ix] == "#end" and ix < 99:
                formatex.insert(ix, "#end")
                print("IX:", ix, "#end")
                break

    return formatex


def varS(txt : str):
    if txt.startswith("\"") and txt.endswith("\""):
        txt = txt.strip('"')
        if txt.startswith(":"):
            txt = txt.lstrip(':')
        elif txt.startswith("$"):
            txt = "_" + txt.lstrip('$')
    return txt


def funcS(txt : str):
    if len(txt.strip()) > 0 and not "," in txt and not " " in txt:
        txt += "()"
    elif len(txt.strip()) > 0 and "," in txt:
        tmp = txt.split(',')
        for i in range(1, len(tmp)):
            tmp[i] = varS(tmp[i])
        txt = tmp[0] + "(" + ",".join(tmp[1:]) + ")"
    return txt


def convertCondi(tmx : str, negate : bool = False):
    tmp = tmx.split(',')
    if tmp[0] == "eq":
        operator = " == "
        if negate:
            operator = " != "
        xyz = varS(tmp[1]) + operator + varS(tmp[2])
    elif tmp[0] == "gt":
        operator = " > "
        if negate:
            operator = " <= "
        xyz = varS(tmp[1]) + operator + varS(tmp[2])
    elif tmp[0] == "ge":
        operator = " >= "
        if negate:
            operator = " < "
        xyz = varS(tmp[1]) + operator + varS(tmp[2])
    else:
        xyz = funcS(tmx)
        if negate:
            xyz = "not " + funcS(tmx)
    return xyz


def convertToPy2(data : list):
    datax = []
    for c in data:
        if c.startswith("if;") or c.startswith("elif;") or c == "else":
            tmp = c.split(';')
            xyz = "if "
            if "elif" in c:
                xyz = "elif "
            elif c == "else":
                xyz = c
            isOr = False
            for iii in range(1, len(tmp)):
                tmp2 = tmp[iii].split(',')
                if tmp2[0].startswith("this_or_next|"):
                    tmp3 = tmp[iii].split('|')[1]
                    xyz += convertCondi(tmp3)
                    isOr = True
                elif tmp2[0].startswith("neg|"):
                    tmp3 = tmp[iii].split('|')[1]
                    xyz += convertCondi(tmp3, True)
                else:
                    xyz += convertCondi(tmp[iii])

                if iii + 2 < len(tmp):
                    if isOr:
                        xyz += " or "
                        isOr = False
                    else:
                        xyz += " and "
            if xyz == "elif ":
                xyz = "else"
            xyz += ":"
            datax.append(xyz)
        elif c.startswith("for;"):
            tmp = c.split(';')
            xyz = "for " + varS(tmp[1]) + " in "
            if is_int(tmp[-1]):
                xyz += "range(" + varS(tmp[2]) + ", " + varS(tmp[3])
                itmp = int(tmp[-1])
                if itmp < 0:
                    xyz + ", " + tmp[-1]
                xyz += "):"
            datax.append(xyz)
        else:
            datax.append(c)
    return datax


def formatGoodText(data : list):
    sx = ""
    indentx = 0
    for s in data:
        st = s
        if indentx > 0 and (s.startswith("elif") or s == "else:" or s == "#end"):
            indentx -= 1
        st = "\t" * indentx + st
        sx += st + "\n"
        if s.startswith("if") or s.startswith("elif") or s == "else:" or s.startswith("for"):
            indentx += 1
    return sx



# main program
readGlobalVariables()
readOperationsFile()

scriptName = "game_enable_cheat_menu"
if len(sys.argv) > 1:
    scriptName = sys.argv[1]

print("Converting:", scriptName)

datac = decompileScript(scriptName)
txt = formatGoodText(datac)
print(txt)
datap = convertToPy(datac)
txt = formatGoodText(datap)
print(txt)




