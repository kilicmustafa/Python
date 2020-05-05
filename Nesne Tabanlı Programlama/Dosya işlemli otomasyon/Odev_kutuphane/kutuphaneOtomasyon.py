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

        
        try:
            self.file = open("kutuphane_db.txt","r+", encoding="utf-8" )
        except FileNotFoundError:
            self.file = open("kutuphane_db.txt","w", encoding="utf-8" )
            self.file.close()
            
            self.file = open("muzik_df.txt","r+", encoding="utf-8" )


    
    
    def Baglantı_kapat(self):
        self.file.close()

    def Kitap_Ekle(self,kitap):

        dk = {
        "isim" : kitap.isim.strip(), # sagındaki ve solundaki boşlukları siliyoruz 
        "yazar" : kitap.yazar.strip(),
        "yayinevi" : kitap.yayinevi.strip(),
        "kitap_t" : kitap.tür.strip(),
        "kitap_b" : kitap.baski.strip(),

        }
        
        
        kitap_ozelliklleri = dk["isim"] + ";" + dk["yazar"]  + ";" + dk["yayinevi"] + ";" + dk["kitap_t"] + ";" + dk["kitap_b"] +"\n"
        
        self.file.write(kitap_ozelliklleri)
        print("işlem başarılı")
        

    
    def Kitap_Göster(self ):
        self.file.seek(0)
        kitaplar = self.file.readlines()

        
        if (len(kitaplar) == 0):
            print("Kitap bulunamadı")
        else:

            for i in kitaplar:
                i.strip("\n")
                i = i.split(";")
                kitap = Kitap(i[0] ,i[1] ,i[2] ,i[3] ,i[4])
                print(kitap)


    def Kitap_Sorgula(self ,isim):
        self.file.seek(0)
        kitaplar = self.file.readlines()
        var = 0
        if (len(kitaplar) == 0):
            print("Kütüphanenizde kitap yok")
        else:

            for i in kitaplar:
                i.strip("\n")
                i = i.split(";")

                if i[0] == isim: 
                    var = 1
                    print("Kitap Başarılı bir şekilde bulundu")
                    kitap = Kitap(i[0] ,i[1] ,i[2] ,i[3] ,i[4])
                    print(kitap) 
                    break

            if var != 1:
                print("Aradıgınız isimde kitap bulunamadı")
            
                

    def Kitap_Sil(self ,isim):
        self.file.seek(0)
        kitaplar = self.file.readlines()
        var = 0
        if (len(kitaplar) == 0):
            print("Kütüphanenizde kitap yok")
        else:

            for i in kitaplar:
                i.strip("\n")
                i = i.split(";")

                if i[0] == isim: 
                    var = 1
                    print("Kitap Başarılı bir şekilde bulundu")
                    silinecek_kitap = i[0]
                    pass

            if var == 1:

                print("Kitap siliniyor.......")
                time.sleep(2)

                yeni_icerik = list()

                for i in kitaplar:
                    i.strip("\n")
                    a = i.split(";")
                    if a[0] == silinecek_kitap:
                        pass
                    else:
                        yeni_icerik.append(i)
                
                

                self.file = open("kutuphane_db.txt" ,"w" ,encoding="utf-8")

                for i in yeni_icerik:
                    self.file.write(i)
                self.file.close() # dosyayı w kipitde açtığımız için kapatıyoruz 
                print("Kitap silme başarılı")

                self.Baglanti_ac() # tekrardan dosya bağlantımızı yapıyoruz

            else:
                print("Böyle bir kitap bulunamadı")

        
    def Baski_Yukselt(self,isim):
        self.file.seek(0)
        kitaplar = self.file.readlines()
        var = 0
        if (len(kitaplar) == 0):
            print("Kütüphanenizde kitap yok")
        else:

            for i in kitaplar:
                i.strip("\n")
                i = i.split(";")

                if i[0] == isim: 
                    var = 1
                    print("Kitap Başarılı bir şekilde bulundu")
                    bsk_y = i[0]
                    pass

            if var == 1:
                
                time.sleep(2)

                

                def yeni_icerik_uretici(): #iç içe fonksiyonu burda kullandım
                    yeni_icerik = list()

                    for i in kitaplar:
                        i.strip("\n")
                        a = i.split(";")

                        if a[0] == bsk_y: # baskısı yükseltilecek kitap
                            print("Kitabın mevcut baskısı =  " + a[4] )
                            yeni_baski = input("Lütfen yeni baskı sayınızı belirtiniz = ")
                            i = a[0] + ";" + a[1]  + ";" + a[2] + ";" + a[3] + ";" + yeni_baski +"\n"
                            yeni_icerik.append(i)
                            
                            
                            
                        else:
                            yeni_icerik.append(i)
                    
                    return yeni_icerik

                yeni_icerik = yeni_icerik_uretici()
                    
                self.file = open("kutuphane_db.txt" ,"w" ,encoding="utf-8")

                for i in yeni_icerik:
                    self.file.write(i)
                self.file.close() # dosyayı w kipitde açtığımız için kapatıyoruz 
                time.sleep(2)
                print("Baskı yükseltme başarılı")

                self.Baglanti_ac() # tekrardan dosya bağlantımızı yapıyoruz

            else:
                print("Böyle bir kitap bulunamadı")



    def Son_Kitabi_Yazdir(self):
        self.file.seek(0)
        kitaplar = self.file.readlines()
        print("Son Kitap aranıyor")
        time.sleep(2)
        if (len(kitaplar) == 0):
            print("Kütüphanenizde kitap yok")
        else:
            print("Son kitap bulundu \n \n")

            print("***************Son kitap ****************")
            son_kitap = kitaplar[len(kitaplar)-1]

            son_kitap = son_kitap.strip("\n")
            son_kitap = son_kitap.split(";")
            kitap = Kitap(son_kitap[0] ,son_kitap[1] ,son_kitap[2] ,son_kitap[3] ,son_kitap[4])    

            print(kitap)