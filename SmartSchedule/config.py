from os import environ

todo_list = [
            {'name':'date night',"bad_weather":["rain","sleet","pellets"],"good_weather":["sunny","overcast"]},
            {'name':"museum","bad_weather":["sunny"]},
            {'name':"Relay for Life, CF, St. Lukes",'date':(2018, 2, 10)},
            {'name':"date night","bad_weather":["rain","sleet","pellets"],"good_weather":["sunny"]}
            ]

state = environ.get('CURRENT_STATE')
city = environ.get('CURRENT_CITY')
