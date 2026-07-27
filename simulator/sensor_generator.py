import random
from datetime import datetime

from config import CITIES
from config import DOOR_STATUS
from config import NETWORK
from config import PRODUCTS


def generate_sensor(sensor_no):

    return {
        "sensor_id": sensor_no,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "container_id": f"C{random.randint(1,500):03}",
        "shipment_id": f"SH{random.randint(1000,9999)}",
        "route_id": f"R{random.randint(1,99):03}",
        "product": random.choice(PRODUCTS),
        "temperature_c": round(random.uniform(2,18),2),
        "humidity_percent": random.randint(60,95),
        "vibration_level": round(random.uniform(0,6),2),
        "door_status": random.choice(DOOR_STATUS),
        "city": random.choice(CITIES),
        "gps_latitude": round(random.uniform(20,24),6),
        "gps_longitude": round(random.uniform(70,74),6),
        "battery_percent": random.randint(40,100),
        "network_signal": random.choice(NETWORK)
    }