import sys
import sqlite3
from PyQt5 import QtWidgets

class Kullanici():
    def __init__(self ,USERNAME ,USERPASSWORD ,FIRSTNAME ,LASTNAME):
        self.USERNAME = USERNAME
        self.USERPASSWORD = USERPASSWORD
        self.FIRSTNAME = FIRSTNAME
        self.LASTNAME = LASTNAME




class Veritabanı():
    def __init__(self):
        self.baglan()

    def baglan(self):
        self.connection = sqlite3.connect("Kullanicilar.db")
        self.cursor = self.connection.cursor()

        sorgu = """CREATE TABLE IF NOT EXISTS USERS(ID INT,
        USERNAME  VARCHAR(25),
        USERPASSWORD VARCHAR(30),
        FIRSTNAME VARCHAR(25),
        LASTNAME VARCHAR(25))"""


        self.cursor.execute(sorgu)
        self.connection.commit()


    def baglanti_kes(self):
        self.connection.close()

    def kullanıcı_kontrol(self, Answer_userName):
        sorgu = """Select * From USERS
         Where USERNAME = ? 
         """
        self.cursor.execute(sorgu ,(self.Answer_userName,))
        self.users = self.cursor.fechall()
        if (len(self.users) == 0 ):
            print("Böyle bir kullanıcı veri tabanında yok")
        else:
            if (self.Answer_userpassword == self.users[2]):

                print("Hosgeldin" + str(self.users[3]) )


    def kullanıcı_ekle(self,kullanici):
        sorgu = """INSERT INTO USERS(USERNAME ,USERPASSWORD ,FIRSTNAME ,LASTNAME) 
        VALUES(? ,? ,? ,?) """
        self.cursor.execute(sorgu,(kullanici.USERNAME ,kullanici.USERPASSWORD ,kullanici.FIRSTNAME ,kullanici.LASTNAME))
        self.connection.commit()

    def kullanıcı_sil(self,id):
        sorgu = """DELETE FROM USERS
        WHERE ID = ?"""
        self.cursor.execute(sorgu,(id,))
        self.connection.commit()

    def parola_degis(self,id,newpassword):

        turkceKarakterler = ["ç" ,"ı" "ü" ,"ğ" ,"ö" ,"ş" ,"İ" ,"Ğ" ,"Ü" ,"Ö" ,"Ş"]



        if (len(newpassword) < 7):

            return "Lütfen parolanızı 8 haneden uzun olacak şekilde girin"



        else:
            for passchar in newpassword:

                for karakter in turkceKarakterler:
                    if (karakter == passchar):
                        return "Lütfen Parolanızda Türkçe karakter kullanmayın"
                    else:

                        sorgu = """UPDATE USERS WHERE 
                                            WHERE ID = ?"""
                        self.cursor.execute(sorgu, (id,))

                        self.connection.commit

                        return "Parola değiştirme Başarılı"









class Pencere(QtWidgets.QWidget ,Veritabanı):
    def __init__(self):
        super().__init__()
        """self.baglan()"""
        self.init_ui()

    def init_ui(self):
        self.userName = QtWidgets.QLineEdit()
        self.userPassword = QtWidgets.QLineEdit()
        self.userPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Giris")
        self.register = QtWidgets.QPushButton("Üye ol")
        self.writing_area = QtWidgets.QLabel("")

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addWidget(self.userName)
        h_box.addWidget(self.userPassword)
        h_box.addWidget(self.login)
        h_box.addWidget(self.register)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()

        self.setLayout(v_box)

        self.login.clicked.connect(self.click())
        self.register.clicked.connect(self.click())

        self.show()

    def click(self):
        self.sender_info = self.sender()

        if (self.sender_info == "Üye ol"):

            self.register_Window = QtWidgets.QWidget()
            self.register_Window.setWindowTitle("Üye ol")

            self.register_Window_FirstName = QtWidgets.QLineEdit()
            self.register_Window_LastName = QtWidgets.QlineEdit()
            self.register_Window_UserName = QtWidgets.QLineEdit()
            self.register_Window_UserPassword = QtWidgets.QLineEdit()
            self.register_Window_text1 = QtWidgets.QLabel("İSİM")
            self.register_Window_text2 = QtWidgets.QLabel("SOYİSİM")
            self.register_Window_text3 = QtWidgets.QLabel("KULLANICI ADI")
            self.register_Window_text4 = QtWidgets.QLabel("PAROLA")
            kullanici = Kullanici(self.register_Window_FirstName.text ,self.register_Window_LastName.text ,self.register_Window_UserName.text ,self.register_Window_UserPassword.text)
            self.kullanıcı_ekle(kullanici)





        else :
            self.Answer_userName = self.userName.text()
            self.Answer_userpassword = self.userPassword.text()
            self.kullanıcı_kontrol()




app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())









