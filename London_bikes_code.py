# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 18:59:44 2023

@author: piotr
"""

# import the pandas library
# pip install pandas
import pandas as pd 
# import zipfile
import zipfile 
# import kaggle library
# import kaggle 
# download dataset from kaggle using the kaggle API
#!kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset # download dataset from kaggle using the kaggle API
import os 
path = 'D:\PythonVS\data'
os.chdir(path)
os.getcwd()

# extract the file from the dowloaded zip file
zipfile_name = 'london-bike-sharing-dataset.zip'
with zipfile.ZipFile(zipfile_name, 'r') as file:
    file.extractall()

# read in the csv file as a pandas dataframe
bikes = pd.read_csv('london_merged.csv')

# explore the data
bikes.info()
bikes.shape
bikes

# count the unique values in the weather_code column
bikes.weather_code.value_counts()

# count the unique values in the season column
bikes.season.value_counts()

# specifying the column names that I want to use

new_cols_dict ={
    'timestamp':'time',
    'cnt':'count',
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kmp',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
    }

# renaming the columns to the specified column names
bikes.rename(new_cols_dict, axis=1, inplace=True)

# changing the humidity values to percentage (i.e. a value between 0 and 1)
bikes.humidity_percent = bikes.humidity_percent / 100

# creating a season dictionary so that we can map the integers 0-3 to the actual values
season_dict = {
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'autumn',
    '3.0':'winter'
    }

# creating a weather dictionary so that we can map the integers to the actual written values
weather_dict = {
    '1.0':'Clear',
    '2.0':'Scattered clouds',
    '3.0':'Broken clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'Snowfall'
    }

# changing the season column data type to string
bikes.season = bikes.season.astype('str')

# mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dict)

# changing the weather column data type to string
bikes.weather = bikes.weather.astype('str')

# mapping the weather column data type to string 
bikes.weather = bikes.weather.map(weather_dict)

# checking our dataframe to see if the mapping have worked
bikes.head()

# writing the final dataframe to an excel file that I will use in the Tableau visualizations. The file will be the 'london_bikes_final'
bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data')