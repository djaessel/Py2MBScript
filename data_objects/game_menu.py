# This Python file uses the following encoding: utf-8


class MenuOption:
    id = "NO_ID_SET"
    text = ""

    def __init__(self, id, text):
        self.id = id
        self.text = text

    def conditionBlock(self):
        pass

    def consequenceBlock(self):
        pass


class GameMenu:
    id = "NO_ID_SET"
    flags = 0
    text = ""
    meshName = ""
    menuOptions = []

    def __init__(self, id, flags, text, meshName="none"):
        self.id = id
        self.flags = flags
        self.text = text
        self.meshName = meshName

    def conditionBlock(self):
        pass

