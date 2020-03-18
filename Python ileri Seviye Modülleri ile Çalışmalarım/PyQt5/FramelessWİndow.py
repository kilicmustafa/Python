import sys
from PyQt5.QtWidgets import QWidget , QVBoxLayout, QSizeGrip ,QLabel ,QApplication ,QHBoxLayout ,QPushButton ,QButtonGroup
from PyQt5 import QtCore
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
        self.setGeometry(self.top , self.left ,self.width ,self.height)



    def Interface(self):

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        sizegrip = QSizeGrip(self)

        v_box = QVBoxLayout()
        v_box.addWidget(sizegrip)

        self.setLayout(v_box)





if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWidow()
    window.show()
    sys.exit(App.exec_())

