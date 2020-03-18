###Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın
##
##def ebobBulma(sayi_1 ,sayi_2):
##    bolenler_1 = list()
##    bolenler_2 = list()
##    
##    for i in range(1,sayi_1+1):
##        i
#        
#def ebob_bulma(sayı1,sayı2):
#    
#    i = 1
#    ebob = 1
#    while (i <= sayı1 and i <= sayı2 ):
#        print("ebob = ",ebob)
#        print("i :" ,i)
#        if ( not (sayı1 % i) and not (sayı2 % i)):
#            ebob = i
#        i += 1
#    return ebob
#sayı1 = int(input("Sayı-1:"))
#sayı2 = int(input("Sayı-2:"))
#
#print("Ebob:",ebob_bulma(sayı1,sayı2))
#
#def ebob_bulma(sayı1,sayı2):
#    
#    i = 1
#    ebob = 1
#    while (i <= sayı1 and i <= sayı2 ):
#        print("ebob = ",ebob)
#        print("i :" ,i)
#        if ( (sayı1 % i == 0 ) and (sayı2 % i == 0)):
#            ebob = i
#        i += 1
#    return ebob
#sayı1 = int(input("Sayı-1:"))
#sayı2 = int(input("Sayı-2:"))

#print("Ebob:",ebob_bulma(sayı1,sayı2))

def ebobBulma(sayi1,sayi2):
    ebob = 1
    if sayi1 > sayi2 :
        for i in range(1,sayi2+1):
            if (sayi1 % i == 0) and (sayi2 % i == 0) : 
                ebob = i
    else:
        for i in range(1,sayi1+1):
            if (sayi1 % i == 0) and (sayi2 % i == 0):
                ebob = i
                
    return ebob


sayi1 = int(input("Birinci sayi : "))
sayi2 = int(input("İkinci sayi : "))

print("Ebobu : ",ebobBulma(sayi1,sayi2))



def ebebBulma2(sayi1,sayi2):
    ebob = 1 
    i = 1 
    while i <= sayi1 and i <= sayi2 : 
        if (not (sayi1 % i ) and not (sayi2 % i )):
            ebob = i
        i += 1
    return  ebob

    
    
    