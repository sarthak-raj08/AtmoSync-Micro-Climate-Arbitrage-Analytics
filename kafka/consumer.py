import os
import sys
import json

# --------------------------------------------------
# Add project root
# --------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from kafka import KafkaConsumer

from kafka_config import BOOTSTRAP_SERVERS, GROUP_ID, TOPIC

from analytics.health_score import HealthScoreEngine
from analytics.spoilage_prediction import SpoilagePredictionEngine
from analytics.route_optimizer import RouteOptimizer
from analytics.arbitrage_engine import ArbitrageEngine

from database.snowflake_db import get_connection
from alerts.alert_engine import AlertEngine
from alerts.email_alert import EmailAlert
# --------------------------------------------------
# Kafka Consumer
# --------------------------------------------------

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    group_id=GROUP_ID,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

# --------------------------------------------------
# Analytics Engines
# --------------------------------------------------

health_engine = HealthScoreEngine()
spoilage_engine = SpoilagePredictionEngine()
route_engine = RouteOptimizer()
arbitrage_engine = ArbitrageEngine()
alert_engine = AlertEngine()
email_alert = EmailAlert()

last_alert = {}

DEFAULT_PRODUCT = "Avocado"

# --------------------------------------------------
# Snowflake Connection
# --------------------------------------------------

conn = get_connection()
cursor = conn.cursor()

print("=" * 80)
print("      AtmoSync Real-Time Analytics Engine")
print("=" * 80)

try:

    for message in consumer:

        data = message.value

        required_fields = [
            "sensor_id",
            "timestamp",
            "container_id",
            "shipment_id",
            "route_id",
            "temperature_c",
            "humidity_percent",
            "vibration_level",
            "door_status",
            "gps_latitude",
            "gps_longitude",
            "battery_percent",
            "network_signal",
        ]

        missing = [field for field in required_fields if field not in data]

        if missing:
            print(f"❌ Missing fields: {missing}")
            continue


        # ------------------------------
        # Analytics
        # ------------------------------

        health = health_engine.calculate(data)

        spoilage = spoilage_engine.predict(data)

        route = route_engine.optimize(data)

        market = arbitrage_engine.find_best_market(DEFAULT_PRODUCT)
        alerts = alert_engine.check(data)

        # ------------------------------
        # Upload to Snowflake
        # ------------------------------

        cursor.execute(
            """
            INSERT INTO SENSOR_DATA
            (
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
            VALUES
            (
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,
                %s,%s,%s
            )
            """,
            (
                data["sensor_id"],
                data["timestamp"],
                data["container_id"],
                data["shipment_id"],
                data["route_id"],
                float(data["temperature_c"]),
                float(data["humidity_percent"]),
                float(data["vibration_level"]),
                data["door_status"],
                float(data["gps_latitude"]),
                float(data["gps_longitude"]),
                int(data["battery_percent"]),
                data["network_signal"],
            )
        )

        try:
            conn.commit()
        except Exception as e:
            print("❌ Snowflake Commit Error:", e)
            continue

        # ------------------------------
        # Console Output
        # ------------------------------

        print("\n" + "=" * 80)

        print("LIVE SENSOR DATA")
        print("-" * 80)

        print(f"Sensor ID      : {data['sensor_id']}")
        print(f"Container ID   : {data['container_id']}")
        print(f"Shipment ID    : {data['shipment_id']}")
        print(f"Temperature    : {data['temperature_c']} °C")
        print(f"Humidity       : {data['humidity_percent']} %")
        print(f"Vibration      : {data['vibration_level']}")
        print(f"Battery        : {data['battery_percent']} %")
        print(f"Door           : {data['door_status']}")
        print(f"Timestamp      : {data['timestamp']}")

        print("\nHEALTH ANALYSIS")
        print("-" * 80)

        print(f"Health Score   : {health['health_score']}")
        print(f"Risk Level     : {health['risk_level']}")

        print("\nSPOILAGE")
        print("-" * 80)

        print(f"Probability    : {spoilage['spoilage_probability']} %")
        print(f"Status         : {spoilage['spoilage_status']}")

        print("\nROUTE")
        print("-" * 80)

        print(f"Priority       : {route['priority']}")
        print(f"Recommendation : {route['recommended_action']}")

        print("\nMARKET")
        print("-" * 80)

        print(f"Product        : {market['product']}")
        print(f"Best Market    : {market['best_market']}")
        print(f"Price          : ₹{market['market_price']}")
        print(f"Demand Index   : {market['demand_index']}")
        print(f"Supply Index   : {market['supply_index']}")
        print(f"Recommendation : {market['recommendation']}")

        print("\n🚨 ALERTS")
        print("-" * 80)

        if alerts:

            for alert in alerts:
                print(alert)

            body = f"""
Container ID : {data['container_id']}

Shipment ID : {data['shipment_id']}

Temperature : {data['temperature_c']} °C

Humidity : {data['humidity_percent']} %

Battery : {data['battery_percent']} %

Alerts:

{chr(10).join(alerts)}
"""

            subject = f"🚨 AtmoSync Alert - {data['container_id']}"

            current_alert = tuple(alerts)

            if last_alert.get(data["container_id"]) != current_alert:

                try:
                    email_alert.send(subject, body)
                    last_alert[data["container_id"]] = current_alert
                    print("📧 Email Alert Sent")

                except Exception as e:
                    print("Email Error:", e)

        else:

            print("No alerts")

        print("\n✅ Uploaded to Snowflake Successfully")

        print("=" * 80)
        
except KeyboardInterrupt:

    print("\nConsumer stopped.")

except Exception as e:

    print("\n❌ Error")
    print(e)

finally:

    consumer.close()
    cursor.close()
    conn.close()