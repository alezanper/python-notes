from datetime import date
from datetime import datetime
from datetime import timedelta

d1 = date(2021, 12, 14)
d2 = date(2020, 7, 23)
print(d1 - d2)  # 509 days, 0:00:00

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2)    # 365 days, 9:07:00

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)    # 16 days, 3:00:00

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)    # 16 days, 2:00:00

delta2 = delta * 2
print(delta2)   # 32 days, 4:00:00

d = date(2019, 10, 4) + delta2
print(d)    # 2019-11-05

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)   # 2019-11-05 18:53:00