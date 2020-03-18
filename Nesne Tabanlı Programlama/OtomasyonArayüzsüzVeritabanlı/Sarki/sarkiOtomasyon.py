from Sarki import *

print("""
***************************************
1-Sarkilari Görüntüle
2-Sarki ekle 
3-Sarki sil
4-Sarki ara(parça ismi ile)
5-Son eklene sarki 
6-Sarkilarin toplam süresi
q-Çıkış
***************************************
""")

görev = islemler()


while True:

    islem = input("Ne Yapmak istiyorsunuz : ")

    if (islem == "q"):
        print("Çıkış yapılıyor ....")
        t.sleep(2)
        print("Çıkış Başarılı")
        break

    elif (islem == "1"):
        print("Şarki listesi taranıyor.....")
        t.sleep(2)
        görev.sarki_goruntule()

    elif (islem == "2"):
        isim = input("Parça Adi : ")
        sanatci = input("Sanatcı : ")
        album =  input("Album : ")
        produksiyon = input("Prodüksiyon : ")
        sure = input("Süre :")

        sarki = Sarki(isim ,sanatci ,album ,produksiyon ,sure)
        print("Sarki ekleniyor.......")
        t.sleep(2)
        görev.sarki_ekle(sarki)
        print("SArki listenize eklendi")

    elif (islem == "3"):
        isim = input("Silmek istediğiniz sarki ismini giriniz : ")

        görev.sarki_sil(isim)

    elif (islem == "4"):

        isim = input("Aranacak sarki : ")
        görev.sarki_bul(isim)

    elif (islem == "5"):

        görev.son_sarki()


    elif (islem == "6"):

        print(görev.sarki_toplam_süre())

    else:
        print("geçersiz işlem")