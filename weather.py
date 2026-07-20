from urllib import response

import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("API_KEY")
    
def get_weather_by_city(city, country_code):

    url = f"https://api.weatherbit.io/v2.0/current?KEY={api_key}"

    params = {
        "key": api_key,
        "city": city,
        "country_code": country_code
    }

    response = requests.get(url, params=params)
    
    weather_history = []

    try:
        with open("/home/alan-rodriguez/Desktop/weatherAPP/json-log/weather_results.json", "r") as json_file:
            weather_history = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        weather_history = []
    
    weather_history.append(response.json())

    with open("/home/alan-rodriguez/Desktop/weatherAPP/json-log/weather_results.json", "w") as json_file:
        json.dump(weather_history, json_file, indent=4)

    return response.json()

def get_search_history():
    try:
        with open("/home/alan-rodriguez/Desktop/weatherAPP/json-log/weather_results.json", "r") as json_file:
            history = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    return history
