import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Import your existing logic if it contains specific analysis functions
# from EconomicSalesAnalysisProject import your_analysis_function

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Economic Sales Analysis | AI Mastery",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- BEAUTIFUL CUSTOM CSS ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(30, 41, 59, 0.7) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Metric Cards */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.3s ease;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        border-color: #38bdf8;
    }

    /* Headers */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(to right, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        color: white;
        padding: 0 20px;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MOCK DATA LOADING (Replace with EconomicSalesAnalysisProject logic) ---
@st.cache_data
def get_economic_data():
    # This is where you would call functions from EconomicSalesAnalysisProject.py
    # Example: return load_and_clean_data()
    data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
        'Revenue': [45000, 52000, 49000, 61000, 58000, 72000, 81000, 78000],
        'Forecast': [42000, 50000, 51000, 58000, 60000, 70000, 79000, 82000],
        'Inflation_Rate': [2.1, 2.3, 2.5, 2.4, 2.2, 2.1, 2.0, 1.9]
    })
    return data

df = get_economic_data()

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3141/3141158.png", width=80)
    st.title("AI Mastery Hub")
    st.markdown("---")
    analysis_type = st.radio("Analysis View", ["Overview", "Revenue Forecast", "Economic Impact"])
    st.info("The logic for this dashboard is powered by `EconomicSalesAnalysisProject.py`")

# --- MAIN INTERFACE ---
st.title("💰 Economic Sales Analysis")
st.markdown("#### Advanced Insights & Financial Projections")

if analysis_type == "Overview":
    # --- ROW 1: KPI METRICS ---
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total YTD Revenue", "$491,000", delta="12%")
    with col2:
        st.metric("Avg. Monthly Sales", "$61,375", delta="4.5%")
    with col3:
        st.metric("Projected Growth", "18.2%", delta="2.1%")
    with col4:
        st.metric("Economic Volatility", "Low", delta="-0.4%", delta_color="inverse")

    st.markdown("---")
    
    col_a, col_b = st.columns(2)
    with col_a:
        fig_pie = px.pie(names=['North', 'South', 'East', 'West'], values=[25, 35, 20, 20], hole=0.6)
        fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), title="Regional Sales")
        st.plotly_chart(fig_pie, use_container_width=True)
    with col_b:
        st.write("### Market Summary")
        st.write("- **South Region** leads performance.\ - **Growth** is steady despite inflation.")

elif analysis_type == "Revenue Forecast":
    st.subheader("Revenue vs Economic Forecast")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Month'], y=df['Revenue'], fill='tozeroy', name='Actual Revenue', line=dict(width=4, color='#38bdf8')))
    fig.add_trace(go.Scatter(x=df['Month'], y=df['Forecast'], name='Economic Forecast', line=dict(width=3, color='#818cf8', dash='dot')))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
    st.plotly_chart(fig, use_container_width=True)

elif analysis_type == "Economic Impact":
    st.subheader("Inflation Rate Correlation")
    fig_impact = px.bar(df, x='Month', y='Inflation_Rate', color='Inflation_Rate', color_continuous_scale='RdYlGn_r')
    fig_impact.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
    st.plotly_chart(fig_impact, use_container_width=True)
    st.info("Higher inflation rates in Q1-Q2 correlate with conservative forecasting.")

# --- ROW 3: DATA INSPECTION ---
with st.expander("🔍 View Raw Analysis Data"):
    st.dataframe(df.style.background_gradient(cmap='Blues'), use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.caption("v2.1.0 | AI Mastery Engineering")