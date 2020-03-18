import sys
from PyQt5.QtWidgets import QApplication ,QDialog ,QGridLayout ,QGroupBox ,QVBoxLayout ,QHBoxLayout ,QPushButton
from PyQt5 import QtGui
from PyQt5 import QtCore


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.Window_Properties()
        self.Window_Properties_Apply()
        self.Interface()



    def Window_Properties(self):
        self.title = "PyQt5 Grid Layout"
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
        Button_first = QPushButton("Football", self)
        Button_first.setIcon(QtGui.QIcon("icon.png"))
        Button_first.setIconSize(QtCore.QSize(40, 50))
        Button_first.setToolTip("<h3>Hello Football><h3>")
        Button_first.setMinimumHeight(40)

        Button_second = QPushButton("Basketball", self)
        Button_second.setIcon(QtGui.QIcon("icon.png"))
        Button_second.setIconSize(QtCore.QSize(35, 50))
        Button_second.setToolTip("<h3>Hello Basketball<h3>")
        Button_second.setMinimumHeight(40)

        Button_third = QPushButton("Tennis", self)
        Button_third.setIcon(QtGui.QIcon("icon.png"))
        Button_third.setIconSize(QtCore.QSize(30, 50))
        Button_third.setToolTip("<h3>Hello Tennis<h3>")
        Button_third.setMinimumHeight(40)

        GridLayout = QGridLayout()
        GridLayout.addWidget(Button_first ,0 ,0)
        GridLayout.addWidget(Button_second ,0 ,1)
        GridLayout.addWidget(Button_third ,1 ,0)

        GroupBox = QGroupBox("CLicked Push Button")
        GroupBox.setLayout(GridLayout)

        v_box = QVBoxLayout()
        v_box.addWidget(GroupBox)

        self.setLayout(v_box)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(App.exec_())

