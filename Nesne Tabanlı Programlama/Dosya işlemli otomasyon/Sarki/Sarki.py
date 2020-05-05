""""
Numara =
Ad =
Soyad =

"""





def Sarki(isim ,sanatci ,album ,produksiyon ,sure):


    sarkilar = {
        "isim" : isim,
        "sanatci" : sanatci,
        "album" : album,
        "produksiyon" : produksiyon,
        "sure" : sure}

    return sarkilar

def sarki_yazdir(sarkilar):
    return print(f"""
    **************************************
    Şarkı İsmi : {sarkilar["isim"]}
    Sanatçı : {sarkilar["sanatci"]}
    Albüm : {sarkilar["album"]}
    Prodüksiyon Şirketi : {sarkilar["produksiyon"]}
    Şarkı Süresi : {sarkilar["sure"]}
    **************************************""")



def baglan():
    

    try:
        muzik_dos = open("muzik_df.txt","r+", encoding="utf-8" )
    except FileNotFoundError:
        muzik_dos = open("muzik_df.txt","w", encoding="utf-8" )#dosya bulunup bulunmama durumunu try ,except ile kontrol ediyorum 
        muzik_dos.close()
        muzik_dos = open("muzik_df.txt","r+", encoding="utf-8" )
    return muzik_dos

muzik_dos = baglan()

def baglanti_kes(dosya_adi):
    dosya_adi.close()

def sarkilari_görüntüle():

    muzik_dos.seek(0)

    sarki_listesi = muzik_dos.readlines()
    if len(sarki_listesi) == 0:
        print("Listenizde sarkı bulunamadı...")
    for i in sarki_listesi:
        i.strip("\n")
        i = i.split("^")
        sarki = Sarki(i[0] ,i[1] ,i[2] ,i[3] ,i[4])
        sarki_yazdir(sarki)



def sarki_yükle(sarki):
    sarkilar = sarki
    

    satir = sarkilar["isim"] + "^" + sarkilar["sanatci"] + "^" + sarkilar["album"] + "^" + sarkilar["produksiyon"] + "^" + sarkilar["sure"]  +"\n"
    
    muzik_dos.writelines(satir)


def sanatci_sarkilari_bul(sanatci_ismi):

    muzik_dos.seek(0)
    sarki_listesi = muzik_dos.readlines()
    sarki_sayisi = 0
    print("Sanatçiya ait şarkılar ")
    for i in sarki_listesi:
        
        i.strip("\n")
        i = i.split("^")
        
        if sanatci_ismi == i[1]:
            sarki_sayisi += 1
            sarki = Sarki(i[0] ,i[1] ,i[2] ,i[3] ,i[4])
            sarki_yazdir(sarki)

    if sarki_sayisi > 0 :
        print("Sanatcıya ait toplam " + str(sarki_sayisi) + " adet sarki vardır")
    else:
        print("Sanatcıya ait şarkı bulunamadı")

def sarki_siliver(sarki_ismi):
    muzik_dos = baglan()
    muzik_dos.seek(0)
    sarki_listesi = muzik_dos.readlines()
    sarki_kontrol = 0

    yeni_sarki_listesi = list()
    for i in sarki_listesi:
        a = i
        i.strip("\n")
        i = i.split("^")

        if sanatci_ismi != i[0]:
            yeni_sarki_listesi.append(a)

        else:
            sarki_kontrol = 1


    
    if sarki_kontrol == 1 :
        muzik_dos_2 = open("muzik_df.txt","w", encoding="utf-8" )

        for j in yeni_sarki_listesi:
            muzik_dos.write(j)

        print("Şarkı başarılı şekilde silindi")
        muzik_dos_2.close()

        muzik_dos = baglan()
        
    else:
        print("Sarki silme başarısız")




        


            

        


