islemler = ["1-toplama ","2-Çıkarma","3-Çarpma","4-Bölme","Çıkmak için 'q' tuşuna basınız"]

while True:
    print("Programa Hoşgeldiniz")
    print("*********************")
    for islem in islemler:
        print(islem)
    secenek = input("Ne yapmak istersiniz ? = ")
    if secenek == "q":
        print("Çıkış Yapılıyor")
        break
    elif secenek == "1":
        sayi_1 = int(input("İlk sayi = "))
        sayi_2 = int(input("İkinci sayi = "))
        sonuc = sayi_1 + sayi_2
        print(str(sayi_1) + " + " + str(sayi_2) + " = " + str(sonuc))
        
    elif secenek == "2":
        sayi_1 = int(input("İlk sayi = "))
        sayi_2 = int(input("İkinci sayi = "))
        sonuc = sayi_1 - sayi_2
        print(str(sayi_1) + " - " + str(sayi_2) + " = " + str(sonuc))
        
    elif secenek == "3":
        sayi_1 = int(input("İlk sayi = "))
        sayi_2 = int(input("İkinci sayi = "))
        sonuc = sayi_1 * sayi_2
        print(str(sayi_1) + " * " + str(sayi_2) + " = " + str(sonuc))
        
    elif secenek == "4":
        sayi_1 = int(input("İlk sayi = "))
        sayi_2 = int(input("İkinci sayi = "))
        sonuc = sayi_1 / sayi_2
        print(str(sayi_1) + " / " + str(sayi_2) + " = " + str(sonuc))
    
    else:
        print("Geçersiz işlem yaptınız")