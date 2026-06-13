import streamlit as st
import plotly.express as px
import pandas as pd
from insights import generate_insights
from india_map import create_state_map

def show_page(df):

    st.title("🇮🇳 Election War Room")

    st.markdown("""
                ### Election Intelligence Dashboard

                Interactive analysis of India's 2024 General Elections.
                Explore party dominance, state intelligence, candidate performance and constituency-level insights.
                """)

    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown(f"""
                    <div class="metric-card">
                    <h2>{len(df):,}</h2>
                    <p>Total Constituencies</p>
                    </div>
                    """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
                    <div class="metric-card">
                    <h2>{df["State/UT"].nunique()}</h2>
                    <p>States</p>
                    </div>
                    """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
                    <div class="metric-card">
                    <h2>{df["Leading Party"].nunique()}</h2>
                    <p>Parties</p>
                    </div>
                    """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
                    <div class="metric-card">
                    <h2>{int(df['Margin'].mean()):,}</h2>
        <p>Average Margin</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Pre-cast to string before value_counts to ensure the resulting index/column is uniform
    party = df["Leading Party"].astype(str).value_counts().reset_index()
    party.columns = ["Party", "Seats"]
    party["Party"] = party["Party"].astype(str)
    
    col1,col2 = st.columns(2)
    
    with col1:
        
        top10 = party.head(10)
        
        others = pd.DataFrame({
            "Party": ["Others"],
            "Seats": [party.iloc[10:]["Seats"].sum()]})
        
        top10 = pd.concat(
            [top10, others],
            ignore_index=True)
        
        fig = px.pie(
            top10,names="Party",values="Seats",hole=.6)
        
        fig.update_layout(
            height=600,legend_title="Party")
        
        st.plotly_chart(
            fig,use_container_width=True
            )
        
    with col2:
        
        fig = px.treemap(
            party,path=["Party"],values="Seats")
        
        fig.update_layout(
            height=600)
        
        st.plotly_chart(
            fig,use_container_width=True)
        
    st.subheader("India Electoral Landscape")
    fig = create_state_map(df)
    
    st.plotly_chart(
        fig,
        use_container_width=True
        )    
        
    st.subheader("AI Election Insights")
    
    insights = generate_insights(df)
    
    for insight in insights:
        
        st.markdown(
            f"""
            <div class="insight-card">
            {insight}
            </div>
            """,
            unsafe_allow_html=True
            )
        
    st.download_button(
        "⬇ Download Election Data",
        df.to_csv(index=False),
        "election_data.csv",
        "text/csv"
        )