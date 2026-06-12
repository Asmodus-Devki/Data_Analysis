def generate_insights(df):

    largest = (
        df.sort_values(
            "Margin",
            ascending=False
        )
        .iloc[0]
    )

    closest = (
        df.sort_values(
            "Margin"
        )
        .iloc[0]
    )

    top_party = (
        df["Leading Party"]
        .value_counts()
        .idxmax()
    )

    return {
        "largest": largest,
        "closest": closest,
        "top_party": top_party
    }