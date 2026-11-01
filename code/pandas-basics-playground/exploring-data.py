import pandas as pd 
import os 

df = pd.read_csv("files/server-metrics-missing.csv")
print(df)

df.head()
df.tail()
row , col = df.shape
print(f"row = {row} , col = {col}")

df.columns
df.info()

df.describe()
df.dtypes
df.sample(5)