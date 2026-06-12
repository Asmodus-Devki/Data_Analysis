import plotly.express as px

def seat_share_chart(df):

    party = (
        df["Leading Party"]
        .value_counts()
        .reset_index()
    )

    party.columns = [
        "Party",
        "Seats"
    ]

    return px.pie(
        party,
        names="Party",
        values="Seats",
        hole=.55
    )