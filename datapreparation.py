# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vJEVeNQm5G3Ie4O9cGwLIA6zPKbqcFsV

# DATA PREPARATION
"""

import pandas as pd
import numpy as np
import seaborn as sns

"""IMPORTING DATA"""

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv "
df = pd.read_csv(url)
df.head()

"""GETTING TO KNOW YOUR DATA SET"""

#describe my dataset
df.describe()

#shape my dataset
df.shape

"""HANDLING DUPLICATES"""

#check if there are duplicates
df.duplicated().sum()

"""HANDLING NULL VALUES"""

#check for null values
df.isnull().sum()

"""DROPPING NULL VALUES"""

#dropping all null values
df.dropna(inplace=True)
#dropping a specific column
df1 = df.dropna(subset=['total_cases'])

"""IMPUTATION"""

#numerical values
#using mean
df['total_cases'] = df['total_cases'].fillna(df['total_cases'].mean())
#using median
df['total_cases'] = df['total_cases'].fillna(df['total_cases'].median())

#categorical values
#select any column with categorical values, impute using mode
df['continent'] = df['continent'].fillna(df['continent'].mode()[0])

"""Drooping columns"""

#drop column named iso_code
df.drop('iso_code', axis=1, inplace=True)
#drop column named new_deaths_smoothed
df.drop('new_deaths_smoothed', axis=1, inplace=True)

"""Getting a subset of your data"""

#get subset data for Zimbabwe and Rwanda
subset = df[(df['location'] == 'Zimbabwe') | (df['location'] == 'Rwanda')]
#displaying the subset
subset.head()

#saving the data
df.to_csv('url')