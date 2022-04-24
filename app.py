# Imports.
import requests

#OpenWeather API key;
API_KEY = ''

user_selected_city = ''
while (not user_selected_city):
    user_selected_city = input('Enter city: ')
    if (user_selected_city == ''):
        print('Please try again.')

#API call;
weather_data = requests.get(
    f'https://api.openweathermap.org/data/2.5/weather?q={user_selected_city}&units=imperial&APPID={API_KEY}'
)

#Display API call results;
if (weather_data.json()['cod'] == '404'):
    print('No city found. Please try again.')
else:
    current_weather = weather_data.json()['weather'][0]['main']
    current_temperature = round(weather_data.json()['main']['temp'])
    current_feels_like_temperature = round(weather_data.json()['main']['feels_like'])
    user_selected_city = weather_data.json()['name']
    
    print(f'The current weather in {user_selected_city} is: {current_weather}.')
    print(f'The temperature is {current_temperature}°F and feels like {current_feels_like_temperature}°F.')
    print('Thank you!')