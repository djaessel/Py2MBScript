# This Python file uses the following encoding: utf-8


class MenuOption:
    def __init__(self, id, text):
        self.id = id
        self.text = text

    def conditionBlock(self):
        pass

    def consequenceBlock(self):
        pass


class GameMenu:
    def __init__(self, id, flags, text, meshName="none"):
        self.id = id
        self.flags = flags
        self.text = text
        self.meshName = meshName
        self.menuOptions = []

    def conditionBlock(self):
        pass

