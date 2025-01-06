from pyhive import hive
import requests

# Hive bağlantısı
def connect_to_hive():
    conn = hive.Connection(
        host='localhost',
        port=10000,
        username='hive',
        database='default'
    )
    return conn

# Veriyi toplama ve Hive'a gönderme
def send_data_to_hive(api_url, hive_table):
    # API'den veri toplama
    response = requests.get(api_url)
    transactions = response.json()

    # Hive bağlantısı
    conn = connect_to_hive()
    cursor = conn.cursor()

    # Veriyi Hive tablosuna ekleme
    for tx in transactions:
        transaction_id = tx['transaction_id']
        transaction_type = tx['transaction_type']
        amount = tx['amount']
        timestamp = tx['timestamp']

        cursor.execute(f"""
            INSERT INTO {hive_table} (transaction_id, transaction_type, amount, timestamp)
            VALUES ('{transaction_id}', '{transaction_type}', {amount}, '{timestamp}')
        """)

    conn.close()
    print(f"Data successfully inserted into {hive_table}.")

if __name__ == "__main__":
    api_url = "https://api.blockchain.com/v3/transactions"
    hive_table = "transactions"
    send_data_to_hive(api_url, hive_table)
