# Blockchain AML - Security Framework

A multi-layered framework designed to enhance blockchain security, mitigate arbitrage attacks, prevent liquidity exploits, and ensure AML compliance.

## Features
- Dynamic Pricing Mechanism
- AI-Based Anomaly Detection
- Regulatory Compliance Layer
- Real-time Transaction Validation

## Architecture Overview
![Architecture Diagram](docs/architecture_diagram.png)

# Blockchain AML-Security Framework 

This project implements a multi-layered blockchain security framework. The Data Warehouse layer is built on Apache Hive to organize and classify blockchain transaction data in real-time.

## Features
- Direct data flow from Input Layer to Hive
- Real-time transaction classification and storage
- Anomaly detection and risk scoring in subsequent layers

## Setup
### Prerequisites
- Hadoop and Hive installed
- Python 3.8+
- Required Python packages (`pyhive`, `requests`)

### Installation
1. Clone the repository:
```bash  
   git clone https://github.com/yourusername/blockchain-security-framework.git  
   cd blockchain-security-framework  
```  

2. install requirements.
```bash  
pip install -r requirements.txt
```

hive -f data_warehouse/setup_hive.sql

Create the Hive table:

```bash  
hive -f data_warehouse/setup_hive.sql
```

Run the Input Layer to collect and send data:
```bash
python input_layer/collect_data.py
```  

Query data from Hive:  
``` bash
python data_warehouse/query_data.py
``` 

## Kütüphane Açıklamaları
pyhive: Apache Hive ile Python arasında bağlantı kurmak için kullanılır.
thrift ve thrift-sasl: HiveServer2 bağlantısı için gerekli protokol ve kimlik doğrulama desteğini sağlar.
sasl: Hive ile güvenli kimlik doğrulama için gereklidir.
requests: API'lerden veri toplamak için kullanılır.
pandas: Verilerin işlenmesi ve düzenlenmesi için güçlü bir kütüphanedir.
scikit-learn: Makine öğrenimi algoritmaları ile risk skorlama ve anomali tespiti için.
tensorflow (Opsiyonel): Gelişmiş yapay zeka analizleri için.
sqlalchemy (Opsiyonel): SQL tabanlı işlemler ve Hive bağlantısı için ek destek sağlar.


## Contributing
Contributions are welcome! Please submit a pull request or open an issue.
