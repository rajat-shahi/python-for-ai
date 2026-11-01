import pandas as pd
import os

df = pd.read_csv("files/server-metrics-missing.csv")
print(df)

df.columns
df["instance"] # select one column
df[["instance","cpu","memory"]] # select multiple columns


# selecting rows using iloc 
# iloc - using integers
# loc - index labels and column labels


df.iloc[0] #first row
df.iloc[1:3] #from row 2 to 3 (index 1 to 2)
df.iloc[2,3] # 3rd row, 4th column 

df.loc[0]
df.loc[0:2,["instance","cpu","memory"]]