"""Siz de bir tane Şarkı projesi geliştirmeye çalışın.

                     Örnek özellikler;

                     1. Şarkı İsmi
                     2. Sanatçı
                     3. Albüm
                     4. Prodüksiyon Şirketi
                     5. Şarkı Süresi

                     Örnek Metodlar;

                     1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
                     2. Şarkı Ekle
                     3. Şarkı Sil """
import sqlite3
import time as t
class Sarki():

    def __init__(self ,isim ,sanatci ,album ,produksiyon ,sure):
        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.produksiyon = produksiyon
        self.sure = sure

    def __str__(self):
        return "Şarkı İsmi : {}\nSanatçı : {}\nAlbüm : {}\nProdüksiyon Şirketi : {}\nŞarkı Süresi : {}\n**************************************\n".format(self.isim ,self.sanatci ,self.album ,self.produksiyon ,self.sure)

class islemler():

    def  __init__(self):

        self.baglanti_ac()


    def baglanti_ac(self):
        self.con = sqlite3.connect("Sarki.db")
        self.cursor = self.con.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS sarkilar(isim TEXT ,sanatci TEXT ,album TEXT ,produksiyon TEXT ,sure int)"

        self.cursor.execute(sorgu)
        self.con.commit()

    def baglantı_kapat(self):

        self.con.close()

    def sarki_goruntule(self):

        sorgu = "SELECT * FROM sarkilar"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0 ):
            print("Hiç şarkı bulunamadı")

        else :
            for i in sarkilar:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)
                print("***********************************")




    def sarki_ekle(self,sarki):

        sorgu = "INSERT INTO sarkilar VALUES(?,?,?,?,?)"

        self.cursor.execute(sorgu ,(sarki.isim ,sarki.sanatci ,sarki.album ,sarki.produksiyon ,sarki.sure))
        self.con.commit()

    def sarki_sil(self,isim):
        sorgu = "SELECT * FROM sarkilar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):
            print("Böyle Bir sarki bulunamadı")

        else:
            sorgu = "DELETE FROM sarkilar WHERE isim = ?"

            self.cursor.execute(sorgu,(isim,))
            self.con.commit()

    def sarki_bul(self,isim):

        sorgu = "SELECT * FROM sarkilar WHERE isim  LIKE ?"
        self.cursor.execute(sorgu,('%'+isim+'%',))
        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0 ):
            print("Böyle bir şarkı bulunmuyor")
        else :
            sarki = Sarki(sarkilar[0][0], sarkilar[0][1], sarkilar[0][2], sarkilar[0][3], sarkilar[0][4] )
            print(sarki)

    def sarki_toplam_süre(self):

        sorgu = "SELECT sure FROM sarkilar"
        self.cursor.execute(sorgu)
        sureler = self.cursor.fetchall()

        #s = len(sarkilar)-1
        toplam = 0
        #sureler = list()
        for i in sureler:
            #a = float(i[0])
            toplam += float(i[0]) # burada index ekleme yapılması gerekebilir


        #toplam = map(lambda x,y : x + y ,sureler)

        #print("Tum sarkıların Toplam Süresi = ",toplam)
        return toplam

    def sanatci_sarkilar(self,sanatci):

        sorgu = "SELECT * FROM sarkilar WHERE sanatci = ?"
        self.cursor.execute(sorgu,(sanatci,))
        sarkilar = self.cursor.fetchall()

        if (sarkilar == 0 ):
            print("Sanatciya ait Şarki Bulunamadı")

        else:
            sarki = Sarki()
            for i in sarkilar:
                sarki(i[0] ,i[1] ,i[2] ,i[3] ,i[4])
                print(sarki)

    def son_sarki(self):

        sorgu = "SELECT * FROM sarkilar"

        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()
        s = len(sarkilar) -1
        if (len(sarkilar) == 0):
            print("Listenizde hiç sarkı bulunmuyor...")

        else:
            sarki = Sarki(sarkilar[s][0] ,sarkilar[s][1] ,sarkilar[s][2] ,sarkilar[s][3] ,sarkilar[s][4])

            print(sarki)


