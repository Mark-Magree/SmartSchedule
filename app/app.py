#SmartSchedule -- scheduler that makes suggestions based on weather
#
#author: markmagree@protonmail.com
#required environment variables: CURRENT_STATE CURRENT_CITY WUNDERGROUND_KEY
#notes: CURRENT_STATE and CURRENT_CITY must be compatable with wunderground.com
# url. WUNDERGROUND_KEY available free from wunderground.com for personal use
#usage: "python app.py"


import datetime 
from config import todo_list 
from tools import time_until_event, get_weather

def condition_met(event, now, w):
    '''determine if event should be displayed'''
    if 'date' in event: 
        time_till = time_until_event(event, now)
        if time_till.days > 7:
            return False
    if 'bad_weather' in event:
        if w['current_observation']['weather'] in event['bad_weather']:
            return False
    return True

def build_report():
    report = []

    now = datetime.datetime.now()
    w = get_weather()

    report.append(f"Today is {now.strftime('%A, %B %d')}")
    report.append("Current conditions: %s, and %s degrees with winds of %s mph." % (
                    w["current_observation"]["weather"],
                    w["current_observation"]["temp_f"],
                    w["current_observation"]["wind_mph"],
                    ))

    #TODO import events from database instead of config
    if todo_list:
        report.append("    On your TODO list:")
        for event in todo_list:
            if condition_met(event, now, w):
                report.append(f"+{event['name']}")
        report.append("    List of things to not worry about yet:")
        for event in todo_list:
            if not condition_met(event, now, w):
                if 'date' in event:
                    time_til = time_until_event(event, now)
                    report.append(f"-{event['name']} deadline in \
                            {time_til.days} days and \
                            {time_til.seconds//3600} hours.")
                else:
                    report.append(f"-{event['name']}")
    else:
        report.append("Nothing on your TODO list!")
    return report

def run():
    print("\nSmartSchedule building report.........")
    for line in build_report():
        print(line)
    print('\n')

if __name__ == "__main__":
    run()
