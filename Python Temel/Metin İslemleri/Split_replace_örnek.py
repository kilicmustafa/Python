#SUBstring

mesaj = "MERHABA DÜNYA"
mesaj_2 = mesaj[:5]

print(mesaj_2)

mesaj_3 = mesaj[1:8]

print(mesaj_3)

mesaj_4 = mesaj[3:]

print(mesaj_4)

#LEN uzunluk

metin = "UZUNLUNLUK LEN"

metin_sonkarakter = metin[len(metin)-1:len(metin)]

print(metin_sonkarakter)

#LOWER VE UPPER CASE

text = " Ali İLE veli El ele " 

buyukharf = text.upper()
kucukharf = text.lower()

print(buyukharf)

#Stringler üzerinde Replace

mesaj = "Dönüşecek metin " 
yenimesaj = mesaj.replace("ö","o")
yenimesaj_2 = yenimesaj.replace("ü","u")
yenimesaj_3 = yenimesaj_2.replace("i","ı")
yenimesaj_4 = yenimesaj_3.replace("ş","s")

print(yenimesaj)
print(yenimesaj_2)
print(yenimesaj_3)
print(yenimesaj_4)


#Split ve Strip ile kelime ayırma ve kelime seçip alma

kelimeler = "KEREM KURNAZ 5425881227 İSTABUL"

kelime_1 = kelimeler.split()
print(kelime_1)

kelime_2 = kelimeler.split()[2] # kelimeler dizisini boşluklara göre splitle ve 2.indisini al
print (kelime_2)

kelimeler_2 = "Furkan;Sağ;Evli;28;".strip(";")
kelime_4 = kelimeler_2.split(";")
print (kelime_4)

kelime_5 = kelimeler_2.split(";")[2]
print (kelime_5)


