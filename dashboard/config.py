"""
AtmoSync Dashboard Configuration
--------------------------------
Central configuration for the Streamlit dashboard.
"""

import os

# =====================================================
# PROJECT ROOT
# =====================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

# =====================================================
# DATA PATHS
# =====================================================

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "raw")

SENSOR_DATA = os.path.join(
    DATA_DIR,
    "container_sensor_data.csv"
)

COMMODITY_DATA = os.path.join(
    DATA_DIR,
    "commodity_prices.csv"
)

# =====================================================
# PERFORMANCE SETTINGS
# =====================================================

# Maximum rows loaded from CSV
MAX_ROWS = 1000

# Rows used for charts
CHART_ROWS = 300

# Rows shown in latest records table
LATEST_RECORDS = 20

# =====================================================
# DASHBOARD
# =====================================================

PAGE_TITLE = "AtmoSync Dashboard"

PAGE_ICON = "🚚"

LAYOUT = "wide"

SIDEBAR = "expanded"

# =====================================================
# COLORS
# =====================================================

LOW_COLOR = "#4CAF50"

MEDIUM_COLOR = "#FFC107"

HIGH_COLOR = "#FF9800"

CRITICAL_COLOR = "#F44336"

# =====================================================
# KPI TITLES
# =====================================================

KPI_SENSORS = "Sensors"

KPI_CONTAINERS = "Containers"

KPI_SHIPMENTS = "Shipments"

KPI_HEALTH = "Average Health"

# =====================================================
# REFRESH
# =====================================================

AUTO_REFRESH_SECONDS = 5