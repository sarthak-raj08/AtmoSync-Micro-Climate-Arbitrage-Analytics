import os
import json
import time
import random
import pandas as pd

from kafka import KafkaProducer
from kafka_config import BOOTSTRAP_SERVERS, TOPIC

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    acks="all"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_file = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "container_sensor_data.csv"
)

df = pd.read_csv(csv_file)

print("="*70)
print("AtmoSync Continuous IoT Simulator Started")
print("=" * 70)
# ==========================================
# Continuous Streaming
# ==========================================

while True:

    for _, row in df.iterrows():

        sensor = row.to_dict()

        # Temperature changes
        sensor["temperature_c"] = round(
            float(sensor["temperature_c"]) +
            random.uniform(-0.8, 0.8),
            2
        )

        # Humidity changes
        sensor["humidity_percent"] = round(
            float(sensor["humidity_percent"]) +
            random.uniform(-2, 2),
            2
        )

        # Vibration changes
        sensor["vibration_level"] = round(
            float(sensor["vibration_level"]) +
            random.uniform(-0.3, 0.3),
            2
        )

        # Battery slowly decreases
        battery = int(sensor["battery_percent"])

        battery -= random.randint(0, 1)

        if battery < 5:
            battery = 100

        sensor["battery_percent"] = battery

        # GPS slightly changes
        sensor["gps_latitude"] = round(
            float(sensor["gps_latitude"]) +
            random.uniform(-0.0005, 0.0005),
            6
        )

        sensor["gps_longitude"] = round(
            float(sensor["gps_longitude"]) +
            random.uniform(-0.0005, 0.0005),
            6
        )

        # Door randomly opens
        if random.random() < 0.02:
            sensor["door_status"] = "OPEN"
        else:
            sensor["door_status"] = "CLOSED"
                    # Update timestamp

        sensor["timestamp"] = pd.Timestamp.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        future = producer.send(
            TOPIC,
            sensor
        )

        metadata = future.get(timeout=10)

        print(
            f"[{sensor['timestamp']}] "
            f"{sensor['sensor_id']} | "
            f"{sensor['temperature_c']}°C | "
            f"{sensor['humidity_percent']}% | "
            f"Battery {sensor['battery_percent']}% | "
            f"{sensor['door_status']} | "
            f"Partition={metadata.partition} Offset={metadata.offset}"
        )

        producer.flush()

        # One sensor reading every second
        time.sleep(1)