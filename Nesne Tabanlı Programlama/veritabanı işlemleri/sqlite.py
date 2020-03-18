class veritabani():
    def __init__(self,ad,yazar,yayinevi,sayfa_sayisi):
        self.ad = ad
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.sayfa_sayisi = sayfa_sayisi

        import sqlite3
        self.con = sqlite3.connect("kütüphane.db")
        self.cursor = self.con.cursor()


    def kayitEkle(self):
        self.cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)" ,(self.ad ,self.yazar ,self.yayinevi ,self.sayfa_sayisi))
        self.con.commit()
        self.con.close()

    #def TabloEkle(self):
     #   self.cursor.execute("CREATE TABLE kitaplar ")

veri = veritabani()
a = input("Ad : ")
b = input("Yazar : ")
c = input("Yayin evi : ")
d = int(input("Sayfa sayisi : "))

veri.kayitEkle(a,b,c,d)