from os import environ

todo_list = [
            {'name':'date night',"bad_weather":["rain","sleet","pellets"],"good_weather":["sunny","overcast"]},
            {'name':"museum","bad_weather":["sunny"]},
            {'name':"Relay for Life, CF, St. Lukes",'date':(2018, 2, 10)},
            ]

state = environ.get('CURRENT_STATE')
city = environ.get('CURRENT_CITY')
#reload_time: minutes between refreshing weather cache
reload_time = 10
