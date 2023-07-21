import json
import requests

API_KEY = 'e6a59121b6d3be147a8f1ae0f22702a2'
city_name = "Seoul,KR"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

response = requests.get(url).json()
temp = response['main']['temp']
temp -= 273.15
print(temp)