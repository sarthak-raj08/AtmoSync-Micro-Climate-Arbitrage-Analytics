import os
import pandas as pd
from snowflake_db import get_connection

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "container_sensor_data.csv"
)

df = pd.read_csv(csv_path)

conn = get_connection()
cursor = conn.cursor()

# Ensure correct context
cursor.execute("USE WAREHOUSE ATMOSYNC_WH")
cursor.execute("USE DATABASE ATMOSYNC_DB")
cursor.execute("USE SCHEMA PUBLIC")

print("Uploading data to Snowflake...")

insert_query = """
INSERT INTO SENSOR_DATA (
    sensor_id,
    timestamp,
    container_id,
    shipment_id,
    route_id,
    temperature_c,
    humidity_percent,
    vibration_level,
    door_status,
    gps_latitude,
    gps_longitude,
    battery_percent,
    network_signal
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

data = [
    (
        row["sensor_id"],
        row["timestamp"],
        row["container_id"],
        row["shipment_id"],
        row["route_id"],
        float(row["temperature_c"]),
        float(row["humidity_percent"]),
        float(row["vibration_level"]),
        row["door_status"],
        float(row["gps_latitude"]),
        float(row["gps_longitude"]),
        int(row["battery_percent"]),
        row["network_signal"]
    )
    for _, row in df.iterrows()
]

cursor.executemany(insert_query, data)

conn.commit()

print(f"✅ Uploaded {len(df)} rows successfully!")

cursor.close()
conn.close()

print("🎉 Snowflake Upload Complete!")