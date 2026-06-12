import streamlit as st
import plotly.express as px

def show_page(df):

    st.title("🎯 Candidate Intelligence")

    winners = (
        df.sort_values(
            "Margin",
            ascending=False
        )
        .head(20)
    )

    closest = (
        df.sort_values(
            "Margin"
        )
        .head(20)
    )

    c1,c2 = st.columns(2)

    with c1:

        fig = px.bar(
            winners,
            x="Margin",
            y="Leading Candidate",
            orientation="h",
            color="Leading Party"
        )

        fig.update_layout(
            height=700
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        st.dataframe(
            closest[
                [
                    "Leading Candidate",
                    "Leading Party",
                    "Constituency",
                    "Margin"
                ]
            ],
            use_container_width=True,
            height=700
        )

    st.subheader("Candidate Search")

    candidate = st.selectbox(
        "Choose Candidate",
        sorted(
            df["Leading Candidate"]
            .unique()
        )
    )

    row = df[
        df["Leading Candidate"]
        == candidate
    ].iloc[0]

    st.dataframe(
        row.to_frame(),
        use_container_width=True
    )