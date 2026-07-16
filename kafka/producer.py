import json
import time
import pandas as pd

from kafka import KafkaProducer

from kafka_config import BOOTSTRAP_SERVERS
from topics import TOPIC


producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)


csv_file = "../data/raw/container_sensor_data.csv"

print("=" * 60)
print("Kafka Producer Started")
print("=" * 60)

df = pd.read_csv(csv_file)

for _, row in df.iterrows():

    future = producer.send(TOPIC, row.to_dict())
    future.get(timeout=10)

    print(
        f"Sent Sensor {row['sensor_id']} "
        f"Container {row['container_id']} "
        f"Temp={row['temperature_c']}"
    )

    time.sleep(0.1)

producer.flush()

print("\nFinished sending all records.")