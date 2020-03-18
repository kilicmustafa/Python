# -*- coding: utf-8 -*-
def topla(liste):
    if (len(liste)) == 0:
        return 0
    else:
        return liste[0] + (topla(liste[1:]))

print(topla([1,3,5,6,9]))


def carp(liste):
    if (len(liste())) == 0:
        return 0
    else:
        return liste[0] * (carp(liste[1:]))