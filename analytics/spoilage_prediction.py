"""
AtmoSync - Spoilage Prediction Engine
-------------------------------------
Predicts spoilage probability using live sensor readings.
"""

class SpoilagePredictionEngine:

    def __init__(self):
        pass

    def predict(self, data):

        probability = 0

        temperature = float(data["temperature_c"])
        humidity = float(data["humidity_percent"])
        vibration = float(data["vibration_level"])
        battery = int(data["battery_percent"])
        door = data["door_status"].upper()

        # Temperature Risk
        if temperature > 12:
            probability += 40
        elif temperature > 10:
            probability += 25
        elif temperature > 8:
            probability += 10

        # Humidity Risk
        if humidity > 90:
            probability += 25
        elif humidity > 80:
            probability += 15
        elif humidity > 70:
            probability += 5

        # Vibration Risk
        if vibration > 5:
            probability += 20
        elif vibration > 3:
            probability += 10

        # Battery Risk
        if battery < 20:
            probability += 10
        elif battery < 40:
            probability += 5

        # Door Risk
        if door == "OPEN":
            probability += 15

        probability = min(probability, 100)

        if probability < 20:
            status = "SAFE"
        elif probability < 40:
            status = "LOW RISK"
        elif probability < 60:
            status = "MEDIUM RISK"
        elif probability < 80:
            status = "HIGH RISK"
        else:
            status = "CRITICAL"

        return {
            "spoilage_probability": probability,
            "spoilage_status": status
        }