import sys
from PyQt5.QtWidgets import QApplication ,QAction ,qApp ,QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        mennubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")

        file_open = QAction("File Open",self)
        file_open.setShortcut("Ctrl+O")

        file_save = QAction("File Save",self)
        file_save.setShortcut("Ctrl+S")

        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")

        file.addAction(file_open)
        file.addAction(file_save)
        file.addAction(exit)

        find_and_changing = edit.addMenu("Find and Changing")

        find = QAction("Find" ,self)
        find.setShortcut("Ctrl+F")

        changing = Qaction("Changing" ,self)
        changing = QAction("Ctrl+R")

        clear = QAction("Clear",self)
        clear.setShortcut("Ctrl+K")

        find_and_changing.addAction(find)
        find_and_changing.addAction(changing)

        edit.addAction(clear)


        exit.trigger(self.Exit_Program)



    def Exit_Program