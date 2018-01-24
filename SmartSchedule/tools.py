import os, json, requests, datetime
from config import city, state

def time_until_event(event, now):
    return datetime.datetime(*event['date']) - now

def get_weather():
    key = os.environ.get('WUNDERGROUND_KEY')
    if os.path.isfile("forecast.json"):
        with open("forecast.json",'r') as forecast_file:
            return json.loads(forecast_file.read())
    else:
        forecast_url = "http://api.wunderground.com/api/%s/forecast\
                /geolookup/conditions/q/%s/%s.json" % (key, state, city)
        forecast = requests.get(forecast_url)
        forecast.raise_for_status()
        with open("forecast.json","w") as okthen:
            okthen.write(forecast.text)
        forecast_data = json.loads(forecast.text)
        return forecast_data

