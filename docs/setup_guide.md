# Setup Guide

## Project Name

AtmoSync - Micro-Climate Arbitrage Analytics

---

## System Requirements

Before running the project, make sure the following software is installed on your system.

---

## Required Software

| Software | Version |
|---------|---------|
| Python | 3.10 or above |
| Visual Studio Code | Latest |
| Git | Latest |
| Apache Kafka | Latest |
| Snowflake Account | Required |
| dbt | Latest |
| Apache Superset | Latest |

---

## Install Python

Verify installation:

```
python --version
```

---

## Install Git

Verify installation:

```
git --version
```

---

## Install Visual Studio Code

Verify installation by opening VS Code.

Recommended Extensions:

- Python
- GitHub Pull Requests
- Markdown Preview
- SQL Tools

---

## Clone the Repository

```
git clone <repository_url>
```

Move to the project folder:

```
cd AtmoSync-Micro-Climate-Arbitrage-Analytics
```

---

## Project Folder Structure

```
AtmoSync-Micro-Climate-Arbitrage-Analytics

│
├── .github
├── alerts
├── analytics
├── data
├── dbt
├── docs
├── kafka
├── Python
├── simulator
├── snowflake
├── sql
├── tests
└── README.md
```

---

## Create Virtual Environment

```
python -m venv venv
```

Activate the virtual environment.

Windows:

```
venv\Scripts\activate
```

Verify:

```
python --version
```

---

## Install Required Libraries

```
pip install pandas
```

```
pip install faker
```

```
pip install kafka-python
```

```
pip install snowflake-connector-python
```

```
pip install dbt-core
```

```
pip install apache-superset
```

You can also install all dependencies using:

```
pip install -r requirements.txt
```

---

## Setup Apache Kafka

Steps:

- Download Kafka.
- Configure Kafka server.
- Create Kafka topics.
- Start Kafka services.

Kafka will be used for:

- Real-time event streaming.
- Message processing.

---

## Setup Snowflake

Create:

- Database
- Schema
- Tables

Required Tables:

- container_master
- shipment_master
- container_sensor_data
- commodity_prices
- market_locations
- spoilage_rules

---

## Setup dbt

Configure:

- Snowflake profile.
- Database connection.
- SQL models.

Verify:

```
dbt debug
```

Run:

```
dbt run
```

---

## Setup Apache Superset

Configure:

- Snowflake connection.
- Dashboard datasets.
- Charts.
- Filters.

Create dashboards for:

- Shipment Monitoring
- Spoilage Analysis
- Container Health
- Market Opportunities

---

## Run the Project

Execution Flow:

```
Run Python Simulator
       ↓
Send Data to Kafka
       ↓
Kafka Consumer Reads Data
       ↓
Store Data in Snowflake
       ↓
Run dbt Models
       ↓
Perform Analytics
       ↓
Visualize in Superset
```

---

## Testing Checklist

Ensure the following components are working properly:

- Python Simulator
- Kafka Producer
- Kafka Consumer
- Snowflake Connection
- dbt Models
- Analytical Queries
- Apache Superset Dashboard
- Business Alerts

---

## Troubleshooting

Common Issues:

- Python installation issues.
- Kafka connection errors.
- Snowflake authentication errors.
- dbt configuration issues.
- Dashboard connection problems.

Verify all software versions before execution.

---

## Conclusion

After completing the above setup steps, the AtmoSync project will be ready for real-time data ingestion, transformation, analytics, and business intelligence reporting.
