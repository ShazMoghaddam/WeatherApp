import tkinter as tk
import requests


def fetch_weather():
    city = city_entry.get()
    api_key = '61c98cbb8da5b41e7b57de26986347fe'  # Replace with your API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        weather_label.config(text=f"Error: {data.get('message', 'Invalid request')}")
        return

    # Extract weather information
    temp = data['main']['temp']
    weather_desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Display data
    weather_text = (f"Temperature: {temp}°C\nWeather: {weather_desc.capitalize()}"
                    f"\nHumidity: {humidity}%\nWind speed: {wind_speed} m/s")
    weather_label.config(text=weather_text)


# Create GUI
root = tk.Tk()
root.title('Weather App')

city_label = tk.Label(root, text='Enter city name:')
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text='Fetch Weather', command=fetch_weather)
fetch_button.pack()

weather_label = tk.Label(root, text='', font=('Arial', 12))
weather_label.pack()

root.mainloop()
