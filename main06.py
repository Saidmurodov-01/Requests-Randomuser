import requests
import csv


url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
data = response.json()


with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    
    
    writer.writerow(["Full Name", "Email", "Phone", "Country"])
    
    
    for user in data['results']:
        full_name = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        phone = user['phone']
        country = user['location']['country']
        
        writer.writerow([full_name, email, phone, country])

print("✅ 10 ta foydalanuvchi 'users.csv' faylga yozildi.")