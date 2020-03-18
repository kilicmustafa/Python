"""Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun.
 Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com

                           //
                           //
                           //


İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz."""

with open ("mailler.txt" ,"r" ,encoding="utf-8") as file:
    
    mail = list()
    mailler = file.read()
    mail = mailler.split("\n")

    for i in mail:
        if (i.endswith(".com")) and (i.find("@") > 0):
            print(i)

        