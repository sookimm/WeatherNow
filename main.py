from weather import get_weather_info
from display import display_weather

def main():
    api_key = "0ddf701347267e3e36de5e566221d650"
    city = input("Enter city name: ")
    weather_info = get_weather_info(api_key, city)
    if weather_info:
        temperature, humidity, description = weather_info
        display_weather(temperature, humidity, description)
    else:
        print("City not found.")

if __name__ == "__main__":
    main()
