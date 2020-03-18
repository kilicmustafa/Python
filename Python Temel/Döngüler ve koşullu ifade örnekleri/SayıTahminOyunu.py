import random as r
import time as t
print ("""
       **************************************
       
         Sayı Tahmin Oyununa Hoşgeldiniz 
         
         ******************************
       """)

rasgele_Sayi = r.randint(1,40)
hak = 7

while True:
    tahmin = int(input("Bir sayı giriniz(1-40 arası) : "))
    
    
    if (tahmin > rasgele_Sayi):
        print("Sorgu yapılıyor...")
        t.sleep(1)
        print("Daha küçük sayi girin")
        hak -= 1
        
    elif (tahmin < rasgele_Sayi):
        print("Sorgu yapılıyor...")
        t.sleep(1)
        print("Daha büyük sayi girin")
        hak -= 1
    else :
        print("Tebrikler Dogru tahminde bulundunuz")
        break
    if ( hak == 0 ):
        print("Tahmin hakkınız bitmiştir sayi : ",rasgele_Sayi)
        break