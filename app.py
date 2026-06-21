import streamlit as st
from utils import apply_custom_css

st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

st.markdown("<h1>⚡ Customer Churn Intelligence System</h1>", unsafe_allow_html=True)
st.write("---")

# Upgraded Copy
st.markdown("""
<div style="text-align: center; margin-bottom: 40px;">
    <h3 style="color: #a0a0b0; text-shadow: none;">Turn Data into Retention</h3>
    <p style="font-size: 1.1rem; max-width: 800px; margin: 0 auto; color: #e0e0e0;">
        Stop guessing why customers leave. This intelligence platform leverages a high-accuracy machine learning engine to analyze behavioral patterns, predict attrition risks, and empower you with actionable insights to secure your revenue.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("") # Spacer

# Navigation Buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Executive Home", use_container_width=True):
        st.switch_page("pages/1_🏠_Home.py")

with col2:
    if st.button("📊 Data Dashboard", use_container_width=True):
        st.switch_page("pages/2_📊_Dashboard.py")

with col3:
    if st.button("⚡ Live Prediction", use_container_width=True):
        st.switch_page("pages/3_⚡_Prediction.py")

with col4:
    if st.button("ℹ️ System Architecture", use_container_width=True):
        st.switch_page("pages/4_ℹ️_About.py")