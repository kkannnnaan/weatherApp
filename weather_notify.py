import requests
from plyer import notification
import time

API_KEY = '7dbd1664d13305925650c207624c143c'  # Replace with your API key

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric'
    try:
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            weather = data['weather'][0]['description'].title()
            temp = data['main']['temp']
            return f"{city}: {weather}, {temp}°C"
        else:
            return None
    except Exception as e:
        return None

def notify_weather(city):
    weather_info = get_weather(city)
    if weather_info:
        print(weather_info)
        # notification.notify(
        #     title="Live Weather Update",
        #     message=weather_info,
        #     timeout=10
        # )
    else:
        print(f"City '{city}' not found or API error.")

if __name__ == '__main__':
    while True:
        city = input("Enter city name in India (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        notify_weather(city)