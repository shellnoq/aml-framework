import requests
import jwt
import json

# JWT token oluşturma fonksiyonu
# Bu, veriyi güvenli bir şekilde göndermek için kimlik doğrulama sağlar.
def generate_token():
    payload = {"user": "input_layer", "role": "collector"}
    secret = "your_secret_key"  # Güvenlik için güçlü bir gizli anahtar kullanın
    return jwt.encode(payload, secret, algorithm="HS256")

# Blockchain API'den veri toplama fonksiyonu
def collect_transactions(api_url):
    headers = {"Authorization": f"Bearer {generate_token()}"}
    response = requests.get(api_url, headers=headers)
    # JSON formatında dönen veriyi kontrol et ve döndür
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from API")

# Hive'a veri gönderme fonksiyonu
# Bu fonksiyon, toplanan veriyi Hive tablosuna gönderir.
def send_to_hive(data):
    headers = {"Authorization": f"Bearer {generate_token()}"}
    response = requests.post("https://localhost:5001/hive", json=data, headers=headers)
    if response.status_code == 200:
        print("Data successfully sent to Hive")
    else:
        raise Exception("Failed to send data to Hive")

if __name__ == "__main__":
    # Blockchain API URL'si
    api_url = "https://api.blockchain.com/v3/transactions"
    # Veri toplama
    transactions = collect_transactions(api_url)
    # Hive'a gönderme
    send_to_hive(transactions)
