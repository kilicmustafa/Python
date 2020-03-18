import sys
from PyQt5.QtWidgets import QDoubleSpinBox, QLineEdit, QApplication ,QMainWindow ,QWidget ,QTableWidget ,QTableWidgetItem , qApp,QVBoxLayout ,QAction ,QHBoxLayout ,QLabel ,QGroupBox ,QPushButton ,QDialog ,QDialogButtonBox ,QCheckBox ,QTabWidget ,QListWidget
from PyQt5.QtGui import QIcon

import sqlite3



class JuctionCenter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Interface_Main()
        self.ControlCenter()

    def Interface_Main(self):
        self.title = "Song Management Panel"
        self.top = 100
        self.left = 100
        self.width = 560
        self.height = 400
        self.setWindowIcon(QIcon("Song_Icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)


    def ControlCenter(self):

        """self.importMenu = MenuBar()
        self.setCentralWidget(self.importMenu)"""
        self.MenuBarWidget()
        self.importTab = Tab()
        self.setCentralWidget(self.importTab)

    def MenuBarWidget(self):
        menubar = self.menuBar()
        tools = menubar.addMenu("Tools")

        exit_ = QAction("Exit")
        exit_.setShortcut("Ctrl+Q")
        tools.addAction(exit_)

        exit_.triggered.connect(self.Exit_Program)

    def Exit_Program(self):
        qApp.exit()

"""class MenuBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.MenuBarWidget()"""




class Tab(QDialog):
    def __init__(self):
        super().__init__()



        tabWidget = QTabWidget()
        tabWidget.addTab(Song_Show() ,"Song Show")
        tabWidget.addTab(Song_Find() ,"Song Find")
        tabWidget.addTab(Song_Delete() ,"Song Delete")
        tabWidget.addTab(Song_Add() ,"Song Add")

        v_box = QVBoxLayout()
        v_box.addWidget(tabWidget)



        self.setLayout(v_box)


    def Refresh_Click(self):
        Song_Show().__init__()
"""////////////////////////////////////////////////////////////////////////////////////////////"""
class Song_Show(QWidget):
    def __init__(self):
        super().__init__()

        self.Interface()
        self.Groupbox()





    def Interface(self):
        self.refresh = QPushButton("Refresh")
        songList = Transactions().Song_Wiew()
        size = len(songList)

        self.reply = QLabel("")
        self.v_boxLabel = QVBoxLayout()
        self.v_boxLabel.addWidget(self.reply)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(size)
        self.tableWidget.setColumnCount(5)

        self.v_boxTable = QVBoxLayout()
        self.v_boxTable.addWidget(self.tableWidget)
        self.v_boxTable.addWidget(self.refresh)


        """self.setLayout(self.v_boxLayout)"""

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Song Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Artist"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Album Name"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Production"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("Song Time"))



        if size == 0 :
            self.reply.setText("Soung list Your empty")
        else :
            self.reply.setText("Number Of Song; " + str(size))
            for i in range(0, size):
                for j in range(0, 5):
                    liste_str = str(songList[i][j])
                    self.tableWidget.setItem(i +1, j, QTableWidgetItem(liste_str))



        if self.refresh.isChecked():
            self.Interface()
            self.Groupbox()

    def Groupbox(self):

        groupBox_table = QGroupBox("List;")
        groupBox_table.setLayout(self.v_boxTable)


        groupBox_reply = QGroupBox("Reply")
        groupBox_reply.setLayout(self.v_boxLabel)
        v_box = QVBoxLayout()
        v_box.addWidget(groupBox_table)

        v_box.addWidget(groupBox_reply)


        self.setLayout(v_box)

"""////////////////////////////////////////////////////////////////////////////"""
class Song_Find(QWidget):
    def __init__(self):
        super().__init__()
        self.Interface()

    def Interface(self):
        search = QLabel("Search")
        self.searchEdit = QLineEdit()
        self.searchButton = QPushButton("Find")
        self.search_answer = QLabel("")
        self.search_piece = QLabel("")

        h_box_first = QHBoxLayout()
        h_box_first.addWidget(search)
        h_box_first.addWidget(self.searchEdit)
        h_box_first.addWidget(self.searchButton)

        h_box_second = QHBoxLayout()

        h_box_second.addWidget(self.search_answer)
        h_box_second.addWidget(self.search_piece)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)

        self.v_boxTable = QVBoxLayout()
        self.v_boxTable.addLayout(h_box_first)
        self.v_boxTable.addWidget(self.tableWidget)
        self.v_boxTable.addLayout(h_box_second)

        """self.setLayout(self.v_boxLayout)"""

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Song Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Artist"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Album Name"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Production"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("Song Time"))


        self.setLayout(self.v_boxTable)

        self.searchButton.clicked.connect(self.FindTable)




        self.setLayout(self.v_boxTable)


    def FindTable(self):

        self.songList = Transactions().Song_Search(self.searchEdit.text())
        print(self.songList)
        self.size = len(self.songList)
        self.tableWidget.setRowCount(self.size)


        self.tableWidget.setItem(0, 0, QTableWidgetItem("Song Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Artist"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Album Name"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Production"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("Song Time"))
        if self.size == 0:
            self.search_answer.setText("Song not found")
            self.search_piece.clear()

            self.tableWidget.setItem(0, 0, QTableWidgetItem("Song Name"))
            self.tableWidget.setItem(0, 1, QTableWidgetItem("Artist"))
            self.tableWidget.setItem(0, 2, QTableWidgetItem("Album Name"))
            self.tableWidget.setItem(0, 3, QTableWidgetItem("Production"))
            self.tableWidget.setItem(0, 4, QTableWidgetItem("Song Time"))
        else:
            self.search_piece.setText("Number Of Song;" + str(self.size))


            for i in range(0, self.size):
                for j in range(0, 5):
                    liste_str = str(self.songList[i][j])
                    self.tableWidget.setItem(i +1 , j, QTableWidgetItem(liste_str))
            self.search_answer.setText("Song find succecfuly")
            self.searchEdit.clear()
            self.setLayout(self.v_boxTable)

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
class Song_Delete(QWidget):
    def __init__(self):
        super().__init__()
        self.Interface()
        self.GroupBox()
    def Interface(self):
        name = QLabel("Name")
        self.nameEdit = QLineEdit()
        delete = QPushButton("Delete")
        self.answer = QLabel("")
        self.songInfermation = QLabel("")

        h_box = QHBoxLayout()
        h_box.addWidget(name)
        h_box.addWidget(self.nameEdit)
        h_box.addWidget(delete)

        h_box_2 = QHBoxLayout()
        h_box_2.addStretch()
        h_box_2.addWidget(self.answer)
        h_box_2.addStretch()

        self.v_box  = QVBoxLayout()
        self.v_box.addLayout(h_box)
        self.v_box.addLayout(h_box_2)

        self.v_box_2 = QVBoxLayout()
        self.v_box_2.addWidget(self.songInfermation)

        delete.clicked.connect(self.deleteSong)


    def GroupBox(self):

        GroupBoxTable = QGroupBox("Deleted Song İnformation")
        GroupBoxTable.setLayout(self.v_box_2)

        v_box_main = QVBoxLayout()
        v_box_main.addLayout(self.v_box)
        v_box_main.addWidget(GroupBoxTable)
        self.setLayout(v_box_main)


    def deleteSong(self):
        inputName = self.nameEdit.text()
        print(inputName)
        songList = Transactions().Song_Search_filter(inputName)



        print(songList)
        if (len(songList) == 0):
            self.answer.setText("Not Found the a like Song")

        else:
            Transactions().Song_Delete(inputName)

            self.answer.setText("Song Deleted Succesfuly")
            for i in songList:
                song = Song(i[0],i[1], i[2], i[3], i[4])
            self.songInfermation.setText(str(song))



"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
class Song_Add(QWidget):
    def __init__(self):
        super().__init__()
        self.TableWidget()
        self.Interface()
        self.SpinBox()
        self.rowCount = 0



    def Interface(self):

        name = QLabel("Song Name;")
        self.nameEdit = QLineEdit()



        artist = QLabel("Atist;")
        self.artistEdit = QLineEdit()


        album = QLabel("Album Name;")
        self.albumEdit = QLineEdit()



        production= QLabel("Prodiction;")
        self.productionEdit = QLineEdit()


        time = QLabel("Song Time")
        self.timeSpinBox = QDoubleSpinBox()
        self.timeAnswer = QLabel("")

        submitButton = QPushButton("Submit")

        self.feedBack = QLabel("")

        v_box_Left = QVBoxLayout()
        v_box_Left.addWidget(name)
        v_box_Left.addWidget(artist)
        v_box_Left.addWidget(album)
        v_box_Left.addWidget(production)
        v_box_Left.addWidget(time)

        v_box_Right = QVBoxLayout()
        v_box_Right.addWidget(self.nameEdit)
        v_box_Right.addWidget(self.artistEdit)
        v_box_Right.addWidget(self.albumEdit)
        v_box_Right.addWidget(self.productionEdit)
        v_box_Right.addWidget(self.timeSpinBox)

        h_box_Upper = QHBoxLayout()
        h_box_Upper.addLayout(v_box_Left)
        h_box_Upper.addLayout(v_box_Right)

        v_box_main = QVBoxLayout()
        v_box_main.addLayout(h_box_Upper)
        v_box_main.addWidget(self.timeAnswer)
        v_box_main.addWidget(submitButton)
        v_box_main.addWidget(self.feedBack)
        v_box_main.addWidget(self.tableWidget)

        submitButton.clicked.connect(self.Submit_Click)

        self.setLayout(v_box_main)

    def Submit_Click(self):
        name = self.nameEdit.text()
        artist = self.artistEdit.text()
        album = self.albumEdit.text()
        production = self.productionEdit.text()
        songTime = str(self.timeSpinBox.value())
        print(type(songTime))
        print(songTime)

        a = len(name)
        b = len(artist)
        c = len(album)
        d = len(production)


        if( (a == 0 ) or (b == 0) or (c == 0 ) or (d == 0) ):
            self.feedBack.setText("Missing information")

        else:
            Song_information = Song(name ,artist ,album ,production ,songTime)
            Transactions().Song_Add(Song_information)
            self.feedBack.setText("Adding Succesfuly")
            self.rowCount += 1
            self.tableWidget.setItem(self.rowCount ,0 ,QTableWidgetItem(name))
            self.tableWidget.setItem(self.rowCount ,1 ,QTableWidgetItem(artist))
            self.tableWidget.setItem(self.rowCount ,2 ,QTableWidgetItem(album))
            self.tableWidget.setItem(self.rowCount ,3 ,QTableWidgetItem(production))
            self.tableWidget.setItem(self.rowCount ,4 ,QTableWidgetItem(songTime))



    def TableWidget(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Song Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Artist"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Album Name"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Production"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("Song Time"))





    def SpinBox(self):




        self.timeSpinBox.setMinimum(00.30)
        self.timeSpinBox.setMaximum(10.00)
        self.timeSpinBox.valueChanged.connect(self.SpinBoxValueChanged)

    def SpinBoxValueChanged(self):
        self.timeAnswer.setText("Current Value : "+ str(self.timeSpinBox.value()))




class Transactions():

    def  __init__(self):

        self.Connect_db()




    def Connect_db(self):
        self.con = sqlite3.connect("Songs.db")
        self.cursor = self.con.cursor()

        query = "CREATE TABLE IF NOT EXISTS Songs(SongName TEXT ,Artist TEXT ,AlbumName TEXT ,Production TEXT ,SongTime TEXT)"

        self.cursor.execute(query)
        self.con.commit()

    def Close_db(self):

        self.con.close()



    def Song_Wiew(self):

        query = "SELECT * FROM Songs"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        return result
    def Song_Search(self,name):
        query = "SELECT * FROM Songs WHERE SongName LIKE ? "
        self.cursor.execute(query,('%'+ name +'%',))
        result = self.cursor.fetchall()
        return result

    def Song_Search_filter(self,name):
        query = "SELECT * FROM Songs WHERE SongName = ?"
        self.cursor.execute(query,(name,))
        result = self.cursor.fetchall()
        return result

    def Song_Delete(self,name):
        query = "DELETE FROM Songs WHERE SongName = ?"
        self.cursor.execute(query, (name,))
        self.con.commit()

    def Song_Add(self ,song):
        query = "INSERT INTO Songs VALUES(? ,? ,? ,? ,?)"
        self.cursor.execute(query ,(song.name ,song.artist ,song.albumName ,song.production ,song.songTime))
        self.con.commit()

class Song():

    def __init__(self ,name ,artist ,albumName ,production ,songTime):
        self.name = name
        self.artist = artist
        self.albumName = albumName
        self.production = production
        self.songTime = songTime

    def __str__(self):
        return "Song Name : {}\nArtist : {}\nAlbum : {}\nProduction : {}\nSong Time : {}\n**************************************\n".format(self.name ,self.artist ,self.albumName ,self.production ,self.songTime)



app = QApplication(sys.argv)
run = JuctionCenter()