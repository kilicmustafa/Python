import sqlite3

import time

class Kitap():

    def __init__(self,isim ,yazar ,yayinevi ,tür ,baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tür = tür
        self.baski = baski

    def __str__(self):
        return "isim : {}\nyazar : {}\nyayinevi : {}\ntür : {}\nbaski : {}\n ***************************".format(self.isim ,self.yazar ,self.yayinevi ,self.tür ,self.baski)


class Kutuphane():

    def __init__(self):

        self.Baglanti_ac()

    def Baglanti_ac(self):

        self.con = sqlite3.connect("Kütüphane.db")
        self.cursor = self.con.cursor()
        sorgu = "Create Table If not exists kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"

        self.cursor.execute(sorgu)

        self.con.commit()

    def Baglanti_kes(self):
        self.con.close()

    def Kitap_Göster(self):

        sorgu = "SELECT * FROM kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if (len(kitaplar) == 0):
            print("Kitap bulunamadı")
        else:

            for i in kitaplar:
                kitap = Kitap(i[0] ,i[1] ,i[2] ,i[3] ,i[4])
                print(kitap)

    def Kitap_Sorgula(self,isim):

        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()
        if (len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor......")

        else:
            kitap = Kitap(kitaplar[0][0] ,kitaplar[0][1] ,kitaplar[0][2] ,kitaplar[0][3] ,kitaplar[0][4])

            print(kitap)


    def Kitap_Ekle(self,kitap):

        sorgu = "INSERT INTO kitaplar VALUES(?,?,?,?,?)"
        self.cursor.execute(sorgu ,(kitap.isim ,kitap.yazar ,kitap.yayinevi ,kitap.tür ,kitap.baski))
        self.con.commit()

    def Son_Kitabi_Yazdir(self):
        sorgu = "SELECT * FROM kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        s = len(kitaplar) -1

        kitap = Kitap(kitaplar[s][0] ,kitaplar[s][1] ,kitaplar[s][2] ,kitaplar[s][3] ,kitaplar[s][4] ,)
        print(kitap)

    def Kitap_Sil(self ,isim):
        sorgu = "DELETE FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu ,(isim,))
        self.con.commit()

    def Baski_Yukselt(self,isim):

        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu ,(isim,))
        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Olmayan Kitabin Baskısı Yükseltilmez")

        else:
            baski = kitaplar[0][4]
            baski += 1

            sorgu = "UPDATE kitaplar SET baskı = ? WHERE isim = ?"
            self.cursor.execute(sorgu ,(baski,isim))
            self.con.commit()
