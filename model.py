'''import requests

#class WeatherInfo:
def getWeather(city):
    hourlyWeather = {}
    weatherData = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={}&APPID=225800a064f12ac6d7fbaadf83ce753f'.format(city))
    weatherData = weatherData.json()
    for x in range(8):
        dateTime = weatherData.list[x].dt_txt
        timeArr = dateTime.rsplit(" ")
        time = timeArr[1]
        hourlyWeather[time] = []
        hourlyWeather[time].append({"Temperature": weatherData.list[x].main.temp - 273.15})
        hourlyWeather[time].append({"Weather": weatherData.list[x].weather[0].main})
        hourlyWeather[time].append({"Weather Details": weatherData.list[x].weather[0].description})
        hourlyWeather[time].append({"Wind Speed": weatherData.list[x].wind.speed})
    return hourlyWeather'''

import requests

#class WeatherInfo:
def getWeather(city):
    weatherData = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={}&APPID=225800a064f12ac6d7fbaadf83ce753f'.format(city))
    weatherData = weatherData.json()
    return weatherData['list']

