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
    df = pd.DataFrame(data)
    return df

def get_geolocation(city):
    api = 'd63617f55a6b5a78d09e85ccc2c6d494'
    api_call = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api}'
    
    response = requests.get(api_call)
    data = response.json()
    if not data:
        raise ValueError(f"Город '{city}' не найден")

    latitude = round(data[2]['lat'], 2)
    longitude = round(data[2]['lon'], 2)
    
    return latitude, longitude

def fetch_daily(city_name, date: datetime.datetime):
    lat, lon = get_geolocation(city_name)
    date_string = date.strftime("%Y-%m-%d")
    return fetch_weather_data(lat, lon, date_string, date_string)['daily']

def fetch_monthly(city_name, begin_date: datetime.datetime):
    #ВНИМАНИЕ: в begin_date должна быть указана дата с ПЕРВЫМ ЧИСЛОМ данного месяца
    lat, lon = get_geolocation(city_name)

    date_string = begin_date.strftime("%Y-%m-%d")
    year = int(date_string[0:4])
    month = int(date_string[5:7])
    days = monthrange(year, month)[1]
    end_date = begin_date + datetime.timedelta(days - 1)

    begin_date_str = begin_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    df = fetch_weather_data(lat, lon, begin_date_str, end_date_str)['daily']
    return df

def fetch_yearly(city_name, begin_date: datetime.datetime):
    #ВНИМАНИЕ: в begin_date должна быть указана дата с ПЕРВЫМ ДНЁМ данного года
    lat, lon = get_geolocation(city_name)

    date_string = begin_date.strftime("%Y-%m-%d")
    year = int(date_string[0:4])
    days = 365
    if isleap(year):
        days = 366
    end_date = begin_date + datetime.timedelta(days - 1)

    begin_date_str = begin_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    df = fetch_weather_data(lat, lon, begin_date_str, end_date_str)['daily']
    return df

#Проверка
#print(fetch_daily('Moscow', datetime.datetime.strptime('2023-01-01', '%Y-%m-%d')))
#print(fetch_monthly('Moscow', datetime.datetime.strptime('2023-01-01', '%Y-%m-%d')))
#print(fetch_yearly('Moscow', datetime.datetime.strptime('2023-01-01', '%Y-%m-%d')))