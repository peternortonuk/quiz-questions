# Test task for GMnT

## Prepare virtual environment
Prepare virtual environment and install dependencies before using.

Type next commands in your command line:
```
$ python3 -m venv ./venv
$ source ./venv/bin/activate
$ pip install
```

## Running CLI
Command line interface can run app in two modes:
- Service mode. In this mode the app will ask remote server every 10 minutes and save data to database
- Filter mode. In this mode the app will fetch all records from database which are matches for specified parameters of city and date

To show more information about allowed parameters just type:
```
$ python cli.py 
```
or
```
$ ./cli.py
```
You can also use `.env` file to specify such arguments like *CITY*, *APP_ID*, *DATABASE*

## Running app as web service
Use next commands to run web server
```
$ python web_server.py
```
or
```
$ ./web_server.py
```
Web server listens port 5050. Type for example 
`http://localhost:5050/weather/London?unit=C`
in your browser. 

Press Ctrl+C to stop it

## Running tests
Type next command in command line:
```
$ python -m unittest
```
or
```
$ coverage run -m unittest
```
Use next command to watch test coverage:
```
$ coverage report test.py
```