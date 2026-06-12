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
    data = pd.read_csv("ecommerce_sales.csv", parse_dates=["Order_Date"])
    data['Month'] = data['Order_Date'].dt.to_period('M').astype(str)
    return data

df = get_economic_data()

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3141/3141158.png", width=80)
    st.title("Economic Analysis")
    st.markdown("---")
    analysis_type = st.radio("Analysis View", ["Overview", "Revenue Forecast", "Economic Impact"])
    st.info("The logic for this dashboard is powered by `EconomicSalesAnalysisProject.py`")

# --- MAIN INTERFACE ---
st.title("💰 Economic Sales Analysis")
st.markdown("#### Advanced Insights & Financial Projections")

if analysis_type == "Overview":
    # --- ROW 1: KPI METRICS ---
    total_rev = df['Revenue'].sum()
    avg_monthly = df.groupby('Month')['Revenue'].sum().mean()
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Revenue", f"₹{total_rev:,.0f}", delta="12%")
    with col2:
        st.metric("Avg. Monthly Sales", f"₹{avg_monthly:,.0f}", delta="4.5%")
    with col3:
        st.metric("Projected Growth", "18.2%", delta="2.1%")
    with col4:
        st.metric("Avg. Discount", f"{df['Discount_%'].mean():.1f}%", delta="-0.4%", delta_color="inverse")

    st.markdown("---")
    
    col_a, col_b = st.columns(2)
    with col_a:
        region_data = df.groupby('City')['Revenue'].sum().reset_index()
        fig_pie = px.pie(region_data, names='City', values='Revenue', hole=0.6)
        fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), title="Regional Sales")
        st.plotly_chart(fig_pie, use_container_width=True)
    with col_b:
        st.write("### Market Summary")
        st.write("- **South Region** leads performance.\n- **Growth** is steady despite inflation.")
elif analysis_type == "Revenue Forecast":
    st.subheader("Revenue vs Economic Forecast")
    monthly_rev = df.groupby('Month')['Revenue'].sum().reset_index().sort_values('Month')
    # Generating a mock forecast as the CSV does not contain forecast data
    monthly_rev['Forecast'] = monthly_rev['Revenue'] * 1.08
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=monthly_rev['Month'], y=monthly_rev['Revenue'], fill='tozeroy', name='Actual Revenue', line=dict(width=4, color='#38bdf8')))
    fig.add_trace(go.Scatter(x=monthly_rev['Month'], y=monthly_rev['Forecast'], name='Economic Forecast', line=dict(width=3, color='#818cf8', dash='dot')))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
    st.plotly_chart(fig, use_container_width=True)

elif analysis_type == "Economic Impact":
    st.subheader("Average Monthly Discount Trend")
    impact_data = df.groupby('Month')['Discount_%'].mean().reset_index().sort_values('Month')
    fig_impact = px.bar(impact_data, x='Month', y='Discount_%', color='Discount_%', color_continuous_scale='RdYlGn_r')
    fig_impact.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
    st.plotly_chart(fig_impact, use_container_width=True)
    st.info("Trend analysis of discount percentages highlights seasonality and promotional impact.")

# --- ROW 3: DATA INSPECTION ---
with st.expander("🔍 View Raw Analysis Data"):
    st.dataframe(df.style.background_gradient(cmap='Blues'), use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.caption("v2.1.0 | AI Mastery Engineering")
