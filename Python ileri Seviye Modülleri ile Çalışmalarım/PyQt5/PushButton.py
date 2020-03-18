import sys
from PyQt5.QtWidgets import QApplication ,QWidget ,QMainWindow,QPushButton
from PyQt5 import QtGui
from PyQt5 import QtCore

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.Window_Properties()
        self.Window_Properties_Apply()
        self.Interface()
        self.show()
    def Window_Properties(self):

        self.title = "PyQt5 Push button"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 200
        self.iconName = "icon.png"

    def Window_Properties_Apply(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top ,self.left ,self.width ,self.height)
        self.setWindowIcon(QtGui.QIcon(self.iconName))

    def Interface(self):
        PushButton = QPushButton("Click Me" ,self)
        #PushButton.move(50,100)
        PushButton.setGeometry(QtCore.QRect(150 ,100 ,100 ,50))
        PushButton.setIcon(QtGui.QIcon("icon.png"))#Button Coordinator
        PushButton.setIconSize(QtCore.QSize(40 ,40))#image size
        PushButton.setToolTip("<h2>This is Click Me Button<h2>")#
        PushButton.clicked.connect(self.Button_Clicked)

    def Button_Clicked(self):
        print("Hello Word")
        sys.exit()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec_())