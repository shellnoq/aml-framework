aml-framework/   
│
├── README.md                  
├── LICENSE                
├── requirements.txt          
├── input_layer/              
│   ├── collect_data.py  
│   └── clean_data.py  
├── data_warehouse/             
│   ├── setup_hive.sql  
│   └── load_data.py   
├── processing_layer/        # Veri işleme ve skor hesaplama  
│   ├── anomaly_detection.py   
│   └── risk_scoring.py   
├── decision_layer/          # Karar katmanı  
│   └── decision_maker.py  
└── tests/                     
    ├── test_processing.py  
    └── test_decision_layer.py  
