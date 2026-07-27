"""
AtmoSync Dashboard Styles
-------------------------
Custom CSS for Streamlit Dashboard
"""

import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* Main Page */

        .main{
            background-color:#f7f9fc;
        }

        /* Sidebar */

        section[data-testid="stSidebar"]{
            background:#20263a;
            color:white;
        }

        section[data-testid="stSidebar"] *{
            color:white;
        }

        /* KPI Cards */

        div[data-testid="metric-container"]{

            background:white;

            border-radius:15px;

            padding:18px;

            box-shadow:0px 3px 12px rgba(0,0,0,0.08);

            border-left:6px solid #4CAF50;
        }

        div[data-testid="metric-container"] label{

            font-size:16px;

            font-weight:bold;
        }

        div[data-testid="metric-container"] div{

            font-size:24px;

            font-weight:bold;
        }

        /* Buttons */

        .stButton>button{

            width:100%;

            border-radius:12px;

            background:#4CAF50;

            color:white;

            border:none;

            font-weight:bold;

            padding:10px;
        }

        .stButton>button:hover{

            background:#388E3C;

            color:white;
        }

        /* Tables */

        .stDataFrame{

            border-radius:10px;

            overflow:hidden;
        }

        /* Headers */

        h1{

            color:#1f2937;
        }

        h2{

            color:#374151;
        }

        h3{

            color:#374151;
        }

        </style>
        """,
        unsafe_allow_html=True
    )