import requests

city = input("Enter the name of the city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b499d46d86204168938175304261804"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error: Could not fetch weather data")

