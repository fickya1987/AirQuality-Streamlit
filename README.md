# Project 5
# *Air Pollutants and Air Quality Index*


## Contents
 - [Problem Statement](#Problem-Statement)
 - [Executive Summary](#Executive-Summary)
 - [File Directory](#File-Directory)
 - [Data](#Data)
 - [Data Dictionary](#Data-Dictionary)
 - [Conclusions and Recommendations](#Conclusions-and-Recommendations)
 - [Areas for Further Research/Study](#Areas-for-Further-Research/Study)
 - [Sources](#Sources)
 - [Visualizations](#Visualizations)


## Problem Statement
[back to top](#Project-5)

We plan to explore the relationship between daily pollutant values and daily temperature readings with overall air quality scores. We will base our model on EPA pollutant data and daily temperature reading in Cleveland, OH from 2017-2019. Our goal is to create an application to help accurately predict a daily air quality index for the residents of Cleveland, OH with the hopes of giving guidance for residents suffering from respiratory illnesses.



## Executive Summary
[back to top](#Project-5)

### *This section should include:*
 - *a brief overview of your process*
 - *models used*
 - *important findings and/or*
 - *metrics, model performance, etc.*
 - *and a brief summary of conclusions and recommendations.*


## File Directory
[back to top](#Project-5)

05-Project<br />
|<br />
|__ code<br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 00_table_of_contents.ipynb <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 01_cleaning.ipynb <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 02_eda.ipynb <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 03_eda_visualizations.ipynb <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 04_modelling_with_regression.ipynb <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 05_modelling_with_time_series.ipynb <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 06_production_model.ipynb <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 07_streamlit_app.ipynb <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 08_conclusion.ipynb <br />
|<br />
|__ data <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_CO.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_NO2.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_O3.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_Pb.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_PM10.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_PM2.5.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_SO2.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2018_all_cleveland_oh_CO.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2018_all_cleveland_oh_NO2.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2018_all_cleveland_oh_O3.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2018_all_cleveland_oh_PM10.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2018_all_cleveland_oh_PM2.5.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2018_all_cleveland_oh_SO2.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2019_all_cleveland_oh_CO.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2019_all_cleveland_oh_NO2.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2019_all_cleveland_oh_O3.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2019_all_cleveland_oh_PM10.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2019_all_cleveland_oh_PM2.5.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2019_all_cleveland_oh_SO2.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ cleaned_aqi_and_temp_data_2017-2019.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ ClevelandOHweather2017.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ ClevelandOHweather2018.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ ClevelandOHweather2019.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ combo_df.csv <br />
|<br />
|__ images <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ nothing.png <br />
|<br />
|__ presentation <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ presentation.pdf <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ presentation.pptx <br />
|<br />
|__ README.md <br />
|__ LICENSE <br />


## Data
[back to top](#Project-5)

Data about pollution and AQI values per pollutant were pulled from the [Download Daily Data](https://www.epa.gov/outdoor-air-quality-data/download-daily-data) section of the [EPA website](https://www.epa.gov/). All data was observed at the George T. Craig National Core (NCore) Monitoring Station in Cleveland, Ohio during 2017, 2018, and 2019.

Temperature data about Cleveland, Ohio was taken from the [Cleveland.com website](https://www.cleveland.com/datacentral/2008/09/cleveland_weather_history_find.html).

*(Please see the __[Sources](#Sources)__ section below for all of the sources we used to make informed decisions about using this data.)*



## Data Dictionary
[back to top](#Project-5)

| Feature            | Python Type | Data Type  | Descritpion   |
| ---                | ---         | ---        | ---           |
| date (index)       | datetime    | Continuous | Date when observations were made  |
| high_temp          |   int64     | Continuous | Highest Temperature measured for the day (in degrees Fahrenheit) |
| low_temp           |   int64     | Continuous | Lowest Temperature measured for the day (in degrees Fahrenheit) |
| co_max             | float64     | Continuous | Amount of Carbon Monoxide measured in ppm |
| co_aqi_val         | float64     | Continuous | AQI value of Carbon Monoxide |
| no2_max            | float64     | Continuous | Amount of Nitrogen Dioxide measured in ppb |
| no2_aqi_val        | float64     | Continuous | AQI value of Nitrogen Dioxide |
| ozone_max          | float64     | Continuous | Amount of Ozone measured in ppm |
| ozone_aqi_val      | float64     | Continuous | AQI value of Ozone |
| pm10_mean          | float64     | Continuous | Average amount of 10um Particulate Matter measured in ug/m<sup>3</sup> |
| pm10_aqi_val       | float64     | Continuous | AQI value of 10um Particulate Matter |
| pm2.5_mean         | float64     | Continuous | Average amount of 2.5um Particulate Matter measured in ug/m<sup>3</sup> |
| pm2.5_aqi_val      | float64     | Continuous | AQI value of 2.5um Particulate Matter |
| so2_max            | float64     | Continuous | Amount of Sulfur Dioxide measured in ppb |
| so2_aqi_val        | float64     | Continuous | AQI value of Sulfur Dioxide |
| cumulitive_aqi     | float64     | Continuous | Calculated AQI for the day by taking the maximum value from all pollutants |
| pct_change_aqi     | float64     | Continuous | Percent changed in AQI from previous day |
| average_daily_temp | float64     | Continuous | Calculated Average Temperature (in degrees Fahrenheit; Mean of Highest and Lowest Temperatures) |
| month              | float64     | Nominal    | Month denoted by numeric value one through twelve |
| weekday            | float64     | Nominal    | Day of the week, assuming the week starts on Monday, which is denoted by 0 and ends on Sunday which is denoted by 6 |




## Conclusions and Recommendations
[back to top](#Project-5)


## Areas for Further Research/Study
[back to top](#Project-5)


## Sources
[back to top](#Project-5)

https://www.epa.gov/outdoor-air-quality-data/download-daily-data <br/>
https://www.cleveland.com/datacentral/2008/09/cleveland_weather_history_find.html <br/>
https://www.airnow.gov/sites/default/files/2020-05/aqi-technical-assistance-document-sept2018.pdf <br/>
https://www.epa.state.oh.us/portals/27/ams/plans/NCORE-GTCraig.pdf <br/>
https://www.breeze-technologies.de/blog/what-is-an-air-quality-index-how-is-it-calculated/ <br/>


## Visualizations
[back to top](#Project-5)
- *Any important visualizations*
- *These can be included in the Executive Summary or Conclusions/Recommendations, or as its own section.*
- *Use good judgement! Include a few here that really highlight your findings.*


