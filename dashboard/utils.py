"""
AtmoSync Dashboard Utilities
Optimized Version
"""

import streamlit as st

from analytics.health_score import HealthScoreEngine
from dashboard.config import MAX_ROWS
from database.snowflake_loader import load_sensor_data


# ==========================================================
# LOAD DATA FROM SNOWFLAKE
# ==========================================================

@st.cache_data(show_spinner=False, ttl=60)
def load_data():

    df = load_sensor_data()

    if len(df) > MAX_ROWS:
        df = df.tail(MAX_ROWS)

    return df.reset_index(drop=True)


# ==========================================================
# HEALTH SCORE
# ==========================================================

@st.cache_data(show_spinner=False)
def calculate_health(df):

    engine = HealthScoreEngine()

    health_scores = []
    risk_levels = []

    for row in df.to_dict("records"):

        result = engine.calculate(row)

        health_scores.append(result["health_score"])
        risk_levels.append(result["risk_level"])

    df = df.copy()

    df["health_score"] = health_scores
    df["risk_level"] = risk_levels

    return df


# ==========================================================
# KPI METRICS
# ==========================================================

@st.cache_data(show_spinner=False)
def get_metrics(df):

    return {
        "sensors": len(df),
        "containers": df["container_id"].nunique(),
        "shipments": df["shipment_id"].nunique(),
        "avg_health": round(df["health_score"].mean(), 2)
    }


# ==========================================================
# FILTER CONTAINER
# ==========================================================

@st.cache_data(show_spinner=False)
def filter_container(df, container_id):

    return (
        df[df["container_id"] == container_id]
        .sort_values("timestamp")
        .reset_index(drop=True)
    )


# ==========================================================
# LATEST RECORDS
# ==========================================================

@st.cache_data(show_spinner=False)
def latest_records(df, rows=20):

    return (
        df.sort_values("timestamp", ascending=False)
        .head(rows)
        .reset_index(drop=True)
    )


# ==========================================================
# CHART DATA
# ==========================================================

@st.cache_data(show_spinner=False)
def chart_data(df, rows=300):

    return (
        df.tail(rows)
        .reset_index(drop=True)
    )


# ==========================================================
# TEMPERATURE SUMMARY
# ==========================================================

@st.cache_data(show_spinner=False)
def temperature_summary(df):

    return {
        "min": round(df["temperature_c"].min(), 2),
        "max": round(df["temperature_c"].max(), 2),
        "avg": round(df["temperature_c"].mean(), 2)
    }


# ==========================================================
# HUMIDITY SUMMARY
# ==========================================================

@st.cache_data(show_spinner=False)
def humidity_summary(df):

    return {
        "min": round(df["humidity_percent"].min(), 2),
        "max": round(df["humidity_percent"].max(), 2),
        "avg": round(df["humidity_percent"].mean(), 2)
    }


# ==========================================================
# BATTERY SUMMARY
# ==========================================================

@st.cache_data(show_spinner=False)
def battery_summary(df):

    return {
        "min": round(df["battery_percent"].min(), 2),
        "max": round(df["battery_percent"].max(), 2),
        "avg": round(df["battery_percent"].mean(), 2)
    }


# ==========================================================
# NETWORK SUMMARY
# ==========================================================

@st.cache_data(show_spinner=False)
def network_summary(df):

    return {
        "count": df["network_signal"].count(),
        "unique": df["network_signal"].nunique()
    }


# ==========================================================
# RISK COUNTS
# ==========================================================

@st.cache_data(show_spinner=False)
def risk_counts(df):

    return (
        df["risk_level"]
        .value_counts()
        .sort_index()
    )


# ==========================================================
# DOOR STATUS
# ==========================================================

@st.cache_data(show_spinner=False)
def door_status(df):

    return (
        df["door_status"]
        .value_counts()
    )


# ==========================================================
# CONTAINER LIST
# ==========================================================

@st.cache_data(show_spinner=False)
def container_list(df):

    return sorted(
        df["container_id"].unique().tolist()
    )


# ==========================================================
# DATASET INFO
# ==========================================================

@st.cache_data(show_spinner=False)
def dataset_information(df):

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "containers": df["container_id"].nunique(),
        "shipments": df["shipment_id"].nunique(),
        "routes": df["route_id"].nunique()
    }


# ==========================================================
# REFRESH CACHE
# ==========================================================

def refresh():

    st.cache_data.clear()