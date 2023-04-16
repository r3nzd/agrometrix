import requests
import json

#define api
url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "eebd57fbb4e552348a4db5c7fca324de"

# ask user to enter lat and long
print("If you don't know your latitude and logitude, goto https://www.latlong.net/.")
lat = input("Enter the latitude of your location: ")
lon = input("Enter the longitude of your location: ")

# create api request
params = {"lat": lat, "lon": lon, "appid": api_key}

# send the request and parsing the json 
response = requests.get(url, params=params)
data = json.loads(response.text)

# extract stuff 
temp = data["main"]["temp"] - 273.15  # convert temperature from kelvin to celsius
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"] * 18 / 5 # convert into km/h
weather_desc = data["weather"][0]["description"]

# print the data 
print("Average temperature: {:.2f}°C".format(temp))
print("Average humidity: {}%".format(humidity))
print(f"Wind Speed: {wind_speed} km/h")
print(f"Weather Condition: {weather_desc}")

# provide suggestion part 1 (based of the temprature)
if temp < 10:
    print("It is too cold for most crops. Consider planting cold-resistant varieties.")
elif temp > 30:
    print("It is too hot for most crops. Consider providing shade or using irrigation to cool the soil.")
else:
    print("Weather conditions are suitable for most crops.")

#provide suggestioon part 2 (based of the wind speed)
if wind_speed < 1:
    print("The wind is calm. No suggestion.")
elif wind_speed < 6:
    print("The wind speed is low. Suitable for farming.")
elif wind_speed < 12:
    print("The wind speed is moderate. Some precautions may be needed.")
else:
    print("The wind speed is high. Farming may not be suitable.")