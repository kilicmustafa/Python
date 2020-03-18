import sys
from PyQt5.QtWidgets import QApplication ,QPushButton ,QCheckBox ,QDialog ,QGroupBox,QVBoxLayout ,QHBoxLayout ,QLabel ,QRadioButton
from PyQt5 import QtGui
from PyQt5 import QtCore


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.Window_Properties()
        self.Window_Properties_Apply()
        self.Interface()



    def Window_Properties(self):
        self.title = "PyQt5 QLabel"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 100
        self.iconName = "icon.png"

    def Window_Properties_Apply(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("icon.png"))

    def Interface(self):


        labal_seventh  = QLabel("Focus and Press Shift + F1")
        button  = QPushButton("Click Me")
        button.setWhatsThis("Click Me :D")
        button.setToolTip("Bane tıkla :)")

        h_box = QHBoxLayout()
        h_box.addWidget(labal_seventh)
        h_box.addWidget(button)

        self.setLayout(h_box)





if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(App.exec_())
