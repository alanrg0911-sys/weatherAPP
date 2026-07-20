import json
import requests

JSON_FILE = "/home/alan-rodriguez/Desktop/weatherAPP/json-log/current_location.json"

def weather_current_location():
    url = "http://ip-api.com/json/"

    response = requests.get(url)
    location = response.json()

    try:
        with open(JSON_FILE, "r") as json_file:
            location_history = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        location_history = []
    
    location_history.append(location)

    with open (JSON_FILE, "w") as json_file:
        json.dump(location_history, json_file, indent=4)
    
    return location

    

 


