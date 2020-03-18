# -*- coding: utf-8 -*-
sehirler = ["FETHİYE" ,"İSTANBUL" ,"KONYA" ,"ORDU" ,"RİZE" ,"TRABZON" ,"MANISA", "KONYA"]
print(sehirler)

sehirler.append("ERZİNCAN")
print(sehirler)

sehirler.insert(2,"ANKARA")
print(sehirler)

print("Silinen eleman = " + sehirler.pop(0))

print ("KONYA kelimesi sıralı dizi de " + str(sehirler.count("KONYA")) + " defa geçiyor " )

sehirler.sort()
print ("Metinlerin sıralanmış hali = " + str(sehirler))

sehirler.reverse()
print ("Metinlerin tersine sıralanmış hali = " + str(sehirler))

print (sehirler.index("KONYA")) #ilk yakaladığı konyadeğerinin index'ini  dondurur 
sehirler_3 = sehirler.copy()
sehirler_2 = sehirler #diziler referans tipindedir bellekte tutulur bundan dolayı değişiklikte her ikiside değişir 

print (sehirler)
print (sehirler_2)
sehirler_2 [0] = "İZMİR"
sehirler_3 [0] = "KASTAMONU"

print ("Sehirler 1 = " + str(sehirler))
print ("Sehirler 2 = " + str(sehirler_2))
print ("Sehirler 3 = " + str(sehirler_3))