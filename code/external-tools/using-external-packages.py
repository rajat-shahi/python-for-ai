import pandas as pd

data = {
    'name' : ["Alice","Bob","Charlie"],
    'age' : [25,30,21],
    'city' : ["NYC","LA","Chicago"]
}

df = pd.DataFrame(data)
print(df)



"""
NOTE : 
- be aware of the naming conflicts

import datetime
datetime = "2026-01-01"

- now the module is gone because it overwrites built-in
- correct way is to use the different name
"""