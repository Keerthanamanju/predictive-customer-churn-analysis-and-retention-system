import streamlit as st
from utils import apply_custom_css

st.set_page_config(page_title="Home", layout="wide")
apply_custom_css()

st.title("🏠 Executive Overview")
st.write("---")

# Top row
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card" style="text-align: left; height: 100%;">
        <h3>🎯 Project Objective</h3>
        <p>Customer churn is the silent killer of subscription businesses. This platform uses predictive analytics to identify at-risk customers before they leave. By processing historical behavioral and demographic data, we generate a live risk profile to enable proactive retention strategies.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card" style="text-align: left; height: 100%;">
        <h3>📂 Data Provenance & Engineering</h3>
        <p>Built on a robust, real-world Kaggle dataset, the data pipeline underwent rigorous feature engineering to extract meaningful patterns and ensure high-quality model training.</p>
        <ul>
            <li><strong>Source:</strong> Kaggle Customer Churn Database</li>
            <li><strong>Scale:</strong> 100,000 Verified Records</li>
            <li><strong>Features:</strong> 21 optimized predictive variables</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Spacer

# Bottom row
col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="glass-card" style="text-align: left; height: 100%;">
        <h3>🧠 Machine Learning Engine</h3>
        <p>After evaluating multiple algorithms (including Random Forest and Decision Trees), Logistic Regression was selected for deployment due to its superior performance and clear interpretability.</p>
        <ul>
            <li><strong>Algorithm:</strong> Logistic Regression (L2 Regularization)</li>
            <li><strong>Validation:</strong> 5-Fold Cross Validation</li>
            <li><strong>Accuracy:</strong> 93.39%</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="glass-card" style="text-align: left; height: 100%;">
        <h3>💼 Business Impact</h3>
        <p>Integrating this model into daily operations allows customer success and retention teams to:</p>
        <ul>
            <li>Prioritize outreach to high-value, high-risk clients.</li>
            <li>Reduce marketing waste by targeting specific pain points.</li>
            <li>Improve overall customer lifetime value (CLV).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# Navigation Button
_, col_btn = st.columns([3, 1]) # Pushes the button to the right side
with col_btn:
    if st.button("Proceed to Dashboard 📊", use_container_width=True):
        st.switch_page("pages/2_📊_Dashboard.py")