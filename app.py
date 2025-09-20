# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 15:16:43 2025

@author: DELL
"""

import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("log_model.pkl")

st.title("Delivery Prediction Model")
st.write("Provide the details below to predict if the delivery will be **On-time** or **Late**:")

# ------------------------------
# Feature 1: Agent Rating (1–6) → box input
f1 = st.number_input("Agent Rating", min_value=1, max_value=6, value=1, step=1)

# Feature 2: Pick-up Hour
f2 = st.number_input("Pick-Up Hour (minutes)", min_value=0, max_value=13, value=0, step=1)

# Feature 3: Traffic (categorical)
traffic_mapping = {'High ': 1, 'Jam ': 2, 'Low ': 3, 'Medium ': 4}
f3_label = st.selectbox("Traffic", list(traffic_mapping.keys()))
f3 = traffic_mapping[f3_label]

# Feature 4: Area (categorical)
area_mapping = {'Metropolitian ': 1, 'Other': 2, 'Semi-Urban ': 3, 'Urban ': 4}
f4_label = st.selectbox("Area", list(area_mapping.keys()))
f4 = area_mapping[f4_label]

# Feature 5: Weather (categorical)
weather_mapping = {'Cloudy': 1, 'Fog': 2, 'Sandstorms': 3, 'Stormy': 4, 'Sunny': 5, 'Windy': 6}
f5_label = st.selectbox("Weather", list(weather_mapping.keys()))
f5 = weather_mapping[f5_label]

# Feature 6: Agent Age
f6 = st.number_input("Agent Age", min_value=15, max_value=50, value=15, step=1)
# ------------------------------

# Prediction button
if st.button("Predict"):
    input_data = np.array([[f1, f2, f3, f4, f5, f6]])
    prediction = model.predict(input_data)[0]

    # Mapping for prediction
    prediction_mapping = {0: "On-time", 1: "Late"}
    result = prediction_mapping[prediction]

    # Display result
    if prediction == 0:
        st.success(f"Prediction: {result}")
    else:
        st.error(f" Prediction: {result}")
    

