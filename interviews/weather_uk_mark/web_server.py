#!/usr/bin/env python

from http import server
from urllib.parse import urlparse, parse_qs
from weather import Weather, TemperatureMeasurement, LocationNotFound
from dotenv import load_dotenv
import os

load_dotenv()
APP_ID = os.getenv('APP_ID')


class RequestHandler(server.BaseHTTPRequestHandler):

    def do_GET(self):
        request_params = urlparse(self.path)
        path_list = request_params.path.split('/')
        query_params = parse_qs(request_params.query)
        # Query always starts from "/" so query_params will contain one_more
        # I don't handle the case when query ends with "/" to
        if path_list[1] == 'weather':
            city = path_list[2]
            unit = query_params.get('unit')[0]
            weather = Weather(APP_ID, city, TemperatureMeasurement(unit))
            try:
                weather.fetch_from_remote_server()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(str(weather).encode())
            except LocationNotFound:
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b'Location not found')
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b'Route not found')


httpd = server.HTTPServer(('0.0.0.0', 5050), RequestHandler)
try:
    print('Server started. Hello!')
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
    print('\rServer stopped. Good bye!')
