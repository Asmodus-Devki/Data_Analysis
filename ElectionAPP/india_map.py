import json
import plotly.express as px


def create_state_map(df):

    with open(
        "india_states.geojson",
        "r",
        encoding="utf-8"
    ) as f:

        geojson = json.load(f)

    # State name mapping
    state_mapping = {

        "Andaman & Nicobar Islands":
            "Andaman and Nicobar",

        "NCT OF Delhi":
            "Delhi",

        "Jammu & Kashmir":
            "Jammu and Kashmir",

        "Dadra & Nagar Haveli and Daman & Diu":
            "Dadra and Nagar Haveli",

        "Odisha":
            "Orissa"
    }

    map_df = df.copy()

    map_df["State/UT"] = (
        map_df["State/UT"]
        .replace(state_mapping)
        .astype(str)
    )

    state_summary = (
        map_df.groupby("State/UT")
        .size()
        .reset_index(name="Seats")
    )

    fig = px.choropleth(
        state_summary,
        geojson=geojson,
        locations="State/UT",
        featureidkey="properties.NAME_1",
        color="Seats",
        hover_name="State/UT",
        color_continuous_scale="Viridis"
    )

    fig.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig.update_layout(
        height=700,
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),
        paper_bgcolor="#081120",
        plot_bgcolor="#081120"
    )

    return fig