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
# from PIL import Image
# img1 = Image.open("galogo.jpeg")
# st.image(img1, width =200)


st.title( '"Welcome and Thank you for using our Air Quality Index Predictor Web App"')
st.subheader(" Developers: ABC (Anna-Ben-Chris)")
#Date Input
import datetime
today = st.date_input('Today is', datetime.datetime.now())
month = today.month
weekday = today.weekday()


#Text title
#st.title('Air Quality Predictor Web App')

#Header/Subheader
st.header('What is the AQI (Air Quality Index) in Cleveland, Ohio? ')

# Initialize
temp_level_max = 110
CO_level_max = 250
no2_level_max = 250
pm10_level_max = 250
pm2_5_level_max = 250
so2_level_max = 250
o3_level_max = 250
CO_slider_txt = "Input the Carbon Monoxide Level (unit: AQI)"
no2_slider_txt = "Input the Nitrogen Dioxide Level (unit: AQI)"
o3_slider_txt = "Input the Ozone Level (unit: AQI)"

model_type = st.radio("Model:", ('Neural Network by AQI', 'Neural Network by Value'))
model = None
if(model_type == 'Neural Network by AQI'):
    model = tf.keras.models.load_model('../models/neural_net_model12.h5')
    CO_level_max = 250
    no2_level_max = 250
    pm10_level_max = 250
    pm2_5_level_max = 250
    so2_level_max = 250
    o3_level_max = 250
    CO_slider_txt = "Input the Carbon Monoxide Level (unit: AQI)"
    no2_slider_txt = "Input the Nitrogen Dioxide Level (unit: AQI)"
    o3_slider_txt = "Input the Ozone Level (unit: AQI)"
elif(model_type == 'Neural Network by Value'):
    model = tf.keras.models.load_model('../models/neural_net_model12_raw.h5')
    CO_level_max = 2000
    no2_level_max = 10000
    pm10_level_max = 120
    pm2_5_level_max = 50
    so2_level_max = 130
    o3_level_max = 1000
    CO_slider_txt = "Input the Carbon Monoxide Level (unit: ppb or ug/L)"
    no2_slider_txt = "Input the Nitrogen Dioxide Level (unit: ppt or ng/L)"
    o3_slider_txt = "Input the Ozone Level (unit: ppb or ug/L)"



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

temp_level = st.slider("Input the Temperature (F)", -10, temp_level_max, get_temp)

CO_level = st.slider(CO_slider_txt, 0, CO_level_max, get_co)

no2_level = st.slider(no2_slider_txt, 0, no2_level_max, get_no2)

pm10_level= st.slider("Input the pm10 Level", 0, pm10_level_max, get_pm10)

pm2_5_level = st.slider("Input the pm2.5 Level", 0, pm2_5_level_max, get_pm25)

so2_level = st.slider("Input the Sulfur Dioxide Level", 0, so2_level_max, get_so2)

o3_level = st.slider(o3_slider_txt, 0, o3_level_max, get_o3)

#with open('baseline_model1.pkl', 'rb') as f:
    #model = pickle.load(f)

#user_values = np.array([np.nan, np.nan, np.nan, CO_level, np.nan, no2_level, np.nan, o3_level, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, temp_level, month, weekday])
#prediction = model.predict(user_values.reshape(1,-1))

#st.header(f'The predicted AQI is: {prediction[0]}')

# with open('saved-aqi-basic-model.pkl', 'rb') as f: 
#     model = pickle.load(f)

# user_values = np.array([ temp_level, CO_level, no2_level, pm10_level, pm2_5_level])
if(model_type == 'Neural Network by Value'):
    CO_level = CO_level/1000
    no2_level = no2_level/1000
    o3_level = o3_level/1000

user_values = np.array([ CO_level, no2_level, pm10_level, pm2_5_level, so2_level, o3_level, temp_level, weekday, month ])

ss = StandardScaler()
uv_scaled = ss.fit_transform(user_values.reshape(-1, 1))
knn = KNNImputer()
uv_knn = knn.fit_transform(uv_scaled)

# prediction = model.predict(user_values.reshape(1,-1))
prediction = model.predict(uv_knn.reshape(1,uv_knn.shape[0]))

show_prediction = round(prediction[0][0])

bg_color = "#64e830"
rating_text = "(Good)"
if(show_prediction > 300):
    bg_color = "#963939"
    rating_text = "(Hazardous)"
elif(show_prediction > 200):
    bg_color = "#c66bc6"
    rating_text = "(Very Unhealthy)"
elif(show_prediction > 150):
    bg_color = "#ff0000"
    rating_text = "(Unhealthy)"
elif(show_prediction > 100):
    bg_color = "#ffb600"
    rating_text = "(Unhealthy for Sensitive Groups)"
elif(show_prediction > 50):
    bg_color = "#f2e124"
    rating_text = "(Moderate)"
else:
    bg_color = "#64e830"
    rating_text = "(Good)"

# st.header(f'The predicted AQI is: {show_prediction}')
st.markdown(f'<p style="background-color:{bg_color};font-size:2em;border-radius:2%;padding:5px">The predicted AQI is: {show_prediction}<br />{rating_text}</p>', unsafe_allow_html=True)



#load data
df = pd.read_csv('clean_aqi.csv')

show_df = st.checkbox("Click here to view the raw data")
if show_df:
    df

# Images
from PIL import Image
img = Image.open("airquality.jpeg")
st.image(img, width =600)


