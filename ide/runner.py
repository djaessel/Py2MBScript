import os
import sys
import time
import threading
from openbrf import OpenBrf
from signal import signal, SIGINT, SIGTERM
from multiprocessing.connection import Listener


openbrf = None
x = None

def handlerContrlC(signal_received, frame):
    if openbrf != None:
        openbrf.closeApp()

    if x != None:
        x.join()

    print('SIGINT or CTRL-C detected. Exiting gracefully')
    #time.sleep(5)
    #sys.exit(0)


def handlerTerminate(signal_received, frame):
    if openbrf != None:
        openbrf.closeApp()

    print('SIGTERM Exiting gracefully')
    #time.sleep(5)
    #sys.exit(0)


def check_commands(openBrf):
    running = True
    file = "piper.txt"
    while running:
        time.sleep(5)
        changed = False
       
        if os.access(file, os.R_OK):
            with open(file) as f:
                txt = f.read()
        
            if txt.startswith("select:mesh:"):
                openbrf.selectItemMesh(txt.split(':')[2].encode('ascii'))
                changed = True
            elif txt == "exit":
                openBrf.closeApp()
                running = False

            if changed:
                time.sleep(1)
                with open(file, "w") as f:
                    f.write("")

    os.remove(file)


def listenAndCommands(openBrf):
    address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
    listener = Listener(address, authkey=b'secret password')
    conn = listener.accept()
    print('connection accepted from', listener.last_accepted)
    
    msg = "ERROR"
    while True:
        msg = conn.recv()
        # do something with msg
        if msg == 'close' or msg == 'exit':
            with open("test2.txt", "w") as f:
                f.write("CHOLERA:" + msg)
            openBrf.closeApp()
            conn.close()
            break
        elif msg.startswith("select:mesh:"):
            openBrf.selectItemMesh(msg.split(':')[2].encode('ascii'))
            with open("test.txt", "w") as f:
                f.write(msg.split(':')[2])

    listener.close()
    with open("test3.txt", "w") as f:
        f.write(msg)


if __name__ == '__main__':
    signal(SIGINT, handlerContrlC)
    signal(SIGTERM, handlerTerminate)

    openbrf = OpenBrf()
    openbrf.setModPath(b"/home/djaessel/.steam/debian-installation/steamapps/common/MountBlade Warband/Modules/Native/")
    
    wid = openbrf.getCurWindowPtr()
    print(wid)
    with open("piper.txt", "w") as f:
        f.write(str(wid))

    #x = threading.Thread(target=check_commands, args=(openbrf,))
    #x.start()
    #x.join()
    
    listenAndCommands(openbrf)


