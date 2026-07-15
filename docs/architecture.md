# AtmoSync - Project Architecture

## Project Overview

AtmoSync is a real-time micro-climate arbitrage analytics system designed to monitor refrigerated shipping containers transporting perishable commodities. The system continuously collects IoT sensor data and provides business intelligence insights for spoilage prediction and market decision-making.

## Architecture Diagram

                IoT Sensors
                      │
                      ▼
            Python IoT Simulator
                      │
                      ▼
                 Apache Kafka
                      │
                      ▼
          Snowflake Data Warehouse
                      │
                      ▼
                 dbt ELT Models
                      │
                      ▼
               Power BI Dashboard
                      │
                      ▼
      Business Alerts & Decision Support
