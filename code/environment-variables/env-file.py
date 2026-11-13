import os

from dotenv import load_dotenv

# load the .env file
load_dotenv()


# read from the environment
api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE")

print(f"Api Key = {api_key}")
print(f"Database : {database}")
