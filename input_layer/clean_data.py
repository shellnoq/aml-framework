import pandas as pd

class DataCleaner:
    """
    A class to perform data cleaning tasks, such as removing null values, 
    correcting data types, removing duplicates, and handling outliers.
    """

    def __init__(self, data):
        """
        Initializes the DataCleaner with raw data.
        
        :param data: List of dictionaries containing raw transaction data.
        """
        self.data = pd.DataFrame(data)

    def remove_null_values(self):
        """
        Removes rows with null or missing values from the dataset.
        """
        self.data.dropna(inplace=True)
        print("Null values removed.")

    def correct_data_types(self):
        """
        Corrects the data types of specific columns.
        Converts 'amount' to numeric and 'timestamp' to datetime.
        """
        self.data['amount'] = pd.to_numeric(self.data['amount'], errors='coerce')
        self.data['timestamp'] = pd.to_datetime(self.data['timestamp'], errors='coerce')
        print("Data types corrected.")

    def remove_duplicates(self):
        """
        Removes duplicate transactions based on the 'transaction_id' column.
        """
        self.data.drop_duplicates(subset=['transaction_id'], inplace=True)
        print("Duplicate records removed.")

    def handle_outliers(self):
        """
        Identifies and removes outliers in the 'amount' column using the IQR method.
        """
        q1 = self.data['amount'].quantile(0.25)
        q3 = self.data['amount'].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        self.data = self.data[(self.data['amount'] >= lower_bound) & (self.data['amount'] <= upper_bound)]
        print("Outliers removed.")

    def get_clean_data(self):
        """
        Returns the cleaned dataset.
        
        :return: Pandas DataFrame containing cleaned data.
        """
        return self.data

# Example usage of DataCleaner
if __name__ == "__main__":
    # Sample raw data
    raw_data = [
        {"transaction_id": "tx1", "transaction_type": "user_transaction", "amount": "100", "timestamp": "2024-12-22T10:00:00"},
        {"transaction_id": "tx2", "transaction_type": "smart_contract", "amount": "200", "timestamp": "invalid_date"},
        {"transaction_id": "tx1", "transaction_type": "user_transaction", "amount": "100", "timestamp": "2024-12-22T10:00:00"},  # Duplicate
        {"transaction_id": "tx3", "transaction_type": "user_transaction", "amount": "10000", "timestamp": "2024-12-22T12:00:00"}  # Outlier
    ]
    
    # Instantiate the cleaner and perform cleaning steps
    cleaner = DataCleaner(raw_data)
    cleaner.remove_null_values()
    cleaner.correct_data_types()
    cleaner.remove_duplicates()
    cleaner.handle_outliers()
    
    # Get the cleaned data
    clean_data = cleaner.get_clean_data()
    print("Cleaned Data:")
    print(clean_data)
