import requests ,  json

api_weather_key="e9911a4a9514e608c247b9c6ae1b3c23"
url="https://api.openweathermap.org/data/2.5/weather?"



city_name=input('please enter you city')

complete_url=f'{url}q={city_name}&appid={api_weather_key}'

response = requests.get(complete_url)


if response.status_code != 404:
    
    response=response.json()
    
    y=response['main']
    
    temp=y['temp']
    pressure=y['pressure']
    humidity=y['humidity']
    
    print(
        'temp' ,temp ,'/n','pressure' ,pressure ,'/n','humidity',humidity ,'/n',
    )

    
    
else:
    print('city not found')