import calendar
print(calendar.calendar(2020))  # it prints a calendar
calendar.prcal(2020)

## Calendar November
print(calendar.month(2020, 11))
calendar.setfirstweekday(calendar.MONDAY)
calendar.prmonth(2020, 12)  # Calendary December starting on Monday
print(calendar.weekday(2020, 12, 24))   # Day of the week 0-6
print(calendar.weekheader(1))   # M T W T F S S
print(calendar.weekheader(3))   # Mon Tue Wed Thu Fri Sat Sun
print(calendar.isleap(2020))    # Año bisiesto
print(calendar.leapdays(2010, 2021))    # 3 dias bisiestos

# Creating a Calendar object
import calendar  
c = calendar.Calendar(calendar.SUNDAY)
for weekday in c.iterweekdays():
    print(weekday, end=" ")     # 6 0 1 2 3 4 5 

# The itermonthdates() method
import calendar  
c = calendar.Calendar()
for date in c.itermonthdates(2019, 11):
    print(date, end=" ")    # all days in the specified month and year are returned, as well as all days before the beginning of the month or the end of the month that are necessary to get a complete week.

# The monthdays2calendar() method
import calendar  
c = calendar.Calendar()
for data in c.monthdays2calendar(2020, 12):
    print(data)
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
# [(7, 0), (8, 1), (9, 2), (10, 3), (11, 4), (12, 5), (13, 6)]
# [(14, 0), (15, 1), (16, 2), (17, 3), (18, 4), (19, 5), (20, 6)]
# [(21, 0), (22, 1), (23, 2), (24, 3), (25, 4), (26, 5), (27, 6)]
# [(28, 0), (29, 1), (30, 2), (31, 3), (0, 4), (0, 5), (0, 6)]

# example
import calendar  
c = calendar.Calendar()
for weekday in c.iterweekdays():
    print(weekday, end=" ")     # 0 1 2 3 4 5 6
