import asyncio

import aiohttp
import aiohttp_jinja2
from bs4 import BeautifulSoup

from src.libs.normalize import get_wind_speed_normalize, get_wind_speed_in_ms_normalize, get_humidity_normalize, \
    get_pressure_normalize
from src.urls import WEATHER_URLS


async def get_weather_from_url_1(session, url):
    async with session.get(url) as response:
        data = await response.text()
        soup = BeautifulSoup(data, 'html.parser')

        temp = soup.find('span', class_='CurrentConditions--tempValue--MHmYY').text[0:2]
        temp = f'{temp}°C'

        wind = soup.find('span', class_='Wind--windWrapper--3Ly7c undefined').text
        wind = get_wind_speed_in_ms_normalize(wind)

        humidity = soup.findAll('div', class_='WeatherDetailsListItem--wxData--kK35q')[2].text

        pressure = soup.find('span', class_='Pressure--pressureWrapper--3SCLm undefined').text
        pressure = get_pressure_normalize(pressure)

        weather_desc = soup.find('div', class_='CurrentConditions--phraseValue--mZC_p').text

        return temp, wind, humidity, pressure, weather_desc


async def get_weather_from_url_2(session, url):
    async with session.get(url) as response:
        data = await response.text()
        soup = BeautifulSoup(data, 'html.parser')

        temp = soup.find('span', class_='unit unit_temperature_c').text
        temp = f'{temp}°C'

        wind = soup.find('div', class_='unit unit_wind_m_s').text
        wind = get_wind_speed_normalize(wind)

        humidity = soup.find('div', class_='now-info-item humidity').text
        humidity = get_humidity_normalize(humidity)

        pressure = soup.find('div', class_='unit unit_pressure_mm_hg_atm').text
        pressure = get_pressure_normalize(pressure)

        weather_desc = soup.find('div', class_='now-desc').text

        return temp, wind, humidity, pressure, weather_desc


async def get_weather_from_url_3(session, url):
    async with session.get(url) as response:
        data = await response.text()
        soup = BeautifulSoup(data, 'html.parser')

        temp = soup.find('a', class_='summaryTemperatureCompact-E1_1 summaryTemperatureHover-E1_1').text

        wind = soup.find('div', id='CurrentDetailLineWindValue').text
        wind = get_wind_speed_in_ms_normalize(wind)

        humidity = soup.find('div', id='CurrentDetailLineHumidityValue').text

        pressure = soup.find('div', id='CurrentDetailLinePressureValue').text
        pressure = get_pressure_normalize(pressure)

        weather_desc = soup.find('div', class_='summaryCaptionCompact-E1_1').text

        return temp, wind, humidity, pressure, weather_desc


async def get_weather_start():
    async with aiohttp.ClientSession() as session:
        task1, task2, task3 = await asyncio.gather(get_weather_from_url_1(session, WEATHER_URLS[0]),
                                                   get_weather_from_url_2(session, WEATHER_URLS[1]),
                                                   get_weather_from_url_3(session, WEATHER_URLS[2]))
        return task1, task2, task3


@aiohttp_jinja2.template('index.html')
async def index(request):
    task1, task2, task3 = await get_weather_start()
    return {'task1': task1, 'task2': task2, 'task3': task3}
