# 2 modules that will provide the datetime and timezone
from datetime import datetime
import  pytz
# Format in which the time will be shown in
format = "%Y-%m-%d %H:%M:%S %Z%z"

# Shows all the timezones in the database
for tz in pytz.all_timezones:
    print (tz)

# Takes in the place we want
local=input('Continent/Country from the above options? ')

# Current time in UTC
now_utc = datetime.now(timezone('UTC'))

# Convert to time zone wanted
now_local = now_utc.astimezone(timezone(local))
print(now_local.strftime(format))

# This is the final project
