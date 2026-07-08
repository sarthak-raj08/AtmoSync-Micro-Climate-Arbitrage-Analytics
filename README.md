# 🌦️ AtmoSync - Micro-Climate Arbitrage Analytics

> An end-to-end real-time data engineering and analytics platform that monitors micro-climate conditions inside commodity shipping containers to predict spoilage risk, identify arbitrage opportunities, and enable intelligent shipment rerouting.

![Status](https://img.shields.io/badge/Status-In%20Development-orange)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Apache Kafka](https://img.shields.io/badge/Apache-Kafka-black?logo=apachekafka)
![Snowflake](https://img.shields.io/badge/Snowflake-Cloud%20Warehouse-29B5E8?logo=snowflake)
![dbt](https://img.shields.io/badge/dbt-Analytics%20Engineering-FF694B?logo=dbt)
![Apache Superset](https://img.shields.io/badge/Apache-Superset-20A6C9)
![SQL](https://img.shields.io/badge/SQL-Analytics-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Project Overview

Traditional supply chain systems primarily rely on GPS tracking and macro-level weather forecasts. However, they often fail to monitor the **real-time environmental conditions inside shipping containers**, where sudden changes in temperature, humidity, or vibration can significantly reduce the quality and shelf life of perishable goods.

**AtmoSync** is a real-time analytics platform that leverages IoT sensor streams, cloud data warehousing, modern ELT pipelines, and interactive dashboards to monitor container health, predict spoilage, calculate arbitrage opportunities, and recommend optimal rerouting decisions before financial losses occur.

---

# 🚀 Business Problem

Perishable commodities such as fruits and vegetables can deteriorate rapidly during transportation due to:

- Rising internal temperature
- Excessive humidity
- Continuous vibration
- Delayed delivery routes

These factors often remain undetected until products reach their destination, resulting in:

- Product spoilage
- Revenue loss
- Customer dissatisfaction
- Supply chain inefficiencies

AtmoSync addresses these challenges through continuous monitoring and predictive analytics.

---

# 🎯 Project Objectives

- Stream real-time IoT sensor data
- Monitor container environmental conditions
- Predict spoilage risk
- Calculate Spoilage Arbitrage opportunities
- Recommend optimal rerouting destinations
- Build automated ELT pipelines
- Visualize operational insights through interactive dashboards

---

# 💼 Business Use Case

A commodities trader monitors avocado shipments across multiple locations.

When the system detects that the temperature inside a shipping container exceeds the acceptable threshold, AtmoSync estimates the remaining shelf life of the products.

Instead of delivering the shipment to its original destination, the platform recommends rerouting it to a nearby market where the products can be sold before spoilage occurs, maximizing profit while minimizing waste.

---

# 🏗️ System Architecture

```
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
Apache Superset Dashboard
      │
      ▼
Business Alerts & Decision Support
```

---

# ⚙️ Technology Stack

| Category | Technology |
|----------|------------|
| Programming | Python |
| Streaming Platform | Apache Kafka |
| Cloud Data Warehouse | Snowflake |
| Data Transformation | dbt Core |
| Database Language | SQL |
| Business Intelligence | Apache Superset |
| Alerting | Slack / Email |
| Version Control | Git & GitHub |

---

# 📂 Project Modules

## 1. IoT Data Simulation

A Python-based simulator continuously generates synthetic sensor data representing shipping container conditions.

Generated parameters include:

- Temperature
- Humidity
- Vibration
- Timestamp
- Container ID

---

## 2. Real-Time Data Streaming

Apache Kafka acts as the event streaming platform responsible for:

- Publishing sensor events
- Managing streaming topics
- Delivering real-time data reliably
- Handling high-throughput ingestion

---

## 3. Cloud Data Warehouse

Snowflake stores:

- Raw IoT sensor data
- Historical commodity prices
- Shipment information
- Market data
- Processed analytical datasets

---

## 4. Data Transformation

dbt transforms raw sensor streams into analytical models by:

- Cleaning data
- Removing duplicates
- Handling missing values
- Creating staging models
- Building business metrics
- Calculating spoilage scores

---

## 5. Spoilage Prediction Engine

Business logic estimates:

- Remaining shelf life
- Spoilage probability
- Container health status
- Risk level

---

## 6. Arbitrage Analytics

The platform compares:

- Current market price
- Nearby market prices
- Transportation cost
- Predicted spoilage

to calculate:

**Spoilage Arbitrage**

This helps determine whether rerouting a shipment will generate additional profit.

---

## 7. Dashboard & Reporting

Apache Superset provides interactive dashboards displaying:

- Live container monitoring
- Temperature trends
- Humidity analysis
- High-risk shipments
- Spoilage predictions
- Arbitrage opportunities
- Shipment recommendations
- Executive KPIs

---

# 📊 Key Performance Indicators (KPIs)

- Total Active Containers
- Average Temperature
- Average Humidity
- High-Risk Containers
- Spoilage Probability
- Predicted Financial Loss
- Arbitrage Profit
- Shipment Health Score
- Remaining Shelf Life
- Live Operational Alerts

---

# 🗂️ Expected Database Tables

### sensor_data

| Column |
|----------|
| container_id |
| temperature |
| humidity |
| vibration |
| timestamp |

---

### commodity_prices

| Column |
|----------|
| commodity |
| market |
| price |
| updated_time |

---

### shipment_routes

| Column |
|----------|
| container_id |
| current_location |
| destination |
| distance |

---

### spoilage_prediction

| Column |
|----------|
| container_id |
| spoilage_score |
| remaining_life |
| risk_level |

---

# 📈 Dashboard Features

- Live IoT Monitoring
- Real-Time Temperature Analysis
- Humidity Monitoring
- Spoilage Risk Gauge
- Arbitrage Opportunity Dashboard
- Shipment Health Overview
- Commodity Price Comparison
- Route Optimization Insights
- Executive Summary
- Automated Alert Panel

---

# 📁 Proposed Project Structure

```
AtmoSync/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── pricing/
│
├── kafka/
│   ├── producer.py
│   ├── consumer.py
│   └── topics.py
│
├── simulator/
│   └── iot_simulator.py
│
├── snowflake/
│   ├── schema.sql
│   └── tables.sql
│
├── dbt/
│   ├── models/
│   ├── staging/
│   └── marts/
│
├── dashboard/
│   └── superset/
│
├── sql/
│
├── notebooks/
│
├── docs/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

---

# 🔄 End-to-End Workflow

1. Generate IoT sensor data
2. Publish events to Apache Kafka
3. Stream data into Snowflake
4. Transform data using dbt
5. Calculate spoilage metrics
6. Compute arbitrage opportunities
7. Visualize insights in Apache Superset
8. Trigger business alerts
9. Enable data-driven shipment decisions

---

# 📚 Learning Outcomes

Through this project, we gain practical experience in:

- Modern Data Engineering
- Event Streaming
- Cloud Data Warehousing
- Analytics Engineering
- ELT Pipeline Development
- SQL Data Modelling
- Business Intelligence
- Real-Time Dashboard Development
- Supply Chain Analytics
- IoT Data Processing

---

# 📌 Future Enhancements

- Machine Learning-based spoilage prediction
- Predictive route optimization
- GIS map visualization
- Live GPS tracking
- Mobile notification support
- Power BI integration
- REST API development
- Docker containerization
- Kubernetes deployment
- CI/CD automation

---

# 👨‍💻 Team Project

This project is being developed as part of an **Advanced Data Analytics & Engineering Internship**.

The objective is to build a production-style, real-time data engineering solution using modern cloud-native technologies and industry best practices.

---

# 📄 License

This project is intended for educational and internship purposes.

---

## ⭐ If you found this project interesting, don't forget to give it a Star!
