import pandas as pd
from helpers import calculate_total,format_currency

# read data
df = pd.read_csv("data/sales.csv")
print(df)

# calculate total for each row 
totals = []
for index,row in df.iterrows():
    total = calculate_total(row['quantity'],row['price'])
    totals.append(total)


# add totals to the dataframe
df['total'] = totals 
print(df)

# display the data with formatted totals 
print("\nSales Data:")
print("-"*len("Sales Data:"))
for index,row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row["product"]} : {formatted_total}")

# show grand total 
grand_total = df['total'].sum()
formatted_grand_total= format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")