def sarki_duzenle(sarki_ismi):
    muzik_dos = baglan()
    muzik_dos.seek(0)
    sarki_listesi = muzik_dos.readlines()
    sarki_kontrol = 0

    yeni_sarki_listesi = list()
    for i in sarki_listesi:
        a = i
        i.strip("\n")
        i = i.split("^")

        if sarki_ismi == i[0]:
            
            duzenlenecek_sarki = a 
            sarki_kontrol = 1

        else:
            yeni_sarki_listesi.append(a)


    
    if sarki_kontrol == 1 :
        duzenlenecek_sarki = duzenlenecek_sarki.strip("\n").split("^")

        sarkilar = Sarki(duzenlenecek_sarki[0] ,duzenlenecek_sarki[1] ,duzenlenecek_sarki[2] ,duzenlenecek_sarki[3] ,duzenlenecek_sarki[4])
        print("======================== Sarkının suanki bilğileri ===================")
        sarki_yazdir(sarkilar)



        isim = input("Lütfen yeni şarkı isminizi giriniz ?? ")
        sanatcı = input("Lütfen yeni şarkı sanatcınızı giriniz ?? ")
        album = input("Lütfen yeni şarkı album adını giriniz ?? ")
        produksiyon = input("Lütfen yeni şarkı produksiyon şirketini giriniz ?? ")
        sure = input("Lütfen yeni şarkı uzunlugunu giriniz ??")
        
        

        sarkilar = Sarki(isim ,sanatcı ,album ,produksiyon ,sure)

        düzenlenmis_sarki = sarkilar["isim"] + "^" + sarkilar["sanatci"] + "^" + sarkilar["album"] + "^" + sarkilar["produksiyon"] + "^" + sarkilar["sure"]  +"\n"
        
        yeni_sarki_listesi.append(düzenlenmis_sarki) # yukarıda düzenlenecek sarkıyı yakadım ve özelliklerini değiştirdim ardından tekrar dosyama yazılacak hale getirdim ve ekrana yazdırdım


        muzik_dos_2 = open("muzik_df.txt","w", encoding="utf-8" )
        for j in yeni_sarki_listesi:
            muzik_dos.write(j)

        print("Şarkı başarılı şekilde düzenlendi")
        muzik_dos_2.close()

        print("============== Sarkinin yeni hali ==================")
        sarki_yazdir(sarkilar)
        muzik_dos = baglan()
        
    else:
        print("Boyle bir şarkı yoktur ")

def en_cok_sarkisi_olan():
    muzik_dos.seek(0)
    sarki_listesi = muzik_dos.readlines()

    
    sanatcilar = list()
    sanatci_isimleri = list()
    print("Sanatçiya ait şarkılar ")
    for i in sarki_listesi:
        i.strip("\n")
        i = i.split("^")

        sanatci_isimleri.append(i[1])

    if len(sanatci_isimleri) > 1:

        for i in sanatci_isimleri:
            print(i)
            sutun = [str(i) ,0] # sanatcı adı , kaç tane sarkısı oldugu 

            sanatcilar.append(sutun)



        for f in (0 ,len(sanatcilar) -1):

            for i in (0 ,len(sanatcilar) -1):

                if sanatcilar[f][0] == sanatcilar[i][0] :# eger sanatcıdan bir tane daha varsa bulur
                    sanatcilar[f][1] = int(sanatcilar[f][1])  + 1 # sarkı sayısını artırır

        
        
        for f in range(0 ,len(sanatcilar)-1):

            for i in range(0 ,len(sanatcilar)-1):

                if sanatcilar[f][1] > sanatcilar[i][1] :
                    
                    sanatci_adi = sanatcilar[f][0]

        
        
        sarki_say  = 0
        for i in sarki_listesi:
            i.strip("\n")
            i = i.split("^")

            if str(sanatci_adi) == i[1]:
                sarki = Sarki(i[0] ,i[1] ,i[2] ,i[3] ,i[4])
                sarki_yazdir(sarki)
                sarki_say = sarki_say + 1

        if int(sarki_say) > 1 :
            print("Sanatcıya ait toplam " + str(sarki_say) + " adet sarki vardır")
        else:
            print("Fark yaratan sanatcı bulunamadı")

    else:
        print("Kütüphanenizde karşılaştırma yapacak kadar sanatcı bulunamadı")



don = "e"
while don == "e":

    print("""
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    1-->Sarki Ekle
    2-->Sarki Görüntüle 
    3-->Sarki ara(sanatçı ismi ile)
    4-->Sarki sil
    5-->Sarki düzenle
    6-->En çok sarkısı olan sanatcıyı bul
    exit-->Çıkış(exit yaz)
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    """)


    girdi = input("Lütfen ne yapmak istediğinizi belirtiniz ?? ")

    if girdi == "exit" :
        print("Otomasyon kapatılıyor...")
        print("İyi günler :)")  
        don = "h"   
           

    elif girdi == "1":
        isim = input("Parça Adi : ")
        sanatci = input("Sanatcı : ")
        album =  input("Album : ")
        produksiyon = input("Prodüksiyon : ")
        sure = input("Süre :")

        sarki = Sarki(isim ,sanatci ,album ,produksiyon ,sure)
        print("Sarki ekleniyor.......")

        sarki_yükle(sarki)
        print("Sarki listenize eklendi")


    elif girdi == "2":
        print("Mevcut şarkı listeniz")
        sarkilari_görüntüle()


    elif girdi == "3":

        sanatci_ismi = input("Hangi sanatçının şarkılarını görüntülemek istiyorsunuz ?? ")

        sanatci_sarkilari_bul(sanatci_ismi)


    elif girdi == "4":

        sanatci_ismi = input("Hangi sarkıyı  silmek istiyorsunuz ?? ")

        sarki_siliver(sanatci_ismi)


    elif girdi == "5":

        sarki_ismi = input("Hangi sarkıyı düzenlemek istiyorsunuz ismini belirtiniz   ?? ")

        sarki_duzenle(sarki_ismi)

    elif girdi == "6":
        en_cok_sarkisi_olan()


    else:
        print("Eksik veya hatalı bir tuşlama yaptınız")


