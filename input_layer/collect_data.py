from clean_data import DataCleaner
import requests
import jwt

# Generate a JWT token for secure communication
def generate_token():
    """
    Generates a JWT token for secure API access.
    
    :return: JWT token as a string.
    """
    payload = {"user": "input_layer", "role": "collector"}
    secret = "your_secret_key"  # Replace with a strong secret key
    return jwt.encode(payload, secret, algorithm="HS256")

# Collect transaction data from the Blockchain API
def collect_transactions(api_url):
    """
    Fetches raw transaction data from the given API URL.
    
    :param api_url: The URL of the Blockchain API.
    :return: List of transaction data in JSON format.
    """
    headers = {"Authorization": f"Bearer {generate_token()}"}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data from API")

# Send cleaned data to the Hive data warehouse
def send_to_hive(data):
    """
    Sends cleaned transaction data to the Hive data warehouse via a secure API.
    
    :param data: List of cleaned transaction data.
    """
    headers = {"Authorization": f"Bearer {generate_token()}"}
    response = requests.post("https://localhost:5001/hive", json=data, headers=headers)
    if response.status_code == 200:
        print("Data successfully sent to Hive")
    else:
        raise Exception("Failed to send data to Hive")

if __name__ == "__main__":
    # API URL for Blockchain transactions
    api_url = "https://api.blockchain.com/v3/transactions"
    
    # Step 1: Collect raw data from the API
    raw_data = collect_transactions(api_url)
    
    # Step 2: Clean the collected data
    cleaner = DataCleaner(raw_data)
    cleaner.remove_null_values()
    cleaner.correct_data_types()
    cleaner.remove_duplicates()
    cleaner.handle_outliers()
    clean_data = cleaner.get_clean_data()
    
    # Step 3: Send the cleaned data to the Hive data warehouse
    send_to_hive(clean_data.to_dict(orient="records"))
