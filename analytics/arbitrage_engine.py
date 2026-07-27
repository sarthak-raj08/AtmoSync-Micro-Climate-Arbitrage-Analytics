"""
AtmoSync Arbitrage Engine
"""

import os
import pandas as pd


class ArbitrageEngine:

    def __init__(self):

        BASE_DIR = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        csv_path = os.path.join(
            BASE_DIR,
            "data",
            "raw",
            "commodity_prices.csv"
        )

        self.df = pd.read_csv(csv_path)

    def find_best_market(self, product):

        product_df = self.df[
            self.df["product"].str.lower() ==
            product.lower()
        ]

        if product_df.empty:

            return {

                "product": product,

                "best_market": "Unknown",

                "market_price": 0,

                "demand_index": 0,

                "supply_index": 0,

                "recommendation": "Product not found"

            }

        best = product_df.sort_values(

            by=[
                "market_price_per_kg",
                "demand_index",
                "supply_index"
            ],

            ascending=[False, False, True]

        ).iloc[0]

        return {

            "product": best["product"],

            "best_market": best["city"],

            "market_price": float(best["market_price_per_kg"]),

            "demand_index": int(best["demand_index"]),

            "supply_index": int(best["supply_index"]),

            "recommendation": "Sell in this market"

        }

    def analyze(self, sensor_data):

        """
        Auto analyze shipment.

        Later we can infer product using AI.
        """

        product = "Tomato"

        return self.find_best_market(product)