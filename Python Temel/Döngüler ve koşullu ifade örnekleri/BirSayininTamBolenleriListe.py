def tamBolen(sayi):
    tamBolenler = list()
    for i in range(sayi,1,-1):
        if (sayi % i == 0):
            tamBolenler.append(i)
    for i in tamBolenler:
        print(i)


while True :
    sayi = input("Bir sayı girin (Cıkmak için q 'a basın) : ")
    if (sayi == "q"):
        print("Programdan cıkılıyor...")
        break
    else:
        sayi = int(sayi)
        tamBolen(sayi)
        
    