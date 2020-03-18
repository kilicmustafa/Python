import sys
from PyQt5.QtWidgets import QWidget ,QApplication ,QCheckBox ,QLabel ,QPushButton ,QVBoxLayout

class Pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.Checkbox = QCheckBox("Lisans Koşullarını Kabul Ediyorum")
        self.Label = QLabel("")
        self.PushButton = QPushButton("KUR")

        V_box = QVBoxLayout()

        V_box.addWidget(self.Checkbox)
        V_box.addWidget(self.Label)
        V_box.addWidget(self.PushButton)

        self.setLayout(V_box)

        self.setWindowTitle("CheckBox")

        self.PushButton.clicked.connect(lambda : self.click(self.Checkbox.isChecked() ,self.Label))
        self.show()


    def click(self,isaret , metin):

        if isaret:
            metin.setText("Program Kuruldu")

        else:
            metin.setText("Lisans Koşullarını kabul ediniz")



app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())