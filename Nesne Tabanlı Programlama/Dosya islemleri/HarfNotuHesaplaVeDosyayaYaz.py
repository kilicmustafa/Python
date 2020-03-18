def not_hesapla(satır):
    

    satır = satır[:-1]

    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):

        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + " ------------------> " + harf + "\n"







with open("dosya.txt","r",encoding= "utf-8") as file:

    eklenecekler_listesi = []
    kalanlar = []
    gecenler = []
    for i in file:

        ayır = not_hesapla(i)
        ayır2 = ayır[:-1]
        hesap = ayır2.split(" ")
        
        print(hesap[3])
        if (hesap[3] == "FF"):
            kalanlar.append(ayır)
        else:
            gecenler.append(ayır)
    with open("notlar.txt","w",encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)
    with open("Geçenler.txt" ,"w" ,encoding = "utf-8") as file3 :
        for i in gecenler:
            file3.write(i)

    with open("kalanlar.txt" ,"w" ,encoding = "utf-8") as file4 :
        file4.writelines(kalanlar)



