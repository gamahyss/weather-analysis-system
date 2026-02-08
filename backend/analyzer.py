import pandas
import fetcher
import datetime
import numpy

def analyze_daily(city_name: str, date: datetime.datetime) -> pandas.DataFrame:
    #должен выводить датафрейм погоды в этот день
    return fetcher.fetch_daily(city_name, date)

def analyze_montly(city_name: str, date: datetime.datetime) -> pandas.DataFrame:
    #должен выводить датафреймы всех погодных параметров по дням месяца и датафрейм со средними значениями по всем параметрам
    data = fetcher.fetch_monthly(city_name, date)

    monthly_temp_max = pandas.DataFrame({'max_temp': data['temperature_2m_max']})
    monthly_temp_min = pandas.DataFrame({'min_temp': data['temperature_2m_min']})
    monthly_prec = pandas.DataFrame({'prec': data['precipitation_sum']})
    monthly_wind_max = pandas.DataFrame({'wind_speed': data['wind_speed_10m_max']})

    average_values = pandas.DataFrame({'avrg_temp_max': [numpy.mean(data['temperature_2m_max'])],
                           'avrg_temp_min': [numpy.mean(data['temperature_2m_min'])],
                           'avrg_prec': [numpy.mean(data['precipitation_sum'])],
                           'avrg_wind_speed': [numpy.mean(data['wind_speed_10m_max'])]
                           })
    max_values = pandas.DataFrame({'max_temp': [numpy.max(data['temperature_2m_max'])],
                                   'max_prec': [numpy.max(data['precipitation_sum'])],
                                   'max_wind_speed': [numpy.max(data['wind_speed_10m_max'])]})
    min_values = pandas.DataFrame({'min_temp': [numpy.min(data['temperature_2m_min'])],
                                   'min_prec': [numpy.min(data['precipitation_sum'])],
                                   'min_wind_speed': [numpy.min(data['wind_speed_10m_max'])]})
    
    return monthly_temp_max, monthly_temp_min, monthly_prec, monthly_wind_max, average_values, max_values, min_values

def analyze_yearly(city_name: str, date: datetime.datetime) -> pandas.DataFrame:
    #должен выводить соответствующие для всех погодных параметров датафреймы, где будут их средние значения по месяцам, а также датафрейм со средними значениями за год, датафрейм с максимальными и датафрейм с минимальными
    return

#Проверка
#print(analyze_daily('Moscow', datetime.datetime.strptime('2024-02-01', '%Y-%m-%d')))
#print(analyze_monthly('Moscow', datetime.datetime.strptime('2024-02-01', '%Y-%m-%d')))