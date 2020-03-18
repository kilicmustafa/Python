import sys
import os
from PyQt5.QtWidgets import QFileDialog ,QWidget ,QAction ,QApplication ,qApp ,QMainWindow ,QTextEdit ,QLabel ,QHBoxLayout ,QVBoxLayout ,QPushButton
from PyQt5 import QtCore
from PyQt5 import QtGui

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.content_head = QLabel("Content")
        self.content = QTextEdit()
        self.answer = QLabel("")

        self.clear_but = QPushButton("Clear",self)
        self.clear_but.setToolTip("Temizle")
        self.clear_but.setIcon(QtGui.QIcon("clear.png"))
        self.clear_but.setIconSize(QtCore.QSize(20,20))

        self.open_but = QPushButton("Open",self)
        self.open_but.setToolTip("Aç")
        self.open_but.setIcon(QtGui.QIcon("open.jpg"))
        self.open_but.setIconSize(QtCore.QSize(20,20))


        self.save_but = QPushButton("Save",self)
        self.save_but.setToolTip("Kapat")
        self.save_but.setIcon(QtGui.QIcon("save.png"))
        self.save_but.setIconSize(QtCore.QSize(20,20))

        h_box = QHBoxLayout()

        h_box.addWidget(self.clear_but)
        h_box.addWidget(self.open_but)
        h_box.addWidget(self.save_but)

        v_box = QVBoxLayout()

        v_box.addWidget(self.content_head)
        v_box.addWidget(self.content)
        v_box.addWidget(self.answer)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.clear_but.clicked.connect(self.Clear)
        self.save_but.clicked.connect(self.Save)
        self.open_but.clicked.connect(self.Open)

    def Clear(self):
        self.content.clear()

    def Save(self):
        file_name = QFileDialog.getSaveFileName(self ,"Save File"  ,os.getenv("HOME"))
        with open(file_name[0] , "w") as file:
            file.write(self.content.toPlainText())


    def Open(self):
        file_name = QFileDialog.getOpenFileName(self ,"Open File" ,os.getenv("Home"))
        with open(file_name[0] , "r") as file:
            self.content.setText(file.read())


class Menu(QMainWindow):

    def __init__(self):

        super().__init__()
        self.window = Window()
        self.setCentralWidget(self.window)
        self.Menus()
        self.show()

    def Menus(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")

        file_open = QAction("File Open",self)
        file_open.setShortcut("Ctrl+O")

        file_save = QAction("File Save",self)
        file_save.setShortcut("Ctrl+S")

        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+W")

        file.addAction(file_open)
        file.addAction(file_save)
        file.addAction(exit)

        find_and_changing  = edit.addMenu("Find and Changing")

        find = QAction("Find",self)
        find.setShortcut("Ctrl+F")

        changing = QAction("Changing",self)
        changing.setShortcut("Ctrl+R")

        find_and_changing.addAction(find)
        find_and_changing.addAction(changing)

        clear = QAction("Clear",self)
        clear.setShortcut("Ctrl+K")
        edit.addAction(clear)


        exit.triggered.connect(self.Exit_Program)
        file.triggered.connect(self.Response)
        edit.triggered.connect(self.Response)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle("Text Editor")
        self.show()

    def Exit_Program(self):
        qApp.quit()

    def Response(self,action):

        if (action.text() == "File Save" ):
            self.window.Save()
        elif (action.text() == "File Open"):
            self.window.Open()
        elif (action.text() == "Exit"):
            self.window.Exit()
        elif (action.text() == "Clear"):
            self.window.Clear()


app = QApplication(sys.argv)
menu = Menu()

sys.exit(app.exec_())


