"""Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek ,
 ekrana isim ve soyisimleri isimlere göre sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"] """


isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

birlesim = list(zip(isim,soyisim))

print(birlesim)
for i,j in birlesim:
    print(i," ",j)