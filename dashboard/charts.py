"""
AtmoSync Dashboard Charts
Optimized Version
"""

import streamlit as st

from dashboard.utils import (
    chart_data,
    risk_counts,
    door_status
)


# ==========================================================
# TEMPERATURE
# ==========================================================

def temperature_chart(df):

    st.subheader("🌡 Temperature Trend")

    data = chart_data(df)

    st.line_chart(
        data["temperature_c"],
        height=250
    )


# ==========================================================
# HUMIDITY
# ==========================================================

def humidity_chart(df):

    st.subheader("💧 Humidity")

    data = chart_data(df)

    st.area_chart(
        data["humidity_percent"],
        height=250
    )


# ==========================================================
# BATTERY
# ==========================================================

def battery_chart(df):

    st.subheader("🔋 Battery Level")

    data = chart_data(df)

    st.bar_chart(
        data["battery_percent"],
        height=250
    )


# ==========================================================
# HEALTH SCORE
# ==========================================================

def health_chart(df):

    st.subheader("❤️ Health Score")

    data = chart_data(df)

    st.line_chart(
        data["health_score"],
        height=250
    )


# ==========================================================
# NETWORK SIGNAL
# ==========================================================

def network_chart(df):

    st.subheader("📡 Network Signal")

    data = chart_data(df)

    st.area_chart(
        data["network_signal"],
        height=250
    )


# ==========================================================
# RISK DISTRIBUTION
# ==========================================================

def risk_chart(df):

    st.subheader("🚨 Risk Level Distribution")

    counts = risk_counts(df)

    st.bar_chart(
        counts,
        height=250
    )


# ==========================================================
# DOOR STATUS
# ==========================================================

def door_chart(df):

    st.subheader("🚪 Door Status")

    status = door_status(df)

    st.bar_chart(
        status,
        height=250
    )


# ==========================================================
# DASHBOARD CHARTS
# ==========================================================

def dashboard_charts(df):

    col1, col2 = st.columns(2)

    with col1:
        temperature_chart(df)

    with col2:
        humidity_chart(df)


    st.divider()


    col3, col4 = st.columns(2)

    with col3:
        battery_chart(df)

    with col4:
        health_chart(df)


    st.divider()


    col5, col6 = st.columns(2)

    with col5:
        network_chart(df)

    with col6:
        risk_chart(df)


    st.divider()


    door_chart(df)