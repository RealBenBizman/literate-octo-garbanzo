import requests

API_KEY = '87b944271cd24810922165120242405'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

def get_weather(city):
    url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
    
    response = requests.get(url)
    
    if response:
        data = response.json()
        current = data['current']
        print("Contents of 'current' dictionary:")
        print(current)
        print("\n")
        weather_desc = current['condition']['text']
        print(f"\nCity: {data['location']['name']}")
        print(f"Temperature: {current['temp_c']}°C")
        print(f"Humidity: {current['humidity']}%")
        print(f"Pressure: {current['pressure_mb']} hPa")
        print(f"Weather Description: {weather_desc}")
        print(f"Wind Speed: {current['wind_kph']} kph")
    else:
        print(f"\nError: {response.status_code}")
        print("Client-side issue / Incorrect city")

if __name__ == "__main__":
    while True:
        city = input("\nEnter city name: ")
        get_weather(city)
        Q = input("\nQuit? ")
        if Q == "Yes":
            break
