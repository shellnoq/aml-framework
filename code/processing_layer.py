import tensorflow as tf

def anomaly_detection(data):
    # Dummy model for anomaly detection
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(data.shape[1],)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model.predict(data)

if __name__ == "__main__":
    # Example data
    data = [[0.1, 0.2], [0.9, 1.0]]
    anomalies = anomaly_detection(data)
    print("Anomalies detected:", anomalies)
