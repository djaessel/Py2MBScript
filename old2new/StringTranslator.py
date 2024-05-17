# This Python file uses the following encoding: utf-8


module_path = "/home/djaessel/warband/Modules/Native/"


def readGameStrings():
    gameStrings = []
    with open(module_path + "strings.txt", encoding="latin1") as f:
        for line in f:
            if line.startswith("str_"):
                tmp = line.strip().split(' ')
                gameStrings.append((tmp[0], tmp[1].replace("_", " ")))
    return gameStrings


def writeString(f, stringx : list):
    idx = stringx[0]
    f.write(idx + " = MBString(\"" + idx + "\", \"" + stringx[1] + "\")\n\n")


if __name__ == "__main__":
    gameStrings = readGameStrings()
    with open("test_strings.py", "w") as f:
        for gstr in gameStrings:
            writeString(f, gstr)





