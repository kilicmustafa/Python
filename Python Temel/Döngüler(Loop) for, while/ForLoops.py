## -*- coding: utf-8 -*-
# #%%
#sehirler = ["Ankara" ,"İstanbul" ,"İzmir" ,"Yozgat"]
#
#for sehir in sehirler :
#    print(sehir + " sehrinin ilk 3 karakteri = " + sehir[:3])
#
#toplam = 0
#for i in range(1,10):
#    toplam = toplam + i
#    print(i)
#print(toplam)
#a=1
#while a <= 5 :
#    print(a)
#    a = a + 1
#    
# #%%  blocklara boler    yıldız yapma
# n = int(input("Kaç yıldız giriceksiniz = "))
# yildiz = "*"
# 
# for i in range(0,n):
#     print(yildiz)
#     yildiz = yildiz + "*"
#     
# 
# 
# #%% asal sayı bulma 
# sayi = int(input("Bir sayı giriniz = "))
#
# for i in range(2,sayi):
#     if (sayi % i)  == 0 :
#         print("Bu sayı asal değildir")
#         break
#     elif(sayi % i) != 0:
#         print("Bu sayı asal değildir")
#         break
 #%% asal sayı bulma kısayol

sayi = int(input("Bir sayi giriniz = "))
asalMi = True

for i in range(2,sayi):
    if (sayi % i) == 0:
        asalMi = False
        break
if asalMi == True : # if asalMi: ile aynı göreve gelir default'u true dir
    print("Asaldır")
else :
    print("Asal değildir")
         
    
    
         