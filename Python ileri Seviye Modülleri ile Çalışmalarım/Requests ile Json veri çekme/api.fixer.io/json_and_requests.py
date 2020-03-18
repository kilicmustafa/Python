import requests 

url = "http://api.fixer.io/latest?base="

birinci_doviz = input("Birinci Doviz ? ")
ikinci_doviz = input("ikinci Doviz ?")
miktar = input("Miktar")

response = requests.get(url + birinci_doviz)

jsonVerisi = response.json()

print(jsonVerisi)