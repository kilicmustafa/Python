import sys
from PyQt5.QtWidgets import QTabWidget,QDialog ,qApp ,QApplication ,QMainWindow ,QAction,QPushButton ,QLabel ,QHBoxLayout ,QVBoxLayout ,QLineEdit ,QWidget
from PyQt5.QtGui import QIcon

import sqlite3
import time

class JuctionCenter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.Interface_Main()

        self.MenuBar()
        self.ImportUserControl = User_Control()
        self.setCentralWidget(self.ImportUserControl)



    def Interface_Main(self):
        self.title = "Market Otomation"
        self.top = 50
        self.left = 50
        self.width = 250
        self.height = 150
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("Market_icon.png"))
        self.setGeometry(self.top ,self.left ,self.width ,self.height)


    def MenuBar(self):
        menubar = self.menuBar()
        tools = menubar.addMenu("Tools")

        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")

        tools.addAction(exit)

        exit.triggered.connect(self.Exit_Program)
    def Exit_Program(self):
        qApp.exit()

class User_Control(QWidget):
    def __init__(self):
        super().__init__()

        Name = QLabel("User Name")
        self.NameText = QLineEdit()
        Password = QLabel("Password")
        self.PasswordText = QLineEdit()
        self.PasswordText.setEchoMode(QLineEdit.Password)
        LoginButton = QPushButton("Login")
        self.answer = QLabel("")

        h_box_first = QHBoxLayout()
        h_box_first.addWidget(Name)
        h_box_first.addWidget(self.NameText)

        h_box_second = QHBoxLayout()
        h_box_second.addWidget(Password)
        h_box_second.addWidget(self.PasswordText)


        v_box_main = QVBoxLayout()
        v_box_main.addStretch()
        v_box_main.addLayout(h_box_first)
        v_box_main.addLayout(h_box_second)
        v_box_main.addWidget(LoginButton)
        v_box_main.addWidget(self.answer)
        v_box_main.addStretch()


        h_box_main = QHBoxLayout()
        h_box_main.addStretch()
        h_box_main.addLayout(v_box_main)
        h_box_main.addStretch()
        LoginButton.clicked.connect(self.User_Authentication)
        self.setLayout(h_box_main)

    def User_Authentication(self):

        name = self.NameText.text()
        password = self.PasswordText.text()

        print(name)
        print(password)



        user = Date_Base().Users_Query(name ,password)

        
        print(len(user))
        size = len(user)
        if size == 0 :
            self.answer.setText("Please try again with incorrect username or password")
        else:
            self.answer.setText("Login successful ,Please Wait")
            JuctionCenter().Exit_Program()

            app = QApplication(sys.argv)
            window_second = JuctionCenter_Second()
            window_second.show()
            sys.exit(app.exec_())

class JuctionCenter_Second(QMainWindow):

    def __init__(self):
        super().__init__()

        self.Intarface_Main()
        self.MenuBar()
        self.panel = General_Panel()
        self.setCentralWidget(self.panel)


    def Interface_Main(self):
        self.title = "Market Otomation"
        self.top = 250
        self.left = 150
        self.width = 550
        self.height = 400
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("Market_icon.png"))
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.title = "Market Otomation"

    def MenuBar(self):

        menubar = self.menuBar()
        tools = menubar.addMenu("Tools")
        edit = menubar.addMenu("Edit")

        exit = QAction("Exit")
        exit.setShortcut("Ctrl+Q")
        tools.addAction(exit)

        update = edit.addMenu("Update")
        name_up = QAction("User Name Update")
        password_up = QAction("Password Update")
        update.addAction(name_up)
        update.addAction(password_up)


        exit.triggered.connect(self.Exit_Program)

        self.show()

    def Exit_Program(self):
        qApp.exit()


class General_Panel(QWidget):
    def __init__(self):
        super().__init__()

    def Interface_Panel(self):
        screen_print = QLabel("hello word")
        v_box = QVBoxLayout()
        v_box.addWidget(screen_print)
        self.setLayout(v_box)

class Date_Base():

    def __init__(self):
        self.Connect_db()


    def Connect_db(self):

        self.con = sqlite3.connect("Users.db")
        self.cursor = self.con.cursor()

        query = "CREATE TABLE IF NOT EXISTS USERS(NAME TEXT , PASSWORD TEXT)"
        self.cursor.execute(query)
        self.con.commit()
    def Users_Query(self ,name ,password):
        query = "SELECT * FROM USERS WHERE NAME = ? AND PASSWORD = ?"
        self.cursor.execute(query ,(name ,password))
        feedback = self.cursor.fetchall()
        return feedback

    def User_Add(self):
        query = "INSERT INTO USERS VALUES('mustafa','123')"

        self.cursor.execute(query)
        self.con.commit()


    def Users_Wiew(self):
        query = "SELECT * FROM USERS"
        self.cursor.execute(query)
        usersList = self.cursor.fetchall()

        for i in usersList:
            print(i)




"""class Tab(QDialog):
    def __init__(self):
        super().__init__()

        tabWidget = QTabWidget()
        tabWidget.addTab(Sales_Screen() ,"Sales Screen")
        tabWidget.addTab(Product_Query() ,"Product Query")
        tabWidget.addTab()
"""
app = QApplication(sys.argv)
tell = JuctionCenter()
tell.show()
sys.exit(app.exec_())

