def generate_insights(df):

    top_party = (
        df["Leading Party"]
        .value_counts()
        .idxmax()
    )

    top_party_seats = (
        df["Leading Party"]
        .value_counts()
        .max()
    )

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

    largest_state = (
        df["State/UT"]
        .value_counts()
        .idxmax()
    )

    insights = []

    insights.append(
        f"{top_party} emerged as the leading party with {top_party_seats} seats."
    )

    insights.append(
        f"{largest_state} remains the most influential electoral state."
    )

    insights.append(
        f"The closest contest was decided by only {int(closest['Margin']):,} votes."
    )

    insights.append(
        f"The biggest victory margin was {int(largest['Margin']):,} votes."
    )

    return insights