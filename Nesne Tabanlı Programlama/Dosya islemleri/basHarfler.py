
"""
Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve
 bu string'i ekrana yazdırın."""

"""class MetinIslemleri():

    def __init__(self):

        with open("şiir.txt" ,"r" , encoding = "utf-8") as file:
            
            siir = file.rad()
            satir = siir.split("\n")

            uzunluk = len(satir)
            self.birlesim = list()
            for i in satir:
               birlesim = i[0]

            print("birlesim")"""


with open("şiir.txt" ,"r" , encoding = "utf-8") as file:
            
            siir = file.read()
            satir = siir.split("\n")

            uzunluk = len(satir)
            birlesim = list()
            for i in satir:
               birlesim.append(i[0])

            print(birlesim)

            for i in birlesim:
                print(i ,end="")

