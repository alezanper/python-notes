# The strftime() function in the time module
import time

timestamp = 1684979180
st = time.gmtime(timestamp)
print(time.strftime("%Y/%m/%d %H:%M:%S", st))   # 2023/05/25 01:46:20
print(time.strftime("%Y/%m/%d %H:%M:%S"))   # 2021/05/23 20:46:09
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))    # time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)
