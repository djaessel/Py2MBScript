# This Python file uses the following encoding: utf-8


module_path = "/home/djaessel/warband/Modules/Native/"


def readQuests():
    quests = []
    with open(module_path + "quests.txt") as f:
        for line in f:
            if line.startswith("qst_"):
                tmp = line.strip().split(' ')
                quests.append(tmp)
    return quests


def writeQuest(f, quest : list):
    idx = quest[0][4:]
    name = quest[1].replace("_"," ")
    text = quest[3].replace("_"," ")

    f.write(idx + " = Quest(\"" + idx + "\", name=\"" + name + "\", description=\"" + text + "\"")

    flagsx = int(quest[2])
    if (flagsx & 0x2) == 0:
        f.write(", is_random=False")
    if (flagsx & 0x1) == 0x1:
        f.write(", show_progress=True")
    f.write(")\n")

    f.write("\n\n")



if __name__ == "__main__":
    quests = readQuests()
    with open("test_quests.py", "w") as f:
        for qst in quests:
            writeQuest(f, qst)


