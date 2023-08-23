# TEST SCRIPT
def script1(waterLevel, fishCount):
    versionx = get_operation_set_version()
    if versionx > 0 and versionx <= 1101:
        banner_id = profile_get_banner_id()
        if banner_id > 20 or banner_id == 0 or banner_id == 10:
            print(versionx)

    if fishCount == 1 and is_edit_mode_enabled():
        print("Test1")

    if waterLevel == 2 or fishCount == 1:
        print("TEST2")

    print("Hello World!")
