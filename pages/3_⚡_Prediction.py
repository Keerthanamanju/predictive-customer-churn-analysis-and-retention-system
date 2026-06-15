import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from utils import load_models, apply_custom_css

st.set_page_config(page_title="Prediction Engine", layout="wide")
apply_custom_css()

model, scaler, encoder = load_models()

st.title("⚡ Live Risk Analysis")
st.markdown("<p style='color: #a0a0b0; font-size: 1.1rem; margin-bottom: 30px;'>Enter the customer's profile parameters below to generate a real-time churn probability report.</p>", unsafe_allow_html=True)

# --- GROUPED INPUT CONSOLE ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='color: #b829ea;'>👤 Demographics & Billing</h3>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    age = c1.number_input("Age", min_value=18, max_value=100, value=30)
    gender = c2.selectbox("Gender", ["Male", "Female"])
    tenure = c1.number_input("Tenure (Months)", min_value=0, max_value=120, value=12)
    contract = c2.selectbox("Contract Type", ["Month-to-Month", "One Year", "Two Year"])
    monthly_charges = c1.number_input("Monthly Charges ($)", value=50.0)
    total_charges = c2.number_input("Total Charges ($)", value=600.0)
    payment_method = c1.selectbox("Payment Method", ["UPI", "Credit Card", "Bank Transfer", "E-Wallet"])
    paperless = c2.selectbox("Paperless Billing", ["Yes", "No"])

