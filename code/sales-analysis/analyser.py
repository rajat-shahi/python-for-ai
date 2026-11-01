import os 

# check if we are in the right place
print("Current Directory : ", os.getcwd())

# check if our data file exists 
data_path = "data/sales.csv"

if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Please make sure you are running this from the sales-analysis folder")