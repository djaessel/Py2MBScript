from MBPlayer import MBPlayer
from MBOptions import MBOptions
from MBParty import MBParty


def script1(waterLevel, fishCount):
    versionx = get_operation_set_version()
    if versionx > 0 and versionx <= 1101:
        banner_id = profile_get_banner_id()
        if banner_id > 20 or banner_id == 0 or banner_id == 10:
            print(versionx)
            if versionx == 1011:
                print("YES!")
            else:
                print("Nope")

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
    optionx = MBOptions()
    ai_strength = optionx.get_campaign_ai()
    print("Hello World!")
    optionx.set_damage_to_friends(ai_strength)
    print(ai_strength)



def loopy():
    for i in range(2, 10):
        print(i)

    for i in range(5):
        optionx = MBOptions()
        ai_strength = optionx.get_campaign_ai()
        if ai_strength == 1: # test 1
            print("YES!")

    for x in range(200, 0, -1): # test 2
        reg0 = x
        print("Backwards: {reg0}")


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


def changeFactionIfActive(partyId, newFactionNo):
    partaaay = MBParty(partyId)
    if partaaay.is_active():
        partaaay.set_faction(newFactionNo)
        partaaay.add_template("pt_sea_raiders")
    else:
        reg0 = partaaay
        print("Party {reg0} is inactive")


def tryAgain(randomVal):
    try:
        is_edit_mode_enabled()

        # has problems
        waterLevel = 5
        if randomVal == 3:
            waterLevel-=2
        else:
            waterLevel += 1
        print(waterLevel)
    except:
        print("There was an error!")



