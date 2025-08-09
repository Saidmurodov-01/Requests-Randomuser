import requests
import json


url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
data = response.json()


users = []
for user in data['results']:
    users.append({
        "full_name": f"{user['name']['first']} {user['name']['last']}",
        "email": user['email'],
        "image": user['picture']['large']
    })


with open("users_with_images.json", "w", encoding="utf-8") as f:
    json.dump(users, f, indent=4)

print("✅ 10 ta foydalanuvchi 'users_with_images.json' faylga yozildi.")