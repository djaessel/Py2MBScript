from MBPlayer import MBPlayer

def script1(waterLevel, fishCount):
    versionx = get_operation_set_version()
    if versionx > 0 and versionx <= 1101:
        banner_id = profile_get_banner_id()
        if banner_id > 20 or banner_id == 0 or banner_id == 10:
            print(versionx)

    if fishCount == 1 and is_edit_mode_enabled():
        print("Test1")
    elif is_edit_mode_enabled() or versionx > 1011:
        print("Test4")

    if waterLevel == 2 or fishCount == 1:
        print("TEST2")
    else:
        print("TEST3")

    print("Hello World!")



def helloWorld():
    ai_strength = options_get_campaign_ai()
    print("Hello World!")
    print(ai_strength)



def whoIsMyPlayerTeam(playerId):
    playerx = MBPlayer(playerId)
    team_no = playerx.get_team_no()
    reg0 = team_no
    print(reg0)


def itemx(playerId, item):
    playerx = MBPlayer(playerId)
    playerx.add_spawn_item(0, item)
    teamNo = playerx.get_team_no()
    entry_point = multiplayer_find_spawn_point(teamNo, 1, 0)
    print("Spawn point")
    print(entry_point)


def setNewTeam(playerId, teamNo):
    playerx = MBPlayer(playerId)
    playerx.set_team_no(teamNo)
    reg0 = playerId
    reg1 = teamNo
    print("{reg0} has team {reg1}")

