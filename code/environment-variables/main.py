import os

#read from environment 
api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_NAME")

print(f"Using Database : {database}")

