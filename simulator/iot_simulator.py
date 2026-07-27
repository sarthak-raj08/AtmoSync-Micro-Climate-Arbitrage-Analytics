import time
import pandas as pd

from sensor_generator import generate_sensor
from weather_generator import generate_weather

records = []

sensor = 1

print("="*60)
print("IoT Simulator Started")
print("="*60)

while True:

    row = generate_sensor(sensor)

    row.update(generate_weather())

    records.append(row)

    print(row)

    sensor += 1

    if sensor > 500:
        break

    time.sleep(0.2)

df = pd.DataFrame(records)

df.to_csv("../data/raw/generated_sensor_data.csv", index=False)

print("\nGenerated", len(df), "records.")