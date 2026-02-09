import pandas
import fetcher
import datetime
import numpy

def analyze_daily(city_name: str, date: datetime.datetime) -> pandas.DataFrame:
    #должен выводить датафрейм погоды в этот день
    return fetcher.fetch_daily(city_name, date)

def analyze_monthly(city_name: str, date: datetime.datetime) -> pandas.DataFrame:
    #должен выводить датафреймы всех погодных параметров по дням месяца и датафрейм со средними значениями по всем параметрам
    data = fetcher.fetch_monthly(city_name, date)

    daily_temp_max = pandas.DataFrame({'max_temp': data['temperature_2m_max']})
    daily_temp_min = pandas.DataFrame({'min_temp': data['temperature_2m_min']})
    daily_prec = pandas.DataFrame({'prec': data['precipitation_sum']})
    daily_wind_speed = pandas.DataFrame({'wind_speed': data['wind_speed_10m_max']})

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
    
    return daily_temp_max, daily_temp_min, daily_prec, daily_wind_speed, average_values, max_values, min_values

def analyze_yearly(city_name: str, date: datetime.datetime) -> pandas.DataFrame:
    #должен выводить соответствующие для всех погодных параметров датафреймы, где будут их средние значения по месяцам, а также датафрейм со средними значениями за год, датафрейм с максимальными и датафрейм с минимальными
    data = fetcher.fetch_yearly(city_name, date)

    average_values = pandas.DataFrame({'avrg_temp_max': [numpy.mean(data['temperature_2m_max'])],
                                       'avrg_temp_min': [numpy.mean(data['temperature_2m_min'])],
                                       'avrg_prec': [numpy.mean(data['precipitation_sum'])],
                                       'avrg_wind_speed': [numpy.mean(data['wind_speed_10m_max'])]})
    max_values = pandas.DataFrame({'max_temp': [numpy.max(data['temperature_2m_max'])],
                                   'max_prec': [numpy.max(data['precipitation_sum'])],
                                   'max_wind_speed': numpy.max(data['wind_speed_10m_max'])})
    min_values = pandas.DataFrame({'min_temp': [numpy.min(data['temperature_2m_min'])],
                                   'min_prec': [numpy.min(data['precipitation_sum'])],
                                   'min_wind_speed': [numpy.min(data['wind_speed_10m_max'])]})
    
    monthly_temp_max_list = []
    monthly_temp_min_list = []
    monthly_prec_list = []
    monthly_wind_speed_list = []

    for month in range(1, 13):
        if month < 10:
            month_str = '0' + str(month)
        else:
            month_str = str(month)

        month_date = datetime.datetime.strptime((datetime.datetime.strftime(date, '%Y-%m-%d')[0:5] + month_str + '-01'), '%Y-%m-%d')
        dict_month_average = analyze_monthly(city_name, month_date)[4].to_dict()

        monthly_temp_max_list.append(dict_month_average['avrg_temp_max'][0])
        monthly_temp_min_list.append(dict_month_average['avrg_temp_min'][0])
        monthly_prec_list.append(dict_month_average['avrg_prec'][0])
        monthly_wind_speed_list.append(dict_month_average['avrg_wind_speed'][0])
    
    monthly_values = pandas.DataFrame({'temp_max': monthly_temp_max_list,
                                       'temp_min': monthly_temp_min_list,
                                       'prec': monthly_prec_list,
                                       'wind_speed': monthly_wind_speed_list})
    
    return monthly_values, average_values, max_values, min_values

#Проверка
#print(analyze_daily('Moscow', datetime.datetime.strptime('2024-02-01', '%Y-%m-%d')))
#print(analyze_monthly('Moscow', datetime.datetime.strptime('2024-02-01', '%Y-%m-%d')))
#print(analyze_yearly('Moscow', datetime.datetime.strptime('2024-02-01', '%Y-%m-%d')))