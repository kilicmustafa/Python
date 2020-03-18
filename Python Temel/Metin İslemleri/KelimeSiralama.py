# -*- coding: utf-8 -*-

cumle = input("Cümle girin = ")
kelimeler = cumle.split(" ")
kelimeler.sort()
print(kelimeler)
for kelime in kelimeler:
    print(kelime)
    
