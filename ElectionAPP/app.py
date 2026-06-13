import streamlit as st
from data_loader import load_data

st.set_page_config(
    page_title="India Election Intelligence",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

df = load_data()

# Sidebar
st.sidebar.image(
    "https://media.istockphoto.com/id/2053374354/photo/indian-general-election-2024.jpg?s=612x612&w=0&k=20&c=NlNIT3oeb6mtxCzLFSSKKsNo5l3TUYorNfB1AB1faHg=",
    width=120
)

st.sidebar.title("Election War Room")

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Overview",
        "Party Analytics",
        "State Intelligence",
        "Candidate Intelligence",
        "Constituency Explorer"
    ]
)

st.sidebar.markdown("---")

states = st.sidebar.multiselect(
    "State/UT",
    sorted(df["State/UT"].astype(str).unique())
)

selected_parties = st.sidebar.multiselect(
    "Leading Party",
    sorted(df["Leading Party"].astype(str).unique())
)

filtered_df = df.copy()

if st.sidebar.button(
     "Reset Filters"
     ):
    st.rerun()

if states:
    filtered_df = filtered_df[
        filtered_df["State/UT"].isin(states)
    ]

if selected_parties:
    
    filtered_df = filtered_df[
    filtered_df["Leading Party"].isin(
        selected_parties
    )
]

if page == "Executive Overview":
    from executive_overview import show_page
    show_page(filtered_df)

elif page == "Party Analytics":
    from party_analytics import show_page
    show_page(filtered_df)

elif page == "State Intelligence":
    from state_intelligence import show_page
    show_page(filtered_df)

elif page == "Candidate Intelligence":
    from candidate_intelligence import show_page
    show_page(filtered_df)

elif page == "Constituency Explorer":
    from constituency_explorer import show_page
    show_page(filtered_df)