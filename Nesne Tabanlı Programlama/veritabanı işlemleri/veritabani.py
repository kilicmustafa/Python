import sqlite3 
con = sqlite3.connect("kütüphana.db")
cursor = con.cursor()


def TabloEkle():
    
    cursor.execute("CREATE TABLE kitaplar(ad TEXT ,yazar TEXT ,yayinevi TEXT ,sayfa_sayisi int)")
    con.commit()
    
def VeriEkle(ad,yazar,yayinevi, sayfa_sayisi):
    
    cursor.execute("INSERT INTO kitaplar VALUES(?,?,?,?) " ,(ad ,yazar ,yayinevi ,sayfa_sayisi))
    con.commit()
    
def VeriCek():
    cursor.execute("SELECT * FROM kitaplar")
    liste = cursor.fetchall()
    for i in liste:
        print(i)
#        for a,b,c,d in i:
#            print("***************************")
#            print(""""
#                  Ad : {} 
#                  Yazar : {}
#                  Yayin Evi : {}
#                  Sayfa sayısı : {}
                
#            """.format(a,b,c,d))
#            
def IstenileniCek(istek):
    cursor.execute("SELECT * FROM kitaplar WHERE yazar = ?",(istek,))
    liste = cursor.fetchall()
    
    for i in liste:
        print(i)
#        for a,b,c,d in i:
#            print("***************************")
#            print(""""
#                  Ad : {} 
#                  Yazar : {}
#                  Yayin Evi : {}
#                  Sayfa sayısı : {}
#                
#            """.format(a,b,c,d))
        
def VerileriGuncelle(eski_yazar ,yeni_yazar):
    cursor.execute("UPDATE kitaplar SET yazar = ? where yazar = ?" ,(yeni_yazar ,eski_yazar))
    con.commit()
    
def VerileriSil(date):
    cursor.execute("DELETE FROM kitaplar WHERE yazar = ?" ,(date,))
    con.commit
    
#TabloEkle()
    
    
#istek = input("yazarı ne olsun : ")



VeriCek()
a = input("t  : ")
#b = input("c : ")
#c = input("d : ")
#VerileriGuncelle(a,b)
VerileriSil(a)
#d = int(input("sayfa sayısı : "))
#VeriEkle(a,b,c,d)


#IstenileniCek(istek)
con.close()

