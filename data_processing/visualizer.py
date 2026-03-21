from matplotlib import pyplot
import pandas

import analyzer
import datetime

def structurize_df(df: pandas.DataFrame, parameter_name: str) -> pandas.DataFrame:
    days = []
    values = []
    for day in df.to_dict()[parameter_name]:
        days.append(day + 1)
        values.append(df.to_dict()[parameter_name][day])
    structured_df = pandas.DataFrame({'Number of the day': days, 'Value': values})
    return structured_df

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

def visualize_monthly(daily_temp_max: pandas.DataFrame,
                      daily_temp_min: pandas.DataFrame,
                      daily_prec: pandas.DataFrame,
                      daily_wind_speed: pandas.DataFrame,
                      average_values: pandas.DataFrame,
                      max_values: pandas.DataFrame,
                      min_values: pandas.DataFrame):
    temp_max_structured = structurize_df(daily_temp_max, 'max_temp')
    temp_min_structured = structurize_df(daily_temp_min, 'min_temp')
    prec_structured = structurize_df(daily_prec, 'prec')
    wind_speed_structured = structurize_df(daily_wind_speed, 'wind_speed')

    days = temp_max_structured['Number of the day'].to_list()
    temp_max_daily = temp_max_structured['Value'].to_list()
    temp_min_daily = temp_min_structured['Value'].to_list()
    prec_daily = prec_structured['Value'].to_list()
    wind_daily = wind_speed_structured['Value'].to_list()

    params = ['Temperature', 'Precipitation', 'Wind speed']
    avrg_statistics = [float(average_values['avrg_temp'].values[0]),
                       float(average_values['avrg_prec'].values[0]),
                       float(average_values['avrg_wind_speed'].values[0])]
    max_statistics = [float(max_values['max_temp'].values[0]),
                       float(max_values['max_prec'].values[0]),
                       float(max_values['max_wind_speed'].values[0])]
    min_statistics = [float(min_values['min_temp'].values[0]),
                       float(min_values['min_prec'].values[0]),
                       float(min_values['min_wind_speed'].values[0])]

    pyplot.plot(days, temp_max_daily, color='red', label='Max temp', marker='.')
    pyplot.plot(days, temp_min_daily, color='green', label='Min temp', marker='.')
    pyplot.plot(days, prec_daily, color='purple', label = 'Precipitation', marker='.')
    pyplot.plot(days, wind_daily, color='blue', label='Wind speed', marker = '.')
    pyplot.title('Monthly weather analysis')
    pyplot.xticks(days)
    pyplot.xlabel("Number of the month's day")
    pyplot.ylabel('Parameters at the day')
    pyplot.legend()
    pyplot.show()

    pyplot.scatter(params, avrg_statistics, color='orange', label='Average values')
    pyplot.scatter(params, max_statistics, color='red', label='Max values')
    pyplot.scatter(params, min_statistics, color='blue', label='Min values')
    y_values = avrg_statistics + max_statistics + min_statistics
    pyplot.yticks(y_values)
    pyplot.legend()
    pyplot.show()

def visualize_yearly(monthly_values: pandas.DataFrame,
                     average_values: pandas.DataFrame,
                     max_values: pandas.DataFrame,
                     min_values: pandas.DataFrame):
    return

#Проверка
# data1 = analyzer.analyze_daily('London', datetime.datetime.strptime('2024-03-01', '%Y-%m-%d'))
# visualize_daily(data1)
data1, data2, data3, data4, data5, data6, data7 = analyzer.analyze_monthly('London', datetime.datetime.strptime('2024-03-01', '%Y-%m-%d'))
visualize_monthly(data1, data2, data3, data4, data5, data6, data7)