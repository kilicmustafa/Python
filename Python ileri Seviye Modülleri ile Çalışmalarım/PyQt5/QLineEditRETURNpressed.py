import sys
from PyQt5.QtWidgets import QApplication ,QWidget ,QLineEdit ,QPushButton ,QCheckBox ,QDialog ,QGroupBox,QVBoxLayout ,QHBoxLayout ,QLabel ,QRadioButton
from PyQt5 import QtGui
from PyQt5 import QtCore

class MainWindow(QWidget):
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


        self.lineEdit = QLineEdit()
        self.lineEdit.setFont(QtGui.QFont("Sanserif" ,15))
        self.lineEdit.returnPressed.connect(self.OnPressed)
        self.lineEdit.setMinimumSize(600,50)
        self.label =QLabel("")
        h_box = QHBoxLayout()
        h_box.addWidget(self.lineEdit)
        h_box.addWidget(self.label)

        self.setLayout(h_box)


    def OnPressed(self):
        self.label.setText(self.lineEdit.text())




if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(App.exec_())
