# This Python file uses the following encoding: utf-8


class InfoPage:
    def __init__(self, id, name, text=""):
        self.id = id
        self.name = name
        self.text = text


    def set_text(self, text):
        self.text = text

