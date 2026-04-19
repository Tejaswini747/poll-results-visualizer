import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Poll Dashboard", layout="wide")

# -----------------------------
# PROFESSIONAL CSS
# -----------------------------
st.markdown("""
<style>

/* Global */
body {
    background-color: #0f172a;
}

/* Header */
.header {
    font-size: 28px;
    font-weight: 600;
    color: white;
}

/* KPI Cards */
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 12px;
    color: white;
    border: 1px solid #334155;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

/* Section Titles */
.section-title {
    font-size: 20px;
    color: #cbd5e1;
    margin-top: 20px;
    margin-bottom: 10px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #020617;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="header">📊 Poll Results Dashboard</div>', unsafe_allow_html=True)
st.markdown("---")

# -----------------------------
# LOAD DATA
# -----------------------------
file_path = "data/poll_data.csv"

if not os.path.exists(file_path):
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame({
        "Age Group": np.random.choice(["18-24", "25-34", "35-44"], 100),
        "Gender": np.random.choice(["Male", "Female"], 100),
        "Preferred Tool": np.random.choice(["Python", "Excel", "R"], 100),
        "Satisfaction": np.random.randint(1, 6, 100)
    })
    df.to_csv(file_path, index=False)
else:
    df = pd.read_csv(file_path)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🔍 Filters")

tool = st.sidebar.multiselect(
    "Tool",
    df["Preferred Tool"].unique(),
    default=df["Preferred Tool"].unique()
)

age = st.sidebar.multiselect(
    "Age Group",
    df["Age Group"].unique(),
    default=df["Age Group"].unique()
)

filtered_df = df[
    (df["Preferred Tool"].isin(tool)) &
    (df["Age Group"].isin(age))
]

# -----------------------------
# KPI SECTION
# -----------------------------
st.markdown('<div class="section-title">Overview</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.markdown(f"""
<div class="card">
<h4>Total Responses</h4>
<h2>{len(filtered_df)}</h2>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="card">
<h4>Avg Satisfaction</h4>
<h2>{round(filtered_df["Satisfaction"].mean(),2)}</h2>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="card">
<h4>Top Tool</h4>
<h2>{filtered_df["Preferred Tool"].mode()[0]}</h2>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# CHART SECTION
# -----------------------------
st.markdown('<div class="section-title">Analysis</div>', unsafe_allow_html=True)

col4, col5 = st.columns(2)

with col4:
    fig1 = px.bar(
        filtered_df,
        x="Preferred Tool",
        color="Preferred Tool",
        title="Tool Preference",
        template="plotly_dark"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    fig2 = px.pie(
        filtered_df,
        names="Preferred Tool",
        title="Tool Share",
        hole=0.4
    )
    fig2.update_layout(template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# TREND SECTION
# -----------------------------
st.markdown('<div class="section-title">Trend</div>', unsafe_allow_html=True)

fig3 = px.line(
    filtered_df.reset_index(),
    y="Satisfaction",
    title="Satisfaction Trend",
    template="plotly_dark"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# DATA TABLE
# -----------------------------
st.markdown('<div class="section-title">Raw Data</div>', unsafe_allow_html=True)
st.dataframe(filtered_df, use_container_width=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("🚀 Built by TEJASWINI | Data Analytics Project")