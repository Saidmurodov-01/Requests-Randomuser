import requests
import json

response = requests.get("https://randomuser.me/api/")
data = response.json()

user = data['results'][0]
user_info = {
    "first_name": user['name']['first'],
    "last_name": user['name']['last'],
    "gender": user['gender'],
    "email": user['email'],
    "phone": user['phone'],
    "address": {
        "street": user['location']['street']['name'],
        "city": user['location']['city'],
        "country": user['location']['country']
    }
}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user_info, f, indent=2)