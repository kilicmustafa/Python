import sys
import os
from PyQt5.QtWidgets import  QTabWidget,qApp ,QAction ,QApplication ,QPushButton ,QMainWindow ,QTextEdit ,QFileDialog ,QLabel ,QWidget ,QHBoxLayout ,QVBoxLayout  ,QLineEdit
from PyQt5 import QtCore
from PyQt5 import QtGui

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):


        self.link_label = QLabel("commantLinkButtonEkle")
        self.sender_label = QLabel("Sender;")
        self.sender_mail_label = QLabel("E-Mail Adress")
        self.sender_mail_line = QLineEdit()
        self.sender_password_label = QLabel("E-Mail Password")
        self.sender_password_line = QLineEdit()
        self.sender_password_line.setEchoMode(QLineEdit.Password)

        self.receiver_label = QLabel("Receiver;")
        self.receiver_mail_label = QLabel("E-Mail Adress")
        self.receiver_mail_line  = QLineEdit()
        self.answer = QLabel("")

        self.mail_subject_label = QLabel("Mail Subject")
        self.mail_subject_line  = QLineEdit()
        self.message_line = QLabel("Mail Content")
        self.message_content = QTextEdit("Mail gönderebilmek için ,Daha az güvenli uygulama erişimi sol üst köşeden aktif edin")

        self.cleaner_but = QPushButton("Cleaner")
        self.open_but = QPushButton("Open")
        self.save_but = QPushButton("Save")
        self.send_but = QPushButton("Send")
        self.test_but = QPushButton("Test")

        h_combination_1 = QHBoxLayout()
        h_combination_1.addWidget(self.sender_mail_label)
        h_combination_1.addWidget(self.sender_mail_line)

        h_combination_2 = QHBoxLayout()
        h_combination_2.addWidget(self.sender_password_label)
        h_combination_2.addWidget(self.sender_password_line)

        h_combination_3 = QHBoxLayout()
        h_combination_3.addWidget(self.receiver_mail_label)
        h_combination_3.addWidget(self.receiver_mail_line)

        h_combination_4 = QHBoxLayout()
        h_combination_4.addStretch()
        h_combination_4.addWidget(self.answer)
        h_combination_4.addStretch()

        v_left_box = QVBoxLayout()
        v_left_box.addStretch()

        v_left_box.addWidget(self.link_label)
        v_left_box.addWidget(self.sender_label)
        v_left_box.addLayout(h_combination_1)
        v_left_box.addLayout(h_combination_2)
        v_left_box.addStretch()
        v_left_box.addWidget(self.receiver_label)

        v_left_box.addLayout(h_combination_3)
        v_left_box.addStretch()
        v_left_box.addLayout(h_combination_4)


        h_combination_5 = QHBoxLayout()
        h_combination_5.addWidget(self.mail_subject_label)
        h_combination_5.addWidget(self.mail_subject_line)

        v_right_box = QVBoxLayout()
        v_right_box.addLayout(h_combination_5)

        v_right_box.addWidget(self.message_line)
        v_right_box.addWidget(self.message_content)


        h_combination_l_r = QHBoxLayout()
        h_combination_l_r.addLayout(v_left_box)
        h_combination_l_r.addLayout(v_right_box)

        h_combination_but = QHBoxLayout()
        h_combination_but.addWidget(self.cleaner_but)
        h_combination_but.addWidget(self.test_but)
        h_combination_but.addWidget(self.open_but)
        h_combination_but.addWidget(self.save_but)
        h_combination_but.addWidget(self.send_but)

        v_box_window = QVBoxLayout()
        v_box_window.addLayout(h_combination_l_r)
        v_box_window.addLayout(h_combination_but)

        self.cleaner_but.clicked.connect(self.Cleaner_click)
        self.test_but.clicked.connect(self.Test_click)
        self.open_but.clicked.connect(self.Open_click)
        self.save_but.clicked.connect(self.Save_click)
        self.send_but.clicked.connect(self.Send_click)

        self.setLayout(v_box_window)

    def new_widget(self):
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)

        self.tabs.addTab(self.tab1 ,"Table 1")
        self.tabs.addTab(self.tab2 ,"Table 2")

        self.button = QPushButton("Okey")

        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.button)
        self.tab1.setLayout(self.tab1.layout)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


    def new_tab(self):
        self.new_answer = QLabel("")
        self.new_Ok_but = QPushButton("Ok")

        new_h_box = QHBoxLayout()
        new_h_box.addWidget(self.new_answer)
        new_h_box.addWidget(self.new_Ok_but)

        new_v_box = QVBoxLayout()
        new_v_box.addLayout(new_h_box)
        self.setLayout(new_v_box)
        self.show()

    def Cleaner_click(self):
        self.message_content.clear()


    def Test_click(self):
        From = "kilicmustafa.tr@gmail.com"
        Password = "null"
        To = "mustafaklc2434@gmail.com"
        Subject = "Test"
        Content = "Null"
        self.Send_mail(From ,Password ,To ,Subject ,Content)

    def Send_mail(self ,From ,Password ,To ,Subject ,Content):

        print("ben")
        message = MIMEMultipart()

        message["From"] = From

        message["To"] = To

        message["Subject"] = Subject

        message_content = Content


        message_g = MIMEText(message_content, "plain")

        message.attach(message_g)
        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)

            mail.ehlo()

            mail.starttls()

            mail.login(message["From"], Password)

            mail.sendmail(message["From"], message["To"], message.as_string())


            self.answer.setText("Mail Server Online")
            mail.close()



        except :
            self.answer.setText("Test Clicked and Rename abaout")



            "Sender E-Mail And Password Error"
        """except SMTPRecipientsRefused:
            self.answer.setText("Reciver E-Mail Error")
"""
    def Open_click(self):
        file_name = QFileDialog.getOpenFileName(self ,"Open File" ,os.getenv("HOME"))
        with open(file_name[0] ,"r") as file:
            self.message_content.setText(file.read())
            #tüm alanları import eden algoritma ekle

    def Save_click(self):
        file_name = QFileDialog.getSaveFileName(self , "Save File" ,os.getenv("HOME"))
        with open(file_name[0] +".txt" ,"w") as file:
            file.read(self.message_content.toPlainText())

    def Send_click(self):
        From = self.sender_mail_line.text()
        Password = self.sender_password_line.text()
        To = self.receiver_mail_line.text()
        Subject = self.mail_subject_line.text()
        Content = self.message_content.toPlainText()


        if ((len(From) >= 1) and (len(Password) >= 1) and  ( len(To) >= 1) and (len(Subject) >= 1) and (len(Content) >= 1)):
            self.Send_mail(From,Password,To,Subject,Content)

        else:
            self.answer.setText("Tüm alanları eksiksiz doldurun")



