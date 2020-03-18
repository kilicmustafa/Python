def asalBulma(sayi):
    
    if ( sayi <= 1):
        return False
    
    else:
        for i in range(2,sayi):
            if (sayi % i == 0):
                return False
    return True

print(asalBulma(5)) 


while True:
    sayi = input("Bir sayi girin(çıkış için q' basın) :")
    if (sayi == "q"):
        print("Programdan çıkılıyor....")
        break
    else:
        sayi = int(sayi)
        if asalBulma(sayi):
            print(sayi,"bir asal sayıdır")
        else:
            print(sayi,"bir asal sayı değildir")# -*- coding: utf-8 -*-

