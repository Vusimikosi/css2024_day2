#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:15:19 2024

@author: vusani
"""

import pandas as pd

df = pd.read_csv("country_data_index.csv")

df = pd.read_csv("Geospatial Data.txt",sep=";")
print(df)
print(df.info())
print(df.describe())

df = pd.read_excel("/Users/vusani/Documents/day2_repractice/residentdoctors.xlsx")
df = pd.read_json("student_data.json")

df = pd.read_csv("country_data_index.csv")
df = pd.read_csv("country_data_index.csv",index_col=0)

df = pd.read_csv("patient_data.csv")
column_names = ["duration", "pulse", "max_pulse", "calories"]
df = pd.read_csv("patient_data.csv", header=None, names=column_names)

df = pd.read_excel("residentdoctors.xlsx")
df['LOWER_AGE'] = df['AGEDIST'].str.extract('(\d+)-')
print(df['LOWER_AGE'])
df['LOWER_AGE'] = df['LOWER_AGE'].astype(int)

df = pd.read_csv("time_series_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%y')
df['Year'] = df['Date']. dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day


df = pd.read_csv("patient_data_dates.csv")
print(df)
df.drop(['Index'],inplace=True,axis=1)

x = df["Calories"].mean()
x = df["Calories"].fillna(x, inplace = True)

df['Date'] = pd.to_datetime(df['Date'])
df.dropna(inplace=True)
df = df.reset_index(drop=True)
























