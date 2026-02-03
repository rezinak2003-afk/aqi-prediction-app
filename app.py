import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="AQI Prediction App", layout="centered")
st.title("Air Quality Index (AQI) Prediction")
st.write("Predict the Air Quality Index (AQI) based on input parameters.")

# Load the trained model
model = joblib.load("LR_AQI_Prediction.joblib")

# Input fields
pm25 = st.number_input("PM2.5", min_value=0.0, max_value=500.0, value=50.0)
pm10 = st.number_input("PM10", min_value=0.0, max_value=500.0, value=80.0)
no2 = st.number_input("NO2", min_value=0.0, max_value=300.0, value=40.0)
so2 = st.number_input("SO2", min_value=0.0, max_value=300.0, value=20.0)
co = st.number_input("CO", min_value=0.0, max_value=10.0, value=1.0)
temperature = st.number_input("Temperature (°C)", min_value=-30.0, max_value=50.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)

# AQI category function
def aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

# Prediction button
if st.button("Predict AQI"):

    # IMPORTANT FIX: DataFrame with feature names
    input_data = pd.DataFrame(
        [[pm25, pm10, no2, so2, co, temperature, humidity]],
        columns=["PM2.5", "PM10", "NO2", "SO2", "CO", "Temperature", "Humidity"]
    )

    prediction = model.predict(input_data)

    st.success(f"Predicted AQI Value: {round(prediction[0], 2)}")
    st.info(f"AQI Category: {aqi_category(prediction[0])}")
