# This Python file uses the following encoding: utf-8


class Quest:
    def __init__(self, id : str, name : str, description : str = "", is_random : bool = True, show_progress : bool = False):
        self.id = id
        self.name = name
        self.description = description
        self.is_random = is_random
        self.show_progress = show_progress


    def set_description(self, description):
        self.description = description


    def set_is_random(self, is_random : bool):
        self.is_random = is_random


    def set_show_progress(self, show_progress : bool):
        self.show_progress = show_progress

