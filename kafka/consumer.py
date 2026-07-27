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

from kafka_config import BOOTSTRAP_SERVERS, GROUP_ID
from topics import TOPIC

from analytics.health_score import HealthScoreEngine
from analytics.spoilage_prediction import SpoilagePredictionEngine
from analytics.route_optimizer import RouteOptimizer
from analytics.arbitrage_engine import ArbitrageEngine


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

health_engine = HealthScoreEngine()
spoilage_engine = SpoilagePredictionEngine()
route_engine = RouteOptimizer()
arbitrage_engine = ArbitrageEngine()

print("=" * 80)
print("        AtmoSync Real-Time Analytics Engine")
print("=" * 80)

# Default product until shipment-product mapping is added
DEFAULT_PRODUCT = "Avocado"

try:

    for message in consumer:

        data = message.value

        health = health_engine.calculate(data)

        spoilage = spoilage_engine.predict(data)

        route = route_engine.optimize(data)

        market = arbitrage_engine.find_best_market(DEFAULT_PRODUCT)

        print("\n" + "=" * 80)

        print("LIVE SENSOR DATA")
        print("-" * 80)

        print(f"Sensor ID        : {data['sensor_id']}")
        print(f"Container ID     : {data['container_id']}")
        print(f"Shipment ID      : {data['shipment_id']}")
        print(f"Temperature      : {data['temperature_c']} °C")
        print(f"Humidity         : {data['humidity_percent']} %")
        print(f"Vibration        : {data['vibration_level']}")
        print(f"Battery          : {data['battery_percent']} %")
        print(f"Door             : {data['door_status']}")
        print(f"Timestamp        : {data['timestamp']}")

        print("\nHEALTH ANALYSIS")
        print("-" * 80)

        print(f"Health Score     : {health['health_score']}/100")
        print(f"Risk Level       : {health['risk_level']}")

        print("\nSPOILAGE ANALYSIS")
        print("-" * 80)

        print(f"Probability      : {spoilage['spoilage_probability']} %")
        print(f"Status           : {spoilage['spoilage_status']}")

        print("\nROUTE OPTIMIZATION")
        print("-" * 80)

        print(f"Priority         : {route['priority']}")
        print(f"Recommendation   : {route['recommended_action']}")

        print("\nMARKET ANALYSIS")
        print("-" * 80)

        print(f"Product          : {market['product']}")
        print(f"Best Market      : {market['best_market']}")
        print(f"Price / Kg       : ₹{market['market_price']}")
        print(f"Demand Index     : {market['demand_index']}")
        print(f"Supply Index     : {market['supply_index']}")
        print(f"Recommendation   : {market['recommendation']}")

        print("=" * 80)

except KeyboardInterrupt:
    print("\nConsumer stopped.")

finally:
    consumer.close()