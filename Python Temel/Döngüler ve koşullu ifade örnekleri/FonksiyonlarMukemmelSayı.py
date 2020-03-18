# -*- coding: utf-8 -*-

#"""1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını 
#dönen bir tane fonksiyon yazın.

#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)."""

#def mukemmelSayi():
#    muskemmeller= list()
#    bolen = 0
#    for i in range(1,1000):
#        for j in range(1,i):
#            if (i % j == 0):
#                bolen += j
#        if (bolen == i ):
#            muskemmeller.append(i)
#    return muskemmeller
#            
#print(mukemmelSayi())


#def MukemmelBulma():
#    
#    mukemmelSayilar = []
#    bolenler = []
#    for i in range (1,1000):
#        for j in range(i):
#            if (i % j == 0):
#                bolenler.append(i)
#        toplam = 0
#        for k in len(bolenler):
#            toplam += i
#        if (toplam == i):
#            mukemmelSayilar.append(i)
#        bolenler.clear
#    return mukemmelSayilar
#
#print(MukemmelBulma())



def MukemmelBulma(sayi):
    toplam = 0
    for i in range(1,sayi):
        if (sayi % i == 0 ):
            toplam += i
    return toplam == sayi



for i in range(1,1001):
    if (MukemmelBulma(i)):
        print(i,"bir mukemmel sayıdır")
    