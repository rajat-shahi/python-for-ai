import pandas as pd
import os
# reading CSV and JSON (we can read other extensions as well)
df1 = pd.read_csv("files/server-metrics.csv")
print(df1)

df2 = pd.read_csv("files/server-metrics-missing.csv")
print(df2)

df3 = pd.read_json("files/server-metrics.json")
print(df3)


# save to CSV 
if os.path.exists("output"):
    df3.to_csv("output/server-metrics-output.csv", index=False)
    df3.to_csv("output/server-metrics-output.xlsx", index=False)
    print("✅ The directory exists")
else:
    print("❌The directory doesn't exists")
    print("Creating the directory . . . . .")
    os.makedirs("output",exist_ok=True)
    df3.to_csv("output/server-metrics-output.csv", index=False)
    df3.to_csv("output/server-metrics-output.xlsx", index=False)