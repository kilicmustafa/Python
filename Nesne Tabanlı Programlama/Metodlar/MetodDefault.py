# -*- coding: utf-8 -*-
def selamVer():
    print("Selamun aleyküm")
selamVer()

def selamVer_2(isim):
    print("Selam " + isim)
selamVer_2("Mustafa")

def selamVer_3(isim = "ziyaretçi"):
    print("Selam "+ isim)
selamVer_3("furkan")
selamVer_3()

def selamVer_4(isim = "Ziyaretci",soyIsim = ""):
    print("Selam " + isim +" "+ soyIsim)
selamVer_4("Kardelen","Gümüş")
#ama üstekinin en mantıklı kullanımı aşşağıdaki gibidir ilk zorunlu değerler 
#başa gelecek şekilde yazılır 

def selamVer_5(isim , soyIsim = "default" ):
    print("Merhaba " + isim + " " + soyIsim)
selamVer_5("MUSTAFA")
selamVer_5("MERT","Küllük")

