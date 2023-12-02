import requests
import geocoder
import time
from plyer import notification

def get_current_location():
    # Get current location using the IP address
    location = geocoder.ip('me')

    # Extract latitude and longitude
    latitude, longitude = location.latlng

    return latitude, longitude

def get_weather(api_key, latitude, longitude):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric",  # You can change this to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(weather_data, city):
    if weather_data and 'main' in weather_data:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        message = f"Temperature: {temperature}°C\nDescription: {description}"
        notification.notify(
            title=f"Weather in {city}",
            message=message,
            timeout=200  # Notification timeout in seconds
        )
    else:
        print("Unable to fetch or parse weather data.")

if _name_ == "_main_":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "8ce438111f4bd923c2664bf4d1ff62b2"

    # Get current location
    city = "Thandalam"  # Change this to your city name
    latitude, longitude = get_current_location()

    while True:
        # Get weather data for the current location
        weather_data = get_weather(api_key, latitude, longitude)

        # Display weather report
        display_weather(weather_data, city)

        # Wait for a period (e.g., 1 hour) before fetching data again
        time.sleep(3600)  # 3600 seconds = 1 hour
