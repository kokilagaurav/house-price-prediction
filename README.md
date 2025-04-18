# House Price Prediction

## Overview

This project is a web-based House Price Prediction tool built using Streamlit and machine learning. It allows users to estimate the price of a house based on key features such as location, number of bedrooms (BHK), number of bathrooms, and total square footage. The model leverages a trained regression algorithm to provide price estimates based on current market trends.

## Features

- **User-Friendly Interface:** Clean and modern UI built with Streamlit.
- **Custom Inputs:** Users can select location, specify BHK, bathrooms, and square footage.
- **Instant Prediction:** Get estimated property value instantly after entering details.
- **Attractive Design:** Includes background images, custom CSS, and responsive layout.

## How It Works

1. The user selects the location and enters property details.
2. The app processes the input and feeds it to a pre-trained regression model.
3. The model predicts the estimated price, which is displayed in a styled result box.

## Files

- `app.py`: Main Streamlit application file.
- `cleaned_data.csv`: Dataset containing cleaned property data.
- `lrmodel.pkl`: Pre-trained regression model used for predictions.

## Getting Started

1. Clone the repository or download the project files.
2. Ensure you have Python and required libraries installed (`streamlit`, `pandas`, `numpy`, `scikit-learn`, `pickle`).
3. Run the app using:
   ```
   streamlit run app.py
   ```
4. Open the provided local URL in your browser to use the app.

## Disclaimer

This tool provides price estimates based on historical data and machine learning. Actual property prices may vary due to market conditions and other factors.

---
