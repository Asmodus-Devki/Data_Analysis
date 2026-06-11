import pandas as pd
import altair as alt
import streamlit as st


st.set_page_config(
    page_title="India Election Campaign Intelligence",
    page_icon="IN",
    layout="wide",
    initial_sidebar_state="expanded",
)


PARTY_COLORS = {
    "BJP (NDA)": "#ff7a1a",
    "Congress (INDIA)": "#2f6fed",
    "SP (INDIA)": "#d94848",
    "TMC (INDIA)": "#1f9d76",
    "DMK (INDIA)": "#111827",
    "TDP (NDA)": "#ffd166",
    "JDU (NDA)": "#2bb3ff",
    "CPI(M)": "#b91c1c",
    "Others / Ind.": "#8b5cf6",
}

ALLIANCE_COLORS = {
    "NDA": "#ff7a1a",
    "INDIA": "#2f6fed",
    "Others": "#8b5cf6",
}


@st.cache_data
def load_data():
    party = pd.DataFrame(
        [
            ["BJP (NDA)", "NDA", 441, 240, 36.56, -3.4, "Majority"],
            ["Congress (INDIA)", "INDIA", 328, 99, 21.19, 2.9, "Gain"],
            ["SP (INDIA)", "INDIA", 80, 37, 9.24, 4.1, "Gain"],
            ["TMC (INDIA)", "INDIA", 48, 29, 7.01, 0.8, "Stable"],
            ["DMK (INDIA)", "INDIA", 23, 22, 3.26, -0.2, "Stable"],
            ["TDP (NDA)", "NDA", 17, 16, 2.68, 1.4, "Gain"],
            ["Shiv Sena UBT", "INDIA", 21, 9, 1.53, None, "New"],
            ["NCP (SP) Pawar", "INDIA", 10, 8, 1.11, None, "New"],
            ["JDU (NDA)", "NDA", 16, 12, 1.58, 0.3, "Stable"],
            ["CPI(M)", "INDIA", 51, 4, 2.10, -0.6, "Loss"],
            ["Others / Ind.", "Others", None, 67, 13.74, None, "Mixed"],
        ],
        columns=[
            "Party / Alliance",
            "Alliance",
            "Seats Contested",
            "Seats Won",
            "Vote Share (%)",
            "Swing vs 2019",
            "Status",
        ],
    )

    spending = pd.DataFrame(
        [
            ["BJP", 75000, 45000, 66.7, 312.5, "TV + Digital + Rallies"],
            ["Congress", 18000, 9500, 89.5, 181.8, "Digital + Print"],
            ["SP", 4200, 2100, 100.0, 113.5, "Ground + Social Media"],
            ["TMC", 5600, 3800, 47.4, 193.1, "Print + TV"],
            ["DMK", 3100, 2400, 29.2, 140.9, "Regional TV + Ground"],
            ["BSP", 800, 1200, -33.3, None, "Ground Mobilisation"],
            ["AAP", 2400, None, None, None, "Digital + Outdoor"],
            ["NDA Others", 12000, 7000, 71.4, None, "Regional Mix"],
        ],
        columns=[
            "Party",
            "2024 Spend (Cr)",
            "2019 Spend (Cr)",
            "YoY Growth (%)",
            "Spend per Seat Won (Cr)",
            "Primary Channel",
        ],
    )

    bjp_channels = pd.DataFrame(
        [
            ["Television Advertising", 28, 21000, "Prime-time ads, debates, news sponsorships"],
            ["Digital & Social Media", 22, 16500, "Meta, YouTube, WhatsApp campaign networks"],
            ["Public Rallies & Events", 20, 15000, "PM rallies, roadshows, nukkad sabhas"],
            ["Print Media", 10, 7500, "National and regional newspaper insertions"],
            ["Outdoor & Hoardings", 9, 6750, "Billboards, banners, wall paintings"],
            ["Ground Mobilisation", 7, 5250, "Booth management and worker incentives"],
            ["Opinion & Exit Polls", 2, 1500, "Surveys and data analytics"],
            ["Miscellaneous", 2, 1500, "Administration, logistics, printing"],
        ],
        columns=["Campaign Channel", "Allocation (%)", "Approx. Spend (Cr)", "Key Activity"],
    )

    turnout = pd.DataFrame(
        [
            ["Uttar Pradesh", 152.8, 91.2, 59.7, 59.1, 0.6],
            ["Maharashtra", 91.7, 52.3, 57.1, 60.5, -3.4],
            ["West Bengal", 73.9, 60.1, 81.3, 82.5, -1.2],
            ["Bihar", 74.3, 49.4, 56.5, 57.3, -0.8],
            ["Tamil Nadu", 61.9, 45.9, 74.2, 72.4, 1.8],
            ["Rajasthan", 51.8, 36.8, 71.0, 64.1, 6.9],
            ["Madhya Pradesh", 55.9, 41.4, 74.1, 71.2, 2.9],
            ["Gujarat", 49.2, 31.4, 63.9, 63.7, 0.2],
            ["Karnataka", 54.2, 38.2, 70.5, 68.0, 2.5],
            ["Kerala", 27.0, 20.4, 75.5, 77.7, -2.2],
            ["Delhi", 15.0, 8.4, 55.9, 60.6, -4.7],
            ["Assam", 22.4, 16.7, 74.7, 79.1, -4.4],
        ],
        columns=[
            "State",
            "Registered Voters (Mn)",
            "Votes Polled (Mn)",
            "Turnout (%)",
            "2019 Turnout (%)",
            "Change",
        ],
    )

    demographics = pd.DataFrame(
        [
            ["Youth 18-35", 34, 38, 22, 40, "Employment & Education"],
            ["Women Voters", 48, 42, 24, 34, "Safety & Welfare Schemes"],
            ["Senior Citizens 60+", 12, 44, 27, 29, "Healthcare & Pension"],
            ["First-time Voters", 6, 35, 25, 40, "Future Opportunities"],
            ["OBC Community", 41, 45, 20, 35, "Reservation & Welfare"],
            ["SC/ST Voters", 26, 36, 28, 36, "Rights & Schemes"],
            ["Urban Professionals", 15, 40, 30, 30, "Economy & Governance"],
            ["Rural Farmers", 45, 37, 23, 40, "MSP & Irrigation"],
        ],
        columns=[
            "Voter Segment",
            "Share of Electorate (%)",
            "BJP Lean (%)",
            "Congress Lean (%)",
            "Regional Party (%)",
            "Key Issue",
        ],
    )

    social = pd.DataFrame(
        [
            ["Twitter / X", 22.4, 9.8, 1.2, 2.1],
            ["Facebook", 18.6, 7.4, 0.9, 1.8],
            ["Instagram", 11.2, 5.6, 0.6, 0.8],
            ["YouTube", 6.8, 2.9, 0.3, 0.5],
            ["Koo", 2.1, 1.4, 0.0, 0.4],
        ],
        columns=["Platform", "BJP", "Congress", "SP", "TMC"],
    )

    digital_ads = pd.DataFrame(
        [
            ["BJP", 820, 1240, 48.6, 34.2, "Modi Guarantee / Viksit Bharat"],
            ["Congress", 310, 480, 18.4, 31.7, "Nyay Patra / Constitution"],
            ["SP", 80, 140, 6.2, 29.8, "PDA + Farmer Rights"],
            ["TMC", 120, 190, 7.9, 32.1, "Banglar Meye / Bengal Pride"],
            ["DMK", 95, 160, 6.1, 30.4, "Tamil Identity + Welfare"],
            ["AAP", 180, 240, 9.3, 33.1, "Kejriwal Guarantee / Delhi Model"],
        ],
        columns=[
            "Party",
            "Google Ads Spend (Cr)",
            "Meta Ads Spend (Cr)",
            "Total Impressions (Bn)",
            "CPM Avg",
            "Top Message Theme",
        ],
    )
    digital_ads["Total Digital Spend (Cr)"] = (
        digital_ads["Google Ads Spend (Cr)"] + digital_ads["Meta Ads Spend (Cr)"]
    )

    zones = pd.DataFrame(
        [
            ["North", "UP, Bihar, MP, Rajasthan, Haryana", 225, 142, 74, 9, "NDA", "Modi + Welfare"],
            ["West", "Maharashtra, Gujarat, Goa", 68, 38, 24, 6, "NDA", "Business + Development"],
            ["South", "TN, Kerala, AP, Telangana, Karnataka", 129, 31, 74, 24, "INDIA", "Regional Identity"],
            ["East", "WB, Odisha, Jharkhand", 74, 24, 40, 10, "INDIA", "Welfare + Anti-BJP"],
            ["NE & J&K", "8 NE states + J&K + Ladakh", 47, 32, 8, 7, "NDA", "Security + Development"],
        ],
        columns=[
            "Zone",
            "States",
            "Total Seats",
            "NDA Won",
            "INDIA Won",
            "Others",
            "Zone Winner",
            "Key Narrative",
        ],
    )

    constituencies = pd.DataFrame(
        [
            ["Varanasi", "UP", "Narendra Modi", "BJP", 152513, 54.7, 35],
            ["Amethi", "UP", "Smriti Irani", "BJP", 55120, 52.3, 12],
            ["Wayanad", "Kerala", "Rahul Gandhi", "INC", 364422, 73.2, 8],
            ["Raebareli", "UP", "Rahul Gandhi", "INC", 390030, 53.1, 10],
            ["Chandni Chowk", "Delhi", "Praveen Khandelwal", "BJP", 110347, 54.8, 9],
            ["Begusarai", "Bihar", "Giriraj Singh", "BJP", 47505, 56.7, 7],
            ["Baramati", "Maharashtra", "Supriya Sule", "NCP(SP)", 158333, 67.1, 11],
            ["Thiruvananthapuram", "Kerala", "Shashi Tharoor", "INC", 16077, 74.5, 6],
            ["Surat", "Gujarat", "Mukesh Dalal", "BJP", None, None, 5],
            ["Indore", "MP", "Shankar Lalwani", "BJP", 1175092, 72.9, 14],
        ],
        columns=[
            "Constituency",
            "State",
            "Winner",
            "Party",
            "Margin (Votes)",
            "Turnout (%)",
            "Campaign Spend (Cr)",
        ],
    )

    recommendations = pd.DataFrame(
        [
            [1, "Build real-time booth-level data pipelines integrating voter rolls and GOTV tracking", "Critical", "Ground Ops", "Immediate"],
            [2, "Invest in vernacular digital content across 12+ language micro-targeting campaigns", "High", "Digital Reach", "90 Days"],
            [3, "Use AI-powered sentiment analysis across WhatsApp and regional social media", "High", "Message Strategy", "60 Days"],
            [4, "Standardise candidate CRM systems for volunteer and donor tracking", "Medium", "Org Efficiency", "6 Months"],
            [5, "Commission caste and demographic surveys in 80 marginal constituencies", "High", "Intel & Analytics", "45 Days"],
            [6, "Establish cross-platform ad attribution model to optimise channel ROI", "Medium", "Expenditure ROI", "3 Months"],
        ],
        columns=["#", "Recommendation", "Priority", "Impact Area", "Timeline"],
    )

    return {
        "party": party,
        "spending": spending,
        "bjp_channels": bjp_channels,
        "turnout": turnout,
        "demographics": demographics,
        "social": social,
        "digital_ads": digital_ads,
        "zones": zones,
        "constituencies": constituencies,
        "recommendations": recommendations,
    }


