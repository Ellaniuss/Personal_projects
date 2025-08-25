from dotenv import load_dotenv
import os
import requests
import pandas as pd

load_dotenv()

city = 'Ostrava'
KEY = os.getenv("KEY", "")

weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric'
response = requests.get(weather_url)
data = response.json()

weather_data = {
    'City' : city,
    'Temperature' : [data['main']['temp']],
    'Pressure' : [data['main']['pressure']],
    'humidity' : [data['main']['humidity']],
    'wind_speed' : [data['wind']['speed']]
}

df = pd.DataFrame(weather_data)
df.to_csv('weather.csv', index=False)

