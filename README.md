# weather-forecast-python
Python script used to provide current weather information for a valid user-provided city.
<br><br>
OpenWeather API was used to fetch weather forecast(s).

## Tools used:
- Python
- requests (Python HTTP Library)
- OpenWeather API

## Installation/Setup

Run the below:

```
mkdir weather-forecast-python
cd weather-forecast-python

git clone git clone https://github.com/malcolmrichardson/weather-forecast-python.git
cd weather-forecast-python

virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

python app.py
```

## Notes
Create an [OpenWeather API account](https://openweathermap.org/api) and request a free API key.
Replace the 'API_KEY' variable in `app.py` with your API key, before running.

See terminal for results.

Enjoy and thank you!

Sample output below:
<br><br>
<img width="1092" alt="Screen Shot 2022-04-24 at 5 46 30 PM" src="https://user-images.githubusercontent.com/70815205/164998117-2062b91f-a674-4e98-884f-9dc6d992c715.png">

