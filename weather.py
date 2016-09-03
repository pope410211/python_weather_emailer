import requests

def get_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Orlanod,FL&units=imperial&appid={{open_weather_api_key_here}}
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    description = weather_json['weather'][0]['description']
    min_temp = weather_json['main']['temp_min']
    max_temp = weather_json['main']['temp_max']

    forecast = "Today's forecast is " + description
    forecast += " with a high of " + str(int(max_temp)) + " and a low of " + str(int(min_temp)) + "."

    return forecast
