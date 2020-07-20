# This document will contain example functions that will be needed in this project
# We will be using an API called OpenWeather to retrieve the weather data
# The API key (which is needed to use the service) is "f3793d49603744dda6b31a3ee5adf22d"

# Template for OpenWeather API GET https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&
# exclude={part}&appid={YOUR API KEY}

import requests

# Example response with Doha, Qatar as the location

w_retrieval = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=25.3&lon=51.1& exclude=minutely,hourly,daily&appid=f3793d49603744dda6b31a3ee5adf22d')

print(w_retrieval.status_code)  # Prints the status code (200 = OK) (If the API isn't connecting properly, this is the first step to troubleshoot)
#print(w_retrieval.json())       # Prints all the content of the API request (All the data)
print("\n")

w_log = w_retrieval.json()      # Store the json file (the json file contains all the data, it's like a neat box of information that OpenWeather and other API's give is)

print("Temperature: " + str(w_log['current']['temp'])) # Prints the current temperature