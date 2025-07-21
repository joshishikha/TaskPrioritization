import requests
from dotenv import load_dotenv
import os

load_dotenv()  # load environment variables from .env
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    #API_KEY = "d0dff6bf7f26229b805c3bc0f39125ba"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or "main" not in data:
            raise ValueError(f"City '{city}' not found or API error.")

        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"]
        }

    except Exception as e:
        print(f"[Error] {e}")
        return {"temp": None, "humidity": None, "pressure": None}
