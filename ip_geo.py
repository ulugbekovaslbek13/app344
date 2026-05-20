# pip install requests
import requests

ip = input("📍 Tekshirmoqchi bo'lgan IP manzilni kiriting: ")
try:
    res = requests.get(f"http://ip-api.com/json/{ip}").json()
    print(f"🇺🇿 Davlat: {res.get('country')}")
    print(f"🏙️ Shahar: {res.get('city')}")
    print(f"📡 Provayder: {res.get('isp')}")
except Exception:
    print("❌ Ma'lumot topilmadi.")