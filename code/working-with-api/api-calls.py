import requests 
latitude = 26.7606
longitude = 83.3732

# building api URL with the required parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"


# make the request
response = requests.get(url)
print(response)
print(response._content)

data = response.json()
print(data)


print(f"Current temperatur : {data['current']['temperature_2m']}")