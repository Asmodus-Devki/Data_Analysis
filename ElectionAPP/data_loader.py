import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_excel(
        "Indian-General-Elections-2024.xlsx"
    )

    df["Leading Party"] = (
        df["Leading Party"].fillna("Unknown").astype(str))
    
    df["State/UT"] = (
        df["State/UT"].fillna("Unknown").astype(str))
    
    df["Margin"] = (
        pd.to_numeric(
             df["Margin"],
             errors="coerce"
             ).fillna(0))

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

    categorical_cols = [
        "Leading Candidate", "Trailing Candidate", 
        "Leading Party", "Trailing Party", 
        "State/UT", "Constituency", "Status"
    ]
    
    for col in categorical_cols:
        if col in df.columns:
            # Fill NaNs first, then cast to string to ensure consistency
            df[col] = df[col].fillna("Unknown")
            # Explicitly force string conversion to prevent bool/str mixed types
            df[col] = df[col].apply(lambda x: str(x) if x is not None else "Unknown")
            df[col] = df[col].str.strip()

    return df