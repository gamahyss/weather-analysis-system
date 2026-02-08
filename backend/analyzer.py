import pandas
import fetcher
import datetime

def analyze_daily(city_name: str, date: datetime.datetime) -> pandas.DataFrame:
    #должен выводить датафрейм погоды в этот день
    return

def analyze_montly(city_name: str, date: datetime.datetime) -> pandas.DataFrame:
    #должен выводить датафреймы всех погодных параметров по дням месяца и датафрейм со средними значениями по всем параметрам
    return

def analyze_yearly(city_name: str, date: datetime.datetime) -> pandas.DataFrame:
    #должен выводить датафреймы всех средних месячных значений погодных параметров по месяцам, а также подробный вывод по каждому месяцу (здесь используем analyze_monthly) 
    return