from flask import Flask, request, jsonify
from pyhive import hive

app = Flask(__name__)

# Hive bağlantısı
def connect_to_hive():
    return hive.Connection(
        host='localhost',
        port=10000,
        username='hive',
        database='default'
    )

# Veri ekleme
@app.route('/hive', methods=['POST'])
def insert_data():
    data = request.json
    conn = connect_to_hive()
    cursor = conn.cursor()

    for tx in data:
        cursor.execute(f"""
            INSERT INTO transactions (transaction_id, transaction_type, amount, timestamp)
            VALUES ('{tx["transaction_id"]}', '{tx["transaction_type"]}', {tx["amount"]}, '{tx["timestamp"]}')
        """)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'), port=5001)
