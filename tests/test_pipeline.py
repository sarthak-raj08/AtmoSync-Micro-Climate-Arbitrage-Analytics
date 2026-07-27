import unittest
import os
import sys
import pandas as pd

# --------------------------------------------------
# Project Root
# --------------------------------------------------

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# --------------------------------------------------
# Imports
# --------------------------------------------------

from analytics.health_score import HealthScoreEngine
from analytics.spoilage_prediction import SpoilagePredictionEngine
from analytics.route_optimizer import RouteOptimizer
from analytics.arbitrage_engine import ArbitrageEngine


class TestPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.dataset = os.path.join(
            PROJECT_ROOT,
            "data",
            "raw",
            "container_sensor_data.csv"
        )

        cls.df = pd.read_csv(cls.dataset)

        cls.health_engine = HealthScoreEngine()
        cls.spoilage_engine = SpoilagePredictionEngine()
        cls.route_engine = RouteOptimizer()
        cls.arbitrage_engine = ArbitrageEngine()

    # --------------------------------------------------

    def test_dataset_exists(self):
        self.assertTrue(os.path.exists(self.dataset))

    # --------------------------------------------------

    def test_dataset_not_empty(self):
        self.assertGreater(len(self.df), 0)

    # --------------------------------------------------

    def test_required_columns(self):

        required = [
            "sensor_id",
            "temperature_c",
            "humidity_percent",
            "battery_percent",
            "vibration_level",
            "door_status"
        ]

        for col in required:
            self.assertIn(col, self.df.columns)

    # --------------------------------------------------

    def test_health_score(self):

        row = self.df.iloc[0].to_dict()

        result = self.health_engine.calculate(row)

        self.assertIn("health_score", result)
        self.assertIn("risk_level", result)

        self.assertGreaterEqual(result["health_score"], 0)
        self.assertLessEqual(result["health_score"], 100)

    # --------------------------------------------------

    def test_spoilage_prediction(self):

        row = self.df.iloc[0].to_dict()

        result = self.spoilage_engine.predict(row)

        self.assertIn("spoilage_probability", result)
        self.assertIn("spoilage_status", result)

    # --------------------------------------------------

    def test_route_optimizer(self):

        row = self.df.iloc[0].to_dict()

        result = self.route_engine.optimize(row)

        self.assertIn("priority", result)
        self.assertIn("recommended_action", result)

    # --------------------------------------------------

    def test_arbitrage_engine(self):

        self.assertIsNotNone(self.arbitrage_engine.df)

        self.assertGreater(len(self.arbitrage_engine.df), 0)


if __name__ == "__main__":

    print("=" * 60)
    print("Running Pipeline Tests")
    print("=" * 60)

    unittest.main(verbosity=2)