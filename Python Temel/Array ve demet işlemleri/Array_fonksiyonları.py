# -*- coding: utf-8 -*-
#String metin srıalı dizilerinde düzenlemeler Append ,remove insert vb

#ogrenci_1 = "ALİ"
#ogrenci_2 = "VELİ"
#ogrenci_3 = "SALİH"
#ogrenci_4 = "KERİM"
    
# teker teker yazmak yerine sıralı diziye alınır

ogrenciler = ["ALİ" ,"VELİ " ,"SALİH" ,"KERİM"]

print(ogrenciler)

ogrenci_1 = ogrenciler[0]
print(ogrenci_1)

ogrenciler.append("SALİM") #yeni kayıt ekler
print(ogrenciler)

ogrenciler[0] = "SELİM" #değişir
ogrenci_1 = ogrenciler[0]
print(ogrenciler)

ogrenciler.remove("KERİM") #siler
print(ogrenciler)

ogrenciler.insert(1,"FATİH") #arasına ekler
print(ogrenciler)

ogrenciler_2 = ["BENSU" ,"BANU" ,"PELİNSU" ,"SEVGİ"]
print (ogrenciler_2)

ogrenciler.extend(ogrenciler_2)
print(ogrenciler)

ogrenciler_3 = ["EMİN" , "BENİ" ,"PERİ"]
ogrenciler_birlesim = ogrenciler + ogrenciler_2 +ogrenciler_3
print(ogrenciler_birlesim)
print("3.ogrenci listesinin uzuuğu = " + str(len(ogrenciler_3)))
print(ogrenciler_3.pop(0))
print("3. ogrenci listesinin uzunlugu = " + str(len(ogrenciler_3)))
