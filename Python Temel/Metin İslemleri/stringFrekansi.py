"""Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

"""

def metinFrekansiBul(metin):
    pass
    

metin = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
sozluk = dict()
for i in metin:
    
    if (i in sozluk):
        sozluk[i] +=1

    else:
        sozluk[i] = 1

for harf ,sayi in sozluk.items():
    
    print("{} : harfi string içinde {} : defa geçiyor".format(harf ,sayi))


