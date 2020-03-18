import json
with open("users.json") as users:
    date = json.load(users)
    for i in range(5):
        print(date[i]["name"])