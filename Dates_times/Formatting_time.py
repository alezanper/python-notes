# The strftime() function in the time module
import time

timestamp = 1684979180
st = time.gmtime(timestamp)
print(time.strftime("%Y/%m/%d %H:%M:%S", st))   # 2023/05/25 01:46:20
print(time.strftime("%Y/%m/%d %H:%M:%S"))   # 2021/05/23 20:46:09