import streamlit as st
import plotly.express as px
from party_colors import PARTY_COLORS

def show_page(df):

    st.title("🏛 Party Command Center")

    party_summary = (
        df.groupby(df["Leading Party"].astype(str))
        .agg(
            Seats=("Leading Party","count"),
            Avg_Margin=("Margin","mean")
        )
        .reset_index()
        .sort_values(
            "Seats",
            ascending=False
        )
    )

    c1,c2 = st.columns(2)

    with c1:

        fig = px.bar(
            party_summary.head(15),
            x="Seats",
            y="Leading Party",
            orientation="h",
            color="Leading Party",
            color_discrete_map=PARTY_COLORS
            )

        fig.update_layout(
            height=600,
            yaxis={
                "categoryorder":"total ascending"
            }
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        fig = px.scatter(
            party_summary,
            x="Seats",
            y="Avg_Margin",
            size="Seats",
            color="Leading Party",
            hover_name="Leading Party"
        )

        fig.update_layout(
            height=600
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.subheader("Party Dominance")
    
    fig = px.treemap(
        party_summary,
        path=["Leading Party"],
        values="Seats",
        color="Seats"
        )
    
    st.plotly_chart(
        fig,
        use_container_width=True
        )

    st.subheader("Party Comparison")

    parties = sorted(
        df["Leading Party"]
        .astype(str)
        .unique()
    )

    col1,col2 = st.columns(2)

    party_a = col1.selectbox(
        "Party A",
        parties
    )

    party_b = col2.selectbox(
        "Party B",
        parties,
        index=1
    )

    a_df = df[
        df["Leading Party"] == party_a
    ]

    b_df = df[
        df["Leading Party"] == party_b
    ]

    compare = {
        "Metric":[
            "Seats Won",
            "Average Margin"
        ],
        party_a:[
            len(a_df),
            int(a_df["Margin"].mean())
        ],
        party_b:[
            len(b_df),
            int(b_df["Margin"].mean())
        ]
    }

    st.dataframe(
        compare,
        use_container_width=True
    )