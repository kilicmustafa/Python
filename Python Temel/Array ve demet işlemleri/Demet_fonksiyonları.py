## -*- coding: utf-8 -*-
sozluk = {"Kitap" : "Book",
          "Kalem" : "Pencil"}
sozluk_2 = dict(Anahtar = "Key",
                Bilgisayar ="Computer"
                )
print(sozluk["Kitap"])
sozluk["Su"] = "water" # yeni kayıt ekleyip değiştirir
print(sozluk["Su"])
del(sozluk["Kitap"]) # içinden kayıt siler
print(sozluk)

karar yapıları if
