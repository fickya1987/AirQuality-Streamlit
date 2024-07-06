import streamlit as st
import datetime
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler

# Set up title and subheader for your app
st.title('"Welcome and Thank You for Using Our Air Quality Index Predictor Web App"')
st.subheader("Developers: ABC (Anna-Ben-Chris)")

# Capture today's date
today = st.date_input('Today is', datetime.datetime.now())
month = today.month
weekday = today.weekday()

# Header for application
st.header('What is the AQI (Air Quality Index) in Cleveland, Ohio?')

# Define the maximum levels for inputs
levels_max = {
    "CO": [250, 2000],
    "NO2": [250, 10000],
    "PM10": [250, 120],
    "PM2_5": [250, 50],
    "SO2": [250, 130],
    "O3": [250, 1000]
}

# Select model type via radio button
model_type = st.radio("Model:", ('Neural Network by AQI', 'Neural Network by Value'))

# Dynamically set the parameter limits based on the model type
param_max = 0 if model_type == 'Neural Network by AQI' else 1

# Initialize model
model_path = 'models/neural_net_model12.h5' if model_type == 'Neural Network by AQI' else 'models/neural_net_model12_raw.h5'
model = tf.keras.models.load_model(model_path, custom_objects={'mse': tf.keras.losses.MeanSquaredError()})

# Create sliders based on the selected model
CO_level = st.slider(f"Input the Carbon Monoxide Level (unit: {'AQI' if param_max == 0 else 'ppb or ug/L'})",
                     0, levels_max["CO"][param_max], 0)
NO2_level = st.slider(f"Input the Nitrogen Dioxide Level (unit: {'AQI' if param_max == 0 else 'ppt or ng/L'})",
                      0, levels_max["NO2"][param_max], 0)
PM10_level = st.slider("Input the PM10 Level", 0, levels_max["PM10"][param_max], 0)
PM2_5_level = st.slider("Input the PM2.5 Level", 0, levels_max["PM2_5"][param./.max], 0)
SO2_level = st.slider("Input the Sulfur Dioxide Level", 0, levels_max["SO2"][param_max], 0)
O3_level = st.slider(f"Input the Ozone Level (unit: {'AQI' if param_max == 0 else 'ppb or ug/L'})",
                     0, levels_max["O3"][param_max], 0)

# Preprocess user inputs
user_values = np.array([CO_level, NO2_level, PM10_level, PM2_5_level, SO2_level, O3_level, today.temperature, weekday, month])
ss = StandardScaler()
uv_scaled = ss.fit_transform(user_values.reshape(-1, 1))
knn = KNNImputer()
uv_knn = knn.fit_transform(uv_scaled)

# Make prediction
prediction = model.predict(uv_knn.reshape(1,uv_knn.shape[0]))
show_prediction = round(prediction[0][0])

# Background colors for AQI rating
bg_color = "#64e830"  # default to Good
rating_text = "(Good)"
if show_prediction > 300:
    bg_color = "#963939"
    rating_text = "(Hazardous)"
elif show_prediction > 200:
    bg_color = "#c66bc6"
    rating_text = "(Very Unhealthy)"
elif show_prediction > 150:
    bg_color = "#ff0000"
    rating_text = "(Unhealthy)"
elif show_prediction > 100:
    bg_color = "#ffb600"
    rating_text = "(Unhealthy for Sensitive Groups)"
elif show_prediction > 50:
    bg_color = "#f2e124"
    rating_text = "(Moderate)"

# Displaying the prediction result with color coding
st.markdown(f'<p style="background-color:{bg_color};font-size:2em;border-radius:2%;padding:5px">The predicted AQI is: {show_prediction}<br />{rating_text}</p>', unsafe_allow_html=True)
