"""Shared helper functions used by all pages."""
import numpy as np
import pandas as pd
import streamlit as st


@st.cache_data
def generate_sample_data(rows: int = 30) -> pd.DataFrame:
    """Generate local sample metrics (no external API needed).

    @st.cache_data remembers the result, so the same `rows` value
    is only generated once instead of on every click.
    """
    rng = np.random.default_rng(seed=42)  # fixed seed = same "random" data every run
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=rows)
    return pd.DataFrame({
        "Date": dates,
        "Users": rng.integers(100, 500, size=rows),
        "Revenue": rng.uniform(1000, 5000, size=rows).round(2),
        "Category": rng.choice(["Web", "Mobile", "Direct"], size=rows),
    })


def calculate_summary(df: pd.DataFrame) -> dict:
    """Return basic summary metrics. Safe for an empty table (all filters removed)."""
    if df.empty:
        return {"total_users": 0, "total_revenue": 0.0, "avg_daily_users": 0}
    return {
        "total_users": int(df["Users"].sum()),
        "total_revenue": float(df["Revenue"].sum()),
        "avg_daily_users": int(df["Users"].mean()),
    }


def get_setting(key: str, default: str) -> str:
    """Read a value from st.secrets['app_settings'], or use `default` if it is missing.

    This stops the app crashing on Streamlit Cloud when no secrets have been added yet.
    """
    try:
        return st.secrets["app_settings"][key]
    except Exception:  # no secrets file, or the key is missing
        return default
