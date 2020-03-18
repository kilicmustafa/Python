import _sqlite3
import sys
import os
import time
from PyQt5.QtWidgets import QWidget , QLineEdit, QPushButton ,QTextEdit ,QVBoxLayout ,QApplication ,QRadioButton ,QHBoxLayout ,QLabel ,QFileDialog

"""class Datebase():

    def Datebase_Connect(self):
        self.connection = _sqlite3.connect("records.db")
        self.cursor = connection.cursor()

        query = "Create Table If Not Exists TextSaved (Name TEXT ,Content TEXT)"
        self.cursor.excute(query)

        self.connection.commit()

    def Datebase_Disconnect(self):
        self.connection.close()

    def Datebase_Content_Saved(self ,file_name ,content):

        query = "Insert Into TextSaved Values( ? , ? )"
        self.cursor.excute(query ,(file_name ,content))
        self.connection.commit()
"""
class File():

    def File_Open(self ,content ,answer):
        file_name = QFileDialog.getOpenFileName(self ,"File Open" ,os.getenv("HOME"))
        try:
            with open(file_name ,"r" ,"UTF-8") as file:
                content.setText(file.read())
            answer.setText("File Open Succesfuly")
        except:
            answer.setText("File Open ERROR")

    def File_Saved(self ,content ,answer):
        file_name = QFileDialog.getSaveFileName(self ,"File Saved" ,os.getevn("HOME"))
        try:
            with open( (file_name+"txt") ,"w" ,encoding="UTF-8") as file:
                file.write(content)
            answer.setText("File Saved Succesfuly")

        except:
            answer.setText("File Saved Error")


class Window(QWidget,File): #Datebase
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label_text = QLabel("Text;")
        self.content = QTextEdit()

        """self.file_datebase = QRadioButton("File Saved DATABASE")
        self.file_text = QRadioButton("File Saved TEXT")"""

        self.label_save = QLabel("File Name :")
        self.file_name = QLineEdit()

        self.clear = QPushButton("Clear")
        self.save = QPushButton("Save")
        self.open = QPushButton("Open")

        self.answer = QLabel("")


        """h_box_line = QHBoxLayout()
        h_box_line.addWidget(self.label_save)
        h_box_line.addWidget(self.file_name)"""


        h_box_button = QHBoxLayout()
        h_box_button.addWidget(self.clear)
        h_box_button.addWidget(self.open)
        h_box_button.addWidget(self.save)


        h_box_radio_answer = QHBoxLayout()
        """h_box_radio_answer.addWidget(self.file_datebase)
        h_box_radio_answer.addWidget(self.file_text)"""
        h_box_radio_answer.addStretch()
        h_box_radio_answer.addWidget(self.answer)


        v_box = QVBoxLayout()
        v_box.addWidget(self.label_text)
        v_box.addWidget(self.content)
        v_box.addLayout(h_box_radio_answer)

        v_box.addLayout(h_box_button)



        self.setLayout(v_box)

        self.setWindowTitle("TextEdit")

        self.clear.clicked.connect(self.Clear_click)
        self.save.clicked.connect(lambda : self.Save_click(self.content ,self.file_name,self.file_datebase.isChecked(),self.file_text.isChecked(),self.answer))

        self.show()

    def Clear_click(self):
        self.content.clear()
        self.answer.setText("Temizleme Başarılı !")#giden yazı yap !!!!!!!!!!!!!!



    def Save_click(self ,content ,file_name ,file_datebase ,file_text ,answer):


        """sender = self.sender()

        if (sender.text() == "Clear"):
            self.content.clear()      program bitince birleştirmeyi dene"""

        content = content.text()

        if file_datebase:
            try :
                self.Datebase_Connect()

                file_name = file_name.text()

                self.Datebase_Content_Saved(file_name ,content)

                self.Datebase_Disconnect()

                answer.setText("KAYIT BAŞARILI")



            except:
                answer.setText("KAYIT BAŞARISIZ") #Program bitince hata tespiti yapıp hataları ekle

        if file_text:
            try:
                self.Files_Saved(content ,answer)
                answer.setText("KAYIT BAŞARILI")

            except:
                answer.setText("KAYIT BAŞARISIZ")
















app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())