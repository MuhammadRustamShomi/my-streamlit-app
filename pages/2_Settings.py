"""Settings page: change display name and sample data size."""
import streamlit as st

st.set_page_config(page_title="Settings", page_icon="⚙️")
st.title("⚙️ App Settings")

# A form re-runs the app only when "Save Settings" is clicked
with st.form("settings_form"):
    new_name = st.text_input("Display Name", value=st.session_state.get("username", "Guest"))
    new_rows = st.slider("Number of Days to Simulate", min_value=7, max_value=90,
                         value=st.session_state.get("data_rows", 30))
    submitted = st.form_submit_button("Save Settings")

if submitted:
    st.session_state.username = new_name.strip() or "Guest"
    st.session_state.data_rows = new_rows
    st.success("Settings saved! Open Home or Dashboard to see the changes.")

st.caption("ℹ️ Settings are kept while this browser tab is open. Refreshing the page resets them.")
