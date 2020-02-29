from datetime import datetime
import os
import pytz
import math
import requests

API_KEY = os.environ.get("API_KEY")
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric')


def get_weather_by_city(city):
    try:
        print(API_URL.format(city, API_KEY))
        response = requests.get(API_URL.format(city, API_KEY))
        return response.json()
    except Exception as exc:
        print(exc)
        data = None
        return data
