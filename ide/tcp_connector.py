# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "com.djaessel.io"
QML_IMPORT_MAJOR_VERSION = 1

from PySide6.QtQml import QmlElement
from PySide6.QtCore import QObject, Slot

from multiprocessing.connection import Client


@QmlElement
class TCPSender(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.connected = True
        self.address = ('localhost', 16987)
        self.conn = Client(self.address, authkey=b'secret password')

    @Slot(str, result=bool)
    def send(self, s):
        if self.connected and len(s.strip()) > 0:
            self.conn.send(s)
            return True
        return False

    @Slot(result=bool)
    def close(self):
        try:
            self.send("close")
            self.conn.close()
            self.connected = False
        except:
            self.connected = False
            return False
        return True

