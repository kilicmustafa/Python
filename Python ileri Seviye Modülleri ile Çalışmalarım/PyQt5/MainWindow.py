import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Window_Properties()
        self.Window_Properties_Apply()
        self.show()

    def Window_Properties(self):
        self.title = "MainWindow"
        self.top = 570
        self.left =350
        self.wight = 300
        self.height = 100
        self.iconName = "icon.png"

    def Window_Properties_Apply(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top ,self.left ,self.wight ,self.height)
        self.setWindowIcon(QIcon(self.iconName))



app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())





