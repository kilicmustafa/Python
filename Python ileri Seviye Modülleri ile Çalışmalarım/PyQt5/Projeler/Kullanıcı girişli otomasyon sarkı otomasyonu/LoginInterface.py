from SongOtomation import *
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication  ,QWidget ,QHBoxLayout ,QVBoxLayout,QLabel ,QLineEdit , QPushButton ,QDialog ,QMessageBox
from PyQt5.QtGui import QIcon ,QPixmap ,QColor
from PyQt5.QtCore import QSize



class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.WindowProperties()
        self.WindowPropertiesApply()
        self.Interface()

    def WindowProperties(self):
        self.title = "Login"
        self.top = 400
        self.left = 770
        self.width = 400
        self.height = 250
        self.iconName ="login.png"

    def WindowPropertiesApply(self):

        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("login.png"))
        self.setGeometry(self.left ,self.top ,self.width ,self.height)



    def Interface(self):
        self.icon  = QLabel(self)
        pixmap = QPixmap("login_screen_3.png")
        self.icon.setPixmap(pixmap)

        name = QLabel("User Name :")
        self.nameText = QLineEdit()

        password = QLabel("Password :")
        self.paswordText = QLineEdit()
        self.paswordText.setEchoMode(QLineEdit.Password)

        self.button = QPushButton("Login")
        self.button.setShortcut("Ctrl+r")


        v_box_first = QVBoxLayout()
        v_box_first.addStretch()
        v_box_first.addWidget(self.icon)

        h_box_first = QHBoxLayout()
        h_box_first.addStretch()
        h_box_first.addLayout(v_box_first)
        h_box_first.addStretch()



        v_box_second = QVBoxLayout()
        v_box_second.addStretch()
        v_box_second.addLayout(h_box_first)

        v_box_second.addWidget(name)
        v_box_second.addWidget(self.nameText)
        v_box_second.addWidget(password)
        v_box_second.addWidget(self.paswordText)
        v_box_second.addStretch()
        v_box_second.addWidget(self.button)
        v_box_second.addStretch()

        h_box_main = QHBoxLayout()
        h_box_main.addStretch()
        h_box_main.addLayout(v_box_second)
        h_box_main.addStretch()

        self.button.clicked.connect(self.userControl)
        self.setLayout(h_box_main)


    def userControl(self):
        name = self.nameText.text()
        password = self.paswordText.text()
        instant_feedback = Db_Operation().db_userControl(name ,password)

        if instant_feedback == True :
            QMessageBox.about(self ,"User found" ,"Login successful")
            self.accept()





        else:

            QMessageBox.about(self ,"User not found" ,"Check your information")








class Db_Operation():
    def __init__(self):

        self.db_connect()
        """self.db_userAdd()"""





    def db_connect(self):
        query = """CREATE TABLE IF NOT EXISTS 
            USER(NAME TEXT,
            PASSWORD TEXT)"""
        self.connect = sqlite3.connect("users.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute(query)
        self.connect.commit()





    def db_close(self):
        self.connect.close()


    def db_userControl(self ,name ,password):
        query = """SELECT * FROM USER
        WHERE NAME = ? AND PASSWORD = ?"""

        self.cursor.execute(query ,(name ,password))
        user_information = self.cursor.fetchall()

        size = len(user_information)

        if  (size == 0) :
            return False
        else:
            return True

    """def db_userAdd(self):
        name = input("Name :")
        password = input("pass :")
        print(type(password))
        query = "INSERT INTO USER VALUES(? ,?)"
        self.connect.execute(query,(name ,password))
        self.connect.commit()"""




if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    if Window.exec_() == QDialog.Accepted:

        run.show()

        sys.exit(App.exec_())





