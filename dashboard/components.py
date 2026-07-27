"""
AtmoSync Dashboard Components
-----------------------------
Reusable UI components for Streamlit.
"""

import streamlit as st
import pandas as pd


# ==========================================================
# KPI CARDS
# ==========================================================

def show_kpi_cards(metrics):

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📡 Sensors",
        metrics["sensors"]
    )

    c2.metric(
        "📦 Containers",
        metrics["containers"]
    )

    c3.metric(
        "🚚 Shipments",
        metrics["shipments"]
    )

    c4.metric(
        "❤️ Average Health",
        metrics["avg_health"]
    )


# ==========================================================
# ALERT BOX
# ==========================================================

def show_alerts(df):

    critical = len(
        df[df["risk_level"] == "CRITICAL"]
    )

    high = len(
        df[df["risk_level"] == "HIGH"]
    )

    if critical > 0:

        st.error(
            f"🚨 {critical} containers are in CRITICAL condition!"
        )

    elif high > 0:

        st.warning(
            f"⚠️ {high} containers require attention."
        )

    else:

        st.success(
            "✅ All containers are operating normally."
        )


# ==========================================================
# HEALTH SUMMARY
# ==========================================================

def show_health_summary(df):

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Highest Health",
        int(df["health_score"].max())
    )

    c2.metric(
        "Lowest Health",
        int(df["health_score"].min())
    )

    c3.metric(
        "Average Health",
        round(df["health_score"].mean(), 2)
    )


# ==========================================================
# DATA TABLE
# ==========================================================

def show_table(df):

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )


# ==========================================================
# CONTAINER INFO
# ==========================================================

def show_container_info(df):

    if df.empty:

        st.warning("No container selected.")

        return

    latest = df.iloc[-1]

    st.subheader("📦 Container Information")

    c1, c2 = st.columns(2)

    with c1:

        st.write(
            f"**Container ID:** {latest['container_id']}"
        )

        st.write(
            f"**Shipment ID:** {latest['shipment_id']}"
        )

        st.write(
            f"**Route ID:** {latest['route_id']}"
        )

    with c2:

        st.write(
            f"**Temperature:** {latest['temperature_c']} °C"
        )

        st.write(
            f"**Humidity:** {latest['humidity_percent']} %"
        )

        st.write(
            f"**Battery:** {latest['battery_percent']} %"
        )

        st.write(
            f"**Risk:** {latest['risk_level']}"
        )


# ==========================================================
# PAGE FOOTER
# ==========================================================

def show_footer():

    st.divider()

    st.caption(
        "AtmoSync • Micro-Climate Arbitrage Analytics Platform"
    )