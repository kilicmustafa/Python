import os 
from datetime import datetime
os.chdir("C:/Users/Mustafa/Desktop")


print(os.getcwd())

degisme_zamanı = os.stat("text.txt").st_mtime

print(datetime.fromtimestamp(degisme_zamanı))
