import pandas as pd
import requests
import datetime
from calendar import monthrange, isleap

def fetch_weather_data(latitude, longitude, start_date, end_date):
    """
    Получает исторические данные о погоде с Open-Meteo API.
    """
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,  # Формат: "2023-01-01"
        "end_date": end_date,
        "daily": ["temperature_2m_max", "temperature_2m_min",
                  "precipitation_sum", "wind_speed_10m_max"],
        "timezone": "auto"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # Преобразуем JSON в DataFrame
    df = pd.DataFrame(data["daily"])
    return df

def get_geolocation(city):
    api = 'd63617f55a6b5a78d09e85ccc2c6d494'
    api_call = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api}'
    
    response = requests.get(api_call)
    data = response.json()
    if not data:
        raise ValueError(f"Город '{city}' не найден")

    latitude = round(data[2]['lat'], 2)
    longtitude = round(data[2]['lon'], 2)
    
    return latitude, longtitude

def fetch_daily(city_name, date: datetime.datetime):
    lat, lon = get_geolocation(city_name)
    date_string = date.strftime("%Y-%m-%d")
    return fetch_weather_data(lat, lon, date_string, date_string)

def fetch_monthly(city_name, begin_date: datetime.datetime):
    #ВНИМАНИЕ: в begin_date должна быть указана дата с ПЕРВЫМ ЧИСЛОМ данного месяца
    lat, lon = get_geolocation(city_name)

    date_string = begin_date.strftime("%Y-%m-%d")
    year = date_string[0:4]
    month = date_string[5:7]
    days = monthrange(year, month)
    end_date = begin_date + datetime.timedelta(days=days-1)

    df = fetch_weather_data(lat, lon, begin_date, end_date)
    return df

def analyze_yearly(city_name, begin_date: datetime.datetime):
    #ВНИМАНИЕ: в begin_date должна быть указана дата с ПЕРВЫМ ДНЁМ данного года
    lat, lon = get_geolocation(city_name)

    date_string = begin_date.strftime("%Y-%m-%d")
    year = date_string[0:4]
    days = 365
    if isleap(year):
        days += 1
    end_date = begin_date + datetime.timedelta(days - 1)

    df = fetch_weather_data(lat, lon, begin_date, end_date)
    return df