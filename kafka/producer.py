import os
import json
import time
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

print("=" * 60)
print("Kafka Producer Started")
print("=" * 60)

print("Reading:", csv_file)

df = pd.read_csv(csv_file)

# Send only first 20 records
df = df.head(20)

print(f"\nSending {len(df)} records...\n")

for _, row in df.iterrows():

    future = producer.send(TOPIC, row.to_dict())

    metadata = future.get(timeout=10)

    print(
        f"✓ Sensor {row['sensor_id']} | "
        f"Partition={metadata.partition} | "
        f"Offset={metadata.offset}"
    )

    time.sleep(0.2)

producer.flush()

print("\nFinished sending all records.")

producer.close()