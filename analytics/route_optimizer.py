"""
AtmoSync Route Optimizer
------------------------
Suggests the best operational action based on live sensor data.
"""


class RouteOptimizer:

    def __init__(self):
        pass

    def optimize(self, data):

        temperature = float(data["temperature_c"])
        humidity = float(data["humidity_percent"])
        vibration = float(data["vibration_level"])
        battery = int(data["battery_percent"])
        door = data["door_status"].upper()

        priority = "LOW"
        recommendation = "Continue current route"

        # Critical conditions
        if (
            temperature > 12
            or humidity > 90
            or vibration > 5
            or battery < 20
            or door == "OPEN"
        ):
            priority = "CRITICAL"
            recommendation = "Immediate inspection at nearest warehouse"

        # High conditions
        elif (
            temperature > 10
            or humidity > 80
            or vibration > 4
            or battery < 40
        ):
            priority = "HIGH"
            recommendation = "Reroute to nearest cold storage"

        # Medium conditions
        elif (
            temperature > 8
            or humidity > 70
            or vibration > 3
        ):
            priority = "MEDIUM"
            recommendation = "Monitor continuously"

        else:
            priority = "LOW"
            recommendation = "Route is optimal"

        return {
            "priority": priority,
            "recommended_action": recommendation
        }