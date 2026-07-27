import unittest
import json
import time
import uuid
import os
import importlib.util

# -------------------------------------------------------
# Project Root
# -------------------------------------------------------

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# -------------------------------------------------------
# Import kafka-python library
# -------------------------------------------------------

from kafka import KafkaProducer, KafkaConsumer

# -------------------------------------------------------
# Load kafka_config.py
# -------------------------------------------------------

config_path = os.path.join(PROJECT_ROOT, "kafka", "kafka_config.py")

spec = importlib.util.spec_from_file_location("kafka_config", config_path)
kafka_config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kafka_config)

BOOTSTRAP_SERVERS = kafka_config.BOOTSTRAP_SERVERS

# -------------------------------------------------------
# Load topics.py
# -------------------------------------------------------

topic_path = os.path.join(PROJECT_ROOT, "kafka", "topics.py")

spec2 = importlib.util.spec_from_file_location("topics", topic_path)
topics = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(topics)

TOPIC = topics.TOPIC


class KafkaTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.producer = KafkaProducer(
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    @classmethod
    def tearDownClass(cls):

        cls.producer.close()

    # ---------------------------------------------------

    def test_connection(self):

        print("\nTesting Kafka connection...")

        self.assertTrue(self.producer.bootstrap_connected())

    # ---------------------------------------------------

    def test_send_receive(self):

        print("\nTesting Producer -> Consumer...")

        consumer = KafkaConsumer(
            bootstrap_servers=BOOTSTRAP_SERVERS,
            group_id=f"test-group-{uuid.uuid4()}",
            auto_offset_reset="latest",
            enable_auto_commit=False,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
            consumer_timeout_ms=10000
        )

        consumer.subscribe([TOPIC])

        # Wait until partitions are assigned
        timeout = time.time() + 10
        while not consumer.assignment():
            consumer.poll(timeout_ms=100)
            if time.time() > timeout:
                self.fail("Consumer failed to subscribe to topic.")

        sensor_id = int(time.time())

        sample = {
            "sensor_id": sensor_id,
            "timestamp": "2026-01-01 00:00:00",
            "container_id": "TEST001",
            "shipment_id": "SHIP001",
            "route_id": "R001",
            "temperature_c": 5,
            "humidity_percent": 70,
            "vibration_level": 1,
            "door_status": "CLOSED",
            "gps_latitude": 0,
            "gps_longitude": 0,
            "battery_percent": 90,
            "network_signal": "Strong"
        }

        future = self.producer.send(TOPIC, sample)

        metadata = future.get(timeout=10)

        self.producer.flush()

        print(
            f"Message sent to Partition={metadata.partition}, "
            f"Offset={metadata.offset}"
        )

        found = False

        end = time.time() + 10

        while time.time() < end:

            records = consumer.poll(timeout_ms=500)

            for tp in records:
                for msg in records[tp]:

                    if msg.value["sensor_id"] == sensor_id:
                        found = True
                        break

                if found:
                    break

            if found:
                break

        consumer.close()

        self.assertTrue(found)


if __name__ == "__main__":

    print("=" * 60)
    print("Running Kafka Unit Tests")
    print("=" * 60)

    unittest.main(verbosity=2)