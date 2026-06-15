import streamlit as st
import plotly.express as px
from utils import load_data, apply_custom_css

st.set_page_config(page_title="Dashboard", layout="wide")
apply_custom_css()

st.title("📊 Data Intelligence Dashboard")
st.write("---")

# Load Data
df = load_data()
color_map = {'Churned': '#ff3366', 'Retained': '#00ff99', 'At Risk': '#ffcc00'}

# --- TOP LEVEL METRICS ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="glass-card"><div class="metric-label">Total Customers</div><div class="metric-value">{len(df):,}</div></div>', unsafe_allow_html=True)
with col2:
    churn_rate = (len(df[df["Churn_Status"] == "Churned"]) / len(df)) * 100
    st.markdown(f'<div class="glass-card"><div class="metric-label">Global Churn Rate</div><div class="metric-value">{churn_rate:.1f}%</div></div>', unsafe_allow_html=True)
with col3:
    avg_tenure = df['Tenure_Months'].mean()
    st.markdown(f'<div class="glass-card"><div class="metric-label">Avg Tenure (Months)</div><div class="metric-value">{avg_tenure:.1f}</div></div>', unsafe_allow_html=True)
with col4:
    avg_revenue = df['Monthly_Charges'].mean()
    st.markdown(f'<div class="glass-card"><div class="metric-label">Avg Monthly Spend</div><div class="metric-value">${avg_revenue:.2f}</div></div>', unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# --- KEY INSIGHTS ---
st.markdown("""
<div class="glass-card" style="text-align: left; margin-bottom: 30px;">
    <h4 style="color: #b829ea;">💡 Key Insights Discovered</h4>
    <ul style="color: #e0e0e0; font-size: 1.1rem;">
        <li><b>Tenure is the strongest predictor:</b> Customers in their first 12 months churn at a significantly higher rate than long-term users.</li>
        <li><b>Contract Risk:</b> Month-to-Month contracts have the highest flight risk. Moving users to annual plans should be a priority.</li>
        <li><b>Financial Sensitivity:</b> Higher monthly charges correlate with increased churn, especially when users aren't fully utilizing the services.</li>
        <li><b>Support Friction:</b> Accounts with multiple support calls or complaints need immediate intervention.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- VISUALIZATION ROW 1 ---
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("<h4 style='color: #a0a0b0;'>Customer Attrition Breakdown</h4>", unsafe_allow_html=True)
    fig_churn = px.pie(
        df, 
        names='Churn_Status', 
        hole=0.5, 
        color='Churn_Status',
        color_discrete_map=color_map
    )
    fig_churn.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', margin=dict(t=20, b=20, l=20, r=20))
    st.plotly_chart(fig_churn, use_container_width=True)

with chart_col2:
    st.markdown("<h4 style='color: #a0a0b0;'>Financial Impact: Monthly Charges vs Tenure</h4>", unsafe_allow_html=True)
    df_sample = df.sample(n=min(2000, len(df)), random_state=42)
    fig_scatter = px.scatter(
        df_sample, 
        x="Tenure_Months", 
        y="Monthly_Charges", 
        color="Churn_Status", 
        opacity=0.7, 
        color_discrete_map=color_map
    )
    fig_scatter.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', margin=dict(t=20, b=20, l=20, r=20))
    st.plotly_chart(fig_scatter, use_container_width=True)

st.write("---")

# --- VISUALIZATION ROW 2 ---
chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    st.markdown("<h4 style='color: #a0a0b0;'>Risk by Contract Type</h4>", unsafe_allow_html=True)
    contract_df = df.groupby(['Contract_Type', 'Churn_Status']).size().reset_index(name='Count')
    fig_bar = px.bar(
        contract_df, 
        x="Contract_Type", 
        y="Count", 
        color="Churn_Status", 
        barmode="group",
        color_discrete_map=color_map
    )
    fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', margin=dict(t=20, b=20, l=20, r=20))
    st.plotly_chart(fig_bar, use_container_width=True)

with chart_col4:
    st.markdown("<h4 style='color: #a0a0b0;'>Density of Monthly Charges by Status</h4>", unsafe_allow_html=True)
    fig_box = px.box(
        df, 
        x="Churn_Status", 
        y="Monthly_Charges", 
        color="Churn_Status",
        color_discrete_map=color_map
    )
    fig_box.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
    st.plotly_chart(fig_box, use_container_width=True)

st.write("---")

# --- NAVIGATION BUTTONS ---
col_back, space, col_next = st.columns([1, 2, 1])
with col_back:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("pages/1_🏠_Home.py")
with col_next:
    if st.button("Launch Prediction Engine ⚡", use_container_width=True):
        st.switch_page("pages/3_⚡_Prediction.py")