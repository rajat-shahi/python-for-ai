import requests

def get_place(latitude,longitude):
    # url = f"GET https://bigdatacloud.net{latitude}&longitude={longitude}&localityLanguage=en"
    url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
    
    headers = {
        'User-Agent': 'weather-app-rajat' 
    }

    response = requests.get(url,headers=headers)
    data = response.json()
    # print(data)
    # print(dict.keys(data))
    return data["address"]["city"]
    


def get_weather(latitude,longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    city = get_place(latitude,longitude)

    response = requests.get(url)
    print(response)
    print(response.status_code)
    print(response.headers)
    print(response.text) #body as a string
    data = response.json() #JSON body converted into python data
    print(data) # print the dictionary we created 
    temperature = data["current"]["temperature_2m"]
    print(f"The current temperature in {city} is {temperature}")




latitude = 26.7606
longitude = 83.3732
get_weather(latitude=latitude,longitude=longitude)