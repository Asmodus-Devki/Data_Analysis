import streamlit as st
import plotly.express as px
from insights import generate_insights

def show_page(df):

    st.title("🇮🇳 Election War Room")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Constituencies",
        len(df)
    )

    c2.metric(
        "States",
        df["State/UT"].nunique()
    )

    c3.metric(
        "Parties",
        df["Leading Party"].nunique()
    )

    c4.metric(
        "Avg Margin",
        f"{int(df['Margin'].mean()):,}"
    )

    party = (
        df["Leading Party"]
        .value_counts()
        .reset_index()
    )

    party.columns = [
        "Party",
        "Seats"
    ]

    col1,col2 = st.columns(2)

    with col1:

        fig = px.pie(
            party.head(15),
            names="Party",
            values="Seats",
            hole=.6
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        fig = px.treemap(
            party,
            path=["Party"],
            values="Seats"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    insights = generate_insights(df)

    st.success(
        f"Top Party: {insights['top_party']}"
    )