#%%
import json
date = '{"pencil":"kalem" ,"desk":"masa" ,"book":"kitap"}'

y = json.loads(date)
print(y)

sozluk = {"FirstName":"Mustafa" ,
          "LastName" :"Kılıç",
          "Age":"18"
          }

jsonSozluk = json.dumps(sozluk)


print(jsonSozluk["FirstName"])

#%%

import json

with open("users.json") as users:
    data = json.load(users)

    for i in range(5):
        print(date[i]["address"]["street"]) 
        print(date[i]["name"])