from flask import Flask, render_template, request
from weather import get_weather_info

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        api_key = "0ddf701347267e3e36de5e566221d650"
        city = request.form.get("city")
        weather_info = get_weather_info(api_key, city)
        if weather_info:
            temperature, humidity, description = weather_info
            weather_data = {
                "temperature": temperature,
                "humidity": humidity,
                "description": description
            }
            return render_template("index.html", weather=weather_data)
        else:
            return render_template("index.html", error="City not found.")
    return render_template("index.html")

def display_weather(temperature, humidity, description):
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")

if __name__ == "__main__":
    app.run(debug=True)

