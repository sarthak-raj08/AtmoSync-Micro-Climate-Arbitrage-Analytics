import random


def generate_weather():

    return {
        "outside_temperature": round(random.uniform(18,42),2),
        "rainfall_mm": round(random.uniform(0,40),2),
        "wind_speed": round(random.uniform(0,25),2)
    }