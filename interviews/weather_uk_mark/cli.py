#!/usr/bin/env python

from weather import Weather, WeatherJsonFileMapper, AppNotAuthorized, TemperatureMeasurement
from time import sleep
from datetime import datetime, date
from dotenv import load_dotenv
import argparse
import os


def run_weather_service(app_id, location, unit):
    interval = 10 * 60  # 10 minutes
    while True:
        weather = Weather(app_id, location, temperature_measurement=TemperatureMeasurement(unit))
        mapper = WeatherJsonFileMapper(os.getenv('DATABASE', 'database.json'))
        print(f'-------------------------------------------')
        try:
            weather.fetch_and_show()
            print('Weather fetched from remote service')
            mapper.save(weather)
            print('Weather saved to database')
            print(f'Service sleeps for {interval} seconds...')
            print(f'==========================================')
        except AppNotAuthorized:
            print('Application is not authorized to access the remote service')
            print(f'==========================================')
            break
        sleep(interval)


def fetch_weather_by_city_and_date(city: str = None, date_str: str = None) -> None:
    mapper = WeatherJsonFileMapper('database.json')
    if date_str:
        date_obj = date.fromisoformat(date_str)
    else:
        date_obj = None
    weather_list = mapper.filter(city, date_obj)
    for weather_item in weather_list:
        print(weather_item)


def cli_run_service(args):
    city = args.city or os.getenv('CITY', None)
    app_id = args.app_id or os.getenv('APP_ID', None)
    unit = args.unit or os.getenv('UNIT', None)
    if app_id and city:
        try:
            run_weather_service(app_id, city, unit)
        except KeyboardInterrupt:
            print('\rService stopped. Good bye!')
    else:
        if not app_id:
            print("App ID is required")
        if not city:
            print("City is required")
        running_parser.print_help()


def cli_run_filter(args):
    city_arg = args.city
    date_arg = args.date
    if city_arg or date_arg:
        fetch_weather_by_city_and_date(city_arg, date_arg)
    else:
        print("City or date is required")
        running_parser.print_help()


if __name__ == '__main__':
    load_dotenv()
    running_parser = argparse.ArgumentParser(
        description="Options for running service",
    )
    running_parser.add_argument("-r", "--run", help="Run as a service", default=False, action="store_true")
    running_parser.add_argument("-a", "--app_id", help="Application ID", type=str, default=None)
    running_parser.add_argument("-c", "--city", help="City name to fetch from remote server or database", type=str,
                                default=None)
    running_parser.add_argument(
        "-d",
        "--date",
        help="Fetch weather records by data. "
             "Use next format to describe date: YYYY-MM-DD for example 2021-12-25",
        type=str,
        default=None
    )
    running_parser.add_argument(
        "-u", "--unit",
        help="Temperature measurement unit",
        type=str,
        choices=['C', 'F'],
        default='C'
    )
    running_args = running_parser.parse_args()
    if running_args.run:
        cli_run_service(running_args)
    else:
        cli_run_filter(running_args)
