import streamlit as st
import plotly.express as px

def show_page(df):

    st.title("📍 State Intelligence")

    state_summary = (
        df.groupby(df["State/UT"].astype(str))
        .agg(
            Seats=("Constituency","count"),
            Avg_Margin=("Margin","mean")
        )
        .reset_index()
    )

    c1,c2 = st.columns(2)

    with c1:

        fig = px.bar(
            state_summary.sort_values(
                "Seats",
                ascending=False
            ),
            x="State/UT",
            y="Seats",
            text="Seats"
        )

        fig.update_layout(
            height=600,
            xaxis_tickangle=-45
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        fig = px.bar(
            state_summary.sort_values(
                "Avg_Margin",
                ascending=False
            ),
            x="State/UT",
            y="Avg_Margin"
        )

        fig.update_layout(
            height=600,
            xaxis_tickangle=-45
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.subheader("Most Competitive States")

    competitive = (
        df.groupby("State/UT")["Margin"].mean().reset_index().sort_values("Margin"))
    
    fig = px.bar(
        competitive.head(10),
        x="Margin",
        y="State/UT",
        orientation="h")
    
    st.plotly_chart(
        fig,
        use_container_width=True
        )

    st.subheader("State Drilldown")

    competitive = (
        df.groupby("State/UT")["Margin"].mean().reset_index().sort_values("Margin"))
    
    fig = px.bar(
        competitive.head(10),
        x="Margin",
        y="State/UT",
        orientation="h",
        title="Most Competitive States"
        )
    
    st.plotly_chart(
        fig,
        use_container_width=True
        )
    
    state = st.selectbox(
        "Select State",
        sorted(df["State/UT"].astype(str).unique())
        )

    state_df = df[
        df["State/UT"] == state
    ]
    
    c1,c2,c3 = st.columns(3)
    
    c1.metric(
        "Constituencies",
        len(state_df)
        )
    
    c2.metric(
        "Parties",
        state_df["Leading Party"].nunique())
    
    c3.metric(
        "Avg Margin",
        int(state_df["Margin"].mean()))

    st.metric(
        "Seats",
        len(state_df)
    )

    party_breakdown = (
        state_df["Leading Party"].astype(str)
        .value_counts()
        .reset_index()
    )

    party_breakdown.columns = [
        "Party",
        "Seats"
    ]

    fig = px.pie(
        party_breakdown,
        names="Party",
        values="Seats"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        state_df,
        use_container_width=True
    )