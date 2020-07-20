#The 2 modules we need
import datetime
import pytz
# Shows us the options we have
for tz in pytz.all_timezones:
    print (tz)
#Takes in the place we want
local=input('Continent/Country from the above options? ')
#Takes current time from system
d = datetime.datetime.now()
#Accounts for time zones
timezone = pytz.timezone(local)
#Prints it out
d_aware = timezone.localize(d)
print(str(d_aware))
# Diala was here... :))
# Maya's here too 