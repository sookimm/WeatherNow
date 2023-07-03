import requests

def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def get_weather_info(api_key, city):
    data = get_weather_data(api_key, city)
    if "main" in data:
        temperature = data["main"].get("temp")
        humidity = data["main"].get("humidity")
        description = data["weather"][0].get("description")
        return temperature, humidity, description
    else:
        return None

