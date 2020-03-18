def ekok_bulma(sayı1,sayı2):
    
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i


        elif (sayı1 % i ==  0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i


        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    return ekok

sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:",ekok_bulma(sayı1,sayı2))




def ekokBulma(sayi1,sayi2):
    ekok = 1
    i = 2 
    while True:
        if (sayi1 % i == 0 and sayi2 % i == 0):
            ekok = ekok * i
