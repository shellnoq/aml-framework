blockchain-security-framework/  
│
├── README.md                
├── LICENSE                  
├── requirements.txt         
├── input_layer/             
│   ├── collect_data.py  
│   └── __init__.py  
├── data_warehouse/          # Hive entegrasyonu  
│   ├── setup_hive.sql  
│   ├── hive_server.py       # Veri alımı için Flask API  
│   └── __init__.py  
├── processing_layer/        # Veri işleme ve skor hesaplama  
│   ├── anomaly_detection.py  
│   ├── risk_scoring.py  
│   └── __init__.py  
├── decision_layer/          # Karar katmanı  
│   ├── decision_maker.py  
│   └── __init__.py    
├── dashboard/               # Raporlama ve görselleştirme  
│   ├── dashboard.py  
│   ├── templates/  
│   │   └── dashboard.html  
│   └── __init__.py  
└── tests/                   # Test dosyaları  
    ├── test_processing.py  
    ├── test_decision_layer.py  
    └── __init__.py  