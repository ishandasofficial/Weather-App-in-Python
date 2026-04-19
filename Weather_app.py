import requests

API_KEY = "a80dfd06b4835618805c328e6cafe4e2"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("City not found!")
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

        print(f"\nWeather in {city_name}, {country}")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_desc.capitalize()}")

    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ")
        if city.lower() == "quit":
            break
        get_weather(city)