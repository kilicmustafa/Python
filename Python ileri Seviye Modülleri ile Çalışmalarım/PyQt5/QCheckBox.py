import sys
from PyQt5.QtWidgets import QApplication ,QCheckBox ,QDialog ,QGroupBox,QVBoxLayout ,QHBoxLayout ,QLabel ,QRadioButton
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

        check_fourth = QCheckBox("Python")
        check_fourth.setIcon(QtGui.QIcon("icon.png"))
        check_fourth.setIconSize(QtCore.QSize(30,30))
        check_fourth.setFont(QtGui.QFont("Marimba" ,28))
        check_fourth.setStyleSheet("Color : gray")

        check_fifth = QCheckBox("Kotlin")
        check_fifth.setIcon(QtGui.QIcon("icon.png"))
        check_fifth.setIconSize(QtCore.QSize(20 ,20))
        check_fifth.setFont(QtGui.QFont("Arial" ,25))
        check_fifth.setStyleSheet("Color : Pink")

        check_sixth = QCheckBox("JavaScript")
        check_sixth.setIcon(QtGui.QIcon("icon.png"))
        check_sixth.setIconSize(QtCore.QSize(25 ,30))
        check_sixth.setFont(QtGui.QFont("sanserif" , 20))
        check_sixth.setStyleSheet("Color : Green")

        h_box = QHBoxLayout()
        h_box.addWidget(check_fourth)
        h_box.addWidget(check_fifth)
        h_box.addWidget(check_sixth)

        self.answer = QLabel(self)

        groupBox = QGroupBox("Select Check Box")
        groupBox.setLayout(h_box)

        v_box = QVBoxLayout()
        v_box.addWidget(groupBox)
        v_box.addWidget(self.answer)



        check_fourth.toggled.connect(self.OnCheckBox)
        check_fifth.toggled.connect(self.OnCheckBox)
        check_sixth.toggled.connect(self.OnCheckBox)

        self.setLayout(v_box)


    def OnCheckBox(self):
        sender = self.sender()

        if sender.isChecked():
            self.answer.setText(sender.text())



        """
        if self.check_fourth.isCLicked() :
            self.answer.setText(self.check_fourth.text()
        
        
        
        """




if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(App.exec_())


