import requests
import json


url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
data = response.json()


young_users = []
for user in data['results']:
    birth_year = int(user['dob']['date'][:4])
    if birth_year > 1990:
        young_users.append({
            "full_name": f"{user['name']['first']} {user['name']['last']}",
            "email": user['email'],
            "birth_date": user['dob']['date']
        })


with open("young_users.json", "w", encoding="utf-8") as f:
    json.dump(young_users, f, indent=4)

print(f"✅ {len(young_users)} ta foydalanuvchi 'young_users.json' faylga yozildi.")