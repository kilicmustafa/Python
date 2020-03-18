import sys

from PyQt5 import QtWidgets

def pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Uygulama")

    Okey_button = QtWidgets.QPushButton("Okey")
    Cancel_button = QtWidgets.QPushButton("Cancel")

    h_box = QtWidgets.QHBoxLayout()
    h_box.addWidget(Okey_button)

    h_box.addStretch()

    h_box.addWidget(Cancel_button)



    pencere.setLayout(h_box)

    pencere.show()
    sys.exit(app.exec_())


pencere()

