import fetcher
import pandas

def test_get_geo():
    assert fetcher.get_geolocation('Cardiff') == (53.77, -113.60)
    assert fetcher.get_geolocation('London') == (42.98, -81.24)
    assert fetcher.get_geolocation('Washington') == (40.70, -89.41)

def test_fetch_data():
    df = fetcher.fetch_weather_data(51.48, -3.18, '2023-01-01', '2023-01-01')
    
    assert not df.empty
    
    expected_columns = ['time', 'temperature_2m_max', 'temperature_2m_min', 
                       'precipitation_sum', 'wind_speed_10m_max']
    assert all(col in df.columns for col in expected_columns)
    
    assert df['time'].iloc[0] == '2023-01-01'
    
    assert pandas.api.types.is_numeric_dtype(df['temperature_2m_max'])
    assert pandas.api.types.is_numeric_dtype(df['temperature_2m_min'])