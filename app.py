import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. Load Data
df = pd.read_csv('processed_monthly_report.csv')

# 2. Header
st.set_page_config(page_title="BigSeller Crisis Analysis 2025", layout="wide")
st.title("📊 2025 Business Impact Analysis: Revenue vs. Cancel Rate")
st.markdown(f"**Analysis for:** Nuttanon Tatiyapongkul (Pitch) | **Status:** Crisis Recovery Phase")

# 3. Key Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue 2025", f"฿{df['Sales'].sum():,.2f}")
col2.metric("Total Orders", f"{df['Total Orders'].sum():,}")
col3.metric("Avg. Cancel Rate", f"{df['Cancel Rate %'].mean():.2f}%")

# 4. Crisis Visualization
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add Revenue Bar Chart
fig.add_trace(
    go.Bar(x=df['Month'], y=df['Sales'], name="Revenue (Sales)", marker_color='skyblue', opacity=0.7),
    secondary_y=False,
)

# Add Cancel Rate Line Chart
fig.add_trace(
    go.Scatter(x=df['Month'], y=df['Cancel Rate %'], name="Cancel Rate %", line=dict(color='red', width=3), marker=dict(size=10)),
    secondary_y=True,
)

# Layout adjustments
fig.update_layout(
    title_text="<b>Revenue Trend vs. Operational Friction (Cancel Rate)</b>",
    xaxis_title="Month (2025)",
    legend=dict(x=0.01, y=0.99),
    hovermode="x unified"
)

fig.update_yaxes(title_text="<b>Total Revenue (THB)</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>Cancel Rate (%)</b>", secondary_y=True)

st.plotly_chart(fig, use_container_width=True)

# 5. Analyst Insights (The "Why")
st.subheader("📝 Analyst Insights: The Story Behind the Data")
st.info("""
- **Q1 Peak (Jan):** Highest Revenue at ฿4.5M. Supply chain was healthy before the CNY holiday.
- **The H2 Crisis (Jul - Dec):** Revenue dropped significantly due to internal fraud and cash flow crunch. 
- **The October Spike:** Notice the spike in **Cancel Rate (13.9%)** in October. Even as sales attempted to recover, the high cancellation rate indicates a severe supply shortage and pricing mismatch against the market equilibrium.
""")