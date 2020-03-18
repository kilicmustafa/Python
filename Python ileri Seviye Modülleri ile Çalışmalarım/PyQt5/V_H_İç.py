import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()

    okey_button = QtWidgets.QPushButton("Okey")
    cancel_button = QtWidgets.QPushButton("Cancel")

    H_box = QtWidgets.QHBoxLayout()

    H_box.addStretch()
    H_box.addWidget(okey_button)
    H_box.addWidget(cancel_button)

    V_box = QtWidgets.QVBoxLayout()

    V_box.addStretch()
    V_box.addLayout(H_box)

    pencere.setLayout(V_box)
    pencere.show()
    sys.exit(app.exec_())


Pencere()

