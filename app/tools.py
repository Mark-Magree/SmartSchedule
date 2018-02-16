import os, json, requests, datetime, stat, time
from config import *

def time_until_event(event, now):
    return datetime.datetime(*event['date']) - now

def file_age(file):
    '''to determine if forecast needs to be replaced. returns minutes'''
    return int((time.time() - os.stat(file).st_mtime)/60)

def get_weather():
    '''returns current conditions. '''
    #TODO get future weather as well
    key = os.environ.get('WUNDERGROUND_KEY')
    if os.path.isfile("forecast.json") and not \
            file_age("forecast.json") > reload_time:
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

