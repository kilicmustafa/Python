""""
Numara =
Ad =
Soyad =

"""

from kutuphaneOtomasyon import *


kutuphane = Kutuphane()
while True:
    print("""
 Kütüphane Otomasyonuna Hoşgeldiniz
*************************************
1- Kitapları Göster
2- Kitap Sorgula
3- Kitap EKle
4- Kitap Sil
5- Baski Yükselt
6- Son Kitabı Yazdır
q - Çıkış
""")
    islem  = input("Ne Yapamak İstiyorsunuz : ")

    if (islem == "q" or islem == "Q"):
        print("Programdan Çıkılıyor.....")
        kutuphane.Baglantı_kapat()
        break

    elif (islem == "1"):
        print("Kitaplar sorgulanıyor ....")
        time.sleep(3)
        kutuphane.Kitap_Göster()


    elif (islem == "2"):
        isim = input("Sorgulamak istediğiniz Kitabi Belirtiniz : ")
        print("Sorgu Yapılıyor....")
        time.sleep(3)
        kutuphane.Kitap_Sorgula(isim)


    elif (islem == "3"):
        isim = input("Kitap adı : ")
        yazar = input("Yazarı : ")
        yayinevi = input("Yayınevi : ")
        tür = input("Kitap Türü : ")
        baski = input("Baski sayisi : ")

        kitap = Kitap(isim ,yazar ,yayinevi ,tür ,baski)
        kutuphane.Kitap_Ekle(kitap)
        

    elif (islem == "4"):
        isim = input("Silmek istediğiniz kitap ismini Belirtiniz : ")
        kutuphane.Kitap_Sil(isim)

    elif (islem == "5"):
        isim = input("Baskı sayısını yükseltmek istediğiniz kitap nedir :")
        kutuphane.Baski_Yukselt(isim)

    elif (islem == "6"):
        kutuphane.Son_Kitabi_Yazdir()

    else:
        print("Geçersiz Bir seçimde Bulundunuz ")