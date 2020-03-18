import sys
from PyQt5.QtWidgets import QWidget ,QLabel ,QApplication ,QHBoxLayout ,QPushButton ,QButtonGroup
from PyQt5 import QtCore
from PyQt5 import QtGui

class MainWidow(QWidget):
    def __init__(self):
        super().__init__()

        self.Window_Properties()
        self.Window_Properties_Apply()
        self.Interface()

    def Window_Properties(self):
        self.title = "PyQt5 Button Group"
        self.top = 200
        self.left = 500
        self.width = 500
        self.height = 500
        self.iconName = "icon.png"


    def Window_Properties_Apply(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.top , self.left ,self.width ,self.height)



    def Interface(self):
        self.label = QLabel()
        button_twelfth = QPushButton("Twelfth")
        button_twelfth.setFont(QtGui.QFont("Sanserif" ,15))
        button_twelfth.setIcon(QtGui.QIcon("icon.png"))
        button_twelfth.setIconSize(QtCore.QSize(40 ,40))

        button_thirteenth = QPushButton("Thirteenth")
        button_fourteenth = QPushButton("Fourteeth")

        self.buttonGroup = QButtonGroup()
        self.buttonGroup.addButton(button_twelfth ,1)
        self.buttonGroup.addButton(button_thirteenth ,2)
        self.buttonGroup.addButton(button_fourteenth , 3)

        h_box = QHBoxLayout()
        h_box.addWidget(self.label)
        h_box.addWidget(button_twelfth)
        h_box.addWidget(button_thirteenth)
        h_box.addWidget(button_fourteenth)


        self.buttonGroup.buttonClicked[int].connect(self.On_Button_Clicked)
        self.setLayout(h_box)

    def On_Button_Clicked(self ,id):
        for button in self.buttonGroup.buttons():
            if button is self.buttonGroup.button(id):
                self.label.setText(button.text() + " Was Clicked")




if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWidow()
    window.show()
    sys.exit(App.exec_())






