import sys
import os
from PyQt5.QtWidgets import QAction ,QFileDialog ,QVBoxLayout ,QHBoxLayout ,QPushButton ,QTextEdit ,QMenuBar ,QApplication ,QLabel ,QMainWindow


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

    def Menus(self):

        menubar = self.menuBar()

        file = menubar.addMenu
