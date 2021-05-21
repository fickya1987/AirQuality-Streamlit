from altair.vegalite.v4.schema.channels import Color
import streamlit as st
# import plotly.express as px
import datetime
import numpy as np
import pandas as pd

import pickle
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler


#image
from PIL import Image
img1 = Image.open("galogo.jpeg")
st.image(img1, width =200)


st.title( '"Welcome and Thank you for using our Air Quality Index Predictor Web App"')
st.subheader(" Developpers: ABC (Anna-Ben-Chris)")
#Date Input
import datetime
today = st.date_input('Today is', datetime.datetime.now())

month = today.month
weekday = today.weekday()


#Text title
#st.title('Air Quality Predictor Web App')

#Header/Subheader

st.header('What is the AQI (Air Quality Index) in Cleveland, Ohio? ')


#load data

df = pd.read_csv('clean_aqi.csv')
#df

show_df = st.checkbox("Click here to view the raw data")

if show_df:
    df


# Images
from PIL import Image
img = Image.open("airquality.jpeg")
st.image(img, width =600)


# read data, these values:
#'co_aqi_val', 'no2_aqi_val', 'pm10_aqi_val', 'pm2.5_aqi_val', 'so2_aqi_val', 'ozone_aqi_val', 'temp_avg'


#load data
get_temp = 50
get_co = 0
get_no2 = 0
get_pm10 = 0
get_pm25 = 0
get_so2 = 0
get_o3 = 0

#get user input
# Slider

temp_level = st.slider("Input the Temperature (F)", -10,110, get_temp)

CO_level = st.slider("Input the Carbon Monoxide Level", 0,10, get_co)

no2_level = st.slider("Input the Nitrogen Dioxide Level", 0,50, get_no2)

pm10_level= st.slider("Input the pm10 Level", 0,100, get_pm10)

pm2_5_level = st.slider("Input the pm2.5 Level", 0,100, get_pm25)

so2_level = st.slider("Input the Sulfur Dioxide Level", 0,100, get_so2)

o3_level = st.slider("Input the Ozone Level", 0,100, get_o3)

#with open('baseline_model1.pkl', 'rb') as f:
    #model = pickle.load(f)

#user_values = np.array([np.nan, np.nan, np.nan, CO_level, np.nan, no2_level, np.nan, o3_level, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, temp_level, month, weekday])
#prediction = model.predict(user_values.reshape(1,-1))

#st.header(f'The predicted AQI is: {prediction[0]}')

# with open('saved-aqi-basic-model.pkl', 'rb') as f: 
#     model = pickle.load(f)
model = tf.keras.models.load_model('../models/neural_net_model12.h5')

# user_values = np.array([ temp_level, CO_level, no2_level, pm10_level, pm2_5_level])
user_values = np.array([ CO_level, no2_level, pm10_level, pm2_5_level, so2_level, o3_level, temp_level, weekday, month ])

ss = StandardScaler()
uv_scaled = ss.fit_transform(user_values.reshape(-1, 1))
knn = KNNImputer()
uv_knn = knn.fit_transform(uv_scaled)

# prediction = model.predict(user_values.reshape(1,-1))
prediction = model.predict(uv_knn.reshape(1,uv_knn.shape[0]))

show_prediction = round(prediction[0][0])

st.header(f'The predicted AQI is: {show_prediction}')


