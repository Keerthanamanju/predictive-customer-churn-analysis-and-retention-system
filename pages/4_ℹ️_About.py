import streamlit as st
from utils import apply_custom_css

st.set_page_config(page_title="About", layout="wide")
apply_custom_css()

st.title("ℹ️ About the Project")
st.write("---")

st.markdown("""
<div class="glass-card" style="text-align: left;">
    <h3 style="color: #b829ea;">Project Architecture</h3>
    <p>This full-stack data science application was built to automate the prediction of customer attrition.</p>
    <h4 style="color: #a0a0b0; margin-top: 15px;">Tech Stack:</h4>
    <ul style="color: #e0e0e0; margin-bottom: 15px;">
        <li><b>Data Manipulation:</b> Pandas, NumPy</li>
        <li><b>Machine Learning:</b> Scikit-Learn (Logistic Regression, Decision Trees, Random Forest)</li>
        <li><b>Visualization:</b> Plotly, Matplotlib, Seaborn</li>
        <li><b>Frontend deployment:</b> Streamlit</li>
    </ul>
    <h4 style="color: #a0a0b0;">Model Performance:</h4>
    <p style="color: #e0e0e0;">The deployed model is a Logistic Regression algorithm that achieved an accuracy of <b>93.39%</b> during the testing phase, outperforming both Decision Tree and Random Forest classifiers on this specific dataset.</p>
</div>
""", unsafe_allow_html=True)