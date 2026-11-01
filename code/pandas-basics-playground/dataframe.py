import pandas as pd 

data = {
    "instance" : ["ins-1","ins-2","ins-3","ins-4"],
    "cpu":[20,80,72,91],
    "memory":[15,77,52,90],
    "requests":[100,1000,750,1500]
}

print(data)

df = pd.DataFrame(data)
print(df)

# data - python dictionary 
# pd.DataFrame(data) - converts it to dataframe
# 'df' is our dataframe variable
