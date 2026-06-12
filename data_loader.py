import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_excel(
        "Indian-General-Elections-2024.xlsx"
    )

    df.columns = df.columns.str.strip()

    df["Margin"] = (
        df["Margin"]
        .astype(str)
        .str.replace(",", "")
    )

    df["Margin"] = pd.to_numeric(
        df["Margin"],
        errors="coerce"
    )

    df["Trailing Candidate"] = (
        df["Trailing Candidate"]
        .fillna("Unknown")
    )

    df["Trailing Party"] = (
        df["Trailing Party"]
        .fillna("Unknown")
    )

    return df