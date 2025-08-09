import requests
import json


url = "https://randomuser.me/api/?results=10&gender=female"
response = requests.get(url)
data = response.json()


female_users = []
for user in data['results']:
    info = {
        "full_name": f"{user['name']['first']} {user['name']['last']}",
        "email": user['email'],
        "phone": user['phone'],
        "country": user['location']['country']
    }
    female_users.append(info)


with open("females.json", "w", encoding="utf-8") as f:
    json.dump(female_users, f, indent=2)