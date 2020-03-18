# -*- coding: utf-8 -*-
#normal fonksiyon 
def dikUcgenAlani(a,b):
    return a*b / 2
print(type(dikUcgenAlani(2,5)))
print(dikUcgenAlani(2,15))

#%% lambda ile değer döndüren argumantlı fonksiyon(metot)
#olay tek satırda biter 
dikUcgenAlani_2 = lambda a,b : a*b/2
print(type(dikUcgenAlani_2))
print(dikUcgenAlani_2(2,15))

x = dikUcgenAlani_2

print(x(4,5))
#fonksiyon başka bir değişkene atanabilir 
dikdorgenAlan = lambda a,b : a*2+b*2
x = dikdorgenAlan
print(x(10,20))


