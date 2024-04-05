# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "com.djaessel.io"
QML_IMPORT_MAJOR_VERSION = 1

from PySide6.QtQml import QmlElement
from PySide6.QtCore import QObject, Slot


@QmlElement
class TextHandler(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.textX = ""

    @Slot(str)
    def setText(self, s):
        self.textX = s
        with open("../modules/items.py", "w") as f:
            f.write(s.replace("<p>","").replace("</p>","\n").replace("<br>", "\n"))

    @Slot(result=str)
    def getText(self):
        return self.textX

