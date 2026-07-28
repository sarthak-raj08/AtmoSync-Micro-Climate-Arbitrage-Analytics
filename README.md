# 🌍 AtmoSync: Micro-Climate Arbitrage Analytics

> **Real-Time IoT Supply Chain Analytics Platform using Apache Kafka, Snowflake, dbt, and Streamlit**

AtmoSync is an end-to-end real-time data engineering and analytics platform that continuously monitors agricultural shipment containers using IoT sensor data. The system predicts spoilage, calculates container health, identifies arbitrage opportunities, and provides live alerts to help traders maximize profit before commodity quality degrades.

---

# 🚀 Features

- Real-Time IoT Sensor Simulation
- Apache Kafka Streaming Pipeline
- Snowflake Cloud Data Warehouse
- dbt ELT Data Transformation
- Streamlit Interactive Dashboard
- Health Score Prediction
- Spoilage Prediction
- Route Optimization
- Market Arbitrage Recommendation
- Live Container Monitoring
- Email Alert System
- Live Maps
- Automated Data Pipeline

---

# 🏗 System Architecture

```text
                 IoT Sensor Simulator
                          │
                          ▼
                  Apache Kafka Producer
                          │
                          ▼
                     Kafka Topic
                          │
                          ▼
                  Apache Kafka Consumer
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
        ▼                                   ▼
 Analytics Engine                  Snowflake Database
        │                                   │
        ▼                                   ▼
 Health Score                      dbt ELT Pipeline
 Spoilage Prediction                      │
 Route Optimization                       ▼
 Arbitrage Engine                 Analytical Models
        │                                   │
        └───────────────┬───────────────────┘
                        ▼
               Streamlit Dashboard
                        │
                        ▼
                 Email Notifications
```

---

# ⚙ Technology Stack

| Layer | Technology |
|--------|------------|
| Programming Language | Python 3.10 |
| Streaming | Apache Kafka |
| Cloud Warehouse | Snowflake |
| ELT | dbt Core |
| Dashboard | Streamlit |
| Visualization | Plotly |
| Analytics | Pandas |
| Alerts | SMTP Email |
| Database Connector | Snowflake Connector |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
AtmoSync
│
├── analytics
│   ├── health_score.py
│   ├── spoilage_prediction.py
│   ├── route_optimizer.py
│   └── arbitrage_engine.py
│
├── alerts
│   ├── alert_engine.py
│   └── email_alert.py
│
├── dashboard
│   └── app.py
│
├── database
│   └── snowflake_db.py
│
├── kafka
│   ├── producer.py
│   └── consumer.py
│
├── dbt
│   ├── models
│   ├── staging
│   ├── intermediate
│   ├── marts
│   ├── tests
│   ├── dbt_project.yml
│   ├── packages.yml
│   └── profiles.yml
│
├── simulator
│
├── requirements.txt
│
└── README.md
```

---

# 📊 Analytics Modules

## Health Score Engine

Calculates overall container health based on:

- Temperature
- Humidity
- Battery
- Network Signal
- Door Status
- Vibration

Outputs

- Health Score
- Risk Level

---

## Spoilage Prediction

Predicts

- Spoilage Probability
- Product Status
- Shelf-Life Risk

---

## Route Optimization

Suggests

- Continue Delivery
- Reroute Shipment
- Immediate Inspection

---

## Arbitrage Engine

Calculates

- Best Market
- Market Price
- Demand Index
- Supply Index
- Financial Recommendation

---

# 🚨 Alert Engine

Automatically detects

- High Temperature
- High Humidity
- Low Battery
- Weak Network
- Door Open
- High Vibration

Alerts are displayed

- Console
- Dashboard
- Email

---

# 📈 Dashboard

The Streamlit dashboard provides

- Live KPI Cards
- Health Score
- Spoilage Analysis
- Market Arbitrage
- Live Charts
- Sensor Feed
- Container Map
- Alert Monitoring
- System Status

Dashboard refreshes automatically every few seconds.

---

# 🗄 Snowflake

Stores

- Raw Sensor Data
- Historical Data
- Analytics Models
- Dashboard Tables

---

# 🔄 dbt Pipeline

### Staging

- stg_sensor_data

### Intermediate

- int_health_score
- int_spoilage

### Mart

- mart_dashboard
- mart_arbitrage

Successfully tested using

```bash
dbt run
dbt test
dbt docs generate
dbt docs serve
```

---

# 📡 Data Pipeline

```text
IoT Simulator

↓

Kafka Producer

↓

Kafka Topic

↓

Kafka Consumer

↓

Analytics Engine

↓

Snowflake

↓

dbt Models

↓

Streamlit Dashboard

↓

Email Alerts
```

---

# ▶ Running the Project

## 1. Clone Repository

```bash
git clone https://github.com/lucasratna/AtmoSync-Micro-Climate-Arbitrage-Analytics.git
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

---

## 4. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 5. Start Kafka Producer

```bash
python kafka/producer.py
```

---

## 6. Start Kafka Consumer

```bash
python kafka/consumer.py
```

---

## 7. Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

## 8. Execute dbt Models

```bash
cd dbt

dbt run --profiles-dir .

dbt test --profiles-dir .

dbt docs generate --profiles-dir .

dbt docs serve --profiles-dir .
```

---

# 📌 Project Workflow

```text
IoT Sensors
      │
      ▼
Kafka Streaming
      │
      ▼
Consumer Analytics
      │
      ▼
Snowflake Storage
      │
      ▼
dbt Transformation
      │
      ▼
Dashboard
      │
      ▼
Email Alerts
```

---

# 📧 Email Notifications

Automatically sends email when

- Temperature exceeds threshold
- Spoilage risk increases
- Door opens unexpectedly
- Battery becomes critical
- Network becomes weak

Duplicate alerts are automatically avoided.

---

# 📚 Future Enhancements

- Docker Deployment
- Apache Airflow Scheduling
- Kubernetes Deployment
- REST APIs
- Machine Learning Models
- Mobile Dashboard
- Slack Integration
- SMS Alerts
- WhatsApp Notifications
- Multi-Warehouse Monitoring

---

# 👨‍💻 Author

**Lucas Ratna Lauretta**

B.Tech Information Technology

BVRIT Hyderabad College of Engineering for Women

GitHub:
https://github.com/lucasratna

LinkedIn:
https://www.linkedin.com/in/lucas-ratna-lauretta-47b26b345/

---

# ✅ Project Status

| Module | Status |
|---------|--------|
| Kafka Producer | ✅ |
| Kafka Consumer | ✅ |
| IoT Simulator | ✅ |
| Snowflake Integration | ✅ |
| Health Score Engine | ✅ |
| Spoilage Prediction | ✅ |
| Route Optimization | ✅ |
| Arbitrage Engine | ✅ |
| Alert Engine | ✅ |
| Email Notifications | ✅ |
| Streamlit Dashboard | ✅ |
| dbt Pipeline | ✅ |
| dbt Documentation | ✅ |
| Live Monitoring | ✅ |

---

# ⭐ Result

AtmoSync demonstrates a complete real-time data engineering workflow combining streaming analytics, cloud warehousing, ELT modeling, predictive analytics, and business intelligence for intelligent agricultural supply chain optimization.
