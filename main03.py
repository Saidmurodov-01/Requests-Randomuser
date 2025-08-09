import requests
import json


url = "https://randomuser.me/api/?results=10&gender=male"
response = requests.get(url)
data = response.json()


male_users = []
for user in data['results']:
    info = {
        "full_name": f"{user['name']['first']} {user['name']['last']}",
        "email": user['email'],
        "phone": user['phone'],
        "country": user['location']['country']
    }
    male_users.append(info)


with open("males.json", "w", encoding="utf-8") as f:
    json.dump(male_users, f, indent=2)