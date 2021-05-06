from unittest import TestCase
from unittest.mock import patch, MagicMock
from weather import Weather, TemperatureMeasurement, WeatherJsonFileMapper
from weather.exceptions import ServiceError, AppNotAuthorized, LocationNotFound
from datetime import date
import json


class TestWeather(TestCase):
    def setUp(self) -> None:
        response_data_file = open('support_files/01_weather_exercise/response_data.json', 'r')
        self.response_data = json.load(response_data_file)
        response_data_file.close()

    def tearDown(self) -> None:
        pass

    @patch('requests.get')
    def test_service_response_200_ok(self, mock_request_get):
        response_mock = MagicMock()
        response_mock.json = MagicMock(return_value=self.response_data)
        response_mock.status_code = 200  # Http status "200 ok"
        mock_request_get.return_value = response_mock
        weather = Weather('some_app_id', 'some_location')
        weather_data = weather.fetch_from_remote_server()
        self.assertEqual(weather_data, self.response_data)

    @patch('requests.get')
    def test_service_response_401_unauthorized(self, mock_request_get):
        response_mock = MagicMock()
        response_mock.json = MagicMock(return_value=self.response_data)
        response_mock.status_code = 401  # Http status "401 Unauthorized"
        mock_request_get.return_value = response_mock
        weather = Weather('some_app_id', 'some_location')
        self.assertRaises(AppNotAuthorized, weather.fetch_from_remote_server)

    @patch('requests.get')
    def test_service_response_404_not_found(self, mock_request_get):
        response_mock = MagicMock()
        response_mock.json = MagicMock(return_value=self.response_data)
        response_mock.status_code = 404  # Http status "404 Not found"
        mock_request_get.return_value = response_mock
        weather = Weather('some_app_id', 'some_location')
        self.assertRaises(LocationNotFound, weather.fetch_from_remote_server)

    @patch('requests.get')
    def test_service_response_error(self, mock_request_get):
        response_mock = MagicMock()
        response_mock.status_code = 400  # Any other http error status
        mock_request_get.return_value = response_mock
        weather = Weather('some_app_id', 'some_location')
        self.assertRaises(ServiceError, weather.fetch_from_remote_server)

    def test_format_weather_data(self):
        weather = Weather('some_app_id', 'some_location')
        weather.weather_data = self.response_data
        formatted_weather = weather.format_weather_data()
        self.assertEqual(formatted_weather, 'London, Wed 14 Dec 2016 10:50, haze, 11C')

    def test_format_temperature_celsius(self):
        weather = Weather('some_app_id', 'some_location', TemperatureMeasurement.Celsius)
        formatted_temperature = weather.format_temperature(0)
        self.assertEqual(formatted_temperature, '-273C')
        formatted_temperature = weather.format_temperature(100)
        self.assertEqual(formatted_temperature, '-173C')

    def test_format_temperature_fahrenheit(self):
        weather = Weather('some_app_id', 'some_location', TemperatureMeasurement.Fahrenheit)
        formatted_temperature = weather.format_temperature(0)
        self.assertEqual(formatted_temperature, '-460F')
        formatted_temperature = weather.format_temperature(100)
        self.assertEqual(formatted_temperature, '-280F')


class TestWeatherJsonFileMapper(TestCase):

    def setUp(self):
        response_data_file = open('support_files/01_weather_exercise/response_data.json', 'r')
        self.response_data = json.load(response_data_file)
        response_data_file.close()
        database_file = open('support_files/01_weather_exercise/db.json', 'r')
        self.database = json.load(database_file)
        database_file.close()

    def tearDown(self):
        pass

    def test_check_filter_condition(self):
        is_condition_true = WeatherJsonFileMapper._WeatherJsonFileMapper__check_filter_condition(
            self.database[0], 'London', None
        )
        self.assertEqual(is_condition_true, True)
        is_condition_true = WeatherJsonFileMapper._WeatherJsonFileMapper__check_filter_condition(
            self.database[0], 'London,uk', None
        )
        self.assertEqual(is_condition_true, True)
        is_condition_true = WeatherJsonFileMapper._WeatherJsonFileMapper__check_filter_condition(
            self.database[0], 'Maykop', None
        )
        self.assertEqual(is_condition_true, False)
        is_condition_true = WeatherJsonFileMapper._WeatherJsonFileMapper__check_filter_condition(
            self.database[0], None, None
        )
        self.assertEqual(is_condition_true, True)
        is_condition_true = WeatherJsonFileMapper._WeatherJsonFileMapper__check_filter_condition(
            self.database[0],
            None, date.fromisoformat('2021-04-27')
        )
        self.assertEqual(is_condition_true, True)
        is_condition_true = WeatherJsonFileMapper._WeatherJsonFileMapper__check_filter_condition(
            self.database[0],
            None, date.fromisoformat('1900-01-01')
        )
        self.assertEqual(is_condition_true, False)
        is_condition_true = WeatherJsonFileMapper._WeatherJsonFileMapper__check_filter_condition(
            self.database[0],
            'London', date.fromisoformat('1900-01-01')
        )
        self.assertEqual(is_condition_true, False)


