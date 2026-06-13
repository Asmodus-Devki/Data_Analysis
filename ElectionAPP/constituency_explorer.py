import streamlit as st

def show_page(df):

    st.title("🔍 Constituency Explorer")

    constituency = st.selectbox(
        "Select Constituency",
        sorted(
            df["Constituency"]
            .astype(str)
            .unique()
        )
    )

    row = df[
        df["Constituency"]
        == constituency
    ].iloc[0]

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Winner",
        row["Leading Candidate"]
    )

    c2.metric(
        "Party",
        row["Leading Party"]
    )

    c3.metric(
        "Margin",
        f"{int(row['Margin']):,}"
    )

    c4.metric(
        "Status",
        row["Status"]
    )

    st.dataframe(
        row.to_frame(),
        use_container_width=True
    )

    st.download_button(
        "Download Constituency Data",
        row.to_csv(),
        file_name=f"{constituency}.csv"
    )