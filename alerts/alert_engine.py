class AlertEngine:

    def __init__(self):

        self.temperature_limit = 30
        self.humidity_limit = 85
        self.vibration_limit = 8
        self.battery_limit = 20

    def check(self, data):

        alerts = []

        # Temperature
        if float(data["temperature_c"]) > self.temperature_limit:

            alerts.append(
                f"🔥 High Temperature ({data['temperature_c']}°C)"
            )

        # Humidity
        if float(data["humidity_percent"]) > self.humidity_limit:

            alerts.append(
                f"💧 High Humidity ({data['humidity_percent']}%)"
            )

        # Battery
        if int(data["battery_percent"]) < self.battery_limit:

            alerts.append(
                f"🔋 Low Battery ({data['battery_percent']}%)"
            )

        # Door
        if str(data["door_status"]).upper() == "OPEN":

            alerts.append(
                "🚪 Door Open Detected"
            )

        # Network Signal
        signal = str(data["network_signal"]).strip().lower()

        if signal == "weak":

            alerts.append(
                "📶 Weak Network Signal"
            )

        # Vibration
        if float(data["vibration_level"]) > self.vibration_limit:

            alerts.append(
                f"📳 High Vibration ({data['vibration_level']})"
            )

        return alerts