import os
import sys


class Translator():
    def __init__(self, language : str, filename : str, id_prefix : str):
        self.language = language
        self.filename = filename
        self.id_prefix = id_prefix
        self.folderPath = "./build_system/languages/" + self.language
        self.filePath = self.folderPath + "/" + self.filename + ".csv"
        self.translations = {}
        self.initHeaderLine()


    def initHeaderLine(self):
        with open(self.filePath) as f:
            self.headerLine = f.readline()


    def translate(self, id : str, text : str):
        self.translations[id] = text


    def save(self):
        if not os.path.exists(self.folderPath):
            os.mkdir(self.folderPath)
        with open(self.filePath, "w") as f:
            if "lockitver" in self.headerLine or len(self.headerLine.strip()) == 0:
                f.write(self.headerLine)
            for tKey in self.translations:
                f.write(self.id_prefix + "_" + tKey + "|" + self.translations[tKey] + "\n")