def apply_theme():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        :root {
            --ink: #101828;
            --muted: #667085;
            --line: #e4e7ec;
            --paper: #f7f8fb;
            --saffron: #ff7a1a;
            --blue: #2f6fed;
            --green: #16a34a;
        }
        html, body, [class*="css"] {
            font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(255, 122, 26, .12), transparent 28rem),
                linear-gradient(180deg, #fbfcff 0%, #f2f5f9 100%);
            color: var(--ink);
        }
        section[data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 1px solid var(--line);
        }
        .hero {
            padding: 2rem 2.2rem;
            border: 1px solid rgba(16, 24, 40, .08);
            background: linear-gradient(135deg, #111827 0%, #1f2937 42%, #f97316 120%);
            color: white;
            border-radius: 8px;
            box-shadow: 0 24px 60px rgba(16, 24, 40, .15);
        }
        .hero h1 {
            font-size: 2.5rem;
            line-height: 1.05;
            letter-spacing: 0;
            margin: 0 0 .75rem 0;
        }
        .hero p {
            max-width: 70rem;
            color: rgba(255,255,255,.84);
            font-size: 1.02rem;
            margin: 0;
        }
        .section-title {
            margin-top: 1.5rem;
            margin-bottom: .6rem;
            font-size: 1.15rem;
            font-weight: 800;
            color: #111827;
        }
        .metric-card {
            background: rgba(255,255,255,.88);
            border: 1px solid rgba(16,24,40,.08);
            border-radius: 8px;
            padding: 1rem 1.1rem;
            box-shadow: 0 14px 36px rgba(16,24,40,.08);
            min-height: 112px;
        }
        .metric-label {
            color: #667085;
            font-size: .78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: .05em;
            margin-bottom: .55rem;
        }
        .metric-value {
            font-size: 1.7rem;
            font-weight: 800;
            color: #111827;
            line-height: 1.05;
        }
        .metric-note {
            color: #667085;
            font-size: .83rem;
            margin-top: .45rem;
        }
        .insight {
            border-left: 4px solid #ff7a1a;
            background: #fff7ed;
            padding: .95rem 1rem;
            border-radius: 0 8px 8px 0;
            color: #7c2d12;
            margin: .5rem 0 1rem 0;
        }
        .priority-critical {border-left: 4px solid #dc2626;}
        .priority-high {border-left: 4px solid #f97316;}
        .priority-medium {border-left: 4px solid #2f6fed;}
        div[data-testid="stDataFrame"] {
            border: 1px solid var(--line);
            border-radius: 8px;
            overflow: hidden;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: .35rem;
        }
        .stTabs [data-baseweb="tab"] {
            background: white;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: .55rem .85rem;
        }
        .stTabs [aria-selected="true"] {
            border-color: #ff7a1a;
            color: #c2410c;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def metric_card(label, value, note=""):
    st.markdown(
        f"""
        <div class="metric-card">
          <div class="metric-label">{label}</div>
          <div class="metric-value">{value}</div>
          <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def insight(text):
    st.markdown(f'<div class="insight"><b>Campaign intelligence:</b> {text}</div>', unsafe_allow_html=True)


def chart_theme(chart, height=420):
    return (
        chart.properties(height=height)
        .configure_view(strokeWidth=0)
        .configure_axis(
            labelColor="#475467",
            titleColor="#344054",
            gridColor="#eaecf0",
            domain=False,
            tickColor="#d0d5dd",
        )
        .configure_legend(
            labelColor="#344054",
            titleColor="#344054",
            orient="top",
            symbolType="circle",
        )
        .configure_title(color="#111827", fontSize=16, anchor="start", fontWeight=800)
    )


data = load_data()
apply_theme()

party = data["party"]
spending = data["spending"]
bjp_channels = data["bjp_channels"]
turnout = data["turnout"]
demographics = data["demographics"]
social = data["social"]
digital_ads = data["digital_ads"]
zones = data["zones"]
constituencies = data["constituencies"]
recommendations = data["recommendations"]


with st.sidebar:
    st.caption("Campaign Analytics Division")
    st.title("Intelligence Controls")
    selected_alliances = st.multiselect(
        "Alliance filter",
        options=["NDA", "INDIA", "Others"],
        default=["NDA", "INDIA", "Others"],
    )
    zone_filter = st.multiselect(
        "Strategic zones",
        options=zones["Zone"].tolist(),
        default=zones["Zone"].tolist(),
    )
    min_turnout = st.slider("Minimum turnout", 50, 85, 55, 1, format="%d%%")
    view_mode = st.radio("Report lens", ["Executive", "Spend", "Voters", "Digital", "Regional"], horizontal=False)
    st.divider()
    st.caption("Source notes")
    st.write(
        "Data is transcribed from the supplied India Election Campaign Analysis Report PDF. "
        "Spend figures are estimates and should be validated before operational use."
    )


filtered_party = party[party["Alliance"].isin(selected_alliances)].copy()
filtered_turnout = turnout[turnout["Turnout (%)"] >= min_turnout].copy()
filtered_zones = zones[zones["Zone"].isin(zone_filter)].copy()

st.markdown(
    """
    <div class="hero">
      <h1>India Election Campaign Intelligence Report</h1>
      <p>Lok Sabha 2024 campaign performance dashboard covering alliance outcomes, spend efficiency,
      voter mobilisation, digital reach, regional battlegrounds, and strategic recommendations.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
m1, m2, m3, m4 = st.columns(4)
with m1:
    metric_card("Constituencies", "543", "Complete Lok Sabha map")
with m2:
    metric_card("Total Campaign Spend", "Rs 1.35L Cr", "Estimated national spend")
with m3:
    metric_card("National Turnout", "64.2%", "Election-wide benchmark")
with m4:
    metric_card("Registered Voters", "968 Mn", "World's largest electorate")

if view_mode == "Executive":
    insight(
        "NDA crossed the majority threshold with 293 seats, while the INDIA bloc reached 234. "
        "The decisive pattern was not national uniformity, but regional variation: NDA strength in North, West, and NE; INDIA strength in South and East."
    )
elif view_mode == "Spend":
    insight(
        "BJP's larger budget created scale, but regional parties such as SP and DMK show stronger spend efficiency per seat won."
    )
elif view_mode == "Voters":
    insight(
        "Women voters, rural farmers, and youth blocs require different issue frames; welfare, MSP, jobs, and education cannot be treated as one generic message."
    )
elif view_mode == "Digital":
    insight(
        "Digital reach amplified narratives, but the report flags that engagement quality matters more than follower totals because follower inflation is material."
    )
else:
    insight(
        "South and East remain structurally different campaign environments, where local identity and regional cadre networks offset national messaging."
    )


tab_overview, tab_spend, tab_voters, tab_digital, tab_region, tab_actions = st.tabs(
    [
        "Executive Map",
        "Spend Intelligence",
        "Voter Signals",
        "Digital War Room",
        "Regional Battles",
        "Action Plan",
    ]
)

with tab_overview:
    st.markdown('<div class="section-title">Alliance And Party Outcome</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1.05, 1])

    alliance = (
        party.groupby("Alliance", as_index=False)["Seats Won"]
        .sum()
        .sort_values("Seats Won", ascending=False)
    )
    with c1:
        fig = (
            alt.Chart(alliance, title="Seat Control By Alliance")
            .mark_arc(innerRadius=82, outerRadius=158, stroke="#ffffff", strokeWidth=2)
            .encode(
                theta=alt.Theta("Seats Won:Q"),
                color=alt.Color(
                    "Alliance:N",
                    scale=alt.Scale(
                        domain=list(ALLIANCE_COLORS.keys()),
                        range=list(ALLIANCE_COLORS.values()),
                    ),
                    legend=alt.Legend(title=None),
                ),
                tooltip=["Alliance:N", alt.Tooltip("Seats Won:Q", format=",.0f")],
            )
        )
        st.altair_chart(chart_theme(fig, 430), use_container_width=True)

    with c2:
        top_party = filtered_party.sort_values("Seats Won", ascending=True)
        fig = (
            alt.Chart(top_party, title="Seats Won By Party")
            .mark_bar(cornerRadiusEnd=4)
            .encode(
                x=alt.X("Seats Won:Q", title="Seats won"),
                y=alt.Y("Party / Alliance:N", sort="-x", title=None),
                color=alt.Color(
                    "Alliance:N",
                    scale=alt.Scale(
                        domain=list(ALLIANCE_COLORS.keys()),
                        range=list(ALLIANCE_COLORS.values()),
                    ),
                    legend=alt.Legend(title=None),
                ),
                tooltip=[
                    "Party / Alliance:N",
                    "Alliance:N",
                    alt.Tooltip("Seats Won:Q", format=",.0f"),
                    alt.Tooltip("Vote Share (%):Q", format=".2f"),
                    "Status:N",
                    alt.Tooltip("Swing vs 2019:Q", format="+.1f"),
                ],
            )
        )
        st.altair_chart(chart_theme(fig, 430), use_container_width=True)

    st.dataframe(
        filtered_party.style.format(
            {
                "Seats Contested": "{:.0f}",
                "Seats Won": "{:.0f}",
                "Vote Share (%)": "{:.2f}%",
                "Swing vs 2019": "{:+.1f}%",
            },
            na_rep="-",
        ),
        use_container_width=True,
        hide_index=True,
    )

with tab_spend:
    st.markdown('<div class="section-title">Campaign Spend And Efficiency</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        spend_long = spending.melt(
            id_vars=["Party"],
            value_vars=["2019 Spend (Cr)", "2024 Spend (Cr)"],
            var_name="Year",
            value_name="Spend (Cr)",
        ).dropna()
        fig = (
            alt.Chart(spend_long, title="Campaign Spend Growth")
            .mark_bar(cornerRadiusEnd=4)
            .encode(
                x=alt.X("Party:N", title=None),
                y=alt.Y("Spend (Cr):Q", title="Spend (Rs crore)"),
                color=alt.Color(
                    "Year:N",
                    scale=alt.Scale(
                        domain=["2019 Spend (Cr)", "2024 Spend (Cr)"],
                        range=["#94a3b8", "#ff7a1a"],
                    ),
                    legend=alt.Legend(title=None),
                ),
                xOffset="Year:N",
                tooltip=["Party:N", "Year:N", alt.Tooltip("Spend (Cr):Q", format=",.0f")],
            )
        )
        st.altair_chart(chart_theme(fig, 430), use_container_width=True)

    with c2:
        efficiency = spending.dropna(subset=["Spend per Seat Won (Cr)"]).sort_values("Spend per Seat Won (Cr)")
        points = (
            alt.Chart(efficiency, title="Spend Scale vs Seat Efficiency")
            .mark_circle(opacity=0.86)
            .encode(
                x=alt.X("2024 Spend (Cr):Q", title="2024 spend (Rs crore)"),
                y=alt.Y("Spend per Seat Won (Cr):Q", title="Spend per seat won (Rs crore)"),
                size=alt.Size("2024 Spend (Cr):Q", legend=None, scale=alt.Scale(range=[200, 2400])),
                color=alt.Color("Party:N", legend=alt.Legend(title=None)),
                tooltip=[
                    "Party:N",
                    alt.Tooltip("2024 Spend (Cr):Q", format=",.0f"),
                    alt.Tooltip("Spend per Seat Won (Cr):Q", format=".1f"),
                    "Primary Channel:N",
                ],
            )
        )
        labels = points.mark_text(align="center", baseline="bottom", dy=-10, fontWeight=700).encode(text="Party:N")
        st.altair_chart(chart_theme(points + labels, 430), use_container_width=True)

    c3, c4 = st.columns([.9, 1.1])
    with c3:
        fig = (
            alt.Chart(bjp_channels, title="BJP 2024 Channel Mix")
            .mark_arc(innerRadius=76, outerRadius=150, stroke="#ffffff", strokeWidth=2)
            .encode(
                theta=alt.Theta("Allocation (%):Q"),
                color=alt.Color("Campaign Channel:N", legend=alt.Legend(title=None, columns=1)),
                tooltip=[
                    "Campaign Channel:N",
                    alt.Tooltip("Allocation (%):Q", format=".0f"),
                    alt.Tooltip("Approx. Spend (Cr):Q", format=",.0f"),
                    "Key Activity:N",
                ],
            )
        )
        st.altair_chart(chart_theme(fig, 420), use_container_width=True)
    with c4:
        st.dataframe(
            bjp_channels.style.format({"Allocation (%)": "{:.0f}%", "Approx. Spend (Cr)": "{:,.0f}"}),
            use_container_width=True,
            hide_index=True,
        )

with tab_voters:
    st.markdown('<div class="section-title">Turnout And Demographic Lean</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1.05])

    with c1:
        sorted_turnout = filtered_turnout.sort_values("Turnout (%)", ascending=True)
        fig = (
            alt.Chart(sorted_turnout, title="State Turnout With 2019 Change")
            .mark_bar(cornerRadiusEnd=4)
            .encode(
                x=alt.X("Turnout (%):Q", title="Turnout"),
                y=alt.Y("State:N", sort="-x", title=None),
                color=alt.Color(
                    "Change:Q",
                    scale=alt.Scale(domain=[-5, 0, 7], range=["#dc2626", "#f8fafc", "#16a34a"]),
                    title="Change vs 2019",
                ),
                tooltip=[
                    "State:N",
                    alt.Tooltip("Turnout (%):Q", format=".1f"),
                    alt.Tooltip("2019 Turnout (%):Q", format=".1f"),
                    alt.Tooltip("Change:Q", format="+.1f"),
                    alt.Tooltip("Registered Voters (Mn):Q", format=".1f"),
                    alt.Tooltip("Votes Polled (Mn):Q", format=".1f"),
                ],
            )
        )
        st.altair_chart(chart_theme(fig, 470), use_container_width=True)

    with c2:
        demo_long = demographics.melt(
            id_vars=["Voter Segment", "Share of Electorate (%)", "Key Issue"],
            value_vars=["BJP Lean (%)", "Congress Lean (%)", "Regional Party (%)"],
            var_name="Political Lean",
            value_name="Lean (%)",
        )
        fig = (
            alt.Chart(demo_long, title="Estimated Segment Preference")
            .mark_bar(cornerRadiusEnd=2)
            .encode(
                x=alt.X("Voter Segment:N", title=None, sort=None, axis=alt.Axis(labelAngle=-35)),
                y=alt.Y("Lean (%):Q", title="Estimated lean"),
                color=alt.Color(
                    "Political Lean:N",
                    scale=alt.Scale(
                        domain=["BJP Lean (%)", "Congress Lean (%)", "Regional Party (%)"],
                        range=["#ff7a1a", "#2f6fed", "#1f9d76"],
                    ),
                    legend=alt.Legend(title=None),
                ),
                tooltip=[
                    "Voter Segment:N",
                    "Political Lean:N",
                    alt.Tooltip("Lean (%):Q", format=".0f"),
                    alt.Tooltip("Share of Electorate (%):Q", format=".0f"),
                    "Key Issue:N",
                ],
            )
        )
        st.altair_chart(chart_theme(fig, 470), use_container_width=True)

    st.dataframe(demographics, use_container_width=True, hide_index=True)

with tab_digital:
    st.markdown('<div class="section-title">Social Media And Ad Intelligence</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        social_long = social.melt(id_vars=["Platform"], var_name="Party", value_name="Followers (Mn)")
        fig = (
            alt.Chart(social_long, title="Social Media Presence At Campaign Peak")
            .mark_bar(cornerRadiusEnd=4)
            .encode(
                x=alt.X("Platform:N", title=None),
                y=alt.Y("Followers (Mn):Q", title="Followers (mn)"),
                color=alt.Color(
                    "Party:N",
                    scale=alt.Scale(
                        domain=["BJP", "Congress", "SP", "TMC"],
                        range=["#ff7a1a", "#2f6fed", "#d94848", "#1f9d76"],
                    ),
                    legend=alt.Legend(title=None),
                ),
                xOffset="Party:N",
                tooltip=["Platform:N", "Party:N", alt.Tooltip("Followers (Mn):Q", format=".1f")],
            )
        )
        st.altair_chart(chart_theme(fig, 430), use_container_width=True)

    with c2:
        points = (
            alt.Chart(digital_ads, title="Digital Spend, Impressions, And CPM")
            .mark_circle(opacity=0.86)
            .encode(
                x=alt.X("Total Digital Spend (Cr):Q", title="Digital spend (Rs crore)"),
                y=alt.Y("Total Impressions (Bn):Q", title="Impressions (bn)"),
                size=alt.Size("CPM Avg:Q", legend=alt.Legend(title="Avg CPM"), scale=alt.Scale(range=[180, 1500])),
                color=alt.Color("Party:N", legend=alt.Legend(title=None)),
                tooltip=[
                    "Party:N",
                    alt.Tooltip("Google Ads Spend (Cr):Q", format=",.0f"),
                    alt.Tooltip("Meta Ads Spend (Cr):Q", format=",.0f"),
                    alt.Tooltip("Total Impressions (Bn):Q", format=".1f"),
                    alt.Tooltip("CPM Avg:Q", format=".1f"),
                    "Top Message Theme:N",
                ],
            )
        )
        labels = points.mark_text(align="center", baseline="bottom", dy=-10, fontWeight=700).encode(text="Party:N")
        st.altair_chart(chart_theme(points + labels, 430), use_container_width=True)

    st.dataframe(
        digital_ads.style.format(
            {
                "Google Ads Spend (Cr)": "{:,.0f}",
                "Meta Ads Spend (Cr)": "{:,.0f}",
                "Total Impressions (Bn)": "{:.1f}",
                "CPM Avg": "{:.1f}",
                "Total Digital Spend (Cr)": "{:,.0f}",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )

with tab_region:
    st.markdown('<div class="section-title">Zone Performance And High-Stakes Seats</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([1.05, 1])

    with c1:
        zone_long = filtered_zones.melt(
            id_vars=["Zone", "States", "Zone Winner", "Key Narrative"],
            value_vars=["NDA Won", "INDIA Won", "Others"],
            var_name="Alliance",
            value_name="Seats",
        )
        fig = (
            alt.Chart(zone_long, title="Zone-Wise Seat Control")
            .mark_bar(cornerRadiusEnd=4)
            .encode(
                x=alt.X("Zone:N", title=None),
                y=alt.Y("Seats:Q", title="Seats"),
                color=alt.Color(
                    "Alliance:N",
                    scale=alt.Scale(
                        domain=["NDA Won", "INDIA Won", "Others"],
                        range=["#ff7a1a", "#2f6fed", "#8b5cf6"],
                    ),
                    legend=alt.Legend(title=None),
                ),
                tooltip=["Zone:N", "Alliance:N", alt.Tooltip("Seats:Q", format=",.0f"), "States:N", "Zone Winner:N", "Key Narrative:N"],
            )
        )
        st.altair_chart(chart_theme(fig, 430), use_container_width=True)

    with c2:
        competitive = constituencies.dropna(subset=["Margin (Votes)", "Turnout (%)"]).copy()
        points = (
            alt.Chart(competitive, title="High-Stakes Constituencies")
            .mark_circle(opacity=0.86)
            .encode(
                x=alt.X("Margin (Votes):Q", title="Winning margin"),
                y=alt.Y("Turnout (%):Q", title="Turnout"),
                size=alt.Size("Campaign Spend (Cr):Q", legend=alt.Legend(title="Spend Cr"), scale=alt.Scale(range=[180, 1500])),
                color=alt.Color("Party:N", legend=alt.Legend(title=None)),
                tooltip=[
                    "Constituency:N",
                    "State:N",
                    "Winner:N",
                    "Party:N",
                    alt.Tooltip("Margin (Votes):Q", format=",.0f"),
                    alt.Tooltip("Turnout (%):Q", format=".1f"),
                    alt.Tooltip("Campaign Spend (Cr):Q", format=".0f"),
                ],
            )
        )
        labels = points.mark_text(align="center", baseline="bottom", dy=-10, fontWeight=700).encode(text="Constituency:N")
        st.altair_chart(chart_theme(points + labels, 430), use_container_width=True)

    st.dataframe(constituencies, use_container_width=True, hide_index=True)

with tab_actions:
    st.markdown('<div class="section-title">Strategic Recommendation Board</div>', unsafe_allow_html=True)
    priorities = ["Critical", "High", "Medium"]
    cols = st.columns(len(priorities))
    for col, priority in zip(cols, priorities):
        with col:
            st.subheader(priority)
            subset = recommendations[recommendations["Priority"] == priority]
            for _, row in subset.iterrows():
                priority_class = f"priority-{priority.lower()}"
                st.markdown(
                    f"""
                    <div class="metric-card {priority_class}">
                      <div class="metric-label">{row['Impact Area']} | {row['Timeline']}</div>
                      <div style="font-size:.98rem;font-weight:700;color:#111827;">{row['Recommendation']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.write("")

    st.markdown('<div class="section-title">Data Quality Risk Flags</div>', unsafe_allow_html=True)
    risks = pd.DataFrame(
        [
            ["Candidate affidavit inconsistencies", "18% affected", "Standardise ECI schema enforcement"],
            ["Constituency boundary mismatches", "12% of third-party datasets", "Use official current shapefiles"],
            ["Voter roll duplicates", "2.8M flagged entries", "Strengthen UIDAI-ECI de-duplication workflows"],
            ["Follower inflation", "15-22% artificial counts", "Use authentic engagement as KPI"],
            ["Expenditure under-reporting", "4-8x gap vs estimates", "Harmonise official and independent data"],
        ],
        columns=["Risk", "Signal", "Recommended Control"],
    )
    st.dataframe(risks, use_container_width=True, hide_index=True)

st.caption(
    "Prepared as a Streamlit intelligence dashboard from the supplied PDF. "
    "Use for portfolio, analysis presentation, or campaign analytics demonstration."
)
