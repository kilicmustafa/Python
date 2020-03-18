# -*- coding: utf-8 -*-
liste = [1,2,3,4,5]
liste_2 =[3,5,8,9,0]
newliste =[0,0,0,0,0]
#def matrisToplama(a,b):
#    yeniListe[i] = lisliste[i]+ liste_2[i]
#    return yeniListe
#for i in range(0,len(liste())):
#    matrisToplama(liste[i],liste_2[i])
#print("yeni liste")

def matrixToplama(a,b,c):
    
    for i in range(0,len(a)):
        c[i] = a[i] + b[i]
    return c

print(matrixToplama(liste,liste_2))

#%% 
x = [[1,5,3] ,[5,4,6] ,[8,4,9]]
y = [[2,3,5] ,[1,5,8] ,[5,8,9]]
z = [[0,0,0] ,[0,0,0] ,[0,0,0]]

for i in range(0,len(z)):
    for j in range(0,len(z[0])):
        z[i][j] = x[i][j] + y[i][j]
print(z)
        
        
            