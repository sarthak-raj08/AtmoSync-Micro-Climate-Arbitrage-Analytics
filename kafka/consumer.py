import json

from kafka import KafkaConsumer
from kafka_config import BOOTSTRAP_SERVERS
from topics import TOPIC

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("=" * 60)
print("Kafka Consumer Started")
print("=" * 60)

for message in consumer:
    data = message.value

    print(f"""
Sensor ID     : {data['sensor_id']}
Container     : {data['container_id']}
Temperature   : {data['temperature_c']} °C
Humidity      : {data['humidity_percent']} %
Battery       : {data['battery_percent']} %
Door          : {data['door_status']}
Location      : ({data['gps_latitude']}, {data['gps_longitude']})
Timestamp     : {data['timestamp']}
---------------------------------------------------------
""")