import sys

from PyQt5 import QtWidgets

def pencere():

    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Baslık")

    okey_button = QtWidgets.QPushButton("Tamam")
    cancel_button = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()

    h_box.addWidget(okey_button)
    h_box.addStretch()
    h_box.addWidget(cancel_button)

    pencere.setLayout(h_box)

    pencere.setGeometry(100 ,100 ,500 ,500)

    pencere.show()

    sys.exit(app.exec_())

pencere()

