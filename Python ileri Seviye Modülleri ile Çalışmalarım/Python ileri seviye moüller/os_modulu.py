import os
from datetime import datetime
os.chdir("C:/Users/Mustafa/Desktop/")

print(os.getcwd())

print(os.stat("Yeni Metin Belgesi.txt").st_mtime)

degisme_zamanı = datetime.fromtimestamp(os.stat("Yeni Metin Belgesi.txt").st_mtime)

print(degisme_zamanı)