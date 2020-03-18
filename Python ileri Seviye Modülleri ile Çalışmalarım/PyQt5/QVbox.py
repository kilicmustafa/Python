
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 100
        self.right = 500
        self.bottom = 500
        self.formIcon = "icon.png"

        self.init_window()

    def init_window(self):
        self.setWindowTitle("Yeni Pencere Oluşturma")
        self.setWindowIcon(QtGui.QIcon(self.formIcon))  # form için ikon oluşturma
        self.setGeometry(self.top, self.left, self.right, self.bottom)
        self.setUI()
        self.show()

    def setUI(self):
        button = QPushButton("Tıkla ", self)
        button.setGeometry(100, 100, 150, 50)  # (x,y,width,height)
        button.setIcon(QtGui.QIcon(self.formIcon))
        button.setIconSize(QtCore.QSize(30, 30))
        button.setToolTip("Butona Tıklayabilirsiniz")


if __name__ == '__main__':  # Programın başlayacağı main metodu

    app = QApplication(sys.argv)
    window = Window()
    app.exit(app.exec())