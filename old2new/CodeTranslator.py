import os
import sys


module_path = "/home/djaessel/warband/Modules/Native/"

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
#    "scene_prop_get_instance", # check
#    "scene_item_get_instance", # check
    "scene_allows_mounted_units",
    "prop_instance_is_valid",
#    "cast_ray", # check
    "prop_instance_intersects_with_prop_instance",
    "agent_has_item_equipped",
    "map_get_land_position_around_position",
    "map_get_water_position_around_position",
    "mission_tpl_are_all_agents_spawned",
    "is_zoom_disabled",
    "is_currently_night",
#    "store_random_party_of_template", # check
    "str_is_empty",
    "item_has_property",
    "item_has_capability",
    "item_has_modifier",
    "item_has_faction",
]

math_ops = [
    "val_mod",
    "val_sub",
    "val_add",
    "val_mul",
    "val_div",
    "store_add",
    "store_sub",
    "store_div",
    "store_mul",
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


localVarNames = dict()
localVarDict = dict()

globalVariables = []
quickStrings = []
sceneProps = []
gameStrings = []
troops = []
scripts = []
presentations = []
factions = []
parties = []
scenes = []
items = []
meshes = []
partyTemplates = []
missionTemplates = []
skills = []
sounds = []
particleSystems = []
menus = []
quests = []
tableaus = []
tracks = []
icons = []
animations = []


def lookupData(funcName : str, data : str, parax : list, all : list, index : int):
    d = data
    if is_int(data):
        x = int(data)
        if x >= LOCAL_MIN and x <= LOCAL_MAX:
            varIdx = str(x - LOCAL_MIN + 1).zfill(3)
            if varIdx in localVarDict: # TODO: Next step is to also rewrite when already in here
                d = "\":" + localVarDict[varIdx] + "\""
            elif "try_for_range" in funcName and len(parax) >= 2:
                t1 = lookupData(funcName, parax[0], [], [], index + 1).split('.')
                t2 = lookupData(funcName, parax[1], [], [], index + 2).split('.')
                if len(t1) > 1 and len(t2) > 1 and t1[0] == t2[0]:
                    y = t1[0] + "_" + varIdx
                    d = "\":" + y + "\""
                    localVarDict[varIdx] = y
            elif funcName in localVarNames:
                if index < len(localVarNames[funcName]):
                    y = localVarNames[funcName][index]
                    if y != "0":
                        y = y.replace("[X]", "_" + varIdx)
                        d = "\":" + y + "\""
                        localVarDict[varIdx] = y
                        for i in range(len(all)):
                            all[i] = all[i].replace("\":var" + varIdx + "\"", d)
                else:
                    print("WARNING: LOOKUP >", funcName, data, index, localVarNames[funcName])
            if d == data:
                d = "\":var" + varIdx + "\""
        elif x >= REG0 and x <= REG127:
            d = "reg" + str(x - REG0)
        elif x >= GLOBAL_MIN and x < GLOBAL_MAX:
            d = "\"$" + globalVariables[x - GLOBAL_MIN] + "\""
        elif x >= QUICKSTRING_MIN and x < QUICKSTRING_MAX:
            d = "\"" + quickStrings[x - QUICKSTRING_MIN][1] + "\""
        elif x >= SPR_MIN and x < SPR_MAX:
            d = "spr." + sceneProps[x - SPR_MIN][0][0][4:]
        elif x >= TRP_PLAYER and x < TROOP_MAX:
            d = "trp." + troops[x - TRP_PLAYER][0][0][4:]
        elif x >= SCRIPT_MIN and x < SCRIPT_MAX:
            d = "script." + scripts[x - SCRIPT_MIN][0][0]
        elif x >= STRING_MIN and x < STRING_MAX:
            d = "gstr." + gameStrings[x - STRING_MIN][0][4:]
        elif x >= PRSNT_MIN and x < PRSNT_MAX:
            d = "prsnt." + presentations[x - PRSNT_MIN][0][0][6:]
        elif x >= FAC_MIN and x < FAC_MAX:
            d = "fac." + factions[x - FAC_MIN][0][0][4:]
        elif x >= P_MAIN_PARTY and x < P_MAX:
            d = "p." + parties[x - P_MAIN_PARTY][0][3][2:]
        elif x >= ITM_MIN and x < ITM_MAX:
            d = "itm." + items[x - ITM_MIN][0][0][4:]
        elif x >= SCENE_MIN and x < SCENE_MAX:
            d = "scn." + scenes[x - SCENE_MIN][0][0][4:]
        elif x >= MESH_MIN and x < MESH_MAX:
            d = "mesh." + meshes[x - MESH_MIN][0][5:]
        elif x >= PT_MIN and x < PT_MAX:
            d = "pt." + partyTemplates[x - PT_MIN][0][3:]
        elif x >= MT_MIN and x < MT_MAX:
            d = "mt." + missionTemplates[x - MT_MIN][0][0][4:]
        elif x >= SKL_MIN and x < SKL_MAX:
            d = "skl." + skills[x - SKL_MIN][0][4:]
        elif x >= SND_MIN and x < SND_MAX:
            d = "snd." + sounds[x - SND_MIN][0][4:]
        elif x >= PSYS_MIN and x < PSYS_MAX:
            d = "psys." + particleSystems[x - PSYS_MIN][0][0][5:]
        elif x >= MENU_MIN and x < MENU_MAX:
            d = "mnu." + menus[x - MENU_MIN][0][0][4:]
        elif x >= QUEST_MIN and x < QUEST_MAX:
            d = "qst." + quests[x - QUEST_MIN][0][4:]
        elif x >= TABLEAU_MAT_MIN and x < TABLEAU_MAT_MAX:
            d = "tab." + tableaus[x - TABLEAU_MAT_MIN][0][0][4:]
        elif x >= TRACK_MIN and x < TRACK_MAX:
            d = "track." + tracks[x - TRACK_MIN][0].split('.')[0]
        elif x >= MAP_ICON_MIN and x < MAP_ICON_MAX:
            d = "icon." + icons[x - MAP_ICON_MIN][0][0]
        elif x >= ANIM_MIN and x < ANIM_MAX:
            d = "anim." + animations[x - ANIM_MIN][0][0]
        else:
            if x >= 0 and x < 0xffff:
                if funcName == "call_script" and index == 0:
                    d = "script." + scripts[x][0][0]
                elif ("troop_get" in funcName or "troop_set" in funcName) and index == 1: # why 1? -> TODO: check that and also create list with possible OP Codes
                    d = "trp." + troops[x][0][0][4:]
                elif ("item_get" in funcName or "item_set" in funcName) and index == 1: # why 1? -> TODO: check that and also create list with possible OP Codes
                    d = "itm." + items[x][0][0][4:]
                #else: # for example slots and such things
                #    pass
            #else: # for example slots and such things
            #    pass
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
    with open(module_path + "variables.txt") as f:
        for line in f:
            globalVariables.append(line.rstrip('\n'))


def readQuickStrings():
    with open(module_path + "quick_strings.txt") as f:
        for line in f:
            if line.startswith("qstr_"):
                tmp = line.split(' ')
                quickStrings.append((tmp[0], "@" + tmp[1].replace("_", " ").rstrip('\n')))


def readSceneProps():
    with open(module_path + "scene_props.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("spr_"):
                tmp = line.strip().split(' ')
                sceneProps.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                sceneProps[len(sceneProps)-1].append(line.strip().split(' '))
            lineCount += 1


def readTroops():
    with open(module_path + "troops.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("trp_"):
                tmp = line.strip().split(' ')
                troops.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                troops[len(troops)-1].append(line.strip().split(' '))
            lineCount += 1


def readScripts():
    with open(module_path + "scripts.txt") as f:
        lineCount = 0
        for line in f:
            if lineCount >= 2 and not line.startswith(" "):
                tmp = line.strip().split(' ')
                scripts.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                scripts[len(troops)-1].append(line.strip().split(' '))
            lineCount += 1


def readScenes():
    with open(module_path + "scenes.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("scn_"):
                tmp = line.strip().split(' ')
                scenes.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                scenes[len(scenes)-1].append(line.strip().split(' '))
            lineCount += 1


def readItems():
    with open(module_path + "item_kinds1.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith(" itm_"):
                tmp = line.strip().split(' ')
                tmp[0] = tmp[0].lstrip()
                items.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                items[len(items)-1].append(line.strip().split(' '))
            lineCount += 1


def readParties():
    with open(module_path + "parties.txt") as f:
        lineCount = 0
        for line in f:
            if " p_" in line:
                tmp = line.strip().split(' ')
                parties.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                parties[len(parties)-1].append(line.strip().split(' '))
            lineCount += 1


def readFactions():
    with open(module_path + "factions.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("fac_") or " fac_" in line:
                tmp = line.strip().split(' ')
                if not line.startswith("fac_"):
                    factions[len(factions)-1].append(tmp[0])
                    factions.append([tmp[1:]])
                else:
                    factions.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                factions[len(factions)-1].append(line.strip().split(' '))
            lineCount += 1


def readPresentations():
    with open(module_path + "presentations.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("prsnt_"):
                tmp = line.strip().split(' ')
                presentations.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                presentations[len(presentations)-1].append(line.strip().split(' '))
            lineCount += 1


def readGameStrings():
    with open(module_path + "strings.txt", encoding="latin1") as f:
        for line in f:
            if line.startswith("str_"):
                tmp = line.strip().split(' ')
                gameStrings.append((tmp[0], tmp[1].replace("_", " ")))


def readMeshes():
    with open(module_path + "meshes.txt") as f:
        for line in f:
            if line.startswith("mesh_"):
                tmp = line.strip().split(' ')
                meshes.append(tmp)


def readPartyTemplates():
    with open(module_path + "party_templates.txt") as f:
        for line in f:
            if line.startswith("pt_"):
                tmp = line.strip().split(' ')
                partyTemplates.append(tmp)


def readMissionTemplates():
    with open(module_path + "mission_templates.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("mst_"):
                tmp = line.strip().split(' ')
                missionTemplates.append([tmp])
            elif lineCount > 2:
                missionTemplates[len(missionTemplates)-1].append(line.strip().split(' '))
            lineCount += 1


def readSkills():
    with open(module_path + "skills.txt") as f:
        for line in f:
            if line.startswith("skl_"):
                tmp = line.strip().split(' ')
                skills.append(tmp)


def readSounds():
    with open(module_path + "sounds.txt") as f:
        for line in f:
            if line.startswith("snd_"):
                tmp = line.strip().split(' ')
                sounds.append(tmp)


def readParticleSystems():
    with open(module_path + "particle_systems.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("psys_"):
                tmp = line.strip().split(' ')
                particleSystems.append([tmp])
            elif lineCount > 2:
                particleSystems[len(particleSystems)-1].append(line.strip().split(' '))
            lineCount += 1


def readMenus():
    with open(module_path + "menus.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("menu_"):
                tmp = line.strip().split(' ')
                menus.append([tmp])
            elif lineCount > 2:
                menus[len(menus)-1].append(line.strip().split(' '))
            lineCount += 1


def readQuests():
    with open(module_path + "quests.txt") as f:
        for line in f:
            if line.startswith("qst_"):
                tmp = line.strip().split(' ')
                quests.append(tmp)


def readTableaus():
    with open(module_path + "tableau_materials.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("tab_"):
                tmp = line.strip().split(' ')
                tableaus.append([tmp])
            elif lineCount > 2:
                tableaus[len(tableaus)-1].append(line.strip().split(' '))
            lineCount += 1


def readTracks():
    with open(module_path + "music.txt") as f:
        for line in f:
            if not is_int(line):
                tmp = line.strip().split(' ')
                tracks.append(tmp)


def readMapIcons():
    with open(module_path + "map_icons.txt") as f:
        lineCount = 0
        for line in f:
            tmp = line.strip().split(' ')
            if not is_int(tmp[0]) and len(line.strip()) > 0:
                icons.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                icons[len(icons)-1].append(tmp)
            lineCount += 1


def readAnimations():
    with open(module_path + "actions.txt") as f:
        lineCount = 0
        for line in f:
            if lineCount > 0:
                tmp = line.strip().split(' ')
                if not is_float(line):
                    animations.append([tmp])
                else:
                    animations[len(animations)-1].append(tmp)
            lineCount += 1


def readLocalVariableNames():
    with open("local_var_names.conf") as f:
        for line in f:
            lineS = line.split('#')[0]
            if " > " in lineS:
                tmp = lineS.split('>')
                tmp2 = tmp[1].strip().split(',')
                #varName = tmp2[0].strip()
                funcName = tmp[0].strip()
                localVarNames[funcName] = tmp2


def is_int(data):
    try:
        _ = int(data)
    except:
        return False
    return True


def is_float(data):
    try:
        _ = float(data)
    except:
        return False
    return True


def decompileScript(name : str, show : bool = False):
    data = []
    localVarDict.clear()
    with open(module_path + "scripts.txt") as f:
        found = False
        for line in f:
            if line.startswith(name):
                found = True
                print("# Converting:", line.strip().split(' ')[0])
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
                            if vv in operations:
                                newData = "this_or_next|" + operations[vv] + ","
                            else:
                                newData = "this_or_next|UNKNOWN_OP_" + vv + ","
                        elif (itmp & 0x80000000) == 0x80000000: # neg
                            vv = str(itmp & 0xFFFF)
                            if vv in operations:
                                newData = "neg|" + operations[vv] + ","
                            else:
                                newData = "neg|UNKNOWN_OP_" + vv + ","
                        elif tmp[i] in operations:
                            newData = operations[tmp[i]] + ","
                        else:
                            newData = "UNKNOWN_OP_" + tmp[i] + ","

                        activeCount = int(tmp[i+1]) + 1
                        lll = 0
                        stx = i + 2
                        enx = i + 1 + activeCount
                        for ix in range(stx, enx):
                            newData += lookupData(newData.split(',')[0], tmp[ix], tmp[ix+1:enx], data, lll) + ","
                            lll += 1
                        newData = newData.rstrip(',')
                        data.append(newData)
                    else:
                        activeCount -= 1
                break
    return data


def varI(v, isPos : bool = False):
    if is_int(v) and not isPos:
        v = "s" + v
    elif is_int(v):
        v = "pos" + v
    return v


def convertToPy(data : list):
    data = convertToPy1(data)
    data = convertToPy2(data)
    data, scriptParams = convertToPy3(data)
    return data, scriptParams


def findMyEndIndex(data : list, idx : int):
    x = -1
    try_open_count = 0
    for i in range(idx, len(data)):
        code = data[i]
        if code == "try_begin" or "try_for" in code:
            try_open_count += 1
        elif code == "try_end":
            try_open_count -= 1
        if try_open_count <= 0:
            x = i
            break
    return x


def searchLastTryHadCondition(data : list, idx : int):
    hasCondition = False
    for i in range(idx - 1, 0, -1):
        code = data[i]
        firstCode = code.split(',')[0]
        if code == "try_begin" or code == "else_try" or code == "try_end" or "try_for" in code:
            break
        elif firstCode in conditionals or "this_or_next|" in firstCode or "neg|" in firstCode:
            hasCondition = True
    return hasCondition


def convertMathOp(funcName : str, params : list):
    if funcName == "val_mod":
        if len(params) > 1:
            retx = params[0] + " %= " + params[1]
        else:
            retx = "val_mod(" + params[0] + ")"
    elif funcName == "val_sub":
        if len(params) > 1:
            retx = params[0] + " -= " + params[1]
        else:
            retx = "val_sub(" + params[0] + ")"
    elif funcName == "val_add":
        if len(params) > 1:
            retx = params[0] + " += " + params[1]
        else:
            retx = "val_add(" + params[0] + ")"
    elif funcName == "val_mul":
        if len(params) > 1:
            retx = params[0] + " *= " + params[1]
        else:
            retx = "val_mul(" + params[0] + ")"
    elif funcName == "val_div":
        if len(params) > 1:
            retx = params[0] + " /= " + params[1]
        else:
            retx = "val_div(" + params[0] + ")"
    elif funcName == "store_sub":
        if len(params) > 2:
            retx = params[0] + " = " + params[1] + " - " + params[2]
        else:
            retx = "store_sub(" + params[0] + ", " + params[1] + ")"
    elif funcName == "store_add":
        if len(params) > 2:
            retx = params[0] + " = " + params[1] + " + " + params[2]
        else:
            retx = "store_add(" + params[0] + ", " + params[1] + ")"
    elif funcName == "store_mul":
        if len(params) > 2:
            retx = params[0] + " = " + params[1] + " * " + params[2]
        else:
            retx = "store_mul(" + params[0] + ", " + params[1] + ")"
    elif funcName == "store_div":
        if len(params) > 2:
            retx = params[0] + " = " + params[1] + " / " + params[2]
        else:
            retx = "store_div(" + params[0] + ", " + params[1] + ")"
    else:
        retx = "ERROR_MATH_OP;" + funcName + ";" + ",".join(params)
        print("# " + retx)
    return retx


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
            lastWasCondit = True
            hasCond = searchLastTryHadCondition(data, i)
            curano = False
            if not hasCond and len(curLine.strip()) > 0:
                curano = True
            curLine = "if;" + code + ";"
            if not isInliner and not curano:
                insertEnds.append(len(formatex))
                isInliner = True
        elif "," in code:
            tmp = code.split(',')
            if "assign" == tmp[0]:
                if len(tmp) > 2:
                    xyz = varS(tmp[1]) + " = " + varS(tmp[2])
                else:
                    xyz = "assign(" + varS(tmp[1]) + ")"
            elif ("store" in tmp[0] or "get_" in tmp[0]) and not tmp[0] in math_ops:
                xyz = tmp[0] + "("
                for i in range(1, len(tmp)):
                    tmp[i] = varS(tmp[i])
                if len(tmp) > 2:
                    xyz += ",".join(tmp[2:])
                isPos = False
                if "position" in tmp[0] or "_pos_" in tmp[0]:
                    isPos = True
                xyz = varI(tmp[1], isPos) + " = " + xyz
                xyz += ")"
            elif "try_for_range" in tmp[0]:
                step = 1
                if "backwards" in tmp[0]:
                    step = -1
                xyz = "for;" + ";".join(tmp[1:]) + ";" + str(step)
            elif "try_for_parties" == tmp[0]:
                xyz = "for;" + tmp[1] + ";__all_parties__"
            elif "try_for_players" == tmp[0]:
                xyz = "for;" + tmp[1] + ";__all_players__"
            elif "try_for_prop_instances" == tmp[0]:
                xyz = "for;" + tmp[1] + ";__all_prop_instances__"
            elif "try_for_agents" == tmp[0]:
                xyz = "for;" + tmp[1] + ";__all_agents__"
            else:
                funcName = tmp[0]
                if funcName == "display_message":
                    funcName = "print"
                for i in range(1, len(tmp)):
                    tmp[i] = varS(tmp[i])
                if funcName in math_ops:
                    xyz = convertMathOp(funcName, tmp[1:])
                else:
                    xyz = funcName + "("
                    if len(tmp) > 1:
                        xyz += ",".join(tmp[1:])
                    xyz += ")"
            formatex.append(xyz)
            condit = False
        else:
            formatex.append(code)
            condit = False

        if not condit and (lastWasCondit or curLine == "elif;"):
            if curLine == "elif;":
                curLine = "else"
            formatex.insert(len(formatex) - 1, curLine)
            curLine = ""
            lastWasCondit = False
            isInliner = False

    insertEnds.reverse()
    for i in insertEnds:
        for ix in range(i, len(formatex)):
            if formatex[ix] == "#end": #and ix < 99:
                formatex.insert(ix, "#end")
                break

    return formatex


def varS(txt : str):
    if txt.startswith("\"") and txt.endswith("\"") and not "@" in txt:
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
        if len(tmp) > 2:
            xyz = varS(tmp[1]) + operator + varS(tmp[2])
        else:
            if negate:
                print("Warning: NEQ >", tmp)
                xyz = "neq(" + varS(tmp[1]) + ")"
            else:
                print("Warning: EQ >", tmp)
                xyz = "eq(" + varS(tmp[1]) + ")"
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
            elif xyz == "if ":
                xyz += "True"
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
            elif len(tmp) == 3:
                xyz += varS(tmp[2]) + ":"
            else:
                print("# ERROR: FOR >", tmp, xyz)
            datax.append(xyz)
        else:
            datax.append(c)
    return datax


extraLists = dict()
def convertToPy3(data : list):
    datax = []
    scriptParams = []
    for i in range(len(data)):
        code = data[i]
        if code.startswith("if") and " or " in code and not " and " in code:
            tmp = code[3:].rstrip(':').split(' or ')
            same = True
            lastC = tmp[0].split(' == ')[0]
            atmo = []
            for c in tmp:
                tmp2 = c.split(' == ')
                if tmp2[0] != lastC:
                    same = False
                elif len(tmp2) > 1:
                    atmo.append(tmp2[1])
            if same:
                lastC2 = lastC + "_list1"
                extraLists[lastC2] = atmo
                datax.insert(0, "]")
                for c in atmo:
                    datax.insert(0, c + ",")
                datax.insert(0, lastC2 + " = [")
                datax.append("if " + lastC + " in " + lastC2 + ":")
            else:
                datax.append(code)
        elif code.startswith("if") and "#end" in data[i+1]:
            # TODO: also add other cases here
            datax.append(code)
            datax.append("pass")
        elif code.startswith("elif") and " or " in code and not " and " in code:
            tmp = code[5:].rstrip(':').split(' or ')
            same = True
            lastC = tmp[0].split(' == ')[0]
            atmo = []
            for c in tmp:
                tmp2 = c.split(' == ')
                if tmp2[0] != lastC:
                    same = False
                elif len(tmp2) > 1:
                    atmo.append(tmp2[1])
            if same:
                lastC2 = lastC + "_list2"
                extraLists[lastC2] = atmo
                datax.insert(0, "]")
                for c in atmo:
                    datax.insert(0, c + ",")
                datax.insert(0, lastC2 + " = [")
                datax.append("elif " + lastC + " in " + lastC2 + ":")
            else:
                datax.append(code)
        elif "call_script" in code and "script." in code:
            tmp = code.replace("call_script(script.", "").replace(",","(",1)
            if not "(" in tmp:
                tmp = tmp.replace(")","()")
            datax.append(tmp)
        elif "store_script_param" in code:
            tmp = code.split('=')
            xname = tmp[0].strip()
            if "store_script_param_1" in code:
                if len(scriptParams) > 0:
                    scriptParams[0] = xname
                else:
                    scriptParams.append(xname)
            elif "store_script_param_2" in code:
                if len(scriptParams) > 1:
                    scriptParams[1] = xname
                else:
                    scriptParams.append(xname)
            else:
                parax = tmp[1].strip().split('(')[1].split(')')[0]
                if is_int(parax):
                    x = int(parax)
                    if x < len(scriptParams):
                        scriptParams[x] = xname
                    else:
                        scriptParams.append(xname)
                else:
                    print("# PARSING ERROR:", parax, "TO INT - SCRIPT_PARAM")
        else:
            datax.append(code)
    return datax, scriptParams


def formatGoodText(data : list, showIndex : bool = False, extraIndent : bool = False):
    sx = ""
    indentx = 0
    if extraIndent:
        indentx = 1
    for i, s in enumerate(data):
        st = s
        if indentx > 0 and (s.startswith("elif") or s == "else:" or s == "#end"):
            indentx -= 1
        st = "    " * indentx + st
        sx += st
        if s.startswith("if") or s.startswith("elif") or s == "else:" or s.startswith("for"):
            indentx += 1
        if showIndex:
            sx += " #" + str(i)
        sx += "\n"
    return sx



# main program
# read txt files
readGlobalVariables()
readOperationsFile()
readQuickStrings()
readSceneProps()
readScripts()
readTroops()
readGameStrings()
readFactions()
readScenes()
readItems()
readPresentations()
readParties()
readMeshes()
readPartyTemplates()
readMissionTemplates()
readSkills()
readSounds()
readParticleSystems()
readMenus()
readQuests()
readTableaus()
readTracks()
readMapIcons()
readAnimations()

# init local variables
readLocalVariableNames()


scriptName = ""
if len(sys.argv) > 1:
    scriptName = sys.argv[1]

if len(scriptName) == 0:
    for script in scripts:
        scriptName = script[0][0]
        datac = decompileScript(scriptName)
        datap, scriptParams = convertToPy(datac)
        txt = formatGoodText(datap, False, True)
        with open("test_scripts.py", "a") as f:
            f.write("def " + scriptName + "(" + ", ".join(scriptParams) + "):\n")
            if len(txt.strip()) > 0:
                f.write(txt)
            else:
                f.write("    pass\n")
            f.write("\n\n")
else:
    datac = decompileScript(scriptName)
    print(datac)
    datap, scriptParams = convertToPy(datac)
    txt = formatGoodText(datap, False, True)
    print("# " + scriptParams)
    print(txt)


