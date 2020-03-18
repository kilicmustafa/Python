import sys

from PyQt5.QtWidgets import QWidget ,QPushButton ,QApplication ,QLabel ,QRadioButton ,QVBoxLayout ,QLayout


class Pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.Label_head = QLabel("Hangi dili seviyorsunuz ? ")
        self.java = QRadioButton("Java")
        self.python = QRadioButton("Python")
        self.php = QRadioButton("Php")
        self.cikti = QLabel("")
        self.Push_button = QPushButton("Send")

        v_box = QVBoxLayout()
        v_box.addWidget(self.Label_head)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.cikti)
        v_box.addWidget(self.Push_button)

        self.setLayout(v_box)

        self.setWindowTitle("RadioButton")

        self.Push_button.clicked.connect(lambda : self.click(self.java.isChecked() ,self.python.isChecked() ,self.php.isChecked() ,self.cikti))

        self.show()

    def click(self,java ,python ,php ,yazi_alani):

        if java:
            yazi_alani.setText("JAVA")
        if python:
            yazi_alani.setText("PYTHON")
        if php:
            yazi_alani.setText("PHP")




app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
