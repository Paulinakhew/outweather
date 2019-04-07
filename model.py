import requests

#class WeatherInfo:
def getWeather(city):
    hourlyWeather = {}
    weatherData = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={}&APPID=225800a064f12ac6d7fbaadf83ce753f'.format(city))
    weatherData = weatherData.json()

    for x in range(8):
        dateTime = weatherData['list'][x]['dt_txt']
        timeArr = dateTime.rsplit(" ")
        date = timeArr[0]
        time = timeArr[1]
        if (time == "12:00:00"):
            hourlyWeather["Temperature"] = round((weatherData['list'][x]['main']['temp'] - 273.15), 1)
            hourlyWeather["Weather"] = weatherData['list'][x]['weather'][0]['main']
            hourlyWeather["Weather Details"] = weatherData['list'][x]['weather'][0]['description']
            hourlyWeather["Wind Speed"] = round((weatherData['list'][x]['wind']['speed']),2)
            hourlyWeather["Date"] = date

    return hourlyWeather

def check_status_code(city):
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={}&APPID=225800a064f12ac6d7fbaadf83ce753f'.format(city))

    if int(response.status_code) != 200:
        return False
    else:
        return True