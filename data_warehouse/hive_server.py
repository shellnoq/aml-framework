from flask import Flask, request, jsonify
from pyhive import hive

app = Flask(__name__)

# Hive bağlantısı kurma fonksiyonu
# Bu fonksiyon, Hive veri tabanına bağlanır.
def connect_to_hive():
    return hive.Connection(host='localhost', port=10000, username='hive', database='default')

# Hive'a veri eklemek için API endpoint
@app.route('/hive', methods=['POST'])
def insert_data():
    data = request.json  # İstekten gelen JSON verisi
    conn = connect_to_hive()
    cursor = conn.cursor()

    # Gelen veriyi işle ve Hive tablosuna ekle
    for tx in data:
        transaction_id = tx["transaction_id"]
        transaction_type = tx["transaction_type"]
        amount = tx["amount"]
        timestamp = tx["timestamp"]
        cursor.execute(f"""
            INSERT INTO transactions (transaction_id, transaction_type, amount, timestamp)
            VALUES ('{transaction_id}', '{transaction_type}', {amount}, '{timestamp}')
        """)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    # Flask uygulamasını HTTPS ile başlat
    app.run(ssl_context=('cert.pem', 'key.pem'), port=5001)
