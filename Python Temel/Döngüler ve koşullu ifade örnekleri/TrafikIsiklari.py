# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:32:35 2019

@author: ASUS
"""
lights = ["1 - red" ," 2 - yellew"," 3 - green"]
print(lights)
n = input("Select = ")
if int(n == "1") :
    currentLight = lights[0]
    print("Stop!")
elif n == "2":
    currentLight = lights[1]
    print("Ready")
else :
    print("Goo")
    currentLight = lights[2]


print(currentLight)

