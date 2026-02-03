import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="AQI Prediction App", layout="centered")
st.title("Air Quality Index (AQI) Prediction")

# Load model
model = joblib.load("LR_AQI_Prediction.joblib")

# Inputs
pm25 = st.number_input("PM2.5", min_value=0.0)
pm10 = st.number_input("PM10", min_value=0.0)
no2  = st.number_input("NO2", min_value=0.0)
so2  = st.number_input("SO2", min_value=0.0)
co   = st.number_input("CO", min_value=0.0)
o3   = st.number_input("O3", min_value=0.0)

if st.button("Predict AQI"):
    input_data = np.array([[pm25, pm10, no2, so2, co, o3]])  # 👈 VERY IMPORTANT
    prediction = model.predict(input_data)
    st.success(f"Predicted AQI: {prediction[0]:.2f}")
