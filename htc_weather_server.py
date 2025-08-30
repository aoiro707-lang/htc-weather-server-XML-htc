from flask import Flask, request, Response, jsonify
import requests

app = Flask(__name__)

API_KEY = "0c60b2b833632e5c653f6c29dada5dfa"  # OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Hàm ánh xạ điều kiện OWM -> HTC
def map_condition(owm_condition):
    mapping = {
        "Clear": "Sunny",
        "Clouds": "Cloudy",
        "Rain": "Showers",
        "Drizzle": "LightRain",
        "Thunderstorm": "Thunder",
        "Snow": "Snow",
        "Mist": "Fog",
        "Fog": "Fog",
        "Haze": "Fog",
        "Dust": "Hazy",
        "Sand": "Hazy",
        "Ash": "Hazy",
        "Squall": "Windy",
        "Tornado": "Windy"
    }
    return mapping.get(owm_condition, "Unknown")

@app.route("/getstaticweather")
def get_static_weather():
    loc = request.args.get("locCode", "Hanoi")
    params = {"q": loc, "appid": API_KEY, "units": "metric"}
    r = requests.get(BASE_URL, params=params)
    data = r.json()

    if "main" not in data:
        return Response("<error>Location not found</error>", mimetype="application/xml")

    condition = map_condition(data["weather"][0]["main"])

    xml_response = f"""<?xml version='1.0' encoding='UTF-8'?>
<weather>
    <location>{data['name']}</location>
    <temperature>{data['main']['temp']}</temperature>
    <humidity>{data['main']['humidity']}</humidity>
    <wind_speed>{data['wind']['speed']}</wind_speed>
    <condition>{condition}</condition>
</weather>"""

    return Response(xml_response, mimetype="application/xml")

# Debug JSON endpoint
@app.route("/getstaticweather_json")
def get_static_weather_json():
    loc = request.args.get("locCode", "Hanoi")
    params = {"q": loc, "appid": API_KEY, "units": "metric"}
    r = requests.get(BASE_URL, params=params)
    data = r.json()

    if "main" not in data:
        return jsonify({"error": "Location not found"})

    return jsonify({
        "location": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "condition": map_condition(data["weather"][0]["main"])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
