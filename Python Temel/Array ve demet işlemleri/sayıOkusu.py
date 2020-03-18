def sayiSeslendirme(sayi):
    sayi = int(sayi)
    birlerBasamagı = sayi % 10
    onlarBasamagı = sayi // 10
    onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
    birler = ["", "Bir" ,"İki" ,"Üç" ,"Dört" ,"Beş" ,"Altı" ,"Yedi" ,"Sekiz" ,"Dokuz"]
    return onlar[onlarBasamagı] + birler[birlerBasamagı]

sayi = input("Bir sayı giriniz : ")
print("Sayının Okunuşu : ", sayiSeslendirme(sayi))
