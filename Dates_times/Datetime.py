# Dates and Time
"""
In Unix, the timestamp expresses the number of seconds since January 1, 1970, 00:00:00 (UTC).
"""
from datetime import date
from datetime import time
from datetime import datetime

today = date.today()

print("Today:", today)  # Today: 2021-05-23
print("Year:", today.year)  # Year: 2021
print("Month:", today.month)    # Month: 5
print("Day:", today.day)    # Day: 23

my_date = date(2021, 5, 4)
print(my_date)  # 2021-05-04

print("\nUsing ISO Format")
d = date.fromisoformat('2019-11-04')
print(d)

print("\nThe replace method")
d = date(1991, 2, 5)
print(d)    # 1991-02-05
d = d.replace(year=1992, month=1, day=16)
print(d)    # 1992-01-16

print("\nUsing weekday and isoweekday")
d = date(2019, 11, 4)
print(d.weekday())  # 0 From 0 to 6
d = date(2019, 11, 4)
print(d.isoweekday())   # 1 From 1 to 7

print("\nCreating datetime objects")
dt = datetime(2021, 5, 23, 20, 32)
print("Datetime:", dt)  # Datetime: 2021-05-23 20:32:00
print("Date:", dt.date())   # Date: 2021-05-23
print("Time:", dt.time())   # Time: 20:32:00
print("Timestamp:", dt.timestamp()) # Timestamp: 1621819920.0
print("today:", datetime.today())   # today: 2021-05-23 20:38:23.864465
print("now:", datetime.now())   # now: 2021-05-23 20:38:23.864465
print("utcnow:", datetime.utcnow()) # utcnow: 2021-05-24 01:38:23.864465

print("\nTime objects")
tm = time(14, 53, 20, 1)
print("Time:", tm)   # Time: 14:53:20.000001
print("Hour:", tm.hour)  # Hour: 14
print("Minute:", tm.minute)  # Minute: 53
print("Second:", tm.second)  # Second: 20
print("Microsecond:", tm.microsecond)    # Microsecond: 1

