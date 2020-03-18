def ekstra(func):

    def wrapper(sayilar):

        tek_toplam = 0
        cift_toplam = 0
        tek_sayi = 0
        cift_sayi = 0

    
        for i in sayilar:

            if (i % 2 == 0):
                cift_sayi  += 1
                cift_toplam += i

            else :

                tek_sayi += 1
                tek_toplam += i


        print("çift sayıların ortalaması : " , (cift_toplam / cift_sayi))

        print("tek sayıların ortalaması : " , (tek_toplam / tek_sayi)) 

        func(sayilar)
    return wrapper

        





@ekstra
def ortalama_hesapla(sayilar):

    toplam = 0 

    for i in sayilar:

        toplam += i

    toplam = toplam / len(sayilar)

    print("sayıların ortalaması : ", (toplam))
    


print(ortalama_hesapla([1,2,3,54,4,32,3,11,23,4,75,76,8,75]))
