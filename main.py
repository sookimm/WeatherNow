import weather
import display
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def get_weather():
    city = request.form["city"]
    api_key = "0ddf701347267e3e36de5e566221d650"

    weather_data = weather.get_weather_data(api_key, city)
    display.display_weather(weather_data)

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run()
