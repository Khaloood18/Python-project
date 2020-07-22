import requests

apiKey = 'f3793d49603744dda6b31a3ee5adf22d'


class weatherLog:
    def __init__(self):
        self.cityLat = 0
        self.cityLong = 0
    def setInfo(self):
        print("Type in the Latitude")
        self.cityLat = input()
        print("Type in the Longitude")
        self.cityLong = input()
        cityLog = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=' + self.cityLat + '&lon=' + self.cityLong + '& exclude=minutely,hourly,daily&units=metric&appid=' + apiKey)
        self.logJson = cityLog.json()
    def getTemp(self):
        self.cityTemp = "Temperature: " + str(self.logJson['current']['temp'])
        return self.cityTemp

weatherA = weatherLog()
weatherA.setInfo()
print(weatherA.getTemp())

