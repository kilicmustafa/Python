from PyQt5.QtWidgets import QApplication ,QWidget ,QFrame ,QPushButton ,QHBoxLayout
import sys
from PyQt5 import QtGui

class MainWidow(QWidget):
    def __init__(self):
        super().__init__()

        self.Window_Properties()
        self.Window_Properties_Apply()
        self.Interface()

    def Window_Properties(self):
        self.title = "PyQt5 Button Group"
        self.top = 200
        self.left = 500
        self.width = 500
        self.height = 500
        self.iconName = "icon.png"

    def Window_Properties_Apply(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.top, self.left, self.width, self.height)

    def Interface(self):