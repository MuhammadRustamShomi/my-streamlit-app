"""Home page (main entry point). Run with:  streamlit run streamlit_app.py"""
import streamlit as st

from utils.helpers import get_setting

st.set_page_config(page_title="My Streamlit App", page_icon="📊", layout="wide")

# Shared values for all pages (st.session_state survives clicks and page changes)
if "username" not in st.session_state:
    st.session_state.username = "Guest"
if "data_rows" not in st.session_state:
    st.session_state.data_rows = 30

st.title(f"👋 Welcome, {st.session_state.username}!")
st.markdown("""
This is a self-contained, multi-page Streamlit app. It needs no external APIs.

### How to navigate (use the sidebar)
* **📊 Dashboard**: metrics, an interactive chart and the raw data.
* **⚙️ Settings**: change your display name and how many days of sample data to show.
""")

environment = get_setting("environment", "cloud")
st.info(f"Running in **{environment}** mode with **{st.session_state.data_rows} days** of sample data.")