with col2:
    st.markdown("<h3 style='color: #b829ea;'>🌐 Services & Ecosystem</h3>", unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    internet = c3.selectbox("Internet Service", ["Fiber", "DSL", "None"])
    usage_gb = c4.number_input("Avg Monthly Usage (GB)", value=100.0)
    security = c3.selectbox("Online Security", ["Yes", "No"])
    tech_support = c4.selectbox("Tech Support", ["Yes", "No"])
    streaming_tv = c3.selectbox("Streaming TV", ["Yes", "No"])
    streaming_movies = c4.selectbox("Streaming Movies", ["Yes", "No"])
    
    st.markdown("<h3 style='color: #b829ea; margin-top: 15px;'>📞 Engagement & Health</h3>", unsafe_allow_html=True)
    c5, c6 = st.columns(2)
    satisfaction = c5.slider("Satisfaction Score", 1.0, 5.0, 3.0, 0.5)
    late_payments = c6.number_input("Late Payments", min_value=0, value=0)
    num_complaints = c5.number_input("Complaints", min_value=0, value=0)
    support_calls = c6.number_input("Support Calls", min_value=0, value=1)

st.write("---")

# Centered Action Button
_, btn_col, _ = st.columns([1, 2, 1])
with btn_col:
    analyze_button = st.button("🚀 Analyze Risk Profile", use_container_width=True)

# --- PREDICTION LOGIC & UI ---
if analyze_button:
    # Map inputs
    input_data = {
        'Age': age, 'Tenure_Months': tenure, 'Monthly_Charges': monthly_charges,
        'Total_Charges': total_charges, 'Num_Complaints': num_complaints,
        'Satisfaction_Score': satisfaction, 'Support_Calls': support_calls,
        'Late_Payments': late_payments, 'Avg_Monthly_Usage_GB': usage_gb,
        'Gender_Male': 1 if gender == "Male" else 0,
        'Contract_Type_One Year': 1 if contract == "One Year" else 0,
        'Contract_Type_Two Year': 1 if contract == "Two Year" else 0,
        'Internet_Service_Fiber': 1 if internet == "Fiber" else 0,
        'Online_Security_Yes': 1 if security == "Yes" else 0,
        'Tech_Support_Yes': 1 if tech_support == "Yes" else 0,
        'Streaming_TV_Yes': 1 if streaming_tv == "Yes" else 0,
        'Streaming_Movies_Yes': 1 if streaming_movies == "Yes" else 0,
        'Payment_Method_Credit Card': 1 if payment_method == "Credit Card" else 0,
        'Payment_Method_E-Wallet': 1 if payment_method == "E-Wallet" else 0,
        'Payment_Method_UPI': 1 if payment_method == "UPI" else 0,
        'Paperless_Billing_Yes': 1 if paperless == "Yes" else 0
    }
    
    # Process
    df_input = pd.DataFrame([input_data])
    scaled_input = scaler.transform(df_input)
    prediction_encoded = model.predict(scaled_input)
    prediction_label = encoder.inverse_transform(prediction_encoded)[0]
    
    probs = model.predict_proba(scaled_input)[0]
    max_prob = np.max(probs) * 100
    
    # Dynamic Styling 
    color_map = {'Churned': '#ff3366', 'Retained': '#00ff99', 'At Risk': '#ffcc00'}
    theme_color = color_map[prediction_label]
    
    # --- UPGRADED DYNAMIC INTELLIGENCE ENGINE ---
    insights = []
    recommendations = []

    if prediction_label in ['Churned', 'At Risk']:
        if tenure <= 12:
            insights.append(f"<b>High-Risk Onboarding Window:</b> This customer is only {tenure} months into their lifecycle. Historical data shows that churn probability spikes significantly during the first year of adoption.")
            recommendations.append("<b>Accelerate Time-to-Value:</b> Immediately assign a customer success representative to conduct a personalized onboarding review and ensure they are fully utilizing their subscribed features.")
        if contract == "Month-to-Month":
            insights.append("<b>Zero Barrier to Exit:</b> The current Month-to-Month contract structure allows the customer to cancel instantly without financial penalty, making them highly susceptible to competitor offers.")
            recommendations.append("<b>Incentivize Commitment:</b> Target this user with an aggressive campaign offering a 15-20% discount or a free month of premium services if they upgrade to an annual billing cycle.")
        if monthly_charges >= 80:
            insights.append(f"<b>Price Sensitivity Triggered:</b> The customer's monthly recurring revenue (MRR) is notably high at ${monthly_charges}. High-tier subscribers expect flawless service and are quick to churn if perceived value drops.")
            recommendations.append("<b>Value Re-alignment:</b> Conduct an immediate account audit. If they are paying for services they aren't using (e.g., high data caps), proactively suggest a cost-saving downgrade to build trust and save the overall account.")
        if support_calls >= 2 or num_complaints >= 1:
            insights.append(f"<b>Severe Service Friction:</b> With {support_calls} support calls and {num_complaints} formal complaints, this account is experiencing significant technical or billing issues. Frustration levels are likely critical.")
            recommendations.append("<b>Executive Escalation:</b> Bypass standard automated retention emails. Route this account directly to a Tier-2 resolution specialist for a 'white-glove' recovery call to address underlying technical issues.")
        if satisfaction <= 2.5:
            insights.append(f"<b>Deteriorating Sentiment:</b> The user has self-reported a highly negative satisfaction score of {satisfaction}/5. This is one of the strongest leading indicators of imminent cancellation.")
            recommendations.append("<b>Damage Control:</b> Issue a personalized apology from leadership and offer a significant retention credit. Suppress all standard marketing and upsell communications immediately.")
            
        if not insights: 
            insights.append("<b>Complex Risk Profile:</b> The machine learning algorithm has detected subtle, multi-variable patterns indicating a high flight risk, despite a lack of obvious single-metric red flags.")
            recommendations.append("<b>Manual Intervention Required:</b> Flag account for a comprehensive manual review by the customer retention team to identify qualitative issues not captured by standard metrics.")
            
    else: # Retained
        insights.append("<b>Healthy Account Status:</b> The model indicates a high probability of continued subscription. Behavioral patterns closely match our most loyal customer cohorts.")
        if total_charges > 2000:
            insights.append(f"<b>High Lifetime Value (CLV):</b> This is a highly profitable account with ${total_charges} in total historical billing. Protecting this revenue stream is a priority.")
            recommendations.append("<b>Reward Loyalty:</b> Enroll the customer in the VIP program and send a personalized 'Thank You' package or exclusive beta-access to upcoming features to cement brand loyalty.")
        if streaming_tv == "No" or streaming_movies == "No":
            insights.append("<b>Untapped Revenue Potential:</b> The customer is highly stable but is currently under-utilizing the broader entertainment ecosystem, relying primarily on core internet/utility services.")
            recommendations.append("<b>Targeted Upsell Campaign:</b> Deploy a soft-sell marketing sequence highlighting the benefits of bundling Streaming TV and Movies at a discounted introductory rate.")
        if contract == "One Year" or contract == "Two Year":
            insights.append("<b>Contractual Stability:</b> Revenue is currently secured via a long-term agreement, severely limiting short-term churn risk.")
            recommendations.append("<b>Proactive Renewal Strategy:</b> Set an automated trigger in the CRM to initiate a renewal conversation 60 days prior to contract expiration, offering early-renewal bonuses.")
        if not recommendations:
            recommendations.append("<b>Maintain Engagement:</b> Continue standard lifecycle marketing communications. No aggressive intervention is required at this time.")

    # Convert lists to HTML bullets
    insight_html = "".join([f"<li style='margin-bottom: 12px;'>{i}</li>" for i in insights])
    rec_html = "".join([f"<li style='margin-bottom: 12px;'>{r}</li>" for r in recommendations])

    # --- LAYOUT RESULTS ---
    st.markdown("<br>", unsafe_allow_html=True)
    res_col1, res_col2 = st.columns([1, 1.5])
    
    with res_col1:
        st.markdown(f"""
            <div class="glass-card" style="height: 100%;">
                <div class="metric-label">Predicted Status</div>
                <div class="metric-value" style="color: {theme_color}; margin-top: 30px;">
                    {prediction_label.upper()}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with res_col2:
        # Plotly Gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=max_prob,
            number={'suffix': "%", 'font': {'color': 'white'}},
            title={'text': "Model Confidence", 'font': {'color': '#a0a0b0', 'size': 18}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
                'bar': {'color': theme_color},
                'bgcolor': "rgba(255, 255, 255, 0.05)",
                'borderwidth': 0,
                'steps': [
                    {'range': [0, 50], 'color': "rgba(255,255,255, 0.02)"},
                    {'range': [50, 75], 'color': "rgba(255,255,255, 0.05)"},
                    {'range': [75, 100], 'color': "rgba(255,255,255, 0.1)"}
                ]
            }
        ))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"}, height=220, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    
    # Insights and Recommendations row
    st.markdown(f"""
        <div class="glass-card" style="text-align: left; border-left: 4px solid {theme_color}; margin-bottom: 20px;">
            <h4 style="color: #a0a0b0; margin-top: 0;">🔍 Detailed AI Diagnostics</h4>
            <ul style="font-size: 1.05rem; color: #e0e0e0; padding-left: 20px; line-height: 1.6;">
                {insight_html}
            </ul>
        </div>
    """, unsafe_allow_html=True)
         
    st.markdown(f"""
        <div class="glass-card" style="text-align: left; border-left: 4px solid {theme_color};">
            <h4 style="color: #a0a0b0; margin-top: 0;">🚀 Strategic Action Plan</h4>
            <ul style="font-size: 1.05rem; color: #e0e0e0; padding-left: 20px; line-height: 1.6;">
                {rec_html}
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Navigation Buttons
st.write("<br>", unsafe_allow_html=True)
col_back, _, _ = st.columns([1, 2, 1])
with col_back:
    if st.button("📊 Back to Dashboard", use_container_width=True):
        st.switch_page("pages/2_📊_Dashboard.py")