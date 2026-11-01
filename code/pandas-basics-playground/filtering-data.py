# we want to find servers where CPU  > 80%

import pandas as pd

df = pd.read_csv("files/server-metrics-missing.csv")
print(df)


print(f"CPU greater than 80%\n{len("CPU greater than 80%")*"-"}")

high_cpu = df[df["cpu"]>80]
print(high_cpu)


specific_instances = df[df["instance"].isin(["ins-3","ins-5"])]
print(specific_instances)
