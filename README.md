# 🌦️ AtmoSync – Micro-Climate Arbitrage Analytics

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Kafka](https://img.shields.io/badge/Apache-Kafka-black)
![Snowflake](https://img.shields.io/badge/Snowflake-Cloud-blue)
![dbt](https://img.shields.io/badge/dbt-Data%20Transformation-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

AtmoSync is a real-time supply chain analytics platform designed to monitor agricultural shipments using IoT sensor streams.

Instead of relying only on weather forecasts and delivery schedules, AtmoSync continuously analyzes micro-climate conditions inside shipping containers to detect spoilage risks before they occur.

The platform streams live sensor data through Apache Kafka, stores it in Snowflake, transforms it using dbt, and visualizes business insights through an interactive dashboard.

---

## 🎯 Problem Statement

Agricultural commodities such as fruits and vegetables are highly sensitive to environmental conditions during transportation.

Even small temperature or humidity changes can lead to:

- Food spoilage
- Financial losses
- Reduced product quality
- Missed market opportunities

Traditional logistics systems cannot detect these issues early enough.

AtmoSync solves this problem by combining streaming analytics with cloud data engineering.

---

# 🚀 Features

✔ Real-time IoT Sensor Streaming

✔ Kafka Event Streaming Pipeline

✔ Snowflake Cloud Data Warehouse

✔ dbt ELT Data Transformation

✔ Live Health Score Calculation

✔ Spoilage Prediction Engine

✔ Route Optimization

✔ Arbitrage Opportunity Detection

✔ Email Alert System

✔ Streamlit Live Dashboard

✔ Interactive Maps

✔ Historical Analytics

✔ Automated Data Quality Tests

---

# 🏗 System Architecture

```
IoT Simulator
      │
      ▼
Apache Kafka
      │
      ▼
Kafka Consumer
      │
      ▼
Analytics Engine
      │
 ┌──────────────┐
 │Health Score  │
 │Spoilage AI   │
 │Route Engine  │
 │Arbitrage AI  │
 └──────────────┘
      │
      ▼
Snowflake
      │
      ▼
dbt Models
      │
      ▼
Streamlit Dashboard
      │
      ▼
Email Alerts
```

---

# ⚙ Technology Stack

| Layer | Technology |
|--------|------------|
| Programming | Python |
| Streaming | Apache Kafka |
| Data Warehouse | Snowflake |
| ELT | dbt |
| Dashboard | Streamlit |
| Database | Snowflake |
| Alerts | SMTP Email |
| Data Processing | Pandas |
| Visualization | Plotly |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
AtmoSync
│
├── analytics/
│   ├── health_score.py
│   ├── spoilage_prediction.py
│   ├── arbitrage_engine.py
│   └── route_optimizer.py
│
├── alerts/
│   ├── alert_engine.py
│   └── email_alert.py
│
├── dashboard/
│   └── app.py
│
├── database/
│   └── snowflake_db.py
│
├── dbt/
│   ├── staging/
│   ├── intermediate/
│   ├── marts/
│   └── models/
│
├── kafka/
│   ├── producer.py
│   └── consumer.py
│
├── simulator/
│
├── screenshots/
│
└── README.md
```

---

# 📊 Analytics Modules

## 1. Health Score Engine

Calculates container health based on

- Temperature
- Humidity
- Battery
- Vibration

---

## 2. Spoilage Prediction

Predicts spoilage probability using environmental conditions.

Outputs:

- Spoilage %
- Risk Status

---

## 3. Route Optimizer

Recommends whether shipment should

- Continue
- Inspect
- Reroute

---

## 4. Arbitrage Engine

Suggests the most profitable nearby market before spoilage occurs.

Outputs:

- Best Market
- Demand Index
- Supply Index
- Estimated Price
- Recommendation

---

# 📡 Real-Time Dashboard

Dashboard includes

- Live KPI Cards
- Health Score
- Spoilage Probability
- Live Charts
- Historical Analytics
- GPS Map
- Email Alerts
- System Status
- Latest Sensor Feed

---

# 📈 dbt Pipeline

```
Raw Sensor Data
        │
        ▼
Staging Models
        │
        ▼
Intermediate Models
        │
        ▼
Mart Models
        │
        ▼
Dashboard
```

Models created

- stg_sensor_data
- int_health_score
- int_spoilage
- mart_dashboard
- mart_arbitrage

---

# 📧 Alert System

Automatic email notifications are generated whenever:

- High Temperature
- High Humidity
- Low Battery
- Weak Network
- Door Open
- High Vibration

---

# 🧪 dbt Testing

Implemented

- Not Null Tests
- Schema Validation
- Documentation
- Model Lineage

Commands

```bash
dbt debug
dbt run
dbt test
dbt docs generate
dbt docs serve
```

---

# 🚀 Installation

Clone repository

```bash
git clone https://github.com/lucasratna/AtmoSync-Micro-Climate-Arbitrage-Analytics.git
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

---

# ▶ Run Project

Producer

```bash
python kafka/producer.py
```

Consumer

```bash
python kafka/consumer.py
```

Dashboard

```bash
streamlit run dashboard/app.py
```

dbt

```bash
cd dbt

dbt run

dbt test
```

---

# 📷 Screenshots

## Dashboard

*(Add Screenshot Here)*

---

## Kafka Producer

*(Add Screenshot Here)*

---

## Kafka Consumer

*(Add Screenshot Here)*

---

## Snowflake

*(Add Screenshot Here)*

---

## dbt Documentation

*(Add Screenshot Here)*

---

# 🎯 Future Enhancements

- Docker Deployment
- Kubernetes
- ML-based Spoilage Forecasting
- Mobile Dashboard
- Power BI Integration
- Apache Superset Dashboard
- Slack Notifications
- Airflow Scheduling

---

# 👨‍💻 Author

**Lucas Ratna Lauretta**

GitHub

https://github.com/lucasratna

LinkedIn

https://www.linkedin.com/in/lucas-ratna-lauretta-47b26b345/

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.