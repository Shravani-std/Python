

import json
import requests

#API to fetch temperature of city
city_name = input("Enter city Name ; ")


api_key ='5f37fa9c7ade22bf7336bf2621dbd66e'

#To build URL api
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_information = requests.get(api_url)
print(get_server_information.json())

