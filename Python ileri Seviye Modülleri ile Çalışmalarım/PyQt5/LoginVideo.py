import sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.baglan()
        self.init_ui()



    def init_ui(self):
        self.UserName = QtWidgets.QLineEdit()
        self.UserPassword = QtWidgets.QLineEdit()
        self.UserPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Login_Button = QtWidgets.QPushButton("Login")
        self.Text_Label = QtWidgets.QLabel("")

        V_box = QtWidgets.QVBoxLayout()

        V_box.addWidget(self.UserName)
        V_box.addWidget(self.UserPassword)
        V_box.addWidget((self.Text_Label))
        V_box.addStretch()
        V_box.addWidget((self.Login_Button))


        H_box = QtWidgets.QHBoxLayout()

        H_box.addStretch()
        H_box.addLayout(V_box)
        H_box.addStretch()

        self.setLayout(H_box)

        self.Login_Button.clicked.connect(self.Login)

        self.show()

    def Login(self):



        a = self.UserName.text()
        b = self.UserPassword.text()
        self.cursor.execute("SELECT * FROM üyeler WHERE kullanıcı_adı = ? and parola = ? ",(a ,b))

        User = self.cursor.fetchall()

        if (len(User) == 0):
            self.Text_Label.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin!")
        else:
            self.Text_Label.setText("Giriş Başarılı")




    def baglan(self):
        connection = sqlite3.connect("Kullanicilar.db")
        self.cursor = connection.cursor()





        self.cursor.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")
        connection.commit()






app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())