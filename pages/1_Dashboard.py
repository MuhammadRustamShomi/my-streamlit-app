"""Dashboard page: KPIs, chart and raw data with a category filter."""
import streamlit as st

from utils.helpers import calculate_summary, generate_sample_data

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")
st.title("📊 Analytics Dashboard")

# Use the row count chosen on the Settings page (30 if not set yet)
rows = st.session_state.get("data_rows", 30)
df = generate_sample_data(rows=rows)

# Sidebar filter
categories = sorted(df["Category"].unique())
selected = st.sidebar.multiselect("Filter by Category", options=categories, default=categories)
filtered_df = df[df["Category"].isin(selected)]

if filtered_df.empty:
    st.warning("No data to show. Pick at least one category in the sidebar.")
    st.stop()  # stop here so the chart below doesn't break

stats = calculate_summary(filtered_df)

# KPI cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Users", f"{stats['total_users']:,}")
col2.metric("Total Revenue", f"${stats['total_revenue']:,.2f}")
col3.metric("Avg Daily Users", f"{stats['avg_daily_users']:,}")

st.divider()

# Chart and data table
st.subheader("Daily Users Trend")
st.line_chart(filtered_df.set_index("Date")["Users"])

with st.expander("View Raw Data"):
    st.dataframe(filtered_df, width="stretch", hide_index=True)  # width="stretch" replaces the old use_container_width
