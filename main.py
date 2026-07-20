import json
from urllib import response
from weather import get_weather_by_city
from weather import get_search_history
from location import weather_current_location

print("\nWelcome to the Weather App!")

option = int(input("\nPlease, select an option: \n\n[ 1 ] Search weather information by city. \n[ 2 ] See weather at your current location." "\n[ 3 ] View seach history. \n[ 4 ] Exit. \n\n"))


def view_search_history():
    with open("/home/alan-rodriguez/Desktop/weatherAPP/json-log/weather_results.json", "r") as json_file:
        data = json.load(json_file)
        for entry in data:
            print(entry)

if option == 1:
    city = input("Please, enter the city name: ")
    country_code = input("Please, enter the country code (e.g., US for United States): ")
    get_weather_by_city(city, country_code)
    print(f"\nWeather information for {city}, {country_code} has been retrieved and saved to the search history.\n")
    print("Current weather information:\n")
    weather = get_weather_by_city(city, country_code)
    print(f"Temperature: {weather['data'][0]['temp']}°C")
    print(f"Description: {weather['data'][0]['weather']['description']}")
    print(f"Humidity: {weather['data'][0]['rh']}%")
    print(f"Wind Speed: {weather['data'][0]['wind_spd']} m/s")


elif option == 2:
    location = weather_current_location()

    print("Weather information for your current location has been retrieved.\n")

    weather = get_weather_by_city(location["city"], location["countryCode"])
    print(f"Current weather in {location['city']}, {location['countryCode']}:\n")
    print(f"Temperature: {weather['data'][0]['temp']}°C")
    print(f"Description: {weather['data'][0]['weather']['description']}")
    print(f"Humidity: {weather['data'][0]['rh']}%")
    print(f"Wind Speed: {weather['data'][0]['wind_spd']} m/s")


elif option == 3:
    history = get_search_history()

    if not history:
        print("No weather history available.")
    else:
        for entry in history[-5:]:
            weather = entry["data"][0]

            print(f"City: {weather['city_name']}")

elif option == 4:
    exit