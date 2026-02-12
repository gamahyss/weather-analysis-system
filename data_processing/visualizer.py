from matplotlib import pyplot
import pandas

import analyzer
import datetime

def visualize_daily(df: pandas.Series):
    params_structured = ['Max. temp., °C', 'Min. temp., °C', 'Precipitation, mm', 'Wind speed, m/s']
    values_structured = []

    df = df.to_frame()
    values = df.values.tolist()
    date = values.pop(0)[0][0]
    for value in values:
        values_structured.append(value[0][0])
    
    df_structured = pandas.DataFrame({'Parameters': params_structured, 'Values': values_structured})
    pyplot.bar(df_structured['Parameters'], df_structured['Values'], color="#3C2ED3")
    pyplot.title(f'Weather analysis for {date}')
    for i in range(len(df_structured['Parameters'])):
        pyplot.text(i, df_structured['Values'][i], df_structured['Values'][i])

    pyplot.show()

def structurize_df(df: pandas.DataFrame, parameter_name: str) -> pandas.DataFrame:
    days = []
    values = []
    for day in df.to_dict()[parameter_name]:
        days.append(day + 1)
        values.append(df.to_dict()[parameter_name][day])
    structured_df = pandas.DataFrame({'Number of the day': days, 'Value': values})
    return structured_df

def visualize_monthly(daily_temp_max: pandas.DataFrame,
                      daily_temp_min: pandas.DataFrame,
                      daily_prec: pandas.DataFrame,
                      daily_wind_speed: pandas.DataFrame,
                      average_values: pandas.DataFrame,
                      max_values: pandas.DataFrame,
                      min_values: pandas.DataFrame):
    temp_max_structured = structurize_df(daily_temp_max, 'temp_max')
    temp_min_structured = structurize_df(daily_temp_min, 'temp_min')
    prec_structured = structurize_df(daily_prec, 'prec')
    wind_speed_structured = structurize_df(daily_wind_speed, 'wind_speed')
    #ДОПИСАТЬ

def visualize_yearly(monthly_values: pandas.DataFrame,
                     average_values: pandas.DataFrame,
                     max_values: pandas.DataFrame,
                     min_values: pandas.DataFrame):
    return

#Проверка
#data1 = analyzer.analyze_daily('London', datetime.datetime.strptime('2024-03-01', '%Y-%m-%d'))
#visualize_daily(data1)
data1, data2, data3, data4, data5, data6, data7 = analyzer.analyze_monthly('London', datetime.datetime.strptime('2024-03-01', '%Y-%m-%d'))
visualize_monthly(data1, data2, data3, data4, data5, data6, data7)