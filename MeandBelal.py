# We will be using an API called OpenWeather to retrieve the weather data
# The API key (which is needed to use the service) is "f3793d49603744dda6b31a3ee5adf22d"

import requests

apiKey = 'f3793d49603744dda6b31a3ee5adf22d'

class weatherLog:
    def __init__(self):
        self.cityName = ''
    def setInfo(self):
        print("Type in a city name:")
        while True:
            cityName = input()
            cityFind = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&exclude=minutely,hourly,daily&units=metric&appid=' + apiKey)
            cityFindJson = cityFind.json()
            if (str(cityFind.status_code) == '200'):
                print("City Found!")
                self.cityLog = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=' + str(cityFindJson['coord']['lat']) + '&lon=' + str(cityFindJson['coord']['lon']) + '&exclude=minutely,hourly,daily&units=metric&appid=' + apiKey)
                break
            print("That is not a valid city, type in a city name:")
        self.logJson = self.cityLog.json()
    def getTemp(self):
        self.cityTemp = "Current Temperature: " + str(self.logJson['current']['temp'])
        return self.cityTemp
    def getHumidity(self):
        self.cityHumidity = " Humidity: " + str(self.logJson['current']['humidity'])
        return self.cityHumidity

weatherA = weatherLog()
weatherA.setInfo()
print(weatherA.getTemp())
print(weatherA.getHumidity())