class Menus(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = Window()
        self.setCentralWidget(self.window)
        self.Menu()
        self.show()

    def Menu(self):

        menubar = self.menuBar()
        file = menubar.addMenu("File")
        editor = menubar.addMenu("Editor")

        open_ = QAction("Open",self)
        save_ = QAction("Save",self)
        send_ = QAction("Send",self)

        file.addAction(open_)
        file.addAction(save_)
        file.addAction(send_)

        cleaner = QAction("Cleaner",self)
        cleaner.setShortcut("Ctrl+M")

        test = QAction("Test",self)
        test.setShortcut("Ctrl+T")

        exit = QAction("Exit")
        exit.setShortcut("Ctrl+Q")

        new_tab = QAction("New Tab",self)
        new_tab.setShortcut("Ctrl+N")

        editor.addAction(cleaner)
        editor.addAction(test)
        editor.addAction(new_tab)

        exit.triggered.connect(self.Exit_program)
        file.triggered.connect(self.Response)
        editor.triggered.connect(self.Response)

    def Exit_program(self):
        qApp.exit()

    def Response(self ,action):

        if action.text() == "Open":
            self.window.Open_click()

        elif action.text() == "Save":
            self.window.Save_click()

        elif action.text() == "Send":
            self.window.Send_click()

        elif action.text() == "Cleaner":
            self.window.Cleaner_click()

        elif action.text() == "Test":
            self.window.Test_click()

        elif action.text() == "New Tab":
            self.window.new_tab()











app = QApplication(sys.argv)

window = Menus()
sys.exit(app.exec_())


