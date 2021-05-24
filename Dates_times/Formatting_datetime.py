# Date and time formatting (part 1)
from datetime import date
from datetime import time
from datetime import datetime

d = date(2021, 5, 23)
print("Date:", d.strftime('%Y/%m/%d'))  # Date: 2021/05/23

t = time(20, 46, 21)
print("Time:", t.strftime("%H:%M:%S"))  # Time: 20:46:21

dt = datetime(2020, 11, 4, 14, 53)
print("Full Date:", dt.strftime("%y/%B/%d %H:%M:%S"))    # Full Date: 20/November/04 14:53:00