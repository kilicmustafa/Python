"""
with open("Futboolcular.txt" ,"w" ,encoding = "utf-8") as file:
    file.write("Selcuk inan,Feguli,Fernando Muslera,Galatasaray\n")
    file.write("Rayn Babel,Atiba Hutchinson,Beşiktaş\n")
    file.write("Simon Kjaer,Musa sow,Fenerbahçe\n")
    
"""
def takımaAta(takim):
    takim = takim[:-1]
    yeniTakim = takim.split(",")
    
    return yeniTakim

with open("Futbolcular.txt" ,"r" ,encoding = "utf-8") as file :

    for i in file:
        yeniTakim = takımaAta(i)
        a = len(yeniTakim)
        with open( yeniTakim[a-1], "w" ,encoding = "utf-8") as file2 :
            yeniTakim = yeniTakim[:-1]
            #file2.writelines(yeniTakim)
            for j in yeniTakim:
                file2.write(j+"\n")        
   

    