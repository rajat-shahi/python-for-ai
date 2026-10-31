# end goal : find the temperature for the last 7 days for Delhi
import requests 
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os


# calculate the dates 
time_now = datetime.now()
time_week_ago = time_now - timedelta(days=7)
print(f"TIME NOW : {time_now} \n TIME WEEK AGO : {time_week_ago}")


#format dates for API (YYYY-MM-DD)
start_date = time_week_ago.strftime("%Y-%m-%d")
end_date = time_now.strftime("%Y-%m-%d")
print(start_date,end_date)

url = f"https://api.open-meteo.com/v1/forecast?latitude=28.64&longitude=77.21&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
# print(data)

print(f"The temperature of Delhi for the last 7 days :")
print(46*"-")

for i in range(1,8):
    print(f"{data["daily"]["time"][i]} => {data["daily"]["temperature_2m_max"][i]}")


# - - - - - - - - - - - - -- - - - - - - - -- - - - - -- - - - --- - - - - 

# let's play a little with 'PANDAS' 

daily_data = data["daily"]

df = pd.DataFrame({
    "date": daily_data["time"],
    "max_temp" : daily_data["temperature_2m_max"],
    "min_temp" : daily_data["temperature_2m_min"]
})

# print(df)

# convert the date strings to datetime
print(type(df["date"][0]))
df["date"] = pd.to_datetime(df["date"])
print(df)
print(type(df["date"][0]))



# - - - - - - - - - - - - -- - - - - - - - -- - - - - -- - - - --- - - - - 

plt.figure(figsize=(10,6))
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Delhi Weather - Past 7 days")
plt.plot(df["date"],df["max_temp"],marker="o",label="Max Temperature")
plt.plot(df["date"],df["min_temp"],marker="o",label="Min Temperature")
plt.legend()


# rotate the x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# save the plot
pwd = os.getcwd()
plt.savefig(f"{pwd}/weather_chart.png")
plt.show()

# save the data to CSV
if not os.path.exists("data"):
    os.makedirs("data")

# save to CSV 
df.to_csv('data/delhi_weather.csv',index=False)
print("Data saved to data/delhi_weather.csv")