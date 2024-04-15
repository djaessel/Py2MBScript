#!/usr/bin/python3

import os
import sys
import time
import signal

sys.path.append('../modules/')

import items


process = None
tcpSender = None


def get_items_code():
    with open("../modules/items.py") as f:
        x = ""
        for line in f:
            if len(line.strip()) == 0:
                x += "<br>"
            else:
                x += "<p>" + line.rstrip('\n') + "</p>"
    return x


def get_window_id(name):
    import Xlib.display

    d = Xlib.display.Display()
    r = d.screen().root

    window_ids = r.get_full_property(
        d.intern_atom('_NET_CLIENT_LIST'), Xlib.X.AnyPropertyType
    ).value

    for window_id in window_ids:
        window = d.create_resource_object('window', window_id)
        if window.get_wm_name() == name:
            return window_id

def close_openbrf():
    print("Close openBrf")
    tcpSender.close()
    if process != None:
        process.send_signal(signal.SIGINT)
        process.wait()


def test_button():
    pass


def retrieveItems():
    itemsx = []
    for i in vars(items):
        if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
            attr = getattr(items,i)
            if not "<function" in str(attr) and not "<module" in str(attr) and not "ItemMesh" in str(attr) and not "SimpleTrigger" in str(attr):
                itemsx.append(attr)
    return itemsx


def dump(obj, objName="ITEM"):
    print(objName + " {")
    for attr in dir(obj):
        if not attr.startswith("__"):
            cc = getattr(obj, attr)
            a = str(cc)
            if not "<" in a and not ">" in a:
                print(" - %s = %r" % (attr, a))
            elif type(cc) == type([]):
                for c in cc:
                    dump(c, "CHILD")
    print("}")


def dumpDict(obj):
    dd = dict()
    for attr in dir(obj):
        if not attr.startswith("__"):
            cc = getattr(obj, attr)
            a = str(cc)
            if type(cc) == type([]):
                aa = []
                if "<" in a and ">" in a:
                    for c in cc:
                        aa.append(dumpDict(c))
                else:
                    for c in cc:
                        aa.append(c)
                dd[attr] = aa
            elif not "<" in a and not ">" in a:
                dd[attr] = a
    return dd


def run_app(window_id):
    from PySide6.QtCore import Qt, QUrl, Slot, QObject
    from PySide6.QtQml import QmlElement, qmlRegisterType
    from PySide6.QtGui import QWindow, QColor, QSurfaceFormat
    from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QApplication, QPushButton, QGridLayout
    from PySide6.QtQuickWidgets import QQuickWidget
    from tcp_connector import TCPSender
    from text_handler import TextHandler

    app = QApplication([])
    main_widget = QWidget()
    main_widget.setGeometry(0, 0, 1000, 800)
    main_widget.setStyleSheet("background-color: 'darkgrey'")
    layout = QVBoxLayout()
    layout2 = QVBoxLayout()
    layout3 = QGridLayout(main_widget)

    window = QWindow.fromWinId(window_id)
    window.setFlag(Qt.FramelessWindowHint, True)
    widget = QWidget.createWindowContainer(window)
    widget.setWindowFlags(Qt.FramelessWindowHint)
    layout.addWidget(widget)

    formatx = QSurfaceFormat()
    formatx.setAlphaBufferSize(8)
    qmlWindow = QQuickWidget()
    qmlWindow.setFormat(formatx)
    qmlWindow.setWindowFlags(Qt.FramelessWindowHint)
    qmlWindow.setAttribute(Qt.WA_AlwaysStackOnTop);
    qmlWindow.setAttribute(Qt.WA_TranslucentBackground)
    qmlWindow.setClearColor(QColor(Qt.transparent))
    qmlWindow.setResizeMode(QQuickWidget.SizeRootObjectToView)

    xitems = []
    for x in retrieveItems():
        #xitems.append({'id': x.id, 'mesh1': x.meshes[0].id})
        #print(x.id, "|", x.__dict__)
        d = dumpDict(x)
        xitems.append(d)
    qmlWindow.engine().rootContext().setContextProperty('xitems', xitems)

    global tcpSender
    tcpSender = TCPSender()
    qmlWindow.engine().rootContext().setContextProperty('tcpSender', tcpSender)

    textHandler = TextHandler()
    textHandler.setText(get_items_code())
    qmlWindow.engine().rootContext().setContextProperty('textHandler', textHandler)
    #qmlWindow.engine().rootContext().setContextProperty('itemsCode', get_items_code())
    
    qmlWindow.setSource(QUrl.fromLocalFile("main.qml"))


    button2 = QPushButton('Close')
    button2.clicked.connect(close_openbrf)
    button2.clicked.connect(main_widget.close)
    layout2.addWidget(button2)

    #buttonTest = QPushButton('Test')
    #buttonTest.clicked.connect(test_button)
    #layout2.addWidget(buttonTest)

    layout2.addWidget(qmlWindow)

    layout3.addLayout(layout,0,0)
    layout3.addLayout(layout2,0,1)
    layout3.setColumnStretch(0, 1)
    layout3.setColumnStretch(1, 2)

    main_widget.show()

    # glitch fix
    time.sleep(1)
    screen_rect = app.primaryScreen().availableGeometry()
    width, height = screen_rect.width(), screen_rect.height()
    main_widget.setGeometry(0, 0, width, height)

    app.exec()


from subprocess import Popen, PIPE, STDOUT
from openbrf import OpenBrf

if __name__ == '__main__':
    process = Popen(['python3', '-B', 'runner.py'], stdout=PIPE, stderr=STDOUT)

    window_id = None
    #for line in iter(process.stdout.readline, b''):
    #    print(">>>", line.rstrip())
    #    try:
    #        window_id = int(line.rstrip())
    #        break
    #    except:
    #        pass

    while not os.access("piper.txt", os.R_OK):
        time.sleep(1)
    
    try:
        with open("piper.txt") as f:
            window_id = int(f.read())
    except:
        window_id = None

    if window_id:
        os.remove("piper.txt")
        run_app(window_id)
    else:
        print("Error: WINDOW_ID NOT SET!")
