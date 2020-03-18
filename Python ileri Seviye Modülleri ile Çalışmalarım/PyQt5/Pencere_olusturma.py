import sys 

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QtWidgets()

    pencere.setWinndowTitle("New Tab")

    pencere.show()

    sys.exit(app.exec_())


Pencere()