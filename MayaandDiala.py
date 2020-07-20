import datetime,pytz
for tz in pytz.all_timezones:
    print (tz)

local=input('Continent/Country from the above options? ')
d = datetime.datetime.now()
timezone = pytz.timezone(local)
d_aware = timezone.localize(d)
print(str(d_aware))
