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

## Architecture Explanation

### 1. IoT Sensors

The IoT sensors continuously monitor:

- Temperature
- Humidity
- GPS Location
- Battery Percentage
- Network Signal Strength
- Container Status

These sensor readings are generated at regular intervals to simulate real-time shipment monitoring.

---

### 2. Python IoT Simulator

The Python IoT Simulator performs the following tasks:

- Generates real-time sensor readings.
- Simulates container movement.
- Creates shipment-related events.
- Sends sensor data to Apache Kafka.

Technologies Used:

- Python
- Pandas
- Faker Library
- Random Library

---

### 3. Apache Kafka

Apache Kafka is responsible for:

- Real-time data streaming.
- Event processing.
- Handling high-volume sensor data.
- Reliable data transmission.

Kafka acts as the communication layer between the Python simulator and Snowflake.

---

### 4. Snowflake Data Warehouse

Snowflake stores:

- Raw sensor data.
- Shipment information.
- Commodity prices.
- Historical records.
- Market information.

Snowflake provides scalable cloud-based storage for analytical processing.

---

### 5. dbt ELT Models

dbt performs:

- Data transformation.
- Data validation.
- Business rule implementation.
- SQL model creation.

Examples:

- Spoilage calculations
- Shipment risk analysis
- Market price analysis
- Temperature trend analysis

---

### 6. Power BI Dashboard

The Power BI dashboard provides:

- Total Shipments
- Total Containers
- Average Temperature
- Spoilage Percentage
- Market Price Analysis
- Shipment Status Analysis
- Risk Analysis

The dashboard helps stakeholders monitor business performance in real time.

---

### 7. Business Alerts & Decision Support

The final module generates business alerts for:

- High temperature levels
- Shipment delays
- Spoilage risks
- Market opportunities
- Container failures

These alerts help businesses make informed decisions before products are damaged.

---
## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Data Generation |
| Apache Kafka | Real-Time Streaming |
| Snowflake | Data Warehousing |
| dbt | Data Transformation |
| SQL | Data Analysis |
| Power BI | Dashboard Creation |
| Git & GitHub | Version Control |
| VS Code | Development Environment |

---
## Project Workflow

Raw Sensor Data
        ↓
Python Simulator
        ↓
Apache Kafka
        ↓
Snowflake
        ↓
dbt Transformations
        ↓
SQL Analysis
        ↓
Power BI Dashboard
        ↓
Business Alerts
        ↓
Decision Support System

---
## Expected Output

The project provides:

- Real-time shipment monitoring.
- Spoilage prediction.
- Market price analysis.
- Risk analysis.
- Business intelligence dashboards.
- Automated business alerts.
