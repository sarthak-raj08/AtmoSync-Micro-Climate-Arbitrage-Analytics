"""
AtmoSync Dashboard
Professional Edition
"""

import os
import sys
import streamlit as st

# =====================================================
# PROJECT ROOT
# =====================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# =====================================================
# IMPORTS
# =====================================================

from dashboard.config import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT
)

from dashboard.styles import load_css

from dashboard.utils import (
    load_data,
    calculate_health,
    get_metrics,
    latest_records,
    dataset_information
)

from dashboard.components import (
    show_kpi_cards,
    show_alerts,
    show_health_summary,
    show_table,
    show_footer
)

from dashboard.charts import dashboard_charts

from analytics.spoilage_prediction import (
    SpoilagePredictionEngine
)

from analytics.route_optimizer import (
    RouteOptimizer
)

from analytics.arbitrage_engine import (
    ArbitrageEngine
)

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)

load_css()

# =====================================================
# LOAD DATA
# =====================================================

with st.spinner("Loading data from Snowflake..."):

    df = load_data()

df = calculate_health(df)

metrics = get_metrics(df)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🚚 AtmoSync")

page = st.sidebar.radio(
    "Navigation",
    (
        "Dashboard",
        "Analytics",
        "AI Insights",
        "Live Monitoring",
        "Settings"
    )
)
# =====================================================
# DASHBOARD
# =====================================================

if page == "Dashboard":

    st.title("📊 AtmoSync Live Dashboard")

    show_kpi_cards(metrics)

    st.divider()

    show_alerts(df)

    st.divider()

    dashboard_charts(df)

    st.divider()

    show_health_summary(df)

    st.divider()

    st.subheader("📋 Latest Sensor Readings")

    latest_df = latest_records(df)

    show_table(latest_df)

    show_footer()


# =====================================================
# ANALYTICS
# =====================================================

elif page == "Analytics":

    st.title("📈 Advanced Analytics")

    dashboard_charts(df)

    st.divider()

    st.subheader("Container Health Distribution")

    risk = (
        df["risk_level"]
        .value_counts()
        .reset_index()
    )

    risk.columns = [
        "Risk Level",
        "Count"
    ]

    st.dataframe(
    risk,
    width="stretch"
)

    st.divider()

    st.subheader("Latest 100 Records")

    show_table(df.head(100))

    show_footer()
    # =====================================================
# AI INSIGHTS
# =====================================================

elif page == "AI Insights":

    st.title("🤖 AI Insights")

    spoilage = SpoilagePredictionEngine()

    optimizer = RouteOptimizer()

    arbitrage = ArbitrageEngine()

    latest = latest_records(df, 1).iloc[0].to_dict()

    spoilage_result = spoilage.predict(latest)

    route_result = optimizer.optimize(latest)

    # Temporary product until sensor data contains product name

    product = "Tomato"

    arbitrage_result = arbitrage.find_best_market(product)

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Spoilage Probability",
            f"{spoilage_result['spoilage_probability']}%"
        )

        st.metric(
            "Spoilage Status",
            spoilage_result["spoilage_status"]
        )

    with col2:

        st.metric(
            "Priority",
            route_result["priority"]
        )

        st.write(
            route_result["recommended_action"]
        )

    st.divider()

    st.subheader("Market Recommendation")

    st.metric(
        "Best Market",
        arbitrage_result["best_market"]
    )

    st.metric(
        "Market Price",
        f"${arbitrage_result['market_price']:.2f}/kg"
    )

    st.metric(
        "Demand Index",
        arbitrage_result["demand_index"]
    )

    st.metric(
        "Supply Index",
        arbitrage_result["supply_index"]
    )

    st.success(
        arbitrage_result["recommendation"]
    )

    show_footer()
    # =====================================================
# LIVE MONITORING
# =====================================================

elif page == "Live Monitoring":

    st.title("📡 Live Monitoring")

    st.success("Connected to Snowflake")

    latest = latest_records(df, rows=50)

    st.subheader("Latest Sensor Data")

    show_table(latest)

    st.divider()

    dashboard_charts(latest)

    st.info(f"Showing latest {len(latest)} sensor readings.")

    show_footer()


# =====================================================
# SETTINGS
# =====================================================

elif page == "Settings":

    st.title("⚙️ Dashboard Settings")

    info = dataset_information(df)

    st.subheader("Project Information")

    col1, col2 = st.columns(2)

    with col1:

        st.metric("Rows", info["rows"])

        st.metric("Containers", info["containers"])

        st.metric("Shipments", info["shipments"])

    with col2:

        st.metric("Columns", info["columns"])

        st.metric("Routes", info["routes"])

        st.metric(
            "Average Health",
            f"{metrics['avg_health']:.2f}"
        )

    st.divider()

    st.subheader("System Status")

    st.success("✅ Snowflake Connected")

    st.success("✅ Dashboard Running")

    st.success("✅ Health Score Engine Loaded")

    st.success("✅ Route Optimizer Loaded")

    st.success("✅ Spoilage Prediction Loaded")

    st.success("✅ Arbitrage Engine Loaded")

    st.success("✅ Charts Loaded")

    st.success("✅ Components Loaded")

    st.divider()

    if st.button("🔄 Refresh Dashboard"):

        st.cache_data.clear()

        st.rerun()

    show_footer()