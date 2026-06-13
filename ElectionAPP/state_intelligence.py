import streamlit as st
import plotly.express as px

def show_page(df):

    st.title("📍 State Intelligence")

    state_summary = (
        df.groupby("State/UT")
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

    st.subheader("State Drilldown")

    state = st.selectbox(
        "Select State",
        sorted(df["State/UT"].unique())
    )

    state_df = df[
        df["State/UT"] == state
    ]

    st.metric(
        "Seats",
        len(state_df)
    )

    party_breakdown = (
        state_df["Leading Party"]
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