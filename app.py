import streamlit as st
import pandas as pd
import pickle
import numpy as np
import sklearn


# Load cleaned data

df = pd.read_csv("cleaned_data.csv")  # Update with the correct file path if needed


locations = df["location"].unique().tolist()  # Extract unique locations

model = pickle.load(open('lrmodel.pkl', 'rb'))


# Title
st.title("Welcome to House Price Predictor")

# Layout
col1, col2 = st.columns([2, 2])
col3, col4 = st.columns([2, 2])

# Dropdown for dynamic location selection
location = col1.selectbox("Select the Location:", locations)

# Input fields for house features
bhk = col2.text_input("Enter BHK:", "4")
bathrooms = col3.text_input("Enter Number of Bathrooms:", "3")
sqft = col4.text_input("Enter Square Feet:", "2000")

# Button to trigger prediction


if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        'location': location,
        'total_sqft': sqft,
        'bath': bathrooms,
        'bhk': bhk
    }])

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Show result
    st.markdown(f"### Prediction: ₹ {prediction:,.2f}")
