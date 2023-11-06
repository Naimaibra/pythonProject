import requests

def fetch_weather():
    municipality = "Helsinki"
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={municipality}&appid=YOUR_API_KEY')
    data = response.json()

    if 'weather' in data and 'description' in data['weather'][0]:
        description = data['weather'][0]['description']
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        print(f"The weather in {municipality} is {description}\n"
              f"with a temperature of {temp_celsius:.2f} degrees Celsius.")
    else:
        print("Could not fetch weather data.")

fetch_weather()
