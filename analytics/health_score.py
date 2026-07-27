"""
Health Score Engine
-------------------
Calculates container health based on IoT sensor readings.
Health Score ranges from 0 to 100.
"""

class HealthScoreEngine:

    def __init__(self):
        pass

    def calculate(self, data):
        score = 100

        temperature = float(data["temperature_c"])
        humidity = float(data["humidity_percent"])
        battery = int(data["battery_percent"])
        vibration = float(data["vibration_level"])
        door = data["door_status"]

        # Temperature
        if temperature > 10:
            score -= 25
        elif temperature > 8:
            score -= 15
        elif temperature < 2:
            score -= 10

        # Humidity
        if humidity > 85:
            score -= 20
        elif humidity > 75:
            score -= 10

        # Battery
        if battery < 20:
            score -= 20
        elif battery < 40:
            score -= 10

        # Vibration
        if vibration > 4:
            score -= 15
        elif vibration > 3:
            score -= 8

        # Door
        if door.upper() == "OPEN":
            score -= 15

        score = max(0, score)

        if score >= 90:
            risk = "LOW"
        elif score >= 70:
            risk = "MEDIUM"
        elif score >= 50:
            risk = "HIGH"
        else:
            risk = "CRITICAL"

        return {
            "health_score": score,
            "risk_level": risk
        }