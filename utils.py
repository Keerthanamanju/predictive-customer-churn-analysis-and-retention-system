import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_models():
    """Loads the trained model, scaler, and encoder."""
    model = joblib.load('churn_lr_model.pkl')
    scaler = joblib.load('scaler.pkl')
    encoder = joblib.load('target_encoder.pkl')
    return model, scaler, encoder

@st.cache_data
def load_data():
    """Loads the dataset for the dashboard."""
    df = pd.read_csv("customer churn.csv")
    return df

def apply_custom_css():
    """Injects the dark theme, neon glow, and glassmorphism CSS."""
    st.markdown("""
        <style>
        .stApp {
            background-color: #0d0d14;
            color: #ffffff;
        }
        h1, h2, h3 {
            color: #ffffff;
            text-shadow: 0 0 10px #b829ea, 0 0 20px #b829ea;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(184, 41, 234, 0.3);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
            text-align: center;
            transition: transform 0.3s ease;
            margin-bottom: 20px;
        }
        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(184, 41, 234, 0.4);
        }
        .metric-value {
            font-size: 2.5rem;
            font-weight: bold;
            color: #b829ea;
            text-shadow: 0 0 5px #b829ea;
        }
        .metric-label {
            font-size: 1.2rem;
            color: #a0a0b0;
        }
        div.stButton > button {
            background: linear-gradient(90deg, #b829ea 0%, #7b2cbf 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 24px;
            font-weight: bold;
            box-shadow: 0 0 15px rgba(184, 41, 234, 0.5);
            width: 100%;
        }
        div.stButton > button:hover {
            box-shadow: 0 0 25px rgba(184, 41, 234, 0.8);
        }
        </style>
    """, unsafe_allow_html=True)