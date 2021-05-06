import json

import requests
from typing import List, Optional

from .exceptions import ServiceError, AppNotAuthorized, LocationNotFound
from datetime import datetime, date
from enum import Enum

ABS_ZERO_KELVIN = -273.15
ABS_ZERO_FAHRENHEIT = -459.67


class TemperatureMeasurement(Enum):
    Celsius = 'C'
    Fahrenheit = 'F'


class Weather(object):
    api_uri = 'http://api.openweathermap.org/data/2.5/weather'

    def __init__(
            self,
            app_id: str,
            city: str,
            temperature_measurement: TemperatureMeasurement = TemperatureMeasurement.Celsius,
            weather_data: dict = None
    ):
        self.app_id = app_id
        self.city = city
        self.temperature_measurement = temperature_measurement
        self.weather_data = weather_data

    def fetch_from_remote_server(self):
        response = requests.get(self.api_uri, params={'appid': self.app_id, 'q': self.city})
        if response.status_code == 200:
            self.weather_data = response.json()
            return self.weather_data
        if response.status_code == 404:
            raise LocationNotFound
        if response.status_code == 401:
            raise AppNotAuthorized
        raise ServiceError()

    def format_weather_data(self) -> str:
        weather_data = self.weather_data
        current_date = datetime.utcfromtimestamp(weather_data['dt'])
        formatted_date = current_date.strftime('%a %d %b %Y %H:%M')
        temperature_kelvin = weather_data['main']['temp']
        weather = weather_data['weather'][0]['description']
        temperature = self.format_temperature(temperature_kelvin)
        return f'{weather_data["name"]}, {formatted_date}, {weather}, {temperature}'

    def format_temperature(self, temperature_kelvin: int) -> str:
        if self.temperature_measurement == TemperatureMeasurement.Celsius:
            temperature = round(temperature_kelvin + ABS_ZERO_KELVIN)
            return f'{temperature}C'
        if self.temperature_measurement == TemperatureMeasurement.Fahrenheit:
            temperature = round((9 / 5) * temperature_kelvin + ABS_ZERO_FAHRENHEIT)
            return f'{temperature}F'

    def fetch_and_show(self) -> str:
        """
            If the information is not available, this method will retry and give the answer as soon as possible.
        """
        while True:
            try:
                self.fetch_from_remote_server()
                weather_str = self.format_weather_data()
                print(self)
                return weather_str
            except AppNotAuthorized as e:
                raise e
            except ServiceError:
                """
                    Do nothing if other weather service error occurs
                """

    def __str__(self):
        return self.format_weather_data()


class WeatherMapper(object):

    def __init__(self, *args, **kwargs) -> None:
        """
            The constructor should contain code
            for database (or file base, or any other persistence) initialization
        """
        raise NotImplementedError()

    def save(self, weather: Weather) -> None:
        """
            Method for save weather object into database
        """
        raise NotImplementedError()

    def filter(self, *args, **kwargs) -> List[Weather]:
        """
            Method for fetch weather multiple records from database
            *args and **kwargs should contain conditions to filter records
        """
        raise NotImplementedError()

    def get(self, *args, **kwargs) -> Weather:
        """
            Method for fetch single (first found) weather record from database
            *args and **kwargs should contain conditions to filter records
        """
        raise NotImplementedError()


class WeatherJsonFileMapper(WeatherMapper):

    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def __weather_to_record(weather: Weather) -> dict:
        return {
            'app_id': weather.app_id,
            'city': weather.city,
            'temperature_measurement': str(weather.temperature_measurement.value),
            'weather_data': weather.weather_data
        }

    @staticmethod
    def __record_to_weather(record: dict) -> Weather:
        return Weather(
            app_id=record['app_id'],
            city=record['city'],
            temperature_measurement=TemperatureMeasurement(record['temperature_measurement']),
            weather_data=record['weather_data']
        )

    @staticmethod
    def __load_database(database_file):
        try:
            database_file.seek(0)
            data = json.load(database_file)
        except json.decoder.JSONDecodeError as e:
            data = []
        return data

    def __save(self, weather: Weather) -> None:
        with open(self.file_name, 'r+') as database:
            data = self.__load_database(database)
            data.append(self.__weather_to_record(weather))
            database.seek(0)
            json.dump(data, database)
            database.truncate()

    @staticmethod
    def __check_filter_condition(weather_record: dict, city: Optional[str], date_obj: Optional[date]):
        record_city = weather_record['city']
        weather_city = weather_record['weather_data']['name']
        record_date = datetime.utcfromtimestamp(weather_record['weather_data']['dt']).date()
        return ((city is None) or (record_city == city) or (weather_city == city)) and \
               ((date_obj is None) or (record_date == date_obj))

    def save(self, weather: Weather) -> None:
        """
            creates file base if it is not existed yet
        """
        try:
            self.__save(weather)
        except FileNotFoundError:
            database = open(self.file_name, 'w+')
            database.close()
            self.__save(weather)

    def filter(self, city: str = None, date_obj: datetime.date = None) -> List[Weather]:
        """
            returns a list of weather objects filtered by city and date
            if city is None or date is None it returns all relevant values for second param
            if both are None it returns all records
        """
        query_set = []
        with open(self.file_name, 'r') as database:
            data = self.__load_database(database)
            for weather_item in data:
                if self.__check_filter_condition(weather_item, city, date_obj):
                    weather = self.__record_to_weather(weather_item)
                    query_set.append(weather)
        return query_set

    def get(self, city=None, date_obj: datetime.date = None) -> Optional[Weather]:
        """
            returns a single weather object filtered by city and data
            returns first found record
        """
        with open(self.file_name, 'r') as database:
            data = self.__load_database(database)
            for weather_item in data:
                if self.__check_filter_condition(weather_item, city, date_obj):
                    return self.__record_to_weather(weather_item)
        return None
