import sys 

from PyQt5 import QtWidgets ,QtGui

def pencere():

    app = QtWindets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("Pencere Baslıgı")


    etiket1 = QtWidgets.Qlabel(pencere)
    etiket2 = QtWidgets.Qlabel(pencere)

    etiket1.setText("Burası bir metindir")
    etiket2.setPixamp(QtGui.Qpixamp("python.png"))


    etiket1.move(100 ,100)
    etiket2.move(50 ,100)

    pencere.setGeometry(100,100,500,500)
    
    pencere.show()

    sys.exit(app.exec_())



