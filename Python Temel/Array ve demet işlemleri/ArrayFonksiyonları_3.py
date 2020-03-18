#info = "404 not font"
#
#print (info[2:7])
#print (info[2:])
#print (info[2:])
#
#liste = list("Bir hata ile karşılaşıldı "+'listelere + ile ekleme yapılır ')
#print(liste)
#
#liste.append("windows dururuluyor ")
#print (liste)
#
#liste_2 = ["Bir hata "]
#print (liste_2)
#
#liste_2.append("Mesajı")
#print (liste_2)
#
#

# Tuple ile çalışmak ve tuple ile string dizisi arasındaki farklar

Liste = ["ÇAY" ,"LİMAONATA" ,("ORALET" ,"VİŞNE SUYU"), "SÜTLÜ KAHVE"]
TupleList = ("LOKUM" ,["CEVİZ" ,"BÜSKÜVİT"] ,"KEK")

Liste.insert(2,"SU")
#TupleListe.insert(2,"FISTIK") tuple read içindir write işelemine izin vermez

print ("Liste'nin veri tipi = " + str(type(Liste)))
print ("TupleListe 'nin veri tipi = " + str(type(TupleList)))

TupleList_2 = ("tek") #tek elemanlı diziyi python tuple olarak algılamaz 
print ("TupleList_2 'nin veri tipi = " + str(type(TupleList_2)))
#bunu çözmek için tek elemanlı turplelerin sonuna virgül atarız

TupleList_3 = ("çift",)
print ("TupleList_3 'ün veri tipi = " + str(type(TupleList_3)))

#elemanlarına erişme

print (Liste[-2])
print (TupleList[-2])

print (Liste[1:2])
print (TupleList[1][0]) #ekran cıktısının sonuna , işareti vermesinin sebebi onun tuple oldugunu belirmektir


#uzunlukları 

print ("Liste'nin uzunlugu = " + str(len(Liste)))
print ("TupleLis'in uzunlugu = " + str(len(TupleList)))

print("--------------------------------------------------------------------------")

# Setler ile çalışma 

mySet = {"Python" ,"Java" ,"C++" ,"C#"}
print (mySet)

for i in mySet:
    print(i)
    
if "Python" in mySet:
    print("mySet'in içinde Python geçiyor")
    
mySet.pop() #Setlerin indexi olmadığı için raskele bir değer siler
print(mySet)

mySet.clear()
print(mySet)
#mySet_2 = set(("Mobil" ,"Masaüstü"))
#
#mySet.add("JavaScript")
#print (mySet)
#
#mySet_2.update(["PC","Tablet"]) #dahil parantezi koymaz isek giridiğimiz değerleri karakterlerine ayrıştırır 
#print (mySet_2)
#del(mySet_2) #seti sildi
#
#
#
#mySet.discard("Java") #siler ancak silinecek öge yok ise hata vermez
#print (mySet)
#mySet.remove("C++") # siler ancak bulamaz ise uyarı verir 
#print (mySet)

print("----------------------------------------")
#




