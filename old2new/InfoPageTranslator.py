# This Python file uses the following encoding: utf-8


module_path = "/home/djaessel/warband/Modules/Native/"


def readInfoPages():
    infoPages = []
    with open(module_path + "info_pages.txt") as f:
        for line in f:
            if line.startswith("ip_"):
                tmp = line.strip().split(' ')
                infoPages.append(tmp)
    return infoPages


def writeInfoPage(f, infoPage : list):
    idx = infoPage[0][3:]
    name = infoPage[1].replace("_"," ")
    text = infoPage[2].replace("_"," ")

    f.write(idx + " = InfoPage(\"" + idx + "\", \"" + name + "\")\n")
    f.write(idx + ".set_text(\"" + text + "\")\n")

    f.write("\n\n")


if __name__ == "__main__":
    infoPages = readInfoPages()
    with open("test_info_pages.py", "w") as f:
        for ip in infoPages:
            writeInfoPage(f, ip)

