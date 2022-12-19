import re


def get_wind_speed_in_ms_normalize(wind):
    wind = int(re.search(r'\d+', wind).group())
    wind = f'{int(wind * 1000 / 3600)} m/s'
    return wind


def get_wind_speed_normalize(wind):
    wind = re.search(r'\d+', wind).group()
    wind = f'{wind} m/s'
    return wind


def get_pressure_normalize(pressure):
    pressure = re.search(r'\d+', pressure).group()
    if float(pressure) > 1000:
        pressure = float(pressure) * 0.75006375541921
    pressure = f'{int(pressure)} mmHg'
    return pressure


def get_humidity_normalize(humidity):
    humidity = re.search(r'\d+', humidity).group()
    humidity = f'{humidity}%'
    return humidity

