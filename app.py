import streamlit as st
import pandas as pd
import pickle
import numpy as np
import sklearn

# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.9);
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        padding: 0.5rem 0;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff2525;
        transform: translateY(-2px);
    }
    .title-text {
        text-align: center;
        padding: 1rem;
        color: #333;
    }
    .prediction-box {
        background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,255,255,0.8));
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.3);
        animation: fadeIn 0.5s ease-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# Add background image with blur
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url("https://images.unsplash.com/photo-1582407947304-fd86f028f716");
        background-size: cover;
        background-position: center;
    }
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: inherit;
        filter: blur(5px);
        z-index: -1;
    }
    </style>
""", unsafe_allow_html=True)

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")
locations = df["location"].unique().tolist()
model = pickle.load(open('lrmodel.pkl', 'rb'))

# Title with custom styling
st.markdown("<h1 class='title-text'>House Price Predictor</h1>", unsafe_allow_html=True)

# Create a container for the main content
with st.container():
    st.markdown("### Please enter the details of the property")
    
    # Create three columns for better layout
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        location = st.selectbox("📍 Location", locations, help="Select the area where the house is located")
    
    with col2:
        bhk = st.number_input("🏠 BHK", min_value=1, max_value=10, value=2, help="Number of Bedrooms, Hall and Kitchen")
    
    with col3:
        bathrooms = st.number_input("🚿 Bathrooms", min_value=1, max_value=10, value=2, help="Number of bathrooms")
    
    # Second row for square feet
    col4, col5, col6 = st.columns([1, 1, 1])
    
    with col4:
        sqft = st.number_input("📏 Square Feet", min_value=100, max_value=20000, value=1000, help="Total area in square feet")
    
    # Prediction button and results
    if st.button("Calculate Price 💰"):
        try:
            input_df = pd.DataFrame([{
                'location': location,
                'total_sqft': float(sqft),
                'bath': int(bathrooms),
                'bhk': int(bhk)
            }])
            
            prediction = model.predict(input_df)[0] * 1000  # Multiply prediction by 1000
            
            st.markdown("---")
            st.markdown(f"""
                <div class='prediction-box'>
                    <h2 style='text-align: center; color: #333; margin-bottom: 1rem;'>Estimated Property Value</h2>
                    <h1 style='text-align: center; color: #ff4b4b; font-size: 2.5rem; margin: 1rem 0;'>₹ {prediction:,.2f}</h1>
                    <p style='text-align: center; color: #666; font-size: 0.9rem;'>This estimate is based on current market trends</p>
                </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error("Please check your input values and try again.")

# Add footer
st.markdown("---")
st.markdown("""
    <p style='text-align: center; color: #666;'>
        This is a machine learning-based prediction tool. Actual prices may vary.
    </p>
""", unsafe_allow_html=True)
