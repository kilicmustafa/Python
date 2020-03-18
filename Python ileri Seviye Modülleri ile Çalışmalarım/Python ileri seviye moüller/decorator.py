import time

def zaman_hesapla(func):
    def wrappers(sayilar):

        baslama = time.time()
        
        liste = func(sayilar)

        bitis = time.time()


        print(func.__name__ + " " + str(bitis-baslama) + " saniye sürdü")
        return liste

    return wrappers

@zaman_hesapla
def kareleri_hesapla(sayilar):

    liste = list()

    for i in sayilar:

        liste.append(i**2)

    return liste

@zaman_hesapla
def kupleri_hesapla(sayilar):

    liste = list()

    for i in sayilar:

        liste.append(i**3)


    return liste





print(kareleri_hesapla(range(10000)))