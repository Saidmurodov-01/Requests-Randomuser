import requests
import os


url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
data = response.json()


os.makedirs("images", exist_ok=True)


for i, user in enumerate(data['results'], start=1):
    image_url = user['picture']['large']
    image_response = requests.get(image_url)
    
    
    file_path = f"images/user{i}.jpg"
    
    with open(file_path, "wb") as f:
        f.write(image_response.content)

print("✅ 10 ta foydalanuvchi rasmi 'images/' papkaga saqlandi.")