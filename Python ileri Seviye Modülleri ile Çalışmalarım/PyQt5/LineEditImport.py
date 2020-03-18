import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.yazi_alanı = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Clear")
        self.yazdir = QtWidgets.QPushButton("Print")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addStretch()

        v_box.addWidget(self.yazi_alanı)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdir)

        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.temizle.clicked.connect(self.click)
        self.yazdir.clicked.connect(self.click)

        self.show()


    def click(self):
        sender = self.sender()

        if (sender.text() == "Clear"):
            self.yazi_alanı.clear()

        else:
            print(self.yazi_alanı.text())


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())